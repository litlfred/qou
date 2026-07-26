import QOU.Machinery.HeckeH4AlgebraLaws
import QOU.Machinery.HeckeH4BlockRep
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4BlockMap22 — the $(2,2)$ coordinate block map of $H_4(q)$

Wedderburn tranche **W2a** (bean `qou-308a`; design provenance: the H₄
Wedderburn design doc §1/§3, session scratchpad `h4_wedderburn_iso/design.md`):
the $(2,2)$ block map of the rank-4 Wedderburn picture
$H_4(q) \cong K \times K \times M_2(K) \times M_3(K) \times M_3(K)$, on the
**subscript** 24-word NF basis of `HeckeH4StabilizationRung` (H₃ Lean basis as
prefix, then (length, canonical word) order).

`blockOf22` is defined by its **explicit entries** — the `rho22_*` rows of
the verified 24×24 coordinate matrix $A$ of
`computations/h4_wedderburn/hecke-h4-wedderburn-seminormal.data.json`
(sympy-exact over $\mathbb{Q}(q)$; row/entry provenance re-verified against the
seminormal word products in the session cofactor derivation) — rather than as a
$v$-weighted sum of seminormal word products.  At rank 4 the longest basis word
is $\sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_0$; unfolding 6-fold
matrix products inside every lemma invites elaboration blowups, while the
explicit-entry definition keeps every per-entry goal a small scalar identity.
The word-product decomposition is *recovered as a theorem* inside
`blockOf22_mulNF₄` (expansion + intertwiners + unit — nothing is trusted
from the symbolic computation).

Proved here (sorry-free):

* `blockOf22_unit` — the unit $\gamma$ maps to $\mathbb{1}$ (column 0 of $A$);
* the three right-action intertwiners `blockOf22_mulσ₀/₁/₂` —
  `blockOf22 q (u·σₖ) = blockOf22 q u * Sₖ` against the proved seminormal
  matrices `S0_22/S1_22/S2_22` of `HeckeH4BlockRep` (12 scalar goals, each
  closed by `linear_combination` against `mul_inv_cancel₀` with sympy-derived,
  exactly-verified cofactors — the SET-E payloads of the design doc);
* `blockOf22_mulNF₄` — multiplicativity on the full NF product, by the
  structured route (right-basis expansion + intertwiner peeling — no 6-fold
  word product is ever elaborated);
* `H4A.blockRep22` — the induced algebra homomorphism
  `H4A K (q - q⁻¹) →ₐ[K] M_2(K)`.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every lemma below is
discharged by computation — no axiom, no conditional class, no `native_decide`;
the sympy cofactors are *payloads*, re-verified by Lean's `linear_combination`
kernel check.  Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[Field K]` — inverses are genuinely used; no
archimedean construct.  Genericity hypotheses per theorem, read off the
cofactor atoms: `q ≠ 0`, `q ^ 2 + 1 ≠ 0`, `q ^ 4 + q ^ 2 + 1 ≠ 0`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H4

set_option maxRecDepth 8000

variable {K : Type*} [Field K]

set_option maxHeartbeats 1600000 in
/-- The $(2,2)$ block map on NF coordinates, by **explicit entries**:
    row $r$, column $c$ is the `rho22_{rc}` row of the verified 24×24
    coordinate matrix $A$ applied to $v$ (inverse atoms kept separated:
    only `q⁻¹`, `(q ^ 2 + 1)⁻¹`, `(q ^ 4 + q ^ 2 + 1)⁻¹`, `(q ^ 4 + 1)⁻¹`). -/
noncomputable def blockOf22 (q : K) (v : Fin 24 → K) :
    Matrix (Fin 2) (Fin 2) K :=
  Matrix.of ![![-q ^ 3*v 21*(q ^ 2 + 1)⁻¹ - q ^ 2*v 15*(q ^ 2 + 1)⁻¹ - q ^ 2*v 16*(q ^ 2 + 1)⁻¹ - q ^ 2*v 18*(q ^ 2 + 1)⁻¹ - q ^ 2*v 19*(q ^ 2 + 1)⁻¹ + q ^ 2*v 8 + q*v 1 - q*v 10*(q ^ 2 + 1)⁻¹ - q*v 11*(q ^ 2 + 1)⁻¹ - q*v 12*(q ^ 2 + 1)⁻¹ - q*v 13*(q ^ 2 + 1)⁻¹ - q*v 14*(q ^ 2 + 1)⁻¹ - q*v 5*(q ^ 2 + 1)⁻¹ + q*v 6 + v 0 + v 17*q⁻¹ ^ 2 - v 2*(q ^ 2 + 1)⁻¹*q⁻¹ + v 20*q⁻¹ + v 22*q⁻¹ + v 23 - v 3*(q ^ 2 + 1)⁻¹ - v 4*(q ^ 2 + 1)⁻¹ - v 7*(q ^ 2 + 1)⁻¹ - v 9*(q ^ 2 + 1)⁻¹,
      q ^ 2*v 13 - q*v 16 - q*v 19 + q*v 4 + q*v 9 - v 10 + v 11*q⁻¹ ^ 2 - v 12 - v 14 + v 15*q⁻¹ + v 18*q⁻¹ + v 2 + v 21 - v 3*q⁻¹ - v 5 - v 7*q⁻¹],
    ![q ^ 6*v 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*v 15*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*v 18*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*v 3*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*v 7*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*v 10*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*v 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*v 12*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*v 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 4*v 14*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*v 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*v 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*v 2*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*v 21*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*v 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*v 5*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*v 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*v 15*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*v 18*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*v 3*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*v 7*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*v 10*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*v 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*v 12*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*v 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 2*v 14*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*v 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*v 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*v 2*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*v 21*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*v 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*v 5*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*v 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q*v 15*(q ^ 2 + 1)⁻¹ ^ 2 - q*v 18*(q ^ 2 + 1)⁻¹ ^ 2 + q*v 3*(q ^ 2 + 1)⁻¹ ^ 2 + q*v 7*(q ^ 2 + 1)⁻¹ ^ 2 - v 10*(q ^ 2 + 1)⁻¹ ^ 2 - v 12*(q ^ 2 + 1)⁻¹ ^ 2 + v 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - v 14*(q ^ 2 + 1)⁻¹ ^ 2 + v 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + v 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + v 2*(q ^ 2 + 1)⁻¹ ^ 2 + v 21*(q ^ 2 + 1)⁻¹ ^ 2 - v 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - v 5*(q ^ 2 + 1)⁻¹ ^ 2 - v 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹,
      q ^ 3*v 2*(q ^ 2 + 1)⁻¹ + q ^ 2*v 17 - q ^ 2*v 3*(q ^ 2 + 1)⁻¹ - q ^ 2*v 4*(q ^ 2 + 1)⁻¹ - q ^ 2*v 7*(q ^ 2 + 1)⁻¹ - q ^ 2*v 9*(q ^ 2 + 1)⁻¹ + q*v 10*(q ^ 2 + 1)⁻¹ + q*v 11*(q ^ 2 + 1)⁻¹ + q*v 12*(q ^ 2 + 1)⁻¹ + q*v 13*(q ^ 2 + 1)⁻¹ + q*v 14*(q ^ 2 + 1)⁻¹ - q*v 20 - q*v 22 + q*v 5*(q ^ 2 + 1)⁻¹ + v 0 - v 1*q⁻¹ - v 15*(q ^ 2 + 1)⁻¹ - v 16*(q ^ 2 + 1)⁻¹ - v 18*(q ^ 2 + 1)⁻¹ - v 19*(q ^ 2 + 1)⁻¹ + v 21*(q ^ 2 + 1)⁻¹*q⁻¹ + v 23 - v 6*q⁻¹ + v 8*q⁻¹ ^ 2]]

set_option maxHeartbeats 1600000 in
/-- The unit $\gamma$ maps to the identity matrix — column 0 of $A$ is the
    identity block $(2,2)$-component (sorry-free). -/
theorem blockOf22_unit (q : K) : blockOf22 q (unitNF₄ (R := K)) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals simp [blockOf22, unitNF₄]

set_option maxHeartbeats 1600000 in
/-- The block map intertwines the right `σ₀`-action with right
    multiplication by `S0_22` (4 scalar goals; each closed by
    `linear_combination` with the sympy-derived, exactly-verified SET-E
    cofactors — sorry-free). -/
theorem blockOf22_mulσ₀ (q : K) (hq : q ≠ 0)
    (u : Fin 24 → K) :
    blockOf22 q (mulσ₀ (q - q⁻¹) u) = blockOf22 q u * S0_22 q := by
  ext r c
  fin_cases r <;> fin_cases c
  · show blockOf22 q (mulσ₀ (q - q⁻¹) u) 0 0 =
        (blockOf22 q u * S0_22 q) 0 0
    simp only [blockOf22, S0_22, mulσ₀, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*u 21*(q ^ 2 + 1)⁻¹ + q*u 15*(q ^ 2 + 1)⁻¹ + q*u 18*(q ^ 2 + 1)⁻¹ + q*u 19*(q ^ 2 + 1)⁻¹ - q*u 8 - u 1 + u 11*(q ^ 2 + 1)⁻¹ + u 14*(q ^ 2 + 1)⁻¹ - u 17*q⁻¹ + u 2*(q ^ 2 + 1)⁻¹ - u 20 + u 5*(q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₀ (q - q⁻¹) u) 0 1 =
        (blockOf22 q u * S0_22 q) 0 1
    simp only [blockOf22, S0_22, mulσ₀, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q*u 13 + u 11*q⁻¹ + u 15 - u 16 + u 18 - u 3 + u 4 + u 9) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₀ (q - q⁻¹) u) 1 0 =
        (blockOf22 q u * S0_22 q) 1 0
    simp only [blockOf22, S0_22, mulσ₀, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*u 15*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 16*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 18*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 3*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 4*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 9*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*u 15*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 16*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 18*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 3*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 4*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 9*(q ^ 2 + 1)⁻¹ ^ 2 - q*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 15*(q ^ 2 + 1)⁻¹ ^ 2 - u 16*(q ^ 2 + 1)⁻¹ ^ 2 + u 18*(q ^ 2 + 1)⁻¹ ^ 2 - u 3*(q ^ 2 + 1)⁻¹ ^ 2 + u 4*(q ^ 2 + 1)⁻¹ ^ 2 + u 9*(q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₀ (q - q⁻¹) u) 1 1 =
        (blockOf22 q u * S0_22 q) 1 1
    simp only [blockOf22, S0_22, mulσ₀, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*u 2*(q ^ 2 + 1)⁻¹ + q*u 17 - q*u 4*(q ^ 2 + 1)⁻¹ - q*u 7*(q ^ 2 + 1)⁻¹ - q*u 9*(q ^ 2 + 1)⁻¹ - u 1 + u 10*(q ^ 2 + 1)⁻¹ + u 12*(q ^ 2 + 1)⁻¹ + u 13*(q ^ 2 + 1)⁻¹ - u 20 + u 21*(q ^ 2 + 1)⁻¹ + u 8*q⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 1600000 in
/-- The block map intertwines the right `σ₁`-action with right
    multiplication by `S1_22` (4 scalar goals; each closed by
    `linear_combination` with the sympy-derived, exactly-verified SET-E
    cofactors — sorry-free). -/
theorem blockOf22_mulσ₁ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (u : Fin 24 → K) :
    blockOf22 q (mulσ₁ (q - q⁻¹) u) = blockOf22 q u * S1_22 q := by
  ext r c
  fin_cases r <;> fin_cases c
  · show blockOf22 q (mulσ₁ (q - q⁻¹) u) 0 0 =
        (blockOf22 q u * S1_22 q) 0 0
    simp only [blockOf22, S1_22, mulσ₁, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue,
      div_eq_mul_inv, mul_inv_rev, ← inv_pow]
    linear_combination (norm := ring1)
        (q ^ 5*u 2*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*u 4*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*u 9*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 2*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*u 17*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*u 2*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*u 20*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*u 22*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*u 23*(q ^ 2 + 1)⁻¹ + q ^ 3*u 3*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*u 4*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*u 7*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*u 9*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 17*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*u 2*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 20*(q ^ 2 + 1)⁻¹ - q ^ 2*u 21*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 22*(q ^ 2 + 1)⁻¹ + q*u 11*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q*u 16*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 16*(q ^ 2 + 1)⁻¹ + q*u 17*(q ^ 2 + 1)⁻¹ - q*u 17*q⁻¹ ^ 2 - q*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 19*(q ^ 2 + 1)⁻¹ + q*u 2*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*u 2*(q ^ 2 + 1)⁻¹*q⁻¹ - q*u 2*q⁻¹ - q*u 20*q⁻¹ - q*u 22*q⁻¹ - q*u 23 + q*u 3*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 4*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 4*(q ^ 2 + 1)⁻¹ - q*u 4 + q*u 7*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 8*(q ^ 2 + 1)⁻¹ + q*u 9*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 9*(q ^ 2 + 1)⁻¹ - q*u 9 + u 1*(q ^ 2 + 1)⁻¹ - u 10*(q ^ 2 + 1)⁻¹ ^ 2 - u 12*(q ^ 2 + 1)⁻¹ ^ 2 + u 12*(q ^ 2 + 1)⁻¹ - u 13*(q ^ 2 + 1)⁻¹ ^ 2 + u 13*(q ^ 2 + 1)⁻¹ - u 14*(q ^ 2 + 1)⁻¹ ^ 2 + u 2*(q ^ 2 + 1)⁻¹ ^ 2 - u 2 - u 5*(q ^ 2 + 1)⁻¹ ^ 2 + u 5*(q ^ 2 + 1)⁻¹ + u 6*(q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 4*u 13*(q ^ 2 + 1)⁻¹ - q ^ 4*u 2*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*u 4*(q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*u 9*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*u 16*(q ^ 2 + 1)⁻¹ + q ^ 3*u 19*(q ^ 2 + 1)⁻¹ + q ^ 2*u 10*(q ^ 2 + 1)⁻¹ - q ^ 2*u 11*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*u 12*(q ^ 2 + 1)⁻¹ - q ^ 2*u 13 + q ^ 2*u 14*(q ^ 2 + 1)⁻¹ - q ^ 2*u 15*(q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*u 17*q⁻¹ ^ 3 - q ^ 2*u 18*(q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*u 2*q⁻¹ ^ 2 - q ^ 2*u 20*q⁻¹ ^ 2 - q ^ 2*u 21*(q ^ 2 + 1)⁻¹ - q ^ 2*u 22*q⁻¹ ^ 2 - q ^ 2*u 23*q⁻¹ - q ^ 2*u 4*q⁻¹ + q ^ 2*u 5*(q ^ 2 + 1)⁻¹ - q ^ 2*u 9*q⁻¹ + q*u 3*(q ^ 2 + 1)⁻¹ + q*u 7*(q ^ 2 + 1)⁻¹ - u 11*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - u 11*q⁻¹ ^ 2 - u 13*(q ^ 2 + 1)⁻¹ - u 15*(q ^ 2 + 1)⁻¹*q⁻¹ - u 15*q⁻¹ + u 17*q⁻¹ ^ 3 - u 18*(q ^ 2 + 1)⁻¹*q⁻¹ - u 18*q⁻¹ - u 2*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + u 20*q⁻¹ ^ 2 - u 21*(q ^ 2 + 1)⁻¹ - u 21 + u 22*q⁻¹ ^ 2 + u 23*q⁻¹ - u 4*(q ^ 2 + 1)⁻¹*q⁻¹ - u 9*(q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ h2
  · show blockOf22 q (mulσ₁ (q - q⁻¹) u) 0 1 =
        (blockOf22 q u * S1_22 q) 0 1
    simp only [blockOf22, S1_22, mulσ₁, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue,
      div_eq_mul_inv, mul_inv_rev, ← inv_pow]
    linear_combination (norm := ring1)
        (q ^ 3*u 2*(q ^ 2 + 1)⁻¹ - q ^ 2*u 11*(q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*u 15*(q ^ 2 + 1)⁻¹ - q ^ 2*u 18*(q ^ 2 + 1)⁻¹ + q ^ 2*u 3*(q ^ 2 + 1)⁻¹ + q ^ 2*u 7*(q ^ 2 + 1)⁻¹ - q*u 11*(q ^ 2 + 1)⁻¹ - q*u 13 - q*u 2 + u 16 + u 19 - u 4 - u 9) * mul_inv_cancel₀ hq
        + (-q ^ 3*u 13 + q ^ 2*u 16 + q ^ 2*u 19 - q ^ 2*u 2*q⁻¹ - q ^ 2*u 4 - q ^ 2*u 9 + q*u 10 + q*u 12 + q*u 13 + q*u 14 + q*u 5 + u 2*q⁻¹ + u 3 + u 4 + u 7 + u 9) * mul_inv_cancel₀ h2
  · show blockOf22 q (mulσ₁ (q - q⁻¹) u) 1 0 =
        (blockOf22 q u * S1_22 q) 1 0
    simp only [blockOf22, S1_22, mulσ₁, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue,
      div_eq_mul_inv, mul_inv_rev, ← inv_pow]
    linear_combination (norm := ring1)
        (q ^ 7*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 7*u 2*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*u 4*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 7*u 9*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 6*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 6*u 4*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 6*u 9*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*u 10*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*u 11*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*u 12*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 5*u 13*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 5*u 14*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*u 16*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 5*u 19*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*u 2*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*u 2*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*u 4*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*u 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*u 5*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*u 9*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*u 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 4*u 15*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 4*u 16*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*u 16*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 18*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 4*u 19*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 3*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 4*u 4*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*u 7*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 4*u 9*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*u 10*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*u 11*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*u 12*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 3*u 13*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 3*u 14*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*u 16*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 3*u 19*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*u 2*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*u 2*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*u 4*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*u 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*u 5*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*u 9*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*u 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*u 13*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 2*u 15*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*u 16*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 2*u 16*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 18*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*u 19*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 2*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 3*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*u 4*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 2*u 7*(q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*u 9*(q ^ 2 + 1)⁻¹ ^ 3 + q*u 10*(q ^ 2 + 1)⁻¹ ^ 3 + q*u 11*(q ^ 2 + 1)⁻¹ ^ 3 + q*u 12*(q ^ 2 + 1)⁻¹ ^ 3 + q*u 13*(q ^ 2 + 1)⁻¹ ^ 3 - q*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q*u 14*(q ^ 2 + 1)⁻¹ ^ 3 - q*u 16*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q*u 19*(q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q*u 2*(q ^ 2 + 1)⁻¹ ^ 2 + q*u 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*u 5*(q ^ 2 + 1)⁻¹ ^ 3 + q*u 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - u 15*(q ^ 2 + 1)⁻¹ ^ 3 - u 16*(q ^ 2 + 1)⁻¹ ^ 3 + u 16*(q ^ 2 + 1)⁻¹ ^ 2 - u 18*(q ^ 2 + 1)⁻¹ ^ 3 - u 19*(q ^ 2 + 1)⁻¹ ^ 3 + u 19*(q ^ 2 + 1)⁻¹ ^ 2 + u 3*(q ^ 2 + 1)⁻¹ ^ 3 + u 7*(q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (-q ^ 6*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 - q ^ 6*u 2*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 6*u 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 6*u 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 4*u 10*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*u 12*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*u 14*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*u 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*u 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*u 3*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 5*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*u 7*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 10*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*u 12*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*u 14*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*u 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 2*u 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 2*u 3*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 5*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*u 7*(q ^ 2 + 1)⁻¹ ^ 2 - u 10*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - u 12*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 - u 14*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 16*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + u 19*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + u 2*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 3*(q ^ 2 + 1)⁻¹ ^ 2 - u 4*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - u 5*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 7*(q ^ 2 + 1)⁻¹ ^ 2 - u 9*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show blockOf22 q (mulσ₁ (q - q⁻¹) u) 1 1 =
        (blockOf22 q u * S1_22 q) 1 1
    simp only [blockOf22, S1_22, mulσ₁, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue,
      div_eq_mul_inv, mul_inv_rev, ← inv_pow]
    linear_combination (norm := ring1)
        (q ^ 5*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*u 4*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*u 9*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 13*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*u 13*(q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*u 16*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*u 23*(q ^ 2 + 1)⁻¹ + q ^ 3*u 4*(q ^ 2 + 1)⁻¹ + q ^ 3*u 9*(q ^ 2 + 1)⁻¹ + q ^ 2*u 1*(q ^ 2 + 1)⁻¹ - q ^ 2*u 13*(q ^ 2 + 1)⁻¹ - q ^ 2*u 2*(q ^ 2 + 1)⁻¹ - q ^ 2*u 21*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 6*(q ^ 2 + 1)⁻¹ - q ^ 2*u 8*(q ^ 2 + 1)⁻¹*q⁻¹ + q*u 13*(q ^ 2 + 1)⁻¹*q⁻¹ - q*u 17 - q*u 23 - q*u 8*(q ^ 2 + 1)⁻¹ - u 12*(q ^ 2 + 1)⁻¹ + u 20 + u 22 - u 5*(q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 4*u 11*(q ^ 2 + 1)⁻¹ - q ^ 4*u 13*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*u 2*(q ^ 2 + 1)⁻¹ + q ^ 4*u 4*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*u 9*(q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*u 15*(q ^ 2 + 1)⁻¹ - q ^ 3*u 17 + q ^ 3*u 18*(q ^ 2 + 1)⁻¹ - q ^ 2*u 11*(q ^ 2 + 1)⁻¹ - q ^ 2*u 11 + q ^ 2*u 20 - q ^ 2*u 21*(q ^ 2 + 1)⁻¹ + q ^ 2*u 22 - q ^ 2*u 23*q⁻¹ + q*u 15*(q ^ 2 + 1)⁻¹ + q*u 15 + q*u 17 + q*u 18*(q ^ 2 + 1)⁻¹ + q*u 18 - q*u 3*(q ^ 2 + 1)⁻¹ - q*u 7*(q ^ 2 + 1)⁻¹ + u 10*(q ^ 2 + 1)⁻¹ + u 12*(q ^ 2 + 1)⁻¹ - u 13*(q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - u 13*q⁻¹ ^ 2 + u 14*(q ^ 2 + 1)⁻¹ - u 16*(q ^ 2 + 1)⁻¹*q⁻¹ - u 19*(q ^ 2 + 1)⁻¹*q⁻¹ - u 2*(q ^ 2 + 1)⁻¹ - u 2 - u 20 - u 21*(q ^ 2 + 1)⁻¹ - u 21 - u 22 + u 23*q⁻¹ + u 4*(q ^ 2 + 1)⁻¹*q⁻¹ + u 4*q⁻¹ + u 5*(q ^ 2 + 1)⁻¹ + u 9*(q ^ 2 + 1)⁻¹*q⁻¹ + u 9*q⁻¹) * mul_inv_cancel₀ h2

set_option maxHeartbeats 1600000 in
/-- The block map intertwines the right `σ₂`-action with right
    multiplication by `S2_22` (4 scalar goals; each closed by
    `linear_combination` with the sympy-derived, exactly-verified SET-E
    cofactors — sorry-free). -/
theorem blockOf22_mulσ₂ (q : K) (hq : q ≠ 0)
    (u : Fin 24 → K) :
    blockOf22 q (mulσ₂ (q - q⁻¹) u) = blockOf22 q u * S2_22 q := by
  ext r c
  fin_cases r <;> fin_cases c
  · show blockOf22 q (mulσ₂ (q - q⁻¹) u) 0 0 =
        (blockOf22 q u * S2_22 q) 0 0
    simp only [blockOf22, S2_22, mulσ₂, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*u 21*(q ^ 2 + 1)⁻¹ + q*u 15*(q ^ 2 + 1)⁻¹ + q*u 16*(q ^ 2 + 1)⁻¹ + q*u 18*(q ^ 2 + 1)⁻¹ - q*u 8 + u 10*(q ^ 2 + 1)⁻¹ + u 11*(q ^ 2 + 1)⁻¹ + u 12*(q ^ 2 + 1)⁻¹ - u 17*q⁻¹ + u 2*(q ^ 2 + 1)⁻¹ - u 22 - u 6) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₂ (q - q⁻¹) u) 0 1 =
        (blockOf22 q u * S2_22 q) 0 1
    simp only [blockOf22, S2_22, mulσ₂, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q*u 13 + u 11*q⁻¹ + u 15 + u 18 - u 19 + u 4 - u 7 + u 9) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₂ (q - q⁻¹) u) 1 0 =
        (blockOf22 q u * S2_22 q) 1 0
    simp only [blockOf22, S2_22, mulσ₂, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*u 15*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 18*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 4*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*u 7*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*u 9*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*u 15*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 18*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 19*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 4*(q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*u 7*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*u 9*(q ^ 2 + 1)⁻¹ ^ 2 - q*u 11*(q ^ 2 + 1)⁻¹ ^ 2 - u 13*(q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + u 15*(q ^ 2 + 1)⁻¹ ^ 2 + u 18*(q ^ 2 + 1)⁻¹ ^ 2 - u 19*(q ^ 2 + 1)⁻¹ ^ 2 + u 4*(q ^ 2 + 1)⁻¹ ^ 2 - u 7*(q ^ 2 + 1)⁻¹ ^ 2 + u 9*(q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show blockOf22 q (mulσ₂ (q - q⁻¹) u) 1 1 =
        (blockOf22 q u * S2_22 q) 1 1
    simp only [blockOf22, S2_22, mulσ₂, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*u 2*(q ^ 2 + 1)⁻¹ + q*u 17 - q*u 3*(q ^ 2 + 1)⁻¹ - q*u 4*(q ^ 2 + 1)⁻¹ - q*u 9*(q ^ 2 + 1)⁻¹ + u 13*(q ^ 2 + 1)⁻¹ + u 14*(q ^ 2 + 1)⁻¹ + u 21*(q ^ 2 + 1)⁻¹ - u 22 + u 5*(q ^ 2 + 1)⁻¹ - u 6 + u 8*q⁻¹) * mul_inv_cancel₀ hq

/-- The NF product as a pointwise `Pi`-sum of the 24 right word composites
    (the `mulNF₄` definition, re-read as a vector identity). -/
private theorem mulNF₄_eq_pi_sum (h : K) (u v : Fin 24 → K) :
    mulNF₄ h u v =
        v 0 • u
      + v 1 • (mulσ₀ h u)
      + v 2 • (mulσ₁ h u)
      + v 3 • (mulσ₀ h (mulσ₁ h u))
      + v 4 • (mulσ₁ h (mulσ₀ h u))
      + v 5 • (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))
      + v 6 • (mulσ₂ h u)
      + v 7 • (mulσ₂ h (mulσ₁ h u))
      + v 8 • (mulσ₀ h (mulσ₂ h u))
      + v 9 • (mulσ₁ h (mulσ₂ h u))
      + v 10 • (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))
      + v 11 • (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))
      + v 12 • (mulσ₁ h (mulσ₂ h (mulσ₁ h u)))
      + v 13 • (mulσ₁ h (mulσ₀ h (mulσ₂ h u)))
      + v 14 • (mulσ₀ h (mulσ₁ h (mulσ₂ h u)))
      + v 15 • (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u))))
      + v 16 • (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u))))
      + v 17 • (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u))))
      + v 18 • (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h u))))
      + v 19 • (mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h u))))
      + v 20 • (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))
      + v 21 • (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h u)))))
      + v 22 • (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h u)))))
      + v 23 • (mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h u)))))) := by
  funext i
  simp only [mulNF₄, Pi.add_apply, Pi.smul_apply, smul_eq_mul]

set_option maxHeartbeats 1600000 in
/-- `blockOf22` is additive in the coordinate vector (entries are linear). -/
private theorem blockOf22_add (q : K) (a b : Fin 24 → K) :
    blockOf22 q (a + b) = blockOf22 q a + blockOf22 q b := by
  ext i j
  fin_cases i <;> fin_cases j
  · show blockOf22 q (a + b) 0 0 =
        (blockOf22 q a + blockOf22 q b) 0 0
    simp only [blockOf22, Matrix.add_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.add_apply]
    ring
  · show blockOf22 q (a + b) 0 1 =
        (blockOf22 q a + blockOf22 q b) 0 1
    simp only [blockOf22, Matrix.add_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.add_apply]
    ring
  · show blockOf22 q (a + b) 1 0 =
        (blockOf22 q a + blockOf22 q b) 1 0
    simp only [blockOf22, Matrix.add_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.add_apply]
    ring
  · show blockOf22 q (a + b) 1 1 =
        (blockOf22 q a + blockOf22 q b) 1 1
    simp only [blockOf22, Matrix.add_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.add_apply]
    ring

set_option maxHeartbeats 1600000 in
/-- `blockOf22` is homogeneous in the coordinate vector. -/
private theorem blockOf22_smul (q c : K) (a : Fin 24 → K) :
    blockOf22 q (c • a) = c • blockOf22 q a := by
  ext i j
  fin_cases i <;> fin_cases j
  · show blockOf22 q (c • a) 0 0 =
        (c • blockOf22 q a) 0 0
    simp only [blockOf22, Matrix.smul_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.smul_apply, smul_eq_mul]
    ring
  · show blockOf22 q (c • a) 0 1 =
        (c • blockOf22 q a) 0 1
    simp only [blockOf22, Matrix.smul_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.smul_apply, smul_eq_mul]
    ring
  · show blockOf22 q (c • a) 1 0 =
        (c • blockOf22 q a) 1 0
    simp only [blockOf22, Matrix.smul_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.smul_apply, smul_eq_mul]
    ring
  · show blockOf22 q (c • a) 1 1 =
        (c • blockOf22 q a) 1 1
    simp only [blockOf22, Matrix.smul_apply, Matrix.of_apply,
      Matrix.cons_val, Fin.isValue, Pi.smul_apply, smul_eq_mul]
    ring

set_option maxHeartbeats 1600000 in
/-- Expansion of `blockOf22 ∘ mulNF₄` along the right basis: the block map
    of a product is the $v$-weighted sum of the block maps of the 24 word
    composites (pure bilinearity — the generator actions stay opaque). -/
private theorem blockOf22_mulNF₄_expand (q : K) (u v : Fin 24 → K) :
    blockOf22 q (mulNF₄ (q - q⁻¹) u v) =
        v 0 • blockOf22 q u
      + v 1 • blockOf22 q (mulσ₀ (q - q⁻¹) u)
      + v 2 • blockOf22 q (mulσ₁ (q - q⁻¹) u)
      + v 3 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u))
      + v 4 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u))
      + v 5 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u)))
      + v 6 • blockOf22 q (mulσ₂ (q - q⁻¹) u)
      + v 7 • blockOf22 q (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u))
      + v 8 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₂ (q - q⁻¹) u))
      + v 9 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) u))
      + v 10 • blockOf22 q (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u)))
      + v 11 • blockOf22 q (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u)))
      + v 12 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u)))
      + v 13 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₂ (q - q⁻¹) u)))
      + v 14 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) u)))
      + v 15 • blockOf22 q (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u))))
      + v 16 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u))))
      + v 17 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u))))
      + v 18 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u))))
      + v 19 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₂ (q - q⁻¹) u))))
      + v 20 • blockOf22 q (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u)))))
      + v 21 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u)))))
      + v 22 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) u)))))
      + v 23 • blockOf22 q (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₂ (q - q⁻¹) (mulσ₀ (q - q⁻¹) (mulσ₁ (q - q⁻¹) (mulσ₀ (q - q⁻¹) u)))))) := by
  rw [mulNF₄_eq_pi_sum]
  simp only [blockOf22_add, blockOf22_smul]

set_option maxHeartbeats 1600000 in
/-- **Multiplicativity of the $(2,2)$ block map on the full NF product
    (sorry-free)** — expand along the right basis, peel every word composite
    with the three intertwiners (both for general `u` and for `u = γ`, which
    recovers the word-product decomposition of the explicit entries), and
    collect with associativity. -/
theorem blockOf22_mulNF₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (u v : Fin 24 → K) :
    blockOf22 q (mulNF₄ (q - q⁻¹) u v) = blockOf22 q u * blockOf22 q v := by
  have hu := blockOf22_mulNF₄_expand q u v
  have h1 := blockOf22_mulNF₄_expand q (unitNF₄ (R := K)) v
  rw [mulNF₄_one_left] at h1
  simp only [blockOf22_mulσ₀ q hq, blockOf22_mulσ₁ q hq h2,
    blockOf22_mulσ₂ q hq, blockOf22_unit q, one_mul] at hu h1
  rw [hu, h1]
  simp only [Matrix.mul_add, Matrix.mul_smul, Matrix.mul_one, Matrix.mul_assoc]

namespace H4A

set_option maxHeartbeats 3200000 in
/-- **The $(2,2)$ block representation (sorry-free).**  The algebra
    homomorphism `H₄(q) →ₐ M_2(K)` induced by the explicit-entry block map;
    with the two characters and the sibling blocks this is the block *data*
    of $H_4(q) \cong K \times K \times M_2 \times M_3 \times M_3$. -/
noncomputable def blockRep22 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    H4A K (q - q⁻¹) →ₐ[K] Matrix (Fin 2) (Fin 2) K where
  toFun x := blockOf22 q x.v
  map_one' := by
    show blockOf22 q (unitNF₄ (R := K)) = 1
    exact blockOf22_unit q
  map_mul' x y := blockOf22_mulNF₄ q hq h2 x.v y.v
  map_zero' := by
    show blockOf22 q (0 : Fin 24 → K) = 0
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf22]
  map_add' x y := by
    show blockOf22 q (x.v + y.v) = blockOf22 q x.v + blockOf22 q y.v
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf22, Matrix.add_apply, Pi.add_apply]
    all_goals try ring
  commutes' c := by
    show blockOf22 q ((c • (1 : H4A K (q - q⁻¹))).v) = _
    rw [smul_v, one_v]
    ext i j
    fin_cases i <;> fin_cases j
    all_goals simp [blockOf22, unitNF₄, Matrix.algebraMap_matrix_apply,
      Pi.smul_apply, smul_eq_mul]

end H4A

end QOU.Machinery.H4
