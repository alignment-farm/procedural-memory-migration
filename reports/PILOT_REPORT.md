# Paid migration selection did not amortize over twelve SQL tasks

17 September 2026. Bounded pilot; original code and synthetic workload. No author
experiment was replicated, no external publication acceptance is claimed, and the
broader procedural-memory question remains open.

## Abstract

A strong unchanged bank resolved this bounded migration comparison. We acquired
procedural SQL guidance from six Qwen3.8 27B task attempts, preserved an initially
unsuccessful bank, and validated a compact revision on fresh tasks. The compact
bank preserved 6/6 source successes while reducing reported use tokens by 41.2%.
For a previously unseen Qwen3 8B recipient, unchanged inheritance solved 12/12
fresh tasks, versus 1/12 without memory and 10/12 after reconstruction from the
identical source archive. A rule selected using paid recipient calibration also
solved 12/12 and reduced use tokens by 17.3% relative to unchanged inheritance.
However, reconstruction and calibration raised its incremental total to 83,495
tokens, versus 28,153 for unchanged inheritance. Thus the policy did not repay its
cost over the observed twelve-task horizon. A token-only extrapolation crosses
at about 149 total tasks; that projection is unvalidated. The evidence concerns
three synthetic query templates, two pinned quantized models, and a bounded
non-thinking interaction budget, not general migration performance.

## Methods and provenance

The [prospective protocol](../protocols/pilot-v1.md),
[compact revision](../protocols/compact-revision.md), and
[final evaluation lock](../protocols/evaluation-lock.md) specify the sequence.
Protocol/code were frozen at `e100ccc` before source workload calls; bank-v2 at
`106c312` before its fresh acquisition screen; policy and final evaluation at
`092ae7d` before any final task. Every model request records its code revision.
The [development log](development-log.md) retains original failures and changes.

We inspected CONTRAMEM 2608.22533v1's trajectory-to-card method and the controlled
migration design in 2609.05339v1. These motivate a strong unchanged bank, common
source evidence, separate calibration and exact scoring. This is an original
small harness, not either paper's implementation. See the
[methods ledger](../sources/methods-inspected.md) and
[versioned source manifest](../sources/manifest.json). Published outcomes are
only author-reported. Existing arXiv query-API metadata was copied with upstream
Git provenance; this run issued no new metadata API/OAI requests.

Source is the model served as `docker.io/ai/qwen3.8:27b-q4_K_M`, Docker digest
`f04d0a543b64…`; recipient is `docker.io/ai/qwen3:8B-Q4_K_M`, digest
`79fa56c07429…`. Full local identities are in
[environment.json](../artifacts/environment.json) and
[recipient-model.json](../artifacts/recipient-model.json). Both use the same
Docker Model Runner endpoint, temperature zero, `enable_thinking=false`, and
1,400 output tokens per action. Serving establishes fixed-weight chat generation;
no gradient, adapter, or persistent KV-transfer capability is assumed. Upstream
training/version identity beyond the pinned local artifacts was not independently
validated.

Each task asks for a reusable SQLite query: independent one-to-many aggregates,
latest state with cutoff and tie-breaking, or NULL-safe universal qualification
and blocking. Every prompt contains its schema, obligations and public data.
The same optional `check` tool returns public actual/expected rows or SQL errors;
`submit` terminates the task. All arms have four actions including submission.
A complete success means the submitted query matches ordered reference rows on
all twelve hidden fixtures. Python computes expectations independently of the
model's SQL; SQLite executes the candidate. This is finite test-suite success,
not a proof for every legal database. The twelve fixtures are not twelve
independent model tasks.

The source archive contains all six tasks, actions, feedback and final checks,
including failure. The source model builds one plain-text card per family.
Retrieval uses the task family, with the relevant shared card offered even to a
recipient absent from construction labels. Memory is optional; ordinary tools
and feedback remain available. Only the cards persist across fresh chat requests.
There is no recipient evidence in source construction. Reconstruction receives
exactly the same archive, compact construction prompt and output cap; archive
hashes match. It is the recipient's own reconstruction, not a deliberately empty
or archive-deprived baseline, and not a claim about the best possible repair
system.

Source seeds 100–105 precede first acquisition seeds 200–205. The compact revision
uses fresh acquisition seeds 500–505. Recipient calibration uses 300–305;
evaluation uses untouched 400–411. The source then runs none/inherit on the same
final tasks, holding facts, obligations, tools, fixtures and inherited artifact
fixed across models. These controls were specified before final outcomes. A
pre-validation audit randomized account roles/IDs, varied eligibility patterns,
and explicitly declared generated event times/states NOT NULL. Original source
schemas and results remain at their original revision. This is documented
workload development; no later comparison mixes generator versions.

## Acquisition and preserved failure

| Screen | No-memory successes | Inherited successes | No-memory tokens | Inherited tokens |
|---|---:|---:|---:|---:|
| Original long bank, six paired tasks | 6/6 | 6/6 | 9,840 | 12,822 |
| Compact bank, six fresh paired tasks | 6/6 | 6/6 | 11,428 | 6,717 |

The original bank failed the prospective gate: no accuracy advantage, and 30.3%
more use tokens. It reduced temporal checking but imposed reading overhead;
its exclusion card hit the output cap in the final recap. This was diagnosed
as an acquisition/cost limitation, not failed transfer. The single allowed
revision asked for compact procedural cards and selective checking advice from
the same original archive. All revised cards finished normally. On fresh paired
tasks they passed the efficiency gate, reducing eleven actions to six while
preserving all successes. Different task seeds prevent a clean direct causal
comparison of the two bank versions; the within-screen controls establish the
reported comparisons. Compression and checking advice changed together.

## Fresh recipient comparison

The paid rule uses two calibration tasks per family. It chooses most successes,
then fewest total tokens, then the fixed none/inherit/reconstruct tie order.
Calibration scored 2/6, 6/6 and 5/6 respectively. Before evaluation, the rule
selected reconstruction for aggregate/exclusion and unchanged inheritance for
temporal tasks. It never selected on final outcomes. The policy uses the recorded
outcome of its selected arm on each fresh task, rather than a duplicate stochastic
run. This reuse was specified prospectively.

| Recipient alternative | Complete successes | Use tokens | Incremental migration setup | Setup + 12 uses |
|---|---:|---:|---:|---:|
| No inherited guidance | 1/12 | 49,590 | 0 | 49,590 |
| Unchanged relevant card | 12/12 | 28,153 | 0 | 28,153 |
| Recipient reconstruction | 10/12 | 23,925 | 11,086 | 35,011 |
| Paid family-wise policy | 12/12 | 23,281 | 60,214 | 83,495 |

Policy setup includes **all** reconstruction (11,086) and **all three** calibration
arms (49,128), including their failures and checks. It is not charged only for
its eventual winning calibration arms. Query checks are also included through
subsequent input and output tokens; checker CPU/wall time is separately recorded.
Source construction is sunk in this incremental migration table, not assumed
free; its full historical expense is reported below.

The policy saves 4,872 use tokens over unchanged inheritance on twelve tasks,
but its 60,214-token setup more than removes that saving. At the observed horizon
it costs 55,342 extra tokens, with no extra successes. The linear extrapolation
`60,214 / (4,872 / 12)` is 148.31 total uses (about 149), assuming the same future
mixture, mean use savings and quality. This is not a measured deployment result,
confidence bound, or monetary break-even. It also omits drift and policy refresh.
Without valuing failed tasks, a raw token projection against a lower-quality arm
is particularly uninformative; the same-quality unchanged arm is the main contrast.

Both reconstructed temporal failures (tasks 404 and 410) submitted a query with
an unadapted `events` table name after correcting only the parent table name.
They used two of four allowed actions; the cap alone does not explain these
failures. Although the reconstructed card retained source cutoff 5, these runs
correctly replaced it with the current cutoff. The observed fault was table-name
adaptation, not stale cutoff facts. This failure mode appeared in calibration
and recurred on fresh tasks. No-memory failures include multiplying joined sums,
excluding entities with no events, invalid column references, and replacing
universal conditions with existential ones. The feedback was present, often
repeatedly; its availability did not guarantee a successful correction.

## Matched source controls

| Model on identical final tasks | No-memory successes | Inherited successes | No-memory use tokens | Inherited use tokens |
|---|---:|---:|---:|---:|
| Source Qwen3.8 27B | 12/12 | 12/12 | 20,918 | 12,953 |
| Recipient Qwen3 8B | 1/12 | 12/12 | 49,590 | 28,153 |

The source saves 38.1% of use tokens and nine actions without changing observed
correctness. The recipient gains eleven complete successes and also uses fewer
tokens. The changed recipient therefore changes the observed marginal value of
the same guidance under matched facts. However, unchanged inheritance preserves
all final successes for both models: a loss of correctness or a family-level
need to retire it was not demonstrated. Some individual source aggregate tasks
incurred extra reading tokens without changing success. This qualifies PM1 rather than confirming every part of
its expectation. Cross-model transfer itself is already covered by the closest
public methods and is not claimed as this pilot's novelty.

The final family-level counts clarify the contrast. Source none/inherit is 4/4
in every family. Recipient none/inherit/reconstruct is 0/4, 4/4, 4/4 for aggregate;
1/4, 4/4, 2/4 for temporal; and 0/4, 4/4, 4/4 for exclusion. The paid policy's
calibrated temporal choice avoids the reconstruction failures, but unchanged
inheritance already avoids them without calibration.

## Costs and interpretation

Before recipient work, actual source acquisition/development spent **73,711
reported tokens**: source experience 9,126; original bank 12,561; failed-bank
screen 22,662; compact construction 11,217; compact screen 18,145. Those failed
and successful stages remain visible. A fixed compact build would use 20,343
source-experience/construction tokens before qualification; that figure is **not**
the historical development total. We do not silently grant a deployer foreknowledge
of the successful prompt or claim a from-scratch lifetime saving against a
no-memory alternative that could avoid bank construction altogether.

The complete harness ledger contains **216 model calls, 108 submitted task
attempts, and 269,509 reported tokens**, including both capability probes,
construction, unsuccessful development, calibration, all static evaluation arms,
and matched source controls. There were 89 successful and 19 failed task attempts;
no transport failures were observed. The first bank's one truncated card is
preserved. Aggregate model-request wall time is about 1,849 seconds; latency is
descriptive and includes differing model runtimes/cache/load behavior, not an
isolated hardware comparison. The original source probe's timing was transcribed
from its shell-tool result and is labeled separately in its record.

| Actual experiment phase | Reported tokens |
|---|---:|
| Both capability probes | 45 |
| Source experience | 9,126 |
| Original bank and failed acquisition screen | 35,223 |
| Compact bank and fresh acquisition screen | 29,362 |
| Recipient reconstruction | 11,086 |
| Recipient calibration, all arms | 49,128 |
| Recipient evaluation, all static arms | 101,668 |
| Matched source evaluation | 33,871 |
| **Total** | **269,509** |

The policy reuses selected evaluation outcomes, so it is not double-counted as
another set of inference calls in this experiment total. Research search and
control-evaluation costs differ from operational migration costs. Model download
(5.03 GB), investigator design/analysis, documentation searches, and local testing
are setup/research work; investigator model tokens, dollars, energy and hardware
compute are not measured. File parsing/retrieval and process orchestration are
not separately timed. The records include model wall time and all tool checker
time, but they do not justify a comprehensive money or compute claim. Token totals
across the two model tokenizers are an accounting ledger, not a currency.

The result supports explanatory progress on the bounded question: paid experience
can implement a useful family-specific choice, but a competent unchanged bank
can match its quality without the inspection bill. PM2's cost concern is observed
at the twelve-task horizon; longer-horizon advantage remains untested. The common
archive yields a serious reconstruction competitor (10/12), yet reconstruction
is neither uniformly reliable nor free. PM3's stronger counterfactual about
archive access is not directly tested: there is no archive-deprived reconstruction
arm. This pilot does not show that paid
selection is generally unnecessary or that recipient-specific adaptation can
never pay. All PM1–PM3 statements in the commissioning README remain unchanged.

Limits are substantial: three closely related synthetic templates; one model
pair and migration direction; tiny calibration samples; deterministic decoding
without repeated model samples; a non-thinking/four-action budget; exact family
retrieval; and finite generated fixture coverage. Baseline competence is scoped
to this implemented model/harness, not all possible prompting or agent scaffolds.
Cards largely contain SQL patterns, so applicability to long-horizon tool use or
other procedural domains is unknown. No significance claim treats fixtures or
same-template tasks as independent scientific replications. No model, policy or
bank was tuned on final outcomes.

## Evidence and reproduction

- [Aggregated raw-call and task accounting](results.json), [paid-policy accounting](policy-results.json), and [SHA-256 evidence manifest](../artifacts/evidence-manifest.json).
- [Source experiences](../runs/source-v1), [failed first bank](../runs/bank-v1), [compact bank](../runs/bank-v2), [recipient reconstruction](../runs/reconstruction-v2).
- [Calibration](../runs/calibration-v2), [frozen policy](../artifacts/policy-v2.json), [recipient evaluation](../runs/evaluation-recipient-v2), [matched source evaluation](../runs/evaluation-source-v2).
- [Reproduction commands](REPRODUCE.md), [offline audit](../scripts/audit.py), and [SQL replay](../scripts/replay.py).

[Unit/mutation tests](unit-tests.txt) pass. [Replay](replay.txt) reproduces all
108 submitted-query scores from the generator committed at each run's revision.
The [integrity audit](audit.txt) verifies pinned weight paths, identical source
archives, no held-out build tasks, policy identity/timestamp before evaluation,
and matched final task facts and inherited text across models.

A [supplemental temporal audit](temporal-stress.json) addresses a post-hoc coverage
concern: original event IDs were correlated with timestamps. It permutes IDs
independently and re-scores all twenty saved final temporal queries on twelve
new fixtures each. A correct reference query passes and a max-ID-only mutant
fails. All observed task success/failure labels remain unchanged. This is an
offline verifier stress check, not new model sampling, a replacement primary
score, or a dataset used for selection. Other untested legal database patterns
remain a limitation. The phase closes on the measured short-horizon cost result;
no further model work remains running.
