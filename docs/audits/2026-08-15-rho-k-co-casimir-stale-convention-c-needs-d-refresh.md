# `rho-k-co-casimir-extended` is stale on convention C, needs a D refresh (2026-08-15)

**Status: finding confirmed and root-caused; the D refresh could not be
completed in this sandbox (⁴He compute infeasible here) — deferred to a faster
environment.** Surfaced while draining the `raw-float64` ratchet
(PRs #5071/#5080). Every numeric claim below was measured, not assumed.

## The finding — a stale tr_M convention (verified)

[`computations/rho-k-co-casimir-extended.witness.json`](../../computations/rho-k-co-casimir-extended.witness.json)
was computed **2026-08-10** (`scriptCommitSha 90140791`) on the **convention-C**
tr_M table. On **2026-08-14** its inputs moved on — the producer + `y-lambda-wenzl`
(`820230f04d`) and, decisively, the tr_M `canonical-mass-table-extended`
(`1af7d4b7a0`), which rebuilt the table **C → D** (*"the corpus moved to D in
#4928"*). This is a genuine object change, not a relabel.

Verified by re-running the current producer against current-`main` inputs and
comparing to the C/D columns printed in `1af7d4b7a0`:

| atom | committed witness | `1af7d4b7a0` C | `1af7d4b7a0` D | fresh run |
|---|---|---|---|---|
| deuteron `|tr_M|` | 0.3883 | 0.3883 | 0.5751 | **0.5751** |
| tritium `|tr_M|` | 0.1041 | 0.1041 | 0.2293 | **0.2293** |
| deuteron ρ_K^pred | `9464.879…` | — | — | **`6390.441…`** |

So the committed witness carries **convention-C** tr_M; the current inputs are
**convention-D**; the fresh light-atom values land exactly on the D column. The
witness is also stale on `scriptHash` (`6b46797533d4` ≠ current producer).

## The raw-float64 RED is only the symptom

The ratchet flags `rho-k-co-casimir-extended` REGRESSED (3→4 raw float64): the
`per_atom[N].compute_wall_sec` wall-clock diagnostics. The current producer
already string-formats that field (`f"{t1-t0:.2f}"`, line 354), so the *float*
values in the committed witness are themselves a pre-08-14 artifact — further
evidence of staleness. A regeneration clears the RED, the stale physics, and the
`scriptHash` together; a surgical wall-time reformat would leave the physics and
hash stale, so it is the wrong fix.

## Why the refresh could not be completed here (measured)

The refresh is the correct §4 action, but the ⁴He compute is **infeasible in
this sandbox**:

- The χ^λ path is `chi_numeric` in `rho_k_h3a_refinement.py` — **pure mpmath**
  Hoefsmit matrices, parallelised over partitions with `multiprocessing.Pool`.
  There is **no `pyhecke-native` / native branch** to enable (an earlier guess
  that a missing Rust wheel was the cause was wrong).
- `gmpy2` was absent, so mpmath was on its pure-Python backend. Installing it
  restored the GMP backend (verified: `mpmath.libmp.BACKEND == 'gmpy'` in the
  main process **and** in the `Pool` workers). That fixed the small atoms
  (deuteron 0.2 s) — but was **necessary, not sufficient**.
- Even with `gmpy2`, tritium (n=9) ran **> 600 s** vs its recorded **9.28 s**
  (≥ 65× slower in this environment). ⁴He (n=12) has Hoefsmit matrices up to
  ~2640×2640 at 50 dps — recorded at **2533 s** on the origin machine; at this
  environment's factor it extrapolates to **tens of hours**. Not completable.

Pushing a partial or `--max-A 3` witness (dropping ⁴He) was rejected — it drops
data and still leaves stale physics.

## Corrections to earlier characterizations (this doc supersedes them)

- **Convention labels:** C is the stale one; **D** is the target (an earlier
  draft had them backwards, from parroting *"the shard was convention C"*).
- **Root cause of the slowness:** intrinsic mpmath Hoefsmit cost at n=12 (plus
  the missing `gmpy2`), **not** a missing `pyhecke-native` wheel.
- The characterizations in #5077 ("carry `mpmath.mpf`") and #5080 ("JSON cache
  round-trip", "compute_wall_sec timing leak") describe only the surface
  symptom; the real issue is the **stale convention**, and the float
  `compute_wall_sec` is a pre-fix producer artifact.

## Recommendation (for the owning session / a capable environment)

Re-run in the environment that produced the 2533 s ⁴He (the origin machine, or
any host where the mpmath Hoefsmit compute for n=12 is tractable):

```bash
python3 -u computations/rho_k_co_casimir_extended.py 2>&1 | tee /tmp/rhok.log
```

`--max-A 4` (default) regenerates the committed atom set on convention D. This
corrects the stale ρ_K values, refreshes `scriptHash`, and clears the ratchet
RED in one pass. The C → D move (`1af7d4b7a0` / #4928) should also trigger a
**sweep of every witness consuming `canonical-mass-table-extended` /
`y-lambda-wenzl`** — this was one consumer left on C; others may remain.
