# H₂O bond-angle — knot-hierarchy angular corrections (Reeb-rotation program)

**Owner direction (2026-06-09).** Push the H₂O angle past the leading
trace-weighted VSEPR value **with no fitting**, via:

> non-abelian Stokes · quadratic relations in Hecke · GB filtration + det
> order · **first knot sets the first approximation of the angle, higher-order
> knots adjust it appropriately** · **knot operator as torsion / rotation on
> the Reeb bundle → angular corrections**.

This doc records how that program maps onto existing framework infrastructure,
the concrete quantities computed so far, an honest assessment, and the next
step. Companion compute:
[`h2o_angle_knot_correction.py`](../../computations/h2o_angle_knot_correction.py)
(witness `h2o-angle-knot-correction`).

## The mechanism, mapped to existing infra

| Owner phrase | Framework realisation (existing) |
|---|---|
| knot operator = torsion/rotation on Reeb bundle | `figure-eight-reeb-rotation.md`: `M_{4₁}=(σ₁σ₂⁻¹)²` on `V_{(2,1)}` has unit-modulus eigenvalues `e^{±iθ}` — a Reeb rotation |
| quadratic relations in Hecke | `σ²=hσ+1` ⇒ `σ⁻¹=σ−h`, eigenvalues `q, −q⁻¹`; the source of the rotation phase |
| det order | `det σ = q·(−q⁻¹) = −1` fixes `det M = 1` ⇒ conjugate eigenvalues on the unit circle |
| GB / jet-order filtration | `three-knot-jet-order-independence.md`: the jet-order grading ranks knots (`4₁`, `5₂`, `B₃`); "first knot, then higher knots" = the filtration |
| non-abelian Stokes | `J_K(q)` = Yekutieli/KZ holonomy parallel-transported on `𝒮 = P×_G ℂP¹`; the rotation IS that holonomy |

## Concrete quantities computed (H₃, V_(2,1), no Rust kernel)

| Quantity | Value | Channel |
|---|---|---|
| leading angle (trace-weighted VSEPR, first knot) | **107.19°** | — (on main, `h2o_bond_angle_magnitude_vsepr.py`) |
| observed | 104.5° | — |
| **residual to explain** | **2.69°** | — |
| bond `σ` eigenvalues | `q, −q⁻¹` (`\|λ\|=1.11, 0.90`) | **growth** (no Reeb phase) |
| lone `e⁻=σ₁σ₂σ₁` eigenvalues | `±1` ⇒ **θ_{e⁻}=90.000°** | **rotation** |
| figure-eight `M_{4₁}` | **θ_{4₁}=117.087°** | rotation (lepton-mixing) |

## Honest assessment (no fitting)

- The Reeb rotations are **real, computable, and large/clean** structural
  angles (lone `e⁻` = exactly 90°; figure-eight = 117°). **Neither is the
  2.69° residual**, and no clean ratio yields 2.69° without fitting — so the
  correction is **not** any single knot's raw rotation. (θ_{4₁} is the
  lepton-mixing rotation, the m_μ mechanism.)
- The **structurally decisive split is real**: the bond `σ` is in the
  *growth* channel (no Reeb phase) while the lone `e⁻` is in the *rotation*
  channel — the same bond↔lone asymmetry that gave the **sign** (`Δtr=hz²>0`)
  now reappears as a **phase asymmetry**. The angular correction should be the
  bond↔lone **Reeb-phase difference**, evaluated where the lone pair carries a
  phase the bond does not.

## Next step (concrete, not a fit)

1. Form the bond and lone sub-braids **dressed with the next knot in the
   jet-order filtration** (the `4₁` alternating block), and compute the
   **difference of their Yekutieli/non-abelian-Stokes holonomies** on
   `V_{(2,1)}` — the angular correction = that holonomy difference, projected
   to the bond-angle coordinate. This is the `Δ`-of-rotations analogue of the
   `Δtr` sign result.
2. The dressed bond/lone braids live in **H₄⁺** (more strands), whose
   seminormal operators need `pyhecke_native` (the **Rust kernel**, currently
   unavailable in the web sandbox — `cross_check`/atom kernels raise
   `NotImplementedError`). Run on CI or a kernel-enabled host.
3. Formalize the rotation-channel split (`σ` growth vs `e⁻` rotation on
   `V_{(2,1)}`) as a Lean lemma — it is a clean eigenvalue fact and would
   anchor the correction's sign the way `prop:h2o-bond-angle-shift` anchors
   the leading sign.

**Discipline.** Report `θ` values raw whether or not they match; never tune a
ratio to 2.69°. The win is a *derived* holonomy-difference, or a clean
"rotations are 90°/117°, the residual is a higher-order effect, here is the
blocked compute" — which is the current honest state.
