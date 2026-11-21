import Mathlib.Algebra.DualNumber
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.RingTheory.Artinian.Ring
import Mathlib.RingTheory.Jacobson.Ideal
import QOU.QBeta.TemperleyLiebTower

/-!
# QOU.QBeta.TraceNondegeneracyInsufficient — nondegeneracy alone is not enough

Brick 4 of `qou-s7z2`, and it is a **negative** one. It was reached by trying to
assemble bricks 2 and 3 into a `WenzlTowerStep` instance at the Markov trace,
and finding that the assembly cannot close — for a reason worth recording rather
than working around.

## The shape of the problem

`WenzlTowerStep.semisimple_ascend` reads

    IsSemisimpleRing Hn →
    (∀ y ≠ 0, ∃ z, trn1 (y * z) ≠ 0) →
    IsSemisimpleRing Hn1

Brick 1 (`MarkovTraceQuotient.quot_pairing_nondegenerate`) makes the **second
hypothesis free** on the quotient: after quotienting by the radical, every
nonzero class is separated by the pairing, by construction. So one might hope
the class becomes easy over `TL_n`.

It does not, and the reason is not a missing lemma. **Nondegeneracy of a trace
does not imply semisimplicity.** The corpus's semisimplicity engine
(`MathlibExt.isSemisimpleRing_of_regTraceForm_nondegenerate`) is about the
**regular trace form** `x, y ↦ trace(L_{xy})` — the trace of left
multiplication, an intrinsic invariant — not about an arbitrary linear
functional that happens to pair non-degenerately. Those are different
hypotheses, and only the former is strong enough.

## The counterexample

The dual numbers `ℚ[ε]/(ε²)` carry the functional `τ(a + bε) = b`. It is linear,
cyclic (the ring is commutative), and **non-degenerate**: given `a + bε ≠ 0`,
pair with `ε` if `a ≠ 0`, and with `1` if `a = 0`. Yet `ℚ[ε]` is **not**
semisimple — `ε` is a nonzero nilpotent, so the ring is not reduced.

So an instance of `WenzlTowerStep` at a general trace cannot be obtained from
its own nondegeneracy hypothesis. Something must supply the *regular* trace
form's nondegeneracy, and in the Hecke setting that is exactly
`HeckeGramFactorial`'s open input — the general `T_w`-basis Gram determinant,
the classical Schur-element product formula. `n = 2` is done; no fabricated
instance may stand in for the general value.

## 🛑 The paragraph above is SUPERSEDED in its second half — corrected 2026-09-27

The counterexample, and the first sentence it supports, **stand untouched**:
nondegeneracy of a trace does not imply semisimplicity, and the class's own
hypothesis is not what discharges it. That is this file's result and it is
unaffected.

What is stale is the *next* step — "something must supply the regular trace
form's nondegeneracy, and that is the Gram determinant". **For
`IsSemisimpleRing` at the Hecke carrier, nothing need supply it.**
`QOU.SchurWeyl.isSemisimpleRing_hecke_generic` gives `IsSemisimpleRing (Hecke K q
q⁻¹ n)` at **every** `n`, over any `CharZero` field, under `q ≠ 0` and
`NotRootOfUnity q` alone. It is sorry-free and routes through `heckeWedderburn`
— a Wedderburn block decomposition — **not** through any trace form and not
through a Gram determinant. Verified rather than read off a docstring: both
declarations check `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.

So the conclusion of `semisimple_ascend` is available outright at that carrier,
which makes an instance there **vacuous** rather than hard —
`QOU.Machinery.HeckeRank.wenzlTowerStep_vacuous_of_isSemisimpleRing` states that
in general, and `WtraceRadicalSemisimple.isSemisimpleRing_traceQuot_of_hecke`
supplies the hypothesis at the `wtrace` quotient.

**The sharper reason not to chase this instance: nothing consumes the class.**
Measured 2026-09-27 over the whole Lean tree — 27 occurrences of
`WenzlTowerStep`, being 1 class definition, 2 discharge targets and 24 prose
mentions, with **zero** instance-hypothesis positions (`grep -rn
'\[WenzlTowerStep'` returns nothing). This file is one of five that name such an
instance as an outstanding blocker; an instance cannot unblock a consumer that
does not exist.

**What this does NOT say.** The Gram determinant may well remain the binding
constraint for other things — in particular for the ideal equality
`⟨U_i U_j U_i − v²·U_i⟩ = rad(tr_M)`, which is the live frontier (beans
`qou-jb7k`, `qou-0cyu`) and is a different question from semisimplicity. The
claim corrected here is only that the Gram determinant is not what stands between
this corpus and `IsSemisimpleRing` of a Hecke algebra. And the genuine ascent
question — does semisimplicity ascend along a nondegenerate Markov trace at a
carrier where the conclusion is *not* already known — is untouched and open
(`qou-s7z2`).

## What this does and does not say

**Scope (b), a structural exclusion**, in the sense of AGENTS.md's refutation
rule: it is not "this route did not work numerically", it is a proved
counterexample to the implication *nondegenerate trace ⇒ semisimple*. Cite it as
such.

It does **not** say `WenzlTowerStep` is wrong, unprovable, or that the TL-quotient
route is dead. It says the class's own nondegeneracy hypothesis is not what
discharges it, so effort aimed at strengthening or re-deriving that hypothesis is
misdirected — the binding constraint is the Gram determinant. Bricks 1–3 are
unaffected and remain what they claim to be.
-/

namespace QOU.QBeta.TraceNondegeneracyInsufficient

open QOU.QBeta.TemperleyLiebTower

/-- The ε-coefficient of a dual number, as a linear functional. -/
noncomputable def epsCoeff : DualNumber ℚ →ₗ[ℚ] ℚ where
  toFun x := TrivSqZeroExt.snd x
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp]
theorem epsCoeff_apply (x : DualNumber ℚ) : epsCoeff x = TrivSqZeroExt.snd x := rfl

/-- **The functional is cyclic** — trivially, the dual numbers commute. -/
theorem epsCoeff_cyclic (x y : DualNumber ℚ) :
    epsCoeff (x * y) = epsCoeff (y * x) := by
  rw [mul_comm]

/-- **The functional is non-degenerate**, in exactly the shape
`WenzlTowerStep.semisimple_ascend` asks for.

Given `x ≠ 0` write `x = a + bε`. If `a ≠ 0`, pairing with `ε` returns `a`; if
`a = 0` then `b ≠ 0`, and pairing with `1` returns `b`. -/
theorem epsCoeff_nondegenerate (x : DualNumber ℚ) (hx : x ≠ 0) :
    ∃ y : DualNumber ℚ, epsCoeff (x * y) ≠ 0 := by
  by_cases ha : TrivSqZeroExt.fst x = 0
  · refine ⟨1, ?_⟩
    rw [mul_one, epsCoeff_apply]
    intro hb
    exact hx (TrivSqZeroExt.ext ha hb)
  · refine ⟨TrivSqZeroExt.inr 1, ?_⟩
    simpa using ha

/-- **But the dual numbers are not semisimple.** `ε` is a nonzero nilpotent, so
the ring is not reduced, and a semisimple ring is. -/
theorem dualNumber_not_isSemisimpleRing : ¬ IsSemisimpleRing (DualNumber ℚ) := by
  intro hss
  haveI := hss
  have hred : IsReduced (DualNumber ℚ) := inferInstance
  have hzero : (TrivSqZeroExt.inr (1 : ℚ) : DualNumber ℚ) = 0 := by
    refine hred.eq_zero _ ⟨2, ?_⟩
    simp [pow_two]
  simpa using congrArg TrivSqZeroExt.snd hzero

/-- **The headline: a non-degenerate cyclic trace does not imply semisimplicity.**

Packaged as the exact conjunction that refutes any attempt to discharge
`WenzlTowerStep`'s conclusion from its own nondegeneracy hypothesis. The witness
is `ℚ[ε]/(ε²)`.

This is why brick 1's `quot_pairing_nondegenerate` — which makes that hypothesis
*free* on the quotient — does not make the class easy: a free hypothesis that
cannot carry the conclusion buys nothing. -/
theorem nondegenerate_cyclic_trace_not_sufficient :
    ∃ (A : Type) (_ : CommRing A) (_ : Algebra ℚ A) (tau : A → ℚ),
      (∀ x y : A, tau (x * y) = tau (y * x)) ∧
      (∀ x : A, x ≠ 0 → ∃ y : A, tau (x * y) ≠ 0) ∧
      ¬ IsSemisimpleRing A :=
  ⟨DualNumber ℚ, inferInstance, inferInstance, fun x => epsCoeff x,
    epsCoeff_cyclic, epsCoeff_nondegenerate, dualNumber_not_isSemisimpleRing⟩

/-- **The radical of this trace is trivial**, so the counterexample is not an
artefact of a degenerate pairing that a quotient would repair.

`ℚ[ε]` *is* its own quotient by the trace radical, and it is still not
semisimple. So passing to `A / rad τ` — bricks 1–3 — cannot by itself rescue the
implication either. -/
theorem traceRadical_epsCoeff_eq_bot :
    traceRadical (fun x : DualNumber ℚ => epsCoeff x) = {0} := by
  ext a
  constructor
  · intro ha
    by_contra hne
    obtain ⟨y, hy⟩ := epsCoeff_nondegenerate a hne
    exact hy (ha y)
  · rintro rfl
    intro b
    simp

end QOU.QBeta.TraceNondegeneracyInsufficient
