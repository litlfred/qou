import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# The `e_inf` search is over a finite set

`EdgeDecoupling` says the `REV_n` excess *decomposes* into three pieces that stop interacting.
This file is about the maximisation that decomposition leaves behind,

    e_inf  =  max over (a, b) of  [ f a + h (a + b) + g b ] ,

where `f` and `g` are the two edge energies as functions of their block sums and `h` is the run.
The maximisation ranges over all pairs of naturals, so on its face it is an infinite search.  It
is not, and the reason is elementary: `f` and `g` are bounded above while `h` falls without
bound, so a pair whose sum is large enough cannot compete with any incumbent.

Two results, of different kinds, matching the two halves of the argument.

`sub_le_mul_of_antitone_step` and `sub_le_neg_mul_of_antitone_step` are the **linearisation**.
A sequence whose downward steps `δ` are antitone — `e` "convex decreasing", in the discrete
sense — satisfies

    e a - e (a + D)  ≤  D · δ a          and          e a - e (a - D)  ≤  - (D · δ a) ,

i.e. one inequality with `D` carrying its own sign.  Both are inductions on `D` over an
`Antitone` hypothesis: no derivative, no integral, no `Real.log`.  This is what turns each pair
term of the block energy into something linear in the displacement, which is the step that makes
the whole pair sum telescope.

`join_lt_of_lt_sum` and `le_of_le_join` are the **reduction**.  If `f, g ≤ B` everywhere and
`h ℓ < V - 2B` past `L`, then no pair with `a + b > L` reaches `V` — so a pair that matches an
incumbent `V` must lie in the finite window `a + b ≤ L`.  Pure order arithmetic; it holds for
whatever `f`, `g`, `h` happen to be.

## Why the `REV_n` arc wanted this

`rev_e_infinity_search_reduction_probe.py` instantiates both.  For the linearisation it takes
`e = ε` with `ε(m) = -log(1 - q₀^{-2m})` and `δ(m) = ε(m) - ε(m+1)`, checks the inequality on a
grid of 2130 `(d, D)` pairs with both signs of `D`, and then uses it to bound every block
uniformly in its length *and* its entries — the bound `B_rig` that makes `L` exist.  For the
reduction it takes `V` to be the incumbent `e_inf` and reports the resulting window: `a + b ≤
345` from the rigorous constants, `≤ 23` from the measured ones.

Both signs of `D` are load-bearing and the probe says so.  Keeping only `D⁺` — dropping the
negative pair terms — makes the bound diverge, because nothing then stops a long alternating
profile from collecting `δ(1)` per step at merely linear cost.

What none of this does is close the search.  It makes the search *finite*; which finite set is
enough, and whether the enumerated maximum is the true one, are separate questions the probe
records as open.

| | |
|---|---|
| `sub_le_mul_of_antitone_step` | antitone steps ⇒ `e a - e (a + D) ≤ D · δ a` |
| `sub_le_neg_mul_of_antitone_step` | the same inequality below `a`, with `D` negative |
| `join_lt_of_lt_sum` | a pair past the window cannot reach `V` |
| `le_of_le_join` | so a pair that reaches `V` lies in the window |

-- Ref: [leitner2026] `computations/deltalambda/rev_e_infinity_search_reduction_probe.py`
-/

namespace QOU.BraidKnot.SearchCoercivity

variable {e δ : ℕ → ℝ}

/-- **Linearisation, upward.** If the downward steps `δ` of `e` are antitone, then dropping `D`
places costs at most `D` copies of the *first* step.

`δ` antitone is the discrete form of "`e` is convex decreasing": later steps are no larger than
earlier ones, so the first one dominates the average. -/
theorem sub_le_mul_of_antitone_step
    (hstep : ∀ m, e m - e (m + 1) = δ m) (hδ : Antitone δ) (a D : ℕ) :
    e a - e (a + D) ≤ (D : ℝ) * δ a := by
  induction D with
  | zero => simp
  | succ n ih =>
      have hrw : a + (n + 1) = (a + n) + 1 := by omega
      have hs : e (a + n) - e ((a + n) + 1) = δ (a + n) := hstep (a + n)
      have hmono : δ (a + n) ≤ δ a := hδ (Nat.le_add_right a n)
      have hexp : ((n : ℝ) + 1) * δ a = (n : ℝ) * δ a + δ a := by ring
      rw [hrw]
      push_cast
      linarith

/-- **Linearisation, downward.** The same inequality on the other side of `a`: climbing `D`
places *gains* at least `D` copies of the first step, so the signed statement is uniform.

This is the half an agent drops, and dropping it is what makes the bound in the `REV_n` arc
diverge — the negative pair terms are exactly what stops a long alternating displacement from
collecting the largest step over and over at linear cost. -/
theorem sub_le_neg_mul_of_antitone_step
    (hstep : ∀ m, e m - e (m + 1) = δ m) (hδ : Antitone δ) (a D : ℕ) (hDa : D ≤ a) :
    e a - e (a - D) ≤ -((D : ℝ) * δ a) := by
  induction D with
  | zero => simp
  | succ n ih =>
      have hn : n ≤ a := by omega
      have ih' := ih hn
      have hrw : a - (n + 1) + 1 = a - n := by omega
      have hs : e (a - (n + 1)) - e (a - (n + 1) + 1) = δ (a - (n + 1)) := hstep _
      have hmono : δ a ≤ δ (a - (n + 1)) := hδ (by omega)
      have hexp : ((n : ℝ) + 1) * δ a = (n : ℝ) * δ a + δ a := by ring
      rw [hrw] at hs
      push_cast
      linarith

/-- **The reduction.** With `f` and `g` bounded above by `B` and `h` below `V - 2B` past `L`,
a pair whose sum exceeds `L` cannot reach `V`.

Nothing here knows what `f`, `g` or `h` are: it is the observation that a bounded-plus-bounded
sum cannot rescue a term that has fallen far enough. -/
theorem join_lt_of_lt_sum {f g h : ℕ → ℝ} {B V : ℝ} {L : ℕ}
    (hf : ∀ a, f a ≤ B) (hg : ∀ b, g b ≤ B)
    (hh : ∀ l, L < l → h l < V - 2 * B)
    {a b : ℕ} (hab : L < a + b) :
    f a + h (a + b) + g b < V := by
  have h1 := hf a
  have h2 := hg b
  have h3 := hh (a + b) hab
  linarith

/-- **The finite window.** Contrapositive of `join_lt_of_lt_sum`: a pair that matches the
incumbent `V` lies in `a + b ≤ L`, so the maximisation is over a finite set. -/
theorem le_of_le_join {f g h : ℕ → ℝ} {B V : ℝ} {L : ℕ}
    (hf : ∀ a, f a ≤ B) (hg : ∀ b, g b ≤ B)
    (hh : ∀ l, L < l → h l < V - 2 * B)
    {a b : ℕ} (hV : V ≤ f a + h (a + b) + g b) :
    a + b ≤ L := by
  by_contra hcon
  exact absurd hV (not_le.mpr (join_lt_of_lt_sum hf hg hh (Nat.lt_of_not_le hcon)))

end QOU.BraidKnot.SearchCoercivity
