import QOU.MathlibExt.TraceFormSemisimple
import QOU.MathlibExt.QIntegerFactorial

/-!
# QOU.MathlibExt.HeckeGenericSemisimple — the Wenzl-criterion bridge

The composition brick (epic `qou-hnhg`) that joins the abstract
semisimplicity engine (track 3, `TraceFormSemisimple`) to the quantum
arithmetic (track 5/B1, `QIntegerFactorial`).  It reduces the *entire*
remaining Hecke problem to a **single Gram-determinant identity**:

> **Bridge.**  Let `A` be a finite-dimensional `K`-algebra and `q ≠ 1`.
> *If* the regular trace form of `A` is nondegenerate exactly when the
> quantum factorial `[n]_q! ≠ 0`, then genericity of `q`
> (`QGeneric q n`) implies `A` is semisimple.

Applied to `A = H_n(q)` with its Markov trace, the hypothesis `hgram`
is exactly the Schur-element / Gram-determinant computation
`det (Gram) = [n]_q!` (up to a unit) — the one thing the concrete
Iwahori–Hecke construction (track 2, beans `qou-w8hn` … `qou-8irr`)
must still supply.  Everything else — genericity ⇔ `[n]_q! ≠ 0` (B1)
and nondegenerate-trace-form ⇒ semisimple (B3d) — is already proven
sorry-free.  This is the crispest possible statement of what
"discharge `WenzlCriterion`" now requires.
-/

namespace QOU.MathlibExt

open Algebra

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]

/-- **Genericity ⇒ semisimple, modulo the Gram–factorial identity
    (sorry-free).**  Composes B1 (`qFactorial_ne_zero_iff`) with the
    abstract keystone B3d (`isSemisimpleRing_of_regTraceForm_nondegenerate`).
    The hypothesis `hgram` is the Schur-element / Gram-determinant
    content that a concrete `H_n(q)` supplies; given it, a Wenzl-generic
    parameter makes the algebra semisimple. -/
theorem isSemisimpleRing_of_qGeneric {q : K} (hq : q ≠ 1) {n : ℕ}
    (hgram : (∀ x : A, (∀ y : A, regTraceForm K A x y = 0) → x = 0)
      ↔ qFactorial q n ≠ 0)
    (hgen : QGeneric q n) : IsSemisimpleRing A :=
  isSemisimpleRing_of_regTraceForm_nondegenerate
    (hgram.mpr ((qFactorial_ne_zero_iff hq n).mpr hgen))

/-- **The substrate specialisation (sorry-free).**  For the real
    substrate `q > 1`, genericity is automatic (`qGeneric_of_one_lt`),
    so — modulo the same Gram–factorial identity — `A` is semisimple at
    every rank.  This is the shape in which the substrate discharges the
    semisimplicity leg of the `P ≠ NP`-in-QOU counting argument. -/
theorem isSemisimpleRing_of_one_lt {q : ℝ} {B : Type*} [Ring B]
    [Algebra ℝ B] [FiniteDimensional ℝ B] (hq : 1 < q) {n : ℕ}
    (hgram : (∀ x : B, (∀ y : B, regTraceForm ℝ B x y = 0) → x = 0)
      ↔ qFactorial q n ≠ 0) :
    IsSemisimpleRing B :=
  isSemisimpleRing_of_qGeneric hq.ne' hgram (qGeneric_of_one_lt hq n)

end QOU.MathlibExt
