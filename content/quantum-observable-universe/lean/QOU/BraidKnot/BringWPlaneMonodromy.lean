import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

/-!
# Bring W-plane Gauss–Manin monodromy operator (§(d) sub-lead, numerology-guarded)

The full-Hecke geometric-index program's Bring/Jacobian sub-lead (program §(d), see
`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`): the rank-2 W-plane is the
elliptic curve `E = Bring/S₄` (`Jac(Bring) ≅ E⁴`, #2710), and the depth-2 selection-rule recurrence
kernel `R(x) = x² − τ·x + 1` (#2488, `τ(q₀) ≈ 2.6424`) is conjectured to come from the **Gauss–Manin
monodromy** of `E` along the S³/2I Seifert fibration.

**Numerology guardrail (STRICT).** `τ = 2.6424` is a single number; matching one geometric scalar to
one algebraic scalar is **not** a derivation (the `W_λ` target is a λ-family). So this file
formalizes the monodromy **operator** and the *functional* form of the recurrence kernel — never the
trace value. The genuine structural content is:

> **The recurrence kernel `x² − τ·x + 1` is the Cayley–Hamilton relation of a unimodular 2×2
> monodromy `M`, with `τ = tr M`.** Its monic, unit-constant-term shape is *forced* by `det M = 1`
> (the symplectic structure of `H¹` of an elliptic curve) — not fitted.

`unimodular_two_recurrence` proves this sorry-free. The geometric identification — that `M` is the
*actual* Seifert / Gauss–Manin monodromy of `E = Bring/S₄` with `tr M = τ` — is the open §3b
conjecture (`BringWPlaneMonodromy`), and the falsifiable functional target (reproduce the **whole**
`(n−1,1)` recurrence family, not the one number `τ`) is stated, not closed.

Base ring `ℝ` (the monodromy acts on the real `H¹`); the structural lemma is pure linear algebra.
No fit; `τ` appears only as the symbol `tr M`.
-/

namespace QOU.BraidKnot

open Matrix

/-- **The recurrence kernel is the Cayley–Hamilton relation of a unimodular 2×2 monodromy.**
For any `M ∈ Mat₂(ℝ)` with `det M = 1` (a symplectic / `SL₂` monodromy on the rank-2 W-plane
`H¹(E)`, `E = Bring/S₄`), `M·M = (tr M)·M − I` — i.e. `M` satisfies the depth-2 recurrence kernel
`R(x) = x² − τ·x + 1` with `τ = tr M`. The monic, unit-constant-term form of the kernel (#2488) is
thus **forced** by unimodularity; this is the operator-level (functional) content, **not** the trace
value `τ ≈ 2.6424` (which the numerology guardrail forbids fitting). -/
theorem unimodular_two_recurrence (M : Matrix (Fin 2) (Fin 2) ℝ) (hdet : M.det = 1) :
    M * M = M.trace • M - 1 := by
  have hd : M 0 0 * M 1 1 - M 0 1 * M 1 0 = 1 := by rw [← Matrix.det_fin_two]; exact hdet
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.smul_apply,
      Matrix.sub_apply] <;>
    (first
      | linear_combination hd
      | linear_combination -hd
      | linear_combination (2 : ℝ) * hd
      | linear_combination (-2 : ℝ) * hd
      | nlinarith [hd])

/-- **Bring W-plane Gauss–Manin monodromy** — §3b conjecture class (numerology-guarded).

The conjecture: there is a unimodular `2×2` operator `M` that is the *actual* Gauss–Manin /
Seifert monodromy of the W-plane elliptic fibre `E = Bring/S₄` along the S³/2I fibration, whose
trace is the depth-2 recurrence kernel coefficient `τ` (#2488). By `unimodular_two_recurrence`, such
an `M` automatically satisfies the recurrence kernel `x² − τ·x + 1` (Cayley–Hamilton) — so the
conjecture's *content* is the **geometric identification** of `M`, not the kernel's form (which is
forced) nor the value of `τ` (which is never fitted). The falsifiable functional target is that the
*same* `M` reproduces the whole `(n−1,1)` recurrence family, not the single scalar `τ`. -/
class BringWPlaneMonodromy where
  /-- The Gauss–Manin monodromy operator on the rank-2 W-plane `H¹(E)`. -/
  M : Matrix (Fin 2) (Fin 2) ℝ
  /-- Unimodular: `det M = 1` (the symplectic structure of `H¹` of an elliptic curve). -/
  unimodular : M.det = 1
  /-- The geometric identification (the open §3b content): `M` is the genuine Seifert / Gauss–Manin
      monodromy of `E = Bring/S₄` along the S³/2I fibration. Carried as an abstract proposition. -/
  is_seifert_gauss_manin : Prop
  /-- **The conjecture**: the geometric identification holds (the §3b conjectural input). -/
  seifert_holds : is_seifert_gauss_manin

/-- **The carried monodromy satisfies the recurrence kernel (sorry-free, from the class).**
Any `BringWPlaneMonodromy` instance's operator obeys `M² = (tr M)·M − I` — the depth-2 recurrence
kernel `R(x) = x² − (tr M)·x + 1`, with `τ = tr M`. Discharged from `unimodular_two_recurrence`
applied to the class's `unimodular` field; the geometric identification (`is_seifert_gauss_manin`)
is not needed for the *algebraic* recurrence — only for the open claim that this `M` is the genuine
Seifert monodromy. -/
theorem monodromy_satisfies_recurrence [self : BringWPlaneMonodromy] :
    self.M * self.M = self.M.trace • self.M - 1 :=
  unimodular_two_recurrence self.M self.unimodular

end QOU.BraidKnot
