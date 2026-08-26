import Mathlib.RingTheory.Artinian.Ring
import Mathlib.RingTheory.Trace.Basic
import Mathlib.RingTheory.Jacobson.Ideal
import Mathlib.LinearAlgebra.Trace

/-!
# A finite-dimensional algebra with nondegenerate trace form is semisimple

The classical criterion, for a **non-commutative** finite-dimensional algebra over
a field. Mathlib does not have it: `Algebra.traceForm_nondegenerate` runs the
other way (*separable ⇒ nondegenerate*) and is stated for field extensions, where
both `K` and `L` are `Field`. Measured against the Mathlib source, bean
`qou-kzjl`; the gap is recorded at `QOU.Machinery.HeckeTower.WenzlTowerStep`,
which is what needs this.

## The argument

Three steps, each a Mathlib citation:

1. `A` finite-dimensional over a field is Artinian, so its Jacobson radical is
   nilpotent (`IsArtinianRing.isNilpotent_jacobson_bot`).
2. Hence every `x` in the radical is nilpotent, and so is `x * y` for any `y`,
   the radical being a two-sided ideal. Left multiplication by a nilpotent
   element is a nilpotent endomorphism, so its trace is nilpotent
   (`LinearMap.isNilpotent_trace_of_isNilpotent`) — and a nilpotent element of a
   field is `0`.
3. So the radical lies in the kernel of the trace form. Nondegeneracy forces it
   to vanish, and `isSemisimpleRing_iff_jacobson` concludes.

## Scope

The nondegeneracy hypothesis is taken in the **left** form — for every `x ≠ 0`
some `y` has `trace (lmul (x * y)) ≠ 0` — because that is the shape the argument
consumes and the shape `WenzlTowerStep` states. No characteristic assumption is
needed: nilpotency alone kills the trace, since a field is reduced.
-/

namespace QOU.MathlibExt

open LinearMap

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]

/-- The trace form of a finite-dimensional algebra, as a function: `x y ↦ tr(L_{xy})`
where `L` is left multiplication. Written out rather than reusing
`Algebra.traceForm`, whose surrounding API is developed for the commutative case. -/
noncomputable def algTrace (x : A) : K :=
  LinearMap.trace K A (LinearMap.mulLeft K x)

omit [FiniteDimensional K A] in
@[simp] theorem algTrace_apply (x : A) :
    algTrace (K := K) x = LinearMap.trace K A (LinearMap.mulLeft K x) := rfl

omit [FiniteDimensional K A] in
/-- **A nilpotent element has vanishing trace.** Left multiplication by a
nilpotent element is a nilpotent endomorphism, whose trace is a nilpotent element
of `K`; a field is reduced, so that trace is `0`. -/
theorem algTrace_eq_zero_of_isNilpotent {x : A} (hx : IsNilpotent x) :
    algTrace (K := K) x = 0 := by
  have hmul : IsNilpotent (LinearMap.mulLeft K x) := by
    obtain ⟨n, hn⟩ := hx
    refine ⟨n, ?_⟩
    ext a
    simp [LinearMap.pow_mulLeft, hn]
  exact IsNilpotent.eq_zero (LinearMap.isNilpotent_trace_of_isNilpotent hmul)

/-- **The criterion.** If the trace form is nondegenerate on the left, the algebra
is semisimple.

`hnd` is stated exactly as `WenzlTowerStep`'s nondegeneracy hypothesis: every
nonzero `x` is detected by some `y`. -/
theorem isSemisimpleRing_of_trace_nondegenerate
    (hnd : ∀ x : A, x ≠ 0 → ∃ y : A, algTrace (K := K) (x * y) ≠ 0) :
    IsSemisimpleRing A := by
  -- `IsArtinianRing.of_finite` is a THEOREM in Mathlib, not an instance, so
  -- synthesis does not find it; supply it by hand.
  haveI : IsArtinianRing A := IsArtinianRing.of_finite K A
  rw [IsArtinianRing.isSemisimpleRing_iff_jacobson]
  by_contra hne
  obtain ⟨x, hxmem, hx0⟩ : ∃ x ∈ Ring.jacobson A, x ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact hne (le_antisymm (fun z hz => hcon z hz) bot_le)
  obtain ⟨y, hy⟩ := hnd x hx0
  refine hy (algTrace_eq_zero_of_isNilpotent ?_)
  -- `x * y` lies in the Jacobson radical, which is nilpotent as an ideal.
  obtain ⟨n, hn⟩ := IsArtinianRing.isNilpotent_jacobson_bot (R := A)
  have hxy : x * y ∈ Ring.jacobson A :=
    Ideal.mul_mem_right _ _ hxmem
  refine ⟨n, ?_⟩
  have : (x * y) ^ n ∈ (Ideal.jacobson (⊥ : Ideal A)) ^ n := by
    rw [Ideal.jacobson_bot]
    exact Ideal.pow_mem_pow hxy n
  rw [hn] at this
  simpa using this

end QOU.MathlibExt
