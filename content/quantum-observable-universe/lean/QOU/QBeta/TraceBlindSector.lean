/-
# The observable is blind to 588 of the 720 dimensions binding lives in

> ## 🛑 THE READING IS CORRECTED (2026-09-01, bean `qou-i9gk`)
>
> This file's title and its `blind_sector` gloss say the `>2`-row blocks carry
> information *the observable cannot see*. They carry **no states at `N = 2`**.
>
> The `>2`-row blocks span the **kernel** of `H_n(q) → TL_n(q)`: measured at
> `n = 3..8`, `ω_λ = 0 ⟺ ℓ(λ) > 2` exactly, and `∑ d_λ²` over the `≤2`-row
> blocks is `Catalan(n)` at every `n`. Since `TL_n(q) = End_{U_q(sl₂)}(V^{⊗n})`,
> that kernel is precisely the part of the algebra acting as **zero** on the
> `N = 2` physical space. It is the Schur–Weyl row cap (`qou-fvzm`), not a
> second, independent vanishing.
>
> **And the reading contradicts the convention it was measured in.**
> `QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean` (bean `qou-n1dj`)
> proves the `ℓ > 2` channels are absent at `N = 2`, and that `y_{(1³)} = 0`
> forces **Jones** — with one open premise between them, that the mass trace *is*
> the categorical trace of the fibre action on `V^{⊗n}`. Convention D is forced
> **by** the premise that empties the blind sector. Measuring in D and then
> reading D's zeros as hidden information asserts both the premise and its
> negation.
>
> **And the premise is NOT open.** `qou-n1dj` is **resolved** — its status is
> `todo` only because closing a bean is a human action (AGENTS.md §4a), and
> `qou-cds1` itself already recorded this at line 4285. Verified here:
> `lem:feynman-eigenbasis-decomposition` **defines** the mass channel as
> `V^{⊗n} ≅ ⊕_{λ ⊢ n, ℓ(λ) ≤ 2} V_λ ⊗ S_λ` — the row cap is **in the index set** —
> and `FibreDimensionForcesTL.lean` (sorry-free) proves `z·[N]_q = q^N`, so a
> two-dimensional fibre leaves **no residual trace freedom**.
> `MassTraceIsFibreCategorical` is a Lean *class* only because no quantum
> Schur–Weyl development exists in this tree; its content is already asserted by
> the mass chapter. **So the blind sector is unphysical FULL STOP, and Step 27's
> headline is false rather than conditional.**
>
> **What survives.** The theorems below are all still true — `blind_sector` is a
> statement about weighted sums and is independent of any of this, and the
> dimension arithmetic is arithmetic. What changes is only what they *mean*:
> `588` is the dimension of the kernel, not of a hidden sector. And since
> `N_min(λ) = ℓ(λ)`, the two small eigenphases Step 27 found need `N ≥ 3`
> (`(3,2,1)`) and `N ≥ 4` (`(2,2,1,1)`) respectively — so the `0.13 %` sum
> coincidence requires `N ≥ 4`, which nothing in the corpus motivates.
>
> **🛑 THIRD CORRECTION, same day — the last positive goes too.** The reading
> *"(3,2,1) is an ℓ = 3 block carrying the largest binding character, so this
> measures what an `N = 3` extension would carry"* cited **`qou-fvzm`'s REOPENED
> paragraph**. That bean is **`status: completed`**, and its line 18 closes
> exactly that paragraph: *"my reopened form … is closed — the route is
> **UNAVAILABLE**, not merely hard"*, and *"**THE MISSING ADDITIVE TERM IS NOT A
> HECKE-TRACE OBJECT AT ALL**."* Moving to `N = 3` re-weights channels the mass
> pipeline already evaluates (`y_(2,1)/y_(3) = q[2]_q[N−1]_q/[N+2]_q` differs at
> every `q`), so it is a **regression risk, not an opening**. The surviving
> candidates that bean names are the ones that were never trace objects — the
> extended-Bloch route (`qou-985x`) and the atomic-braid→nucleus map (`qou-imcd`).
>
> **So Steps 27–28 retain no positive claim about the blind sector at all.** What
> stands from that arc is the construction `Δ_bind = P·(I−1)·N` (validated to
> `5.4·10⁻¹⁵`, genuinely `H₆`-valued) and the chain-vs-all-pairs structural
> finding.
>
> Measured in `computations/qbeta/qbeta_blind_sector_is_the_tl_kernel_probe.py`
> (4/4).

Bean `qou-cds1`, Step 27. Computed and validated in
`computations/qbeta/qbeta_level_k_binding_operator_probe.py` (6/6).

## The construction being formalised

Binding is never observed. What is observed is the mass of the free constituents
and the mass of the bound composite; binding is their **difference**. Do the same
subtraction one level up — not to the numbers but to the **operators**:

    Δ_bind  =  β_atom − β_free                                 (in `H_{3A}(q)`)

`β_atom` is `atom_braid_word_3A(Z, N, include_inter := true)`, `β_free` the same
word with the inter-nucleon interfaces dropped. For the deuteron (`3A = 6`) the
word factors exactly as `Δ_bind = P · (I − 1) · N`, where `P` and `N` are the two
nucleons on generators `{0,1}` and `{3,4}` and `I` is the single interface letter
at generator `2`. `β_free` lives in `H₃ ⊗ H₃`; `I − 1 = σ₂ + (d−1)·1` does not, so
**`Δ_bind` is genuinely `H₆`-valued** and the branching argument of Step 24 —
which is what let Steps 24–26 dismiss the tower — does not reach it.

`tr_M` is linear, so `tr_M(Δ_bind)` is exactly the binding number the corpus
already computes (`markov_trace_binding` below). But `Δ_bind` is an operator, and
an operator has a spectrum that no linear functional determines.

## The blind sector

Convention D is the SU(2) / Temperley–Lieb (Jones) trace, `z = q³/(q²+1)`, so it
factors through the TL quotient, whose irreps are the partitions with **at most
two rows**. Measured at `n = 6`: the Ocneanu weights are `|ω| ~ 10⁻¹` on the four
such shapes and `|ω| < 2·10⁻¹⁶` on the other seven. `visible_dim` and
`total_dim` below confirm it by arithmetic instead — `132 = C₆ = dim TL₆` against
`720 = 6! = dim H₆`, leaving `588` dimensions that contribute nothing to the
observable no matter what they contain.

`blind_sector` is the formal content of that: a weighted sum whose weights vanish
on a set is **unchanged** by altering the summand there. And
`spectrum_not_determined_by_trace` is why it matters — two operators can share a
weighted trace and differ in spectrum, so a blind block's eigenphases are not
constrained by any measurement the corpus makes.

## What is *not* here

The eigenphases themselves (`0.0252506` in `(3,2,1)`, `0.0195531` in `(2,2,1,1)`
— the first values in this arc *below* the required ladder phase), the
`(2,2,1,1)` ellipticity wall, and the `1.07·10⁷ σ` distance from the substrate
pin at which their sum meets the required phase. Those are **measurements**, they
belong in the witness, and the sum in particular is an unmotivated combination
recorded as a target rather than a result.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import QOU.QBeta.TraceRealSpectrumComplex

namespace QOU.QBeta

open Finset

/-! ### Binding is a difference, and the trace is linear -/

/-- The binding number is the trace of the binding **operator**. Trivial as
algebra, and the whole point of the construction: because `tr_M` is linear, the
subtraction can be done on the operators instead of on the numbers, and what
comes out is an operator whose spectrum the numbers never saw. -/
theorem markov_trace_binding {ι : Type*} (s : Finset ι) (w chiAtom chiFree : ι → ℝ) :
    (∑ i ∈ s, w i * chiAtom i) - (∑ i ∈ s, w i * chiFree i)
      = ∑ i ∈ s, w i * (chiAtom i - chiFree i) := by
  rw [← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun _ _ => by ring

/-! ### The blind sector -/

/-- **The observable cannot see a zero-weight block.** If the weights vanish on
`S`, the weighted sum is identical for any two summands agreeing off `S` —
whatever they do on `S`. At `n = 6` under convention D, `S` is the seven
partitions with more than two rows, and `Δ_bind`'s character there is large
(`χ_{(3,2,1)} = −9.598`, the biggest of any block) and contributes nothing. -/
theorem blind_sector {ι : Type*} [DecidableEq ι] (s S : Finset ι) (w f g : ι → ℝ)
    (hw : ∀ i ∈ S, w i = 0) (hfg : ∀ i ∈ s, i ∉ S → f i = g i) :
    ∑ i ∈ s, w i * f i = ∑ i ∈ s, w i * g i := by
  refine Finset.sum_congr rfl fun i hi => ?_
  by_cases h : i ∈ S
  · rw [hw i h]; ring
  · rw [hfg i hi h]

/-- The dimensions of the eleven irreps of `H₆`, in the order
`(6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1), (3,1,1,1), (2,2,2), (2,2,1,1),
(2,1⁴), (1⁶)`. -/
def h6Dims : List ℕ := [1, 5, 9, 10, 5, 16, 10, 5, 9, 5, 1]

/-- Which of them convention D can see: exactly the partitions with at most two
rows. -/
def h6Visible : List Bool := [true, true, true, false, true, false,
                              false, false, false, false, false]

/-- `∑ d² = 720 = 6! = dim H₆` — the Artin–Wedderburn count, so the list is the
right one. -/
theorem total_dim :
    1*1 + 5*5 + 9*9 + 10*10 + 5*5 + 16*16 + 10*10 + 5*5 + 9*9 + 5*5 + 1*1 = 720 := by
  norm_num

/-- `∑ d² over the visible blocks = 132 = C₆ = dim TL₆`. Convention D factors
through the Temperley–Lieb quotient, and this is that quotient's dimension
recovered from the block list — an arithmetic confirmation independent of the
numerically-measured Ocneanu weights. -/
theorem visible_dim : 1*1 + 5*5 + 9*9 + 5*5 = 132 := by norm_num

/-- **588 of 720 dimensions are invisible to the observable** — 81.7 % of the
algebra the binding operator lives in. -/
theorem blind_dim : 720 - 132 = 588 := by norm_num

/-- And the blindness deepens with the nucleus. At `A = 3` the strand count is
`n = 9`, so the observable sees `C₉ = 4862` of `9! = 362880` dimensions — **98.66 %
blind**, against 81.67 % at `A = 2`. The visible share is `Cₙ/n! ~ 4ⁿ/n!`, which
falls super-exponentially: by `A = 6` it is `7.5·10⁻⁶` %. -/
theorem blind_dim_A3 : 362880 - 4862 = 358018 := by norm_num

/-! ### Why the blind sector is not merely unmeasured but unconstrained -/

/-- **A weighted trace does not determine a spectrum.** Two operators sharing
every trace the corpus computes can differ in discriminant — one elliptic, one
hyperbolic. So the eigenphases of a zero-weight block are not constrained by any
measurement, which is what makes the blind sector a place a phase could live
without contradicting anything.

Witness on the invariants: `tr = 0` with `det = 1` (elliptic, `disc = −4`) and
`tr = 0` with `det = −1` (hyperbolic, `disc = +4`). -/
theorem spectrum_not_determined_by_trace :
    IsElliptic 0 1 ∧ ¬ IsElliptic 0 (-1) := by
  constructor <;> unfold IsElliptic <;> norm_num

/-- The same statement in the form the blind sector uses it: a block carrying
weight zero contributes `0` to the observable for **either** operator, so the
observable is consistent with both the elliptic and the hyperbolic one. -/
theorem zero_weight_admits_both_spectra (w : ℝ) (hw : w = 0) (trA trB : ℝ) :
    w * trA = w * trB ∧ (IsElliptic 0 1 ∧ ¬ IsElliptic 0 (-1)) := by
  refine ⟨by rw [hw]; ring, spectrum_not_determined_by_trace⟩

end QOU.QBeta
