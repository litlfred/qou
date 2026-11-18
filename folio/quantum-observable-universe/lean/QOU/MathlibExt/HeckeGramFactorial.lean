import QOU.MathlibExt.RegTraceGram
import QOU.MathlibExt.QIntegerFactorial

/-!
# QOU.MathlibExt.HeckeGramFactorial — the end-to-end Gram=[n]_q! hook

Brick `qou-twwf` interface (epic `qou-yi7h`).  Closes the gap between the
**abstract** Gram-determinant criterion (`RegTraceGram`) and the **quantum
arithmetic** (`QIntegerFactorial`) into a single consumable theorem:

> **Hook.**  Let `A` be a finite-dimensional `K`-algebra, `b` a finite
> basis, `q ≠ 1` Wenzl-generic, and `c` a unit.  *If* the regular-trace
> Gram determinant in `b` equals `c · [n]_q!`, then `A` is semisimple.

This is the exact shape a `T_w`-basis computation for `H_n(q)` plugs
into: supply `(b, c, proof det = c·[n]_q!)` — the Schur/Poincaré identity
`det(Gram) = [n]_q!` up to a unit (bricks `qou-lrz1` + `qou-twwf`) — and
semisimplicity follows with **no further Hecke input**.  Everything on the
Lean side of that identity is now proven sorry-free:

* `det(Gram) ≠ 0 ⇒ semisimple`   — `isSemisimpleRing_of_regTraceGram_det_ne_zero`
  (via `nondegenerate_iff_det_ne_zero` + the B3d keystone);
* `[n]_q! ≠ 0 ⇔ q` generic       — `qFactorial_ne_zero_iff` (B1);
* the `n = 2` determinant value   — `QOU.Hecke.H2CompanionRep.h2GramFromRep_det`
  (`det = [2]_q²`, computed from the regular representation).

The one remaining open input is the **general** determinant value in the
`n!`-dimensional `T_w` basis — the deep classical Schur-element product
formula — which no fabricated instance may stand in for.
-/

namespace QOU.MathlibExt

open Algebra

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]

/-- **`det(Gram) = c·[n]_q!` (unit `c`) + generic ⇒ semisimple
    (sorry-free).**  The final consumable form of the Wenzl criterion.
    A `T_w`-basis Gram computation for `H_n(q)` supplies the basis `b`, a
    unit `c`, and a proof that the regular-trace Gram determinant in `b`
    equals `c · [n]_q!`; then at any Wenzl-generic `q` the algebra is
    semisimple.  Composes `isSemisimpleRing_of_regTraceGram_det_ne_zero`
    (det ≠ 0 ⇒ semisimple) with `qFactorial_ne_zero_iff` (generic ⇒
    `[n]_q! ≠ 0`) and `mul_ne_zero`. -/
theorem isSemisimpleRing_of_gram_det_eq_qFactorial
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A)
    {q c : K} (hq : q ≠ 1) (hc : c ≠ 0) {n : ℕ} (hgen : QGeneric q n)
    (hdet : (BilinForm.toMatrix b (regTraceBilin K A)).det = c * qFactorial q n) :
    IsSemisimpleRing A :=
  isSemisimpleRing_of_regTraceGram_det_ne_zero b
    (by rw [hdet]; exact mul_ne_zero hc ((qFactorial_ne_zero_iff hq n).mpr hgen))

/-- **The exact-value case `det(Gram) = [n]_q!` ⇒ semisimple
    (sorry-free).**  The unit specialises to `c = 1`: if the Gram
    determinant is *exactly* the quantum factorial, a Wenzl-generic `q`
    makes `A` semisimple. -/
theorem isSemisimpleRing_of_gram_det_eq_qFactorial_one
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A)
    {q : K} (hq : q ≠ 1) {n : ℕ} (hgen : QGeneric q n)
    (hdet : (BilinForm.toMatrix b (regTraceBilin K A)).det = qFactorial q n) :
    IsSemisimpleRing A :=
  isSemisimpleRing_of_gram_det_eq_qFactorial b hq one_ne_zero hgen
    (by rw [hdet, one_mul])

/-- **The substrate specialisation (sorry-free).**  For the real
    substrate `q > 1`, genericity is automatic, so a real algebra whose
    regular-trace Gram determinant is `c · [n]_q!` (unit `c`) is
    semisimple.  This is the shape in which the substrate `q₀ ≈ 1.10998`
    discharges the semisimplicity leg of the `P ≠ NP`-in-QOU counting
    argument, once the `T_w`-basis determinant is supplied. -/
theorem isSemisimpleRing_of_gram_det_eq_qFactorial_one_lt
    {B : Type*} [Ring B] [Algebra ℝ B] [FiniteDimensional ℝ B]
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι ℝ B)
    {q c : ℝ} (hq : 1 < q) (hc : c ≠ 0) {n : ℕ}
    (hdet : (BilinForm.toMatrix b (regTraceBilin ℝ B)).det = c * qFactorial q n) :
    IsSemisimpleRing B :=
  isSemisimpleRing_of_gram_det_eq_qFactorial b hq.ne' hc
    (qGeneric_of_one_lt hq n) hdet

omit [FiniteDimensional K A] in
/-- **Non-vanishing of the regular-trace Gram determinant at Wenzl-generic `q`.**
    If the regular-trace Gram determinant in basis `b` equals `c * qFactorial q n`
    with `q ≠ 1`, `c ≠ 0`, and `QGeneric q n`, then the Gram determinant is non-zero. -/
theorem regTraceGram_det_ne_zero_of_eq_qFactorial
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A)
    {q c : K} (hq : q ≠ 1) (hc : c ≠ 0) {n : ℕ} (hgen : QGeneric q n)
    (hdet : (BilinForm.toMatrix b (regTraceBilin K A)).det = c * qFactorial q n) :
    (BilinForm.toMatrix b (regTraceBilin K A)).det ≠ 0 := by
  rw [hdet]
  exact mul_ne_zero hc ((qFactorial_ne_zero_iff hq n).mpr hgen)

/-- **Exact-factorial substrate specialisation (`c = 1`, `q > 1`).**
    For any real finite-dimensional algebra `B` with basis `b` whose regular-trace
    Gram determinant equals `qFactorial q n` at `1 < q`, `B` is semisimple. -/
theorem isSemisimpleRing_of_gram_det_eq_qFactorial_one_lt_exact
    {B : Type*} [Ring B] [Algebra ℝ B] [FiniteDimensional ℝ B]
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι ℝ B)
    {q : ℝ} (hq : 1 < q) {n : ℕ}
    (hdet : (BilinForm.toMatrix b (regTraceBilin ℝ B)).det = qFactorial q n) :
    IsSemisimpleRing B :=
  isSemisimpleRing_of_gram_det_eq_qFactorial_one_lt b hq one_ne_zero
    (by rw [hdet, one_mul])

omit [FiniteDimensional K A] in
/-- **Failure-locus detection from Gram degeneracy.**
    If the regular-trace Gram determinant equals `c * qFactorial q n` (`q ≠ 1`, `c ≠ 0`)
    and vanishes, then `q` is not Wenzl-generic at level `n`. -/
theorem not_qGeneric_of_gram_det_eq_zero
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A)
    {q c : K} (hq : q ≠ 1) (hc : c ≠ 0) {n : ℕ}
    (hdet : (BilinForm.toMatrix b (regTraceBilin K A)).det = c * qFactorial q n)
    (hzero : (BilinForm.toMatrix b (regTraceBilin K A)).det = 0) :
    ¬ QGeneric q n := by
  intro hgen
  exact regTraceGram_det_ne_zero_of_eq_qFactorial b hq hc hgen hdet hzero

end QOU.MathlibExt
