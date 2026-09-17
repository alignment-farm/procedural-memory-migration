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
