import Mathlib.Algebra.BigOperators.Ring.Finset
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
| `one_body_sub_le_mul_of_antitone` | antitone `e` ⇒ one-body gain `fi (b + D) - fi b ≤ D · e (b + 1)` |
| `ghatBot` | per-row bottom-frame slope: one-body + rows below (`<`) − rows above (`>`) |
| `ghatBot_frame_bound` | finite-sum assembly of the per-row bound over `[Fintype ι]` |
| `sum_ghatBot_frame_bound` | multi-row sum of the `ghatBot` frame bound over a displacement profile `u` |
| `join_lt_of_lt_sum` | a pair past the window cannot reach `V` |
| `le_of_le_join` | so a pair that reaches `V` lies in the window |

-- Ref: [leitner2026] `computations/deltalambda/rev_e_infinity_search_reduction_probe.py`
-- Ref: [leitner2026] `computations/deltalambda/rev_e_infinity_xbot_coercivity_probe.py`
-/

namespace QOU.BraidKnot.SearchCoercivity

open Finset

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

/-- **One-body linearisation.** If the upward steps of the one-body potential `fi` are `e (m + 1)`
and `e` is antitone, then displacing a row from `b` to `b + D` gains at most `D * e (b + 1)`. -/
theorem one_body_sub_le_mul_of_antitone {fi : ℕ → ℝ}
    (hfi : ∀ m, fi (m + 1) - fi m = e (m + 1)) (he : Antitone e) (b D : ℕ) :
    fi (b + D) - fi b ≤ (D : ℝ) * e (b + 1) := by
  induction D with
  | zero => simp
  | succ n ih =>
      have hrw : b + (n + 1) = (b + n) + 1 := by omega
      have hs : fi ((b + n) + 1) - fi (b + n) = e ((b + n) + 1) := hfi (b + n)
      have hmono : e ((b + n) + 1) ≤ e (b + 1) := he (by omega)
      have hexp : ((n : ℝ) + 1) * e (b + 1) = (n : ℝ) * e (b + 1) + e (b + 1) := by ring
      rw [hrw]
      push_cast
      linarith

/-- **Per-row bottom-frame slope `Ghat_bot`.**
At frame row `a` with undisplaced positions `b0 : ι → ℕ`, `ghatBot` combines:
1. the one-body slope `e (b0 a + 1)`,
2. the gain from rows strictly below `a` (`b0 j < b0 a`), where the gap `b0 a - b0 j` widens, and
3. the loss from rows strictly above `a` (`b0 a < b0 j`), where the gap `b0 j - b0 a` narrows.

It is a signed difference, not a sum (`qou-zx9y`). -/
def ghatBot {ι : Type*} [Fintype ι] (e δ : ℕ → ℝ) (b0 : ι → ℕ) (a : ι) : ℝ :=
  e (b0 a + 1)
    + (∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a), δ (b0 a - b0 j))
    - (∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j), δ (b0 j - b0 a))

/-- **Finite-sum `Ghat_bot` frame assembly (`qou-zx9y`).**
For any finite frame `b0 : ι → ℕ`, displacing row `a` by `D` (within the gaps `b0 j - b0 a` of rows
above `a`) changes the sum of its one-body potential and its pairwise interactions with the rest of
the frame by at most `(D : ℝ) * ghatBot e δ b0 a`. -/
theorem ghatBot_frame_bound {ι : Type*} [Fintype ι]
    {fi : ℕ → ℝ}
    (hfi : ∀ m, fi (m + 1) - fi m = e (m + 1))
    (he : Antitone e)
    (hstep : ∀ m, e m - e (m + 1) = δ m)
    (hδ : Antitone δ)
    (b0 : ι → ℕ) (a : ι) (D : ℕ)
    (hD : ∀ j, b0 a < b0 j → D ≤ b0 j - b0 a) :
    (fi (b0 a + D) - fi (b0 a))
      + (∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a),
          (e (b0 a - b0 j) - e (b0 a - b0 j + D)))
      + (∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j),
          (e (b0 j - b0 a) - e (b0 j - b0 a - D)))
      ≤ (D : ℝ) * ghatBot e δ b0 a := by
  have hob : fi (b0 a + D) - fi (b0 a) ≤ (D : ℝ) * e (b0 a + 1) :=
    one_body_sub_le_mul_of_antitone hfi he (b0 a) D
  have hbelow :
      (∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a),
        (e (b0 a - b0 j) - e (b0 a - b0 j + D)))
        ≤ (D : ℝ) * ∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a), δ (b0 a - b0 j) := by
    rw [Finset.mul_sum]
    refine Finset.sum_le_sum fun j _ => ?_
    exact sub_le_mul_of_antitone_step hstep hδ (b0 a - b0 j) D
  have habove :
      (∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j),
        (e (b0 j - b0 a) - e (b0 j - b0 a - D)))
        ≤ -((D : ℝ) * ∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j), δ (b0 j - b0 a)) := by
    rw [Finset.mul_sum, ← Finset.sum_neg_distrib]
    refine Finset.sum_le_sum fun j hj => ?_
    have hlt : b0 a < b0 j := (Finset.mem_filter.mp hj).2
    exact sub_le_neg_mul_of_antitone_step hstep hδ (b0 j - b0 a) D (hD j hlt)
  unfold ghatBot
  linarith

/-- **Multi-row `Ghat_bot` frame bound.**
Summing `ghatBot_frame_bound` across a displacement profile `u : ι → ℕ` bounds the total
frame-linearised excess by `∑ a, (u a : ℝ) * ghatBot e δ b0 a`. -/
theorem sum_ghatBot_frame_bound {ι : Type*} [Fintype ι]
    {fi : ℕ → ℝ}
    (hfi : ∀ m, fi (m + 1) - fi m = e (m + 1))
    (he : Antitone e)
    (hstep : ∀ m, e m - e (m + 1) = δ m)
    (hδ : Antitone δ)
    (b0 u : ι → ℕ)
    (hu : ∀ a j, b0 a < b0 j → u a ≤ b0 j - b0 a) :
    (∑ a : ι,
      ((fi (b0 a + u a) - fi (b0 a))
        + (∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a),
            (e (b0 a - b0 j) - e (b0 a - b0 j + u a)))
        + (∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j),
            (e (b0 j - b0 a) - e (b0 j - b0 a - u a)))))
      ≤ ∑ a : ι, (u a : ℝ) * ghatBot e δ b0 a := by
  refine Finset.sum_le_sum fun a _ => ?_
  exact ghatBot_frame_bound hfi he hstep hδ b0 a (u a) (hu a)

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

/-- Positive margin between the incumbent threshold `V` and the joined evaluation past `L`. -/
theorem sub_join_pos_of_lt_sum {f g h : ℕ → ℝ} {B V : ℝ} {L : ℕ}
    (hf : ∀ a, f a ≤ B) (hg : ∀ b, g b ≤ B)
    (hh : ∀ l, L < l → h l < V - 2 * B)
    {a b : ℕ} (hab : L < a + b) :
    0 < V - (f a + h (a + b) + g b) :=
  sub_pos.mpr (join_lt_of_lt_sum hf hg hh hab)

end QOU.BraidKnot.SearchCoercivity
