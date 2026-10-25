# Measurement version history

## V4.1 current

Measurements completed 22 October 2026; local documentation updated 23 October. Canonical version `mixed-bank-corrected-original-4.1`, view `mixed-original-contract`.

The active basket combines original controlled subject/entity tasks with natural sentiment V2. Weights remain 40/40/20; the experimental native/incoming summary remains 50/50. Sentiment now uses four test corpora and five fixed training resamples. Source panels, model precision and missing-task rules are explicit.

Binary ranking uses continuous decisions before clipping/sigmoid. Multiclass Logistic preserves its relative probability target. Multiclass Ridge preserves the original positive-L1 link. All stored probabilities, CAL thresholds and operating decisions remain unchanged.

The canonical choice was documented after the opened V4.0 audit and before deriving V4.1 totals. It is a development amendment, not a retroactive preregistration. Existing captures, heads, maps, negative results and V4.0 outputs were preserved.

## V4.0 sensitivity

The first consolidated V4.0 run used a relative-softmax link for multiclass Ridge. That changes the measurement target, not just its numerical representation: 160/162 controlled subject/Ridge q cells changed. It remains a separate sensitivity in the private package and recorded version comparison. It is not the current default.

## Original controlled pilot

The 20 October pilot used controlled sentiment templates. OLMo scored 92.33 native / 83.70 incoming / 88.02 combined. Applying the numerical repair alone to those same artifacts leaves that OLMo aggregate unchanged. Natural sentiment replaces the bank and its heads/resamples, so the V4.1 value of 82.52 / 72.61 / 77.57 is not a pure numerical-correction delta.

The old native-perfect sentiment result therefore remains historical evidence of an easy test. It is not overwritten or presented as the current task. Original exports are under [the dated result history](../results/history/2026-10-20/fixed-panel-olmo.json); the previous full documentation snapshot is archived privately.

## Interpreting the audit

Eight controlled Sentiment/Ridge q cells change under numerical correction. The real 72B self-map OOD cell goes from 17.1875/14.0625 points with half/full anchors to 100 using the same raw decisions. These are per-domain cells; historical domain-averaged values were 58.59375/57.03125. Direct identity is a separate check.

Entity/Ridge q remains unchanged while 19 class/cell AUROC and AP values change slightly. Equal low-FPR q does not imply identical full ranking. [Machine-readable audit](../results/ranking-audit.json).
