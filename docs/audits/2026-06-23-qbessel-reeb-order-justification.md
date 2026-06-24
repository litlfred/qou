# Reeb-flow propagator order: +1/2 justified, −1/2 is the artifact, and forced weights leave it subdominant

**Date:** 2026-06-23
**Branch:** `claude/nice-dirac-ywun65` (PR #2661)
**Status:** order-disambiguation + scale test for the qbk2 Reeb propagator; no fit; nothing wired.
**Script:** [`computations/qbeta/qbessel_reeb_order_justification.py`](../../computations/qbeta/qbessel_reeb_order_justification.py)
**Witness:** [`computations/probes/qbessel-reeb-order-justification.witness.json`](../../computations/probes/qbessel-reeb-order-justification.witness.json)
**Resolves:** the ±1/2 proxy ambiguity flagged in [`2026-06-20-qbessel-reeb-flow-radial-argument.md`](2026-06-20-qbessel-reeb-flow-radial-argument.md) / `qbessel_qdeformed_reeb_scale.py`.

## Two questions (owner)

1. *Try the proper integer-order reduction* (no ±0.5 proxy).
2. *Justify the ±1/2.*

## The ±1/2 is physics, not a resonance-dodge — and it picks +1/2

The `qbessel_qdeformed_reeb_scale.py` proxy used `ν = dim−1 ± 1/2` to dodge the
integer resonance `(q^k−q^ν)=0` in the **`d_k`-recurrence** second solution, then
read the ±0.5 swing as "not forced." But the **reduction-of-order** second solution
(`g2 = −g1·Σ_j (q^j w)^{−ν}/[g1(q^j w)g1(q^{j+1}w)]`, the q-Casoratian q-integral)
has **no such resonance** and gives the genuine integer-order log-Neumann directly.
And half-integer order is independently motivated — all three reasons pick **+1/2**:

1. **Spherical Bessel** `j_l = √(π/2x)·J_{l+1/2}` — radial modes of a *3D* tube (integer = 2D-annular cross-section).
2. **Langer correction** — the d-dim radial Laplacian reduces to Bessel order `ν = l+(d−2)/2`: d=3 → `+1/2`.
3. **Reeb spin half-twist** — the framing/writhe flow lives on the SU(2) double cover; its natural angular order is spinorial (half-integer).

The **−1/2 branch is unphysical**: it puts every dim-1 block at `ν=−1/2` (negative order ⇒ the `(q^j w)^{−ν}` factor *grows* ⇒ a divergent, dominant propagator). So the honest forced-ness test is **integer vs +1/2** (both `ν≥0`), not the old ±1/2 swing.

## Result (deuteron, real χ_λ + forced y_λ; reduction-of-order g2)

| order | raw (unwtd) | A = Σ y·dG | B = Σ y·χ·dG | \|A\|/(B_D/m_e) | top-block |
|-------|-------------|------------|--------------|------------------|-----------|
| **integer** (2D-annular) | 9.715 (ratio 2.23) | −0.0563 | −0.244 | **0.013×** | 27% |
| **+1/2** (spherical/Langer/spin) | 9.697 | +0.104 | +0.235 | **0.024×** | 58% |
| −1/2 (unphysical) | **27.24** (inflated) | −0.098 | −0.523 | 0.023× | 53% |

- The integer-order raw (9.7151) and y-weighted A (−0.0563) **reproduce the established #2549 values exactly** — the reduction-of-order `g2` is correct.
- The **−1/2 branch inflates `raw` to 27.2** and carries the single-block domination — confirming it was the artifact, not physics.

## Honest verdict — order resolved, lead deflated

- **±1/2 resolved:** +1/2 is the physical half-integer order; −1/2 is the artifact. The old "ratio 6.16 / ~150× q-enhancement" was largely the **unphysical −1/2 branch + the *unweighted* sum**.
- **At proper order + forced weights it is SUBDOMINANT.** Integer and +1/2 both give `|A|/(B_D/m_e) ≈ 0.013–0.024` and `|B|/… ≈ 0.05` — i.e. **≈20–80× too small**. The forced `y_λ` weights induce a **near-cancellation** among the dominant blocks ([4,2] `+0.16` vs [5,1] `−0.15`, [6] `−0.08`), crashing the raw 2.23× down to subdominant.
- **Two residual structural choices remain** (both leave it subdominant): the weighting form (A vs B differ ~0.6 relative) and the order (integer vs +1/2 spread 0.30). Neither is a magnitude lifter; the bar-parity gate (untested) is a symmetry, not a scale.

## Bucket (per the too-small≠wrong triage)

**SUBDOMINANT-but-REAL.** The Reeb propagator correction is forced (no fit), now correctly ordered, and real — but it is **not** the binding closure. The earlier promising "few-×" reading does not survive proper ordering + forced weights. This is the honest deflation, not a refutation: qbk2 stays a real, subdominant, un-wired correction; `c_k`/`Δ_λ` cal-anchored. No production change.
