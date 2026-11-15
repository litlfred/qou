import QOU.Information.SkeinObservationBridge
import Mathlib.Algebra.Polynomial.Eval.Degree

/-!
# QOU.Information.SkeinNPEncoding — the NP → Jones (Markov-trace) encoding

The **hardness / reduction leg** of the Skein-observation bridge
(`SkeinObservationBridge`). That file supplied the *lower-bound* side —
the `3^c` resolution horizon (`not_polyObservable_of_horizon_cost`) and
the residue obstruction. This file supplies the complementary
**encoding** side: a polynomial-size many-one reduction of a decision
problem *into* the skein (Markov-trace) observation, so the observation
is **at least as hard as** the encoded language. When that language is
NP-complete, the skein observation is NP-hard — the QOU-internal shadow
of the classical fact that evaluating the Jones polynomial / Markov
trace is `#P`-hard (Jaeger–Vertigan–Welsh).

Contents (all sorry-free over the abstract `SkeinObservationSystem`):

* `NPSkeinReduction` — a poly-size reduction: an encoding `enc : I → S`
  of instances as skein words, a `Polynomial ℕ` size budget `encBudget`
  with `len (enc i) ≤ encBudget (size i)`, and correctness
  `accepts i ↔ HaltsObserved (enc i)`.
* `eval_mono` — `Polynomial ℕ` evaluation is monotone (nonneg coeffs).
* `decisionBudget` — **poly-time transfer**: if the encoding's image is
  poly-observable under a single `Polynomial ℕ` budget `obsBudget`, then
  every accepted instance is decided within the **genuine polynomial**
  `obsBudget.comp encBudget` — poly∘poly is poly. A poly-observable
  skein observation collapses the encoded language into P.
* `not_uniform_polyObservable_of_superpoly` — the contrapositive:
  a super-polynomial decision lower bound on the encoded language
  transfers to the skein observation (it is not poly-observable). The
  honest shadow of "the skein / Markov-trace observation is NP-hard".
* `accepts_of_observed` — soundness of the observation as an acceptor,
  from the reduction's `correct` field.

**Honesty (STRICT).** Nothing here proves P ≠ NP or constructs a
concrete NP-complete braid encoding. The existence of the encoding for a
specific NP-complete problem is carried as the structure's *fields* (an
honest open input); what is proved is that any such reduction *transfers
polynomiality both ways*. Nothing is wired to production. This composes
with — does not replace — `PNeqNpEquivalence.JonesComplexityCitations`
(the `#P` counting inclusion) and the instance-free `QouPNeqNp` carrier.

-- Ref: [leitner2026] information-theory/skein-turing-machine,
   information-theory/p-vs-np-boundary
-/

namespace QOU.Information

open SkeinObservationSystem Polynomial

variable {S V : Type*}

/-- A **polynomial-size many-one reduction of a decision problem into the
    skein (Markov-trace) observation** of `sys`. Each instance `i : I` of
    size `size i` is encoded as a skein word `enc i` whose observation
    decides membership, at a skein length polynomial in the instance size.
    This is the NP→Jones encoding: it witnesses that the skein observation
    is at least as hard as `accepts`. -/
structure NPSkeinReduction (sys : SkeinObservationSystem S V)
    {I : Type*} (size : I → ℕ) (accepts : I → Prop) where
  /-- Encoding of instances as skein words. -/
  enc : I → S
  /-- The polynomial size budget of the encoding. -/
  encBudget : Polynomial ℕ
  /-- The encoding is polynomial-size in the instance. -/
  enc_len_le : ∀ i, sys.len (enc i) ≤ encBudget.eval (size i)
  /-- Correctness: the instance is accepted iff the encoded word is
      observed-halting (its Markov trace matches the normal form's). -/
  correct : ∀ i, accepts i ↔ sys.HaltsObserved (enc i)

namespace NPSkeinReduction

variable {sys : SkeinObservationSystem S V} {I : Type*}
  {size : I → ℕ} {accepts : I → Prop}

/-- `Polynomial ℕ` evaluation is monotone in its argument — all
    coefficients are `≥ 0`, so a larger input never shrinks the value. -/
lemma eval_mono (q : Polynomial ℕ) : Monotone (fun n => q.eval n) := by
  intro a b hab
  simp only
  rw [eval_eq_sum_range, eval_eq_sum_range]
  refine Finset.sum_le_sum fun i _ => ?_
  gcongr

/-- **Poly-time transfer (completeness within a polynomial budget).** If
    every accepted instance's encoding is poly-observable under a single
    `Polynomial ℕ` budget `obsBudget` (the "P side" on the encoding's
    image), then each accepted instance is decided by the observation
    within the **genuine polynomial** `obsBudget.comp encBudget` in the
    instance size — poly ∘ poly is poly. A poly-observable skein
    observation collapses the encoded NP language into P. -/
theorem decisionBudget (red : NPSkeinReduction sys size accepts)
    (obsBudget : Polynomial ℕ)
    (hobs : ∀ i, accepts i → sys.PolyObservable (obsBudget.eval ·) (red.enc i)) :
    ∀ i, accepts i → ∃ k ≤ (obsBudget.comp red.encBudget).eval (size i),
      sys.obs (sys.step^[k] (red.enc i)) = sys.obs sys.normalForm := by
  intro i hi
  obtain ⟨k, hk, heq⟩ := hobs i hi
  refine ⟨k, ?_, heq⟩
  rw [eval_comp]
  exact hk.trans (eval_mono obsBudget (red.enc_len_le i))

/-- **NP-hardness lower bound transfers to the skein observation.** If the
    encoded language admits no polynomial decision budget — for every
    candidate polynomial budget some accepted instance escapes it (its
    super-polynomial lower bound) — then the skein observation is not
    poly-observable under any single polynomial budget on the encoding's
    image. The honest QOU-internal shadow of "the skein / Markov-trace
    observation is NP-hard". -/
theorem not_uniform_polyObservable_of_superpoly
    (red : NPSkeinReduction sys size accepts)
    (hhard : ∀ decBudget : Polynomial ℕ, ∃ i, accepts i ∧
        ∀ k ≤ decBudget.eval (size i),
          sys.obs (sys.step^[k] (red.enc i)) ≠ sys.obs sys.normalForm) :
    ∀ obsBudget : Polynomial ℕ, ∃ i, accepts i ∧
        ¬ sys.PolyObservable (obsBudget.eval ·) (red.enc i) := by
  intro obsBudget
  obtain ⟨i, hi, hno⟩ := hhard (obsBudget.comp red.encBudget)
  refine ⟨i, hi, fun hpoly => ?_⟩
  obtain ⟨k, hk, heq⟩ := hpoly
  have hkb : k ≤ (obsBudget.comp red.encBudget).eval (size i) := by
    rw [eval_comp]
    exact hk.trans (eval_mono obsBudget (red.enc_len_le i))
  exact hno k hkb heq

/-- **Soundness of the observation as an acceptor.** From the reduction's
    correctness, an observed-halting encoding forces acceptance — so a
    matching Markov-trace observation is a *sound* accept certificate. -/
theorem accepts_of_observed (red : NPSkeinReduction sys size accepts)
    (i : I) (h : sys.HaltsObserved (red.enc i)) : accepts i :=
  (red.correct i).mpr h

/-- **Completeness of the observation as an acceptor.** Accepted instances
    are observed-halting — the converse direction of `correct`. -/
theorem observed_of_accepts (red : NPSkeinReduction sys size accepts)
    (i : I) (h : accepts i) : sys.HaltsObserved (red.enc i) :=
  (red.correct i).mp h

end NPSkeinReduction

end QOU.Information
