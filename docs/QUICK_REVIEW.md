# RuxyScore technical review

RuxyScore benchmarks how readily a fixed set of properties can be read with linear probes, and how well reference probes work after activation alignment into a target model.

V4.1 includes controlled subject routing, natural sentiment and controlled entity endings. Four models have complete native profiles. OLMo2 7B is the target with a common Qwen8B/32B/72B reference panel: 82.52 native and 72.61 incoming ranking points. The largest gap is in subject routing. [Results](RESULTS.md).

The protocol fixes data roles, native SELECT-based layer/regularization choice, unlabeled alignment anchors, source-head identities and task weights. Missing required tasks give no total. Its numerical audit preserves the original multiclass target and alarm decisions. [Method](METHODS.md).

The current panel is Qwen-only and two tasks remain constructed. Earlier tests did not establish improved model choice or label-target prediction on new monitoring tasks. The mixed-bank score remains a development benchmark, with conditional test uncertainty and separate sentiment training spread.

Useful review questions:

- Which additional task would be the most convincing test of the benchmark's value?
- What should a reference panel cover before comparisons between new models become informative?
- Would the task profile, transfer matrix or native learning curve be most useful in your own probe work?

[Recorded exports](../results/benchmark-v4.1.json) · [Contact Pio](mailto:pio@ruxytrace.com)
