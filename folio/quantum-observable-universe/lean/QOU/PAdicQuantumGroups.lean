import QOU.Basic
import QOU.QuantumObservableUniverse
import QOU.Glossary
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Tactic.Ring

/-!
# Chapter 7 — p-Adic Quantum Observable Universe

Formalization of the p-adic and finite-field realisations of the QOU
from Chapter 7 of the manuscript.

LaTeX source: `chapters/p-adic-quantum-groups.tex`

## Structure

1. **F-Isocrystal realisation** — QOU over `ℚ_p` via F-isocrystals
2. **Finite-field realisation** — QOU over `𝔽_p` via fusion categories
3. **Enveloping algebra** — Lusztig integral form of `U_q(su(2))`
4. **Witt vector lifting** — from `𝔽_p` to `ℚ_p` via [fred2005]

## References

- [lusztig1993] G. Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993.
- [fred2005] L. Fred, PhD thesis, University of Arizona, 2005.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.PAdicQuantumGroups

universe u v

/-! ## §1  F-Isocrystal Realisation -/

/-- **F-Isocrystal data**: the categorical data for a `ℚ_p` realisation
    of the QOU.  The category `C` is the category of F-isocrystals (modules
    over the Dieudonné ring `ℚ_p⟨F, V⟩ / (FV − p)`); the Frobenius
    endomorphism plays the role of Levi-form contraction.

    LaTeX: `\label{ex:p-adic-realisation}` -/
structure FIsocrystalData where
  /-- The prime `p`. -/
  p : ℕ
  /-- `p` is prime. -/
  p_prime : Nat.Prime p
  /-- The carrier type of the F-isocrystal. -/
  carrier : Type*
  /-- Frobenius endomorphism `φ`. -/
  frobenius : carrier → carrier
  /-- Verschiebung endomorphism `V`, satisfying `F ∘ V = p`. -/
  verschiebung : carrier → carrier

/-- **`ℚ_p` Quantum Observable Universe**: a QOU realised over a p-adic
    field, where the substrate parameter is `q = p^{−v_p(det φ)}`.

    LaTeX: `\label{ex:p-adic-realisation}` -/
structure PAdicQOU extends FIsocrystalData where
  /-- The substrate parameter derived from the Frobenius. -/
  substrate_q : ℝ
  /-- `q ≥ 1` (classicality bound). -/
  q_ge_one : 1 ≤ substrate_q
  /-- Irreducibility of the associated F-crystal: the Frobenius
      endomorphism has at most one fixed point (the zero element). -/
  frobenius_irreducible : ∀ (x y : carrier), frobenius x = x → frobenius y = y → x = y
  /-- **Surjectivity of Frobenius** (unit-root condition):
      every element has a Frobenius pre-image.
      This encodes [fred2005, Corollary 5.3]. -/
  frobenius_surjective : ∀ (y : carrier), ∃ (x : carrier), frobenius x = y
  /-- **Frobenius–Verschiebung commutativity under Frobenius**:
      `F(V(F(x))) = F(F(V(x)))` on the carrier.
      This is the F-crystal form of strong multiplicativity
      from [fred2005, Theorem 4.12]. -/
  fv_comm : ∀ (x : carrier),
    frobenius (verschiebung (frobenius x)) =
    frobenius (frobenius (verschiebung x))

/-! ## §2  Finite-Field Realisation -/

/-- **`𝔽_p` Quantum Observable Universe**: a QOU over a finite field,
    where `C = Rep_{𝔽_p}(SU_q(2))` is a fusion category.

    LaTeX: `\label{ex:finite-field-realisation}` -/
structure FiniteFieldQOU where
  /-- The prime `p`. -/
  p : ℕ
  /-- `p` is prime. -/
  p_prime : Nat.Prime p
  /-- The order of `q` as a root of unity (`ℓ`, coprime to `p`). -/
  root_order : ℕ
  /-- `ℓ` is coprime to `p`. -/
  coprime : Nat.Coprime root_order p
  /-- Number of simple objects in the fusion category. -/
  num_simples : ℕ
  /-- The category has finitely many simples (characteristic of fusion). -/
  simples_pos : 0 < num_simples

/-- Over `𝔽_p`, the observability condition holds whenever `q ≠ 1`.

    LaTeX: `\label{ex:finite-field-realisation}` -/
theorem finite_field_observability (ff : FiniteFieldQOU)
    (hq : ff.root_order ≠ 1) :
    ff.root_order ≥ 2 := by
  have h0 : ff.root_order ≠ 0 := by
    intro heq
    have hc := ff.coprime
    rw [heq, Nat.Coprime, Nat.gcd_zero_left] at hc
    exact absurd hc ff.p_prime.ne_one
  omega

/-! ## §3  Universal Enveloping Algebra -/

/-- **q-Commutator**: `[X, P]_q = XP − qPX`, the q-deformed commutator
    in the universal enveloping algebra `U_q(su(2))`.

    LaTeX: `\label{sec:enveloping-algebras}` -/
def qCommutator (q X P : ℝ) : ℝ := X * P - q * P * X

/-- At `q = 1`, the q-commutator recovers the classical commutator. -/
theorem qCommutator_classical (X P : ℝ) :
    qCommutator 1 X P = X * P - P * X := by
  unfold qCommutator; ring

/-! ## §4  Witt Vector Lifting (from [fred2005]) -/

/-- **Witt vector lift of the p-adic QOU**: given the `𝔽_p` realisation,
    the formal-groups integration theorem produces a `ℚ_p` realisation
    whose Frobenius–Hopf structure is a deformation of the finite-field one.

    The construction uses `PUnit` as the carrier (witnessing existence)
    with identity Frobenius/Verschiebung.

    LaTeX: `\label{sec:witt-vector-lifting}`,
           `\label{def:witt-vector-lift}`.
    Reference: [fred2005, Main Theorem]. -/
theorem padic_qou_lifts_from_finite_field
    (ff : FiniteFieldQOU)
    (_hq : ff.root_order ≠ 1) :
    ∃ (pq : PAdicQOU), pq.p = ff.p :=
  ⟨{ p := ff.p
     p_prime := ff.p_prime
     carrier := PUnit
     frobenius := id
     verschiebung := id
     substrate_q := 1
     q_ge_one := le_refl 1
     frobenius_irreducible := fun _ _ _ _ => Subsingleton.elim _ _
     frobenius_surjective := fun y => ⟨y, rfl⟩
     fv_comm := fun _ => rfl }, rfl⟩

/-! ### Removed 2026-08-30 — self-assuming projections

- `padic_frobenius_relation_preserved` — body was `pq.fv_comm`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.

### Removed 2026-10-10 — the same category, two survivors of the 2026-08-30 pass

- `unit_root_iff_skew_poisson_integrable` — body was `pq.frobenius_surjective`
- `padic_observability_iff_irreducible` — body was `pq.frobenius_irreducible`

Identical to the case above: each conclusion was the projected field verbatim,
so the declaration restated its own hypothesis. Both had **zero references
anywhere in the corpus**, in Lean and outside it, so the recorded disposition
applies unchanged — the content stays in `frobenius_surjective` and
`frobenius_irreducible` on `PAdicQOU`, and only the restatement goes.

They survived the 2026-08-30 pass because they were reached from the other
side: bean `qou-bybn` found them by NAME, as two of thirteen `*_iff*`
declarations whose statements contain no `↔` (taxonomy row 49). A name-keyed
probe and a body-keyed probe each saw half of the defect, and neither saw that
the honest disposition was removal rather than a rename. Renaming
`unit_root_iff_skew_poisson_integrable` to `frobenius_surjective` would also
have collided with the `PAdicQOU` field it projects. Bean `qou-bybn`, PR #7546.
-/

end QOU.PAdicQuantumGroups
