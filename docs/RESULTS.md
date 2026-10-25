# RuxyScore V4.1 results

Measurements completed 22 October 2026. Primary setting: Ridge, full fit anchors and the corrected original ranking contract. Natural sentiment uses TRAIN256, five fixed training resamples and four equally weighted test corpora. Subject routing and entity endings retain their original single-head evidence.

## Native comparison

| Model | Subject | Sentiment | Entity endings | Native |
|---|---:|---:|---:|---:|
| Qwen3 8B BF16 | 81.07 | 68.02 | 89.84 | **77.60** |
| Qwen3 32B BF16 | 91.51 | 72.68 | 99.43 | **85.56** |
| Qwen2.5 72B INT8/BF16 | 92.00 | 77.31 | 100.00 | **87.72** |
| OLMo2 7B BF16 | 82.87 | 75.47 | 95.91 | **82.52** |

All values are q × 100 ranking points, with chance at zero and perfect ranking at 100. Native values use the same task contract. Family, generation and 72B precision differ; this is not a causal size comparison. Test intervals and per-task training spread are in [the recorded profiles](../results/benchmark-v4.1.json).

## Fixed-panel transfer into OLMo

Qwen3 8B BF16, Qwen3 32B BF16 and Qwen2.5 72B INT8/BF16 are equally weighted sources. Each task has its own registered bank, source heads and anchors.

| Task | Native | Incoming |
|---|---:|---:|
| Subject routing | 82.87 | 61.44 |
| Sentiment | 75.47 | 72.28 |
| Entity endings | 95.91 | 95.62 |
| Weighted basket | **82.52** | **72.61** |

The 50/50 summary is **77.57**, conditional test interval **75.06–81.34**. The largest gap remains in subject routing. Incoming averages source quality measurements; it does not combine sources into an ensemble alarm.

The [directed matrix](../results/transfer-matrix.csv) includes both recipes, half/full anchors and separate learned self-maps. Qwen targets use different leave-self-out pools. Their composite values are descriptive variants, not entries in a common-panel leaderboard. Qwen3 8B INT8 lacks natural sentiment and therefore has no complete total.

## Fixed operating point example

IMDb, Ridge, TRAIN256, seed17, the unchanged CAL threshold. Positive means a favorable overall review rating. N=512, 50% positive; sampling reserves 6.25% for reviews with predefined mixed-valence markers.

| Model | TP / FP / FN / TN | Detected / missed | Precision | FP / TP |
|---|---|---|---:|---:|
| Qwen3 8B BF16 | 146/12/110/244 | 57.0% / 43.0% | 92.4% | 0.082 |
| Qwen3 32B BF16 | 255/76/1/180 | 99.6% / 0.4% | 77.0% | 0.298 |
| Qwen2.5 72B INT8/BF16 | 256/119/0/137 | 100.0% / 0.0% | 68.3% | 0.465 |
| OLMo2 7B BF16 | 253/50/3/206 | 98.8% / 1.2% | 83.5% | 0.198 |

The recorded AUROC range is 0.940–0.966 and AP 0.932–0.954. Strong ranking and a useful fixed threshold are different measurements. No TEST recalibration was performed. Full operating counts and separate ranking inputs are in [recorded cells](../results/recorded-cells.json).

## Numerical correction and version comparison

V4.1 uses continuous binary decisions, stable relative multiclass Logistic scores and the original positive-L1 multiclass Ridge target. On identical controlled data, numerical correction changes eight Sentiment/Ridge q cells. Entity/Ridge q stays unchanged although some AUROC/AP values change. The separate V4.0 softmax link changes the meaning of multiclass Ridge and remains a historical sensitivity.

For OLMo, the old controlled basket remains 92.33 native / 83.70 incoming / 88.02 combined under numerical correction alone. Replacing template sentiment with natural V2 changes the mixed-basket result to 82.52 / 72.61 / 77.57. That change includes different texts, heads and training resamples; it is not the isolated effect of the numerical repair. [Recorded version comparison](../results/version-comparison.json) · [metric audit](../results/ranking-audit.json).

## What this supports

The harness produces comparable native profiles and an explicit incoming-transfer measurement under a declared source panel. It does not yet establish a general model ranking or a forecast for unseen safety tasks. The earlier negative six-task model-choice and label-target study remains unchanged.

The recorded V4.1 checks include independent numerical replay, preserved operating counts, actual CLI interruption/resume and cached OLMo onboarding. These are internal checks, not an external scientific reproduction. [Provenance](../results/provenance.json).
