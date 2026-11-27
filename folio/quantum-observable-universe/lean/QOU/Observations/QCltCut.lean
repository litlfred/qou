import QOU.Core.CutLimit
import QOU.Core.QGaussianMoments

/-!
# QOU.Observations.QCltCut — the q-CLT as convergence of located cuts to ℤ[q] moments

Bean `qou-e1uf` (item 6 of epic `qou-dk7p`), strangler step 2. This is the
algebraic restatement of the conditional q-CLT for Hecke transfer matrices.
The older class `QCltNonCommutative` stated moment convergence with
`Filter.Tendsto` into a topological field and left both the limit moments and a
characteristic-function limit as free data. Here:

* the limit of the `k`-th moment is **pinned**: it is the q-Gaussian moment
  `qGaussMoment k ∈ ℤ[q]` (weighted Dyck paths, `QOU.Core.QGaussianMoments`)
  evaluated at the deformation parameter `q`. That makes the class refutable
  by a single moment;
* convergence is `QOU.Core.CutLimit.ConvergesTo`, a located cut in an ordered
  field, with no topology and no ε–δ;
* the characteristic-function clause is dropped. It is analytic (`exp_q` of an
  operator), and for a moment-determinate limit it adds nothing to the
  moments. If it is needed, it belongs behind the transcendental boundary.

The old class now lives in `QOU.Transcendental.QCltNonCommutative`, which proves
that its instances with the pinned limit give instances of this class.

`@conjecture: primary`. It has no instance; it is a hypothesis to be discharged
by the moment computation, not an axiom. No empirical value enters this file.
-/

namespace QOU.Observations.QCltCut

open Polynomial QOU.Core.CutLimit QOU.Core.QGaussianMoments

/-- The value of an integer polynomial at `q ∈ K`. -/
noncomputable def evalAt {K : Type*} [Field K] (q : K) (p : ℤ[X]) : K :=
  p.eval₂ (Int.castRingHom K) q

/-- **Conditional q-CLT, cut form.** For each degree `k`, the `k`-th moment of
the rescaled centred Hecke generator sum under `tr_M` converges, as a located
cut in `K`, to the `k`-th q-Gaussian moment at `q`. -/
class QCltCut (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q : K) where
  /-- `momentSequence n k`: the `k`-th moment at the `n`-th stage. -/
  momentSequence : ℕ → ℕ → K
  /-- Moment convergence to the pinned ℤ[q] limit. -/
  momentConverges :
    ∀ k : ℕ, ConvergesTo (fun n => momentSequence n k) (evalAt q (qGaussMoment k))

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K}

/-- The limit of each moment sequence is unique: any other limit equals the
q-Gaussian moment. -/
theorem QCltCut.limit_eq [h : QCltCut K q] (k : ℕ) {L : K}
    (hL : ConvergesTo (fun n => h.momentSequence n k) L) :
    L = evalAt q (qGaussMoment k) :=
  hL.unique (h.momentConverges k)

/-- Odd moments converge to `0`. -/
theorem QCltCut.odd_moment_converges_zero [h : QCltCut K q] (k : ℕ) :
    ConvergesTo (fun n => h.momentSequence n (2 * k + 1)) 0 := by
  have := h.momentConverges (2 * k + 1)
  rwa [qGaussMoment_odd, evalAt, eval₂_zero] at this

/-- The fourth moment converges to `2 + q`. -/
theorem QCltCut.fourth_moment_converges [h : QCltCut K q] :
    ConvergesTo (fun n => h.momentSequence n 4) (2 + q) := by
  have := h.momentConverges 4
  rw [qGaussMoment_four, evalAt] at this
  simpa using this

end QOU.Observations.QCltCut
