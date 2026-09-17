# Methods used in this pilot

Inspected on 2026-09-17, before workload execution. Exact HTML files are cached
with SHA-256 in manifest.json; arXiv metadata is copied from the upstream query
API cache with provenance. No new metadata API/OAI requests were issued here.
The broader source ledger is a copied prior inspection, not a claim that every
paper was reread in this session.

- CONTRAMEM, [2608.22533v1](https://arxiv.org/html/2608.22533v1), Methodology,
  Problem Setup / Trajectory normalization: preserve task attempts and outcomes,
  form reusable procedural cards, and retrieve relevant unchanged cards for an
  unseen recipient. Our pilot borrows that experimental structure, not its
  multi-model contrastive construction, benchmarks or author implementation.
- Does Your Agent's Memory Survive a Model Upgrade?,
  [2609.05339v1](https://arxiv.org/html/2609.05339v1), §§3.1–3.5: controlled exact
  scoring, distinct calibration and evaluation, and an analysis lock. Our
  recipient comparison concerns query procedures rather than factual stores.

All paper performance claims remain author-reported. No author model runs or
code have been replicated. The present code and synthetic data are original.
Inference to test: paid recipient calibration might choose useful guidance;
unchanged memory, reconstruction or retirement can each be the right choice.

The [official Codex non-interactive documentation](https://learn.chatgpt.com/docs/non-interactive-mode)
and local CLI 0.154.0 help were inspected as a possible batch interface using
the OpenAI Docs skill. No Codex experimental model call was made; direct Docker
Model Runner calls keep the source/recipient harness consistent instead.
