import QOU.SchurWeyl.WenzlNormalisation
import QOU.SchurWeyl.SeminormalNodeForm

/-!
# QOU.SchurWeyl.WenzlMarkovCorner — the corner identity at general level `r`

`MarkovAssembly.markov_of_corner_identity` reduces the Markov condition to a **per-corner**
identity on the weights,

`∑_{s addable} w_{ν + s} · a(axialDistance c s) = z · w_ν`   for every removable corner `c` of `ν`,

and `OcneanuWeightMarkovCorner` proves that identity at `r = 2` one row at a time.  This file proves
it at **every** level `r`, for `wenzlWeight r Q` with `Q = q²`, with

`z_r = Q^r / (q · [r]_Q)`.

At `r = 2` that is `q⁴/(q(1+q²)) = q³/(q²+1) = z_D`, the convention-D parameter — so the general
statement specialises back to the merged chain's, and `wenzlMarkovParam_conventionD` is the
`q`-shifted form of the same number (`z_W = q·z_D`, `z_r = z_W/q`).

| | |
|---|---|
| `pow_ne_pow_of_ne` | distinct exponents, distinct powers, at a non-root-of-unity `Q` |
| `levelBracket_ne_zero` | `[r]_Q ≠ 0` for `r ≠ 0` |
| `betaR_succ_ne_of_corner` | **no β is one above a corner's β** — the mirror of `betaR_ne_succ_of_addable` |
| `sum_wenzlWeight_node_weighted` | the algebraic core, over any field |
| `wenzlWeight_markov_corner` | **the corner identity**, over `ℝ` at `Q = q²` |

**Why two theorems.**  The arithmetic is field-generic and has nothing to do with `ℝ`; only the
translation of `seminormalParam` into the node weight `Q·x_a/(Q·x_a − x_b)` is `ℝ`-bound, because
`seminormalParam` is.  `sum_wenzlWeight_node_weighted` carries the former,
`wenzlWeight_markov_corner` the latter.

**What the corner hypothesis buys.**  `sum_prod_qratio_weighted` needs `Q·x_i ≠ x_b` for every
`i ≠ b`, i.e. `β_i + 1 ≠ β_b` — otherwise a summand is `0/0`.  Strict decrease of `β` does not give
this: it permits `β_{b−1} = β_b + 1`.  What rules it out is that `c` is a *removable corner*, so
`ν_{b+1} < ν_b`, which pushes `β_{b+1}` a full two below `β_b`.  That is `betaR_succ_ne_of_corner`,
and it is the exact mirror of what addability buys in `betaR_ne_succ_of_addable`.

## Scope

`r` is the **Wenzl level** — the number of variables in the principal specialisation — and is an
integer by construction; `Q^r = z/(1−Q+z)` pins the lattice.  General integer `r` is **on** that
lattice.  Nothing here bears on arbitrary `z`, which is off it.

## Base ring (§7c)

`sum_wenzlWeight_node_weighted` is generic `[Field F]`.  `wenzlWeight_markov_corner` is `ℝ`, forced
by `seminormalParam`; nothing archimedean is used.

LaTeX label: `thm:wenzl-markov-corner`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib

section Algebra

variable {F : Type*} [Field F]

/-- **Distinct exponents give distinct powers** at a non-root-of-unity `Q`. -/
theorem pow_ne_pow_of_ne {Q : F} (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    {m n : ℕ} (hmn : m ≠ n) : Q ^ m ≠ Q ^ n := by
  have key : ∀ a b : ℕ, a < b → (Q : F) ^ a ≠ Q ^ b := by
    intro a b hab hEq
    have hsplit : (Q : F) ^ b = Q ^ a * Q ^ (b - a) := by
      rw [← pow_add]; congr 1; omega
    rw [hsplit] at hEq
    have hone : (Q : F) ^ (b - a) = 1 :=
      mul_left_cancel₀ (pow_ne_zero a hQ0) (by rw [mul_one]; exact hEq.symm)
    exact one_sub_pow_ne_zero hgen (n := b - a) (by omega) (by rw [hone, sub_self])
  rcases Nat.lt_or_ge m n with h | h
  · exact key m n h
  · exact fun hEq => key n m (by omega) hEq.symm

/-- `[r]_Q ≠ 0` for `r ≠ 0`: it divides `1 − Q^r`, which `hgen` keeps nonzero. -/
theorem levelBracket_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0) :
    levelBracket r Q ≠ 0 := by
  intro h
  refine one_sub_pow_ne_zero hgen hr ?_
  rw [one_sub_pow_eq_mul_levelBracket r Q, h, mul_zero]

end Algebra

/-- **No β sits one above a corner's β.**

If `c` is a removable corner in row `b` then `ν_{b+1} < ν_b`, so `β_{b+1} ≤ β_b − 2`; rows further
down are lower still, and rows above have `β > β_b` outright.  Hence `β_i + 1 = β_b` for no `i ≠ b`.

This is the mirror of `betaR_ne_succ_of_addable`, and it is what discharges the `hne` hypothesis of
`QOU.Mathlib.sum_prod_qratio_weighted` at the corner node. -/
theorem betaR_succ_ne_of_corner {r : ℕ} {ν : YoungDiagram} {c : ℕ × ℕ} {i : ℕ}
    (hc : IsCornerCell ν c) (hcr : c.1 < r) (hi : i < r) (hic : i ≠ c.1) :
    betaR r ν i + 1 ≠ betaR r ν c.1 := by
  rcases lt_or_gt_of_ne hic with hlt | hgt
  · have := betaR_lt (μ := ν) (r := r) hlt hcr
    omega
  · have hc2 : c.2 + 1 = ν.rowLen c.1 := rowLen_of_isCornerCell hc
    have hbelow : ν.rowLen (c.1 + 1) ≤ c.2 := by
      by_contra hcon
      push_neg at hcon
      exact hc.2.1 (mem_iff_lt_rowLen.mpr hcon)
    have hc1r : c.1 + 1 < r := by omega
    have hgap : betaR r ν (c.1 + 1) + 2 ≤ betaR r ν c.1 := by
      unfold betaR
      omega
    have hmono : betaR r ν i ≤ betaR r ν (c.1 + 1) := by
      rcases Nat.lt_or_ge (c.1 + 1) i with h | h
      · exact le_of_lt (betaR_lt (μ := ν) (r := r) h hi)
      · have heq : i = c.1 + 1 := by omega
        rw [heq]
    omega

/-- **The algebraic core of the corner identity.**

Summing the branching ratio against the node weight `Q·x_a/(Q·x_a − x_b)` collapses by
`sum_prod_qratio_weighted` — the Lagrange residue sum — to `Q^r/(Q−1)`, and the branching itself
contributes `w_ν/[r]_Q`.  Non-addable rows drop out on their own: the `q`-ratio numerator already
vanishes there.

`hgap` is the `0/0` guard, supplied at the corner node by `betaR_succ_ne_of_corner`. -/
theorem sum_wenzlWeight_node_weighted {F : Type*} [Field F] (Q : F) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r b : ℕ} {ν : YoungDiagram}
    (hrν : ν.colLen 0 ≤ r) (hb : b < r)
    (hgap : ∀ i, i < r → i ≠ b → betaR r ν i + 1 ≠ betaR r ν b) :
    (∑ a ∈ Finset.range r,
        (if IsAddableCell ν (a, ν.rowLen a) then
          wenzlWeight r Q (addCellOrSelf ν (a, ν.rowLen a))
            * (Q * Q ^ betaR r ν a / (Q * Q ^ betaR r ν a - Q ^ betaR r ν b))
        else 0))
      = Q ^ r / (Q - 1) / levelBracket r Q * wenzlWeight r Q ν := by
  classical
  have hbr : levelBracket r Q ≠ 0 := levelBracket_ne_zero hgen (by omega)
  have hterm : ∀ a ∈ Finset.range r,
      (if IsAddableCell ν (a, ν.rowLen a) then
        wenzlWeight r Q (addCellOrSelf ν (a, ν.rowLen a))
          * (Q * Q ^ betaR r ν a / (Q * Q ^ betaR r ν a - Q ^ betaR r ν b))
      else 0)
        = ((∏ j ∈ (Finset.range r).erase a,
              (Q * Q ^ betaR r ν a - Q ^ betaR r ν j) / (Q ^ betaR r ν a - Q ^ betaR r ν j))
            * (Q * Q ^ betaR r ν a / (Q * Q ^ betaR r ν a - Q ^ betaR r ν b)))
          * (wenzlWeight r Q ν / levelBracket r Q) := by
    intro a ha
    rw [Finset.mem_range] at ha
    by_cases hadd : IsAddableCell ν (a, ν.rowLen a)
    · rw [if_pos hadd, addCellOrSelf_of hadd,
        wenzlWeight_addCell_eq Q hQ0 hgen hadd ha hrν hbr]
      ring
    · rw [if_neg hadd]
      obtain ⟨hpos, heq⟩ := not_isAddableCell_rowEnd ν hadd
      rw [Finset.prod_div_distrib, qratio_prod_eq_zero_of_not_addable Q hpos ha heq,
        zero_div, zero_mul, zero_mul]
  have hne : ∀ i ∈ Finset.range r, i ≠ b →
      Q * (fun i => Q ^ betaR r ν i) i - (fun i => Q ^ betaR r ν i) b ≠ 0 := by
    intro i hi hib
    rw [Finset.mem_range] at hi
    dsimp only
    rw [show Q * Q ^ betaR r ν i = Q ^ (betaR r ν i + 1) from (pow_succ' Q _).symm]
    exact sub_ne_zero.mpr (pow_ne_pow_of_ne hQ0 hgen (hgap i hi hib))
  have hsum := QOU.Mathlib.sum_prod_qratio_weighted
    (s := Finset.range r) (v := fun i => Q ^ betaR r ν i)
    (betaR_pow_injOn hQ0 hgen r ν) (fun i _ => pow_ne_zero _ hQ0) hQ0 hQ1
    (Finset.mem_range.mpr hb) hne
  rw [Finset.card_range] at hsum
  rw [Finset.sum_congr rfl hterm, ← Finset.sum_mul]
  rw [show (∑ a ∈ Finset.range r,
        (∏ j ∈ (Finset.range r).erase a,
            (Q * Q ^ betaR r ν a - Q ^ betaR r ν j) / (Q ^ betaR r ν a - Q ^ betaR r ν j))
          * (Q * Q ^ betaR r ν a / (Q * Q ^ betaR r ν a - Q ^ betaR r ν b)))
      = Q ^ r / (Q - 1) from hsum]
  ring

/-- **Bridge between the corpus's two `axialDistance`s.**

`QOU.SchurWeyl.axialDistance` (`HoefsmitRep`, via `cellContent`) and
`QOU.BraidKnot.TableauContent.axialDistance` (via `content`) are the same function under two names —
both are `(content of the second) − (content of the first)`.  They are `rfl`-equal, but they are
*different constants*, so a bare `axialDistance` inside `namespace QOU.SchurWeyl` resolves to the
first even under `open QOU.BraidKnot.TableauContent`, and a `rw` with a lemma stated in the second
will not fire.  `markov_of_corner_identity` uses the first; `axialDistance_corner_addable` the
second.  This lemma is what lets one consume the other.

(The duplication itself is a notation collision worth draining corpus-wide; that is not this file's
scope.) -/
theorem axialDistance_eq_tableauContent (c d : ℕ × ℕ) :
    axialDistance c d = QOU.BraidKnot.TableauContent.axialDistance c d := rfl

open Seminormal QOU.BraidKnot.TableauContent in
/-- **The corner identity at general level `r`.**

For every removable corner `c` of `ν`,

`∑_{s addable} w_{ν+s} · a(axialDistance c s) = z_r · w_ν`,  `z_r = Q^r/(q·[r]_Q)`, `Q = q²`.

This is the hypothesis `MarkovAssembly.markov_of_corner_identity` consumes, so with it the Markov
condition holds for `wenzlWeight r (q²)` at every integer level — `OcneanuWeightMarkovCorner`'s
row-by-row `r = 2` argument, replaced by one uniform proof.

At `r = 2` the parameter is `q⁴/(q(1+q²)) = q³/(q²+1) = z_D`.

The proof: the subtype sum becomes a guarded row sum (`sum_addable_eq_sum_range`), which is trimmed
to `range r` (rows past `colLen 0` are not addable; rows past `r` give a diagram with too many rows,
which `wenzlWeight_addCell_beyond_eq_zero` kills), and each surviving `seminormalParam` becomes the
node weight by `axialDistance_corner_addable` + `seminormalParam_node_form`.  Then
`sum_wenzlWeight_node_weighted` does the arithmetic.

Note there is **no `a = b` special case**: at `s.1 = c.1` the axial distance is `1` and the node form
gives `(q − q⁻¹)·Q/(Q−1) = q` on its own. -/
theorem wenzlWeight_markov_corner (q : ℝ) (hq : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : ℝ)) ^ k ≠ 1)
    {r : ℕ} (hr : r ≠ 0) (ν : YoungDiagram) {c : ℕ × ℕ} (hc : IsCornerCell ν c) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
        wenzlWeight r (q ^ 2) (addCell ν s.1 s.2) * seminormalParam q (axialDistance c s.1))
      = (q ^ 2) ^ r / (q * levelBracket r (q ^ 2)) * wenzlWeight r (q ^ 2) ν := by
  classical
  have hQ0 : (q ^ 2 : ℝ) ≠ 0 := pow_ne_zero _ hq
  have hQ1 : (q ^ 2 : ℝ) ≠ 1 := by
    have h := hgen 1 one_ne_zero
    rwa [zpow_one] at h
  have hbr : levelBracket r (q ^ 2 : ℝ) ≠ 0 := levelBracket_ne_zero hgen hr
  by_cases hrν : ν.colLen 0 ≤ r
  · have hcr : c.1 < r := lt_of_lt_of_le (isCornerCell_row_lt hc) hrν
    -- Step 1: the subtype sum is a guarded row sum.
    have hG : ∀ s : {s : ℕ × ℕ // IsAddableCell ν s},
        wenzlWeight r (q ^ 2) (addCell ν s.1 s.2) * seminormalParam q (axialDistance c s.1)
          = (fun x : ℕ × ℕ => wenzlWeight r (q ^ 2) (addCellOrSelf ν x)
              * seminormalParam q (axialDistance c x)) s.1 := by
      intro s
      dsimp only
      rw [addCellOrSelf_of s.2]
    rw [Finset.sum_congr rfl fun s _ => hG s,
      sum_addable_eq_sum_range ν (fun x : ℕ × ℕ => wenzlWeight r (q ^ 2) (addCellOrSelf ν x)
        * seminormalParam q (axialDistance c x))]
    -- Step 2: trim the row range to `range r`.
    have hswap : ∀ (M N : ℕ) (T : ℕ → ℝ), M ≤ N → (∀ a, M ≤ a → T a = 0) →
        (∑ a ∈ Finset.range N, T a) = ∑ a ∈ Finset.range M, T a := by
      intro M N T hMN hz
      refine (Finset.sum_subset ?_ ?_).symm
      · intro x hx
        rw [Finset.mem_range] at hx ⊢
        omega
      · intro x _ hnx
        rw [Finset.mem_range] at hnx
        exact hz x (by omega)
    have key : ∀ T : ℕ → ℝ, (∀ a, r ≤ a → T a = 0) → (∀ a, ν.colLen 0 + 1 ≤ a → T a = 0) →
        (∑ a ∈ Finset.range (ν.colLen 0 + 1), T a) = ∑ a ∈ Finset.range r, T a := by
      intro T h1 h2
      have e1 := hswap (ν.colLen 0 + 1) (max (ν.colLen 0 + 1) r) T (le_max_left _ _) h2
      have e2 := hswap r (max (ν.colLen 0 + 1) r) T (le_max_right _ _) h1
      rw [← e1]; exact e2
    rw [key _ ?_ ?_]
    rotate_left
    · intro a hra
      by_cases hadd : IsAddableCell ν (a, ν.rowLen a)
      · rw [if_pos hadd, addCellOrSelf_of hadd,
          wenzlWeight_addCell_beyond_eq_zero hQ0 hgen hbr hra hadd, zero_mul]
      · rw [if_neg hadd]
    · intro a ha
      have hnot : ¬ IsAddableCell ν (a, ν.rowLen a) := by
        rw [isAddableCell_rowEnd_iff]
        push_neg
        refine ⟨by omega, ?_⟩
        have hz : ν.rowLen (a - 1) = 0 := by
          by_contra hne0
          have hmem : ((a - 1, 0) : ℕ × ℕ) ∈ ν := mem_iff_lt_rowLen.mpr (by omega)
          have := mem_iff_lt_colLen.mp hmem
          omega
        omega
      rw [if_neg hnot]
    -- Step 3: `seminormalParam` becomes the node weight.
    have hnode : ∀ a ∈ Finset.range r,
        (if IsAddableCell ν (a, ν.rowLen a) then
          wenzlWeight r (q ^ 2) (addCellOrSelf ν (a, ν.rowLen a))
            * seminormalParam q (axialDistance c (a, ν.rowLen a))
        else 0)
          = (q - q⁻¹) *
            (if IsAddableCell ν (a, ν.rowLen a) then
              wenzlWeight r (q ^ 2) (addCellOrSelf ν (a, ν.rowLen a))
                * (q ^ 2 * (q ^ 2) ^ betaR r ν a
                    / (q ^ 2 * (q ^ 2) ^ betaR r ν a - (q ^ 2) ^ betaR r ν c.1))
            else 0) := by
      intro a ha
      rw [Finset.mem_range] at ha
      by_cases hadd : IsAddableCell ν (a, ν.rowLen a)
      · rw [if_pos hadd, if_pos hadd]
        have hden : q ^ 2 * (q ^ 2) ^ betaR r ν a - (q ^ 2) ^ betaR r ν c.1 ≠ 0 := by
          rw [show q ^ 2 * (q ^ 2) ^ betaR r ν a = (q ^ 2) ^ (betaR r ν a + 1) from
            (pow_succ' (q ^ 2) _).symm]
          by_cases hac : a = c.1
          · rw [hac]
            refine sub_ne_zero.mpr (pow_ne_pow_of_ne hQ0 hgen (by omega))
          · exact sub_ne_zero.mpr
              (pow_ne_pow_of_ne hQ0 hgen (betaR_succ_ne_of_corner hc hcr ha hac))
        rw [axialDistance_eq_tableauContent, axialDistance_corner_addable r ν hadd hc (by exact ha) hcr,
          seminormalParam_node_form q hq ((q ^ 2) ^ betaR r ν a) ((q ^ 2) ^ betaR r ν c.1)
            (pow_ne_zero _ hQ0) _ (zpow_node_dictionary hQ0 _ _) hden]
        ring
      · rw [if_neg hadd, if_neg hadd, mul_zero]
    rw [Finset.sum_congr rfl hnode, ← Finset.mul_sum,
      sum_wenzlWeight_node_weighted (q ^ 2 : ℝ) hQ0 hQ1 hgen hrν hcr
        (fun i hi hic => betaR_succ_ne_of_corner hc hcr hi hic)]
    have hQm1 : (q ^ 2 : ℝ) - 1 ≠ 0 := sub_ne_zero.mpr hQ1
    field_simp
  · push_neg at hrν
    have hz : wenzlWeight r (q ^ 2 : ℝ) ν = 0 := (wenzlWeight_eq_zero_iff hQ0 hgen hbr ν).mpr hrν
    rw [hz, mul_zero]
    refine Finset.sum_eq_zero fun s _ => ?_
    have hzz : wenzlWeight r (q ^ 2 : ℝ) (addCell ν s.1 s.2) = 0 :=
      (wenzlWeight_eq_zero_iff hQ0 hgen hbr _).mpr
        (lt_of_lt_of_le hrν (colLen_zero_le_addCell s.2))
    rw [hzz, zero_mul]

end QOU.SchurWeyl
