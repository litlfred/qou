import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Core.LawvereCut — observables as cuts, and the one non-constructive axiom

Bean `qou-dk7p` (constructive turn), foundation chosen by the owner on
2026-11-27: every QOU quantity is an element of an algebraic ring `R`
(`ℚ(q)`, `ℚ[[h]]`, …). Comparison with an ordered field `K` (typically `ℚ`)
goes through a **cut**, a pair of lower and upper probe predicates, after
Lawvere's enriched Cauchy completion (Lawvere 1973, "Metric spaces,
generalized logic, and closed categories").

* **`ev`** (the counit) is *interval soundness*: no accepted lower probe
  exceeds an accepted upper probe. It is part of the data of a `Cut` and is
  proved, constructively, for each quantity.
* **`coev = 0`** (the unit) is *locatedness*, the squeeze: lower and upper
  probes pinch to within every `ε > 0`. This is `Cut.Located`.
* **`coev ≤ ε`** is `Cut.WithinResolution ε`: a finite-precision interval
  observable, with no completed real number anywhere.

## The single axiom

`Coev E` states that every observable under a cut evaluation `E` is located.
It is a hypothesis class, not a Lean `axiom`, so `#print axioms` stays clean
and every result that needs it says so in its signature. The strangler-fig
migration moves each residual analytic result in QOU (KZ evaluation at the
physical coupling, hyperbolic volume as a limit, dilogarithm asymptotics, the
surreal transfer, …) onto `[Coev E]`, deleting that result's private analytic
hypothesis as it moves. Results proved with `ev` alone need no axiom at all.

## The adic case: locatedness is free

`AdicCut` is the ultrametric (max-quantale) analogue: a tower of stages
`stage n ∈ R` whose consecutive differences lie in a decreasing chain of ideals.
In the Habiro tower `I_n = ((q;q)_n)` the squeeze holds by construction: every
later stage lies within `I_n` of `stage n` (`AdicCut.stage_sub_mem`). So an
observable presented adically needs no `Coev` instance; the axiom is only for
the Archimedean comparison with an ordered field.

No empirical value enters this file.
-/

namespace QOU.Core.LawvereCut

/-- A two-sided cut over an ordered type `K`: accepted lower probes are closed
downward, accepted upper probes are closed upward, and `ev` (interval
soundness) holds. -/
structure Cut (K : Type*) [LE K] where
  /-- Accepted lower probes. -/
  lower : K → Prop
  /-- Accepted upper probes. -/
  upper : K → Prop
  lower_down : ∀ a a' : K, a' ≤ a → lower a → lower a'
  upper_up : ∀ b b' : K, b ≤ b' → upper b → upper b'
  /-- Lawvere `ev`: interval soundness. -/
  ev : ∀ a b : K, lower a → upper b → a ≤ b

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

namespace Cut

/-- `coev ≤ ε`: some accepted lower and upper probes lie within `ε`. -/
def WithinResolution (c : Cut K) (ε : K) : Prop :=
  ∃ a b : K, c.lower a ∧ c.upper b ∧ b - a ≤ ε

/-- `coev = 0`: the cut is located (the squeeze). -/
def Located (c : Cut K) : Prop :=
  ∀ ε : K, 0 < ε → c.WithinResolution ε

/-- `x` lies between every accepted lower and upper probe. -/
def Contains (c : Cut K) (x : K) : Prop :=
  (∀ a, c.lower a → a ≤ x) ∧ (∀ b, c.upper b → x ≤ b)

theorem WithinResolution.mono {c : Cut K} {ε ε' : K}
    (h : c.WithinResolution ε) (hle : ε ≤ ε') : c.WithinResolution ε' := by
  obtain ⟨a, b, ha, hb, hab⟩ := h
  exact ⟨a, b, ha, hb, hab.trans hle⟩

/-- A located cut contains at most one element of `K`. -/
theorem Located.eq_of_contains {c : Cut K} (hc : c.Located) {x y : K}
    (hx : c.Contains x) (hy : c.Contains y) : x = y := by
  by_contra hne
  rcases lt_or_gt_of_ne hne with h | h
  · obtain ⟨a, b, ha, hb, hab⟩ := hc ((y - x) / 2) (half_pos (sub_pos.mpr h))
    have h1 := hx.1 a ha
    have h2 := hy.2 b hb
    linarith
  · obtain ⟨a, b, ha, hb, hab⟩ := hc ((x - y) / 2) (half_pos (sub_pos.mpr h))
    have h1 := hy.1 a ha
    have h2 := hx.2 b hb
    linarith

/-- The cut of an exact element of `K`. -/
def ofPoint (x : K) : Cut K where
  lower a := a ≤ x
  upper b := x ≤ b
  lower_down _ _ h ha := le_trans h ha
  upper_up _ _ h hb := le_trans hb h
  ev _ _ ha hb := le_trans ha hb

theorem ofPoint_contains (x : K) : (ofPoint x).Contains x :=
  ⟨fun _ ha => ha, fun _ hb => hb⟩

/-- An exact element is located with no axiom. -/
theorem ofPoint_located (x : K) : (ofPoint x).Located := by
  intro ε hε
  refine ⟨x, x, le_refl x, le_refl x, ?_⟩
  rw [sub_self]
  exact hε.le

/-- The cut of a finite-precision interval `[lo, hi]`. -/
def ofInterval (lo hi : K) (h : lo ≤ hi) : Cut K where
  lower a := a ≤ lo
  upper b := hi ≤ b
  lower_down _ _ h' ha := le_trans h' ha
  upper_up _ _ h' hb := le_trans hb h'
  ev _ _ ha hb := le_trans ha (le_trans h hb)

/-- An interval observable has `coev ≤ hi - lo`, with no axiom. -/
theorem ofInterval_withinResolution (lo hi : K) (h : lo ≤ hi) :
    (ofInterval lo hi h).WithinResolution (hi - lo) :=
  ⟨lo, hi, le_refl lo, le_refl hi, le_refl _⟩

end Cut

/-- Evaluation of ring-valued observables `R` as cuts over `K`. This is
constructive data: only `ev` is asserted. -/
structure CutEvaluation (R : Type*) (K : Type*) [LE K] where
  cut : R → Cut K

/-- **The one non-constructive axiom of QOU (Lawvere `coev = 0`).** Every
observable's cut is located. Results that need it take `[Coev E]`. -/
class Coev {R : Type*} (E : CutEvaluation R K) : Prop where
  located : ∀ r : R, (E.cut r).Located

/-- Under `Coev`, each observable has at most one exact value in `K`. -/
theorem Coev.unique_value {R : Type*} (E : CutEvaluation R K) [Coev E] (r : R)
    {x y : K} (hx : (E.cut r).Contains x) (hy : (E.cut r).Contains y) : x = y :=
  (Coev.located (E := E) r).eq_of_contains hx hy

/-- Under `Coev`, every observable is known to every positive resolution. -/
theorem Coev.withinResolution {R : Type*} (E : CutEvaluation R K) [Coev E] (r : R)
    {ε : K} (hε : 0 < ε) : (E.cut r).WithinResolution ε :=
  Coev.located (E := E) r ε hε

/-! ### Adic cuts (max-quantale case) -/

/-- An adic cut over a commutative ring: stages that agree modulo a decreasing
chain of ideals. -/
structure AdicCut (R : Type*) [CommRing R] where
  ideal : ℕ → Ideal R
  ideal_anti : Antitone ideal
  stage : ℕ → R
  compat : ∀ n, stage (n + 1) - stage n ∈ ideal n

/-- Locatedness is free for an adic cut: every later stage lies within the
`n`-th ideal of stage `n`. No axiom is used. -/
theorem AdicCut.stage_sub_mem {R : Type*} [CommRing R] (c : AdicCut R) {n m : ℕ}
    (h : n ≤ m) : c.stage m - c.stage n ∈ c.ideal n := by
  induction m, h using Nat.le_induction with
  | base => simp
  | succ m hnm ih =>
    have h1 : c.stage (m + 1) - c.stage m ∈ c.ideal n := c.ideal_anti hnm (c.compat m)
    have h2 := Ideal.add_mem _ h1 ih
    rwa [sub_add_sub_cancel] at h2

/-- The `q`-Pochhammer symbol `(q;q)_n = ∏_{k<n} (1 - q^{k+1})`. -/
def qPoch {R : Type*} [CommRing R] (q : R) (n : ℕ) : R :=
  ∏ k ∈ Finset.range n, (1 - q ^ (k + 1))

/-- The Habiro ideal `I_n = ((q;q)_n)`. -/
def habiroIdeal {R : Type*} [CommRing R] (q : R) (n : ℕ) : Ideal R :=
  Ideal.span {qPoch q n}

/-- The Habiro ideals decrease, so they define an adic cut tower. -/
theorem habiroIdeal_antitone {R : Type*} [CommRing R] (q : R) :
    Antitone (habiroIdeal q) := by
  intro n m h
  show Ideal.span {qPoch q m} ≤ Ideal.span {qPoch q n}
  exact Ideal.span_singleton_le_span_singleton.mpr
    (Finset.prod_dvd_prod_of_subset _ _ _ (Finset.range_mono h))

end QOU.Core.LawvereCut
