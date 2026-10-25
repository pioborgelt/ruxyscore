# Related work

RuxyScore combines existing probe-fitting and activation-alignment ideas into a versioned comparative measurement. Probe transfer itself is established prior work.

## Model stitching

Chen, Merullo, Stolfo and Pavlick, **Transferring Linear Features Across Language Models With Model Stitching**, NeurIPS 2025, learn affine maps between residual streams. They transfer SAEs, probes and steering vectors across differently sized models. Their dense-probe experiment includes Pythia 70M→160M; further feature and steering experiments include Gemma 2B↔9B. [Paper](https://papers.neurips.cc/paper_files/paper/2025/file/4569a868e7aa891248832ec08445d071-Paper-Conference.pdf)

## Probe-visible alignment

Lee and Kondor, **Deep Minds and Shallow Probes**, May 2026 preprint, study coordinate-stable probe families and transfer through a probe-visible quotient. Their empirical monitor transfer includes Qwen7B→Qwen3B/14B and Mistral7B, with layer-pair and alignment-budget analyses. This is relevant both as a comparison method and as a warning that reconstructing the whole state is not the only transfer strategy. [Paper](https://arxiv.org/html/2605.11448)

## Learned layer correspondence

Sudakov, Bar-Shalom, Frasca and Maron, **Learning Cross-Model Activation Alignments with Explicit Many-to-Many Layer Maps**, 6 October 2026 preprint, introduce MATCHA. They study 42 directed pairs across seven 1–8B models and three families, with downstream probe and steering transfer. Their size-group categories follow model depth. RuxyScore currently selects among individual target layers and uses an affine map; it does not implement MATCHA. [Paper](https://arxiv.org/html/2610.09058)

## Monitoring and benchmark scope

Obeso et al., **Real-Time Detection of Hallucinated Entities in Long-Form Generation**, study hallucination detectors and cross-model generalization. Their cross-model experiments include using a detector model to read another model's generated text and reusing annotated generations for training. Those settings should not be conflated with transporting a frozen head into another model's activation space. [Paper, section 5.2](https://arxiv.org/html/2509.03531#S5.SS2)

[ProbeBench](https://openinterp.org/probebench/about) evaluates probes, including their transfer properties. RuxyScore's intended unit of comparison is the receiving model under a fixed task and source protocol.

## Questions this prototype can explore

The existing matrix can expose direction-specific transfer gaps and reference-pool sensitivity under one declared budget. A broader study could test how source-panel design affects model comparisons, how those effects change with scale and family, and whether the conclusions survive alternative alignment methods.

Primary papers were inspected on 20 October 2026.