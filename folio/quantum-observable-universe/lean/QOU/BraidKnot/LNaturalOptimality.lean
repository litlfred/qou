import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith

/-!
# The L♮ optimality criterion from discrete midpoint concavity

Bean `qou-r9a6`.  The `Xbot` arc (`qou-as81`) certifies `e_inf` with a steepest-ascent fixed
point (M5 of `rev_e_infinity_xbot_lnatural_probe.py`) and cites **Murota, *Discrete Convex
Analysis* (2003), Ch. 7** for the step that makes that fixed point *the* integer maximum:

    for an L♮-concave `g`, a point `x` is a global maximiser iff no move `x ± χ_S` improves it.

The corpus holds no copy of Murota.  This file proves the direction the arc uses from a
property the corpus already has: **discrete midpoint concavity**,

    g x + g y ≤ g ⌈(x+y)/2⌉ + g ⌊(x+y)/2⌋,

which `LNaturalConcaveForm` proves for the arc's objective (`concave_exchange_inward`,
`parity_spread`, `midpoint_concave_add`).  So the citation is no longer load-bearing.

## The proof (two steps, no min-cut, no submodularity)

* **Distance one.**  If every coordinate of `y − x` is in `{−1, 0, 1}`, then
  `y = x + χ_S − χ_T` with `S = {y > x}`, `T = {y < x}`, and the two midpoints are exactly
  `x + χ_S` and `x − χ_T` (`ceilMid_of_near`, `floorMid_of_near`).  Midpoint concavity and the
  two local-optimality hypotheses give `g x + g y ≤ g x + g x`.
* **Halving.**  If every coordinate of `y − x` is at most `d ≥ 2` in absolute value, both
  midpoints are within `d − 1` of `x` (`ceilMid_near`, `floorMid_near`), so strong induction on
  `d` closes it.

## Scope

* The theorem is stated for an arbitrary function on `ι → ℤ` with an arbitrary domain `D`, and
  takes midpoint concavity on `D` (including that `D` contains both midpoints) as a hypothesis.
  It does **not** prove that the arc's objective is midpoint concave — that is
  `LNaturalConcaveForm` plus the probe's source assertion C1 and grid check C2b, whose tier is
  recorded there.
* It does **not** prove that steepest ascent terminates, nor that M5's implementation finds a
  point with no improving `±χ_S` move; the probe's M4 checks the min-cut move against brute force.
* Only the "local ⟹ global" direction; the converse is trivial and not stated.

Values lie in any linearly ordered cancellative additive monoid (§7c: an order is needed; no ring,
no `ℝ`).

-- Ref: [leitner2026] computations/deltalambda/rev_e_infinity_xbot_lnatural_probe.py (M5);
--      Murota, Discrete Convex Analysis (SIAM 2003), Thm 7.14 (not held in the corpus).
-/

namespace QOU.BraidKnot.LNaturalOptimality

open Finset

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The upper midpoint `⌈(x+y)/2⌉`, coordinatewise. -/
def ceilMid (x y : ι → ℤ) : ι → ℤ := fun i => (x i + y i + 1) / 2

/-- The lower midpoint `⌊(x+y)/2⌋`, coordinatewise. -/
def floorMid (x y : ι → ℤ) : ι → ℤ := fun i => (x i + y i) / 2

/-- The indicator vector `χ_S`. -/
def chi (S : Finset ι) : ι → ℤ := fun i => if i ∈ S then 1 else 0

/-- `x` is within `d` of `y` in every coordinate. -/
def Near (d : ℕ) (x y : ι → ℤ) : Prop := ∀ i, |y i - x i| ≤ (d : ℤ)

theorem ceilMid_of_near (x y : ι → ℤ) (h : Near 1 x y) :
    ceilMid x y = x + chi (univ.filter fun i => x i < y i) := by
  funext i
  have hi := h i
  simp only [ceilMid, chi, Pi.add_apply, mem_filter, mem_univ, true_and]
  rw [abs_le] at hi
  split_ifs with hlt <;> omega

theorem floorMid_of_near (x y : ι → ℤ) (h : Near 1 x y) :
    floorMid x y = x - chi (univ.filter fun i => y i < x i) := by
  funext i
  have hi := h i
  simp only [floorMid, chi, Pi.sub_apply, mem_filter, mem_univ, true_and]
  rw [abs_le] at hi
  split_ifs with hlt <;> omega

omit [Fintype ι] [DecidableEq ι] in
theorem ceilMid_near {d : ℕ} (hd : 2 ≤ d) (x y : ι → ℤ) (h : Near d x y) :
    Near (d - 1) x (ceilMid x y) := by
  intro i
  have hi := h i
  simp only [ceilMid]
  rw [abs_le] at hi ⊢
  push_cast [Nat.cast_sub (by omega : 1 ≤ d)]
  omega

omit [Fintype ι] [DecidableEq ι] in
theorem floorMid_near {d : ℕ} (hd : 2 ≤ d) (x y : ι → ℤ) (h : Near d x y) :
    Near (d - 1) x (floorMid x y) := by
  intro i
  have hi := h i
  simp only [floorMid]
  rw [abs_le] at hi ⊢
  push_cast [Nat.cast_sub (by omega : 1 ≤ d)]
  omega

omit [Fintype ι] [DecidableEq ι] in
theorem near_mono {d e : ℕ} (hde : d ≤ e) {x y : ι → ℤ} (h : Near d x y) : Near e x y :=
  fun i => (h i).trans (by exact_mod_cast hde)

omit [DecidableEq ι] in
/-- Every point is `Near` some distance: the `ℓ¹` distance bounds every coordinate. -/
theorem exists_near (x y : ι → ℤ) : ∃ d : ℕ, Near d x y := by
  refine ⟨∑ i, (y i - x i).natAbs, fun i => ?_⟩
  have h1 : (y i - x i).natAbs ≤ ∑ j, (y j - x j).natAbs :=
    Finset.single_le_sum (f := fun j => (y j - x j).natAbs) (fun _ _ => Nat.zero_le _) (mem_univ i)
  rw [Int.abs_eq_natAbs]
  exact_mod_cast h1

variable {V : Type*} [AddCommMonoid V] [LinearOrder V] [IsOrderedCancelAddMonoid V]

/-- **The L♮ optimality criterion, local ⟹ global, from midpoint concavity.**

`D` is the effective domain.  Hypotheses: `g` is discretely midpoint concave on `D` (and `D` is
closed under both midpoints); `x ∈ D` admits no improving move `x + χ_S` or `x − χ_S` inside `D`.
Conclusion: `x` maximises `g` on `D`. -/
theorem global_of_local (D : Set (ι → ℤ)) (g : (ι → ℤ) → V)
    (hmidD : ∀ x ∈ D, ∀ y ∈ D, ceilMid x y ∈ D ∧ floorMid x y ∈ D)
    (hmid : ∀ x ∈ D, ∀ y ∈ D, g x + g y ≤ g (ceilMid x y) + g (floorMid x y))
    {x : ι → ℤ} (hx : x ∈ D)
    (hup : ∀ S : Finset ι, x + chi S ∈ D → g (x + chi S) ≤ g x)
    (hdown : ∀ S : Finset ι, x - chi S ∈ D → g (x - chi S) ≤ g x) :
    ∀ y ∈ D, g y ≤ g x := by
  -- strong induction on the coordinatewise distance
  have key : ∀ d : ℕ, ∀ y ∈ D, Near d x y → g y ≤ g x := by
    intro d
    induction d using Nat.strong_induction_on with
    | _ d ih =>
      intro y hy hnear
      have hm := hmid x hx y hy
      obtain ⟨hcD, hfD⟩ := hmidD x hx y hy
      by_cases hd : d ≤ 1
      · have h1 : Near 1 x y := near_mono hd hnear
        rw [ceilMid_of_near x y h1] at hm hcD
        rw [floorMid_of_near x y h1] at hm hfD
        have := add_le_add (hup _ hcD) (hdown _ hfD)
        exact le_of_add_le_add_left (hm.trans this)
      · have hd2 : 2 ≤ d := by omega
        have hc := ih (d - 1) (by omega) _ hcD (ceilMid_near hd2 x y hnear)
        have hf := ih (d - 1) (by omega) _ hfD (floorMid_near hd2 x y hnear)
        exact le_of_add_le_add_left (hm.trans (add_le_add hc hf))
  intro y hy
  obtain ⟨d, hd⟩ := exists_near x y
  exact key d y hy hd

/-! ## Midpoint closure of the L♮-convex polyhedron (box + pairwise difference bounds)

The `Xbot` integer domain is cut out by box constraints `lo i ≤ u i ≤ hi i` together with pairwise
difference bounds `u i - u j ≤ c i j` (ordering / gap-wall constraints).  Wait-free discharge of the
domain midpoint-closure hypothesis `hmidD` of `global_of_local`: any such polyhedron is closed under
both `ceilMid` and `floorMid`. -/

/-- The standard L♮-convex integer domain defined by coordinatewise box bounds `lo ≤ u ≤ hi` and
pairwise difference bounds `u i - u j ≤ c i j`. -/
def boxDiffDomain (lo hi : ι → ℤ) (c : ι → ι → ℤ) : Set (ι → ℤ) :=
  {u | (∀ i, lo i ≤ u i ∧ u i ≤ hi i) ∧ ∀ i j, u i - u j ≤ c i j}

omit [Fintype ι] [DecidableEq ι] in
/-- The upper midpoint `⌈(x+y)/2⌉` preserves all box and pairwise-difference bounds. -/
theorem ceilMid_mem_boxDiffDomain (lo hi : ι → ℤ) (c : ι → ι → ℤ)
    {x y : ι → ℤ} (hx : x ∈ boxDiffDomain lo hi c) (hy : y ∈ boxDiffDomain lo hi c) :
    ceilMid x y ∈ boxDiffDomain lo hi c := by
  refine ⟨fun i => ?_, fun i j => ?_⟩
  · have hxi := hx.1 i
    have hyi := hy.1 i
    simp only [ceilMid]
    omega
  · have hxij := hx.2 i j
    have hyij := hy.2 i j
    simp only [ceilMid]
    omega

omit [Fintype ι] [DecidableEq ι] in
/-- The lower midpoint `⌊(x+y)/2⌋` preserves all box and pairwise-difference bounds. -/
theorem floorMid_mem_boxDiffDomain (lo hi : ι → ℤ) (c : ι → ι → ℤ)
    {x y : ι → ℤ} (hx : x ∈ boxDiffDomain lo hi c) (hy : y ∈ boxDiffDomain lo hi c) :
    floorMid x y ∈ boxDiffDomain lo hi c := by
  refine ⟨fun i => ?_, fun i j => ?_⟩
  · have hxi := hx.1 i
    have hyi := hy.1 i
    simp only [floorMid]
    omega
  · have hxij := hx.2 i j
    have hyij := hy.2 i j
    simp only [floorMid]
    omega

omit [Fintype ι] [DecidableEq ι] in
/-- Combined midpoint-closure witness for `boxDiffDomain`, ready to feed `global_of_local`. -/
theorem boxDiffDomain_midpoint_closed (lo hi : ι → ℤ) (c : ι → ι → ℤ) :
    ∀ x ∈ boxDiffDomain lo hi c, ∀ y ∈ boxDiffDomain lo hi c,
      ceilMid x y ∈ boxDiffDomain lo hi c ∧ floorMid x y ∈ boxDiffDomain lo hi c :=
  fun _ hx _ hy => ⟨ceilMid_mem_boxDiffDomain lo hi c hx hy, floorMid_mem_boxDiffDomain lo hi c hx hy⟩

/-- **The L♮ optimality criterion on a box-plus-difference domain**, with domain midpoint closure
discharged automatically by `boxDiffDomain_midpoint_closed`. -/
theorem global_of_local_boxDiffDomain (lo hi : ι → ℤ) (c : ι → ι → ℤ) (g : (ι → ℤ) → V)
    (hmid : ∀ x ∈ boxDiffDomain lo hi c, ∀ y ∈ boxDiffDomain lo hi c,
      g x + g y ≤ g (ceilMid x y) + g (floorMid x y))
    {x : ι → ℤ} (hx : x ∈ boxDiffDomain lo hi c)
    (hup : ∀ S : Finset ι, x + chi S ∈ boxDiffDomain lo hi c → g (x + chi S) ≤ g x)
    (hdown : ∀ S : Finset ι, x - chi S ∈ boxDiffDomain lo hi c → g (x - chi S) ≤ g x) :
    ∀ y ∈ boxDiffDomain lo hi c, g y ≤ g x :=
  global_of_local (boxDiffDomain lo hi c) g (boxDiffDomain_midpoint_closed lo hi c) hmid hx hup hdown

end QOU.BraidKnot.LNaturalOptimality
