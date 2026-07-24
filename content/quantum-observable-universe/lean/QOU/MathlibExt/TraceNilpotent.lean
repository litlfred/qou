import Mathlib.RingTheory.Trace.Basic
import Mathlib.LinearAlgebra.Trace
import Mathlib.Tactic

/-!
# QOU.MathlibExt.TraceNilpotent — the trace form kills nilpotents

Reusable building blocks for the abstract symmetric-algebra
semisimplicity theorem (track 3 of the Hecke-semisimplicity attack,
epic `qou-hnhg`; this file is bricks `qou-ubz8` (B3c) core lemmas).

The keystone of Wenzl's criterion is: *a finite-dimensional algebra
whose regular trace form is nondegenerate is semisimple.*  Its
mathematical heart is that the trace form annihilates the (nilpotent)
Jacobson radical, which rests on two facts proved here, sorry-free,
over any field.

**Base-ring note.**  Mathlib's `Algebra.trace` / `Algebra.traceForm`
are **commutative-only** (`CommRing S`), so they do *not* apply to the
noncommutative Hecke algebra.  We therefore use the **regular
representation trace** `regTrace x = LinearMap.trace K A (lmul K A x)`
directly (the trace of left-multiplication as a `K`-endomorphism),
which is defined for any finite-dimensional algebra, commutative or
not.  This is exactly the object Wenzl's / Geck–Pfeiffer's criterion
uses.

The remaining assembly — threading these through the *two-sided*
Jacobson ideal (`Ring.jacobson` / `TwoSidedIdeal`) and
`isSemisimpleRing_iff_jacobson` — is the next brick (`qou-u181`, B3d);
the noncommutative ideal API is the identified hard joint.
-/

namespace QOU.MathlibExt

open Algebra

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- **Left multiplication by a nilpotent element is nilpotent
    (sorry-free).**  `lmul K A` is an algebra homomorphism into the
    endomorphism ring, so it carries `xⁿ = 0` to `(lmul x)ⁿ = 0`. -/
theorem isNilpotent_lmul_of_isNilpotent {x : A} (hx : IsNilpotent x) :
    IsNilpotent (lmul K A x) :=
  hx.map (lmul K A)

variable (K A) in
/-- **The regular trace form** `B(x, y) = trace(L_{xy})`, the trace of
    left-multiplication by `x * y` as a `K`-linear endomorphism of `A`.
    Defined for any (possibly noncommutative) algebra — the
    noncommutative analogue of `Algebra.traceForm`. -/
noncomputable def regTraceForm (x y : A) : K :=
  LinearMap.trace K A (lmul K A (x * y))

variable [FiniteDimensional K A]

/-- **The regular trace of a nilpotent element vanishes (sorry-free).**
    A nilpotent `z` has nilpotent `lmul z`, whose `LinearMap.trace` is a
    nilpotent element of the field `K`, hence `0` (a field is reduced). -/
theorem trace_lmul_eq_zero_of_isNilpotent {z : A} (hz : IsNilpotent z) :
    LinearMap.trace K A (lmul K A z) = 0 :=
  (LinearMap.isNilpotent_trace_of_isNilpotent
    (isNilpotent_lmul_of_isNilpotent hz)).eq_zero

/-- **The regular trace form vanishes whenever the product is nilpotent
    (sorry-free).**  If `x * y` is nilpotent then `regTraceForm K A x y = 0`.
    For an `x` in a nil two-sided ideal, `x * y` is always nilpotent,
    giving the radical-annihilation step of the semisimplicity theorem
    (the two-sided-ideal plumbing is brick B3d, `qou-u181`). -/
theorem regTraceForm_eq_zero_of_mul_isNilpotent {x y : A}
    (hxy : IsNilpotent (x * y)) : regTraceForm K A x y = 0 :=
  trace_lmul_eq_zero_of_isNilpotent hxy

end QOU.MathlibExt
