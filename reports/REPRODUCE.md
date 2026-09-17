# Reproduction

Run from this repository; Python is managed with `uv`. No third-party Python
packages or author code are required. Model weights and Docker caches are not
versioned. All requests are serial; avoid overlapping inference on shared
hardware if conducting a timing study (this pilot makes no timing claim).

Offline checks:

```sh
uv run python -m unittest discover -s tests -v
uv run python scripts/replay.py
uv run python scripts/summarize.py
```

`replay.py` loads the generator from each outcome's Git revision, executes its
submitted SQL under a read-only SQLite connection and instruction limit, and
checks all saved verifier results. It makes no model calls. The original source
experience used `e100ccc`; strengthened later fixtures were committed in
`34800b7`. Do not re-score source-v1 with the later generator and call it a replay.

Live runs incur inference and may differ even at temperature zero. The precise
requested model, resolved model path, server fingerprint, prompts, usage,
provider timings and wall time are in each raw call JSON. The source Docker
digest is in artifacts/environment.json. Bank JSON contains a hash of the full
source archive supplied to its builder. Reconstruction must have the same hash.
Choose NEW run names: existing records refuse overwrite.

```sh
uv run python scripts/experiment.py batch --run source-new --start 100 --count 6
uv run python scripts/experiment.py build --run bank-new --source-run source-new
uv run python scripts/experiment.py batch --run acquisition-new --start 200 --count 6 --bank bank-new
```

The commands above use the current stronger generator. To reproduce the original
source distribution, use a separate checkout of `e100ccc` with new run directories.
A model replay cannot establish an exact replication of historical stochastic
responses. Historical outputs are already retained for deterministic analysis.

Do not start a migration analysis unless the acquisition gate in
protocols/pilot-v1.md passes, or a documented fresh development revision passes.
The script migration.py implements calibration comparisons and the fixed
family-wise selection rule. Freeze policy artifacts before evaluation; include
all reconstruction and calibration requests in policy deployment cost. Failed
requests without usage have unknown cost, not a claimed free attempt.

Source refresh is optional. `scripts/cache_sources.py` fetches versioned paper
HTML and copies the upstream ledger; it makes no arXiv metadata API requests.
The committed copies and hashes suffice for offline reading. No credential,
model weight, environment or general-purpose cache is part of the evidence.

Apply the preregistered screen after the full six paired tasks:

```sh
uv run python scripts/acquisition_gate.py acquisition-new --output acquisition-new-gate.json
```

The executed compact revision and recipient phase used:

```sh
uv run python scripts/experiment.py build --run bank-v2-new --source-run source-new --style compact
uv run python scripts/experiment.py batch --run acquisition-v2-new --start 500 --count 6 --bank bank-v2-new
uv run python scripts/experiment.py build --run reconstruction-v2-new --source-run source-new --style compact --model docker.io/ai/qwen3:8B-Q4_K_M
uv run python scripts/migration.py compare --run calibration-v2-new --model docker.io/ai/qwen3:8B-Q4_K_M --start 300 --count 6 --inherit bank-v2-new --reconstruct reconstruction-v2-new
uv run python scripts/migration.py select --run calibration-v2-new --output policy-v2-new.json
```

Commit and lock that policy before fresh evaluation. The final recipient run uses
`migration.py compare` with start 400, count 12, and the frozen banks. Matched
source controls use `experiment.py batch` with start 400, count 12 and the same
inherited bank. Repeat studies should use genuinely new task seeds and preserve
the original seed-to-family mapping; reusing historical held-out seeds is a
reproduction, not fresh confirmation.

Completed-run accounting and integrity checks:

```sh
uv run python scripts/policy_report.py --evaluation evaluation-recipient-v2 --policy policy-v2.json --reconstruction reconstruction-v2
uv run python scripts/audit.py
uv run python scripts/stress_temporal.py
```

`audit.py` targets this historical pilot's explicit revisions/run names.
`stress_temporal.py` is a post-hoc offline verifier audit: it permutes event IDs
independently of time, checks the saved temporal SQL, and leaves primary scores
unchanged. It does not invoke a model. Its reference query passes and a max-ID-only
mutant fails, establishing sensitivity to the intended coverage gap.
