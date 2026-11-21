import QOU.BraidKnot.HookSumBetaCoordinates

/-!
# The staircase's hook lengths, in closed form

The staircase `δ_k = (k, k−1, …, 1)` is the minimiser of the hook sum at `n = T_k`, and the
`REV_n` arc (bean `qou-hok7`) measures every other shape against it.  Its value there is a
two-constant series, and that series rests on exactly one combinatorial fact:

    the hook length `2j − 1` occurs `k + 1 − j` times, and no even hook length occurs.

Until now that fact was **enumerated** — verified for `k = 1..40` by
`rev_staircase_closed_form_and_constant_term_probe.py`.  This file proves it for every `k`, and
the proof is short because the right presentation of the staircase makes it a one-liner: its
cells are `{(i, j) : i + j < k}`, which is visibly symmetric in `i` and `j`, so

    rowLen i = k − i,    colLen j = k − j,    hook (i, j) = 2(k − i − j) − 1 .

The hook depends on the **antidiagonal index** `s = i + j` alone, and the antidiagonal `s` has
`s + 1` cells.  That is the multiset statement, and `staircase_hookSum` is the telescoped sum
identity the arc actually consumes.

| | |
|---|---|
| `mem_staircaseYD` | `(i, j) ∈ δ_k ↔ i + j < k` |
| `staircaseYD_rowLen` / `staircaseYD_colLen` | `k − i` / `k − j` |
| `staircase_hook` | `hook (i, j) = 2(k − i − j) − 1` on a cell |
| `staircase_hookSum` | `Σ_{c} g(h(c)) = Σ_{s<k} (s+1) • g(2(k−s)−1)` for any `g` into an `AddCommMonoid` |

## Relation to what the corpus already had

`QOU.StaircaseCornerHook.staircase_corner_hook_eq_two_k_sub_one` proves the **corner** hook is
`2k − 1`.  That is the `s = 0` case of `staircase_hook` and nothing more; the rest of that file
is the EW-residual conjecture, a different subject.  `QOU.Hecke.staircasePartition` is a
`Nat.Partition`, so the arc's `YoungDiagram`-indexed hook machinery cannot reach it — hence the
diagram here rather than a bridge.

## Why the `{(i,j) : i+j < k}` presentation and not `ofRowLens`

`YoungDiagram.ofRowLens` would need the row-length list, its sortedness, and then a separate
argument for `colLen` (the transpose).  The sublevel-set presentation gets `colLen` for free:
`i + j < k` is symmetric, so the diagram is its own transpose by inspection, and the two
`mem_iff_lt_*` characterisations then give both lengths by the same `omega`.

## Base ring (§7c)

No ring at all: hooks are `ℕ`, and the sum identity is stated for an arbitrary `AddCommMonoid`
target exactly as `(I')` is in `HookSumBetaCoordinates`.  The `ε`-valued specialisation the arc
uses lives downstream, past the archimedean wall.

-- Ref: [leitner2026] computations/deltalambda/rev_staircase_closed_form_and_constant_term_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset

/-- The staircase `δ_k = (k, k−1, …, 1)` as a Young diagram, presented as the sublevel set
`{(i, j) : i + j < k}`.  Visibly symmetric in `i` and `j`, which is what makes `colLen` free. -/
def staircaseYD (k : ℕ) : YoungDiagram where
  cells := (range k ×ˢ range k).filter (fun c => c.1 + c.2 < k)
  isLowerSet := by
    -- `isLowerSet` is stated on the COERCED set, so `Finset.mem_coe` has to come first —
    -- `mem_filter` alone makes no progress against `_ ∈ ↑(Finset.filter ..)`.
    rintro ⟨a, b⟩ ⟨a', b'⟩ hle hmem
    have h₁ : a' ≤ a := hle.1
    have h₂ : b' ≤ b := hle.2
    simp only [Finset.mem_coe, mem_filter, Finset.mem_product, mem_range] at hmem ⊢
    exact ⟨⟨by omega, by omega⟩, by omega⟩

@[simp] theorem mem_staircaseYD (k i j : ℕ) : (i, j) ∈ staircaseYD k ↔ i + j < k := by
  change (i, j) ∈ (staircaseYD k).cells ↔ _
  simp only [staircaseYD, mem_filter, Finset.mem_product, mem_range]
  omega

/-- `rowLen i = k − i`.  Read off `mem_iff_lt_rowLen`: `j` is in row `i` iff `j < k − i`. -/
theorem staircaseYD_rowLen (k i : ℕ) : (staircaseYD k).rowLen i = k - i := by
  have h : ∀ j, j < (staircaseYD k).rowLen i ↔ j < k - i := by
    intro j
    rw [← YoungDiagram.mem_iff_lt_rowLen, mem_staircaseYD]
    omega
  have h₁ := h ((staircaseYD k).rowLen i)
  have h₂ := h (k - i)
  omega

/-- `colLen j = k − j`, by the same argument — the presentation is symmetric. -/
theorem staircaseYD_colLen (k j : ℕ) : (staircaseYD k).colLen j = k - j := by
  have h : ∀ i, i < (staircaseYD k).colLen j ↔ i < k - j := by
    intro i
    rw [← YoungDiagram.mem_iff_lt_colLen, mem_staircaseYD]
    omega
  have h₁ := h ((staircaseYD k).colLen j)
  have h₂ := h (k - j)
  omega

/-- **The staircase's hook length, in closed form.**  On a cell, `h(i, j) = 2(k − i − j) − 1`.

It depends only on the antidiagonal index `s = i + j`, which is the whole content: the hook is
constant along antidiagonals, and antidiagonal `s` carries `s + 1` cells. -/
theorem staircase_hook (k i j : ℕ) (h : i + j < k) :
    QOU.QBeta.WenzlWeight.hook (staircaseYD k) (i, j) = 2 * (k - i - j) - 1 := by
  simp only [QOU.QBeta.WenzlWeight.hook, staircaseYD_rowLen, staircaseYD_colLen]
  omega

/-- Every hook length of the staircase is **odd**, and no even value occurs — immediate from
`staircase_hook`, and the half of the multiset claim that is easiest to misstate. -/
theorem staircase_hook_odd (k i j : ℕ) (h : i + j < k) :
    Odd (QOU.QBeta.WenzlWeight.hook (staircaseYD k) (i, j)) := by
  rw [staircase_hook k i j h]
  exact ⟨k - i - j - 1, by omega⟩

/-- The antidiagonal `s` of the staircase: the cells with `i + j = s`. -/
theorem staircaseYD_filter_antidiag (k s : ℕ) (hs : s < k) :
    (staircaseYD k).cells.filter (fun c => c.1 + c.2 = s)
      = (range (s + 1)).image (fun i => (i, s - i)) := by
  ext ⟨a, b⟩
  simp only [mem_filter, mem_image, mem_range, YoungDiagram.mem_cells, mem_staircaseYD,
    Prod.mk.injEq]
  constructor
  · rintro ⟨-, hab⟩
    exact ⟨a, by omega, rfl, by omega⟩
  · rintro ⟨i, hi, rfl, rfl⟩
    omega

/-- Antidiagonal `s` carries exactly `s + 1` cells. -/
theorem staircaseYD_antidiag_card (k s : ℕ) (hs : s < k) :
    ((staircaseYD k).cells.filter (fun c => c.1 + c.2 = s)).card = s + 1 := by
  rw [staircaseYD_filter_antidiag k s hs, card_image_of_injective _ (fun a b hab => by
    simpa using congrArg Prod.fst hab), card_range]

/-- **The telescoped hook sum of the staircase.**  For any `g` into an additive commutative
monoid,

    Σ_{c ∈ δ_k} g(h(c))  =  Σ_{s<k} (s+1) • g(2(k−s) − 1) .

This is the identity the `REV_n` arc consumes.  Reindexing `s = k − j` turns the right-hand
side into `Σ_{j=1}^{k} (k+1−j) g(2j−1)`, which at `g = ε` is the staircase's β-side — and with
`betaSide_eq_hookSum` that is the whole of `V(δ_k)` bar the `L`-free constant.

The proof is the antidiagonal fibration: the hook is constant on each antidiagonal
(`staircase_hook`) and antidiagonal `s` has `s+1` cells (`staircaseYD_antidiag_card`). -/
theorem staircase_hookSum {N : Type*} [AddCommMonoid N] (g : ℕ → N) (k : ℕ) :
    ∑ c ∈ (staircaseYD k).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD k) c)
      = ∑ s ∈ range k, (s + 1) • g (2 * (k - s) - 1) := by
  have hmaps : ∀ c ∈ (staircaseYD k).cells, c.1 + c.2 ∈ range k := by
    intro c hc
    rw [YoungDiagram.mem_cells] at hc
    rw [mem_range]
    exact (mem_staircaseYD k c.1 c.2).mp (by simpa using hc)
  rw [← Finset.sum_fiberwise_of_maps_to hmaps]
  refine Finset.sum_congr rfl fun s hs => ?_
  rw [mem_range] at hs
  have hconst : ∀ c ∈ (staircaseYD k).cells.filter (fun c => c.1 + c.2 = s),
      g (QOU.QBeta.WenzlWeight.hook (staircaseYD k) c) = g (2 * (k - s) - 1) := by
    intro c hc
    rw [mem_filter, YoungDiagram.mem_cells] at hc
    obtain ⟨hcell, hsum⟩ := hc
    have hlt : c.1 + c.2 < k := (mem_staircaseYD k c.1 c.2).mp (by simpa using hcell)
    have hh := staircase_hook k c.1 c.2 hlt
    rw [Prod.mk.eta] at hh
    rw [hh]
    congr 1
    omega
  rw [Finset.sum_congr rfl hconst, Finset.sum_const, staircaseYD_antidiag_card k s hs]

end QOU.BraidKnot.HookSum
