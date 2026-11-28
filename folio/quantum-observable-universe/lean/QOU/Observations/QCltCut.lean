import QOU.Core.CutLimit
import QOU.Core.QGaussianMoments
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Observations.QCltCut — the q-CLT as convergence of located cuts to ℤ[q] moments

Bean `qou-e1uf` (item 6 of epic `qou-dk7p`), strangler step 2.

## Restated 2026-11-27 (owner pick "Do both")

The first version of this class carried `momentSequence : ℕ → ℕ → K` as a **free
field**. Nothing tied it to a state or to a generator sum, so any sequence
converging to the q-Gaussian moments discharged it: the class asserted nothing
about `tr_M`. It is restated here so the moments are **computed** from data:

* an algebra `A` over `K`, a tracial normalised state `state : A →ₗ[K] K` (the
  intended instance is the Markov trace `tr_M` on the Hecke tower, which is a
  trace and satisfies `tr_M(1) = 1`), and a sequence `sum n ∈ A` (the centred
  generator sum `Σ_{i<n} (σ_i - tr_M(σ_i))`);
* the normalised **even** moment `state (sum n ^ (2k)) / n ^ k`. Odd moments are
  dropped: normalising them needs `√n`, which is not in an arbitrary ordered
  field. For a centred symmetric limit they carry no information;
* the limit of the `2k`-th moment is pinned to `v ^ k · qGaussMoment (2k)` at `q`,
  with `v ≠ 0` the limit variance.

## The pin fails for `q ≠ 1`

`q_eq_one_of_fourth_limit`: if the normalised fourth moment converges to the
classical value `3 v²`, the class forces `q = 1`. The exact computation
`computations/probes/qclt_fourth_moment_exact_probe.py` (rational arithmetic,
convention D, `q = 11/10, 3/2, 2`) finds the fourth-moment ratio of the
convention-D Markov trace tending to `3`, so **the `tr_M` instance of this class
exists at most at `q = 1`**. The reason: the Markov trace is a product state on
`V^{⊗N}`, crossing pair partitions weigh `1`, and the limit is the classical
Gaussian. Audit: `docs/audits/2026-11-27-qclt-fourth-moment-classical.md`.

The analytic proof that `tr_M` gives `3 v²` (the classical CLT for the Markov
trace) is **not** in this file; it is the open hypothesis `ClassicalClt` below,
the `q = 1` member of the class.

`@conjecture: primary`. No instance is provided. No empirical value enters.
-/

namespace QOU.Observations.QCltCut

open Polynomial QOU.Core.CutLimit QOU.Core.QGaussianMoments

/-- The value of an integer polynomial at `q ∈ K`. -/
noncomputable def evalAt {K : Type*} [CommRing K] (q : K) (p : ℤ[X]) : K :=
  p.eval₂ (Int.castRingHom K) q

/-- The normalised `2k`-th moment `ω(S_n^{2k}) / n^k` of a sum sequence under a
state. -/
noncomputable def evenMoment {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (state : A →ₗ[K] K) (sum : ℕ → A) (k n : ℕ) : K :=
  state (sum n ^ (2 * k)) / (n : K) ^ k

section OrderedClt

variable (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  (A : Type*) [Ring A] [Algebra K A]

/-- **Conditional q-CLT, cut form.** Under a tracial normalised state, the
normalised even moments of the sum sequence converge, as located cuts in `K`,
to `v ^ k` times the `2k`-th q-Gaussian moment at `q`. -/
class QCltCut (q : K) where
  /-- The state (intended: the Markov trace `tr_M`). -/
  state : A →ₗ[K] K
  /-- Normalised: `ω(1) = 1`. -/
  state_one : state 1 = 1
  /-- Tracial: `ω(ab) = ω(ba)`, as `tr_M` is. -/
  state_comm : ∀ a b : A, state (a * b) = state (b * a)
  /-- The sum sequence (intended: the centred generator sum). -/
  sum : ℕ → A
  /-- Limit variance. -/
  variance : K
  variance_ne_zero : variance ≠ 0
  /-- Even-moment convergence to the pinned ℤ[q] limit. -/
  evenMomentConverges : ∀ k : ℕ,
    ConvergesTo (evenMoment state sum k) (variance ^ k * evalAt q (qGaussMoment (2 * k)))

/-- **Classical CLT** for a state: the `q = 1` member of the class. Its limit
moments are `v^k (2k-1)!!`. -/
abbrev ClassicalClt := QCltCut K A (1 : K)

variable {K A} {q : K}

/-- The limit of each even-moment sequence is unique. -/
theorem QCltCut.limit_eq [h : QCltCut K A q] (k : ℕ) {L : K}
    (hL : ConvergesTo (evenMoment h.state h.sum k) L) :
    L = h.variance ^ k * evalAt q (qGaussMoment (2 * k)) :=
  hL.unique (h.evenMomentConverges k)

/-- The normalised second moment converges to the variance. -/
theorem QCltCut.second_moment_converges [h : QCltCut K A q] :
    ConvergesTo (evenMoment h.state h.sum 1) h.variance := by
  have := h.evenMomentConverges 1
  rwa [show 2 * 1 = 2 by rfl, qGaussMoment_two, evalAt, eval₂_one, pow_one, mul_one]
    at this

/-- The normalised fourth moment converges to `v² (2 + q)`. -/
theorem QCltCut.fourth_moment_converges [h : QCltCut K A q] :
    ConvergesTo (evenMoment h.state h.sum 2) (h.variance ^ 2 * (2 + q)) := by
  have := h.evenMomentConverges 2
  rw [show 2 * 2 = 4 by rfl, qGaussMoment_four, evalAt] at this
  simpa using this

/-- **The q-pin fails off `q = 1`.** If the normalised fourth moment converges to
the classical Gaussian value `3 v²`, then `q = 1`. -/
theorem QCltCut.q_eq_one_of_fourth_limit [h : QCltCut K A q]
    (h4 : ConvergesTo (evenMoment h.state h.sum 2) (3 * h.variance ^ 2)) : q = 1 := by
  have e := h4.unique h.fourth_moment_converges
  have hv : h.variance ^ 2 ≠ 0 := pow_ne_zero 2 h.variance_ne_zero
  have : h.variance ^ 2 * (q - 1) = 0 := by linear_combination -e
  rcases mul_eq_zero.1 this with h0 | h0
  · exact absurd h0 hv
  · linear_combination h0

/-- Contrapositive: at `q ≠ 1` a state whose fourth moment has the classical
limit admits no instance of the class. -/
theorem not_qCltCut_of_classical_fourth (hq : q ≠ 1) (state : A →ₗ[K] K)
    (sum : ℕ → A) (v : K)
    (h4 : ConvergesTo (evenMoment state sum 2) (3 * v ^ 2)) :
    ¬ ∃ h : QCltCut K A q, h.state = state ∧ h.sum = sum ∧ h.variance = v := by
  rintro ⟨h, rfl, rfl, rfl⟩
  exact hq (h.q_eq_one_of_fourth_limit h4)

/-- In the classical class the fourth moment converges to `3 v²`. -/
theorem ClassicalClt.fourth_moment_converges [h : ClassicalClt K A] :
    ConvergesTo (evenMoment h.state h.sum 2) (3 * h.variance ^ 2) := by
  have := QCltCut.fourth_moment_converges (h := h)
  convert this using 1
  ring

end OrderedClt

end QOU.Observations.QCltCut
