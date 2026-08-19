/-
  How fast Gonshor's sign expansion converges — the arithmetic half of the bridge
  `DiophantineBirthdayTrajectory` says is missing.

  Bean `qou-bday`.

  ═══ WHAT THIS IS FOR ═══

  `DiophantineBirthdayTrajectory.lean` established that a trajectory criterion for
  `conj:diophantine-birthday` is **not obstructed** (unlike birthday-of-the-number) and
  that one direction is already a Mathlib theorem, then recorded the remaining gap:

  > nothing here proves that `gonshor`'s length-`n` prefix value *is* the dyadic
  > approximant of `α` at denominator `2ⁿ`.

  This module supplies the quantitative core of that: **once the expansion has bracketed
  its target, every further sign halves the bracket.**

  ═══ ⚠ WHY THIS IS AVAILABLE WHEN THE SHARPER BIRTHDAY BOUND IS NOT ═══

  `SignSequence.lean` records that Gonshor's `birthday ≤ s.length` is **not** derivable
  from the `SurrealField` axioms, because the induction step needs a per-step bound on
  `birthday (x / 2)` — the halving move — which is not among the axioms and is not implied
  by them.

  That blocker is about **lifting to `birthday`**. It says nothing about the rational
  values themselves, and `gonshor : List Sign → ℚ` never leaves `ℚ`. So the convergence
  *rate* is ordinary rational arithmetic and needs no axiom at all. The two halves of the
  bridge have genuinely different status, and conflating them is what made this look
  harder than it is:

  | half | status |
  |---|---|
  | rate of the rational approximants | **proved here**, axiom-free |
  | lifting the rate to surreal birthday | blocked, needs a `birthday (x/2)` axiom |

  ═══ THE INVARIANT ═══

  `GonshorState.step` has two regimes. Before a bound exists it steps by `±1` (integer
  search); once the opposite bound appears it bisects. `Bracketed` names the bisection
  regime, and its load-bearing clause is `value = (lo + hi) / 2` — **the value is the
  midpoint of its own bracket**. That is what makes the halving work: without it,
  `step`'s new bracket `[value, hi]` would have no fixed relation to the old `[lo, hi]`.

  ═══ ⚠ SCOPE ═══

  This is about `gonshor`'s *own* bracket, not about any target real. Nothing here says a
  given sign sequence converges to a given `α` — that needs the sequence to be *the* sign
  expansion of `α`, which `SignSequence.lean` does not define. What is proved is the rate
  at which the bracket closes, which is the part the Liouville comparison needs and the
  part that was missing.

  -- Ref: [gonshor1986] An Introduction to the Theory of Surreal Numbers, Ch. 2
-/
import QOU.AppendixSurreals.SignSequence

namespace QOU.AppendixSurreals

/-- The **bisection regime**: both bounds exist, the value lies strictly inside them, and
— the clause that does the work — the value is the *midpoint* of its own bracket.

`GonshorState.step` re-establishes this at every step, which is why the bracket halves. -/
structure Bracketed (st : GonshorState) : Prop where
  hasLo : st.hasLo = true
  hasHi : st.hasHi = true
  mid : st.value = (st.lo + st.hi) / 2
  lt : st.lo < st.hi

/-- The bracket width. -/
def GonshorState.gap (st : GonshorState) : ℚ := st.hi - st.lo

/-- **One sign halves the bracket**, and leaves the state in the bisection regime.

Both signs are covered: `+` keeps the upper bound and moves the lower one up to the old
value; `-` keeps the lower bound and moves the upper one down. In each case the new
bracket is exactly one half of the old, because the old value was its midpoint. -/
theorem Bracketed.step (st : GonshorState) (h : Bracketed st) (s : Sign) :
    Bracketed (st.step s) ∧ (st.step s).gap = st.gap / 2 := by
  obtain ⟨hlo, hhi, hmid, hlt⟩ := h
  cases s with
  | plus =>
    -- `hasHi` is true, so `step` bisects upward: new bracket is `[value, hi]`.
    refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩ <;>
      simp only [GonshorState.step, GonshorState.gap, hhi, if_true] <;>
      rw [hmid] <;> ring_nf <;> linarith
  | minus =>
    -- `hasLo` is true, so `step` bisects downward: new bracket is `[lo, value]`.
    refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩ <;>
      simp only [GonshorState.step, GonshorState.gap, hlo, if_true] <;>
      rw [hmid] <;> ring_nf <;> linarith

/-- **`n` signs shrink the bracket by `2ⁿ`.**

This is the rate the trajectory statement needs: prefix length `n` buys a bracket of width
`gap₀ / 2ⁿ`, so the approximant is within `gap₀ / 2ⁿ⁺¹` of anything the bracket still
contains — a dyadic approximation whose denominator is exponential in the prefix length,
which is exactly the quantity a Liouville exponent is measured against. -/
theorem Bracketed.foldl_gap (l : List Sign) :
    ∀ st : GonshorState, Bracketed st →
      Bracketed (l.foldl GonshorState.step st)
      ∧ (l.foldl GonshorState.step st).gap = st.gap / 2 ^ l.length := by
  induction l with
  | nil => intro st h; simpa using h
  | cons s t ih =>
    intro st h
    obtain ⟨hstep, hgap⟩ := Bracketed.step st h s
    obtain ⟨hb, hg⟩ := ih (st.step s) hstep
    refine ⟨hb, ?_⟩
    rw [List.foldl_cons] at *
    rw [hg, hgap, List.length_cons, pow_succ]
    ring

/-- The bracket stays positive, so the rate above is a genuine contraction rather than a
statement about an empty interval. -/
theorem Bracketed.gap_pos {st : GonshorState} (h : Bracketed st) : 0 < st.gap := by
  have := h.lt
  simp only [GonshorState.gap]
  linarith

/-! ### ⚠ Non-vacuity — without this the whole module proves nothing

Everything above is conditional on `Bracketed`. If no state reachable from
`GonshorState.init` ever satisfied it, all of it would be vacuously true and the module
would be an instance of exactly the degeneracy
`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md` catalogues — a statement
whose *form* suggests content it does not carry.

So the regime is exhibited, not assumed. `[+, -]` is the shortest sign sequence that
brackets: `+` steps to `1` with no upper bound, then `-` finds `hasLo` set and bisects,
producing `1/2` inside `(0, 1)`. -/

/-- **The bisection regime is reached**, by the shortest sequence that reaches it. -/
theorem bracketed_plus_minus :
    Bracketed ([Sign.plus, Sign.minus].foldl GonshorState.step GonshorState.init) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    norm_num [GonshorState.step, GonshorState.init]

/-- **The rate, on a concrete sequence.**  Extending `[+, -]` by `k` further signs leaves a
bracket of width `2⁻ᵏ`, since `[+, -]` brackets `(0, 1)` at width `1`.

This is the statement a Liouville comparison consumes: prefix length controls approximation
quality exponentially, with the dyadic denominator that `2ⁿ` names. -/
theorem gap_after_plus_minus (l : List Sign) :
    ((Sign.plus :: Sign.minus :: l).foldl GonshorState.step GonshorState.init).gap
      = 1 / 2 ^ l.length := by
  have h := (Bracketed.foldl_gap l _ bracketed_plus_minus).2
  have hg : ([Sign.plus, Sign.minus].foldl GonshorState.step GonshorState.init).gap = 1 := by
    norm_num [GonshorState.step, GonshorState.init, GonshorState.gap]
  -- Rewrite `h` BEFORE simping: `simpa [hg]` normalises the `foldl` on both sides first,
  -- after which `hg`'s literal `[Sign.plus, Sign.minus].foldl` no longer matches anything.
  rw [hg] at h
  simpa using h

/-! ### The sign expansion of a real, and the fact that it brackets its target

Everything above concerns `gonshor`'s own bracket.  To compare against a Liouville
exponent one needs a **given `α`** inside that bracket, which means a map
`ℝ → sign sequence` — the thing `SignSequence.lean` does not define and whose absence
`DiophantineBirthdayTrajectory` records as the remaining gap.

It is the obvious greedy rule, and it is `GonshorState.step` read backwards: emit `+` when
the current value undershoots `α`, `-` otherwise.  Noncomputable because comparing a real
to a rational is not decidable; that is a statement about `ℝ`, not about this construction. -/

open scoped Classical in
/-- The state after `n` signs of `α`'s own expansion. -/
noncomputable def expandState (α : ℝ) : ℕ → GonshorState
  | 0 => GonshorState.init
  | n + 1 =>
      let st := expandState α n
      st.step (if (st.value : ℝ) < α then Sign.plus else Sign.minus)

/-- `α` lies within the state's bracket — weakly, so that a rational `α` landing exactly on
a bound is covered rather than excluded. -/
def Brackets (α : ℝ) (st : GonshorState) : Prop :=
  (st.hasLo = true → (st.lo : ℝ) ≤ α) ∧ (st.hasHi = true → α ≤ (st.hi : ℝ))

open scoped Classical in
/-- **The expansion always brackets its target.**

Induction on `n`.  The base case is vacuous — `init` has neither bound set — and each step
re-establishes the invariant by construction: a `+` moves the *lower* bound up to a value
known to undershoot `α`, a `-` moves the *upper* bound down to one known not to. -/
theorem expandState_brackets (α : ℝ) : ∀ n, Brackets α (expandState α n) := by
  intro n
  induction n with
  | zero => exact ⟨by simp [expandState, GonshorState.init], by simp [expandState, GonshorState.init]⟩
  | succ n ih =>
    obtain ⟨ihlo, ihhi⟩ := ih
    rw [expandState]
    by_cases hlt : ((expandState α n).value : ℝ) < α
    · -- `+`: the new lower bound is the old value, which undershoots `α`.
      simp only [hlt, if_true]
      by_cases hhi : (expandState α n).hasHi = true <;>
        simp only [GonshorState.step, hhi, if_true, if_false, Bool.not_eq_true] at * <;>
        exact ⟨fun _ => le_of_lt hlt, by simpa using ihhi⟩
    · -- `-`: the new upper bound is the old value, which does not undershoot `α`.
      simp only [hlt, if_false]
      by_cases hlo : (expandState α n).hasLo = true <;>
        simp only [GonshorState.step, hlo, if_true, if_false, Bool.not_eq_true] at * <;>
        exact ⟨by simpa using ihlo, fun _ => not_lt.mp hlt⟩

/-- **The approximation bound.**  When the state both brackets `α` and is in the bisection
regime, its value is within the bracket width of `α`.

Both `α` and `value` lie in `[lo, hi]` — `α` by `Brackets`, `value` strictly by
`Bracketed` — so they differ by at most the width. -/
theorem dist_le_gap {α : ℝ} {st : GonshorState}
    (hb : Bracketed st) (hbr : Brackets α st) :
    |α - (st.value : ℝ)| ≤ (st.gap : ℝ) := by
  obtain ⟨hlo, hhi, hmid, hlt⟩ := hb
  obtain ⟨bl, bh⟩ := hbr
  have hα_lo : ((st.lo : ℚ) : ℝ) ≤ α := bl hlo
  have hα_hi : α ≤ ((st.hi : ℚ) : ℝ) := bh hhi
  have hv : (st.value : ℝ) = (((st.lo + st.hi) / 2 : ℚ) : ℝ) := by rw [hmid]
  have hgap : (st.gap : ℝ) = ((st.hi : ℚ) : ℝ) - ((st.lo : ℚ) : ℝ) := by
    simp [GonshorState.gap]
  rw [abs_le]
  constructor <;> · rw [hv, hgap]; push_cast; linarith

/-- **The payoff**: the expansion of `α`, once it has bracketed, approximates `α` to within
its bracket width — and `Bracketed.foldl_gap` says that width halves per sign.

This is the statement `DiophantineBirthdayTrajectory` wanted and could not state: prefix
length controls approximation quality, with an exponential dyadic denominator, for a *given*
real. -/
theorem dist_le_gap_of_expansion (α : ℝ) (n : ℕ) (hb : Bracketed (expandState α n)) :
    |α - ((expandState α n).value : ℝ)| ≤ ((expandState α n).gap : ℝ) :=
  dist_le_gap hb (expandState_brackets α n)

open scoped Classical in
/-- **The expansion's own bracket halves per sign.**

`Bracketed.foldl_gap` says this for a `List.foldl`; `expandState` is defined by recursion
on `ℕ` instead, so the two need connecting.  They connect directly through
`Bracketed.step` — no list bookkeeping required, because `expandState α (n+1)` is literally
one `step` applied to `expandState α n`. -/
theorem expandState_gap (α : ℝ) (n : ℕ) (hb : Bracketed (expandState α n)) :
    ∀ k, Bracketed (expandState α (n + k))
      ∧ (expandState α (n + k)).gap = (expandState α n).gap / 2 ^ k := by
  intro k
  induction k with
  | zero => simpa using hb
  | succ k ih =>
    obtain ⟨hbk, hgk⟩ := ih
    obtain ⟨hb', hg'⟩ := Bracketed.step _ hbk
      (if ((expandState α (n + k)).value : ℝ) < α then Sign.plus else Sign.minus)
    refine ⟨by rw [← Nat.add_assoc]; rw [expandState]; exact hb', ?_⟩
    rw [← Nat.add_assoc, expandState]
    rw [hg', hgk, pow_succ]
    ring

/-- **The bridge, in one statement.**  For *any* real `α`, once its expansion has bracketed,
`k` further signs approximate `α` to within `gap / 2ᵏ`.

This is what `conj:diophantine-birthday`'s "birthday **trajectory**" needs on the surreal
side: prefix length controls approximation quality, the denominator is exponential in the
prefix length, and the target is a genuine given real rather than the expansion's own
bracket. -/
theorem expansion_approximates (α : ℝ) (n : ℕ) (hb : Bracketed (expandState α n)) (k : ℕ) :
    |α - ((expandState α (n + k)).value : ℝ)|
      ≤ (((expandState α n).gap / 2 ^ k : ℚ) : ℝ) := by
  obtain ⟨hbk, hgk⟩ := expandState_gap α n hb k
  have := dist_le_gap_of_expansion α (n + k) hbk
  rwa [hgk] at this

/-! ### Runs, and why they are where the Liouville exponent lives

`expansion_approximates` gives error `gap / 2ᵏ` at a state whose own denominator has also
grown by `2ᵏ`.  That is error `≈ 1/q` — approximation **exponent 1**, which
`LiouvilleWith.liouvilleWith_one` gives for *every* real for free.  So the bracket rate on
its own certifies nothing, and it would be easy to mistake it for progress.

The exponent lives in the **run structure**.  A `+` step keeps `hi` and raises `lo`; a `-`
step keeps `lo` and lowers `hi`.  So a **run of `k` identical signs freezes one endpoint**
while the bracket keeps halving — leaving a rational fixed at step `n`, with denominator
from step `n`, that approximates `α` to accuracy `2⁻ᵏ` better.  Error `1/q^{(n+k)/n}` rather
than `1/q`: the exponent is the run length relative to the prefix length, which is exactly
the shape of a Liouville condition. -/

/-- A `+` step leaves the **upper** bound alone (it raises the lower one). -/
theorem step_plus_hi (st : GonshorState) (h : Bracketed st) :
    (st.step Sign.plus).hi = st.hi := by
  simp [GonshorState.step, h.hasHi]

/-- **A run of `+` freezes the upper bound.**  Induction on the run length, using that each
step both preserves the bisection regime and leaves `hi` untouched. -/
theorem foldl_replicate_plus_hi (k : ℕ) (st : GonshorState) (h : Bracketed st) :
    ((List.replicate k Sign.plus).foldl GonshorState.step st).hi = st.hi
      ∧ Bracketed ((List.replicate k Sign.plus).foldl GonshorState.step st) := by
  induction k generalizing st with
  | zero => simpa using h
  | succ k ih =>
    obtain ⟨hb', _⟩ := Bracketed.step st h Sign.plus
    obtain ⟨hhi, hbk⟩ := ih (st.step Sign.plus) hb'
    refine ⟨?_, ?_⟩
    · rw [List.replicate_succ, List.foldl_cons, hhi, step_plus_hi st h]
    · rw [List.replicate_succ, List.foldl_cons]; exact hbk

/-- **The Liouville-shaped statement.**  After a run of `k` plus-signs, `α` is within
`gap / 2ᵏ` of `st.hi` — a rational **fixed before the run began**.

The denominator is whatever `st.hi` already had; the accuracy improves by `2ᵏ` without it
growing. That decoupling is what an approximation exponent above `1` means, and it is
supplied by the run rather than by the bisection rate. -/
theorem run_plus_approximates {α : ℝ} {st : GonshorState} (k : ℕ) (hb : Bracketed st)
    (hbr : Brackets α ((List.replicate k Sign.plus).foldl GonshorState.step st)) :
    |α - ((st.hi : ℚ) : ℝ)| ≤ (((st.gap / 2 ^ k : ℚ)) : ℝ) := by
  obtain ⟨hhi, hbk⟩ := foldl_replicate_plus_hi k st hb
  have hgap := (Bracketed.foldl_gap (List.replicate k Sign.plus) st hb).2
  rw [List.length_replicate] at hgap
  obtain ⟨bl, bh⟩ := hbr
  -- `α` sits in the final bracket, whose top is still `st.hi` and whose width is `gap/2ᵏ`.
  have hlo : ((((List.replicate k Sign.plus).foldl GonshorState.step st).lo : ℚ) : ℝ) ≤ α :=
    bl hbk.hasLo
  have hhi' : α ≤ ((st.hi : ℚ) : ℝ) := by
    have := bh hbk.hasHi
    rwa [hhi] at this
  -- `gap` is *definitionally* `hi - lo`, but `linarith` treats it as an opaque atom, so
  -- the identity has to be handed over explicitly on both the old and the new state.
  have hgd : st.gap = st.hi - st.lo := rfl
  have hpos : (0 : ℚ) < st.gap / 2 ^ k :=
    div_pos hb.gap_pos (by positivity)
  have hwidth : (((List.replicate k Sign.plus).foldl GonshorState.step st).lo : ℚ)
      = st.hi - st.gap / 2 ^ k := by
    have hg : ((List.replicate k Sign.plus).foldl GonshorState.step st).gap
        = st.gap / 2 ^ k := hgap
    simp only [GonshorState.gap] at hg
    rw [hhi] at hg
    -- `simp only [GonshorState.gap]` unfolded the RIGHT side too, so `hg` now reads
    -- `st.hi - lo_k = (st.hi - st.lo) / 2 ^ k` while the goal says `st.gap / 2 ^ k`.
    -- `linarith` cannot divide, so those are two unrelated atoms to it: fold the
    -- subtraction back into `gap` before asking.
    rw [← hgd] at hg
    linarith
  have hposR : (0 : ℝ) ≤ ((st.gap / 2 ^ k : ℚ) : ℝ) := by exact_mod_cast hpos.le
  rw [abs_le]
  refine ⟨?_, by linarith⟩
  rw [hwidth] at hlo
  push_cast at hlo ⊢
  linarith

/-! ### Runs in `α`'s own expansion

`run_plus_approximates` is stated for an arbitrary `List.replicate k Sign.plus` fold.  To
apply it to `α`'s *own* expansion one needs to know that the greedy rule actually emitted
`+` at each of those steps — which it does exactly when the current value undershoots `α`.
That is the definition of the rule, so the bridge is short; it is stated separately because
without it the run lemma has nothing to attach to. -/

open scoped Classical in
/-- A step where the value undershoots `α` is a `+` step. -/
theorem expandState_succ_plus (α : ℝ) (n : ℕ)
    (h : ((expandState α n).value : ℝ) < α) :
    expandState α (n + 1) = (expandState α n).step Sign.plus := by
  rw [expandState]; simp [h]

open scoped Classical in
/-- **`α` undershot at every step of the window ⟹ that window is a plus-run.**

The hypothesis is a statement about `α` — it says the expansion's value stayed below `α`
for `k` consecutive steps — and the conclusion puts `expandState` into the shape
`run_plus_approximates` consumes. -/
theorem expandState_plus_run (α : ℝ) (n : ℕ) :
    ∀ k, (∀ j, j < k → ((expandState α (n + j)).value : ℝ) < α) →
      expandState α (n + k)
        = (List.replicate k Sign.plus).foldl GonshorState.step (expandState α n) := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ k ih =>
    intro h
    have hk := ih fun j hj => h j (Nat.lt_succ_of_lt hj)
    rw [← Nat.add_assoc, expandState_succ_plus α (n + k) (h k (Nat.lt_succ_self k)), hk,
      List.replicate_succ']
    simp [List.foldl_append]

/-! ### The denominator invariant — what turns a run into an *exponent*

`run_plus_approximates` says `α` is within `gap / 2ᵏ` of `st.hi`.  To read that as an
approximation **exponent** one needs `st.hi` as `m / q` with `q` known, and `GonshorState`
stores bare `ℚ` with no denominator information at all.  This supplies it: every bound
after `n` steps is a dyadic with denominator dividing `2ⁿ`.

Both regimes preserve it, for different reasons — the unbounded `±1` moves keep the
denominator exactly, and the bisecting moves at worst double it. -/

/-- `x` is a dyadic rational with denominator dividing `2ⁿ`.

⚠ Stated **multiplicatively** (`2ⁿ · x` is an integer) rather than as `x = m / 2ⁿ`.  The
division form is the natural reading but it defeats `ring`: closing the step cases needs
`2ⁿ / 2ⁿ = 1`, which `ring` cannot do without knowing `2ⁿ ≠ 0`, so every case would need
`field_simp` and a side condition.  Multiplied through, all four cases are `ring`
identities. -/
def IsDyadicAt (n : ℕ) (x : ℚ) : Prop := ∃ m : ℤ, (2 : ℚ) ^ n * x = (m : ℚ)

/-- A dyadic at level `n` is a dyadic at level `n + 1`. -/
theorem IsDyadicAt.succ {n : ℕ} {x : ℚ} (h : IsDyadicAt n x) : IsDyadicAt (n + 1) x := by
  obtain ⟨m, hm⟩ := h
  exact ⟨2 * m, by push_cast; linear_combination 2 * hm⟩

/-- All three bounds are dyadic at level `n`. -/
def DyadicState (n : ℕ) (st : GonshorState) : Prop :=
  IsDyadicAt n st.value ∧ IsDyadicAt n st.lo ∧ IsDyadicAt n st.hi

/-- `init` is dyadic at level `0` — every bound is `0`. -/
theorem dyadicState_init : DyadicState 0 GonshorState.init :=
  ⟨⟨0, by simp [GonshorState.init]⟩, ⟨0, by simp [GonshorState.init]⟩,
   ⟨0, by simp [GonshorState.init]⟩⟩

/-- **One step at most doubles the denominator.**

The four cases split by regime rather than by sign: `±1` keeps the denominator (add
`±2ⁿ` to the numerator), and the two bisecting cases average two level-`n` dyadics, which
lands at level `n + 1`. -/
theorem DyadicState.step {n : ℕ} {st : GonshorState} (h : DyadicState n st) (s : Sign) :
    DyadicState (n + 1) (st.step s) := by
  obtain ⟨⟨a, ha⟩, ⟨b, hb⟩, ⟨c, hc⟩⟩ := h
  cases s with
  | plus =>
    by_cases hhi : st.hasHi = true
    · -- bisect up: value ↦ (value + hi)/2, lo ↦ value, hi ↦ hi
      refine ⟨⟨a + c, ?_⟩, ⟨2 * a, ?_⟩, ⟨2 * c, ?_⟩⟩ <;>
        simp only [GonshorState.step, hhi, if_true] <;> push_cast
      · linear_combination ha + hc
      · linear_combination 2 * ha
      · linear_combination 2 * hc
    · -- step up by 1: value ↦ value + 1, lo ↦ value, hi unused (0)
      simp only [Bool.not_eq_true] at hhi
      refine ⟨⟨2 * a + 2 ^ (n + 1), ?_⟩, ⟨2 * a, ?_⟩, ⟨0, ?_⟩⟩ <;>
        simp only [GonshorState.step, hhi, if_false] <;> push_cast
      · linear_combination 2 * ha
      · linear_combination 2 * ha
      · ring
  | minus =>
    by_cases hlo : st.hasLo = true
    · -- bisect down: value ↦ (lo + value)/2, lo ↦ lo, hi ↦ value
      refine ⟨⟨b + a, ?_⟩, ⟨2 * b, ?_⟩, ⟨2 * a, ?_⟩⟩ <;>
        simp only [GonshorState.step, hlo, if_true] <;> push_cast
      · linear_combination hb + ha
      · linear_combination 2 * hb
      · linear_combination 2 * ha
    · -- step down by 1: value ↦ value − 1, lo unused (0), hi ↦ value
      simp only [Bool.not_eq_true] at hlo
      refine ⟨⟨2 * a - 2 ^ (n + 1), ?_⟩, ⟨0, ?_⟩, ⟨2 * a, ?_⟩⟩ <;>
        simp only [GonshorState.step, hlo, if_false] <;> push_cast
      · linear_combination 2 * ha
      · ring
      · linear_combination 2 * ha

open scoped Classical in
/-- **Every bound of `α`'s expansion after `n` steps is a dyadic with denominator dividing
`2ⁿ`.**

This is the piece that was missing: it names the `q` in `|α − m/q|`, so a run of length `k`
at step `n` reads as an approximation of exponent `(n + k)/n` rather than merely as a small
error. -/
theorem expandState_dyadic (α : ℝ) : ∀ n, DyadicState n (expandState α n) := by
  intro n
  induction n with
  | zero => simpa [expandState] using dyadicState_init
  | succ n ih => rw [expandState]; exact ih.step _

/-! ### The three pieces, assembled

`run_plus_approximates` (accuracy), `expandState_dyadic` (denominator) and
`expandState_plus_run` (that the window really is a run) each say something partial.  Put
together they give the shape a Diophantine exponent is read off: an explicit rational
`m / 2ⁿ` with the error controlled by the *run length* rather than by `n`. -/

open scoped Classical in
/-- **A run of `k` in `α`'s expansion gives a dyadic of denominator `2ⁿ` accurate to
`gapₙ / 2ᵏ`.**

Denominator fixed by `n`; accuracy improving with `k`. That is the decoupling an
approximation exponent above `1` consists of, now stated for a *given* real and an
*explicit* rational. -/
theorem expansion_run_approximates (α : ℝ) (n k : ℕ)
    (hb : Bracketed (expandState α n))
    (hrun : ∀ j, j < k → ((expandState α (n + j)).value : ℝ) < α) :
    ∃ m : ℤ, |α - (m : ℝ) / 2 ^ n| ≤ (((expandState α n).gap / 2 ^ k : ℚ) : ℝ) := by
  obtain ⟨m, hm⟩ := (expandState_dyadic α n).2.2
  refine ⟨m, ?_⟩
  have hbr : Brackets α
      ((List.replicate k Sign.plus).foldl GonshorState.step (expandState α n)) := by
    rw [← expandState_plus_run α n k hrun]; exact expandState_brackets α (n + k)
  have hmain := run_plus_approximates k hb hbr
  -- `hm` is the multiplicative dyadic form; turn it into `hi = m / 2ⁿ`.
  have h2 : (2 : ℚ) ^ n ≠ 0 := by positivity
  have hhi : (expandState α n).hi = (m : ℚ) / 2 ^ n := by
    field_simp at hm ⊢; linarith [hm]
  rwa [hhi, Rat.cast_div, Rat.cast_intCast, Rat.cast_pow, Rat.cast_ofNat] at hmain

/-! ### From a run to an approximation *exponent*

`expansion_run_approximates` bounds the error by `gapₙ / 2ᵏ` against a denominator `2ⁿ`.
Reading that as an exponent means comparing it to `1 / (2ⁿ)ᵗ`, which needs the run length
`k` measured **against `n`** rather than absolutely: `k ≥ n·t` is exactly what buys
exponent `t`.

⚠ `gapₙ ≤ 1` is taken as a hypothesis rather than derived. It is always true at the first
bracketed step — an unbounded `+` sets `lo := value` and `value := value + 1`, so the
following `-` bisects an interval of width exactly `1`, and every later gap is smaller —
but proving "the first bracketed step" requires reasoning about when the bounds first
appear, which is a separate induction and not needed for the statement below. -/

open scoped Classical in
/-- **A run of `k ≥ n·t` signs gives approximation exponent `t`.**

The conclusion is the Diophantine form: an explicit rational of denominator `q = 2ⁿ` with
error at most `1 / qᵗ`. The run length is what supplies `t`; the bisection rate alone
supplies only `t = 1`, which every real has for free. -/
theorem approx_exponent_of_run (α : ℝ) (n k t : ℕ)
    (hb : Bracketed (expandState α n))
    (hg : (expandState α n).gap ≤ 1)
    (hrun : ∀ j, j < k → ((expandState α (n + j)).value : ℝ) < α)
    (hk : n * t ≤ k) :
    ∃ m : ℤ, |α - (m : ℝ) / 2 ^ n| ≤ 1 / ((2 : ℝ) ^ n) ^ t := by
  obtain ⟨m, hm⟩ := expansion_run_approximates α n k hb hrun
  refine ⟨m, hm.trans ?_⟩
  -- `gapₙ / 2ᵏ ≤ 1 / 2ᵏ ≤ 1 / 2^(n·t) = 1 / (2ⁿ)ᵗ`
  have hgR : (((expandState α n).gap : ℚ) : ℝ) ≤ 1 := by exact_mod_cast hg
  have h2k : (0 : ℝ) < 2 ^ k := by positivity
  have hstep : (((expandState α n).gap / 2 ^ k : ℚ) : ℝ)
      = (((expandState α n).gap : ℚ) : ℝ) / 2 ^ k := by push_cast; ring
  rw [hstep]
  have h1 : (((expandState α n).gap : ℚ) : ℝ) / 2 ^ k ≤ 1 / 2 ^ k := by gcongr
  refine h1.trans ?_
  have hpow : ((2 : ℝ) ^ n) ^ t = 2 ^ (n * t) := by rw [← pow_mul]
  rw [hpow]
  -- `gcongr` discharges BOTH side conditions from context (`1 ≤ 2` by `norm_num`, and
  -- `n * t ≤ k` from `hk`).  Supplying them as bullets afterwards fails with "No goals to
  -- be solved" — the same shape as the cofactor-0 case in the gluing generator, where a
  -- tactic closing more than expected reads as a broken proof rather than a finished one.
  gcongr <;> norm_num

/-! ### ⚠ Non-vacuity of the expansion, for the same reason as before

`Brackets` is two implications *guarded* by `hasLo` / `hasHi`, and `dist_le_gap_of_expansion`
is conditional on `Bracketed`.  If the expansion never set those flags, both would hold
vacuously and this section would prove nothing about any real.

So the regime is exhibited on a concrete target.  For `α = 1/2`: step 0 has value `0 < 1/2`
and emits `+`, reaching value `1` with a lower bound only; step 1 has value `1`, which does
*not* undershoot, so it emits `-`, finds `hasLo` set, and bisects into `(0, 1)`. -/

open scoped Classical in
/-- The expansion of a concrete real reaches the bisection regime — so `Bracketed` is a
condition the expansion actually meets, not a hypothesis that is never discharged. -/
theorem expandState_half_bracketed : Bracketed (expandState (1/2 : ℝ) 2) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    norm_num [expandState, GonshorState.step, GonshorState.init]

open scoped Classical in
/-- …and both bound flags are genuinely set there, so `Brackets` is a real constraint at
that state rather than two vacuous implications. -/
theorem expandState_half_flags :
    (expandState (1/2 : ℝ) 2).hasLo = true ∧ (expandState (1/2 : ℝ) 2).hasHi = true := by
  norm_num [expandState, GonshorState.step, GonshorState.init]

/-! And the same question one level up, for the **run** hypothesis.

`expansion_run_approximates` is conditional on `∀ j < k, value undershoots α`. At `k = 0`
that is vacuously true and the theorem degenerates to "the value is within one bracket
width", which is `dist_le_gap` again. So the content is entirely in whether a **positive**
`k` is ever satisfied, and that needs exhibiting.

`α = 9/10` runs: after `[+, -]` the value is `1/2`, and `1/2` then `3/4` both undershoot
`9/10`, so the expansion emits `+` twice more. -/

open scoped Classical in
/-- A real whose expansion genuinely plus-runs, so the run hypothesis is satisfiable at
`k = 2` and not only at `k = 0`. -/
theorem expandState_nineTenths_runs :
    Bracketed (expandState (9/10 : ℝ) 2)
      ∧ ∀ j, j < 2 → ((expandState (9/10 : ℝ) (2 + j)).value : ℝ) < 9/10 := by
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩
  · norm_num [expandState, GonshorState.step, GonshorState.init]
  · norm_num [expandState, GonshorState.step, GonshorState.init]
  · norm_num [expandState, GonshorState.step, GonshorState.init]
  · norm_num [expandState, GonshorState.step, GonshorState.init]
  · intro j hj
    interval_cases j <;> norm_num [expandState, GonshorState.step, GonshorState.init]

open scoped Classical in
/-- The headline instantiated on that real: a dyadic of denominator `4` approximating
`9/10` to within `gap₂ / 4`. Discharges every hypothesis of
`expansion_run_approximates`, which is what makes it applicable rather than merely true. -/
theorem nineTenths_run_approximates :
    ∃ m : ℤ, |(9/10 : ℝ) - (m : ℝ) / 2 ^ 2|
      ≤ (((expandState (9/10 : ℝ) 2).gap / 2 ^ 2 : ℚ) : ℝ) :=
  expansion_run_approximates _ 2 2 expandState_nineTenths_runs.1 expandState_nineTenths_runs.2

open scoped Classical in
/-- …and the **exponent** form on the same real, discharging its extra `gapₙ ≤ 1`
hypothesis too. `n = 2`, `k = 2`, `t = 1`: the run is exactly long enough for exponent `1`.

Only `t = 1` here, which is the exponent every real has for free — `9/10` is rational and
has no long runs to give more. That is the honest witness: it shows the theorem *applies*,
not that this `α` is interesting. A witness with `t ≥ 2` would need a real chosen for its
run structure, which is the number theory this lane deliberately does not attempt. -/
theorem nineTenths_exponent_one :
    ∃ m : ℤ, |(9/10 : ℝ) - (m : ℝ) / 2 ^ 2| ≤ 1 / ((2 : ℝ) ^ 2) ^ 1 :=
  approx_exponent_of_run _ 2 2 1 expandState_nineTenths_runs.1
    (by norm_num [expandState, GonshorState.step, GonshorState.init, GonshorState.gap])
    expandState_nineTenths_runs.2 (by norm_num)

end QOU.AppendixSurreals
