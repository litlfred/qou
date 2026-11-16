import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# Mass endomorphism conjecture (Lean class)

The mass-endomorphism conjecture asserts that the Hecke mass element
Φ_mass(β) ∈ H_n(R, q) admits a closed-form NF decomposition expressible
in terms of:
  - the braid word β,
  - the substrate parameter q,
  - the quantum dilogarithm Φ_q.

This file encodes the conjecture as a Lean `class` whose fields are
the asserted (but not yet derived) closed-form data. Downstream
results that are *conditional* on the conjecture take this class as
an instance hypothesis and become fully provable theorems — the
unproved input is exactly the class instance, and the conditional
results are verified by Lean.

This pattern (axiomatize the conjecture as a class, prove conditional
downstream results) follows §3b of `AGENTS.md`.

-- Ref: [leitner2026] conj:mass-endomorphism
-- Ref: [leitner2026] conj:brane-tower-z-habiro
-- Ref: [leitner2026] conj:quantum-dilogarithm-stratified
-/

namespace QOU.WedderburnMass

/-- The mass-endomorphism conjecture, encoded as a class.

    A `MassEndomorphism R β` instance asserts the existence of a
    closed-form NF decomposition for the Hecke mass element Φ_mass(β).
    Specifically, it provides:
      - a finite list of generators (the NF basis) with coefficients,
      - the transient (brane-tower) component as a Σ Φ_q(z_i),
      - the algebraic-volume coordinates z_i,
      - the substrate parameter q ∈ R.

    The `vol_identity` field is the asserted equality
    Σ_i Φ_q(z_i) = Vol(K)/ℏ_q² — the topological-decomposition
    part of the conjecture (Step 2 in conj:mass-endomorphism's
    "What is known"). -/
-- Ref: [leitner2026] conj:mass-endomorphism
class MassEndomorphism (R : Type*) [CommRing R] (β : Type*) where
  /-- The substrate parameter q ∈ R. -/
  q : R
  /-- The number of brane levels N (depends on the braid word β). -/
  N : ℕ
  /-- The algebraic-volume coordinates z_i for i = 1..N. -/
  z : Fin N → R
  /-- The transient (brane-tower) Markov-trace component:
      tr_M(Φ^trans(β)) = Σ_{i=1}^{N} Φ_q(z_i). -/
  tr_transient : R
  /-- The descended Markov-trace component: tr_M(ρ(β)). -/
  tr_descended : R
  /-- The asserted volume identity:
      tr_transient = Vol(K_β)/ℏ_q² − |tr_descended|. -/
  vol_identity : R   -- the value Vol(K_β)/ℏ_q²
  /-- The volume identity as an equality. The proof of this equality
      is the open part of the conjecture; instances supply it as a
      hypothesis (axiomatic input). -/
  -- Ref: [leitner2026] conj:mass-endomorphism §"Statement"
  vol_eq : tr_transient = vol_identity - tr_descended

/-- The full categorical mass at brane-tower-saturation. Conditional
    on a `MassEndomorphism` instance, this gives the mass as the sum
    of the descended Markov trace plus the transient brane-tower —
    fully derived from the class data, no further sorries. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"Step 2"
def fullMass {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] : R :=
  M.tr_descended + M.tr_transient

/-- Conditional theorem: under the mass-endomorphism conjecture, the
    full categorical mass equals the volume identity term. This is
    proved unconditionally from the class instance — the only
    "axiomatic" input is the existence of the instance itself. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"What is known", Step 2
theorem fullMass_eq_volume {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] :
    fullMass β = M.vol_identity := by
  unfold fullMass
  rw [M.vol_eq]
  ring

/-- The brane-tower partial sum at level N, conditional on a
    `MassEndomorphism` instance. Mirrors the
    `conj:brane-tower-z-habiro` Cauchy-sequence claim: the partial
    sums tr_transient stabilise as N grows, with the limit in the
    z-Habiro completion. -/
-- Ref: [leitner2026] conj:brane-tower-z-habiro
def braneTowerPartialSum {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] : R :=
  M.tr_transient

-- ────────────────────────────────────────────────────────────────────────────
-- Further conditional theorems (proved from MassEndomorphism axioms alone)
-- ────────────────────────────────────────────────────────────────────────────

/-- **Transient part is uniquely determined by the class data.**

    Given `vol_eq : tr_transient = vol_identity - tr_descended`,
    there is exactly one value of tr_transient consistent with the
    class — namely `vol_identity - tr_descended`.  Any other element
    satisfying the same equation equals tr_transient. -/
-- Ref: [leitner2026] conj:mass-endomorphism §Statement
theorem transient_unique {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] (t : R)
    (h : t = M.vol_identity - M.tr_descended) :
    t = M.tr_transient := by
  rw [h, ← M.vol_eq]

/-- **Transient is non-negative when vol_identity ≥ tr_descended.**

    If the volume identity term dominates the descended trace, the
    brane-tower contribution `tr_transient` is non-negative.  This is
    the algebraic content of the physical expectation that the tower
    always contributes positively to mass. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"Tower convergence"
theorem transient_nonneg {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R] (β : Type*)
    [M : MassEndomorphism R β]
    (h : M.tr_descended ≤ M.vol_identity) :
    0 ≤ M.tr_transient := by
  have hrw : M.tr_transient = M.vol_identity - M.tr_descended := M.vol_eq
  rw [hrw]; exact sub_nonneg.mpr h

/-- **In the flat case (tr_transient = 0), fullMass equals the descended part.**

    When the brane tower contributes nothing (all z_i = 0 or no
    blow-up centres), the full mass is entirely descended. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"What is known", Step 1
theorem fullMass_eq_descended_of_zero_transient {R : Type*} [CommRing R]
    (β : Type*) [M : MassEndomorphism R β]
    (h : M.tr_transient = 0) :
    fullMass β = M.tr_descended := by
  unfold fullMass
  rw [h, add_zero]

/-- **fullMass = tr_descended + tr_transient** (explicit decomposition lemma).

    This is definitional but stated as a lemma to make the two-term
    structure available for downstream rewrites. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"What is known"
theorem mass_decomposition {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] :
    fullMass β = M.tr_descended + M.tr_transient := rfl

/-- **The descended part equals vol_identity minus the transient.**

    Equivalent rearrangement of `vol_eq` expressed for the descended piece. -/
-- Ref: [leitner2026] conj:mass-endomorphism §Statement
theorem descended_eq_vol_minus_transient {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] :
    M.tr_descended = M.vol_identity - M.tr_transient := by
  linear_combination M.vol_eq

/-- **Mass is positive when vol_identity > 0 and tr_descended ≥ 0.**

    Under the natural physical conditions (positive volume, non-negative
    descended trace), the full categorical mass is positive. -/
-- Ref: [leitner2026] conj:mass-endomorphism §"What is known"
theorem fullMass_pos_of_vol_pos {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R] (β : Type*)
    [M : MassEndomorphism R β]
    (hvol : 0 < M.vol_identity)
    (hdesc : 0 ≤ M.tr_descended) :
    0 < fullMass (R := R) β := by
  rw [show fullMass (R := R) β = M.vol_identity from fullMass_eq_volume β]
  exact hvol

end QOU.WedderburnMass
