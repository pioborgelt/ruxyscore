# RuxyScore method
The RuxyScore benchmarks how easily we can read internal signals from a specific language model. For this, it tests several tasks under the same protocol, measures how well probes can be trained directly on the model, and checks how much can be reused from a set of reference models.


The pipeline selects layers, trains probes, fits transfer adapters and evaluates the results automatically.
The results include task profiles, native and transfer scores, and a combined RuxyScore. These show how easy it is to read certain signals inside the models. With a broader set of tasks and models, the goal is to test whether these profiles help predict how well new monitoring probes will work.

## Tasks and activations

| Task | Data and label | Where activations are read | Weight |
|---|---|---|---:|
| Subject routing | Constructed texts, eight subject labels | Last prompt token, using the model's chat format | 0.40 |
| Sentiment | Natural Amazon/IMDb reviews, labeled by their original ratings | Mean block output across review tokens, excluding padding. No chat template | 0.40 |
| Entity endings | Constructed sentences, labeled at entity endings | Last token in the text up to each tested word | 0.20 |

Read block outputs at 25%, 50%, 75%, 90% and 100% of the model's depth, before final normalization. I know we need more tasks here - if you have some high quality probes please reach out!

## Data and splits

| Task | TRAIN | SELECT | CAL | Fit / selection anchors | TEST |
|---|---|---:|---:|---|---|
| Subject routing | 256 texts | 128 | 128 | 128 / 128 | 128 texts per controlled domain |
| Sentiment | 256 reviews per fit from a 512-review pool | 128 | 128 | 256 / 128 | 1,536 reviews across four corpora |
| Entity endings | 64 sentence groups | 64 | 64 | 32 / 32 | 64 sentence groups each for ID and OOD |

[Exact counts](../configs/bank-description.json)

Sentiment has 2,752 reviews, including 64 development reviews. All splits except TEST use Amazon Beauty and Musical Instruments. TEST uses Beauty (256), Musical Instruments (256), Fashion (512) and IMDb (512). Each test corpus is 50% positive. Sampling reserves 6.25% for reviews with predefined mixed-sentiment markers. Original ratings provide the labels, without new human annotation.

## Native probes and transfer

### Training a native probe

Native probes use Ridge regression (L2 regularization) with one-hot class labels. Activations use TRAIN-only centering and a single shared scale, applied unchanged to SELECT, CAL and TEST.

SELECT log loss chooses the layer and λ from `{0.001, 0.01, 0.1, 1.0}`. CAL sets the alarm threshold. TEST evaluates the selected probe without further tuning.

Subject and entity probes are fitted once. Sentiment uses five fixed TRAIN samples, with 512 labels per fit including SELECT and CAL.

### Transferring an existing probe

An affine Ridge adapter maps target activations into the source probe's input space. The source probe and layer stay fixed. Fit anchors are unlabeled and paired by semantic ID.

Separate unlabeled selection anchors choose the target layer and λ by relative feature MSE. The λ grid matches native fitting. Task labels are not used.

Sentiment uses matched V2 probes and 256 fit / 128 selection anchor groups, or 128 / 128 in the half-anchor check. Other tasks use the counts above. Logistic regression probes are a separate check.

Target-CAL fits the alarm threshold on target CAL labels. Source-Cut retains the source threshold. Neither changes the ranking scores.

Controls include learned self-maps and unchanged probe/feature identity. Self-maps are excluded from incoming sources.

## Ranking inputs

| Probe | Value used for ranking |
|---|---|
| Binary Ridge | Raw linear output for the positive class, without clipping |
| Binary Logistic | Positive-class logit before sigmoid |
| Multiclass Logistic | Class-versus-rest log-odds from softmax |
| Multiclass Ridge | Class-versus-rest log-odds after flooring and L1 normalization |

Multiclass Ridge uses positive-L1 normalization with a floor of `1e-6`. Compute the equivalent class-versus-rest log-odds for stable ranking

```text
log(max(z_class, 1e-6)) - logsumexp(log(max(z_other_classes, 1e-6)))
```

Floor ties, original probabilities and CAL decisions (`score >= threshold`) stay unchanged. The V4.0 softmax variant is reported separately. [Changes and numerical checks](CHANGELOG.md).

## Score

Let `A` be partial ROC area over FPR 0–0.05, using trapezoidal integration and boundary interpolation. Score each binary task or one-vs-rest class with `alpha = 0.05`

```text
q = (A - alpha² / 2) / (alpha - alpha² / 2)
points = 100 × q
```

Chance is zero and perfect ranking is 100.

For subject routing, average classes and both test domains equally. For entity endings, average both domains. For sentiment, average four corpora and five training samples. Apply the task weights

```text
native   = Σ_task weight_task × native_task
incoming = Σ_task weight_task × mean_source(transfer_source,task)
score    = 0.5 × native + 0.5 × incoming
```

Sources have equal weight. Missing required tasks or sources produce `null`, without renormalizing.

OLMo's sources are Qwen3 8B, Qwen3 32B and Qwen2.5 72B. Qwen targets exclude themselves. Their incoming scores use different source sets, so they do not form a common-panel ranking. [Source probe versions](../configs/reference-panel-summary.json).
