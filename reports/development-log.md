# Development record

- Initial repository `f7ca4fc`; instructions and README read before execution.
- Closest public methods inspected and cached; upstream evidence copied from
  Construct-2 `52f8eaac42fdfc9ef7333c584bea21a25b40e7ac`. No root or sibling edits.
- Docker inventory exposed Qwen3.8 27B Q4_K_M, digest in environment.json.
  One live READY smoke call succeeded (19 tokens). Serving establishes fixed
  chat generation only; no gradient, adapter or KV-transfer capability claimed.
- Codex CLI and official batch docs inspected as fallback; no Codex model call.
  A 5.03 GB Qwen3 8B Q4_K_M download was started using `docker model pull` within
  the supplied resources to allow the same direct-chat harness for both models.
- Original prospective protocol, workload and oracle mutation tests committed
  as `e100ccc` before source workload calls. Six source tasks were then run
  serially with no memory and ordinary checking available.
- After two source outcomes, code audit found fixed account roles/IDs in hidden
  fixtures. A pre-validation amendment randomizes IDs and varies some empty,
  temporal and disqualification cases. Original running source process and
  outcomes retained unchanged; stronger fixtures frozen as `34800b7`.
- Source outcomes: aggregate-100 failed (join multiplication); all five other
  tasks passed. Four tasks used the checker; both aggregate tasks submitted
  directly, one incorrectly and one correctly. Source work: 10 calls, 9,126
  total reported tokens. Failures are included.
- Card construction uses the full per-family source archive, including final
  expected/actual rows, under a 700 output-token cap. No expert SQL solution is
  inserted. The first card correctly identifies multiplication and independent
  aggregation; that inspection does not establish a performance benefit.

Experimental search includes this agent's workload design, code construction,
methods reading, download, tests and analysis. The API ledger quantifies model
requests made by the experiment harness, not all investigator effort. Investigator
model tokens, energy and hardware compute are unavailable here; do not describe
this as a full dollar/energy cost account. Deployment comparisons must include
all measured source construction, migration calibration/reconstruction and use
costs, while reporting unmeasured quantities as unknown.
- First acquisition screen (`acquisition-v1`): 6/6 correct in each arm. Inherited
  guidance cost 12,822 tokens versus 9,840 without memory (+30.3%), despite two
  fewer model actions. Bank-v1 cost 12,561 tokens, with the exclusion card reaching
  its 700-token cap in the concluding recap. Recorded gate failed, and the
  originally allowed single revision was frozen in protocols/compact-revision.md.
- Qwen3 8B download completed, 5.03 GB transferred; both model IDs are now
  advertised by the same endpoint. Recipient digest/quantization are retained in
  artifacts/recipient-model.json. No recipient inference has yet occurred at
  the compact revision's lock. Its use depends on the acquisition gate.
- Compact bank-v2 finished without truncation: cards of 106, 121 and 170 output
  tokens; build cost 11,217 total tokens. Its archive hash matches bank-v1.
- Fresh compact acquisition (`acquisition-v2`, seeds 500–505): both arms 6/6,
  inheritance 6,717 tokens versus no-memory 11,428 (-41.2%). Memory used six
  actions versus eleven without memory. The prespecified efficiency gate passes.
  This supports useful source guidance within this workload, not a broad accuracy
  gain or a direct causal comparison with bank-v1 on different tasks.
- Proceed to previously unseen Qwen3 8B with unchanged compact bank and same
  current workload/tool harness. Recipient reconstruction uses source-v1 and the
  identical compact construction prompt. Calibration remains seeds 300–305;
  evaluation remains untouched seeds 400–411.
- Recipient JSON capability probe succeeded (26 tokens). Reconstruction-v2 used
  the identical archive and compact prompt, completed without truncation, and
  retained a literal temporal cutoff. In calibration it correctly changed that
  cutoff when needed; the observed failure was an unadapted event table name.
- Calibration: none 2/6, inherit 6/6, reconstruct 5/6. The deterministic rule
  selected reconstruct for aggregate/exclusion and inherit for temporal. Policy
  and evaluation protocol are locked before seed 400–411 runs. Added paired
  source-model none/inherit controls on the same final tasks to identify a model
  change with facts held fixed. No final outcomes inform the addition or choices.
- Final recipient evaluation: none 1/12, inherit 12/12, reconstruct 10/12;
  frozen policy 12/12. Policy use 23,281 tokens versus unchanged 28,153, but
  all calibration/reconstruction raises policy total to 83,495. No final tuning.
- Matched final source controls: both arms 12/12; none 20,918 use tokens,
  inherit 12,953. Same task facts and inherited card are audited across models.
- Offline verification: all 108 saved submissions replay exactly; pinned model
  paths, shared archive hashes and pre-evaluation policy lock pass integrity
  checks. A post-hoc temporal verifier audit shuffles event IDs independently of
  time, catches a max-ID-only mutant, and leaves all twenty final temporal task
  success labels unchanged. This is supplementary grader diagnosis, not model
  search or a replacement primary endpoint.
- Bounded phase closed with explanatory progress: unchanged inheritance matches
  the paid policy's quality at lower total token cost over twelve uses. Full
  harness ledger: 216 calls, 269,509 reported tokens, 108 complete submitted
  attempts (89 successes, 19 failures). No broader closure or publication
  acceptance is claimed; no model runs remain active.
