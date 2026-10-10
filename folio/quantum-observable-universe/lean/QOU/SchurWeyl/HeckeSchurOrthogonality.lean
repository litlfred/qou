import QOU.SchurWeyl.HeckeSchurElements
import QOU.SchurWeyl.HeckeWedderburnGeneral

/-!
# QOU.SchurWeyl.HeckeSchurOrthogonality — Schur orthogonality for `H_{m+1}(q)`

Over a field `K` of characteristic `0`, with `q ≠ 0` not a root of unity, write `ρ_λ` for the
seminormal representation of `H_{m+1}(q)` on shape `λ ⊢ m+1` and `c_λ = c_λ(q²)` for its Schur
element.  Then for all partitions `λ, μ` and tableau indices,

```
Σ_w ρ_μ(T_{w⁻¹})_{a d} · ρ_λ(T_w)_{b c} = c_μ · δ_{λ μ} δ_{b d} δ_{c a},
Σ_w χ_μ(T_{w⁻¹}) · χ_λ(T_w)             = δ_{λ μ} · c_μ · f^μ,
```

where `f^μ` is the number of standard tableaux of shape `μ`.

## Main results

* `repr_eq_symTrace` — the `T_w`-coefficient of `x` is `τ(x T_{w⁻¹})` (dual basis at `qi = q⁻¹`).
* `symTrace_eq_sum_schur_partition` — `τ = Σ_λ χ_λ / c_λ`, indexed by partitions.
* `schur_orthogonality` — the matrix-coefficient form.
* `schur_orthogonality_char` — the character form.

## Proof

Take `x` with `ρ_ν(x) = 0` for `ν ≠ μ` and `ρ_μ(x) = E_{d a}` (Wedderburn surjectivity).  The
dual-basis expansion `x = Σ_w τ(x T_{w⁻¹}) T_w`, read in block `λ` at entry `(b, c)`, is the claim,
because `τ(x T_{w⁻¹}) = tr(E_{d a} ρ_μ(T_{w⁻¹})) / c_μ = ρ_μ(T_{w⁻¹})_{a d} / c_μ`.

## Base ring (§7c)

Generic `[Field K] [CharZero K]`; characteristic `0` is what the Wedderburn split
(`heckeProduct_surjective`) uses.  No ordering, no `ℝ`.

LaTeX label: `thm:hecke-schur-orthogonality`

-- Ref: [geckpfeiffer2000] https://global.oup.com/academic/product/9780198502500 (Thm. 7.2.1 and Cor. 7.2.4: Schur relations for symmetric algebras)
-/

namespace QOU.SchurWeyl

open Finset Hecke HeckeCoset Equiv
open QOU.Mathlib (StandardYoungTableau partitionShape partitionShapeEquiv)

section Expansion

variable {K : Type*} [Field K]

/-- **The dual basis at `qi = q⁻¹`**: the `T_w`-coefficient of `x` is `τ(x T_{w⁻¹})`. -/
theorem repr_eq_symTrace (q : K) (hq0 : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m)
    (w : Perm (Fin (m + 1))) :
    (stdBasisAny q q⁻¹ m).repr x w = symTrace q q⁻¹ m (x * stdElt m w⁻¹) := by
  rw [symTrace_mul_stdElt_inv, mul_inv_cancel₀ hq0, one_pow, mul_one]

/-- **The dual-basis expansion** `x = Σ_w τ(x T_{w⁻¹}) T_w`. -/
theorem eq_sum_symTrace_smul (q : K) (hq0 : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    x = ∑ w : Perm (Fin (m + 1)), symTrace q q⁻¹ m (x * stdElt m w⁻¹) • stdElt m w := by
  conv_lhs => rw [← (stdBasisAny q q⁻¹ m).sum_repr x]
  refine Finset.sum_congr rfl fun w _ => ?_
  rw [repr_eq_symTrace q hq0, stdBasisAny_apply]

end Expansion

variable {K : Type*} [Field K] [CharZero K]

/-- **`τ = Σ_λ χ_λ / c_λ`, over partitions** — `symTrace_eq_sum_schur` reindexed along
`partitionShapeEquiv`, in the blocks of `heckeProduct`. -/
theorem symTrace_eq_sum_schur_partition (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    symTrace q q⁻¹ m x
      = ∑ lam : Nat.Partition (m + 1),
          (heckeProduct q hq0 hq2 m x lam).trace / schurElt (q ^ 2) (partitionShape lam) := by
  rw [SeminormalRep.symTrace_eq_sum_schur q hq0 hq2 m x]
  exact (Fintype.sum_equiv (partitionShapeEquiv (m + 1)) _ _ (fun lam => rfl)).symm

/-- **Schur orthogonality, matrix-coefficient form.** -/
theorem schur_orthogonality (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam mu : Nat.Partition (m + 1))
    (a d : StandardYoungTableau (partitionShape mu))
    (b c : StandardYoungTableau (partitionShape lam)) :
    ∑ w : Perm (Fin (m + 1)),
        heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu a d
          * heckeProduct q hq0 hq2 m (stdElt m w) lam b c
      = schurElt (q ^ 2) (partitionShape mu)
          * (Pi.single (M := fun nu : Nat.Partition (m + 1) =>
              Matrix (StandardYoungTableau (partitionShape nu))
                (StandardYoungTableau (partitionShape nu)) K)
              mu (Matrix.single d a 1)) lam b c := by
  classical
  have hc : schurElt (q ^ 2) (partitionShape mu) ≠ 0 :=
    schurElt_ne_zero _ (pow_ne_zero 2 hq0) (gen_of_notRootOfUnity hq2) _
  obtain ⟨x, hx⟩ := heckeProduct_surjective q hq0 hq2 m
    (Pi.single (M := fun nu : Nat.Partition (m + 1) =>
      Matrix (StandardYoungTableau (partitionShape nu))
        (StandardYoungTableau (partitionShape nu)) K) mu (Matrix.single d a 1))
  have hτ : ∀ w : Perm (Fin (m + 1)), symTrace q q⁻¹ m (x * stdElt m w⁻¹)
      = heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu a d / schurElt (q ^ 2) (partitionShape mu) := by
    intro w
    rw [symTrace_eq_sum_schur_partition q hq0 hq2, Finset.sum_eq_single mu]
    · rw [map_mul, Pi.mul_apply, hx, Pi.single_eq_same, Matrix.trace_single_mul, smul_eq_mul,
        one_mul]
    · intro l _ hl
      rw [map_mul, Pi.mul_apply, hx, Pi.single_eq_of_ne hl, zero_mul, Matrix.trace_zero, zero_div]
    · intro h; exact absurd (Finset.mem_univ _) h
  have hexp := congrArg (fun y => heckeProduct q hq0 hq2 m y lam b c)
    (eq_sum_symTrace_smul q hq0 m x)
  simp only [map_sum, map_smul, Finset.sum_apply, Pi.smul_apply, Matrix.sum_apply,
    Matrix.smul_apply, smul_eq_mul, hx] at hexp
  rw [hexp, Finset.mul_sum]
  refine Finset.sum_congr rfl fun w _ => ?_
  rw [hτ w]
  field_simp

/-- **Schur orthogonality, character form**:
`Σ_w χ_μ(T_{w⁻¹}) χ_λ(T_w) = δ_{λμ} · c_μ · f^μ`. -/
theorem schur_orthogonality_char (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam mu : Nat.Partition (m + 1)) :
    ∑ w : Perm (Fin (m + 1)),
        (heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu).trace
          * (heckeProduct q hq0 hq2 m (stdElt m w) lam).trace
      = if lam = mu then
          schurElt (q ^ 2) (partitionShape mu)
            * (Fintype.card (StandardYoungTableau (partitionShape mu)) : K)
        else 0 := by
  classical
  have h : ∀ (a : StandardYoungTableau (partitionShape mu))
      (b : StandardYoungTableau (partitionShape lam)),
      ∑ w : Perm (Fin (m + 1)),
          heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu a a
            * heckeProduct q hq0 hq2 m (stdElt m w) lam b b
        = schurElt (q ^ 2) (partitionShape mu)
          * (Pi.single (M := fun nu : Nat.Partition (m + 1) =>
              Matrix (StandardYoungTableau (partitionShape nu))
                (StandardYoungTableau (partitionShape nu)) K)
              mu (Matrix.single a a 1)) lam b b :=
    fun a b => schur_orthogonality q hq0 hq2 m lam mu a a b b
  have hsum : (∑ w : Perm (Fin (m + 1)),
        (heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu).trace
          * (heckeProduct q hq0 hq2 m (stdElt m w) lam).trace)
      = ∑ a, ∑ b, ∑ w : Perm (Fin (m + 1)),
          heckeProduct q hq0 hq2 m (stdElt m w⁻¹) mu a a
            * heckeProduct q hq0 hq2 m (stdElt m w) lam b b := by
    simp only [Matrix.trace, Matrix.diag_apply, Finset.sum_mul_sum]
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl fun a _ => Finset.sum_comm
  rw [hsum]
  simp only [h]
  by_cases hlm : lam = mu
  · subst hlm
    have hd : ∀ x y : StandardYoungTableau (partitionShape lam),
        Matrix.single x x (1 : K) y y = if x = y then 1 else 0 := by
      intro x y
      by_cases hxy : x = y
      · subst hxy; rw [Matrix.single_apply_same, if_pos rfl]
      · rw [Matrix.single_apply_of_row_ne hxy, if_neg hxy]
    simp only [Pi.single_eq_same, hd, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq,
      Finset.mem_univ, if_true, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    ring
  · rw [if_neg hlm]
    simp [Pi.single_eq_of_ne hlm]

end QOU.SchurWeyl
