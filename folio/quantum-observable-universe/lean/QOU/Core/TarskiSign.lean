import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.Observations.SignSequence
import QOU.Core.LawvereCut
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# QOU.Core.TarskiSign — finite-N signs decided by rational arithmetic

Bean `qou-rc4t` (constructive turn, epic `qou-dk7p`): the real-closed
(Tarski) route for finite-`N` comparisons.

A finite-`N` QOU quantity is an algebraic number, an element `f(α)` of
`ℚ(α)` where `α` is a root of a rational polynomial `p`. Its sign is not an
analytic question. This file proves, over **any** ordered field `K` and with
no axiom, the three facts that let every such sign be decided by finite
rational arithmetic.

1. **Positivity certificates** (`bernstein_pos`, `taylorUp_pos`,
   `taylorDown_pos`). If `f` is written in the Bernstein basis
   `(x - a)^i (b - x)^(n-i)` of `[a, b]` with nonnegative coefficients and
   positive end coefficients, then `f > 0` on `[a, b]`. On a half-line
   `[m, ∞)` the same holds for the Taylor shift `∑ cᵢ (x - m)^i`. Checking a
   certificate is a polynomial identity plus finitely many rational
   inequalities. By Bernstein's theorem (degree elevation) a certificate
   exists whenever `f > 0` on `[a, b]`; that completeness is not needed
   here and not proved.

2. **Root exclusion** (`lt_of_excluded`, `lt_of_excluded'`). If `p(α) = 0`
   and `p` has no zero on `[m, b]`, then `α < m`. This is one bisection step
   of real root isolation (the job a Sturm sequence or Thom encoding does in
   a real closed field), carried out without the intermediate value
   theorem: `α` is given, and only its location is refined.

3. **Gonshor windows** (`follow`, `follow_window`, `signPrefix`). Following
   `α` through Conway's sign-expansion recipe (`GonshorState.step` from
   `QOU.Observations.SignSequence`) produces dyadic windows
   `lo < α ≤ hi`. The `n` signs chosen are the first `n` signs of the
   surreal sign expansion of `α`, and the first one is `+` exactly when
   `0 < α` (`signPrefix_one`). Each sign is one comparison of `α` with a
   dyadic, so each is decided by a certificate from (1) and (2).

## Birthdays

Every irrational real, in particular every irrational algebraic number, is
born on day `ω`, so the surreal birthday does not grade the algebraic
numbers. It does grade the dyadic windows: the window after `n` signs has
endpoints born by day `n`. The **decision depth** of a sign claim
`0 < f(α)` is the least `n` for which the window after `n` signs carries a
certificate for `f` (`pos_of_window`). It is a finite natural number for
each decided claim, and it is the birthday of the coarsest dyadic window
that decides it.

The same depth measures the embedding itself. For `ℚ(ζ_N)⁺ = ℚ(c)`,
`c = ζ_N + ζ_N⁻¹`, choosing `ζ_N = e^{2πi/N}` means choosing the largest
root of the minimal polynomial `Ψ_N` of `c`. That choice is the shortest
sign prefix whose window holds no other root of `Ψ_N`: finite rational data,
with no cosine and no `π`.

## What stays on `[Coev E]`

Nothing in this file needs `QOU.Core.LawvereCut.Coev`. Finite-`N` signs are
decided outright. Only the `N → ∞` limit (the volume conjecture proper)
remains a `coev` claim.

No empirical value enters this file.

-/

namespace QOU.Core.TarskiSign

open Finset QOU.AppendixSurreals

/-! ### 1. Positivity certificates -/

section Certificates

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The Bernstein-basis polynomial on `[a, b]` of degree `n` with coefficients
`c`: `∑_{i ≤ n} cᵢ (x - a)^i (b - x)^(n-i)`. Binomial factors are absorbed
into `c`. -/
def bernstein (a b : K) (n : ℕ) (c : ℕ → K) (x : K) : K :=
  ∑ i ∈ range (n + 1), c i * (x - a) ^ i * (b - x) ^ (n - i)

/-- **Bernstein certificate.** Nonnegative Bernstein coefficients with
positive end coefficients give positivity on the closed interval. -/
theorem bernstein_pos {a b x : K} {n : ℕ} {c : ℕ → K}
    (hab : a < b) (hax : a ≤ x) (hxb : x ≤ b)
    (hc : ∀ i ≤ n, 0 ≤ c i) (h0 : 0 < c 0) (hn : 0 < c n) :
    0 < bernstein a b n c x := by
  unfold bernstein
  have hterm : ∀ i ∈ range (n + 1), 0 ≤ c i * (x - a) ^ i * (b - x) ^ (n - i) := by
    intro i hi
    have hi' : i ≤ n := Nat.lt_succ_iff.mp (mem_range.mp hi)
    have h1 : 0 ≤ x - a := sub_nonneg.mpr hax
    have h2 : 0 ≤ b - x := sub_nonneg.mpr hxb
    have := hc i hi'
    positivity
  rcases lt_or_eq_of_le hxb with hlt | heq
  · -- `x < b`: the `i = 0` term is positive.
    have hpos : 0 < c 0 * (x - a) ^ 0 * (b - x) ^ (n - 0) := by
      have : 0 < b - x := sub_pos.mpr hlt
      simp only [pow_zero, mul_one, Nat.sub_zero]
      positivity
    exact lt_of_lt_of_le hpos
      (single_le_sum hterm (mem_range.mpr (Nat.succ_pos n)))
  · -- `x = b`: the `i = n` term is positive.
    have hpos : 0 < c n * (x - a) ^ n * (b - x) ^ (n - n) := by
      have : 0 < x - a := by rw [heq]; exact sub_pos.mpr hab
      simp only [Nat.sub_self, pow_zero, mul_one]
      positivity
    exact lt_of_lt_of_le hpos
      (single_le_sum hterm (mem_range.mpr (Nat.lt_succ_self n)))

/-- Taylor shift at `m` with coefficients `c`: `∑_{i ≤ n} cᵢ (x - m)^i`. -/
def taylorUp (m : K) (n : ℕ) (c : ℕ → K) (x : K) : K :=
  ∑ i ∈ range (n + 1), c i * (x - m) ^ i

/-- **Half-line certificate, upward.** Nonnegative Taylor coefficients at
`m` with positive constant term give positivity on `[m, ∞)`. -/
theorem taylorUp_pos {m x : K} {n : ℕ} {c : ℕ → K} (hmx : m ≤ x)
    (hc : ∀ i ≤ n, 0 ≤ c i) (h0 : 0 < c 0) : 0 < taylorUp m n c x := by
  unfold taylorUp
  have hterm : ∀ i ∈ range (n + 1), 0 ≤ c i * (x - m) ^ i := by
    intro i hi
    have h1 : 0 ≤ x - m := sub_nonneg.mpr hmx
    have := hc i (Nat.lt_succ_iff.mp (mem_range.mp hi))
    positivity
  have hpos : 0 < c 0 * (x - m) ^ 0 := by simpa using h0
  exact lt_of_lt_of_le hpos (single_le_sum hterm (mem_range.mpr (Nat.succ_pos n)))

/-- Reflected Taylor shift at `m`: `∑_{i ≤ n} cᵢ (m - x)^i`. -/
def taylorDown (m : K) (n : ℕ) (c : ℕ → K) (x : K) : K :=
  ∑ i ∈ range (n + 1), c i * (m - x) ^ i

/-- **Half-line certificate, downward.** Positivity on `(-∞, m]`. -/
theorem taylorDown_pos {m x : K} {n : ℕ} {c : ℕ → K} (hxm : x ≤ m)
    (hc : ∀ i ≤ n, 0 ≤ c i) (h0 : 0 < c 0) : 0 < taylorDown m n c x := by
  unfold taylorDown
  have hterm : ∀ i ∈ range (n + 1), 0 ≤ c i * (m - x) ^ i := by
    intro i hi
    have h1 : 0 ≤ m - x := sub_nonneg.mpr hxm
    have := hc i (Nat.lt_succ_iff.mp (mem_range.mp hi))
    positivity
  have hpos : 0 < c 0 * (m - x) ^ 0 := by simpa using h0
  exact lt_of_lt_of_le hpos (single_le_sum hterm (mem_range.mpr (Nat.succ_pos n)))

end Certificates

/-! ### 2. Root exclusion (one bisection step)

These need only a linear order on `K`. -/

section Exclusion

variable {K : Type*} [Zero K] [LinearOrder K]

/-- If `p` has no zero on `[m, b]` and `α ≤ b` is a zero of `p`, then
`α < m`. -/
theorem lt_of_excluded {p : K → K} {α m b : K} (hα : p α = 0) (hαb : α ≤ b)
    (hcert : ∀ x, m ≤ x → x ≤ b → p x ≠ 0) : α < m := by
  by_contra h
  exact hcert α (not_lt.mp h) hαb hα

/-- If `p` has no zero on `[a, m]` and `a ≤ α` is a zero of `p`, then
`m < α`. -/
theorem lt_of_excluded' {p : K → K} {α m a : K} (hα : p α = 0) (haα : a ≤ α)
    (hcert : ∀ x, a ≤ x → x ≤ m → p x ≠ 0) : m < α := by
  by_contra h
  exact hcert α haα (not_lt.mp h) hα

/-- Unbounded form: no zero on `[m, ∞)`. -/
theorem lt_of_excluded_up {p : K → K} {α m : K} (hα : p α = 0)
    (hcert : ∀ x, m ≤ x → p x ≠ 0) : α < m := by
  by_contra h
  exact hcert α (not_lt.mp h) hα

/-- Unbounded form: no zero on `(-∞, m]`. -/
theorem lt_of_excluded_down {p : K → K} {α m : K} (hα : p α = 0)
    (hcert : ∀ x, x ≤ m → p x ≠ 0) : m < α := by
  by_contra h
  exact hcert α (not_lt.mp h) hα

end Exclusion

/-! ### 3. Gonshor windows: the sign expansion of `α`, one decision per sign

These need only a field with a linear order (no compatibility axiom). -/

section Windows

variable {K : Type*} [Field K] [LinearOrder K]

/-- The sign of `α` against the current Gonshor value: `+` if the value lies
strictly below `α`, else `-`. -/
def signAt (α : K) (st : GonshorState) : Sign :=
  if ((st.value : ℚ) : K) < α then Sign.plus else Sign.minus

/-- The Gonshor state after following `α` for `n` signs. -/
def follow (α : K) : ℕ → GonshorState
  | 0 => GonshorState.init
  | n + 1 => (follow α n).step (signAt α (follow α n))

/-- The first `n` signs of the sign expansion of `α`. -/
def signPrefix (α : K) : ℕ → List Sign
  | 0 => []
  | n + 1 => signPrefix α n ++ [signAt α (follow α n)]

theorem signPrefix_length (α : K) (n : ℕ) : (signPrefix α n).length = n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [signPrefix, ih]

/-- Following `α` is folding its sign prefix through Gonshor's recipe. -/
theorem follow_eq_foldl (α : K) (n : ℕ) :
    follow α n = (signPrefix α n).foldl GonshorState.step GonshorState.init := by
  induction n with
  | zero => rfl
  | succ n ih => simp [follow, signPrefix, List.foldl_append, ← ih]

/-- The dyadic reached after `n` signs is Gonshor's value of the prefix. -/
theorem gonshor_signPrefix (α : K) (n : ℕ) :
    gonshor (signPrefix α n) = (follow α n).value := by
  rw [follow_eq_foldl]; rfl

/-- **Window invariant.** After any number of signs, `α` lies in the
half-open dyadic window `(lo, hi]` (each side only when present). -/
theorem follow_window (α : K) (n : ℕ) :
    ((follow α n).hasLo = true → (((follow α n).lo : ℚ) : K) < α) ∧
    ((follow α n).hasHi = true → α ≤ (((follow α n).hi : ℚ) : K)) := by
  induction n with
  | zero => simp [follow, GonshorState.init]
  | succ n ih =>
    obtain ⟨ihLo, ihHi⟩ := ih
    simp only [follow, signAt]
    split_ifs with hlt
    · -- sign `+`: new lower bound is the old value
      unfold GonshorState.step
      by_cases hH : (follow α n).hasHi = true
      · simp only [hH, if_true]; exact ⟨fun _ => hlt, fun _ => ihHi hH⟩
      · simp only [hH]; simp
        exact hlt
    · -- sign `-`: new upper bound is the old value
      have hle : α ≤ (((follow α n).value : ℚ) : K) := not_lt.mp hlt
      unfold GonshorState.step
      by_cases hL : (follow α n).hasLo = true
      · simp only [hL, if_true]; exact ⟨fun _ => ihLo hL, fun _ => hle⟩
      · simp only [hL]; simp
        exact hle

/-- The first sign of the expansion is `+` exactly when `α > 0`. -/
theorem signPrefix_one (α : K) :
    signPrefix α 1 = [if 0 < α then Sign.plus else Sign.minus] := by
  simp [signPrefix, signAt, follow, GonshorState.init]

/-- **Decision at depth `n`.** If the window after `n` signs is bounded on
both sides and `f` has a positivity certificate on it, then `0 < f α`. The
least such `n` is the decision depth (the birthday of the deciding window). -/
theorem pos_of_window {α : K} {f : K → K} {n : ℕ}
    (hLo : (follow α n).hasLo = true) (hHi : (follow α n).hasHi = true)
    (hcert : ∀ x, (((follow α n).lo : ℚ) : K) ≤ x →
      x ≤ (((follow α n).hi : ℚ) : K) → 0 < f x) : 0 < f α :=
  hcert α ((follow_window α n).1 hLo).le ((follow_window α n).2 hHi)

end Windows

/-! ### 4. Windows halve: a finite-`N` algebraic number is located with no axiom

Once the window has both bounds, every further sign halves it. So the cut of
`α` by its Gonshor windows is within resolution `w / 2^k` after `k` more
signs, and in an Archimedean field it is located (`gonshorCut_located`). For
a finite-`N` algebraic `α` every one of those signs is a certificate, so the
Lawvere `coev = 0` holds here as a theorem: `[Coev E]` is not needed at
finite `N`. -/

/-- A state that bisects: both bounds present and the value at the midpoint. -/
def Bisecting (st : GonshorState) : Prop :=
  st.hasLo = true ∧ st.hasHi = true ∧ st.value = (st.lo + st.hi) / 2

/-- After any step, a state with both bounds bisects. -/
theorem step_bisecting (st : GonshorState) (s : Sign)
    (hL : (st.step s).hasLo = true) (hH : (st.step s).hasHi = true) :
    Bisecting (st.step s) := by
  refine ⟨hL, hH, ?_⟩
  cases s <;> cases h1 : st.hasHi <;> cases h2 : st.hasLo <;>
    simp_all [GonshorState.step]

/-- A bisecting state stays bisecting and its window halves. -/
theorem step_halves (st : GonshorState) (s : Sign) (hb : Bisecting st) :
    Bisecting (st.step s) ∧
      (st.step s).hi - (st.step s).lo = (st.hi - st.lo) / 2 := by
  obtain ⟨hL, hH, hm⟩ := hb
  have hflags : (st.step s).hasLo = true ∧ (st.step s).hasHi = true := by
    cases s <;> simp [GonshorState.step, hL, hH]
  refine ⟨step_bisecting st s hflags.1 hflags.2, ?_⟩
  cases s <;> simp [GonshorState.step, hL, hH, hm] <;> ring

section Located

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

omit [IsStrictOrderedRing K] in
theorem follow_bisecting_of_bounds (α : K) (n : ℕ) (hL : (follow α n).hasLo = true)
    (hH : (follow α n).hasHi = true) : Bisecting (follow α n) := by
  cases n with
  | zero => simp [follow, GonshorState.init] at hL
  | succ n => exact step_bisecting _ _ hL hH

omit [IsStrictOrderedRing K] in
/-- `k` more signs halve a bisecting window `k` times. -/
theorem follow_halves (α : K) (n : ℕ) (hb : Bisecting (follow α n)) (k : ℕ) :
    Bisecting (follow α (n + k)) ∧
      (follow α (n + k)).hi - (follow α (n + k)).lo
        = ((follow α n).hi - (follow α n).lo) / 2 ^ k := by
  induction k with
  | zero => simp [hb]
  | succ k ih =>
    obtain ⟨hb', hw⟩ := step_halves _ (signAt α (follow α (n + k))) ih.1
    refine ⟨hb', ?_⟩
    change (follow α (n + k + 1)).hi - (follow α (n + k + 1)).lo = _
    simp only [follow]
    rw [hw, ih.2, pow_succ]; field_simp

open QOU.Core.LawvereCut in
/-- The cut of `α` by all of its Gonshor windows. Its `ev` (interval
soundness) is the window invariant; no axiom. -/
def gonshorCut (α : K) : Cut K where
  lower a := ∃ n, (follow α n).hasLo = true ∧ a ≤ (((follow α n).lo : ℚ) : K)
  upper b := ∃ n, (follow α n).hasHi = true ∧ (((follow α n).hi : ℚ) : K) ≤ b
  lower_down _ _ h := fun ⟨n, hn, ha⟩ => ⟨n, hn, le_trans h ha⟩
  upper_up _ _ h := fun ⟨n, hn, hb⟩ => ⟨n, hn, le_trans hb h⟩
  ev _ _ := fun ⟨n, hn, ha⟩ ⟨m, hm, hb⟩ =>
    le_trans ha (le_trans ((follow_window α n).1 hn).le
      (le_trans ((follow_window α m).2 hm) hb))

omit [IsStrictOrderedRing K] in
open QOU.Core.LawvereCut in
theorem gonshorCut_contains (α : K) : (gonshorCut α).Contains α :=
  ⟨fun _ ⟨n, hn, ha⟩ => le_trans ha ((follow_window α n).1 hn).le,
   fun _ ⟨n, hn, hb⟩ => le_trans ((follow_window α n).2 hn) hb⟩

open QOU.Core.LawvereCut in
/-- After a bisecting stage `n`, `k` more signs give resolution `w / 2^k`. -/
theorem gonshorCut_withinResolution (α : K) (n : ℕ) (hb : Bisecting (follow α n))
    (k : ℕ) : (gonshorCut α).WithinResolution
      ((((follow α n).hi - (follow α n).lo : ℚ) : K) / 2 ^ k) := by
  obtain ⟨⟨hL, hH, _⟩, hw⟩ := follow_halves α n hb k
  refine ⟨_, _, ⟨n + k, hL, le_refl _⟩, ⟨n + k, hH, le_refl _⟩, le_of_eq ?_⟩
  rw [← Rat.cast_sub, hw]; push_cast; ring

open QOU.Core.LawvereCut in
/-- **Located with no axiom.** In an Archimedean ordered field, once some
window of `α` has both bounds, the Gonshor cut of `α` is located: Lawvere
`coev = 0` is a theorem here, not the `Coev` hypothesis. -/
theorem gonshorCut_located [Archimedean K] (α : K) {n : ℕ}
    (hL : (follow α n).hasLo = true) (hH : (follow α n).hasHi = true) :
    (gonshorCut α).Located := by
  intro ε hε
  have hb := follow_bisecting_of_bounds α n hL hH
  set w : K := (((follow α n).hi - (follow α n).lo : ℚ) : K)
  obtain ⟨k, hk⟩ := pow_unbounded_of_one_lt (w / ε) (by norm_num : (1 : K) < 2)
  obtain ⟨a, b, ha, hb', hab⟩ := gonshorCut_withinResolution α n hb k
  refine ⟨a, b, ha, hb', le_trans hab ?_⟩
  have h2 : (0 : K) < 2 ^ k := by positivity
  rw [div_le_iff₀ h2]
  have := (div_lt_iff₀ hε).mp hk
  linarith [mul_comm ε ((2 : K) ^ k)]

end Located

end QOU.Core.TarskiSign
