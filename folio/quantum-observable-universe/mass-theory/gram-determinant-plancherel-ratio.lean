import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import QOU.Archimedean.GramDetRatioCongruence

/-!
# QOU.Archimedean.GramDeterminantPlancherelRatio

Class-axiomatised formulation (§3b-cond) of `conj:gram-determinant-plancherel-ratio`
together with unconditional Wedderburn block-diagonal and basis-invariance
theorems over an arbitrary field `K` (§7c, zero `ℝ` specialisation).

The Chern–Simons Gram-determinant ratio `κ := det G_CS^cl / det G_CS^q` on the
rank-2 force-carrier sublattice (`def:cs-gram-determinant-ratio`) is conjectured
to admit a closed-form Plancherel-weighted character product once `T_{2,9}` and
`T_{3,5}` are placed in a common `n`-strand Hecke algebra with integer pairing
exponents `e_λ ∈ ℤ`:

  `det G_CS^cl / det G_CS^q = ∏_{λ ⊢ n} ((dim V_λ / dim_q V_λ) · ([n]_q! / n!))^{e_λ}`.

## What is proved unconditionally vs carried by the class

1. **Unconditional (`gramKappaProduct_classical_limit`):** when quantum block
   dimensions and `[n]_q!` coincide with their classical counterparts (and are
   non-zero), the Plancherel product equals `1`.
2. **Unconditional (`gramKappaProduct_dual_eq_inv`):** swapping classical and
   quantum dimensions/factorials inverts the Plancherel product.
3. **Unconditional (`diagonal_gramDetRatio_eq_prod`):** for diagonal Wedderburn
   Gram matrices `diagonal wCl` and `diagonal wQ`, the Gram-determinant ratio
   equals the product of blockwise ratios `∏ i, (wCl i / wQ i)`.
4. **Conditional (`gram_determinant_plancherel_ratio`):** under
   `[GramDeterminantPlancherelRatio K Gcl Gq]`, any invertible change of basis
   `B` (`B.det ≠ 0`) transports `Gcl, Gq` to congruent Gram matrices whose
   determinant ratio equals the same `gramKappaProduct D`.

LaTeX label: `conj:gram-determinant-plancherel-ratio`

## References

- [leitner2026] §5/gram-determinant-plancherel-ratio
- [jones1987] https://doi.org/10.2307/1971403 — Hecke algebra Markov traces
- [serre1977] https://doi.org/10.1007/978-1-4684-9458-7 — Wedderburn characters
-/

namespace QOU.Archimedean

open Matrix

/-- Algebraic Wedderburn–Plancherel character datum over a field `K` on a common
    `n`-strand Hecke embedding, with integer pairing exponents `pairingExp λ ∈ ℤ`. -/
structure WedderburnPlancherelDatum (K : Type*) [Field K] where
  /-- Active partition labels `λ ⊢ n` on the common strand count `n`. -/
  blocks : Finset (List ℕ)
  /-- Classical irreducible dimension `dim V_λ` in `K`. -/
  dimClassical : List ℕ → K
  /-- Quantum dimension `dim_q V_λ` in `K`. -/
  dimQuantum : List ℕ → K
  /-- Integer character-pairing exponent `e_λ ∈ ℤ`. -/
  pairingExp : List ℕ → ℤ
  /-- Quantum factorial `[n]_q!` in `K`. -/
  qFactorial : K
  /-- Classical factorial `n!` in `K`. -/
  nFactorial : K

/-- Dual datum exchanging classical and quantum dimensions and factorials. -/
def WedderburnPlancherelDatum.dual {K : Type*} [Field K]
    (D : WedderburnPlancherelDatum K) : WedderburnPlancherelDatum K where
  blocks := D.blocks
  dimClassical := D.dimQuantum
  dimQuantum := D.dimClassical
  pairingExp := D.pairingExp
  qFactorial := D.nFactorial
  nFactorial := D.qFactorial

/-- The Plancherel-weighted character product over `D.blocks` in `K`. -/
def gramKappaProduct {K : Type*} [Field K]
    (D : WedderburnPlancherelDatum K) : K :=
  D.blocks.prod fun lam =>
    ((D.dimClassical lam / D.dimQuantum lam) * (D.qFactorial / D.nFactorial)) ^
      (D.pairingExp lam)

/-- **Unconditional (classical limit `q → 1`).** When every active block has
    non-zero `dimQuantum lam = dimClassical lam` and non-zero
    `qFactorial = nFactorial`, the Plancherel product evaluates to `1`. -/
theorem gramKappaProduct_classical_limit {K : Type*} [Field K]
    (D : WedderburnPlancherelDatum K)
    (hdim : ∀ lam ∈ D.blocks, D.dimClassical lam = D.dimQuantum lam)
    (hdim_nz : ∀ lam ∈ D.blocks, D.dimQuantum lam ≠ 0)
    (hfact : D.qFactorial = D.nFactorial)
    (hfact_nz : D.nFactorial ≠ 0) :
    gramKappaProduct D = 1 := by
  unfold gramKappaProduct
  apply Finset.prod_eq_one
  intro lam hlam
  rw [hdim lam hlam, hfact, div_self (hdim_nz lam hlam), div_self hfact_nz,
    mul_one, one_zpow]

/-- **Unconditional (classical/quantum inversion duality).** Exchanging the
    classical and quantum data inverts every block factor and hence inverts
    `gramKappaProduct`. -/
theorem gramKappaProduct_dual_eq_inv {K : Type*} [Field K]
    (D : WedderburnPlancherelDatum K) :
    gramKappaProduct D.dual = (gramKappaProduct D)⁻¹ := by
  unfold gramKappaProduct WedderburnPlancherelDatum.dual
  rw [← Finset.prod_inv_distrib]
  apply Finset.prod_congr rfl
  intro lam _
  rw [← inv_zpow]
  congr 1
  rw [mul_inv, inv_div, inv_div]

/-- **Unconditional (Wedderburn diagonal Gram factorisation).** For diagonal Gram
    matrices `diagonal wCl` and `diagonal wQ` with non-vanishing quantum weights,
    `det (diagonal wCl)` factors as `det (diagonal wQ) * ∏ i, (wCl i / wQ i)`. -/
theorem diagonal_gramDetRatio_eq_prod {K : Type*} [Field K]
    {m : Type*} [Fintype m] [DecidableEq m]
    (wCl wQ : m → K) (hwQ : ∀ i : m, wQ i ≠ 0) :
    (Matrix.diagonal wCl).det =
      (Matrix.diagonal wQ).det * Finset.univ.prod (fun i => wCl i / wQ i) := by
  rw [Matrix.det_diagonal, Matrix.det_diagonal, ← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i _
  exact (mul_div_cancel₀ (wCl i) (hwQ i)).symm

/-- **Open conjecture (`conj:gram-determinant-plancherel-ratio`, §3b-cond).**
    Asserts the existence of a common-strand integer-exponent Wedderburn–Plancherel
    datum `D` with non-vanishing quantum dimensions and `n!` whose character
    product equals the rank-2 Chern–Simons Gram-determinant ratio
    `Gcl.det / Gq.det`. No global instance is registered. -/
class GramDeterminantPlancherelRatio (K : Type*) [Field K]
    (Gcl Gq : Matrix (Fin 2) (Fin 2) K) : Prop where
  /-- Non-degeneracy of the `q`-deformed Chern–Simons pairing (`det G_CS^q ≠ 0`). -/
  gq_det_ne_zero : Gq.det ≠ 0
  /-- Existence of a well-defined common-strand Plancherel datum reproducing `κ`. -/
  plancherel_factorisation :
    ∃ D : WedderburnPlancherelDatum K,
      (∀ lam ∈ D.blocks, D.dimQuantum lam ≠ 0) ∧
      D.nFactorial ≠ 0 ∧
      Gcl.det / Gq.det = gramKappaProduct D

/-- **Conditional theorem (basis-independent Plancherel identity).**
    Under `[GramDeterminantPlancherelRatio K Gcl Gq]`, transporting both
    Chern–Simons pairings by any invertible rank-2 basis change `B` (`B.det ≠ 0`)
    preserves non-degeneracy of `Bᵀ * Gq * B` and yields the identical
    Plancherel character product `gramKappaProduct D`. -/
-- Ref: [leitner2026] §5/gram-determinant-plancherel-ratio
theorem gram_determinant_plancherel_ratio {K : Type*} [Field K]
    (Gcl Gq B : Matrix (Fin 2) (Fin 2) K)
    [h : GramDeterminantPlancherelRatio K Gcl Gq]
    (hB : B.det ≠ 0) :
    (Bᵀ * Gq * B).det ≠ 0 ∧
    ∃ D : WedderburnPlancherelDatum K,
      (∀ lam ∈ D.blocks, D.dimQuantum lam ≠ 0) ∧
      D.nFactorial ≠ 0 ∧
      (Bᵀ * Gcl * B).det / (Bᵀ * Gq * B).det = gramKappaProduct D := by
  refine ⟨?_, ?_⟩
  · rw [det_congr_eq]
    exact mul_ne_zero (pow_ne_zero 2 hB) h.gq_det_ne_zero
  · obtain ⟨D, hq, hn, heq⟩ := h.plancherel_factorisation
    refine ⟨D, hq, hn, ?_⟩
    rw [gramDetRatio_congr_invariant B Gcl Gq hB, heq]

end QOU.Archimedean
