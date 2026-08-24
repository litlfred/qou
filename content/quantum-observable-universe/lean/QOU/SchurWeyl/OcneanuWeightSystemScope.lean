import QOU.SchurWeyl.MarkovNormalisation
import QOU.QBeta.WenzlWeightVanishing

/-!
# QOU.SchurWeyl.OcneanuWeightSystemScope — why the identification does not discharge `IsOcneanuWeightSystem`

`MarkovTraceInstance` proves that `ocneanuWeight` at convention D **is** the Markov trace.  The
natural next thought is that this discharges the corpus's conditional-class carrier of Wenzl's
theorem, `QBeta.WenzlWeight.IsOcneanuWeightSystem`, letting downstream statements drop their
`[IsOcneanuWeightSystem …]` hypothesis.  **It does not**, and this file proves why, so that nobody
spends a session trying.

## The mismatch

The class asks for a **single** normaliser:

```
weight_eq_schurPrincipal : ∃ Z, Z ≠ 0 ∧ ∀ μ, y μ = schurPrincipal r Q μ / Z
```

`Z` is quantified *outside* `∀ μ`.  The true relation, `ocneanuWeight_conventionD_eq_schurPrincipal`,
carries a normaliser that depends on the **size** of `μ`:

```
ocneanuWeight q z_D μ = schurPrincipal 2 (q²) μ / (q² + 1)^{|μ|}
```

and those are incompatible unless `q² + 1 = 1`.  `not_isOcneanuWeightSystem` is that argument:
evaluate at `⊥` (where `|μ| = 0` and the weight is `1`) to force `Z = 1`, then at a single cell
(where `|μ| = 1` and the weight is nonzero) to force `q² + 1 = 1`, hence `q = 0`.

## Scope of this negative result — read before quoting it

This is a **structural exclusion** in the sense of AGENTS.md §"Before declaring refuted": it rests
on a proved invariant (the bridge, plus `ocneanuWeight_bot` and the one-cell non-vanishing), not on
a failed search.  But it is narrow, and two things it does **not** say:

* **It does not say the class is wrong.**  For an *unnormalised* `y` a single `Z` is exactly right
  — take `Z = 1` and `y = schurPrincipal r Q`.  The class is inhabitable; it is just not inhabited
  by a per-size-normalised weight family.
* **It does not say the corpus is inconsistent.**  What it shows is a gap between the class's
  *prose* — the file header describes the weights as "normalised so that `Σ_λ f^λ y_λ = 1`" — and
  its *fields*, which encode no normalisation and whose `Z` cannot vary with `|μ|`.  Per-size
  normalisation is proved for `ocneanuWeight` (`sum_dim_weight_eq_one`), so the two cannot both
  hold of one weight family.

The resolution is an authoring decision for whoever owns that class — index `Z` by the size, or
drop the normalisation from the prose — and is deliberately **not** made here.

## Base ring (§7c)

`ℝ`, inherited; `q ≠ 0`, `q² + 1 ≠ 0`, and the root-of-unity exclusion `∀ k ≠ 0, (q²)^k ≠ 1`.

LaTeX label: `thm:ocneanu-weight-system-scope`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram QOU.QBeta.WenzlWeight

/-- The single-cell diagram has weight `1 / 1`… we only need it nonzero. -/
theorem ocneanuWeight_oneCell_ne_zero (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow 1 0 (by omega)) ≠ 0 := by
  intro hz
  have h := (ocneanuWeight_conventionD_eq_zero_iff q hq hq21 hgen (twoRow 1 0 (by omega))).mp hz
  rw [colLen_twoRow] at h
  simp at h

/-- **The corpus's normalised weight cannot satisfy `IsOcneanuWeightSystem` as stated.**
The class asks for a **single** normaliser `Z`, independent of the diagram; the bridge supplies
`(q²+1)^{|μ|}`, which is not. -/
theorem not_isOcneanuWeightSystem (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1) :
    ¬ IsOcneanuWeightSystem (q ^ 2) (q ^ 3 / (q ^ 2 + 1)) 2
        (ocneanuWeight q (q ^ 3 / (q ^ 2 + 1))) := by
  rintro ⟨-, Z, hZ, hy⟩
  -- at the empty diagram: `W = 1`, `|μ| = 0`, so `Z = 1`
  have hbotW : ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (⊥ : YoungDiagram) = 1 :=
    ocneanuWeight_bot q _
  have hbotS : schurPrincipal 2 (q ^ 2) (⊥ : YoungDiagram)
      = (q ^ 2 + 1) ^ (⊥ : YoungDiagram).cells.card
        * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (⊥ : YoungDiagram) := by
    rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21]
    field_simp
  have hZ1 : Z = 1 := by
    have := hy (⊥ : YoungDiagram)
    rw [hbotW, hbotS, hbotW, YoungDiagram.cells_bot] at this
    simp only [Finset.card_empty, pow_zero, mul_one] at this
    field_simp at this
    exact this
  -- at a single cell: `|μ| = 1`, so `Z = q² + 1`
  have hone : (twoRow 1 0 (by omega)).cells.card = 1 := by rw [card_twoRow]
  have hWne := ocneanuWeight_oneCell_ne_zero q hq hq21 hgen
  have hS : schurPrincipal 2 (q ^ 2) (twoRow 1 0 (by omega))
      = (q ^ 2 + 1) ^ (1 : ℕ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow 1 0 (by omega)) := by
    rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21, hone]
    field_simp
  have h2 := hy (twoRow 1 0 (by omega))
  rw [hS, hZ1, div_one, pow_one] at h2
  have hq2 : (q : ℝ) ^ 2 = 0 := by
    field_simp at h2
    linarith
  exact hq (pow_eq_zero_iff (n := 2) (by omega) |>.mp hq2)

end QOU.SchurWeyl
