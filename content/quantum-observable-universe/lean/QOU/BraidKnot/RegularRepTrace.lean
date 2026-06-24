import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Trace
import Mathlib.Data.Fintype.Perm
import QOU.BraidKnot.JucysMurphyCoeff

/-!
# QOU.BraidKnot.RegularRepTrace — the regular-representation trace bridge for Identity (B)

This file supplies the **general-`n`** bridge that the `n ≤ 12` partition-form check of
Identity (B) (`IdentityIContentDecomposition.idB_verified_le12`) flagged as future work in its
status note: *"the central Jucys–Murphy element `Σ_k X_k²` acts on the block `V_λ` by the scalar
`Σ_{c∈λ} c(c)²`, so its Plancherel average is its identity coefficient `Σ_{k<n} k = binom(n,2)`."*

That note names the **two** ways to compute the trace of the central element `C₂ = Σ_k X_k²`
acting by left multiplication on the regular representation `R[S_n]`:

1. **Coefficient side (this file, general `n`, ℂ-free):**
   `tr_reg(C₂) = |S_n| · coeff_1(C₂) = n! · binom(n,2)`.
   The general fact — `tr` of left-multiplication by `z` on `R[G]` is `|G|·z(1)` — is
   `trace_mulLeft_eq_card_mul_coeff_one`; specialised to `C₂` (whose identity coefficient is
   `binom(n,2)`, the merged `JucysMurphyCoeff.centralC2_coeff_one`) it gives
   `trace_centralC2_eq_factorial_mul_choose_two`.

2. **Block side (Wedderburn, *not* in pinned Mathlib):**
   `tr_reg(C₂) = Σ_λ dim(λ) · tr_{V_λ}(C₂) = Σ_λ dim(λ)² · Σ_{c∈λ} c(c)²`,
   using `R[S_n] ≅ ⊕_λ dim(λ)·V_λ` and the JM eigenvalue `ω_λ(C₂) = Σ_{c∈λ} c(c)²`.

Equating the two sides is exactly Identity (B):
`Σ_λ dim(λ)² · Σ_{c∈λ} c(c)² = n! · binom(n,2)`.
**This file discharges side 1 in full generality over any `CommRing R`** (§7c base-ring
discipline — no ℂ, no representation theory, no `dim(λ)`/SYT/RSK). Side 2 — the Wedderburn
block decomposition of the group algebra together with the Jucys–Murphy eigenvalue theorem —
is absent from the pinned Mathlib, so the equality of the two sides for **general `n`** remains
future work; the `n ≤ 12` machine check stands in the meantime.

The general lemma `trace_mulLeft_eq_card_mul_coeff_one` is the standard "trace of the left
regular representation reads off the identity coefficient" fact, proved here directly from the
basis-of-`single`s matrix of `LinearMap.mulLeft`: the `(i,j)` entry is `z(i·j⁻¹)`, so the
diagonal is the constant `z(1)`, and the trace is `|G|·z(1)`.

## References
- [manuscript] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (B)"
- [manuscript] content/.../BraidKnot/IdentityIContentDecomposition.lean (the `n ≤ 12` block-side check)
- [manuscript] content/.../BraidKnot/JucysMurphyCoeff.lean (`centralC2_coeff_one`, the ℂ-free coefficient)
-/

open MonoidAlgebra Finset

namespace QOU.BraidKnot.RegularRepTrace

variable {R : Type*} [CommRing R]

/-- **Trace of the left regular representation reads off the identity coefficient.**
For a finite group `G` and `z ∈ R[G] = MonoidAlgebra R G` over any `CommRing R`, the trace of
left-multiplication by `z` on the regular representation is `|G| · z(1)`. Proof: in the basis of
`single g 1` (`Finsupp.basisSingleOne`), the matrix of `LinearMap.mulLeft R z` has `(i,j)` entry
`(z * single j 1) i = z(i · j⁻¹)` (`MonoidAlgebra.mul_single_apply`), so every diagonal entry is
`z(j · j⁻¹) = z(1)`; summing the constant diagonal over the `|G|` basis vectors gives `|G|·z(1)`.
No field, no representation theory — pure group-algebra/linear-algebra over generic `R`. -/
theorem trace_mulLeft_eq_card_mul_coeff_one {G : Type*} [Group G] [Fintype G] [DecidableEq G]
    (z : MonoidAlgebra R G) :
    LinearMap.trace R (MonoidAlgebra R G) (LinearMap.mulLeft R z) = (Fintype.card G : R) * z 1 := by
  let b : Module.Basis G R (MonoidAlgebra R G) := Finsupp.basisSingleOne
  rw [LinearMap.trace_eq_matrix_trace R b (LinearMap.mulLeft R z), Matrix.trace]
  have hdiag : ∀ j : G,
      (LinearMap.toMatrix b b (LinearMap.mulLeft R z)).diag j = z 1 := by
    intro j
    rw [Matrix.diag_apply, LinearMap.toMatrix_apply, LinearMap.mulLeft_apply]
    show (z * single j (1 : R)) j = z 1
    rw [MonoidAlgebra.mul_single_apply, mul_inv_cancel, mul_one]
  rw [Finset.sum_congr rfl (fun j _ => hdiag j), Finset.sum_const, Finset.card_univ, nsmul_eq_mul]

/-- The Jucys–Murphy central element `C₂ = Σ_k X_k²`, `X_k = Σ_{i<k}(i k)`, as a named element of
`R[S_n] = MonoidAlgebra R (Perm (Fin n))`. This is the exact expression whose identity coefficient
is computed by `JucysMurphyCoeff.centralC2_coeff_one`. -/
noncomputable def centralC2 (n : ℕ) : MonoidAlgebra R (Equiv.Perm (Fin n)) :=
  ∑ k : Fin n, (∑ i ∈ Finset.univ.filter (fun i : Fin n => i.val < k.val),
    single (Equiv.swap i k) (1 : R)) ^ 2

/-- The identity coefficient of `centralC2` is `binom(n,2)` (re-exported from the merged
ℂ-free core `JucysMurphyCoeff.centralC2_coeff_one`; the two agree by definitional unfolding). -/
theorem centralC2_coeff_one (n : ℕ) : (centralC2 (R := R) n) 1 = (n.choose 2 : R) :=
  QOU.BraidKnot.JucysMurphyCoeff.centralC2_coeff_one n

/-- **Identity (B), coefficient side, general `n`, ℂ-free.** The trace of the Jucys–Murphy central
element `C₂` acting by left multiplication on the regular representation `R[S_n]` is
`n! · binom(n,2)`, over **any** `CommRing R`. Combines the general trace formula
(`trace_mulLeft_eq_card_mul_coeff_one`: `tr_reg(z) = |S_n|·z(1)`), the order `|S_n| = n!`
(`Fintype.card_perm` + `Fintype.card_fin`), and the identity coefficient `C₂(1) = binom(n,2)`
(`centralC2_coeff_one`). This is side 1 of the Identity-(B) trace equation; equating it with the
Wedderburn block side `Σ_λ dim(λ)²·Σ_{c∈λ} c(c)²` (absent from pinned Mathlib) yields (B). -/
theorem trace_centralC2_eq_factorial_mul_choose_two (n : ℕ) :
    LinearMap.trace R (MonoidAlgebra R (Equiv.Perm (Fin n)))
        (LinearMap.mulLeft R (centralC2 (R := R) n))
      = (n.factorial : R) * (n.choose 2 : R) := by
  rw [trace_mulLeft_eq_card_mul_coeff_one (centralC2 (R := R) n), centralC2_coeff_one]
  congr 1
  rw [Fintype.card_perm, Fintype.card_fin]

end QOU.BraidKnot.RegularRepTrace
