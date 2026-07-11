/-
# Standard Young Tableaux — the SYT infrastructure Mathlib lacks

Mathlib has `YoungDiagram` and `SemistandardYoungTableau`, but **no**
`StandardYoungTableau`, no skew SYT, and no `f^λ` dimension count. This file
supplies that Tier-1 infrastructure so the keystone `W_λ` C8 super-exponential
bound (`QOU.BraidKnot.KeystoneC8SuperExpBound`) can be discharged
*unconditionally modulo the three classical RSK identities*.

## Scope (honest)

* `StandardYoungTableau` / `SkewStandardYoungTableau` — new structures (fillings
  by `{0,…,|μ|−1}`, strictly increasing along rows and columns).
* `fDim` / `fDimSkew` — the SYT dimension counts `f^μ`, `f^{outer/inner}`.
* `entry_lt_card` — a genuine, fully proved non-vacuity lemma about the fill.
* `involutionNumber_pos` — a genuine, fully proved positivity helper.
* `c8_superexp` — an **unconditional** corollary of the sibling arithmetic core;
  its only gaps are the three cited RSK identities.

The **only** `sorry`s are the three classical Standard-Young-Tableau counting
facts Mathlib cannot yet prove (branching, skew↪straight, RSK-for-involutions).
Each states the real proposition and carries a `-- Ref:` to Sagan.

Base ring `ℝ` appears only in the C8 corollary (it consumes the archimedean
`c8_lower_bound`); the tableau infrastructure itself is entirely over `ℕ`
(AGENTS.md §7c).

-- Ref: [sagan2001] Sagan, The Symmetric Group, §3–4 (SYT, RSK, branching)
-/
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Multiset.Sort
import Mathlib.SetTheory.Cardinal.Finite
import QOU.BraidKnot.KeystoneC8SuperExpBound

namespace QOU.BraidKnot.YoungTableauStandard

open Finset
open QOU.BraidKnot.KeystoneC8SuperExpBound

/-! ## Standard Young tableaux -/

/-- A **standard Young tableau** of shape `μ` is a filling of the cells of `μ` by
the natural numbers `{0, …, |μ|−1}`, each used exactly once, strictly increasing
left-to-right along rows and top-to-bottom along columns. Represented as an
unrestricted `entry : ℕ → ℕ → ℕ` that vanishes off `μ`. -/
structure StandardYoungTableau (μ : YoungDiagram) where
  /-- `entry i j` is the value in cell `(i, j)`. -/
  entry : ℕ → ℕ → ℕ
  /-- Rows are strictly increasing (left to right). -/
  row_strict : ∀ {i j₁ j₂ : ℕ}, j₁ < j₂ → (i, j₂) ∈ μ → entry i j₁ < entry i j₂
  /-- Columns are strictly increasing (top to bottom). -/
  col_strict : ∀ {i₁ i₂ j : ℕ}, i₁ < i₂ → (i₂, j) ∈ μ → entry i₁ j < entry i₂ j
  /-- `entry` vanishes outside `μ`. -/
  zeros : ∀ {i j : ℕ}, (i, j) ∉ μ → entry i j = 0
  /-- The entries on the cells are exactly `{0, …, |μ|−1}`. -/
  content : μ.cells.image (fun c => entry c.1 c.2) = Finset.range μ.cells.card

/-- A **skew standard Young tableau** of shape `outer / inner` is a filling of the
skew cells `outer.cells \ inner.cells` by `{0, …, |diff|−1}`, each used once,
strictly increasing along rows and columns among the skew (non-`inner`) cells. -/
structure SkewStandardYoungTableau (outer inner : YoungDiagram) where
  /-- `entry i j` is the value in cell `(i, j)`. -/
  entry : ℕ → ℕ → ℕ
  /-- Rows are strictly increasing among the skew cells. -/
  row_strict : ∀ {i j₁ j₂ : ℕ}, j₁ < j₂ → (i, j₂) ∈ outer → (i, j₁) ∉ inner →
    entry i j₁ < entry i j₂
  /-- Columns are strictly increasing among the skew cells. -/
  col_strict : ∀ {i₁ i₂ j : ℕ}, i₁ < i₂ → (i₂, j) ∈ outer → (i₁, j) ∉ inner →
    entry i₁ j < entry i₂ j
  /-- `entry` vanishes off the skew region (on `inner`, or outside `outer`). -/
  zeros : ∀ {i j : ℕ}, (i, j) ∈ inner ∨ (i, j) ∉ outer → entry i j = 0
  /-- The entries on the skew cells are exactly `{0, …, |diff|−1}`. -/
  content : (outer.cells \ inner.cells).image (fun c => entry c.1 c.2)
    = Finset.range (outer.cells \ inner.cells).card

/-! ## SYT dimensions `f^μ` and `f^{outer/inner}` -/

/-- `f^μ` — the number of standard Young tableaux of shape `μ`. -/
noncomputable def fDim (μ : YoungDiagram) : ℕ := Nat.card (StandardYoungTableau μ)

/-- `f^{outer/inner}` — the number of skew standard Young tableaux of shape
`outer / inner`. -/
noncomputable def fDimSkew (outer inner : YoungDiagram) : ℕ :=
  Nat.card (SkewStandardYoungTableau outer inner)

/-! ## A genuine non-vacuity lemma (fully proved) -/

/-- **Every entry of a standard Young tableau is `< |μ|`.** This is real content
extracted from the `content` field: the entry on any cell lies in the image of
the fill, which equals `Finset.range μ.cells.card`. It witnesses that
`StandardYoungTableau` is not an empty marker. -/
theorem entry_lt_card {μ : YoungDiagram} (T : StandardYoungTableau μ) {c : ℕ × ℕ}
    (hc : c ∈ μ.cells) : T.entry c.1 c.2 < μ.cells.card := by
  have hmem : T.entry c.1 c.2 ∈ μ.cells.image (fun c => T.entry c.1 c.2) :=
    Finset.mem_image_of_mem (fun c => T.entry c.1 c.2) hc
  rw [T.content] at hmem
  exact Finset.mem_range.mp hmem

/-! ## The shape `(2,1)` and partition → diagram -/

/-- The Young diagram of shape `(2, 1)` — the smallest hook, with `f^{(2,1)} = 2`
and `|(2,1)|! = 6`. -/
def mu21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)

/-- The Young diagram of a partition `p ⊢ k`: sort its parts weakly decreasing and
feed them to `YoungDiagram.ofRowLens`. -/
def ydOfPartition {k : ℕ} (p : Nat.Partition k) : YoungDiagram :=
  YoungDiagram.ofRowLens (p.parts.sort (· ≥ ·)) (Multiset.sort_sorted _ _)

/-! ## Involution-number positivity (fully proved) -/

/-- The involution numbers are strictly positive (`I(n) ≥ 1`). Needed as the C8
denominator `I(k)` must be positive for `k!/(9·I(k))` to be a finite lower
bound. -/
theorem involutionNumber_pos : ∀ n, 0 < involutionNumber n := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 ih2 =>
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    omega

/-! ## The three classical RSK-family identities (cited `sorry`)

These are the deep Standard-Young-Tableau counting facts that Mathlib does not
prove (no hook-length formula, no RSK correspondence). Each states the real
proposition; the fill is `sorry` with a `-- Ref:` to Sagan. -/

/-- **Classical branching** `Σ_{λ⊢k} f^λ · f^{λ/(2,1)} = k! · f^{(2,1)} / |(2,1)|!`
at `μ = (2,1)` (where `f^{(2,1)} = 2`, `|(2,1)|! = 6`, so the RHS is `k!/3`).
Stated in the cast-clean form `3 · (Σ …) = k!`, valid for `k ≥ |μ| = 3`. -/
theorem branching_two_one (k : ℕ) (hk : 3 ≤ k) :
    3 * (∑ p : Nat.Partition k,
        fDim (ydOfPartition p) * fDimSkew (ydOfPartition p) mu21) = Nat.factorial k := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, Thm 3.10.2 (branching rule)
  sorry

/-- **Skew SYT inject into straight SYT.** `Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ_{λ⊢k} f^λ`,
the latter being the involution number `I(k)` (RSK for involutions, below). -/
theorem skew_le_straight (k : ℕ) :
    (∑ p : Nat.Partition k, fDimSkew (ydOfPartition p) mu21)
      ≤ (∑ p : Nat.Partition k, fDim (ydOfPartition p)) := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, §4 (skew tableaux, Jacobi–Trudi)
  sorry

/-- **RSK for involutions.** `Σ_{λ⊢k} f^λ = I(k)`, the number of involutions in
`S_k` — the `q = 1` value of the QOU na-Stokes period. -/
theorem sum_fDim_eq_involution (k : ℕ) :
    (∑ p : Nat.Partition k, fDim (ydOfPartition p)) = involutionNumber k := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, §3.1 (RSK ⇒ involutions)
  sorry

/-! ## The unconditional C8 super-exponential corollary -/

/-- **C8 super-exponential lower bound (unconditional modulo the three RSK
`sorry`s above).** Instantiating the sibling arithmetic core `c8_lower_bound`
with `f = f^λ`, `g = f^{λ/(2,1)}`, `kfac = k!`, `Ik = I(k)`, and discharging its
inputs by casting `branching_two_one` (A) and `skew_le_straight` +
`sum_fDim_eq_involution` (C) to `ℝ`, the Plancherel-weighted branched sum obeys

    k! / (9·I(k))  ≤  (Σ_{λ⊢k} (f^λ)² f^{λ/(2,1)}) / k!.

All positivity and arithmetic are proved here; only (A)/(C) are RSK-supplied. -/
theorem c8_superexp (k : ℕ) (hk : 3 ≤ k) :
    (Nat.factorial k : ℝ) / (9 * (involutionNumber k : ℝ))
      ≤ (∑ p : Nat.Partition k,
            (fDim (ydOfPartition p) : ℝ) ^ 2 * (fDimSkew (ydOfPartition p) mu21 : ℝ))
          / (Nat.factorial k : ℝ) := by
  classical
  have hIkpos : 0 < involutionNumber k := involutionNumber_pos k
  -- (A) Σ f g = k!/3, from `3 · Σ = k!` cast to ℝ.
  have hA : ∑ p : Nat.Partition k,
      (fDim (ydOfPartition p) : ℝ) * (fDimSkew (ydOfPartition p) mu21 : ℝ)
        = (Nat.factorial k : ℝ) / 3 := by
    have hnat := branching_two_one k hk
    have hc : (3 : ℝ) * (∑ p : Nat.Partition k,
        (fDim (ydOfPartition p) : ℝ) * (fDimSkew (ydOfPartition p) mu21 : ℝ))
        = (Nat.factorial k : ℝ) := by exact_mod_cast hnat
    linarith [hc]
  -- (C) Σ g ≤ I(k), from skew↪straight and RSK-for-involutions cast to ℝ.
  have hC : ∑ p : Nat.Partition k, (fDimSkew (ydOfPartition p) mu21 : ℝ)
        ≤ (involutionNumber k : ℝ) := by
    have hnat : (∑ p : Nat.Partition k, fDimSkew (ydOfPartition p) mu21)
        ≤ involutionNumber k := by
      rw [← sum_fDim_eq_involution k]; exact skew_le_straight k
    exact_mod_cast hnat
  exact c8_lower_bound (Finset.univ : Finset (Nat.Partition k))
    (fun p => (fDim (ydOfPartition p) : ℝ))
    (fun p => (fDimSkew (ydOfPartition p) mu21 : ℝ))
    (Nat.factorial k : ℝ) (involutionNumber k : ℝ)
    (fun i _ => by positivity)
    (by exact_mod_cast Nat.factorial_pos k)
    (by exact_mod_cast hIkpos)
    hA hC

end QOU.BraidKnot.YoungTableauStandard
