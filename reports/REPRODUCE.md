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
