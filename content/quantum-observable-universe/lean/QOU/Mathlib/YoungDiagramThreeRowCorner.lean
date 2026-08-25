import QOU.Mathlib.YoungDiagramCorner
import Mathlib.Tactic.IntervalCases
import QOU.QBeta.TemperleyLiebTower

/-!
# A removable corner that preserves "at least three rows"

**Bean `qou-7gei`.** Discharges the combinatorial hypothesis `hpred` of
`QOU.QBeta.TemperleyLiebTower.vanishing_step`, which until now was stated as a
hypothesis and justified only by exhaustion at `n + 1 = 4, 5, 6, 7`.

## The statement, and why it is the right one

`vanishing_step` needs: *every shape at level `n+1` with `≥ 3` rows covers some
shape at level `n` with `≥ 3` rows.* Dually — and this is the form that is
actually convenient — every Young diagram with `≥ 3` rows and at least 4 cells
has a **removable corner whose removal still leaves `≥ 3` rows**.

Two encoding facts make it tractable:

* **"at least three rows" is `(2,0) ∈ μ`.** The row count is `μ.colLen 0`, and
  `mem_iff_lt_colLen` turns `3 ≤ μ.colLen 0` into `2 < μ.colLen 0` into
  `(2,0) ∈ μ`. So the goal `3 ≤ (eraseCorner μ c hc).colLen 0` unfolds, via
  `mem_eraseCorner`, to `(2,0) ∈ μ ∧ (2,0) ≠ c` — and the first conjunct is the
  hypothesis. **The whole theorem is therefore "there is a corner other than
  `(2,0)`."**
* **The last cell of the last row is always a corner** (`isCorner_lastRow`), in
  closed form, with no search: `(μ.colLen 0 − 1, μ.rowLen (μ.colLen 0 − 1) − 1)`.

So the proof is: take that corner; if it is not `(2,0)` we are done; if it *is*,
then `μ` has exactly three rows with a single cell in the third, and a corner in
row 0 or row 1 serves instead.

## Where the cardinality hypothesis is used

**Exactly once**, and it is the content rather than an edge case. With three
rows, a one-cell third row, and `rowLen 0 = 1`, the diagram is forced to be
`(1,1,1)` — three cells. That single shape is the only obstruction, and it is
precisely why `n = 3` is the *base case* of the induction in
`vanishing_all_levels` rather than a step: `(1³)` covers only `(1²)`, which has
two rows. Do not "simplify" the `4 ≤ card` hypothesis away; it is carrying that
fact.

Machinery is the repo's own (`QOU.Mathlib.YoungDiagramCorner`): Mathlib supplies
`YoungDiagram`, `rowLen`, `colLen` and their monotonicity, but has no corner API.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-- **"At least three rows" is membership of `(2,0)`.** The row count of a Young
diagram is the length of column `0`. -/
theorem threeRows_iff (μ : YoungDiagram) : 3 ≤ μ.colLen 0 ↔ (2, 0) ∈ μ := by
  rw [mem_iff_lt_colLen]
  omega

/-- **The last cell of a row is a removable corner exactly when the next row is
strictly shorter.** -/
theorem isCorner_rowEnd (μ : YoungDiagram) (i : ℕ) (hpos : 0 < μ.rowLen i)
    (hdrop : μ.rowLen (i + 1) < μ.rowLen i) :
    IsCornerCell μ (i, μ.rowLen i - 1) := by
  refine ⟨?_, ?_, ?_⟩ <;> simp only [mem_iff_lt_rowLen] <;> omega

/-- Row `i` is nonempty exactly when the diagram has more than `i` rows. -/
theorem rowLen_pos_of_lt_colLen (μ : YoungDiagram) {i : ℕ} (h : i < μ.colLen 0) :
    0 < μ.rowLen i := by
  have : (i, 0) ∈ μ := mem_iff_lt_colLen.mpr h
  exact mem_iff_lt_rowLen.mp this

/-- Row `i` is empty once the rows run out. -/
theorem rowLen_eq_zero_of_colLen_le (μ : YoungDiagram) {i : ℕ} (h : μ.colLen 0 ≤ i) :
    μ.rowLen i = 0 := by
  by_contra hne
  have hpos : 0 < μ.rowLen i := Nat.pos_of_ne_zero hne
  have : (i, 0) ∈ μ := mem_iff_lt_rowLen.mpr hpos
  have := mem_iff_lt_colLen.mp this
  omega

/-- **The last cell of the last row is always a removable corner** of a nonempty
diagram — in closed form, needing no search. -/
theorem isCorner_lastRow (μ : YoungDiagram) (hne : 0 < μ.colLen 0) :
    IsCornerCell μ (μ.colLen 0 - 1, μ.rowLen (μ.colLen 0 - 1) - 1) := by
  have hpos : 0 < μ.rowLen (μ.colLen 0 - 1) :=
    rowLen_pos_of_lt_colLen μ (by omega)
  have hnext : μ.rowLen (μ.colLen 0 - 1 + 1) = 0 :=
    rowLen_eq_zero_of_colLen_le μ (by omega)
  exact isCorner_rowEnd μ _ hpos (by omega)

/-- **A diagram with three rows whose first row is a single cell is `(1,1,1)`**,
hence has three cells. This is the sole obstruction the cardinality hypothesis
rules out. -/
theorem card_le_three_of_rowLen_zero_le_one (μ : YoungDiagram)
    (hrows : μ.colLen 0 = 3) (h0 : μ.rowLen 0 ≤ 1) : μ.cells.card ≤ 3 := by
  have hsub : μ.cells ⊆ ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)) := by
    rintro ⟨a, b⟩ hx
    have hxm : (a, b) ∈ μ := hx
    have hb : b < μ.rowLen a := mem_iff_lt_rowLen.mp hxm
    have hle : μ.rowLen a ≤ μ.rowLen 0 := μ.rowLen_anti 0 a (Nat.zero_le _)
    have hb0 : b = 0 := by omega
    subst hb0
    have ha : a < μ.colLen 0 := mem_iff_lt_colLen.mp hxm
    rw [hrows] at ha
    interval_cases a <;> decide
  have hc3 : ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)).card = 3 := by decide
  have := Finset.card_le_card hsub
  omega

/-- **THE THEOREM. A diagram with at least three rows and at least four cells has
a removable corner whose removal still leaves at least three rows.**

This is `hpred` of `QOU.QBeta.TemperleyLiebTower.vanishing_step`, no longer a
hypothesis. Three cases, each exhibiting an explicit corner:

1. the last-row corner is not `(2,0)` — use it;
2. it *is* `(2,0)`, and row 1 is shorter than row 0 — use the row-0 corner;
3. it is `(2,0)` and rows 0 and 1 are equal — then they have length `≥ 2` (else
   `μ = (1,1,1)`, ruled out by the cardinality hypothesis) and the row-1 corner
   serves. -/
theorem exists_threeRow_corner (μ : YoungDiagram)
    (hrows : 3 ≤ μ.colLen 0) (hcard : 4 ≤ μ.cells.card) :
    ∃ c, ∃ hc : IsCornerCell μ c, 3 ≤ (eraseCorner μ c hc).colLen 0 := by
  have h20 : (2, 0) ∈ μ := (threeRows_iff μ).mp hrows
  -- the goal reduces to "there is a corner other than `(2,0)`"
  have key : ∀ (c : ℕ × ℕ) (hc : IsCornerCell μ c), c ≠ (2, 0) →
      3 ≤ (eraseCorner μ c hc).colLen 0 := by
    intro c hc hne
    rw [threeRows_iff, mem_eraseCorner]
    exact ⟨h20, fun h => hne h.symm⟩
  -- the last-row corner, always available
  have hne0 : 0 < μ.colLen 0 := by omega
  set i := μ.colLen 0 - 1 with hi
  have hlast : IsCornerCell μ (i, μ.rowLen i - 1) := isCorner_lastRow μ hne0
  by_cases hcase : (i, μ.rowLen i - 1) = ((2, 0) : ℕ × ℕ)
  · -- the last-row corner IS `(2,0)`: exactly three rows, third row a single cell
    have hi2 : i = 2 := congrArg Prod.fst hcase
    have hrow2 : μ.rowLen 2 = 1 := by
      have h := congrArg Prod.snd hcase
      simp only [hi2] at h
      have hp : 0 < μ.rowLen 2 := rowLen_pos_of_lt_colLen μ (by omega)
      omega
    have hrows3 : μ.colLen 0 = 3 := by omega
    -- row 0 must have at least two cells, else `μ = (1,1,1)` has three
    have h0 : 2 ≤ μ.rowLen 0 := by
      by_contra hlt
      have := card_le_three_of_rowLen_zero_le_one μ hrows3 (by omega)
      omega
    have h1pos : 0 < μ.rowLen 1 := rowLen_pos_of_lt_colLen μ (by omega)
    have h10 : μ.rowLen 1 ≤ μ.rowLen 0 := μ.rowLen_anti 0 1 (by omega)
    have h21 : μ.rowLen 2 ≤ μ.rowLen 1 := μ.rowLen_anti 1 2 (by omega)
    -- omega treats `rowLen (1+1)` and `rowLen 2` as distinct atoms; link them
    have hidx1 : μ.rowLen (0 + 1) = μ.rowLen 1 := by norm_num
    have hidx2 : μ.rowLen (1 + 1) = μ.rowLen 2 := by norm_num
    by_cases hstrict : μ.rowLen 1 < μ.rowLen 0
    · -- case 2: the row-0 corner
      refine ⟨(0, μ.rowLen 0 - 1), isCorner_rowEnd μ 0 (by omega) (by omega), ?_⟩
      exact key _ _ (by simp)
    · -- case 3: rows 0 and 1 agree, so both have length ≥ 2; the row-1 corner
      have heq : μ.rowLen 1 = μ.rowLen 0 := by omega
      refine ⟨(1, μ.rowLen 1 - 1), isCorner_rowEnd μ 1 (by omega) (by omega), ?_⟩
      exact key _ _ (by simp)
  · -- case 1: the last-row corner already differs from `(2,0)`
    exact ⟨_, hlast, key _ hlast hcase⟩

/-! ## Instantiating the propagation — bean `qou-7gei` item 2

`QOU.QBeta.TemperleyLiebTower.vanishing_all_levels_dom` is stated on abstract
`Shape`, `Cov` and `rows`, with the combinatorial predecessor fact as a
hypothesis. Here that hypothesis is discharged on real Young diagrams, so the
propagation is no longer conditional on it.

Shapes are `{μ : YoungDiagram // μ.cells.card = n}` — written inline rather than
behind a `def`, so subtype projections stay definitionally transparent and no
unfolding lemmas are needed. `Cov` is the *converse* of corner removal: `l`
covers `m` when deleting some removable corner of `l` gives `m`. `rows` is
`colLen 0`.

Note what this deliberately avoids. Phrasing covers as a `Finset (Shape (n+1))`
would need `Fintype {μ : YoungDiagram // μ.cells.card = n}`, which Mathlib does
not provide and which is real work to build. The domination form of the
induction never sums, so `Cov` can be a bare `Prop` and the finiteness question
never arises. -/

/-- **The predecessor fact, on Young diagrams of a given size.**

Every shape of size `n+1` with at least three rows covers a shape of size `n`
with at least three rows, provided `3 ≤ n`. This is `hpred` of
`vanishing_all_levels_dom`, discharged.

The `3 ≤ n` guard is exactly the `4 ≤ card` of `exists_threeRow_corner`, and it
is load-bearing: at `n = 2` the shape `(1³)` of size 3 covers only `(1²)`, which
has two rows. That is the base case of the induction, not a step. -/
theorem youngPred (n : ℕ) (hn : 3 ≤ n)
    (l : {μ : YoungDiagram // μ.cells.card = n + 1}) (hl : 3 ≤ l.val.colLen 0) :
    ∃ m : {μ : YoungDiagram // μ.cells.card = n}, 3 ≤ m.val.colLen 0 ∧
      ∃ c, ∃ hc : IsCornerCell l.val c, eraseCorner l.val c hc = m.val := by
  have hcard : 4 ≤ l.val.cells.card := by rw [l.property]; omega
  obtain ⟨c, hc, hrows⟩ := exists_threeRow_corner l.val hl hcard
  have hcard' : (eraseCorner l.val c hc).cells.card = n := by
    have h := card_eraseCorner l.val c hc
    rw [l.property] at h
    omega
  exact ⟨⟨eraseCorner l.val c hc, hcard'⟩, hrows, ⟨c, hc, rfl⟩⟩

/-- **At three cells there is exactly one shape with three rows, namely `(1³)`.**

Three rows forces `(0,0), (1,0), (2,0) ∈ μ` — that is already three cells — and
`card = 3` leaves no room for a fourth. So the base case of the induction is a
statement about a *single* diagram, which is what lets the scalar pinning
`TemperleyLiebTower.conventionD_kills_antisymmetriser` discharge it: there is
nothing to quantify over.

This is the glue between the scalar layer (which knows `y₍₁³₎ = 0`) and the
diagram layer (which needs `∀ m of size 3 with ≥ 3 rows, y m = 0`). -/
theorem card_three_threeRow_unique (μ : YoungDiagram)
    (hcard : μ.cells.card = 3) (hrows : 3 ≤ μ.colLen 0) :
    μ.cells = ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)) := by
  have h20 : (2, 0) ∈ μ := (threeRows_iff μ).mp hrows
  have h10 : (1, 0) ∈ μ := μ.up_left_mem (by omega) (by omega) h20
  have h00 : (0, 0) ∈ μ := μ.up_left_mem (by omega) (by omega) h20
  have hsub : ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)) ⊆ μ.cells := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with h | h | h <;> subst h <;> assumption
  have hc3 : ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)).card = 3 := by decide
  exact (Finset.eq_of_subset_of_card_le hsub (by omega)).symm

/-- **Hence the base case needs only one scalar fact.** Any two size-3 shapes
with three rows are equal, so `∀ m, 3 ≤ rows m → y m = 0` collapses to the
single instance the pinning already provides. -/
theorem threeRow_size_three_subsingleton
    (m m' : {μ : YoungDiagram // μ.cells.card = 3})
    (h : 3 ≤ m.val.colLen 0) (h' : 3 ≤ m'.val.colLen 0) : m = m' := by
  have e : m.val.cells = m'.val.cells := by
    rw [card_three_threeRow_unique m.val m.property h,
      card_three_threeRow_unique m'.val m'.property h']
  exact Subtype.ext (YoungDiagram.ext e)

/-- **The propagation, with every combinatorial hypothesis discharged.**

If the weights are nonnegative, each cover is dominated by its parent, and all
`≥ 3`-row weights vanish at three strands, then they vanish at every level
above. Nothing here is assumed about Young diagrams — `youngPred` supplies it.

The two remaining hypotheses are the *analytic* ones and both are proved
elsewhere on this branch for the actual Markov weights: `hnn` from
`TemperleyLiebTower.yw_nonneg`, and `hdom` from
`TemperleyLiebTower.dominates_of_branching` applied to `yw_branching`. The base
case is `conventionD_kills_antisymmetriser`.

So the `≥ 3`-row vanishing at all `n ≥ 3` now rests on the `n = 3` pinning plus
proved facts, with no appeal to Wenzl's theorem. -/
theorem threeRow_vanishing_all_levels {R : Type*} [AddCommMonoid R] [PartialOrder R]
    [CovariantClass R R (· + ·) (· ≤ ·)]
    (y : ∀ n, {μ : YoungDiagram // μ.cells.card = n} → R)
    (hnn : ∀ n (l : {μ : YoungDiagram // μ.cells.card = n + 1}), 0 ≤ y (n + 1) l)
    (hdom : ∀ n (m : {μ : YoungDiagram // μ.cells.card = n})
      (l : {μ : YoungDiagram // μ.cells.card = n + 1}),
      (∃ c, ∃ hc : IsCornerCell l.val c, eraseCorner l.val c hc = m.val) →
        y (n + 1) l ≤ y n m)
    (base : ∀ m : {μ : YoungDiagram // μ.cells.card = 3}, 3 ≤ m.val.colLen 0 → y 3 m = 0) :
    ∀ k : ℕ, ∀ l : {μ : YoungDiagram // μ.cells.card = 3 + k},
      3 ≤ l.val.colLen 0 → y (3 + k) l = 0 :=
  QOU.QBeta.TemperleyLiebTower.vanishing_all_levels_dom
    y (fun _ m l => ∃ c, ∃ hc : IsCornerCell l.val c, eraseCorner l.val c hc = m.val)
    (fun _ m => m.val.colLen 0) 3 hnn hdom
    (fun n hn l hl => youngPred n hn l hl) base

/-- **The composed statement: one scalar in, vanishing at every level out.**

`threeRow_vanishing_all_levels` still asks for a base case quantified over
shapes. `threeRow_size_three_subsingleton` collapses that quantifier, so the
input becomes a **single scalar fact** — the weight of the one three-row shape
of size 3 is zero — which is exactly what
`TemperleyLiebTower.conventionD_kills_antisymmetriser` delivers.

That is as far as this layer can honestly go, and the boundary is worth naming.
Going further means saying that the framework's `y_λ` *is* the Wedderburn weight
of the Markov trace, i.e. `tr_M = Σ_λ y_λ χ_λ`. That is a statement about
characters and the Wedderburn decomposition — the representation theory this
module deliberately does not carry, and which the Hecke-instance layer
(`QOU.Hecke`, PR #4857) is building. Until it lands, `y` here is any function
satisfying the hypotheses, and the theorem is a genuine implication rather than
a tautology: nothing below *defines* `y` to be zero anywhere.

The one place a reader could be misled is `hpin`. It is an input, not a
conclusion. What is proved is that a single zero at `n = 3` propagates to every
level — not that the zero is there. -/
theorem threeRow_vanishing_of_pinning {R : Type*} [AddCommMonoid R] [PartialOrder R]
    [CovariantClass R R (· + ·) (· ≤ ·)]
    (y : ∀ n, {μ : YoungDiagram // μ.cells.card = n} → R)
    (hnn : ∀ n (l : {μ : YoungDiagram // μ.cells.card = n + 1}), 0 ≤ y (n + 1) l)
    (hdom : ∀ n (m : {μ : YoungDiagram // μ.cells.card = n})
      (l : {μ : YoungDiagram // μ.cells.card = n + 1}),
      (∃ c, ∃ hc : IsCornerCell l.val c, eraseCorner l.val c hc = m.val) →
        y (n + 1) l ≤ y n m)
    (m₀ : {μ : YoungDiagram // μ.cells.card = 3}) (hm₀ : 3 ≤ m₀.val.colLen 0)
    (hpin : y 3 m₀ = 0) :
    ∀ k : ℕ, ∀ l : {μ : YoungDiagram // μ.cells.card = 3 + k},
      3 ≤ l.val.colLen 0 → y (3 + k) l = 0 := by
  refine threeRow_vanishing_all_levels y hnn hdom ?_
  intro m hm
  rw [threeRow_size_three_subsingleton m m₀ hm hm₀]
  exact hpin

end QOU.Mathlib
