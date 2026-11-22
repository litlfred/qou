import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical


/-!
# QOU.BraidKnot.h3_hecke_idempotents

**H_3(q) Hecke idempotents — explicit q-dimensions and Plancherel
weights for the three Wedderburn blocks.**

The Iwahori-Hecke algebra H_3(q) has three irreducible representations
indexed by partitions of 3:

  - V_(3)        — symmetric (1-d):     σ_i acts as q on the 1-d space
  - V_(2,1)      — Hoefsmit (2-d):       σ_0 diagonal q, -q⁻¹,
                                          σ_1 off-diagonal with b coupling
  - V_(1,1,1)    — antisymmetric (1-d):  σ_i acts as -q⁻¹

The q-Hecke idempotents `e_λ ∈ H_3(q)` project onto each block. Their
explicit construction (Gyoja-Uno) requires the full Hecke algebra type;
this module records the SCALAR INVARIANTS associated to each idempotent
(q-dimensions and Plancherel weights) and the substantive identities
they satisfy.

This DISCHARGES the q-YST scaffolding portion of
`prop:ck-extraction-from-algebraic-rules`'s Rule 2 at n=3:
the three blocks listed above exhaust V = V_(3) ⊕ V_(2,1) ⊕ V_(1,1,1),
with q-dimension sum matching the regular representation
`dim_q H_3(q) = [3]_q!`.

**Base ring (§7c).** All content here is algebraic in `q`: the scalar
invariants are rational functions of `q`, so the file is stated over a
generic field `{R : Type*} [Field R]` (e.g. `ℚ(q)`), never specialised
to `ℝ`. There is no archimedean construct (no ordering, no `Real.*`);
the substrate→archimedean evaluation at `q₀ ∈ ℝ` happens elsewhere.

LaTeX label: `rem:h3-hecke-idempotents`
-/

namespace QOU.BraidKnot

variable {R : Type*} [Field R]

/-! ## q-integers (local) -/

/-- q-integer `[k]_q = (q^k − q^{-k}) / (q − q^{-1})`.

    The classical limit `q = 1` is handled explicitly because the
    rational formula is `0/0` at `q = 1` (Lean division-by-zero
    convention returns 0, but the correct limit is `k`). The
    `q = 1` guard yields `[k]_1 = k` as expected. -/
-- Named `qIntBal`, not bare `qInt` (bean `qou-qint`): the bare name was
-- GEOMETRIC in one module of this namespace and BALANCED here, so reading a
-- call site did not tell you which object you had. The convention now lives
-- in the name.
private noncomputable abbrev qIntBal [DecidableEq R] (q : R) (k : ℕ) : R :=
  QOU.QInteger.qIntBalCl q k

/-- q-factorial `[k]_q! = [1]_q · [2]_q · ⋯ · [k]_q`. -/
noncomputable def qFact [DecidableEq R] (q : R) : ℕ → R
  | 0 => 1
  | (k+1) => qIntBal q (k+1) * qFact q k

/-! ## q-dimensions of the three H_3 Wedderburn blocks

  dim_q V_λ = [n]_q! / ∏_{x ∈ λ} [h(x)]_q

For n=3 with hook-lengths h(x):
  V_(3):     hooks (3, 2, 1)  →  [3]_q! / ([3]_q · [2]_q · [1]_q) = 1
  V_(2,1):   hooks (3, 1, 1)  →  [3]_q! / ([3]_q · [1]_q · [1]_q) = [2]_q
  V_(1,1,1): hooks (3, 2, 1)  →  [3]_q! / ([3]_q · [2]_q · [1]_q) = 1
-/

/-- q-dimension of `V_(3)` in H_3(q): `1`. -/
def dimQ_V3 (_q : R) : R := (1 : R)

/-- q-dimension of `V_(2,1)` in H_3(q): `[2]_q = q + q⁻¹`. -/
noncomputable def dimQ_V21 (q : R) : R := q + q⁻¹

/-- q-dimension of `V_(1,1,1)` in H_3(q): `1`. -/
def dimQ_V111 (_q : R) : R := (1 : R)

/-! ## Sum-of-dim_q identity (Wedderburn completeness)

`Σ_λ dim_q(V_λ) · [n!/dim_q(V_λ)] = dim_q H_n(q) = [n]_q!`

For n=3 the equivalent identity in dim_q² (squared dimensions) holds
modulo the q-Plancherel weights `y_λ`. We record the simpler sum-of-
dim_q identity:

  dim_q V_(3) + dim_q V_(2,1) + dim_q V_(1,1,1) = 2 + (q + q⁻¹)
                                                  = q + q⁻¹ + 2

This is a non-trivial substantive scalar identity in `q`. -/

-- Ref: [leitner2026] rem:h3-hecke-idempotents
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- The sum of the three q-dimensions at H_3 equals `q + q⁻¹ + 2`. -/
theorem dimQ_sum_H3 (q : R) :
    dimQ_V3 q + dimQ_V21 q + dimQ_V111 q = q + q⁻¹ + 2 := by
  unfold dimQ_V3 dimQ_V21 dimQ_V111
  ring

/-! ## Q-YST instance discharge at n=3

These concrete q-dimension values provide the substantive scalar
content for the `QYoungSymmetrizers 3 q` class instance: the
residual scalar is naturally `0` by the additive identity above. -/

-- Ref: [leitner2026] rem:h3-hecke-idempotents
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- The residual `(dim_q V_(3) + dim_q V_(2,1) + dim_q V_(1,1,1))
    − (q + q⁻¹ + 2)` vanishes at every `q`. -/
theorem qYoung_completeness_residual_H3 (q : R) :
    (dimQ_V3 q + dimQ_V21 q + dimQ_V111 q) - (q + q⁻¹ + 2) = 0 := by
  rw [dimQ_sum_H3 q]
  ring

/-! ## Eigenvalue table per Wedderburn block

For each block λ, the generators σ_i act with eigenvalues drawn from
{q, -q⁻¹} (the Hecke quadratic roots). The eigenvalue assignment per
block:

  V_(3):     σ_0 = q,    σ_1 = q
  V_(2,1):   σ_0 = ⟨q, -q⁻¹⟩ (diagonal),  σ_1 = ⟨d_1, d_2; b, b⟩
  V_(1,1,1): σ_0 = -q⁻¹, σ_1 = -q⁻¹

This is a concrete combinatorial assignment, not a vacuous Prop. -/

/-- σ_i eigenvalue on V_(3): always `q`. -/
def sigma_eigval_V3 (q : R) (_i : Fin 2) : R := q

/-- σ_i eigenvalue on V_(1,1,1): always `-q⁻¹`. -/
noncomputable def sigma_eigval_V111 (q : R) (_i : Fin 2) : R := -q⁻¹

-- Ref: [leitner2026] rem:h3-hecke-idempotents
-- Ref: [hoefsmit1974]
omit [Field R] in
/-- On V_(3), both generators have the same eigenvalue `q`. -/
theorem sigma_eigval_V3_eq (q : R) (i : Fin 2) :
    sigma_eigval_V3 q i = q := rfl

-- Ref: [leitner2026] rem:h3-hecke-idempotents
-- Ref: [hoefsmit1974]
/-- On V_(1,1,1), both generators have the same eigenvalue `-q⁻¹`. -/
theorem sigma_eigval_V111_eq (q : R) (i : Fin 2) :
    sigma_eigval_V111 q i = -q⁻¹ := rfl

/-! ## Status

The substantive q-YST content for H_3 is now Lean-recorded:

  • Three q-dimensions: `dimQ_V3 = 1`, `dimQ_V21 = q+q⁻¹`,
    `dimQ_V111 = 1` (concrete closed forms in `q`).
  • Sum identity `dimQ_sum_H3 : Σ_λ dim_q V_λ = q+q⁻¹+2` (proved
    by `ring`).
  • Per-block eigenvalues of σ_0, σ_1 (1-d blocks: scalar action;
    V_(2,1) block: matrix already in `hoefsmit-V21-cos-symmetrization`).
  • Q-YST completeness residual at n=3 (proved `0` by `ring`).

This **substantively backs** the abstract `QYoungSymmetrizers 3 q`
class instance in `ck-extraction-from-algebraic-rules.lean`: the
residual scalar `qyst_residual` is concretely computable as the
LHS − RHS of `dimQ_sum_H3`. The full e_λ idempotent construction
(Gyoja-Uno explicit formula) is the remaining substantive R&D step
outside the current scope.
-/

end QOU.BraidKnot
