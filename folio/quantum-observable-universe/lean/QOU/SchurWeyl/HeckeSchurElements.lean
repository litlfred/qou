import QOU.SchurWeyl.HeckeSymmetricAlgebra
import QOU.SchurWeyl.MolienSymmetrisingTrace

/-!
# QOU.SchurWeyl.HeckeSchurElements — `τ = Σ_λ χ_λ / c_λ`

The symmetrising trace `τ = symTrace` of `H_{m+1}(q)` (the `T_1`-coefficient, defined over any
commutative ring in `HeckeSymmetricAlgebra`) decomposes over the irreducible seminormal
characters `χ_λ` with weights `1 / c_λ`, where the **Schur element** is

```
c_λ(Q) = Q^{−n(λ)} · ∏_{x ∈ λ} (1 − Q^{h(x)}) / (1 − Q),      Q = q²,
```

i.e. `c_λ = 1 / M_λ` for the Molien weight `M_λ`.

## Main results

* `schurElt_eq` — the closed form of `c_λ` (generic field, no hypotheses).
* `schurElt_ne_zero` — `c_λ ≠ 0` when `Q ≠ 0` is not a root of unity.
* `molien_eq_symTrace` — the Molien-weighted seminormal trace **is** `τ` (`ℝ`, generic `q`).
* `symTrace_eq_sum_schur` — `τ(x) = Σ_{|λ| = m+1} χ_λ(x) / c_λ`.

## Proof

`MolienSymmetrisingTrace` shows the Molien-weighted seminormal trace is a Markov trace with
`z = 0`; `HeckeSymmetricAlgebra.MarkovTraceFamily.tr_eq_symTrace` shows every such trace is `τ`.
The rest is `c_λ⁻¹ = M_λ`.

## Scope

The **weight** side (`schurElt`, its closed form and nonvanishing) is over a generic field.  The
**decomposition** is over `ℝ` at `q ≠ 0` not a root of unity, because the seminormal
representations in the corpus are built only there.  `τ` itself, and its product formula,
cyclicity and nondegeneracy, are over any commutative ring (`HeckeSymmetricAlgebra`); the
real-`q` restriction belongs to the characters, not to `τ`.

## Base ring (§7c)

Generic `[Field F]` for `schurElt`; `ℝ` only where the seminormal characters are used.

LaTeX label: `thm:hecke-schur-elements`

-- Ref: [geckpfeiffer2000] https://global.oup.com/academic/product/9780198502500 (Thm. 7.2.6 and §10.5: Schur elements of the generic Iwahori–Hecke algebra of type A)
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.QBeta.WenzlWeight

section Generic

variable {F : Type*} [Field F]

/-- The **Schur element** `c_λ(Q) = (M_λ(Q))⁻¹`. -/
noncomputable def schurElt (Q : F) (μ : YoungDiagram) : F := (molienWeight Q μ)⁻¹

/-- **Closed form**: `c_λ = Q^{−n(λ)} ∏_x (1 − Q^{h(x)}) / (1 − Q)`. -/
theorem schurElt_eq (Q : F) (μ : YoungDiagram) :
    schurElt Q μ = (∏ x ∈ μ.cells, (1 - Q ^ hook μ x) / (1 - Q)) / Q ^ nPart μ := by
  rw [schurElt, molienWeight, mul_inv, ← Finset.prod_inv_distrib, div_eq_inv_mul]
  congr 1
  exact Finset.prod_congr rfl fun x _ => inv_div _ _

/-- Every cell has hook length at least `1`. -/
theorem one_le_hook {μ : YoungDiagram} {x : ℕ × ℕ} (hx : x ∈ μ.cells) : 1 ≤ hook μ x := by
  have h1 : x.2 < μ.rowLen x.1 := μ.mem_iff_lt_rowLen.mp hx
  have h2 : x.1 < μ.colLen x.2 := μ.mem_iff_lt_colLen.mp hx
  unfold hook
  omega

theorem molienWeight_ne_zero (Q : F) (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (μ : YoungDiagram) : molienWeight Q μ ≠ 0 := by
  have hpow : ∀ k : ℕ, 1 ≤ k → 1 - Q ^ k ≠ 0 := by
    intro k hk h
    have := hgen k (by exact_mod_cast (by omega : k ≠ 0))
    rw [zpow_natCast] at this
    exact this (sub_eq_zero.mp h).symm
  refine mul_ne_zero (pow_ne_zero _ hQ0) (Finset.prod_ne_zero_iff.mpr fun x hx => ?_)
  exact div_ne_zero (by simpa using hpow 1 le_rfl) (hpow _ (one_le_hook hx))

/-- `c_λ ≠ 0` when `Q ≠ 0` is not a root of unity. -/
theorem schurElt_ne_zero (Q : F) (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (μ : YoungDiagram) : schurElt Q μ ≠ 0 :=
  inv_ne_zero (molienWeight_ne_zero Q hQ0 hgen μ)

end Generic

namespace SeminormalRep

/-- **The Molien trace is the symmetrising trace** `τ`. -/
theorem molien_eq_symTrace (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : wtraceW q hq0 hq2 (molienWeight (q ^ 2)) m = HeckeCoset.symTrace q q⁻¹ m := by
  rw [← molienMarkovTrace_tr q hq0 hq2]
  exact HeckeCoset.MarkovTraceFamily.tr_eq_symTrace q q⁻¹ _ m

/-- **Schur-element decomposition**: `τ(x) = Σ_{|λ| = m+1} χ_λ(x) / c_λ(q²)`. -/
theorem symTrace_eq_sum_schur (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (x : Hecke ℝ q q⁻¹ m) :
    HeckeCoset.symTrace q q⁻¹ m x
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          (seminormalRep q hq0 hq2 m ν.2 x).trace / schurElt (q ^ 2) ν.1 := by
  rw [← molien_eq_symTrace q hq0 hq2 m, wtraceW_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [schurElt, div_inv_eq_mul, mul_comm]

end SeminormalRep
end QOU.SchurWeyl
