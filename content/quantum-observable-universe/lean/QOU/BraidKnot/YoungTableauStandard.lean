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
* `fDimSkew` — the skew SYT dimension count `f^{outer/inner}`.
* `mu21` — the hook shape `(2,1)`.
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
`outer / inner`. -/
noncomputable def fDimSkew (outer inner : YoungDiagram) : ℕ :=
  Nat.card (SkewStandardYoungTableau outer inner)

/-! ## The shape `(2,1)` -/

/-- The Young diagram of shape `(2, 1)` — the smallest hook, with `f^{(2,1)} = 2`
and `|(2,1)|! = 6`. -/
def mu21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)

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
Stated in the cast-clean form `3 · (Σ …) = k!`, valid for `k ≥ |μ| = 3`. -/
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
