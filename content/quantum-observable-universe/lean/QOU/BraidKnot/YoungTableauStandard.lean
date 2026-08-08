/-
# Skew standard Young tableaux + the keystone C8 corollary

This file **reuses** the canonical in-repo standard-Young-tableau infrastructure
rather than redefining it:

* `QOU.Mathlib.StandardYoungTableau` / `QOU.Mathlib.numStandardYoungTableaux`
  (`QOU/Mathlib/StandardYoungTableau.lean`) — the `SemistandardYoungTableau`-refinement
  with a `Set.BijOn` filling, proving strict rows (`row_strict`), `injOn_cells`, a
  `Finite` instance, and the count `#SYT(μ) = Nat.card (StandardYoungTableau μ)`.
* `QOU.Mathlib.partitionShape` / `QOU.Mathlib.dimSYT`
  (`QOU/Mathlib/RSKBurnsideTarget.lean`) — the partition → `YoungDiagram` map (via
  `ofRowLens` of the weakly-decreasing sorted parts) and `dimSYT p := #SYT(partitionShape p)`,
  together with the `RSKBurnsideHolds` target `∑_{p⊢n} dim(p)² = n!`.

It therefore no longer defines its own `StandardYoungTableau`, `fDim`, or
`ydOfPartition`; those were duplicates of the canonical, superior versions above.

## Scope (honest)

What remains here is genuinely new — the canonical infra has **no** skew tableaux
and the C8 corollary is `KeystoneC8SuperExpBound`-specific:

* `SkewStandardYoungTableau` — skew SYT (fillings of `outer.cells \ inner.cells` by
  `{0,…,|diff|−1}`, strictly increasing along rows and columns among the skew cells);
  Mathlib and the canonical `QOU.Mathlib` SYT both lack this.
* `fDimSkew` — the skew SYT dimension count `f^{outer/inner}`, **guarded on
  `inner ≤ outer`**; see below.
* `mu21` — the hook shape `(2,1)`; `row3` — the shape `(3)`, the witness of
  `skewSYT_nonempty_of_not_le`.
* `involutionNumber_pos` — a genuine, fully proved positivity helper
  (`involutionNumber` lives in the imported `KeystoneC8SuperExpBound`).
* `c8_superexp` — an **unconditional** corollary of the sibling arithmetic core
  `c8_lower_bound`, expressed over the canonical `dimSYT` / `partitionShape`; its only
  gaps are the three cited RSK identities below.

The three cited `sorry`s (`branching_two_one`, `skew_le_straight`,
`sum_dimSYT_eq_involution`) are the classical Standard-Young-Tableau counting facts
Mathlib cannot yet prove — siblings of the canonical `QOU.Mathlib.RSKBurnsideHolds`
target, all discharged by the RSK correspondence (the open P1–P5 program
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`). Each states the
real proposition and carries a `-- Ref:` to Sagan.

## The containment guard on `fDimSkew` (was: a false statement behind a `sorry`)

`SkewStandardYoungTableau outer inner` fills the set difference
`outer.cells \ inner.cells`, and imposes **no** containment `inner ⊆ outer`.  That
difference stays inhabited when `inner ⊄ outer`, so the raw
`Nat.card (SkewStandardYoungTableau outer inner)` is *not* the classical skew
count `f^{outer/inner}`, which is `0` off containment.  `fDimSkew` therefore
guards on `inner ≤ outer`, and `skewSYT_nonempty_of_not_le` machine-proves that
the guard is necessary rather than defensive.

Unguarded, `branching_two_one` was **false, not merely open** — already at
`k = 3`, where the shapes `(3)` and `(1,1,1)` each contribute a spurious `1` and
`3 · 4 = 12 ≠ 6 = 3!`.  A `sorry` in front of a false proposition is worse than an
open gap, so the definition is fixed rather than the statement weakened; guarded,
the identity checks out at `k = 3` and `k = 4` (arithmetic in the
`skewSYT_nonempty_of_not_le` docstring).

Base ring `ℝ` appears only in the C8 corollary (it consumes the archimedean
`c8_lower_bound`); the tableau infrastructure itself is entirely over `ℕ`
(AGENTS.md §7c).

-- Ref: [sagan2001] Sagan, The Symmetric Group, §3–4 (SYT, RSK, branching)
-/
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.SetTheory.Cardinal.Finite
import QOU.Mathlib.RSKBurnsideTarget
import QOU.BraidKnot.KeystoneC8SuperExpBound

namespace QOU.BraidKnot.YoungTableauStandard

open Finset
open QOU.BraidKnot.KeystoneC8SuperExpBound
open QOU.Mathlib

/-! ## Skew standard Young tableaux (genuinely new — canonical infra lacks these) -/

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

/-- `f^{outer/inner}` — the number of skew standard Young tableaux of shape
`outer / inner`.

**The containment guard is load-bearing, not defensive.**  The classical skew
count is `0` unless `inner ⊆ outer` (the skew shape `λ/μ` is undefined
otherwise), but `SkewStandardYoungTableau` imposes no containment: it fills the
set difference `outer.cells \ inner.cells`, which stays perfectly well-behaved —
and inhabited — when `inner ⊄ outer`.  `skewSYT_nonempty_of_not_le` below exhibits
that, and records the arithmetic showing that the unguarded count makes
`branching_two_one` false. -/
noncomputable def fDimSkew (outer inner : YoungDiagram) : ℕ := by
  classical
  exact if inner ≤ outer then Nat.card (SkewStandardYoungTableau outer inner) else 0

/-! ## The shape `(2,1)` -/

/-- The Young diagram of shape `(2, 1)` — the smallest hook, with `f^{(2,1)} = 2`
and `|(2,1)|! = 6`. -/
def mu21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)

/-- The single-row shape `(3)`.  Present only as the witness shape of
`skewSYT_nonempty_of_not_le`: it is the smallest partition of `3` that does *not*
contain `(2,1)`. -/
def row3 : YoungDiagram := YoungDiagram.ofRowLens [3] (by decide)

/-- **Why `fDimSkew` must guard on containment** (machine-proved, no `sorry`).

`(2,1) ⊄ (3)`, yet `SkewStandardYoungTableau (3) (2,1)` is inhabited: the skew
region `(3).cells \ (2,1).cells` is the single cell `(0,2)`, both strictness
fields are vacuous there, and the all-zero filling satisfies `zeros` and
`content`.  So the *raw* `Nat.card` is `1` where the classical `f^{(3)/(2,1)}`
is `0`.

Unguarded, `branching_two_one` would be **false already at `k = 3`**: the three
partitions of `3` contribute `f^{(3)}·1 + f^{(2,1)}·1 + f^{(1,1,1)}·1
= 1 + 2 + 1 = 4` (each raw skew count is `1`, the shapes `(3)` and `(1,1,1)`
contributing spuriously), and `3 · 4 = 12 ≠ 6 = 3!`.  Guarded, only `(2,1)`
survives and the sum is `2`, with `3 · 2 = 6 = 3!` ✓ — and at `k = 4` the
surviving shapes `(3,1), (2,2), (2,1,1)` give `3·1 + 2·1 + 3·1 = 8` with
`3 · 8 = 24 = 4!` ✓. -/
theorem skewSYT_nonempty_of_not_le :
    ¬ mu21 ≤ row3 ∧ Nonempty (SkewStandardYoungTableau row3 mu21) := by
  constructor
  · rw [← YoungDiagram.cells_subset_iff]
    intro hsub
    have hmem : ((1, 0) : ℕ × ℕ) ∈ mu21.cells := by
      simp [mu21, YoungDiagram.mem_ofRowLens]
    have hnot : ((1, 0) : ℕ × ℕ) ∉ row3.cells := by
      simp [row3, YoungDiagram.mem_ofRowLens]
    exact hnot (hsub hmem)
  · refine ⟨⟨fun _ _ => 0, ?_, ?_, fun _ => rfl, ?_⟩⟩
    · -- rows: `(i, j₂) ∈ (3)` forces `i = 0` and `j₂ < 3`, so `j₁ < j₂ ≤ 2 < 2`
      -- puts `(0, j₁)` inside `(2,1)` after all — contradicting the hypothesis
      intro i j₁ j₂ hj hout hin
      exfalso
      apply hin
      simp only [row3, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add] at hout
      obtain ⟨hi, hj₂⟩ := hout
      have hi0 : i = 0 := by omega
      subst hi0
      simp only [List.getElem_cons_zero] at hj₂
      simp only [mu21, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add, List.getElem_cons_zero]
      exact ⟨by norm_num, by omega⟩
    · -- columns: `(i₂, j) ∈ (3)` forces `i₂ = 0`, and nothing is `< 0`
      intro i₁ i₂ j hi hout _
      exfalso
      simp only [row3, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add] at hout
      obtain ⟨hi₂, -⟩ := hout
      omega
    · -- the skew region is the single cell `(0,2)`; both sides are `{0}`
      decide

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
proposition over the canonical `dimSYT` / `partitionShape` / skew count; the fill
is `sorry` with a `-- Ref:` to Sagan. They are siblings of the canonical
`QOU.Mathlib.RSKBurnsideHolds` target — all discharged by the RSK correspondence
(open P1–P5 program `docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`). -/

/-- **Classical branching** `Σ_{λ⊢k} f^λ · f^{λ/(2,1)} = k! · f^{(2,1)} / |(2,1)|!`
at `μ = (2,1)` (where `f^{(2,1)} = 2`, `|(2,1)|! = 6`, so the RHS is `k!/3`).
Stated in the cast-clean form `3 · (Σ …) = k!`, valid for `k ≥ |μ| = 3`.

Representation-theoretically this is the dimension of
`Ind_{S_m × S_{k−m}}^{S_k}(S^μ ⊠ ℚ[S_{k−m}])` counted two ways: `k!·f^μ/m!` by the
index-times-dimension formula, and `Σ_λ f^{λ/μ} f^λ` by `s_μ·s_1^{k−m} =
Σ_λ f^{λ/μ} s_λ`.

**Only true because `fDimSkew` guards on containment** — the sum must skip every
`λ` not containing `(2,1)`.  See `skewSYT_nonempty_of_not_le`, which exhibits the
counterexample the guard removes and checks this identity at `k = 3, 4`. -/
theorem branching_two_one (k : ℕ) (hk : 3 ≤ k) :
    3 * (∑ p : Nat.Partition k,
        dimSYT p * fDimSkew (partitionShape p) mu21) = Nat.factorial k := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, Thm 3.10.2 (branching rule)
  sorry

/-- **Skew SYT inject into straight SYT.** `Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ_{λ⊢k} f^λ`,
the latter being the involution number `I(k)` (RSK for involutions, below). -/
theorem skew_le_straight (k : ℕ) :
    (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21)
      ≤ (∑ p : Nat.Partition k, dimSYT p) := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, §4 (skew tableaux, Jacobi–Trudi)
  sorry

/-- **RSK for involutions.** `Σ_{λ⊢k} f^λ = I(k)`, the number of involutions in
`S_k` — the `q = 1` value of the QOU na-Stokes period. -/
theorem sum_dimSYT_eq_involution (k : ℕ) :
    (∑ p : Nat.Partition k, dimSYT p) = involutionNumber k := by
  -- Ref: [sagan2001] Sagan, The Symmetric Group, §3.1 (RSK ⇒ involutions)
  sorry

/-! ## The unconditional C8 super-exponential corollary -/

/-- **C8 super-exponential lower bound (unconditional modulo the three RSK
`sorry`s above).** Instantiating the sibling arithmetic core `c8_lower_bound`
with `f = f^λ = dimSYT`, `g = f^{λ/(2,1)}`, `kfac = k!`, `Ik = I(k)`, and
discharging its inputs by casting `branching_two_one` (A) and `skew_le_straight` +
`sum_dimSYT_eq_involution` (C) to `ℝ`, the Plancherel-weighted branched sum obeys

    k! / (9·I(k))  ≤  (Σ_{λ⊢k} (f^λ)² f^{λ/(2,1)}) / k!.

All positivity and arithmetic are proved here; only (A)/(C) are RSK-supplied. -/
theorem c8_superexp (k : ℕ) (hk : 3 ≤ k) :
    (Nat.factorial k : ℝ) / (9 * (involutionNumber k : ℝ))
      ≤ (∑ p : Nat.Partition k,
            (dimSYT p : ℝ) ^ 2 * (fDimSkew (partitionShape p) mu21 : ℝ))
          / (Nat.factorial k : ℝ) := by
  classical
  have hIkpos : 0 < involutionNumber k := involutionNumber_pos k
  -- (A) Σ f g = k!/3, from `3 · Σ = k!` cast to ℝ.
  have hA : ∑ p : Nat.Partition k,
      (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ)
        = (Nat.factorial k : ℝ) / 3 := by
    have hnat := branching_two_one k hk
    have hc : (3 : ℝ) * (∑ p : Nat.Partition k,
        (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ))
        = (Nat.factorial k : ℝ) := by exact_mod_cast hnat
    linarith [hc]
  -- (C) Σ g ≤ I(k), from skew↪straight and RSK-for-involutions cast to ℝ.
  have hC : ∑ p : Nat.Partition k, (fDimSkew (partitionShape p) mu21 : ℝ)
        ≤ (involutionNumber k : ℝ) := by
    have hnat : (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21)
        ≤ involutionNumber k := by
      rw [← sum_dimSYT_eq_involution k]; exact skew_le_straight k
    exact_mod_cast hnat
  exact c8_lower_bound (Finset.univ : Finset (Nat.Partition k))
    (fun p => (dimSYT p : ℝ))
    (fun p => (fDimSkew (partitionShape p) mu21 : ℝ))
    (Nat.factorial k : ℝ) (involutionNumber k : ℝ)
    (fun i _ => by positivity)
    (by exact_mod_cast Nat.factorial_pos k)
    (by exact_mod_cast hIkpos)
    hA hC

end QOU.BraidKnot.YoungTableauStandard
