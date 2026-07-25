import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.Mass.QbetaC3OddDOF — why the Q_β ladder rung `c₃` is a SEPARATE degree of
freedom, not pinned by the determined ℚ(√3) net solve that pins `c₂`.

**Scope (read first).** This file settles — HONESTLY, sorry-free — the decisive
fork on bean `qou-1dnr`: is the Q_β precision-ladder rung `c₃` pinned (exactly
determined) by the determined triangular solve on the derived net decay-width,
the same object that makes `c₂ = -1` a structural identity? **Verdict (B):
`c₃` is a separate DOF.** The structural reason is formalized here; the exact
ℚ(√3) evaluation lives in the witness
`qbeta-c3-odd-dof-normalization-fork.witness.json`
(producer `computations/qbeta/qbeta_c3_odd_dof_normalization_fork_probe.py`).

**The ladder.** `Q_β = Q_base · ∏_{k≥2} (1 + c_k · u^k)`, `u = b · ℏ_q²`
(`ck-dk-canonical-registry.md §3`). Reading `log R` order by order, each `c_k`
is pinned triangularly at the leading order of its rung.

**What changes at order 3 (the crux).**

* `c₂` is the LEADING rung: pinned at the first order where `u²` appears, with
  NO prior rung to subtract. It equals `f₄ / u₂²`, depending only on the
  observable's order-4 coefficient `f₄` and the ladder variable's LEADING
  coefficient `u₂`. It is therefore invariant under any reparametrisation
  `ũ = w · u` of the ladder variable by a unit series `w = 1 + w₁ s + …`
  (which preserves `u₂`). This is the algebraic shadow of the closed N=2
  correction factor `1 − b²ℏ_q⁴ = 1 − u²` (`QOU.QBeta.C2Structural`,
  `q-beta-c-2-eq-neg-one-structural.lean`): a finite degree-2 factor, so its
  coefficient is a genuine structural invariant `c₂ = -1`.

* `c₃` is the first SUBLEADING rung: pinning it at order `s⁶` requires
  subtracting the order-6 TAIL of the already-fixed `c₂` rung, and that tail,
  `2·u₂·u₄ + u₃²`, depends on the SUBLEADING coefficients `u₃, u₄`. The unit
  reparametrisation moves them (`u₃ ↦ u₃ + w₁u₂`, `u₄ ↦ u₄ + w₁u₃ + w₂u₂`), so
  the extracted `c₃` SHIFTS by an explicit amount `c₂·(4w₁u₃ + 2w₂u₂ + w₁²u₂)/u₂²`.
  It is NOT a reparametrisation invariant, hence NOT a canonical structural
  identity pinned by the determined solve.

  The physically-mandated reparametrisation is exactly `w = q` (bar-weight:
  `u = b·ℏ_q²` has `u ∘ σ = q²·u`, so the bar-even variable is `ũ = q·u`;
  audit `2026-07-03-u-tilde-bar-weight-normalization.md`). At `w = q` the shift
  is `c₂·(4u₃ + u₂)/u₂²`, evaluated in the witness to the nonzero exact
  ℚ(√3) number `35/6 + 7343√3/216` — c₂ diff `= 0` exactly, c₃ diff `≠ 0`.

**Consequence.** Because `c₃`'s determined-solve value is not presentation-
invariant AND (see the odd-residual pillar in the audit) the bar-ODD content
`c₃` must carry decouples from the even-power ladder entirely, fixing `c₃`
requires an input BEYOND the determined even solve — the fibre-saddle Stokes
datum `A_ω` (`QOU.Mass.QbetaC3Stokes`, #3805). This file's non-invariance is
the algebraic certificate that `A_ω` is REQUIRED, not optional.

**Honesty (AGENTS.md §Axiomatization is NOT a Proof, §Before declaring
"refuted", §7c).** No `c_k` is wired to production. This is a scope-(a)
structural result: a reparametrisation-invariance identity (`c₂`) and an
explicit non-vanishing reparametrisation shift (`c₃`), both proved over a
generic field. It excludes `c₃` from being a *presentation-invariant* pinned
value; it does not claim `c₃` is unknowable — its value is fixed once the extra
(fibre `A_ω`) datum is supplied.
-/

namespace QOU.Mass.QbetaC3OddDOF

variable {R : Type*} [Field R]

/-- **Leading (k=2) ladder rung.** Pinned at order `s⁴`, the leading order of
`u²`. Takes the full local ladder data `(u₂, u₃, u₄)` but, being the leading
rung with no prior rung to subtract, uses ONLY `u₂` — the source of its
reparametrisation invariance. -/
def c2Of (f4 u2 _u3 _u4 : R) : R := f4 / u2 ^ 2

/-- **First subleading (k=3) ladder rung.** Pinned at order `s⁶` after removing
the order-6 tail `2·u₂·u₄ + u₃²` of the fixed `c₂` rung; `[u³]₆ = u₂³`. -/
def c3Of (f4 f6 u2 u3 u4 : R) : R :=
  (f6 - c2Of f4 u2 u3 u4 * (2 * u2 * u4 + u3 ^ 2)) / u2 ^ 3

/-- **The leading rung is independent of the subleading ladder data.**
`c₂` does not depend on `u₃, u₄`, so any reparametrisation that preserves the
leading coefficient `u₂` (a unit rescaling `ũ = w·u`, `w[0]=1`) leaves `c₂`
unchanged. This is the exact-zero `c₂` fork of the witness. -/
theorem c2Of_indep_subleading (f4 u2 u3 u4 u3' u4' : R) :
    c2Of f4 u2 u3 u4 = c2Of f4 u2 u3' u4' := rfl

/-- **The unit reparametrisation `ũ = w·u`.** With `w = 1 + w₁ s + w₂ s² + …`
and `u = u₂ s² + u₃ s³ + u₄ s⁴ + …`, the product `w·u` has coefficients
`ũ₂ = u₂`, `ũ₃ = u₃ + w₁u₂`, `ũ₄ = u₄ + w₁u₃ + w₂u₂`. The leading coefficient
is preserved. -/
theorem reparam_leading_preserved (u2 u3 u4 w1 w2 : R) :
    c2Of (0 : R) u2 (u3 + w1 * u2) (u4 + w1 * u3 + w2 * u2)
      = c2Of (0 : R) u2 u3 u4 := rfl

/-- **The k=3 rung SHIFTS under the unit reparametrisation — explicit formula.**
Extracting `c₃` from the reparametrised variable `ũ = w·u` (same observable, so
same `f₄, f₆`; same leading `u₂`) differs from the original by exactly
`c₂ · (4w₁u₃ + 2w₂u₂ + w₁²u₂) / u₂²`. Sorry-free `field_simp; ring`. -/
theorem c3Of_reparam_shift (f4 f6 u2 u3 u4 w1 w2 : R) (hu2 : u2 ≠ 0) :
    c3Of f4 f6 u2 u3 u4
      - c3Of f4 f6 u2 (u3 + w1 * u2) (u4 + w1 * u3 + w2 * u2)
      = c2Of f4 u2 u3 u4 * (4 * w1 * u3 + 2 * w2 * u2 + w1 ^ 2 * u2) / u2 ^ 2 := by
  unfold c3Of c2Of
  field_simp
  ring

/-- **The physically-mandated case `w = q` (`w₁ = 1, w₂ = 0`): shift is
`c₂·(4u₃ + u₂)/u₂²`.** This is the `u → ũ = q·u` bar-weight renormalization. -/
theorem c3Of_reparam_shift_q (f4 f6 u2 u3 u4 : R) (hu2 : u2 ≠ 0) :
    c3Of f4 f6 u2 u3 u4 - c3Of f4 f6 u2 (u3 + u2) (u4 + u3)
      = c2Of f4 u2 u3 u4 * (4 * u3 + u2) / u2 ^ 2 := by
  have h := c3Of_reparam_shift f4 f6 u2 u3 u4 1 0 hu2
  simpa using h

/-- **The k=3 shift is nonzero whenever the leading rung and the combination are
nonzero.** So `c₃` is genuinely not a reparametrisation invariant: it is a
SEPARATE degree of freedom relative to the determined leading solve. -/
theorem c3Of_reparam_shift_ne_zero (f4 f6 u2 u3 u4 w1 w2 : R) (hu2 : u2 ≠ 0)
    (hc2 : c2Of f4 u2 u3 u4 ≠ 0)
    (hcomb : 4 * w1 * u3 + 2 * w2 * u2 + w1 ^ 2 * u2 ≠ 0) :
    c3Of f4 f6 u2 u3 u4
      - c3Of f4 f6 u2 (u3 + w1 * u2) (u4 + w1 * u3 + w2 * u2) ≠ 0 := by
  rw [c3Of_reparam_shift f4 f6 u2 u3 u4 w1 w2 hu2]
  exact div_ne_zero (mul_ne_zero hc2 hcomb) (pow_ne_zero 2 hu2)

/-- **Decisive contrast, one statement.** For the unit reparametrisation
`ũ = q·u` there EXIST ladder data over any field for which the leading `c₂`
shift is `0` while the `c₃` shift is `≠ 0`: `c₂` is a reparametrisation
invariant, `c₃` is not. This is the sorry-free algebraic form of the exact
witness (`c₂ diff = 0`, `c₃ diff = 35/6 + 7343√3/216 ≠ 0`). -/
theorem c2_pinned_c3_free :
    ∃ f4 f6 u2 u3 u4 : R,
      (c2Of f4 u2 u3 u4 - c2Of f4 u2 (u3 + u2) (u4 + u3) = 0) ∧
      (c3Of f4 f6 u2 u3 u4 - c3Of f4 f6 u2 (u3 + u2) (u4 + u3) ≠ 0) := by
  refine ⟨1, 0, 1, 0, 0, ?_, ?_⟩
  · simp [c2Of]
  · rw [c3Of_reparam_shift_q (1 : R) 0 1 0 0 one_ne_zero]
    norm_num [c2Of]

end QOU.Mass.QbetaC3OddDOF
