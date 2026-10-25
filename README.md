![RuxyScore](assets/ruxyscore-logo.png)

**How easily can we read this model?**

RuxyScore benchmarks how well probes can be trained on language models and transferred between them.

It grew out of [RuxyTrace](https://github.com/pioborgelt/llm-oscilloscope) and the question of how much understanding one model can help us understand another.

## How it works

1. Give each model the same task examples.
2. Train probes directly on its activations. Select layers and regularization on a separate selection split.
3. Transfer existing probes into it through adapters trained on paired, unlabeled activations.
4. Compare the native and transferred readouts.

## What we have so far

V4.1 covers subject routing, sentiment and entity endings, weighted 40/40/20. Native Ridge results are shown below in ranking points.

| Model | Subject | Sentiment | Entity endings | Native |
|---|---:|---:|---:|---:|
| Qwen3 8B BF16 | 81.07 | 68.02 | 89.84 | **77.60** |
| Qwen3 32B BF16 | 91.51 | 72.68 | 99.43 | **85.56** |
| Qwen2.5 72B INT8/BF16 | 92.00 | 77.31 | 100.00 | **87.72** |
| OLMo2 7B BF16 | 82.87 | 75.47 | 95.91 | **82.52** |

[Full results and uncertainty](docs/RESULTS.md)

For OLMo2 7B, probes transferred from the fixed Qwen 8B/32B/72B panel reach 72.61 points, compared with 82.52 natively. The 50/50 summary is **77.57**, with a conditional test interval of 75.06–81.34. You can still inspect both sides and each individual task.

Only OLMo uses the full reference panel. The Qwen models have different source pools because self-transfer is excluded, so their incoming averages don't form a shared leaderboard.

## Take a look

Start with the [results](docs/RESULTS.md) for task profiles and transfer comparisons. The recorded numbers are also available as [JSON](results/benchmark-v4.1.json), [native profiles](results/native-profiles.csv) and a [transfer matrix](results/transfer-matrix.csv).

To check the snapshot locally, run:

```bash
python3 scripts/verify_snapshot.py
```

You don't need your GPU to inspect the results. The research runner and the automatic onboarding are private for now, but will come soon.

## Still early

The old sentiment task gave every model 100 native points, and that's a fairly boring benchmark. V4.1 uses natural reviews instead and fixes ranking information lost through clipped readout values. [What changed](docs/CHANGELOG.md).

Subject routing and entity endings still use controlled texts, and the reference panel is entirely Qwen. All current test banks have already been opened during development. This is a research prototype, with a limited task set.

Whether these profiles predict how well an unseen safety probe will work is still unproven, and we need more good probes in the inventory to optimise this benchmark.

I'm working hard to add more models, more reliable probes and better controls. This is still early, so expect quite a bit to change! :)
## Documentation

| Document | Contents |
|---|---|
| [Method](docs/METHODS.md) | How the probes, adapters and score work |
| [Results](docs/RESULTS.md) | Profiles, transfer comparisons and alarm behavior |
| [Limits](docs/LIMITATIONS.md) | What these results can and can't tell us |
| [Data and artifacts](docs/DATA_AND_ARTIFACTS.md) | Where the data comes from and what's included |
| [Version history](docs/CHANGELOG.md) | Corrections and earlier measurements |
| [Related work](docs/RELATED_WORK.md) | The research this builds on |

## Feedback

If you work on probes, what would you want this benchmark to test next? A useful task, a failure case or a criticism of the setup would all really help.

[Pio Borgelt](mailto:pio@ruxytrace.com)/[RuxyTrace](https://ruxytrace.com/)
