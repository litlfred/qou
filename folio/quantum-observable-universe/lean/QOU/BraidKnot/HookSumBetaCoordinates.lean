import QOU.BraidKnot.HookSumClosedForm
import QOU.SchurWeyl.SchurPrincipalBetaForm

/-!
# The hook sum in β-coordinates

The β-numbers of a Young diagram at `L` rows are the first-column hook lengths of
the diagram padded to `L` rows,

    β_i = λ_i + (L − 1 − i),        i < L,

already in the corpus as `QOU.SchurWeyl.betaR`.  They strictly decrease, and the
multiset of hook lengths of row `i` is `{1, …, β_i}` with the `β_i − β_j` (`j > i`)
removed — which turns two *cell*-indexed statistics into *row*-indexed ones:

| | |
|---|---|
| **(III)** | `Σ_{i<L} β_i = n + L(L−1)/2` |
| **(II)** | `Σ_{c∈μ} h(c) = Σ_{i<L} β_i(β_i+1)/2 − Σ_{i<j<L} (β_i − β_j)` |

Both are stated here doubled, to stay in `ℤ` without division:
`two_mul_sum_betaR` and `two_mul_sum_hookZ_betaForm`.

**(II) is not proved here from the hook multiset.**  It is derived from the
closed form already in `HookSumClosedForm` — `2Σ_h = p₂(λ) + p₂(λ')` — together
with the `n(λ)` register lemmas of that file, which give
`p₂(λ') = n + 2·Σ_i i·λ_i`.  The whole β-side then collapses by a *termwise*
polynomial identity in `(λ_i, L, i)` plus the vanishing of one pure-`L` sum,
`sum_shift_quad_eq_zero`.  That vanishing is the content: `−3Σm² + (2L−1)Σm = 0`
for `m_i = L − 1 − i`, which is why (II) holds for **every** padding `L ≥ ℓ(μ)`
rather than only at `L = ℓ(μ)`.  The padding-independence is not a side remark —
it is what makes the identity usable against whatever row bound a caller already
has, exactly as `HookSumClosedForm`'s `N`/`M` hypotheses are.

## What this is for

The `REV_n` / `Z_n(q)` asymptotics arc (bean `qou-hok7`) works in these
coordinates: the shape free energy's one-body term is `Σ_i F(β_i)` and its
two-body term is `−Σ_{i<j} ε(β_i − β_j)`, and the energy `H = Σ_c h(c)` enters
through exactly (II).  The two identities were verified numerically over every
partition of `n ≤ 16` by
`computations/deltalambda/rev_beta_coordinate_identity_probe.py`; this file is
the formalize-first discharge of that numerical check.

## Prior art

`SYTBetaGapVandermonde` and `SchurPrincipalBetaForm` establish the β-numbers and
their *products* (the Vandermonde denominator of the hook-length formula).  No
identity about **sums** over the β-numbers existed anywhere in the corpus before
this file — the product side and the sum side are independent uses of the same
coordinates.

## Base ring (§7c)

All sums over `ℤ`, matching `HookSumClosedForm` and `PieceAGeneral`.  No `ℝ`, no
ordering, no archimedean input.

-- Ref: [leitner2026] computations/deltalambda/rev_beta_coordinate_identity_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset QOU.BraidKnot.PieceA

/-! ## `betaR` over `ℤ`

`betaR` is a `ℕ` with a truncated subtraction; below `i < L` it is the honest
`λ_i + L − 1 − i`. -/

/-- The β-number of row `i`, cast to `ℤ`, for `i` inside the padded row range. -/
theorem betaR_cast (μ : YoungDiagram) {L i : ℕ} (hi : i < L) :
    ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
      = (μ.rowLen i : ℤ) + (L : ℤ) - 1 - (i : ℤ) := by
  unfold QOU.SchurWeyl.betaR
  omega

/-! ## Two elementary range sums -/

/-- `6 · Σ_{i<L} i² = L(L−1)(2L−1)`, the square-pyramidal closed form over `ℤ`. -/
theorem six_mul_sum_range_sq (L : ℕ) :
    6 * ∑ i ∈ range L, (i : ℤ) ^ 2 = (L : ℤ) * ((L : ℤ) - 1) * (2 * (L : ℤ) - 1) := by
  induction L with
  | zero => simp
  | succ L ih =>
    rw [Finset.sum_range_succ, mul_add]
    push_cast
    push_cast at ih
    linear_combination ih

/-- **The pure-`L` part of the β-form vanishes.** With `m_i = L − 1 − i`,
`−3 Σ m_i² + (2L−1) Σ m_i = 0` for every `L` — the reason (II) is independent of
the padding. -/
theorem sum_shift_quad_eq_zero (L : ℕ) :
    ∑ i ∈ range L, (-3 * ((L : ℤ) - 1 - (i : ℤ)) ^ 2
        + (2 * (L : ℤ) - 1) * ((L : ℤ) - 1 - (i : ℤ))) = 0 := by
  have hterm : ∀ i ∈ range L,
      (-3 * ((L : ℤ) - 1 - (i : ℤ)) ^ 2
          + (2 * (L : ℤ) - 1) * ((L : ℤ) - 1 - (i : ℤ)))
        = -3 * (i : ℤ) ^ 2
          + (6 * ((L : ℤ) - 1) - (2 * (L : ℤ) - 1)) * (i : ℤ)
          + ((2 * (L : ℤ) - 1) * ((L : ℤ) - 1) - 3 * ((L : ℤ) - 1) ^ 2) :=
    fun i _ => by ring
  have hsq : ∑ i ∈ range L, (-3 : ℤ) * (i : ℤ) ^ 2
      = -3 * ∑ i ∈ range L, (i : ℤ) ^ 2 := (Finset.mul_sum _ _ _).symm
  have hlin : ∑ i ∈ range L, (6 * ((L : ℤ) - 1) - (2 * (L : ℤ) - 1)) * (i : ℤ)
      = (6 * ((L : ℤ) - 1) - (2 * (L : ℤ) - 1)) * ∑ i ∈ range L, (i : ℤ) :=
    (Finset.mul_sum _ _ _).symm
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib, Finset.sum_add_distrib,
    hsq, hlin, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  have h2 := two_mul_sum_range_cast L
  have h6 := six_mul_sum_range_sq L
  have key : (6 : ℤ) * (-3 * (∑ i ∈ range L, (i : ℤ) ^ 2)
      + (6 * ((L : ℤ) - 1) - (2 * (L : ℤ) - 1)) * (∑ i ∈ range L, (i : ℤ))
      + (L : ℤ) * ((2 * (L : ℤ) - 1) * ((L : ℤ) - 1) - 3 * ((L : ℤ) - 1) ^ 2)) = 0 := by
    linear_combination (-3 : ℤ) * h6
      + (3 * (6 * ((L : ℤ) - 1) - (2 * (L : ℤ) - 1))) * h2
  linarith

/-- **Upper-triangular sum swap.** `Σ_{i<L} Σ_{i<j<L} g j = Σ_{j<L} j·g j`: the
value `g j` is counted once for each `i < j`. -/
theorem sum_Ico_upper_swap (g : ℕ → ℤ) (L : ℕ) :
    ∑ i ∈ range L, ∑ j ∈ Ico (i + 1) L, g j = ∑ j ∈ range L, (j : ℤ) * g j := by
  induction L with
  | zero => simp
  | succ L ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    have hlast : ∑ j ∈ Ico (L + 1) (L + 1), g j = 0 := by simp
    rw [hlast, add_zero]
    have hsplit : ∀ i ∈ range L, ∑ j ∈ Ico (i + 1) (L + 1), g j
        = (∑ j ∈ Ico (i + 1) L, g j) + g L := by
      intro i hi
      rw [mem_range] at hi
      exact Finset.sum_Ico_succ_top (by omega) g
    rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib, ih, Finset.sum_const,
      Finset.card_range, nsmul_eq_mul]

/-! ## The two β-coordinate identities -/

/-- **(III) The β-numbers sum to `n + L(L−1)/2`**, doubled to stay in `ℤ`:
`2 Σ_{i<L} β_i = 2n + L(L−1)`, for any padding `L` covering the diagram. -/
theorem two_mul_sum_betaR (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    2 * ∑ i ∈ range L, ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
      = 2 * (μ.cells.card : ℤ) + (L : ℤ) * ((L : ℤ) - 1) := by
  have hterm : ∀ i ∈ range L, ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
      = (μ.rowLen i : ℤ) + ((L : ℤ) - 1 - (i : ℤ)) := by
    intro i hi
    rw [mem_range] at hi
    have := betaR_cast μ hi
    linarith
  have hshift : ∑ i ∈ range L, ((L : ℤ) - 1 - (i : ℤ))
      = (L : ℤ) * ((L : ℤ) - 1) - ∑ i ∈ range L, (i : ℤ) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib, sum_rowLen_eq_card μ hL,
    hshift]
  have h2 := two_mul_sum_range_cast L
  linarith

/-- The `Σ_{i<j}(β_i − β_j)` pair sum, collapsed to a single row sum:
`Σ_{i<j<L} (β_i − β_j) = Σ_{i<L} (L − 1 − 2i) β_i`. -/
theorem sum_pair_betaR_sub (μ : YoungDiagram) (L : ℕ) :
    ∑ i ∈ range L, ∑ j ∈ Ico (i + 1) L,
        (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) - ((QOU.SchurWeyl.betaR L μ j : ℕ) : ℤ))
      = ∑ i ∈ range L,
          ((L : ℤ) - 1 - 2 * (i : ℤ)) * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) := by
  set b : ℕ → ℤ := fun i => ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) with hbdef
  have hrow : ∀ i ∈ range L, ∑ j ∈ Ico (i + 1) L, (b i - b j)
      = ((L : ℤ) - 1 - (i : ℤ)) * b i - ∑ j ∈ Ico (i + 1) L, b j := by
    intro i hi
    rw [mem_range] at hi
    have hc : ((L - (i + 1) : ℕ) : ℤ) = (L : ℤ) - 1 - (i : ℤ) := by omega
    rw [Finset.sum_sub_distrib, Finset.sum_const, Nat.card_Ico, nsmul_eq_mul, hc]
  rw [Finset.sum_congr rfl hrow, Finset.sum_sub_distrib, sum_Ico_upper_swap b L,
    ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- **(II) The hook sum in β-coordinates**, doubled to stay in `ℤ`:

    2 Σ_{c∈μ} h(c) = Σ_{i<L} β_i(β_i + 1) − 2 Σ_{i<j<L} (β_i − β_j),

for any padding `L ≥ ℓ(μ)` and any column bound `M ≥ λ_1`.  Equivalently
`Σ_c h(c) = Σ_i C(β_i + 1, 2) − Σ_{i<j}(β_i − β_j)`, which is the row-indexed
form of the statement that row `i`'s hooks are `{1,…,β_i} ∖ {β_i − β_j : j > i}`.

Derived from `two_mul_sum_hookZ_eq_sum_sq` and the `n(λ)`-register lemmas, **not**
from the hook multiset. -/
theorem two_mul_sum_hookZ_betaForm (μ : YoungDiagram) {L M : ℕ}
    (hL : μ.colLen 0 ≤ L) (hM : μ.rowLen 0 ≤ M) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range L,
          ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1)
        - 2 * ∑ i ∈ range L, ∑ j ∈ Ico (i + 1) L,
            (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR L μ j : ℕ) : ℤ)) := by
  have hterm : ∀ i ∈ range L,
      ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1)
          - 2 * (((L : ℤ) - 1 - 2 * (i : ℤ)) * ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ))
        = ((μ.rowLen i : ℤ) ^ 2 + (μ.rowLen i : ℤ) + 2 * (i : ℤ) * (μ.rowLen i : ℤ))
          + (-3 * ((L : ℤ) - 1 - (i : ℤ)) ^ 2
              + (2 * (L : ℤ) - 1) * ((L : ℤ) - 1 - (i : ℤ))) := by
    intro i hi
    rw [mem_range] at hi
    rw [betaR_cast μ hi]
    ring
  have hrhs : ∑ i ∈ range L,
        ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1)
      - 2 * ∑ i ∈ range L, ∑ j ∈ Ico (i + 1) L,
          (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) - ((QOU.SchurWeyl.betaR L μ j : ℕ) : ℤ))
      = (∑ i ∈ range L,
          ((μ.rowLen i : ℤ) ^ 2 + (μ.rowLen i : ℤ) + 2 * (i : ℤ) * (μ.rowLen i : ℤ)))
        + ∑ i ∈ range L, (-3 * ((L : ℤ) - 1 - (i : ℤ)) ^ 2
            + (2 * (L : ℤ) - 1) * ((L : ℤ) - 1 - (i : ℤ))) := by
    rw [sum_pair_betaR_sub μ L, Finset.mul_sum, ← Finset.sum_sub_distrib,
      Finset.sum_congr rfl hterm, Finset.sum_add_distrib]
  rw [hrhs, sum_shift_quad_eq_zero L, add_zero, Finset.sum_add_distrib,
    Finset.sum_add_distrib, sum_rowLen_eq_card μ hL]
  -- Remaining goal: `2 Σ_h = Σ_i λ_i² + n + Σ_i 2·i·λ_i`.
  have h2i : ∑ i ∈ range L, 2 * (i : ℤ) * (μ.rowLen i : ℤ)
      = 2 * ∑ i ∈ range L, (i : ℤ) * (μ.rowLen i : ℤ) := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  have hsq := two_mul_sum_hookZ_eq_sum_sq μ hL hM
  have hfst := two_mul_sum_fst μ hM
  have hb := sum_fst_eq_bStat μ hL
  have hcol := sum_colLen_eq_card μ hM
  have hcolsq : ∑ j ∈ range M, (μ.colLen j : ℤ) ^ 2
      = (μ.cells.card : ℤ) + 2 * ∑ i ∈ range L, (i : ℤ) * (μ.rowLen i : ℤ) := by
    have h : ∑ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1)
        = (∑ j ∈ range M, (μ.colLen j : ℤ) ^ 2) - (μ.cells.card : ℤ) := by
      rw [Finset.sum_congr rfl (fun j _ => by ring :
          ∀ j ∈ range M, (μ.colLen j : ℤ) * ((μ.colLen j : ℤ) - 1)
            = (μ.colLen j : ℤ) ^ 2 - (μ.colLen j : ℤ)),
        Finset.sum_sub_distrib, hcol]
    rw [h, hb] at hfst
    linarith
  rw [h2i]
  linarith

/-! ## (I') The general one-body / two-body decomposition

The identity (II) above is the `g = id` shadow of something much more general, and
the general form is what the `REV_n` arc actually runs on: the shape free energy's
one-body term is `Σ_i F(β_i)` and its two-body term is `−Σ_{i<j} ε(β_i − β_j)`,
for `F` the partial sums of `ε`.

That general form is **already in the corpus multiplicatively** —
`QOU.SchurWeyl.hookSide_betaR` states it for an arbitrary `CommMonoid`, as the
divisor-free hook-length formula with its Vandermonde denominator.  Transporting
it through `Multiplicative N` turns the products into sums at no cost.  So (I')
needs no new combinatorial input here; what it needed was noticing that the
product identity and the sum identity are the same statement. -/

/-- **(I')** For **any** `g : ℕ → N` into an additive commutative monoid,

    Σ_{c∈μ} g(h(c)) + Σ_{i<j<L} g(β_i − β_j) = Σ_{i<L} Σ_{m=1}^{β_i} g(m),

for every padding `L ≥ ℓ(μ)`.  The `j`-index runs as `i+1+k`, matching the
corpus's `hookSide_betaR`; `sum_hookZ_betaForm_of_hookMultiset` below reindexes it
to `Ico (i+1) L`.

Row `i`'s hook lengths are `{1, …, β_i}` with `{β_i − β_j : j > i}` removed — that
is the whole content, and it is `hookSide_betaR`'s, not this file's. -/
theorem sum_hookF_add_pairF {N : Type*} [AddCommMonoid N] (g : ℕ → N)
    (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    (∑ c ∈ μ.cells, g (QOU.QBeta.WenzlWeight.hook μ c))
        + ∑ i ∈ range L, ∑ k ∈ range (L - (i + 1)),
            g (QOU.SchurWeyl.betaR L μ i - QOU.SchurWeyl.betaR L μ (i + 1 + k))
      = ∑ i ∈ range L, ∑ j ∈ range (QOU.SchurWeyl.betaR L μ i),
          g (QOU.SchurWeyl.betaR L μ i - j) := by
  have h := QOU.SchurWeyl.hookSide_betaR
    (M := Multiplicative N) (fun n => Multiplicative.ofAdd (g n)) hL
  apply Multiplicative.ofAdd.injective
  simp only [QOU.Mathlib.SYTBeta.descFactF] at h
  simpa only [ofAdd_add, ofAdd_sum] using h

/-! ## The β-side does not see the padding

(I') has `L` on its right-hand side and on one summand of its left, but the *other*
summand — the cell sum — has no `L` at all.  Rearranged over a group that is the whole
statement of the two results below: **the one-body sum minus the pair sum is the cell
sum**, hence is the same for every admissible padding.

This is exactly the quantity the `REV_n` arc calls the β-side,
`Σ_i F(β_i) − Σ_{i<j} ε(β_i − β_j)` with `F` the partial sums of `ε` — take
`g = ε` and note `Σ_{j<β_i} g(β_i − j) = Σ_{m=1}^{β_i} ε(m) = F(β_i)`.  Since the
hook sum `H = Σ_c h(c)` is cell-indexed and likewise `L`-free, the arc's whole
objective `V` is padding-invariant.

**Why this is worth a name.** A maximisation of `V` over shapes *at fixed row count*
`ℓ` is a real search; a maximisation *over* `ℓ` above the shape's own row count is
not a search at all — it is re-reading one number.  PR #7294 scanned `ℓ ∈ [k, k+5]`
and recorded a caveat that three of its eleven points "sit at the cap, so those three
are censored downward".  That caveat is **withdrawn**: the theorem says the scan was
over padding, so a value at the cap is the same value as at every larger `ℓ`, and the
only content in the scan is that `ℓ` must be at least the maximiser's row count (which
is why `ℓ = k` and `ℓ = k+1` genuinely lose).  Measured in agreement afterwards —
`rev_l_cap_is_padding_invariance_probe.py`, where the residual across `ℓ` is `1e-49`
at `mp.dps = 50`. -/

/-- **The β-side is the cell sum.**  For any `g` into an additive commutative *group*,

    Σ_{i<L} Σ_{m=1}^{β_i} g(m) − Σ_{i<j<L} g(β_i − β_j) = Σ_{c∈μ} g(h(c)) .

The right-hand side carries no `L`, so the left-hand side is the same for every
padding `L ≥ ℓ(μ)`. -/
theorem betaSide_eq_hookSum {N : Type*} [AddCommGroup N] (g : ℕ → N)
    (μ : YoungDiagram) {L : ℕ} (hL : μ.colLen 0 ≤ L) :
    (∑ i ∈ range L, ∑ j ∈ range (QOU.SchurWeyl.betaR L μ i),
          g (QOU.SchurWeyl.betaR L μ i - j))
        - ∑ i ∈ range L, ∑ k ∈ range (L - (i + 1)),
            g (QOU.SchurWeyl.betaR L μ i - QOU.SchurWeyl.betaR L μ (i + 1 + k))
      = ∑ c ∈ μ.cells, g (QOU.QBeta.WenzlWeight.hook μ c) := by
  rw [← sum_hookF_add_pairF g μ hL]
  abel

/-- **Padding invariance, subtraction-free.**  The same statement over a mere additive
commutative *monoid*: the β-side at `L` and at `L'` agree, written without subtraction
by adding the other padding's pair sum to each. -/
theorem betaSide_padding_invariant {N : Type*} [AddCommMonoid N] (g : ℕ → N)
    (μ : YoungDiagram) {L L' : ℕ} (hL : μ.colLen 0 ≤ L) (hL' : μ.colLen 0 ≤ L') :
    (∑ i ∈ range L, ∑ j ∈ range (QOU.SchurWeyl.betaR L μ i),
          g (QOU.SchurWeyl.betaR L μ i - j))
        + ∑ i ∈ range L', ∑ k ∈ range (L' - (i + 1)),
            g (QOU.SchurWeyl.betaR L' μ i - QOU.SchurWeyl.betaR L' μ (i + 1 + k))
      = (∑ i ∈ range L', ∑ j ∈ range (QOU.SchurWeyl.betaR L' μ i),
            g (QOU.SchurWeyl.betaR L' μ i - j))
        + ∑ i ∈ range L, ∑ k ∈ range (L - (i + 1)),
            g (QOU.SchurWeyl.betaR L μ i - QOU.SchurWeyl.betaR L μ (i + 1 + k)) := by
  rw [← sum_hookF_add_pairF g μ hL, ← sum_hookF_add_pairF g μ hL']
  abel

/-! ## (II) again, from the hook multiset — an independent second proof

Everything above (II) went through `HookSumClosedForm`'s `2Σ_h = p₂(λ) + p₂(λ')`.
The route below instead specialises (I') at `g = (· : ℤ)`.  The two proofs share
no step: one is a reflection argument over the cells, the other is the hook-length
formula's β-multiset.  Agreement is therefore a check on both. -/

/-- The corpus's `ℕ`-valued hook, cast to `ℤ`, is `hookZ` — on a genuine cell,
where both truncated subtractions are honest. -/
theorem wenzlHook_cast (μ : YoungDiagram) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    ((QOU.QBeta.WenzlWeight.hook μ c : ℕ) : ℤ) = hookZ μ c := by
  have hmem : (c.1, c.2) ∈ μ := by simpa using (YoungDiagram.mem_cells c).mp hc
  have hrow : c.2 < μ.rowLen c.1 := YoungDiagram.mem_iff_lt_rowLen.mp hmem
  have hcol : c.1 < μ.colLen c.2 := YoungDiagram.mem_iff_lt_colLen.mp hmem
  rw [hookZ_eq]
  unfold QOU.QBeta.WenzlWeight.hook
  omega

/-- `2 Σ_{j<b} (b − j) = b(b+1)`: the descending sum `b + (b−1) + ⋯ + 1`. -/
theorem two_mul_sum_desc (b : ℕ) :
    2 * ∑ j ∈ range b, ((b - j : ℕ) : ℤ) = (b : ℤ) * ((b : ℤ) + 1) := by
  have hterm : ∀ j ∈ range b, ((b - j : ℕ) : ℤ) = (b : ℤ) - (j : ℤ) := by
    intro j hj
    rw [mem_range] at hj
    omega
  rw [Finset.sum_congr rfl hterm, Finset.sum_sub_distrib, Finset.sum_const,
    Finset.card_range, nsmul_eq_mul]
  have h2 := two_mul_sum_range_cast b
  linear_combination (-1 : ℤ) * h2

/-- **(II), proved a second time** — from the hook multiset (I') rather than from
the closed form.  Statement identical to `two_mul_sum_hookZ_betaForm`, and it needs
**no** column bound `M`. -/
theorem sum_hookZ_betaForm_of_hookMultiset (μ : YoungDiagram) {L : ℕ}
    (hL : μ.colLen 0 ≤ L) :
    2 * ∑ c ∈ μ.cells, hookZ μ c
      = ∑ i ∈ range L,
          ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1)
        - 2 * ∑ i ∈ range L, ∑ j ∈ Ico (i + 1) L,
            (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR L μ j : ℕ) : ℤ)) := by
  have key := sum_hookF_add_pairF (fun m => (m : ℤ)) μ hL
  -- (a) the cell sum is the `hookZ` sum
  have ha : ∑ c ∈ μ.cells, ((QOU.QBeta.WenzlWeight.hook μ c : ℕ) : ℤ)
      = ∑ c ∈ μ.cells, hookZ μ c :=
    Finset.sum_congr rfl fun c hc => wenzlHook_cast μ hc
  -- (b) the pair sum, reindexed from `range (L − (i+1))` to `Ico (i+1) L`
  have hb : ∀ i ∈ range L,
      ∑ k ∈ range (L - (i + 1)),
          ((QOU.SchurWeyl.betaR L μ i - QOU.SchurWeyl.betaR L μ (i + 1 + k) : ℕ) : ℤ)
        = ∑ j ∈ Ico (i + 1) L,
            (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ)
              - ((QOU.SchurWeyl.betaR L μ j : ℕ) : ℤ)) := by
    intro i hi
    rw [mem_range] at hi
    rw [Finset.sum_Ico_eq_sum_range]
    refine Finset.sum_congr rfl fun k hk => ?_
    rw [mem_range] at hk
    have hlt : QOU.SchurWeyl.betaR L μ (i + 1 + k) < QOU.SchurWeyl.betaR L μ i :=
      QOU.SchurWeyl.betaR_lt (by omega) (by omega)
    omega
  -- (c) the descending sums
  have hc2 : 2 * ∑ i ∈ range L, ∑ j ∈ range (QOU.SchurWeyl.betaR L μ i),
        ((QOU.SchurWeyl.betaR L μ i - j : ℕ) : ℤ)
      = ∑ i ∈ range L,
          ((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) * (((QOU.SchurWeyl.betaR L μ i : ℕ) : ℤ) + 1) := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => two_mul_sum_desc _
  rw [ha, Finset.sum_congr rfl hb] at key
  linarith [key, hc2]

end QOU.BraidKnot.HookSum
