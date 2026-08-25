# `rho-k-co-casimir-extended` is stale on convention C, needs a D refresh (2026-08-15)

**Status: DONE (2026-08-16). The refresh ran; the witness is uniformly
convention D.** The original status — *"could not be completed in this sandbox
(⁴He compute infeasible here) — deferred to a faster environment"* — stood on a
misdiagnosed blocker. See §"The blocker was memory, not time" below; the
finding and root cause in the rest of this document were correct and are
unchanged.

Result of the refresh (`--max-A 4 --workers 1`, this same class of sandbox):

| atom | `\|tr_M\|` C → D | ρ_K^pred C → D | err vs CODATA |
|---|---|---|---|
| deuteron | 0.38829 → **0.57509** | 9464.879 → **6390.441** | 67.5614 → 67.5677 ppm |
| tritium | 0.10407 → **0.22931** | 52978.840 → **24044.137** | 8.0768 → 8.0775 ppm |
| helium-3 | 0.20658 → **0.40377** | 26677.801 → **13649.103** | 12.7705 → 12.7716 ppm |
| helium-4 | 0.05536 → **0.16097** | 132765.417 → **45657.533** | 1.61857 → 1.61871 ppm |

The deuteron and tritium `|tr_M|` land exactly on the D column tabulated
above, as predicted. Note `err_ppm` barely moves at any atom while ρ_K moves by
factors of 1.5–2.9: `M_pred = ρ·m_e·|tr_M|`, and the two factors move
reciprocally. The refresh clears the `raw-float64` RED (the witness now carries
**0** raw floats; `REGRESSED` is 0 corpus-wide), the stale convention, and the
stale `scriptHash` together — as this document said it would.

## The blocker was memory, not time

The original deferral rested on a wall-clock extrapolation: tritium ran > 600 s
against its recorded 9.28 s, so ⁴He at ~2533 s was projected to "tens of hours".
That measurement was taken **before `gmpy2` was installed**, and the conclusion
did not survive installing it. Measured on 2026-08-16 with `gmpy2 2.3.1`
(`mpmath.libmp.BACKEND == 'gmpy'`), 4 cores:

| atom | recorded (origin machine) | this run |
|---|---|---|
| deuteron | 0.34 s | **0.08 s** |
| tritium | 9.28 s | **0.48 s** |
| helium-3 | 9.45 s | **0.19 s** |
| helium-4 | 2533 s | **734 s** (single worker) |

Every atom is *faster* here than on the origin machine — ⁴He by 3.5×, and on
one worker. There was never a tens-of-hours run to wait out.

What actually stopped ⁴He is the producer's own memory guard, which says so:

```
SKIP helium-4: needs ~14.8GiB for the largest λ (dim 7700), 14.9GiB available
              — pass --workers N to force
PRESERVING committed helium-4: this run returned skip_insufficient_memory,
              keeping the stored result
```

14.8 GiB wanted against 14.9 GiB free is a margin the guard declines, so it
skipped ⁴He and — correctly — preserved the committed entry rather than writing
a stub. `--workers 1` drops the per-worker requirement and it completes in 734 s
with ~1 GiB resident.

**A partial run is worse than none here, and silently so.** With ⁴He preserved
and the light atoms refreshed, the on-disk witness is *mixed-convention* — three
atoms D, one C — which is harder to detect than uniform staleness and violates
the standing "never straddle two layers inside one quantity" rule. The tell is
`compute_wall_sec`: computed atoms carry a string (`f"{t1-t0:.2f}"`), a
preserved one carries the old float. If that field is a float for some atom and
a string for others, the witness is mixed — do not commit it.

Both corrections were found by re-running, not by re-reading: the first
`--max-A 4` attempt here reproduced the deferral exactly, and the guard message
in its log is what redirected the diagnosis from time to memory.

---

*Original status line, retained for the record:* "finding confirmed and
root-caused; the D refresh could not be completed in this sandbox (⁴He compute
infeasible here) — deferred to a faster environment." Surfaced while draining
the `raw-float64` ratchet (PRs #5071/#5080). Every numeric claim below was
measured, not assumed.

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

## This is a known, tooled migration — use the canonical regenerator

The C → D staleness is **already tracked and tooled**, not a novel finding:

- `scripts/convention-c-producer-audit.py` — confirms the *producers* are all
  convention D (0 actionable sites); only their committed *witnesses* lag.
- `scripts/regenerate-convention-c-witnesses.py` (`--plan` / `--run` /
  `--report`) — the canonical, serial, resumable regenerator that re-runs each
  such producer and records how far every number moved. `rho-k-co-casimir` is
  one of its targets. **Use this, not a hand-edit** (it never writes a witness
  itself).

The refresh must run where the χ compute is tractable. This document exists
because a fresh sandbox that has **not** built `pyhecke-native` (see
[`docs/pyhecke-native-setup.md`](../pyhecke-native-setup.md)) — and/or whose
`chi_numpy` fast path silently fell back to mpmath `chi_numeric` — makes ⁴He
(n=12) a tens-of-hours run. On a correctly-provisioned environment the origin
run was ~2533 s for ⁴He.
