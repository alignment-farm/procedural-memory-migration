# Pilot v1 — prospective acquisition and migration gate

Recorded 2026-09-17 before workload model calls. The earlier READY endpoint check
used 17 prompt and 2 completion tokens (experimental setup; not acquisition).
No model has seen the workload at protocol creation. PM1–PM3 in README remain
unchanged. This is feasibility, not a confirmatory powered study.

## Scope and closest methods

CONTRAMEM 2608.22533v1 Methodology motivates typed procedural cards derived from
trajectories and unchanged task-relevant retrieval. We implement a small original
harness, not its multi-model construction or a replication. The factual migration
study 2609.05339v1 §§3.1–3.5 motivates fixed evidence, exact scoring and separate
calibration; procedural SQL decisions are our different target. Cached original
methods and the upstream reading ledger have a provenance manifest in sources/.
Published outcomes are author-reported and are not local evidence.

## Workload and persistence

Three synthetic SQLite query families: independent aggregates, temporal latest
state, NULL-safe exclusion with universal conditions. Each complete task requires
a reusable SQL query, scored on 12 independent databases, not just visible rows.
All obligations and schema semantics appear in each prompt. Identifiers, data,
and requested thresholds vary by task; the distribution and obligations do not
change when the recipient changes. This is a query-writing workload, not a broad
software-engineering benchmark. SQLite execution and public checking are available
identically to all arms, with at most four model actions per task. A submission
terminates the task; failure, exhaustion, malformed output, and transport failure
are retained. A check returns public expected and actual rows; hidden fixtures
are scored only at submission. No local or external agent tool access is used.

Source: served Qwen3.8 27B Q4_K_M, pinned Docker model digest. Recipient: a distinct
8B Qwen3 Q4_K_M model if the authorized Docker pull and serving probe succeed.
This is a cross-model migration, not necessarily an upgrade. No recipient history
is available when the bank is constructed. Only plain-text per-family cards
persist across fresh chat calls; no weights, adapters, or reusable KV state are
assumed. Backend caching is recorded where reported, not credited as learned
memory. Both models use the same JSON action protocol and temperature 0, with
thinking disabled if supported. Model fingerprints and all raw responses persist.

## Splits and decision sequence

1. Build six source experiences: two tasks/family, seeds 100–105, no memory.
2. Source model distills one card/family from the full corresponding source
   archive including task, actions, feedback and final verification. At most 700
   output tokens per card, no manually supplied solution. Freeze bank.
3. Paired source acquisition check: six fresh tasks, seeds 200–205, no-memory
   and unchanged relevant card. Alternate arm order deterministically.
4. Acquisition gate: at least two additional complete successes with no net
   quality loss, OR equal-or-better success with at least 15% fewer total model
   tokens. These are screening thresholds, not statistical significance.
5. If acquisition fails, diagnose ceiling, wrong guidance, protocol errors,
   budget truncation and weak verifier using preserved traces. Permit one clearly
   labeled development revision, frozen before fresh diagnostic tasks; do not
   reinterpret a failed acquisition as transfer failure. Close this phase on a
   demonstrated limitation if useful guidance remains unestablished.
6. Only after acquisition passes: recipient reconstructs per-family guidance
   from exactly the same source archive (not hidden evaluation answers).
   Compare no memory, unchanged and reconstruction on six calibration tasks,
   seeds 300–305. A paid deterministic rule selects the arm with most completed
   tasks per family; ties choose lowest total model tokens, then no-memory,
   unchanged, reconstruction. It implements retain/reconstruct/retire, not a
   post-hoc oracle. Adaptation here is reconstruction, not a cosmetic rewrite.
7. Freeze choices before 12 fresh evaluation tasks, seeds 400–411. Evaluate
   all three static arms and score the policy's selected arm; reuse identical
   selected-arm evaluation records rather than incur duplicate stochastic calls.
   Identity retrieval always falls back to the full relevant shared card.

## Costs, fairness and boundaries

Log every request, response, usage, elapsed wall time, test/check time, action,
error, and outcome. Report task failures and successes separately from costs.
Source construction, experimental search/diagnosis, reconstruction, calibration,
and downstream use are separate categories. Policy deployment pays for all
calibration arms plus reconstruction; static reconstruction pays its own build.
No inference about monetary savings, energy or GPU compute without telemetry.
Token totals across model tokenizers are not monetary equivalence. Report
break-even token projections only with quality caveats and observed per-task
means. Latency is descriptive only: no controlled hardware timing comparison.
Calls are serial and bounded; no shared hardware stress/timing benchmark.
Model download is setup/research overhead, not deployment inference.

Raw run files are never overwritten. Freeze code, task manifest, oracle tests,
and protocol in Git before execution. Hidden test material must never appear in
model prompts. All development outcomes remain visible; no final-outcome selection.
