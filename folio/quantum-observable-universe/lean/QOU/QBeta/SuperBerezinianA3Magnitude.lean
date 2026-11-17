import Mathlib.Tactic

/-!
# QOU.QBeta.SuperBerezinianA3Magnitude — the A=3 magnitude factor `r*` is a FREE parameter of the Berezinian cross-term (underdetermination, not closure)

**Scope (read this first).**  ROUTE 2 of the A=3 magnitude cross-channel program.
This file attacks — and returns an **honest scope-(a) negative on closure** — the
question of whether the super-Berezinian even/odd cross-sector mixing term
`t = B·D⁻¹·C` supplies the **A=3 magnitude factor**
`r* = μ₃/c₃ ≈ 1.585` (the factor by which every *single*-Markov-trace ingredient
— level / geometric `W_λ` / edge / exact-order `μ̄_A` / Vassiliev-weight — is
bracketed short; see `docs/coordination/option-e.md`).

**What is already established (do NOT re-prove).**  The *parity* of the cross-term
is fully worked ON MAIN:

* `QOU.QBeta.OddDecayWeightParity` (`docs/audits/2026-07-25-odd-face-parity-constraint.md`)
  — models `c₃` as the cross-term `t = g·γ` (bar-even dressing × bar-odd weight),
  proves it bar-ODD, and `classical_shadow_on_even_face`: the classical `q=1` mass
  content sits ENTIRELY on the even face; the odd/mixing cross-term has vanishing
  `q=1` shadow.
* `QOU.QBeta.BerezinianSelfAdjointCrossTerm`
  (`docs/audits/2026-07-31-berezinian-selfadjoint-crossterm-bar-even.md`) — a
  self-adjoint off-block pair `C = −σB` forces the cross-term bar-EVEN (`|B|²/D`);
  a genuinely bar-ODD `c₃` therefore requires **non-self-adjoint, INDEPENDENT**
  off-blocks `B, C` (two free amplitudes).

**This file's distinct angle — the MAGNITUDE, not the parity.**  The parity bricks
above settle *how the sign works*; they say nothing about whether the cross-term's
*size* is the missing `r* ≈ 1.585`.  We formalize the magnitude question and prove
the decisive structural fact:

> **The even-face multiplicative correction `(A − t)/A` supplied by the cross-term
> `t = B·D⁻¹·C` is a FREE parameter: for fixed nonzero even/odd blocks `A, C, D`,
> the map `B ↦ (A − B·D⁻¹·C)/A` is SURJECTIVE onto the base field
> (`crossTerm_magnitude_surjective`).  Hence `r*` — like *every* other value — is
> achievable, but only by pinning the off-block `B` to the target, i.e. by a FIT.**

Two proved consequences frame the verdict:

1. **`evenFaceCorrection_no_mixing`** — with **no** mixing (`B = 0`) the correction
   is identically `1`: a block-diagonal / single-trace ingredient supplies **no**
   magnitude lift.  This is *why* every single-trace ingredient is bracketed at the
   same `0.63×` — none of them can move the coefficient at all.
2. **`crossTerm_magnitude_surjective`** — the cross-term is the *unique* source of a
   lift, and its size is unconstrained.  So the Berezinian route is the **first**
   A=3-magnitude ingredient that is *not excluded* from reaching `r*` (unlike the
   bracketed single-trace family) — but it reaches `r*` **only** as a two-amplitude
   fit (bar-oddness already demands the two off-blocks be independent).

**Net verdict (scope-(a), honest negative on closure).**  The super-Berezinian
cross-term does **not** *derive* `r*`.  It **relocates** the wall from "which
single trace" to "**derive the off-diagonal mixing blocks `B, C`**" — which is
exactly the open keystone `conj:qdifference-kernel-prolongation-symbol` /
`qCubicGradedSplit` (bean `qou-jqof`, PR #4140): the DM q-cubic period datum would
*pin* `B, C` geometrically, and only then would the resulting correction be a
prediction rather than a fit.  Absent that derivation the magnitude is a **hidden
degree of freedom** (AGENTS.md Rule 14), directly analogous to the q-dim-convention
hidden DOF (`option-e.md`, 2026-06-28).  `r* ≈ log₂3` is a flagged irrational
coincidence (`VassilievMagnitudeA3.no_integer_weight_eq_rStar`), not a target.

**Honesty (STRICT — AGENTS.md §Axiomatization-is-NOT-a-Proof / §3b).**  Nothing
here is a fit or is wired.  The two theorems are genuine algebra (surjectivity of a
Möbius-type map; the no-mixing identity), sorry-free.  The single conjecture class
`A3CrossTermMagnitudeClosed` is a §3b-tax **dependent** carrier with **NO instance**
— the honest open state of "a *geometrically-derived* (not fitted) off-block yields
the physical magnitude".  It is content-bearing (a parameter-quantified equation on
the derived datum), never `True`, never self-assuming.

**Base ring (§7c).**  Generic `{R : Type*} [Field R]` — the scalar inverses
`D⁻¹`, `A⁻¹`, `C⁻¹` are genuinely required (the §7c `[Field R]` inverse carve-out).
No `ℝ`, no ordering, no `Real.*`; the numeric `r* ≈ 1.585` lives only in the
Python witness / audit, downstream of the substrate→archimedean wall.

## References

- [leitner2026] `conj:qdifference-kernel-prolongation-symbol`; the super-DM /
  Berezinian scaffold `QOU.Brings.SuperDMBerezinian` (`qCubicGradedSplit`, PR #4140,
  off-main); `QOU.QBeta.OddDecayWeightParity`;
  `QOU.QBeta.BerezinianSelfAdjointCrossTerm`;
  `docs/coordination/option-e.md` (the A=3 magnitude bracket rows);
  `docs/audits/2026-08-01-a3-magnitude-super-berezinian-cross-sector.md`.
- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1 (the cubic
  condition that would pin the off-blocks).
-/

noncomputable section

namespace QOU.QBeta.SuperBerezinianA3Magnitude

/-! ### Scalar model of the Berezinian even-face correction

For the leading `(1-even, 1-odd)` super-block with even diagonal block `A`, odd
diagonal block `D`, and off-diagonal (grade-reversing, even↔odd) blocks `B, C`,
the Berezinian numerator is the Schur complement `A − B·D⁻¹·C`
(`Matrix.det_fromBlocks₂₂`, packaged in `QOU.Brings.SuperDMBerezinian.berezinian`).
The **cross-sector correction** the corpus's naive block-diagonal measure drops is
the multiplicative factor `(A − t)/A` on the even (bar-even / mass / C1) face, where
`t` is the cross-term.  Its magnitude is the A=3 factor `r*` under test. -/

/-- The Berezinian **cross-term** `t = B·D⁻¹·C` — the first even↔odd mixing order
    (grade-reversing off-blocks `B, C` bridged by the odd block inverse `D⁻¹`).
    Vanishes exactly at block-diagonal / single-trace order (`B = 0` or `C = 0`). -/
def crossTerm {R : Type*} [Field R] (B C D : R) : R := B * D⁻¹ * C

/-- The multiplicative **even-face correction** the cross-term supplies to the
    bar-even (mass / C1) face: `(A − t)/A` where `t` is the cross-term.  Equals `1`
    exactly when there is no mixing (`t = 0`); the A=3 magnitude claim is that this
    correction equals `r* ≈ 1.585`. -/
def evenFaceCorrection {R : Type*} [Field R] (A t : R) : R := (A - t) / A

/-- **No mixing ⇒ no lift (sorry-free).**  With the off-block `B = 0` the cross-term
    vanishes and the even-face correction is identically `1` (for `A ≠ 0`): a
    block-diagonal / single-trace ingredient supplies **no** magnitude lift.  This
    is the structural reason every single-Markov-trace A=3 ingredient is bracketed
    at the same coefficient — none of them can move it.  The lift must come from the
    cross-term, which is off-diagonal by construction. -/
theorem evenFaceCorrection_no_mixing {R : Type*} [Field R] (A C D : R) (hA : A ≠ 0) :
    evenFaceCorrection A (crossTerm 0 C D) = 1 := by
  simp [evenFaceCorrection, crossTerm, div_self hA]

/-- **A lift requires a nonzero cross-term (sorry-free).**  For `A ≠ 0`, the
    even-face correction equals `1` **iff** the cross-term vanishes.  So any
    magnitude coefficient `≠ 1` (in particular `r* ≈ 1.585`) is possible ONLY through
    a nonzero even↔odd mixing term — never from the diagonal (single-trace) data. -/
theorem evenFaceCorrection_eq_one_iff {R : Type*} [Field R] (A t : R) (hA : A ≠ 0) :
    evenFaceCorrection A t = 1 ↔ t = 0 := by
  unfold evenFaceCorrection
  rw [div_eq_iff hA, one_mul]
  constructor
  · intro h; linear_combination -h
  · intro h; rw [h, sub_zero]

/-- **THE DECISIVE INVARIANT — the cross-term magnitude is a FREE parameter
    (sorry-free).**  For fixed nonzero even/odd blocks `A, C, D`, the map
    `B ↦ evenFaceCorrection A (crossTerm B C D)` is **surjective** onto `R`: for
    *any* target value `r` there is an off-block `B` realizing it.  Concretely the
    witness is `B = A·(1 − r)·D·C⁻¹`, which drives the cross-term to `A·(1 − r)` and
    the correction to `r`.

    **Consequence (the honest verdict).**  The A=3 magnitude factor `r*` is not
    *derived* by the Berezinian cross-term — it is one real constraint on an
    unconstrained off-block, i.e. a **fit**.  Bar-oddness already forces the two
    off-blocks `B, C` to be independent (`BerezinianSelfAdjointCrossTerm`), so the
    route carries ≥ 2 free amplitudes and can hit any sign *and* any magnitude.
    Deriving `B, C` from the DM q-cubic period datum (`qou-jqof`) is the open wall;
    absent it, `r*` is a hidden DOF. -/
theorem crossTerm_magnitude_surjective {R : Type*} [Field R] (A C D r : R)
    (hA : A ≠ 0) (hC : C ≠ 0) (hD : D ≠ 0) :
    ∃ B : R, evenFaceCorrection A (crossTerm B C D) = r := by
  refine ⟨A * (1 - r) * D * C⁻¹, ?_⟩
  unfold evenFaceCorrection crossTerm
  field_simp
  ring

/-! ### The open closure — a *derived* (not fitted) off-block, as an honest carrier

The only way the cross-term supplies `r*` as a *prediction* is if the off-block is
pinned by an independent geometric datum (the DM q-cubic period matrix, `qou-jqof`)
rather than tuned to the target.  We record that open state as a §3b-tax **dependent
conjecture class with NO instance** — content-bearing, never self-assuming, never a
fit. -/

/-- **§3b dependent target conjecture — the A=3 magnitude closes via a DERIVED
    off-block.**

    `@conjecture: dependent` (its content depends on the open DM-cubic derivation of
    the off-blocks — `conj:qdifference-kernel-prolongation-symbol` / the `qou-jqof`
    wall — supplying `B_geom`).

    The claim: the off-block value `B_geom` **supplied by the geometry** (the DM
    q-cubic period datum, an INPUT independent of the physical target) yields exactly
    the physical cross-sector magnitude `κ_phys` on the even face, and `κ_phys ≠ 1`
    (a genuine lift, matching `r* ≈ 1.585 ≠ 1`).

    **Why this is content-bearing and NOT the fit.**  In a *fit*, `B` is solved from
    `κ_phys` (`crossTerm_magnitude_surjective`).  Here `B_geom` is a *given*
    (geometric) input and the equation `evenFaceCorrection A (crossTerm B_geom C D) =
    κ_phys` is a nontrivial *check* that the geometry lands the physics — false for a
    generic `B_geom`.  **No instance is supplied**: the framework does not yet derive
    `B_geom` (that derivation IS the open keystone).  Discharging this by *choosing*
    `B_geom` to hit `κ_phys` would be the forbidden fit and is explicitly not done. -/
-- Ref: [donagi-markman1994] https://arxiv.org/abs/alg-geom/9408004 §1
-- Ref: [leitner2026] conj:qdifference-kernel-prolongation-symbol;
--      QOU.Brings.SuperDMBerezinian (qCubicGradedSplit); qou-jqof;
--      docs/audits/2026-08-01-a3-magnitude-super-berezinian-cross-sector.md
class A3CrossTermMagnitudeClosed {R : Type*} [Field R]
    (A C D B_geom κ_phys : R) : Prop where
  /-- The geometrically-derived off-block `B_geom` (an input from the DM q-cubic,
      NOT tuned to the target) drives the even-face correction to the physical
      cross-sector magnitude `κ_phys`, which is a genuine lift (`≠ 1`). -/
  geom_offblock_gives_magnitude :
    evenFaceCorrection A (crossTerm B_geom C D) = κ_phys ∧ κ_phys ≠ 1


/-! ### Inverse recovery and gauge-scale invariance of the even-face correction (`qou-6r6d`) -/

/-- **Exact left-inverse recovery of the off-block (`qou-6r6d`).** For nonzero blocks `A, C, D`,
the off-block `B` is uniquely recovered from `evenFaceCorrection A (crossTerm B C D)` by
`A * (1 - evenFaceCorrection A (crossTerm B C D)) * D * C⁻¹ = B`. -/
theorem crossTerm_inverse_recovery {R : Type*} [Field R] (A B C D : R)
    (hA : A ≠ 0) (hC : C ≠ 0) (hD : D ≠ 0) :
    A * (1 - evenFaceCorrection A (crossTerm B C D)) * D * C⁻¹ = B := by
  unfold evenFaceCorrection crossTerm
  field_simp
  ring

/-- **Block-rescaling invariance (`qou-6r6d`).** Rescaling `(A, B)` by `α ≠ 0` and
`(C, D)` by `β ≠ 0` leaves `evenFaceCorrection` unchanged. -/
theorem evenFaceCorrection_scale_invariant {R : Type*} [Field R]
    (A B C D α β : R) (hA : A ≠ 0) (hD : D ≠ 0) (hα : α ≠ 0) (hβ : β ≠ 0) :
    evenFaceCorrection (α * A) (crossTerm (α * B) (β * C) (β * D)) =
      evenFaceCorrection A (crossTerm B C D) := by
  unfold evenFaceCorrection crossTerm
  field_simp
  ring

end QOU.QBeta.SuperBerezinianA3Magnitude
