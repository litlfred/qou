import QOU.Information.SkeinObservationBridge
import QOU.Information.SurrealBudgetGrade
import QOU.Information.CountingModuliGrade
import Mathlib.SetTheory.Ordinal.Arithmetic

/-!
# QOU.Information.SkeinSurrealGrade — the surreal-level (ω-grade) brick

The honest core of *"complexity ↔ surreal birthday/length"*, formalized
**sorry-free** as a **conditional whose hypothesis is the growth bound**
(formalize-first: the growth bound is the honest input, the grade gap is
*derived*).

## What this is — and is NOT

This module does **not** prove `P ≠ NP`, and adds nothing to the open
counting→decision transfer. It formalizes the strictly weaker, genuinely-true
sub-fact that the QOU horizon actually supports: **exponential-in-length
observation cost occupies a strictly higher transseries level (ω-grade) than
any polynomial budget.** See `docs/audits/2026-08-09-pneqnp-robustness-mathlib-infra.md`.

## The mathematics

* **Transseries level = ω-grade.** Berarducci–Mantova: the surreals are the
  universal transseries field; a growth function's *level* orders it against
  iterated exp/log (poly = level 0, exp = level 1). In the coarser ω-monomial
  grade the corpus uses, `nᵏ` has magnitude `ωᵏ` (finite) while `2ⁿ` exceeds
  every `ωᵏ`. That is exactly `SuperPolynomial` vs `PolyBounded`
  (`QOU.Information.SurrealBudgetGrade`): `ord_ω(2ⁿ) > ord_ω(nᵏ)` for all `k`.
  The `P ⊊ EXP` band-gap reads as this strict ω-grade inequality — proved
  sorry-free as `not_polyBounded_of_superPoly` (the "surreal squeeze").

* **`len` is the finite birthday shadow.** A finite braid word's surreal
  sign-expansion length is literally its `ℕ` length, and the birthday of a
  finite ordinal `n` is `n`. So `SkeinObservationSystem.len` is the *finite
  (birthday `< ω`, archimedean) shadow* of the surreal length. The exponential
  blow-up lives in the **cost as a function of** this level (`3^{len}`), never
  in the level of any single word (`birthdayShadow_lt_omega0`).

## The bricks (all sorry-free)

`level_gap` (the squeeze), `levelGeOne_of_exp_growth` (the conditional —
hypothesis = growth bound), the horizon-cost family
`horizonCostOfLen`/`horizonCostOfLen_levelGeOne`, and the corpus cross-check
`horizonCostOfLen_boundary_eq_physicalCost` recovering `physicalCost_superPoly`.

Base ring not applicable (ℕ-valued costs; `Ordinal` for the birthday shadow).

-- Ref: [leitner2026] quantum-observable-universe/information-theory — surreal/transseries level grading
-/

namespace QOU.Information

open SkeinObservationSystem

/-! ## The finite birthday shadow of the length filtration -/

/-- **Birthday shadow** of a state: the finite ordinal equal to its `ℕ`-valued
    length filtration. A finite braid word's surreal sign-expansion length is
    literally its `ℕ` length, and the birthday of a finite ordinal `n` is `n`,
    so `len` is the finite (archimedean, birthday `< ω`) shadow of the surreal
    length. -/
def SkeinObservationSystem.birthdayShadow {S : Type*} {V : Type*}
    (sys : SkeinObservationSystem S V) (P : S) : Ordinal :=
  (sys.len P : Ordinal)

/-- **A single state sits in the finite (archimedean) birthday band
    (sorry-free).**  Its birthday shadow is `< ω`: the exponential blow-up is
    in the *cost as a function of* the length, never in the length of one
    word. -/
theorem SkeinObservationSystem.birthdayShadow_lt_omega0 {S : Type*} {V : Type*}
    (sys : SkeinObservationSystem S V) (P : S) :
    sys.birthdayShadow P < Ordinal.omega0 := by
  unfold SkeinObservationSystem.birthdayShadow
  exact Ordinal.nat_lt_omega0 _

/-! ## Transseries levels of a cost-growth function -/

/-- **Level 0** — the polynomial (archimedean) band: `ord_ω(g) ≤ ord_ω(nᵏ)`.
    Poly is transseries level 0. -/
def LevelZero (g : ℕ → ℕ) : Prop := PolyBounded g

/-- **Level ≥ 1** — the exponential-or-higher band: `ord_ω(g) > ord_ω(nᵏ)` for
    every `k`. Exp is transseries level 1. -/
def LevelGeOne (g : ℕ → ℕ) : Prop := SuperPolynomial g

/-- **The level gap (sorry-free)** — the two transseries bands are disjoint: a
    level-≥1 function is not level-0. This is the ω-grade squeeze
    `ord_ω(cost) > ord_ω(budget)`, the honest machine-checked core of the
    `P ⊊ EXP` band separation. -/
theorem level_gap {g : ℕ → ℕ} (h : LevelGeOne g) : ¬ LevelZero g :=
  not_polyBounded_of_superPoly h

/-- **Exponential growth forces level ≥ 1 (sorry-free) — THE conditional.**
    The *hypothesis is the exponential growth bound* `2ⁿ ≤ g n`; the level-≥1
    grade is *derived* (formalize-first: the growth bound is the honest input).
    Routes through `superPoly_two_pow` (Mathlib little-o) lifted along `≤`. -/
theorem levelGeOne_of_exp_growth {g : ℕ → ℕ} (hgrow : ∀ n, 2 ^ n ≤ g n) :
    LevelGeOne g :=
  superPoly_two_pow.of_le hgrow

/-- **Exponential growth ⇒ no polynomial budget (sorry-free).**  Composition of
    the conditional with the level gap: an exponentially-growing cost is not
    polynomially bounded — the surreal `ord_ω(cost) > ord_ω(budget)` conclusion,
    with the growth bound as the sole hypothesis. -/
theorem not_levelZero_of_exp_growth {g : ℕ → ℕ} (hgrow : ∀ n, 2 ^ n ≤ g n) :
    ¬ LevelZero g :=
  level_gap (levelGeOne_of_exp_growth hgrow)

/-! ## The horizon-cost family graded by the length filtration -/

/-- **The horizon cost as a function of a length family**: `3` to the
    filtration level `lenFamily n` (the surviving `3^{len}` skein resolution
    tree at problem size `n`). -/
def horizonCostOfLen (lenFamily : ℕ → ℕ) : ℕ → ℕ := fun n => 3 ^ (lenFamily n)

/-- **`2ⁿ ≤ 3^{lenFamily n}` under at-least-linear length growth (sorry-free).**
    If the filtration level grows at least linearly in problem size
    (`n ≤ lenFamily n`), the horizon cost dominates `2ⁿ`. -/
theorem two_pow_le_horizonCostOfLen {lenFamily : ℕ → ℕ}
    (hlin : ∀ n, n ≤ lenFamily n) (n : ℕ) :
    2 ^ n ≤ horizonCostOfLen lenFamily n := by
  unfold horizonCostOfLen
  calc 2 ^ n ≤ 3 ^ n := Nat.pow_le_pow_left (by norm_num) n
    _ ≤ 3 ^ (lenFamily n) := Nat.pow_le_pow_right (by norm_num) (hlin n)

/-- **MAIN BRICK (sorry-free) — the length filtration's ω-grade is level ≥ 1.**
    Conditional on at-least-linear length growth `hlin`, the horizon cost
    `3^{len}` occupies transseries level ≥ 1: `ord_ω(3^{len}) > ord_ω(budget)`.
    The hypothesis `hlin` is the honest input (length really grows with size);
    the grade is derived. -/
theorem horizonCostOfLen_levelGeOne {lenFamily : ℕ → ℕ}
    (hlin : ∀ n, n ≤ lenFamily n) :
    LevelGeOne (horizonCostOfLen lenFamily) :=
  levelGeOne_of_exp_growth (two_pow_le_horizonCostOfLen hlin)

/-- **No polynomial budget bounds the length-graded horizon cost (sorry-free).**
    The main brick composed with the level gap: under at-least-linear length
    growth, no `c·nᵏ` dominates `3^{len}`. -/
theorem not_levelZero_horizonCostOfLen {lenFamily : ℕ → ℕ}
    (hlin : ∀ n, n ≤ lenFamily n) :
    ¬ LevelZero (horizonCostOfLen lenFamily) :=
  level_gap (horizonCostOfLen_levelGeOne hlin)

/-! ## Corpus cross-check: the boundary family recovers `physicalCost` -/

/-- **The boundary family recovers the corpus physical cost (sorry-free).**  The
    `NP`-boundary family has `c = 3N` crossings and `len =` crossing count, so
    `lenFamily n = 3n` and `horizonCostOfLen (3·) = physicalCost = 3^{3n}`.
    Anchors the abstract length grade to the already-proved `#P`-over-moduli
    result. -/
theorem horizonCostOfLen_boundary_eq_physicalCost :
    horizonCostOfLen (fun n => 3 * n) = physicalCost := by
  funext n
  simp [horizonCostOfLen, physicalCost, resolutionTreeSize]

/-- **Re-derivation cross-check (sorry-free).**  Applying the main brick to the
    boundary family recovers `physicalCost_superPoly`: the corpus's proved
    `#P`-hard boundary cost is exactly the level-≥1 verdict of this brick. -/
theorem physicalCost_levelGeOne : LevelGeOne physicalCost := by
  rw [← horizonCostOfLen_boundary_eq_physicalCost]
  exact horizonCostOfLen_levelGeOne (fun n => by omega)

/-! ## Single-instance shadow: the per-state horizon separation -/

/-- **Surreal-grade reading of the per-state horizon separation (sorry-free).**
    If the observed output of `P` is reached no earlier than its birthday-shadow
    horizon cost `3^{len P}`, then `P` is not poly-observable under the identity
    budget — the single-instance shadow of the level gap. Re-exposes the corpus
    bridge lemma `not_polyObservable_id_of_horizon_cost` in surreal-grade
    language. -/
theorem not_polyObservable_id_of_birthday_horizon {S : Type*} {V : Type*}
    (sys : SkeinObservationSystem S V) (P : S)
    (hcost : ∀ k : ℕ,
        sys.obs (sys.step^[k] P) = sys.obs sys.normalForm → 3 ^ sys.len P ≤ k) :
    ¬ sys.PolyObservable id P :=
  sys.not_polyObservable_id_of_horizon_cost P hcost

end QOU.Information
