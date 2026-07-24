import QOU.MathlibExt.TraceNilpotent
import Mathlib.RingTheory.Artinian.Ring
import Mathlib.RingTheory.Artinian.Module
import Mathlib.RingTheory.Jacobson.Ideal

/-!
# QOU.MathlibExt.TraceFormSemisimple — the abstract semisimplicity theorem

Brick B3d (epic `qou-hnhg`, track 3): the keystone of Wenzl's
semisimplicity criterion, as a general Mathlib statement.

> **Theorem.**  A finite-dimensional algebra `A` over a field `K` whose
> **regular trace form** `regTraceForm K A x y = trace(L_{xy})` is
> nondegenerate is a semisimple ring.

Proof (assembled from the `TraceNilpotent` core):

1. `A` is Artinian (finite-dimensional over a field), so its Jacobson
   radical `Ring.jacobson A = Ideal.jacobson ⊥` is a **nilpotent** ideal
   (`IsArtinianRing.isNilpotent_jacobson_bot`).
2. For `x` in that radical and any `y`, `y * x` lies in the radical (a
   *left* ideal), hence is nilpotent, so
   `regTraceForm K A y x = trace(L_{yx}) = 0`
   (`regTraceForm_eq_zero_of_mul_isNilpotent`).  By trace cyclicity
   `regTraceForm K A x y = regTraceForm K A y x = 0` — note we never
   need the radical to be two-sided.
3. Nondegeneracy forces `x = 0`, so `Ring.jacobson A = ⊥`, i.e. `A` is
   semisimple (`isSemisimpleRing_iff_jacobson`).

This discharges the *abstract* half of the criterion.  Instantiating it
at the Iwahori–Hecke algebra with its Markov trace, and identifying
nondegeneracy with `[n]_q! ≠ 0` (bricks `qou-t2ot`/`qou-8irr`), turns
the cited `WenzlCriterion` class into a theorem.
-/

namespace QOU.MathlibExt

open Algebra

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]

/-- **The regular trace form is symmetric/cyclic (sorry-free).**
    `B(x, y) = trace(L_x L_y) = trace(L_y L_x) = B(y, x)`. -/
theorem regTraceForm_comm (x y : A) :
    regTraceForm K A x y = regTraceForm K A y x := by
  unfold regTraceForm
  rw [map_mul (lmul K A) x y, map_mul (lmul K A) y x]
  exact LinearMap.trace_mul_comm K (lmul K A x) (lmul K A y)

/-- **Abstract semisimplicity from a nondegenerate regular trace form
    (sorry-free).**  A finite-dimensional `K`-algebra whose regular trace
    form is nondegenerate is a semisimple ring.  This is the general
    engine behind Wenzl's / Geck–Pfeiffer's criterion. -/
theorem isSemisimpleRing_of_regTraceForm_nondegenerate
    (h : ∀ x : A, (∀ y : A, regTraceForm K A x y = 0) → x = 0) :
    IsSemisimpleRing A := by
  -- A finite-dimensional algebra over a field is an Artinian ring.
  haveI : IsArtinianRing A := IsArtinianRing.of_finite K A
  rw [IsArtinianRing.isSemisimpleRing_iff_jacobson, eq_bot_iff]
  -- The Jacobson radical is nilpotent (A is Artinian).
  obtain ⟨n, hn⟩ :
      IsNilpotent (Ring.jacobson A) :=
    Ideal.jacobson_bot (R := A) ▸ IsArtinianRing.isNilpotent_jacobson_bot
  intro x hx
  rw [Ideal.mem_bot]
  apply h x
  intro y
  -- Move to `y * x`, which lies in the (left ideal) radical.
  rw [regTraceForm_comm]
  have hyx : y * x ∈ Ring.jacobson A := Ideal.mul_mem_left _ y hx
  -- Every element of the nilpotent radical is nilpotent.
  have hnil : IsNilpotent (y * x) := by
    refine ⟨n, ?_⟩
    have hmem : (y * x) ^ n ∈ (Ring.jacobson A) ^ n := Ideal.pow_mem_pow hyx n
    rw [hn] at hmem
    exact Ideal.mem_bot.mp hmem
  exact regTraceForm_eq_zero_of_mul_isNilpotent hnil

end QOU.MathlibExt
