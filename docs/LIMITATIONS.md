# Current limits

RuxyScore V4.1 measures three specific probe tasks under declared fitting and alignment recipes. Subject routing and entity endings use controlled, self-authored references; sentiment uses natural review ratings. The current basket does not measure deception, reward hacking, general honesty or whether a model can evade a monitor.

## Breadth and comparison

The common reference panel contains only Qwen models. Only OLMo is evaluated against that full panel. Qwen targets use different leave-self-out sources, so their incoming averages and 50/50 summaries cannot be read as a common leaderboard. Qwen3 8B INT8 lacks natural sentiment and remains incomplete.

Size, family, generation and precision are mixed. A smaller model scoring near a larger one is a descriptive finding, not evidence that size has no effect. A transfer gap can come from the source head, chosen layers, anchor coverage, affine-map capacity or target representation; the score does not separate these causes.

## Data

Controlled references share construction patterns and are narrower than natural monitoring tasks. Sentiment ratings are proxies for overall text sentiment. Ambiguous/neutral ratings are excluded under preparation rules; they are not a new human-gold labeling study. A 6.25% marker quota changes the sample mix, and 50% positive prevalence is an evaluation choice. Unknown pretraining overlap remains possible. Amazon products/authors and IMDb films are grouped; IMDb author IDs are unavailable.

All current banks are already opened. The new composite is a development reanalysis of existing captures and fits, not a fresh independent model/corpus confirmation. V4.1 preserves the original multiclass Ridge target following the opened V4.0 audit; that chronology is recorded in the version history.

## Ranking and calibration

The index summarizes continuous low-FPR ranking. The frozen CAL threshold can behave differently under domain shift. On IMDb, OLMo's native Ridge/seed17 head detects 253 of 256 positive reviews and misses 3, but also flags 50 negative reviews: TP/FP/FN/TN=253/50/3/206, 83.5% precision and 0.198 FP/TP at 50% positive prevalence. No TEST recalibration is hidden behind the ranking correction. [Full operating comparison](RESULTS.md).

The conditional bootstrap intervals hold all fitted choices fixed. They do not establish training robustness across the whole basket or confidence over the population of models. Single-head controlled tasks and five-resample sentiment provide different amounts of training evidence.

## Predictive usefulness

An earlier study on six new monitoring tasks did not improve model choice or label-target prediction in its main comparison. V4.1 does not replace that negative result. Predicting performance on unseen safety tasks, choosing a better deployment model and saving new human annotations remain unconfirmed.

The useful demonstrated output is an inspectable native/transfer profile under a fixed contract. External scientific reproduction and a new target under the full V4.1 mixed bank remain future checks.
