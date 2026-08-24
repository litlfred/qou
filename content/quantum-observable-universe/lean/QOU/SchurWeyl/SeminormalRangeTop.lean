import QOU.SchurWeyl.SeminormalRange
import QOU.SchurWeyl.SytSwapTransport
import QOU.SchurWeyl.OffDiagNonvanishing

/-!
# QOU.SchurWeyl.SeminormalRangeTop — the seminormal representation is onto

**The irreducibility half of SW-5** (bean `qou-jfr8`), in the range form
`AlgHom.range (seminormalRep …) = ⊤` that the Wedderburn assembly consumes.  Surjectivity onto
the full matrix block *is* irreducibility here, and stating it this way avoids standing up a
module-over-the-algebra structure only to say "no proper submodule".

## The assembly

Five facts, each already proved, compose along a chain:

| fact | supplies |
|---|---|
| `single_self_mem_range` | the diagonal units, via the simple `q`-Jucys–Murphy spectrum |
| `syt_swapStep_connected` | a chain of admissible swaps between any two tableaux |
| `offDiag_axialDist_ne_zero` | each step's off-diagonal entry is nonzero |
| `single_mem_range_of_entry_ne_zero` | a nonzero entry promotes to a matrix unit |
| `eq_top_of_single_mem` | the units generate everything |

The third is the one that was missing until now, and its absence was not visible from the plan:
`offDiag q (-1) = 0`, so an admissible swap at distance `−1` would contribute a *vanishing* entry
and the promotion step would have nothing to consume.  `TableauCells.two_le_natAbs_axialDist`
rules that out by showing `±1` happens only in the same-row / same-column cases, which
admissibility excludes.

Note the induction composes units as a **three-factor sandwich**
`single c b 1 * single b T 1 * single T T 1`, which `Matrix.single_mul_mul_single` evaluates
directly.  The two-factor identity `single a b 1 * single b c 1 = single a c 1` is not in Mathlib
at this pin and is not needed.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

variable {μ : YoungDiagram}

/-- **One admissible swap step promotes to an off-diagonal matrix unit.**  The generator `σ_k`
carries the entry `offDiag q (axialDist T k)` at `(s_k·T, T)`, which
`offDiag_axialDist_ne_zero` makes nonzero. -/
theorem single_mem_range_of_swapStep (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) {T T' : StandardYoungTableau μ} (h : SwapStep T T') :
    Matrix.single T' T (1 : ℝ) ∈ (seminormalRep q hq0 hq2 n hN).range := by
  obtain ⟨k, hk, hkn, hadm, rfl⟩ := h
  have hkle : k ≤ n := by omega
  have hk1 : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hk2 : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hne : swapTableau T k hk hkn hadm ≠ T := swapTableau_ne T hk hkn hadm
  set i : Fin n := ⟨k - 1, by omega⟩ with hidef
  have hik : (i : ℕ) + 1 = k := by simp only [hidef]; omega
  have hgen : seminormalGen q n hN i = genMat q k hk hkn := by
    simp only [seminormalGen]
    congr 1
  have hentry : seminormalRep q hq0 hq2 n hN (Hecke.σ ℝ q q⁻¹ n i)
      (swapTableau T k hk hkn hadm) T ≠ 0 := by
    rw [seminormalRep_σ, hgen, genMat_swap q k hk hkn hadm hne]
    exact offDiag_axialDist_ne_zero q hq0 hq2 T hk1 hk2 hadm
  exact single_mem_range_of_entry_ne_zero q hq0 hq2 n hN hentry

/-- **Every matrix unit lies in the image.**  Induct along the connectivity chain: the diagonal
units are already there, and each admissible step composes on a new off-diagonal unit. -/
theorem single_mem_range (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (T T' : StandardYoungTableau μ) :
    Matrix.single T' T (1 : ℝ) ∈ (seminormalRep q hq0 hq2 n hN).range := by
  have hchain : Relation.ReflTransGen (SwapStep (μ := μ)) T T' := syt_swapStep_connected T T'
  induction hchain with
  | refl => exact single_self_mem_range q hq0 hq2 n hN T
  | @tail b c _ hbc ih =>
    have hstep := single_mem_range_of_swapStep q hq0 hq2 n hN hbc
    have hprod : Matrix.single c b (1 : ℝ) * Matrix.single b T 1 * Matrix.single T T 1
        = Matrix.single c T 1 := by
      rw [Matrix.single_mul_mul_single]
      simp
    rw [← hprod]
    exact mul_mem (mul_mem hstep ih) (single_self_mem_range q hq0 hq2 n hN T)

/-- **The seminormal representation is surjective onto the matrix block.**

`ρ_λ : H_n(q) →ₐ[ℝ] M_{#SYT λ}(ℝ)` hits *everything* — the irreducibility statement SW-7 consumes.
Every matrix unit is in the image (`single_mem_range`), and the units generate. -/
theorem seminormalRep_range_eq_top (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    (seminormalRep q hq0 hq2 n hN).range = ⊤ :=
  eq_top_of_single_mem _ (fun T' T => single_mem_range q hq0 hq2 n hN T T')

end QOU.SchurWeyl
