import QOU.SchurWeyl.OcneanuWeightWenzl

/-!
# QOU.SchurWeyl.WenzlWeightLevelR — the normalised Wenzl weight at a general level `r`

The convention-D chain proved in PR #5575 — vanishing, branching, normalisation, uniqueness —
is stated at Wenzl **level `r = 2`**, because that is where convention D sits
(`wenzlLevel_conventionD`).  Nothing in the *vanishing* half needs `r = 2`:
`QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` is already general in `r`, and it was only the
downstream specialisation that fixed the level.  This file removes that specialisation.

| | |
|---|---|
| `levelBracket r Q` | `1 + Q + ⋯ + Q^{r−1}`, the level-`r` principal specialisation of the one-box Schur function |
| `wenzlWeight r Q μ` | `s_μ(1, Q, …, Q^{r−1}) / [r]_Q^{|μ|}` — the normalised weight at level `r` |
| `wenzlWeight_eq_zero_iff` | **`w_μ = 0 ⟺ ℓ(μ) > r`**, for every `n`, every `μ` and every level `r` |
| `wenzlMarkovParam_eq` | Wenzl's `z_W = Q^r(1−Q)/(1−Q^r)` is `Q^r / [r]_Q` |
| `wenzlWeight_two_eq_ocneanuWeight` | at `r = 2`, `Q = q²` this **is** the convention-D Ocneanu weight |
| `wenzlMarkovParam_conventionD` | and its Markov parameter **is** `q · z_D` |

## Why the last two rows matter

A generalisation that does not contain its own special case is a different object wearing the same
name.  The two convention-D theorems are the evidence that this one does: at `r = 2`, `Q = q²` the
normalised level-`r` weight is *definitionally* the weight the merged chain works with, and its
level-`r` Markov parameter is *definitionally* `q · z_D`.  So every statement proved here at general
`r` specialises back to a statement about the object PR #5575 proved things about, rather than to a
lookalike.

## Branching at general `r` — proved downstream, not here

**Status corrected 2026-08-24 (bean `qou-4a68`).**  This section previously recorded general-`r`
branching as an open item on bean `qou-j7ln`.  It is **proved, sorry-free**, in the files that
import this one:

* `BranchingGenericity.sum_schurPrincipal_addCellOrSelf` — the identity itself,
  `∑_{s addable to μ} s_{μ+s}(1, …, Q^{r−1}) = [r]_Q · s_μ(1, …, Q^{r−1})`;
* `AddableCellIndexing.sum_addable_wenzlWeight` — the same for the normalised weight, in the
  addable-cell subtype indexing the corner exchange hands over;
* `WenzlNormalisation.sum_addable_wenzlWeight_all` — with the row-count hypothesis removed.

The pessimism this section used to record was about a *route*, and the route was avoidable.  That identity is Pieri's rule
at the principal specialisation — Orellana's Lemma 5.1 `[orellana1998]`, proved there by the
Littlewood–Richardson rule on the integer-level lattice `Q = −q^{r₁+m}` followed by rational
continuation — and neither half is in Mathlib.  The proof that landed does not go through either:
it works directly from `schurPrincipal_addCell_eq`'s per-row β-factor form, with the four
non-vanishing side conditions all derived from the single `hgen`.  So "not in Mathlib" was true and
"therefore open here" did not follow.

What remains true is the reading of the two-row case: `OcneanuWeightBranching` rests on
`schurPrincipal_twoRow`, a closed form that exists because the hook-content product *telescopes* for
a two-row diagram, and there is no such telescoping at general `r`.  The general-`r` proof replaces
the telescoping with the β-factor identity rather than recovering it.

## Base ring (§7c)

Generic `[Field R]` throughout — a rational function of `Q`.  No ordering, no `Real.sqrt`, no `ℝ`.

LaTeX label: `thm:wenzl-weight-level-r`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.QBeta.WenzlWeight

variable {R : Type*} [Field R] {r : ℕ}

/-! ## The level bracket -/

/-- `[r]_Q = 1 + Q + ⋯ + Q^{r−1}`.

This is `s_{[1]}(1, Q, …, Q^{r−1})`, the principal specialisation of the one-box Schur function —
the factor Wenzl's normalisation divides by, once per cell. -/
noncomputable def levelBracket (r : ℕ) (Q : R) : R := ∑ i ∈ Finset.range r, Q ^ i

theorem levelBracket_two (Q : R) : levelBracket 2 Q = 1 + Q := by
  simp [levelBracket, Finset.sum_range_succ]

/-- `1 − Q^r = (1 − Q)·[r]_Q`. -/
theorem one_sub_pow_eq_mul_levelBracket (r : ℕ) (Q : R) :
    1 - Q ^ r = (1 - Q) * levelBracket r Q := by
  induction r with
  | zero => simp [levelBracket]
  | succ n ih =>
    have hstep : levelBracket (n + 1) Q = levelBracket n Q + Q ^ n := by
      simp [levelBracket, Finset.sum_range_succ]
    rw [hstep, mul_add, ← ih]
    ring

/-- A `Q` that is not a root of unity is not `1`. -/
theorem ne_one_of_gen {Q : R} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) : Q ≠ 1 :=
  fun h => hgen 1 one_ne_zero (by rw [h]; simp)

/-- **The level bracket is nonzero under genericity.**

`[r]_Q = 0` would make `1 − Q^r = (1 − Q)·[r]_Q` vanish, i.e. `Q^r = 1` with `r ≠ 0`.  So the `hbr`
side condition carried separately through the level-`r` chain is *implied* by `hgen`, and the chain
runs on one genericity assumption rather than two. -/
theorem levelBracket_ne_zero_of_gen {Q : R} {r : ℕ}
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hr : r ≠ 0) : levelBracket r Q ≠ 0 := by
  intro h
  have h1 : (1 : R) - Q ^ r = (1 - Q) * levelBracket r Q :=
    one_sub_pow_eq_mul_levelBracket r Q
  rw [h, mul_zero, sub_eq_zero] at h1
  exact hgen (r : ℤ) (by exact_mod_cast hr) (by rw [zpow_natCast, ← h1])

/-! ## The normalised weight -/

/-- **The normalised Wenzl weight at level `r`.**

`w_μ^{(r)}(Q) = s_μ(1, Q, …, Q^{r−1}) / [r]_Q^{|μ|}`.

The normalisation is the one that makes `∑_{μ ⊢ n} f^μ w_μ = tr(1) = 1`: each of the `n` cells
contributes one factor of `[r]_Q`, which is exactly what the branching identity consumes. -/
noncomputable def wenzlWeight (r : ℕ) (Q : R) (mu : YoungDiagram) : R :=
  schurPrincipal r Q mu / levelBracket r Q ^ mu.cells.card

theorem wenzlWeight_bot (r : ℕ) (Q : R) : wenzlWeight r Q (⊥ : YoungDiagram) = 1 := by
  simp [wenzlWeight, schurPrincipal, nPart]

/-- **The vanishing criterion at a general level.**

`w_μ^{(r)}(Q) = 0 ⟺ μ has more than `r` rows.`

At `r = 2` this is the Temperley–Lieb row cap; at general `r` it is the `SU(r)` level-`r` cap, and
it is the reason the level-`r` trace factors through the quotient by the `≥ (r+1)`-row blocks.

The root-of-unity hypothesis `hQ` is doing real work — without it a *hook length* can kill a
denominator and the `iff` fails — and so is `hbr`: at `[r]_Q = 0` the normalisation is undefined and
every weight would read as `0/0`. -/
theorem wenzlWeight_eq_zero_iff {Q : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hbr : levelBracket r Q ≠ 0) (mu : YoungDiagram) :
    wenzlWeight r Q mu = 0 ↔ r < mu.colLen 0 := by
  have hden : (levelBracket r Q) ^ mu.cells.card ≠ 0 := pow_ne_zero _ hbr
  rw [wenzlWeight, div_eq_zero_iff]
  simp only [hden, or_false]
  exact schurPrincipal_eq_zero_iff hQ0 hQ r mu

/-- The surviving side, stated positively: at most `r` rows ⇒ nonzero weight. -/
theorem wenzlWeight_ne_zero_of_le_rows {Q : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hbr : levelBracket r Q ≠ 0) (mu : YoungDiagram)
    (h : mu.colLen 0 ≤ r) : wenzlWeight r Q mu ≠ 0 := by
  rw [Ne, wenzlWeight_eq_zero_iff hQ0 hQ hbr]
  omega

/-! ## Wenzl's Markov parameter at level `r` -/

/-- **Wenzl's level-`r` Markov parameter, in bracket form.**

`z_W = Q^r(1−Q)/(1−Q^r) = Q^r / [r]_Q`.

The `(1−Q)/(1−Q^r)` of the literature is `1/[r]_Q` once the geometric factor is cancelled; the
bracket form is the one that survives `Q = 1`, and the one the normalisation of `wenzlWeight` is
stated in. -/
theorem wenzlMarkovParam_eq (r : ℕ) (Q : R) (hbr : levelBracket r Q ≠ 0) (hQ1 : (1 : R) - Q ≠ 0) :
    Q ^ r * (1 - Q) / (1 - Q ^ r) = Q ^ r / levelBracket r Q := by
  rw [one_sub_pow_eq_mul_levelBracket r Q]
  field_simp

/-! ## Recovering the level from the parameter -/

/-- Wenzl's parameter relation holds at `z_W = Q^r / [r]_Q`, in the denominator-cleared form
`QBeta.WenzlWeight.level_unique_of_markovParameter` consumes. -/
theorem wenzlMarkovParam_spec {Q : R} {r : ℕ} (hbr : levelBracket r Q ≠ 0) :
    Q ^ r / levelBracket r Q * (1 - Q ^ r) = Q ^ r * (1 - Q) := by
  rw [one_sub_pow_eq_mul_levelBracket r Q]
  field_simp

/-- **Equal level-`r` Markov parameters force equal levels.**

The `q` of `z_r = Q^r/(q·[r]_Q)` is the Hecke-normalisation shift; clearing it lands on Wenzl's
`Q^r/[r]_Q`, where `level_unique_of_markovParameter` applies. -/
theorem level_unique_of_wenzlMarkovParam_eq {q : R} (hq0 : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : R)) ^ k ≠ 1) {r s : ℕ} (hr : r ≠ 0) (hs : s ≠ 0)
    (h : (q ^ 2) ^ r / (q * levelBracket r (q ^ 2))
        = (q ^ 2) ^ s / (q * levelBracket s (q ^ 2))) : r = s := by
  have hbr : levelBracket r (q ^ 2) ≠ 0 := levelBracket_ne_zero_of_gen hgen hr
  have hbs : levelBracket s (q ^ 2) ≠ 0 := levelBracket_ne_zero_of_gen hgen hs
  have e : ∀ t : ℕ, (q ^ 2) ^ t / (q * levelBracket t (q ^ 2))
      = (q ^ 2) ^ t / levelBracket t (q ^ 2) / q := fun t => by rw [mul_comm, div_div]
  rw [e r, e s] at h
  have key : (q ^ 2) ^ r / levelBracket r (q ^ 2) = (q ^ 2) ^ s / levelBracket s (q ^ 2) := by
    have h2 := congrArg (fun x : R => x * q) h
    simp only at h2
    rwa [div_mul_cancel₀ _ hq0, div_mul_cancel₀ _ hq0] at h2
  refine QOU.QBeta.WenzlWeight.level_unique_of_markovParameter (pow_ne_zero 2 hq0) hgen
    (wenzlMarkovParam_spec hbr) ?_
  rw [key]
  exact wenzlMarkovParam_spec hbs

/-! ## Conservativity: at `r = 2`, `Q = q²` this is the convention-D object -/

/-- **The level-2 weight is the convention-D Ocneanu weight**, on the nose.

`wenzlWeight 2 (q²) μ = ocneanuWeight q (q³/(q²+1)) μ` — so every general-`r` statement above
specialises back to a statement about the weight the merged convention-D chain works with. -/
theorem wenzlWeight_two_eq_ocneanuWeight (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (mu : YoungDiagram) :
    wenzlWeight 2 (q ^ 2) mu = ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu := by
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21 mu, wenzlWeight, levelBracket_two,
    add_comm (1 : R) (q ^ 2)]

/-- **The level-2 Markov parameter is `q · z_D`.**

The factor `q` is the Hecke-normalisation shift between `g² = (Q−1)g + Q` and `σ² = (q − q⁻¹)σ + 1`,
under which `σ = g/q` and `Q = q²` — the same shift `wenzlLevel_conventionD` inverts through. -/
theorem wenzlMarkovParam_conventionD (q : R) (hq21 : q ^ 2 + 1 ≠ 0) :
    (q ^ 2) ^ 2 / levelBracket 2 (q ^ 2) = q * (q ^ 3 / (q ^ 2 + 1)) := by
  have h1 : (1 : R) + q ^ 2 ≠ 0 := by rwa [add_comm]
  rw [levelBracket_two]
  field_simp
  ring

/-- The level-2 bracket is nonzero exactly under the hypothesis the convention-D chain already
carries, so `wenzlWeight_eq_zero_iff` at `r = 2` needs nothing new. -/
theorem levelBracket_two_ne_zero {q : R} (hq21 : q ^ 2 + 1 ≠ 0) :
    levelBracket 2 (q ^ 2) ≠ 0 := by
  rw [levelBracket_two, add_comm]
  exact hq21

end QOU.SchurWeyl
