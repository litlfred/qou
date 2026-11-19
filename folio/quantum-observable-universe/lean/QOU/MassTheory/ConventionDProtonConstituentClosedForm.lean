/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.Archimedean.BringSchwingerNormalizationDerivation

/-!
# Convention-D Constituent Nucleon Closed Forms, Mass-Tower Trace Reconciliation, and `α_EM` Bridge

This module resolves three coupled structural gaps in the mass-endomorphism and
electromagnetic-coupling sectors:

1. **Exact Convention-D Rational Closed Forms for Constituent Nucleon Traces (`qou-nzp3`):**
   Under the forced Convention-D Markov parameter $z_D(q) = q^3/(q^2 + 1)$ on $H_3(q)$,
   the three-row Wedderburn–Markov weight vanishes ($y_{(1,1,1)}^D(q) = 0$) and the
   remaining two weights are
   $$
     y_{(3)}^D(q) = \frac{q^4 + 1}{(q^2 + 1)^2} = \frac{h^2 + 2}{h^2 + 4},
     \qquad
     y_{(2,1)}^D(q) = \frac{q^2}{(q^2 + 1)^2} = \frac{1}{h^2 + 4},
     \qquad
     h = q - q^{-1}.
   $$
   Evaluating the irreducible characters $\chi_{(3)}$ and $\chi_{(2,1)}$ on the
   11-letter canonical proton and neutron elements in $H_3(q)$ (with the two
   intra-nucleon averaged letters $\sigma_g - \frac{h}{2}\mathbf{1}$ expanded by
   linearity) yields exact rational closed forms in $\mathbb{Q}(q)$ for **both**
   the canonical alternating (`borromean`) core $(\sigma_0 \sigma_1^{-1})^3$ and
   the historical `grouped` core $\sigma_0^3 \cdots \sigma_1^{-3}$:
   - **Canonical alternating (`borromean`) proton constituent step:**
     $$
       \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})(q)
       = \frac{(q^4 + 1)(q^{18} - 3q^{16} + 7q^{14} - 8q^{12} + 10q^{10} - 9q^8 + 10q^6 - 6q^4 + 3q^2 - 1)}
              {4 q^9 (q^2 + 1)^2},
     $$
   - **Canonical alternating (`borromean`) neutron constituent step:**
     $$
       \mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})(q)
       = \frac{(q^4 + 1)(q^{14} - 3q^{12} + 4q^{10} - 4q^8 + 5q^6 - 4q^4 + 3q^2 - 1)}
              {4 q^9},
     $$
   - **Historical `grouped` proton and neutron constituent steps:**
     $$
       \mathrm{tr}_M^{z_D}(p_{\mathrm{grp}})(q)
       = \frac{(q^8 + q^4 + q^2 + 1)(q^{14} + q^{12} + q^{10} - 1)}
              {4 q^9 (q^2 + 1)^2},
       \qquad
       \mathrm{tr}_M^{z_D}(n_{\mathrm{grp}})(q)
       = \frac{(q^8 - q^6 + q^4 + 1)(q^{10} + q^6 - q^4 + q^2 - 1)}
              {4 q^9}.
     $$
   At $q = 1$, all four Convention-D nucleon traces evaluate to $z_D(1) = 1/2$,
   refuting the C-era ansatz $2q - 1$ ($= 1$ at $q = 1$).

2. **Reconciliation of `tr_M` vs. `tr_reg` and Classical vs. $q$-Deformed Weights
   in `prop:mass-endomorphism-tower` (`qou-j11h`):**
   On any single-generator factor $a_i \sigma_i + b_i \mathbf{1} \in \langle \sigma_i \rangle \subset H_3(q)$,
   the localized Convention-D Jones–Markov trace equals the standard channel
   $V_i^{\mathrm{std}} = z_D(q)\,a_i + b_i$, and the grouped whole-word trace factors
   identically as $\mathrm{tr}_M^{z_D}(X_0(\sigma_0) X_1(\sigma_1)) = V_0^{\mathrm{std}} V_1^{\mathrm{std}}$.
   By contrast, the 3-channel additive Wedderburn volume $V_i^{\mathrm{full}}$ is a linear
   functional $z_{\mathrm{full}}(q)\,a_i + b_i$ with effective parameter
   $$
     z_{\mathrm{full},q}(q) = \frac{h + (h^2 + 4) z_D(q)}{h^2 + 6}
                            = \frac{q(q^4 + 2q^2 - 1)}{q^4 + 4q^2 + 1},
     \qquad
     z_{\mathrm{full,cl}}(q) = \frac{h + 4 z_D(q)}{6}
                             = \frac{5q^4 - 1}{6 q (q^2 + 1)},
   $$
   yielding the exact channel-difference and weight-difference formulas:
   $$
     V_i^{\mathrm{full},q} - V_i^{\mathrm{std}}
       = -\frac{q(q^4 + 1)}{(q^2 + 1)(q^4 + 4q^2 + 1)}\,a_i,
     \qquad
     V_i^{\mathrm{full},q} - V_i^{\mathrm{full,cl}}
       = \frac{(q^2 - 1)^2 (q^4 + 1)}{6 q (q^2 + 1)(q^4 + 4q^2 + 1)}\,a_i.
   $$

3. **Reconciliation of the Three $\alpha_{\mathrm{EM}}^{-1}$ Formulations (`qou-aemx`):**
   Proves that the superseded gluon-octet prefactor $45[3]_q$ ($= 135$ at $q = 1$) and
   the derived Layer-2/3 bare prefactor $T_{\mathrm{bare}}(q) = q[9]_q[10]_q$ ($= 90$ at $q = 1$)
   have distinct classical limits ($90 \neq 135$), while the live Chern–Simons resummed
   tower and the Bring–Schwinger fixed-point equation share the exact same bare prefactor
   $T_{\mathrm{bare}}(q)$ and coincide if and only if the resummed Chern–Simons shift
   $\Delta_{\mathrm{CS}}(q) / (1 - \kappa\,\delta_{\mathrm{CS}}(q))$ equals the
   tiling-derived Bring–Schwinger shift $2/(3\pi) + \alpha\,\mathcal{H}(q)(1 - c\alpha)$.

## References

- [leitner2026] `prop:interface-knot-markov-z`, `prop:mass-endomorphism-tower`,
  `conj:em-coupling-chern-simons`, `prop:em-coupling-bring-zero-mode`
- [jones1987] V. F. R. Jones, *Hecke algebra representations of braid groups and link
  polynomials*, Ann. of Math. (2) **126** (1987), 335–388.
- [wenzl1988] H. Wenzl, *Hecke algebras of type $A_n$ and subfactors*, Invent. Math.
  **92** (1988), 349–383.
-/

namespace QOU.MassTheory.ConventionDProtonConstituentClosedForm

open scoped Matrix

/-! ## Section 1: Convention-D Wedderburn–Markov Weights & Constituent Nucleon Closed Forms (`qou-nzp3`) -/

section FieldAlgebraic

variable {K : Type*} [Field K] [CharZero K]
set_option linter.unusedSectionVars false

/-- The Iwahori–Hecke skein parameter $h(q) = q - q^{-1}$ from `σ_i^2 = h σ_i + 1`. -/
def heckeH (q : K) : K := q - 1 / q

/-- The forced Convention-D Markov parameter $z_D(q) = q^3 / (q^2 + 1)$ on $H_n(q)$. -/
def markovZD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Convention-D Wedderburn–Markov weight $y_{(3)}^D(q) = (q^4 + 1) / (q^2 + 1)^2$
    for the trivial 1D representation $\lambda = (3)$ of $H_3(q)$. -/
def yThreeD (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- Convention-D Wedderburn–Markov weight $y_{(2,1)}^D(q) = q^2 / (q^2 + 1)^2$
    for the standard 2D representation $\lambda = (2,1)$ of $H_3(q)$. -/
def yTwoOneD (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- Convention-D Wedderburn–Markov weight $y_{(1,1,1)}^D(q) = 0$ for the sign
    representation $\lambda = (1,1,1)$ of $H_3(q)$ (Temperley–Lieb 2-row cap). -/
def yOneOneOneD : K := 0

/-- **Markov identity normalization on $H_3(q)$:**
    $\mathrm{tr}_M^{z_D}(\mathbf{1}) = y_{(3)}^D(q)\cdot 1 + y_{(2,1)}^D(q)\cdot 2 + y_{(1,1,1)}^D\cdot 1 = 1$. -/
theorem wenzlD_norm_id (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    yThreeD q + 2 * yTwoOneD q + yOneOneOneD = 1 := by
  unfold yThreeD yTwoOneD yOneOneOneD
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hsq]
  ring

/-- **Markov single-generator trace on $H_3(q)$:**
    $\mathrm{tr}_M^{z_D}(\sigma_i) = y_{(3)}^D(q)\,q + y_{(2,1)}^D(q)\,h(q) - y_{(1,1,1)}^D\,q^{-1} = z_D(q)$. -/
theorem wenzlD_trace_gen (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    yThreeD q * q + yTwoOneD q * heckeH q - yOneOneOneD * (1 / q) = markovZD q := by
  unfold yThreeD yTwoOneD yOneOneOneD heckeH markovZD
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Markov two-generator trace on $H_3(q)$:**
    $\mathrm{tr}_M^{z_D}(\sigma_0 \sigma_1) = y_{(3)}^D(q)\,q^2 - y_{(2,1)}^D(q) + y_{(1,1,1)}^D\,q^{-2} = z_D(q)^2$. -/
theorem wenzlD_trace_pair (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    yThreeD q * q ^ 2 - yTwoOneD q + yOneOneOneD * (1 / q) ^ 2 = (markovZD q) ^ 2 := by
  unfold yThreeD yTwoOneD yOneOneOneD markovZD
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Skein-parameter form of $y_{(3)}^D(q)$ and $y_{(2,1)}^D(q)$:**
    In terms of $h = q - q^{-1}$ (so $h^2 + 2 = q^2 + q^{-2}$ and $h^2 + 4 = (q + q^{-1})^2$),
    $y_{(3)}^D(q) = (h^2 + 2)/(h^2 + 4)$ and $y_{(2,1)}^D(q) = 1/(h^2 + 4)$. -/
theorem wenzlD_weights_eq_heckeH (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hh4 : (heckeH q) ^ 2 + 4 ≠ 0) :
    yThreeD q = ((heckeH q) ^ 2 + 2) / ((heckeH q) ^ 2 + 4) ∧
    yTwoOneD q = 1 / ((heckeH q) ^ 2 + 4) := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  constructor
  · unfold yThreeD
    rw [div_eq_div_iff hsq hh4]
    unfold heckeH
    field_simp [hq]
    ring
  · unfold yTwoOneD
    rw [div_eq_div_iff hsq hh4]
    unfold heckeH
    field_simp [hq]
    ring

/-! ### Explicit $2 \times 2$ Standard Representation $\rho_{(2,1)}$ of $H_3(q)$ and Borromean Core -/

/-- The generator $\rho_{(2,1)}(\sigma_0) = \begin{pmatrix} q & 0 \\ 1 & -q^{-1} \end{pmatrix}$
    in the 2D standard representation $\lambda = (2,1)$ of $H_3(q)$. -/
def stdGen0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![q, 0; 1, -(1 / q)]

/-- The generator $\rho_{(2,1)}(\sigma_1) = \begin{pmatrix} -q^{-1} & 1 \\ 0 & q \end{pmatrix}$
    in the 2D standard representation $\lambda = (2,1)$ of $H_3(q)$. -/
def stdGen1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-(1 / q), 1; 0, q]

/-- The inverse generator $\rho_{(2,1)}(\sigma_1^{-1}) = \rho_{(2,1)}(\sigma_1) - h I_2
    = \begin{pmatrix} -q & 1 \\ 0 & q^{-1} \end{pmatrix}$. -/
def stdGen1Inv (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-q, 1; 0, 1 / q]

/-- Single Borromean step $B_1(q) := \rho_{(2,1)}(\sigma_0 \sigma_1^{-1})
    = \begin{pmatrix} -q^2 & q \\ -q & 1 - q^{-2} \end{pmatrix}$. -/
def stdBorromeanStep (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen0 q * stdGen1Inv q

/-- **Hecke quadratic relation on $\rho_{(2,1)}(\sigma_0)$:**
    $\rho_{(2,1)}(\sigma_0)^2 = h(q)\,\rho_{(2,1)}(\sigma_0) + I_2$. -/
theorem stdGen0_sq_eq (q : K) (hq : q ≠ 0) :
    stdGen0 q * stdGen0 q = heckeH q • stdGen0 q + (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen0, heckeH, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp [hq] <;> ring

/-- **Hecke quadratic relation on $\rho_{(2,1)}(\sigma_1)$:**
    $\rho_{(2,1)}(\sigma_1)^2 = h(q)\,\rho_{(2,1)}(\sigma_1) + I_2$. -/
theorem stdGen1_sq_eq (q : K) (hq : q ≠ 0) :
    stdGen1 q * stdGen1 q = heckeH q • stdGen1 q + (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdGen1, heckeH, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp [hq] <;> ring

/-- **Yang–Baxter braid relation on $\rho_{(2,1)}$:**
    $\rho_{(2,1)}(\sigma_0)\rho_{(2,1)}(\sigma_1)\rho_{(2,1)}(\sigma_0)
     = \rho_{(2,1)}(\sigma_1)\rho_{(2,1)}(\sigma_0)\rho_{(2,1)}(\sigma_1)$. -/
theorem stdGen_braid_relation (q : K) (hq : q ≠ 0) :
    stdGen0 q * stdGen1 q * stdGen0 q = stdGen1 q * stdGen0 q * stdGen1 q := by
  ext i j
  fin_cases i <;> fin_cases j
  · simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two, hq]
  · simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two]; field_simp [hq]; ring
  · simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two]; field_simp [hq]; ring
  · simp [stdGen0, stdGen1, Matrix.mul_apply, Fin.sum_univ_two, hq]

/-- **Trace and determinant of the single Borromean step $B_1 = \rho_{(2,1)}(\sigma_0 \sigma_1^{-1})$:**
    $\mathrm{tr}(B_1) = -(1 + h^2)$ and $\det(B_1) = 1$. -/
theorem stdBorromeanStep_trace_and_det (q : K) (hq : q ≠ 0) :
    Matrix.trace (stdBorromeanStep q) = -(1 + (heckeH q) ^ 2) ∧
    Matrix.det (stdBorromeanStep q) = 1 := by
  constructor
  · simp [stdBorromeanStep, stdGen0, stdGen1Inv, heckeH, Matrix.trace, Matrix.diag,
      Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  · simp [stdBorromeanStep, stdGen0, stdGen1Inv, Matrix.det_fin_two]
    field_simp [hq]
    ring

/-- **Cayley–Hamilton theorem for the 6-letter Borromean confinement core $\beta_{\mathrm{Bor}} = (\sigma_0 \sigma_1^{-1})^3$:**
    On the 2D standard representation $\lambda = (2,1)$ of $H_3(q)$,
    $$
      \rho_{(2,1)}\!\bigl((\sigma_0 \sigma_1^{-1})^3\bigr)
      = (1 + h^2)\,I_2 + h^2(h^2 + 2)\,\rho_{(2,1)}(\sigma_0 \sigma_1^{-1}).
    $$
    Consequently, at $q = 1$ ($h = 0$), the Borromean core acts as the identity matrix $I_2$. -/
theorem borromeanCore_cayley_hamilton (q : K) (hq : q ≠ 0) :
    stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q =
      (1 + (heckeH q) ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) +
      ((heckeH q) ^ 2 * ((heckeH q) ^ 2 + 2)) • stdBorromeanStep q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdBorromeanStep, stdGen0, stdGen1Inv, heckeH, Matrix.mul_apply,
      Fin.sum_univ_two] <;>
    field_simp [hq] <;> ring

/-- **Standard character and Convention-D Markov trace of the bare 6-letter Borromean core $\beta_{\mathrm{Bor}}$:**
    $\chi_{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3 h^4 - h^6$ and
    $$
      \mathrm{tr}_M^{z_D}(\beta_{\mathrm{Bor}})
      = y_{(3)}^D(q)\cdot 1 + y_{(2,1)}^D(q)\,(2 - 3 h^4 - h^6)
      = \frac{4 + h^2 - 3 h^4 - h^6}{4 + h^2}.
    $$ -/
theorem trM_borromeanCore_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hh4 : (heckeH q) ^ 2 + 4 ≠ 0) :
    Matrix.trace (stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q) =
      2 - 3 * (heckeH q) ^ 4 - (heckeH q) ^ 6 ∧
    yThreeD q * 1 + yTwoOneD q * (2 - 3 * (heckeH q) ^ 4 - (heckeH q) ^ 6) =
      (4 + (heckeH q) ^ 2 - 3 * (heckeH q) ^ 4 - (heckeH q) ^ 6) /
        ((heckeH q) ^ 2 + 4) := by
  constructor
  · rw [borromeanCore_cayley_hamilton q hq]
    simp [Matrix.trace, Matrix.diag, Fin.sum_univ_two, stdBorromeanStep, stdGen0,
      stdGen1Inv, heckeH]
    field_simp [hq]
    ring
  · obtain ⟨hy3, hy21⟩ := wenzlD_weights_eq_heckeH q hq hq2 hh4
    rw [hy3, hy21]
    field_simp [hh4]
    ring

/-! ### Exact Characters and Convention-D Rational Closed Forms for the 11-Letter Canonical Proton and Neutron (`qou-nzp3`) -/

/-- The 1D trivial representation character $\chi_{(3)}$ of the 11-letter proton element
    (identical for `borromean` and `grouped` orderings since 1D representations are commutative):
    $\chi_{(3)}(p) = q^6 \cdot (q - h/2)^2 \cdot q^{-3} = q(q^2 + 1)^2 / 4$. -/
def chiThreeProton (q : K) : K :=
  q ^ 6 * (q - heckeH q / 2) ^ 2 * (1 / q) ^ 3

/-- The 1D trivial representation character $\chi_{(3)}$ of the 11-letter neutron element:
    $\chi_{(3)}(n) = q^5 \cdot (q - h/2)^2 \cdot q^{-4} = (q^2 + 1)^2 / (4q)$. -/
def chiThreeNeutron (q : K) : K :=
  q ^ 5 * (q - heckeH q / 2) ^ 2 * (1 / q) ^ 4

/-- The 1D sign representation character $\chi_{(1,1,1)}$ of the 11-letter proton element:
    $\chi_{(1,1,1)}(p) = (-q^{-1})^6 \cdot (-q^{-1} - h/2)^2 \cdot (-q)^3 = -(q^2 + 1)^2 / (4q^5)$. -/
def chiOneOneOneProton (q : K) : K :=
  (-(1 / q)) ^ 6 * (-(1 / q) - heckeH q / 2) ^ 2 * (-q) ^ 3

/-- The 1D sign representation character $\chi_{(1,1,1)}$ of the 11-letter neutron element:
    $\chi_{(1,1,1)}(n) = (-q^{-1})^5 \cdot (-q^{-1} - h/2)^2 \cdot (-q)^4 = -(q^2 + 1)^2 / (4q^3)$. -/
def chiOneOneOneNeutron (q : K) : K :=
  (-(1 / q)) ^ 5 * (-(1 / q) - heckeH q / 2) ^ 2 * (-q) ^ 4

/-- **Closed form of the 1D trivial character $\chi_{(3)}$ and its weighted Convention-D contribution:**
    $\chi_{(3)}(p) = q(q^2 + 1)^2 / 4 = q^3 (h^2 + 4) / 4$ and
    $\chi_{(3)}(n) = (q^2 + 1)^2 / (4q) = q (h^2 + 4) / 4$, so the $(q^2 + 1)^2$ denominator
    of $y_{(3)}^D(q) = (q^4 + 1)/(q^2 + 1)^2$ cancels identically in $y_{(3)}^D \chi_{(3)}$. -/
theorem yThreeD_mul_chiThree_nucleons (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    chiThreeProton q = q * (q ^ 2 + 1) ^ 2 / 4 ∧
    chiThreeNeutron q = (q ^ 2 + 1) ^ 2 / (4 * q) ∧
    yThreeD q * chiThreeProton q = q * (q ^ 4 + 1) / 4 ∧
    yThreeD q * chiThreeNeutron q = (q ^ 4 + 1) / (4 * q) := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold chiThreeProton heckeH; field_simp [hq]; ring
  · unfold chiThreeNeutron heckeH; field_simp [hq]; ring
  · unfold yThreeD chiThreeProton heckeH; field_simp [hq, hq2, hsq]; ring
  · unfold yThreeD chiThreeNeutron heckeH; field_simp [hq, hq2, hsq]; ring

/-- The intra-nucleon color-averaged generator matrix
    $\rho_{(2,1)}(\sigma_0 - \tfrac{h}{2}\mathbf{1}) = \rho_{(2,1)}(\sigma_0) - \tfrac{h(q)}{2} I_2$. -/
def stdGen0Avg (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen0 q - (heckeH q / 2) • (1 : Matrix (Fin 2) (Fin 2) K)

/-- The intra-nucleon color-averaged generator matrix
    $\rho_{(2,1)}(\sigma_1 - \tfrac{h}{2}\mathbf{1}) = \rho_{(2,1)}(\sigma_1) - \tfrac{h(q)}{2} I_2$. -/
def stdGen1Avg (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen1 q - (heckeH q / 2) • (1 : Matrix (Fin 2) (Fin 2) K)

/-- The 5-letter canonical alternating (`borromean`) proton valence tail matrix
    $Q_p(q) = \rho_{(2,1)}\!\bigl(\sigma_0 (\sigma_0 - \tfrac{h}{2}) (\sigma_1 - \tfrac{h}{2}) \sigma_0^2\bigr)$
    in the 2D standard representation $\lambda = (2,1)$ of $H_3(q)$. -/
def stdProtonTail (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen0 q * stdGen0Avg q * stdGen1Avg q * (stdGen0 q * stdGen0 q)

/-- The 5-letter canonical alternating (`borromean`) neutron valence tail matrix
    $Q_n(q) = \rho_{(2,1)}\!\bigl((\sigma_0 - \tfrac{h}{2})^2 \sigma_1^{-1} \sigma_0^2\bigr)$
    in the 2D standard representation $\lambda = (2,1)$ of $H_3(q)$. -/
def stdNeutronTail (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen0Avg q * stdGen0Avg q * stdGen1Inv q * (stdGen0 q * stdGen0 q)

/-- The 7-letter $\sigma_0$-block matrix of the historical `grouped` proton word
    $X_{p,0}(q) = \rho_{(2,1)}\!\bigl(\sigma_0^4 (\sigma_0 - \tfrac{h}{2}) \sigma_0^2\bigr)$. -/
def stdProtonGroupedG0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  (stdGen0 q * stdGen0 q) * (stdGen0 q * stdGen0 q) * stdGen0Avg q * (stdGen0 q * stdGen0 q)

/-- The 4-letter $\sigma_1$-block matrix of the historical `grouped` proton word
    $X_{p,1}(q) = \rho_{(2,1)}\!\bigl((\sigma_1^{-1})^3 (\sigma_1 - \tfrac{h}{2})\bigr)$. -/
def stdProtonGroupedG1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen1Inv q * stdGen1Inv q * stdGen1Inv q * stdGen1Avg q

/-- The 7-letter $\sigma_0$-block matrix of the historical `grouped` neutron word
    $X_{n,0}(q) = \rho_{(2,1)}\!\bigl(\sigma_0^3 (\sigma_0 - \tfrac{h}{2})^2 \sigma_0^2\bigr)$. -/
def stdNeutronGroupedG0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  (stdGen0 q * stdGen0 q) * stdGen0 q * stdGen0Avg q * stdGen0Avg q * (stdGen0 q * stdGen0 q)

/-- The 4-letter $\sigma_1$-block matrix of the historical `grouped` neutron word
    $X_{n,1}(q) = \rho_{(2,1)}\!\bigl((\sigma_1^{-1})^4\bigr)$. -/
def stdNeutronGroupedG1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  stdGen1Inv q * stdGen1Inv q * stdGen1Inv q * stdGen1Inv q

/-- The 2D standard character $\chi_{(2,1)}(p_{\mathrm{Bor}})$ of the 11-letter canonical
    alternating (`borromean`) proton element $p_{\mathrm{Bor}} = \beta_{\mathrm{Bor}}\,Q_p$,
    derived via the Cayley–Hamilton decomposition
    $\chi_{(2,1)}(\beta_{\mathrm{Bor}} Q_p) = (1 + h^2)\,\mathrm{tr}(Q_p) + h^2(h^2 + 2)\,\mathrm{tr}(B_1 Q_p)$
    with $\mathrm{tr}(Q_p) = -h(h^2 + 2)(h^2 + 3)/4$ and
    $\mathrm{tr}(B_1 Q_p) = h(h^2 + 3)(h^4 + 3h^2 + 4)/4$. -/
def chiTwoOneProtonBorromean (q : K) : K :=
  let h := heckeH q
  (1 + h ^ 2) * (-h * (h ^ 2 + 2) * (h ^ 2 + 3) / 4) +
    h ^ 2 * (h ^ 2 + 2) * (h * (h ^ 2 + 3) * (h ^ 4 + 3 * h ^ 2 + 4) / 4)

/-- The 2D standard character $\chi_{(2,1)}(n_{\mathrm{Bor}})$ of the 11-letter canonical
    alternating (`borromean`) neutron element $n_{\mathrm{Bor}} = \beta_{\mathrm{Bor}}\,Q_n$,
    derived via the Cayley–Hamilton decomposition
    $\chi_{(2,1)}(\beta_{\mathrm{Bor}} Q_n) = (1 + h^2)\,\mathrm{tr}(Q_n) + h^2(h^2 + 2)\,\mathrm{tr}(B_1 Q_n)$
    with $\mathrm{tr}(Q_n) = -h(h^2 + 2)(h^2 + 4)/4$ and
    $\mathrm{tr}(B_1 Q_n) = h(h^2 + 4)(h^2 + 2)^2 / 4$. -/
def chiTwoOneNeutronBorromean (q : K) : K :=
  let h := heckeH q
  (1 + h ^ 2) * (-h * (h ^ 2 + 2) * (h ^ 2 + 4) / 4) +
    h ^ 2 * (h ^ 2 + 2) * (h * (h ^ 2 + 4) * (h ^ 2 + 2) ^ 2 / 4)

/-- The 2D standard character $\chi_{(2,1)}(p_{\mathrm{grp}})$ of the 11-letter historical
    `grouped` proton element $p_{\mathrm{grp}} = (a_{p,0}\sigma_0 + b_{p,0}\mathbf{1})(a_{p,1}\sigma_1 + b_{p,1}\mathbf{1})$,
    evaluated from $\chi_{(2,1)}((a_0\sigma_0 + b_0)(a_1\sigma_1 + b_1)) = -a_0 a_1 + h(a_0 b_1 + b_0 a_1) + 2 b_0 b_1$. -/
def chiTwoOneProtonGrouped (q : K) : K :=
  let h := heckeH q
  let a0 := (h ^ 2 + 2) * (h ^ 4 + 4 * h ^ 2 + 1) / 2
  let b0 := h * (h ^ 4 + 5 * h ^ 2 + 5) / 2
  let a1 := -h * (h ^ 2 + 3) / 2
  let b1 := (h ^ 4 + 4 * h ^ 2 + 2) / 2
  (-a0) * a1 + h * (a0 * b1 + b0 * a1) + 2 * b0 * b1

/-- The 2D standard character $\chi_{(2,1)}(n_{\mathrm{grp}})$ of the 11-letter historical
    `grouped` neutron element $n_{\mathrm{grp}} = (a_{n,0}\sigma_0 + b_{n,0}\mathbf{1})(a_{n,1}\sigma_1 + b_{n,1}\mathbf{1})$. -/
def chiTwoOneNeutronGrouped (q : K) : K :=
  let h := heckeH q
  let a0 := (h ^ 2 + 4) * (h ^ 4 + 3 * h ^ 2 + 1) / 4
  let b0 := h * (h ^ 2 + 4) * (h ^ 2 + 2) / 4
  let a1 := -h * (h ^ 2 + 2)
  let b1 := h ^ 4 + 3 * h ^ 2 + 1
  (-a0) * a1 + h * (a0 * b1 + b0 * a1) + 2 * b0 * b1

/-- **Quadratic identities for the color-averaged and inverse generators on $\rho_{(2,1)}$:**
    1. $(\sigma_0 - \tfrac{h}{2})^2 = \tfrac{h^2 + 4}{4}\,I_2$,
    2. $\sigma_0 (\sigma_0 - \tfrac{h}{2}) = \tfrac{h}{2}\,\sigma_0 + I_2$,
    3. $(\sigma_1^{-1})^2 = -h\,\sigma_1^{-1} + I_2$,
    4. $\sigma_1^{-1} (\sigma_1 - \tfrac{h}{2}) = -\tfrac{h}{2}\,\sigma_1^{-1} + I_2$. -/
theorem stdGen_avg_and_inv_quadratic (q : K) (hq : q ≠ 0) :
    stdGen0Avg q * stdGen0Avg q =
      (((heckeH q) ^ 2 + 4) / 4) • (1 : Matrix (Fin 2) (Fin 2) K) ∧
    stdGen0 q * stdGen0Avg q =
      (heckeH q / 2) • stdGen0 q + (1 : Matrix (Fin 2) (Fin 2) K) ∧
    stdGen1Inv q * stdGen1Inv q =
      (-heckeH q) • stdGen1Inv q + (1 : Matrix (Fin 2) (Fin 2) K) ∧
    stdGen1Inv q * stdGen1Avg q =
      (-heckeH q / 2) • stdGen1Inv q + (1 : Matrix (Fin 2) (Fin 2) K) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [stdGen0Avg, stdGen0, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [stdGen0Avg, stdGen0, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [stdGen1Inv, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [stdGen1Inv, stdGen1Avg, stdGen1, heckeH, -Matrix.cons_mul, Matrix.mul_apply,
        Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring

/-- **Explicit $2\times 2$ Matrix-Product Derivation of the 11-Letter Borromean Characters:**
    Proves directly from the $2\times 2$ matrix representation $\rho_{(2,1)}$ that the
    5-letter proton and neutron valence tails $Q_p, Q_n$ satisfy
    $\mathrm{tr}(Q_p) = -h(h^2+2)(h^2+3)/4$,
    $\mathrm{tr}(B_1 Q_p) = h(h^2+3)(h^4+3h^2+4)/4$,
    $\mathrm{tr}(Q_n) = -h(h^2+2)(h^2+4)/4$,
    $\mathrm{tr}(B_1 Q_n) = h(h^2+4)(h^2+2)^2/4$,
    and hence by `borromeanCore_cayley_hamilton` that the full 11-letter matrix products
    $\beta_{\mathrm{Bor}} Q_p$ and $\beta_{\mathrm{Bor}} Q_n$ have traces equal to
    `chiTwoOneProtonBorromean q` and `chiTwoOneNeutronBorromean q`. -/
theorem chiTwoOne_borromean_eq_matrix_trace (q : K) (hq : q ≠ 0) :
    let h := heckeH q
    let core := stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q
    Matrix.trace (stdProtonTail q) = -h * (h ^ 2 + 2) * (h ^ 2 + 3) / 4 ∧
    Matrix.trace (stdBorromeanStep q * stdProtonTail q) =
      h * (h ^ 2 + 3) * (h ^ 4 + 3 * h ^ 2 + 4) / 4 ∧
    Matrix.trace (core * stdProtonTail q) = chiTwoOneProtonBorromean q ∧
    Matrix.trace (stdNeutronTail q) = -h * (h ^ 2 + 2) * (h ^ 2 + 4) / 4 ∧
    Matrix.trace (stdBorromeanStep q * stdNeutronTail q) =
      h * (h ^ 2 + 4) * (h ^ 2 + 2) ^ 2 / 4 ∧
    Matrix.trace (core * stdNeutronTail q) = chiTwoOneNeutronBorromean q := by
  obtain ⟨havg_sq, h0_avg, _, _⟩ := stdGen_avg_and_inv_quadratic q hq
  have hqp :
      Matrix.trace (stdProtonTail q) =
        -(heckeH q) * ((heckeH q) ^ 2 + 2) * ((heckeH q) ^ 2 + 3) / 4 := by
    unfold stdProtonTail
    rw [h0_avg, stdGen0_sq_eq q hq]
    simp [stdGen0, stdGen1Avg, stdGen1, heckeH, -Matrix.cons_mul, Matrix.trace, Matrix.diag,
      Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  have hbp :
      Matrix.trace (stdBorromeanStep q * stdProtonTail q) =
        (heckeH q) * ((heckeH q) ^ 2 + 3) * ((heckeH q) ^ 4 + 3 * (heckeH q) ^ 2 + 4) / 4 := by
    unfold stdProtonTail
    rw [h0_avg, stdGen0_sq_eq q hq]
    simp [stdBorromeanStep, stdGen0, stdGen1Inv, stdGen1Avg, stdGen1, heckeH, -Matrix.cons_mul,
      Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  have hcp :
      Matrix.trace ((stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q) *
        stdProtonTail q) = chiTwoOneProtonBorromean q := by
    have hmul :
        (stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q) * stdProtonTail q =
          (1 + (heckeH q) ^ 2) • stdProtonTail q +
            ((heckeH q) ^ 2 * ((heckeH q) ^ 2 + 2)) • (stdBorromeanStep q * stdProtonTail q) := by
      rw [borromeanCore_cayley_hamilton q hq, Matrix.add_mul, Matrix.smul_mul,
        Matrix.smul_mul, Matrix.one_mul]
    rw [hmul, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, hqp, hbp]
    unfold chiTwoOneProtonBorromean
    simp [smul_eq_mul]
  have hqn :
      Matrix.trace (stdNeutronTail q) =
        -(heckeH q) * ((heckeH q) ^ 2 + 2) * ((heckeH q) ^ 2 + 4) / 4 := by
    unfold stdNeutronTail
    rw [havg_sq, stdGen0_sq_eq q hq]
    simp [stdGen0, stdGen1Inv, heckeH, -Matrix.cons_mul, Matrix.trace, Matrix.diag,
      Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  have hbn :
      Matrix.trace (stdBorromeanStep q * stdNeutronTail q) =
        (heckeH q) * ((heckeH q) ^ 2 + 4) * ((heckeH q) ^ 2 + 2) ^ 2 / 4 := by
    unfold stdNeutronTail
    rw [havg_sq, stdGen0_sq_eq q hq]
    simp [stdBorromeanStep, stdGen0, stdGen1Inv, heckeH, -Matrix.cons_mul,
      Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  have hcn :
      Matrix.trace ((stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q) *
        stdNeutronTail q) = chiTwoOneNeutronBorromean q := by
    have hmul :
        (stdBorromeanStep q * stdBorromeanStep q * stdBorromeanStep q) * stdNeutronTail q =
          (1 + (heckeH q) ^ 2) • stdNeutronTail q +
            ((heckeH q) ^ 2 * ((heckeH q) ^ 2 + 2)) • (stdBorromeanStep q * stdNeutronTail q) := by
      rw [borromeanCore_cayley_hamilton q hq, Matrix.add_mul, Matrix.smul_mul,
        Matrix.smul_mul, Matrix.one_mul]
    rw [hmul, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, hqn, hbn]
    unfold chiTwoOneNeutronBorromean
    simp [smul_eq_mul]
  exact ⟨hqp, hbp, hcp, hqn, hbn, hcn⟩

/-- **Explicit $2\times 2$ Matrix-Product Derivation of the 11-Letter Grouped Characters:**
    Proves directly from the $2\times 2$ matrix representation $\rho_{(2,1)}$ that the
    11-letter grouped proton and neutron matrix products
    `stdProtonGroupedG0 q * stdProtonGroupedG1 q` and
    `stdNeutronGroupedG0 q * stdNeutronGroupedG1 q` have traces equal to
    `chiTwoOneProtonGrouped q` and `chiTwoOneNeutronGrouped q`. -/
theorem chiTwoOne_grouped_eq_matrix_trace (q : K) (hq : q ≠ 0) :
    Matrix.trace (stdProtonGroupedG0 q * stdProtonGroupedG1 q) = chiTwoOneProtonGrouped q ∧
    Matrix.trace (stdNeutronGroupedG0 q * stdNeutronGroupedG1 q) = chiTwoOneNeutronGrouped q := by
  obtain ⟨havg_sq, _, h1inv_sq, h1inv_avg⟩ := stdGen_avg_and_inv_quadratic q hq
  have hp0 :
      stdProtonGroupedG0 q =
        (((heckeH q) ^ 2 + 2) * ((heckeH q) ^ 4 + 4 * (heckeH q) ^ 2 + 1) / 2) • stdGen0 q +
          ((heckeH q) * ((heckeH q) ^ 4 + 5 * (heckeH q) ^ 2 + 5) / 2) •
            (1 : Matrix (Fin 2) (Fin 2) K) := by
    unfold stdProtonGroupedG0
    rw [stdGen0_sq_eq q hq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [stdGen0, stdGen0Avg, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  have hp1 :
      stdProtonGroupedG1 q =
        (-(heckeH q) * ((heckeH q) ^ 2 + 3) / 2) • stdGen1 q +
          (((heckeH q) ^ 4 + 4 * (heckeH q) ^ 2 + 2) / 2) •
            (1 : Matrix (Fin 2) (Fin 2) K) := by
    have hmul :
        stdProtonGroupedG1 q =
          (stdGen1Inv q * stdGen1Inv q) * (stdGen1Inv q * stdGen1Avg q) := by
      unfold stdProtonGroupedG1; noncomm_ring
    rw [hmul, h1inv_sq, h1inv_avg]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [stdGen1Inv, stdGen1, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  have hn0 :
      stdNeutronGroupedG0 q =
        (((heckeH q) ^ 2 + 4) * ((heckeH q) ^ 4 + 3 * (heckeH q) ^ 2 + 1) / 4) • stdGen0 q +
          ((heckeH q) * ((heckeH q) ^ 2 + 4) * ((heckeH q) ^ 2 + 2) / 4) •
            (1 : Matrix (Fin 2) (Fin 2) K) := by
    have hmul :
        stdNeutronGroupedG0 q =
          (stdGen0 q * stdGen0 q) * stdGen0 q * (stdGen0Avg q * stdGen0Avg q) *
            (stdGen0 q * stdGen0 q) := by
      unfold stdNeutronGroupedG0; noncomm_ring
    rw [hmul, havg_sq, stdGen0_sq_eq q hq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [stdGen0, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  have hn1 :
      stdNeutronGroupedG1 q =
        (-(heckeH q) * ((heckeH q) ^ 2 + 2)) • stdGen1 q +
          ((heckeH q) ^ 4 + 3 * (heckeH q) ^ 2 + 1) •
            (1 : Matrix (Fin 2) (Fin 2) K) := by
    have hmul :
        stdNeutronGroupedG1 q =
          (stdGen1Inv q * stdGen1Inv q) * (stdGen1Inv q * stdGen1Inv q) := by
      unfold stdNeutronGroupedG1; noncomm_ring
    rw [hmul, h1inv_sq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [stdGen1Inv, stdGen1, heckeH, -Matrix.cons_mul, Matrix.mul_apply, Fin.sum_univ_two] <;>
      field_simp [hq] <;> ring
  constructor
  · rw [hp0, hp1]
    unfold chiTwoOneProtonGrouped
    simp [stdGen0, stdGen1, heckeH, -Matrix.cons_mul, Matrix.trace, Matrix.diag,
      Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring
  · rw [hn0, hn1]
    unfold chiTwoOneNeutronGrouped
    simp [stdGen0, stdGen1, heckeH, -Matrix.cons_mul, Matrix.trace, Matrix.diag,
      Matrix.mul_apply, Fin.sum_univ_two]
    field_simp [hq]
    ring

/-- **Factored skein-polynomial forms of all four standard 2D nucleon characters:**
    1. $\chi_{(2,1)}(p_{\mathrm{Bor}}) = \tfrac{1}{4}\,h(h^2 + 2)(h^2 + 3)(h^6 + 3h^4 + 3h^2 - 1)$,
    2. $\chi_{(2,1)}(n_{\mathrm{Bor}}) = \tfrac{1}{4}\,h(h^2 + 2)(h^2 + 4)(h^6 + 4h^4 + 3h^2 - 1)$,
    3. $\chi_{(2,1)}(p_{\mathrm{grp}}) = \tfrac{1}{4}\,h(h^2 + 3)(h^4 + 4h^2 + 2)(h^4 + 5h^2 + 5)$,
    4. $\chi_{(2,1)}(n_{\mathrm{grp}}) = \tfrac{1}{4}\,h(h^2 + 4)(h^8 + 8h^6 + 22h^4 + 23h^2 + 7)$. -/
theorem chiTwoOne_nucleon_factored_heckeH (q : K) :
    let h := heckeH q
    chiTwoOneProtonBorromean q =
      h * (h ^ 2 + 2) * (h ^ 2 + 3) * (h ^ 6 + 3 * h ^ 4 + 3 * h ^ 2 - 1) / 4 ∧
    chiTwoOneNeutronBorromean q =
      h * (h ^ 2 + 2) * (h ^ 2 + 4) * (h ^ 6 + 4 * h ^ 4 + 3 * h ^ 2 - 1) / 4 ∧
    chiTwoOneProtonGrouped q =
      h * (h ^ 2 + 3) * (h ^ 4 + 4 * h ^ 2 + 2) * (h ^ 4 + 5 * h ^ 2 + 5) / 4 ∧
    chiTwoOneNeutronGrouped q =
      h * (h ^ 2 + 4) * (h ^ 8 + 8 * h ^ 6 + 22 * h ^ 4 + 23 * h ^ 2 + 7) / 4 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold chiTwoOneProtonBorromean; ring
  · unfold chiTwoOneNeutronBorromean; ring
  · unfold chiTwoOneProtonGrouped; ring
  · unfold chiTwoOneNeutronGrouped; ring

/-- Convention-D Jones–Markov trace of the 11-letter canonical alternating (`borromean`) proton:
    $\mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}}) = y_{(3)}^D(q)\,\chi_{(3)}(p) + y_{(2,1)}^D(q)\,\chi_{(2,1)}(p_{\mathrm{Bor}})$. -/
def trMProtonBorromean (q : K) : K :=
  yThreeD q * chiThreeProton q + yTwoOneD q * chiTwoOneProtonBorromean q

/-- Convention-D Jones–Markov trace of the 11-letter canonical alternating (`borromean`) neutron:
    $\mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}}) = y_{(3)}^D(q)\,\chi_{(3)}(n) + y_{(2,1)}^D(q)\,\chi_{(2,1)}(n_{\mathrm{Bor}})$. -/
def trMNeutronBorromean (q : K) : K :=
  yThreeD q * chiThreeNeutron q + yTwoOneD q * chiTwoOneNeutronBorromean q

/-- Convention-D Jones–Markov trace of the 11-letter historical `grouped` proton:
    $\mathrm{tr}_M^{z_D}(p_{\mathrm{grp}}) = y_{(3)}^D(q)\,\chi_{(3)}(p) + y_{(2,1)}^D(q)\,\chi_{(2,1)}(p_{\mathrm{grp}})$. -/
def trMProtonGrouped (q : K) : K :=
  yThreeD q * chiThreeProton q + yTwoOneD q * chiTwoOneProtonGrouped q

/-- Convention-D Jones–Markov trace of the 11-letter historical `grouped` neutron:
    $\mathrm{tr}_M^{z_D}(n_{\mathrm{grp}}) = y_{(3)}^D(q)\,\chi_{(3)}(n) + y_{(2,1)}^D(q)\,\chi_{(2,1)}(n_{\mathrm{grp}})$. -/
def trMNeutronGrouped (q : K) : K :=
  yThreeD q * chiThreeNeutron q + yTwoOneD q * chiTwoOneNeutronGrouped q

/-- **Theorem (`qou-nzp3` Primary Closed Form 1 — Canonical Alternating Proton Trace):**
    Under Convention D ($z_D = q^3/(q^2 + 1)$), the constituent per-$Z$ step
    $\mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})(q)$ on the canonical alternating (`borromean`)
    11-letter proton element has the exact rational closed form over $K(q)$:
    $$
      \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})(q)
      = \frac{(q^4 + 1)(q^{18} - 3q^{16} + 7q^{14} - 8q^{12} + 10q^{10} - 9q^8 + 10q^6 - 6q^4 + 3q^2 - 1)}
             {4 q^9 (q^2 + 1)^2}.
    $$
    At $q_{\mathrm{proton}} = 1.1099785827513808076$, this evaluates to
    $0.62932840220292191817$. -/
theorem trM_proton_borromean_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trMProtonBorromean q =
      (q ^ 4 + 1) *
        (q ^ 18 - 3 * q ^ 16 + 7 * q ^ 14 - 8 * q ^ 12 + 10 * q ^ 10 -
          9 * q ^ 8 + 10 * q ^ 6 - 6 * q ^ 4 + 3 * q ^ 2 - 1) /
        (4 * q ^ 9 * (q ^ 2 + 1) ^ 2) := by
  unfold trMProtonBorromean yThreeD yTwoOneD chiThreeProton chiTwoOneProtonBorromean heckeH
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Theorem (`qou-nzp3` Primary Closed Form 2 — Canonical Alternating Neutron Trace):**
    Under Convention D ($z_D = q^3/(q^2 + 1)$), the constituent per-$N$ step
    $\mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})(q)$ on the canonical alternating (`borromean`)
    11-letter neutron element has the exact Laurent-polynomial closed form over $K[q, q^{-1}]$
    (the $(q^2 + 1)^2$ denominator cancels completely):
    $$
      \mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})(q)
      = \frac{(q^4 + 1)(q^{14} - 3q^{12} + 4q^{10} - 4q^8 + 5q^6 - 4q^4 + 3q^2 - 1)}
             {4 q^9}.
    $$
    At $q_{\mathrm{proton}} = 1.1099785827513808076$, this evaluates to
    $0.47513351715568221251$. -/
theorem trM_neutron_borromean_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trMNeutronBorromean q =
      (q ^ 4 + 1) *
        (q ^ 14 - 3 * q ^ 12 + 4 * q ^ 10 - 4 * q ^ 8 + 5 * q ^ 6 -
          4 * q ^ 4 + 3 * q ^ 2 - 1) /
        (4 * q ^ 9) := by
  unfold trMNeutronBorromean yThreeD yTwoOneD chiThreeNeutron chiTwoOneNeutronBorromean heckeH
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Theorem (`qou-nzp3` Primary Closed Form 3 — Historical Grouped Proton Trace):**
    Under Convention D ($z_D = q^3/(q^2 + 1)$), the constituent proton trace on the
    historical `grouped` 11-letter word has the exact factored rational closed form:
    $$
      \mathrm{tr}_M^{z_D}(p_{\mathrm{grp}})(q)
      = \frac{(q^8 + q^4 + q^2 + 1)(q^{14} + q^{12} + q^{10} - 1)}
             {4 q^9 (q^2 + 1)^2}.
    $$
    At $q_{\mathrm{proton}} = 1.1099785827513808076$, this evaluates to
    $1.14575969245730086969$. -/
theorem trM_proton_grouped_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trMProtonGrouped q =
      (q ^ 8 + q ^ 4 + q ^ 2 + 1) * (q ^ 14 + q ^ 12 + q ^ 10 - 1) /
        (4 * q ^ 9 * (q ^ 2 + 1) ^ 2) := by
  unfold trMProtonGrouped yThreeD yTwoOneD chiThreeProton chiTwoOneProtonGrouped heckeH
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Theorem (`qou-nzp3` Primary Closed Form 4 — Historical Grouped Neutron Trace):**
    Under Convention D ($z_D = q^3/(q^2 + 1)$), the constituent neutron trace on the
    historical `grouped` 11-letter word has the exact factored Laurent-polynomial closed form:
    $$
      \mathrm{tr}_M^{z_D}(n_{\mathrm{grp}})(q)
      = \frac{(q^8 - q^6 + q ^ 4 + 1)(q^{10} + q^6 - q^4 + q^2 - 1)}
             {4 q^9}.
    $$
    At $q_{\mathrm{proton}} = 1.1099785827513808076$, this evaluates to
    $0.98774368811580957163$. -/
theorem trM_neutron_grouped_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trMNeutronGrouped q =
      (q ^ 8 - q ^ 6 + q ^ 4 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) /
        (4 * q ^ 9) := by
  unfold trMNeutronGrouped yThreeD yTwoOneD chiThreeNeutron chiTwoOneNeutronGrouped heckeH
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  field_simp [hq, hq2, hsq]
  ring

/-- **Theorem (`qou-nzp3` Full Per-$Z$ Step Closed Form):**
    Adding one proton and one positive $p$-$p$ interface $\sigma_g$ (Markov factor $z_D = q^3/(q^2 + 1)$)
    multiplies the full Convention-D atomic trace by the exact rational closed form:
    $$
      z_D(q)\cdot \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})(q)
      = \frac{(q^4 + 1)(q^{18} - 3q^{16} + 7q^{14} - 8q^{12} + 10q^{10} - 9q^8 + 10q^6 - 6q^4 + 3q^2 - 1)}
             {4 q^6 (q^2 + 1)^3},
    $$
    which evaluates at $q_{\mathrm{proton}}$ to $0.38558198434401969594$. -/
theorem trM_full_per_Z_step_borromean_eq (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovZD q * trMProtonBorromean q =
      (q ^ 4 + 1) *
        (q ^ 18 - 3 * q ^ 16 + 7 * q ^ 14 - 8 * q ^ 12 + 10 * q ^ 10 -
          9 * q ^ 8 + 10 * q ^ 6 - 6 * q ^ 4 + 3 * q ^ 2 - 1) /
        (4 * q ^ 6 * (q ^ 2 + 1) ^ 3) := by
  rw [trM_proton_borromean_eq_rational q hq hq2]
  unfold markovZD
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  have hcb : (q ^ 2 + 1) ^ 3 ≠ 0 := pow_ne_zero 3 hq2
  field_simp [hq, hq2, hsq, hcb]

/-- **Exact intra-nucleon ordering shift (`grouped` minus `borromean`) in terms of $h = q - q^{-1}$:**
    Because $\chi_{(3)}$ and $\chi_{(1,1,1)}$ are 1D commutative characters, the difference
    between the `grouped` and `borromean` traces comes purely from the 2D standard channel
    $\lambda = (2,1)$ and has all-positive polynomial coefficients in $h$:
    $$
      \mathrm{tr}_M^{z_D}(p_{\mathrm{grp}}) - \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})
      = \frac{h\,(h^2 + 3)(4 h^6 + 18 h^4 + 25 h^2 + 12)}{4 (h^2 + 4)},
    $$
    $$
      \mathrm{tr}_M^{z_D}(n_{\mathrm{grp}}) - \mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})
      = \frac{h\,(h^2 + 1)(h^2 + 3)(2 h^2 + 3)}{4}.
    $$ -/
theorem trM_grouped_sub_borromean_eq_heckeH (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hh4 : (heckeH q) ^ 2 + 4 ≠ 0) :
    let h := heckeH q
    trMProtonGrouped q - trMProtonBorromean q =
      h * (h ^ 2 + 3) * (4 * h ^ 6 + 18 * h ^ 4 + 25 * h ^ 2 + 12) /
        (4 * (h ^ 2 + 4)) ∧
    trMNeutronGrouped q - trMNeutronBorromean q =
      h * (h ^ 2 + 1) * (h ^ 2 + 3) * (2 * h ^ 2 + 3) / 4 := by
  have hy21 := (wenzlD_weights_eq_heckeH q hq hq2 hh4).2
  constructor
  · unfold trMProtonGrouped trMProtonBorromean
    have hsub :
        yThreeD q * chiThreeProton q + yTwoOneD q * chiTwoOneProtonGrouped q -
          (yThreeD q * chiThreeProton q + yTwoOneD q * chiTwoOneProtonBorromean q) =
        yTwoOneD q * (chiTwoOneProtonGrouped q - chiTwoOneProtonBorromean q) := by ring
    rw [hsub, hy21]
    unfold chiTwoOneProtonGrouped chiTwoOneProtonBorromean
    field_simp [hh4]
    ring
  · unfold trMNeutronGrouped trMNeutronBorromean
    have hsub :
        yThreeD q * chiThreeNeutron q + yTwoOneD q * chiTwoOneNeutronGrouped q -
          (yThreeD q * chiThreeNeutron q + yTwoOneD q * chiTwoOneNeutronBorromean q) =
        yTwoOneD q * (chiTwoOneNeutronGrouped q - chiTwoOneNeutronBorromean q) := by ring
    rw [hsub, hy21]
    unfold chiTwoOneNeutronGrouped chiTwoOneNeutronBorromean
    field_simp [hh4]
    ring

/-- **Exact isospin trace differences ($\mathrm{tr}_M^{z_D}(\text{proton}) - \mathrm{tr}_M^{z_D}(\text{neutron})$)
    in both intra-nucleon orderings:**
    1. On the `grouped` word:
       $$
         \mathrm{tr}_M^{z_D}(p_{\mathrm{grp}}) - \mathrm{tr}_M^{z_D}(n_{\mathrm{grp}})
         = \frac{(q^2 - 1)(q^4 + 1)(q^4 + 2q^2 + 2)}{4 q (q^2 + 1)^2},
       $$
    2. On the canonical alternating (`borromean`) word:
       $$
         \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}}) - \mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})
         = -\frac{(q^2 - 1)(q^4 + 1)(2q^{12} - 6q^{10} + 3q^8 - 6q^6 + 5q^4 - 5q^2 + 2)}
                 {4 q^7 (q^2 + 1)^2}.
       $$ -/
theorem trM_proton_sub_neutron_eq_rational (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trMProtonGrouped q - trMNeutronGrouped q =
      (q ^ 2 - 1) * (q ^ 4 + 1) * (q ^ 4 + 2 * q ^ 2 + 2) /
        (4 * q * (q ^ 2 + 1) ^ 2) ∧
    trMProtonBorromean q - trMNeutronBorromean q =
      -((q ^ 2 - 1) * (q ^ 4 + 1) *
        (2 * q ^ 12 - 6 * q ^ 10 + 3 * q ^ 8 - 6 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2)) /
        (4 * q ^ 7 * (q ^ 2 + 1) ^ 2) := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  constructor
  · rw [trM_proton_grouped_eq_rational q hq hq2, trM_neutron_grouped_eq_rational q hq hq2]
    field_simp [hq, hq2, hsq]
    ring
  · rw [trM_proton_borromean_eq_rational q hq hq2, trM_neutron_borromean_eq_rational q hq hq2]
    field_simp [hq, hq2, hsq]
    ring

/-- **Refutation of `conj:constit-factor-2q-minus-1` at $q = 1$ (`qou-nzp3` scope-(b) exclusion):**
    At the classical specialization $q = 1$, all four Convention-D nucleon traces
    ($p_{\mathrm{Bor}}, n_{\mathrm{Bor}}, p_{\mathrm{grp}}, n_{\mathrm{grp}}$) evaluate to
    $z_D(1) = 1/2$, whereas $2q - 1$ evaluates to $2(1) - 1 = 1 \neq 1/2$. -/
theorem trM_nucleons_at_q_eq_one_refute_two_q_sub_one :
    trMProtonBorromean (1 : K) = 1 / 2 ∧
    trMNeutronBorromean (1 : K) = 1 / 2 ∧
    trMProtonGrouped (1 : K) = 1 / 2 ∧
    trMNeutronGrouped (1 : K) = 1 / 2 ∧
    trMProtonBorromean (1 : K) ≠ 2 * (1 : K) - 1 ∧
    trMProtonGrouped (1 : K) ≠ 2 * (1 : K) - 1 := by
  have hp_bor : trMProtonBorromean (1 : K) = 1 / 2 := by
    unfold trMProtonBorromean yThreeD yTwoOneD chiThreeProton chiTwoOneProtonBorromean heckeH
    norm_num
  have hn_bor : trMNeutronBorromean (1 : K) = 1 / 2 := by
    unfold trMNeutronBorromean yThreeD yTwoOneD chiThreeNeutron chiTwoOneNeutronBorromean heckeH
    norm_num
  have hp_grp : trMProtonGrouped (1 : K) = 1 / 2 := by
    unfold trMProtonGrouped yThreeD yTwoOneD chiThreeProton chiTwoOneProtonGrouped heckeH
    norm_num
  have hn_grp : trMNeutronGrouped (1 : K) = 1 / 2 := by
    unfold trMNeutronGrouped yThreeD yTwoOneD chiThreeNeutron chiTwoOneNeutronGrouped heckeH
    norm_num
  refine ⟨hp_bor, hn_bor, hp_grp, hn_grp, ?_, ?_⟩
  · rw [hp_bor]; norm_num
  · rw [hp_grp]; norm_num

/-! ## Section 2: Mass-Endomorphism Tower `tr_M` vs. `tr_reg` and Classical vs. $q$-Deformed Weights (`qou-j11h`) -/

/-- Single-generator trivial channel $V^{\mathrm{sym}}(q, a, b) = a q + b$
    on $a \sigma_i + b \mathbf{1} \in \langle \sigma_i \rangle \subset H_3(q)$. -/
def vSymChannel (q a b : K) : K := a * q + b

/-- Single-generator sign channel $V^{\mathrm{alt}}(q, a, b) = -a q^{-1} + b$
    on $a \sigma_i + b \mathbf{1} \in \langle \sigma_i \rangle \subset H_3(q)$. -/
def vAltChannel (q a b : K) : K := -a * (1 / q) + b

/-- Single-generator standard / localized Convention-D Jones–Markov channel
    $V^{\mathrm{std}}(q, a, b) = z_D(q)\,a + b$ on $a \sigma_i + b \mathbf{1} \in \langle \sigma_i \rangle \subset H_3(q)$. -/
def vStdChannel (q a b : K) : K := markovZD q * a + b

/-- **Theorem (`qou-j11h` — $V^{\mathrm{std}}$ Is the Exact Localized Convention-D Jones–Markov Trace):**
    For any single-generator Hecke element $X_i = a \sigma_i + b \mathbf{1} \in H_3(q)$,
    its irreducible characters are $\chi_{(3)}(X_i) = a q + b$, $\chi_{(2,1)}(X_i) = a h(q) + 2 b$,
    and $\chi_{(1,1,1)}(X_i) = -a q^{-1} + b$, so its Convention-D Jones–Markov trace
    equals $V^{\mathrm{std}}(q, a, b) = z_D(q)\,a + b$. -/
theorem vStd_eq_wenzlD_markov_trace (q a b : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    yThreeD q * vSymChannel q a b +
      yTwoOneD q * (a * heckeH q + 2 * b) +
      yOneOneOneD * vAltChannel q a b =
    vStdChannel q a b := by
  have hid := wenzlD_norm_id q hq2
  have hgen := wenzlD_trace_gen q hq hq2
  unfold vSymChannel vAltChannel vStdChannel
  linear_combination a * hgen + b * hid

/-- **Theorem (`qou-j11h` — Grouped Whole-Word Convention-D Markov Trace Equals $V_0^{\mathrm{std}} \cdot V_1^{\mathrm{std}}$):**
    For the 11-letter historical `grouped` proton and neutron elements
    $X_0(\sigma_0)\,X_1(\sigma_1) \in H_3(q)$, the whole-word Convention-D Jones–Markov trace
    factors identically as the product of the per-generator standard channel volumes:
    $$
      \mathrm{tr}_M^{z_D}(p_{\mathrm{grp}})(q)
      = V_{p,0}^{\mathrm{std}}(q) \cdot V_{p,1}^{\mathrm{std}}(q),
      \qquad
      \mathrm{tr}_M^{z_D}(n_{\mathrm{grp}})(q)
      = V_{n,0}^{\mathrm{std}}(q) \cdot V_{n,1}^{\mathrm{std}}(q).
    $$ -/
theorem trM_grouped_eq_prod_vStd (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let h := heckeH q
    let vp0 := vStdChannel q ((h ^ 2 + 2) * (h ^ 4 + 4 * h ^ 2 + 1) / 2)
                             (h * (h ^ 4 + 5 * h ^ 2 + 5) / 2)
    let vp1 := vStdChannel q (-h * (h ^ 2 + 3) / 2)
                             ((h ^ 4 + 4 * h ^ 2 + 2) / 2)
    let vn0 := vStdChannel q ((h ^ 2 + 4) * (h ^ 4 + 3 * h ^ 2 + 1) / 4)
                             (h * (h ^ 2 + 4) * (h ^ 2 + 2) / 4)
    let vn1 := vStdChannel q (-h * (h ^ 2 + 2))
                             (h ^ 4 + 3 * h ^ 2 + 1)
    vp0 = (q ^ 14 + q ^ 12 + q ^ 10 - 1) / (2 * q ^ 5 * (q ^ 2 + 1)) ∧
    vp1 = (q ^ 8 + q ^ 4 + q ^ 2 + 1) / (2 * q ^ 4 * (q ^ 2 + 1)) ∧
    trMProtonGrouped q = vp0 * vp1 ∧
    vn0 = (q ^ 2 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) / (4 * q ^ 5) ∧
    vn1 = (q ^ 8 - q ^ 6 + q ^ 4 + 1) / (q ^ 4 * (q ^ 2 + 1)) ∧
    trMNeutronGrouped q = vn0 * vn1 := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  have hvp0 :
      vStdChannel q (((heckeH q) ^ 2 + 2) * ((heckeH q) ^ 4 + 4 * (heckeH q) ^ 2 + 1) / 2)
        ((heckeH q) * ((heckeH q) ^ 4 + 5 * (heckeH q) ^ 2 + 5) / 2) =
      (q ^ 14 + q ^ 12 + q ^ 10 - 1) / (2 * q ^ 5 * (q ^ 2 + 1)) := by
    unfold vStdChannel markovZD heckeH; field_simp [hq, hq2]; ring
  have hvp1 :
      vStdChannel q (-(heckeH q) * ((heckeH q) ^ 2 + 3) / 2)
        (((heckeH q) ^ 4 + 4 * (heckeH q) ^ 2 + 2) / 2) =
      (q ^ 8 + q ^ 4 + q ^ 2 + 1) / (2 * q ^ 4 * (q ^ 2 + 1)) := by
    unfold vStdChannel markovZD heckeH; field_simp [hq, hq2]; ring
  have hvn0 :
      vStdChannel q (((heckeH q) ^ 2 + 4) * ((heckeH q) ^ 4 + 3 * (heckeH q) ^ 2 + 1) / 4)
        ((heckeH q) * ((heckeH q) ^ 2 + 4) * ((heckeH q) ^ 2 + 2) / 4) =
      (q ^ 2 + 1) * (q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1) / (4 * q ^ 5) := by
    unfold vStdChannel markovZD heckeH; field_simp [hq, hq2]; ring
  have hvn1 :
      vStdChannel q (-(heckeH q) * ((heckeH q) ^ 2 + 2))
        ((heckeH q) ^ 4 + 3 * (heckeH q) ^ 2 + 1) =
      (q ^ 8 - q ^ 6 + q ^ 4 + 1) / (q ^ 4 * (q ^ 2 + 1)) := by
    unfold vStdChannel markovZD heckeH; field_simp [hq, hq2]; ring
  refine ⟨hvp0, hvp1, ?_, hvn0, hvn1, ?_⟩
  · rw [trM_proton_grouped_eq_rational q hq hq2, hvp0, hvp1]
    field_simp [hq, hq2, hsq]; ring
  · rw [trM_neutron_grouped_eq_rational q hq hq2, hvn0, hvn1]
    field_simp [hq, hq2]

/-- Normalized $q$-deformed Plancherel / Wedderburn 1D channel weight
    $\widetilde{w}_{(3)}(q) = \widetilde{w}_{(1,1,1)}(q) = \dfrac{1}{1 + [2]_q^2 + 1} = \dfrac{1}{h^2 + 6}$
    (since $[2]_q^2 = (q + q^{-1})^2 = h^2 + 4$ and the common denominator $[3]_q!$ cancels). -/
def plancherelWeight1DQ (q : K) : K :=
  1 / ((heckeH q) ^ 2 + 6)

/-- Normalized $q$-deformed Plancherel / Wedderburn 2D standard channel weight
    $\widetilde{w}_{(2,1)}(q) = \dfrac{[2]_q^2}{1 + [2]_q^2 + 1} = \dfrac{h^2 + 4}{h^2 + 6}$. -/
def plancherelWeight2DQ (q : K) : K :=
  ((heckeH q) ^ 2 + 4) / ((heckeH q) ^ 2 + 6)

/-- Classical ($q = 1$) regular-representation / Plancherel 1D channel weight
    $w_{(3)}^{\mathrm{cl}} = w_{(1,1,1)}^{\mathrm{cl}} = 1^2 / |S_3| = 1 / 6$. -/
def plancherelWeight1DCl : K := 1 / 6

/-- Classical ($q = 1$) regular-representation / Plancherel 2D standard channel weight
    $w_{(2,1)}^{\mathrm{cl}} = 2^2 / |S_3| = 4 / 6 = 2 / 3$. -/
def plancherelWeight2DCl : K := 2 / 3

/-- **Normalization and $q$-deformation shift of the Plancherel channel weights (`qou-j11h`):**
    1. $\widetilde{w}_{(3)}(q) + \widetilde{w}_{(2,1)}(q) + \widetilde{w}_{(1,1,1)}(q) = 1$,
    2. $\widetilde{w}_{(2,1)}(q) - w_{(2,1)}^{\mathrm{cl}} = \dfrac{h^2}{3(h^2 + 6)}$,
    3. $\widetilde{w}_{(3)}(q) - w_{(3)}^{\mathrm{cl}} = -\dfrac{h^2}{6(h^2 + 6)}$. -/
theorem plancherelQ_norm_and_shift (q : K) (hh6 : (heckeH q) ^ 2 + 6 ≠ 0) :
    plancherelWeight1DQ q + plancherelWeight2DQ q + plancherelWeight1DQ q = 1 ∧
    plancherelWeight2DQ q - plancherelWeight2DCl =
      (heckeH q) ^ 2 / (3 * ((heckeH q) ^ 2 + 6)) ∧
    plancherelWeight1DQ q - plancherelWeight1DCl =
      -(heckeH q) ^ 2 / (6 * ((heckeH q) ^ 2 + 6)) := by
  unfold plancherelWeight1DQ plancherelWeight2DQ plancherelWeight1DCl plancherelWeight2DCl
  refine ⟨?_, ?_, ?_⟩
  · field_simp [hh6]; ring
  · field_simp [hh6]; ring
  · field_simp [hh6]; ring

/-- Single-generator 3-channel additive Wedderburn volume $V^{\mathrm{full},q}(q, a, b)$
    using the $q$-deformed normalized Plancherel weights $\widetilde{w}_\lambda(q)$. -/
def vFullChannelQ (q a b : K) : K :=
  plancherelWeight1DQ q * vSymChannel q a b +
    plancherelWeight2DQ q * vStdChannel q a b +
    plancherelWeight1DQ q * vAltChannel q a b

/-- Single-generator 3-channel additive Wedderburn volume $V^{\mathrm{full,cl}}(q, a, b)$
    using the classical regular-representation weights $w_\lambda^{\mathrm{cl}} = (1/6, 2/3, 1/6)$. -/
def vFullChannelCl (q a b : K) : K :=
  plancherelWeight1DCl * vSymChannel q a b +
    plancherelWeight2DCl * vStdChannel q a b +
    plancherelWeight1DCl * vAltChannel q a b

/-- Genuine normalized classical regular-representation trace
    $\tau_{\mathrm{reg,cl}}(q, a, b) = \tfrac{1}{6}\chi_{(3)}(a\sigma_i + b) + \tfrac{2}{6}\chi_{(2,1)}(a\sigma_i + b) + \tfrac{1}{6}\chi_{(1,1,1)}(a\sigma_i + b)$
    on $a\sigma_i + b\mathbf{1} \in H_3(q)$, where $\chi_{(2,1)}(a\sigma_i + b) = a h(q) + 2 b$
    (distinct from $V^{\mathrm{full,cl}}$, which places $V^{\mathrm{std}} = z_D a + b$ in the middle slot). -/
def tauRegChannelCl (q a b : K) : K :=
  (1 / 6 : K) * vSymChannel q a b +
    (2 / 6 : K) * (a * heckeH q + 2 * b) +
    (1 / 6 : K) * vAltChannel q a b

/-- Effective Markov parameter $z_{\mathrm{full},q}(q) = \dfrac{q(q^4 + 2q^2 - 1)}{q^4 + 4q^2 + 1}$
    of the $q$-deformed 3-channel volume $V^{\mathrm{full},q}$. -/
def zEffectiveFullQ (q : K) : K :=
  q * (q ^ 4 + 2 * q ^ 2 - 1) / (q ^ 4 + 4 * q ^ 2 + 1)

/-- Effective Markov parameter $z_{\mathrm{full,cl}}(q) = \dfrac{5q^4 - 1}{6 q (q^2 + 1)}$
    of the classical-weight 3-channel volume $V^{\mathrm{full,cl}}$. -/
def zEffectiveFullCl (q : K) : K :=
  (5 * q ^ 4 - 1) / (6 * q * (q ^ 2 + 1))

/-- **Theorem (`qou-j11h` — Complete Reconciliation of `tr_M` (`vStd`), `vFullQ`, `vFullCl`, and `tauRegCl`):**
    Every single-generator trace functional on $a\sigma_i + b\mathbf{1} \in \langle \sigma_i \rangle \subset H_3(q)$
    reduces to the linear form $z_\star(q)\,a + b$:
    1. $V^{\mathrm{full},q}(q, a, b) = z_{\mathrm{full},q}(q)\,a + b$,
    2. $V^{\mathrm{full,cl}}(q, a, b) = z_{\mathrm{full,cl}}(q)\,a + b$,
    3. $\tau_{\mathrm{reg,cl}}(q, a, b) = \tfrac{1}{2}\,h(q)\,a + b$ (which equals $b$ at $q = 1$),
    with the exact factored differences:
    4. $V^{\mathrm{full},q}(q, a, b) - V^{\mathrm{std}}(q, a, b)
       = -\dfrac{q(q^4 + 1)}{(q^2 + 1)(q^4 + 4q^2 + 1)}\,a$,
    5. $V^{\mathrm{full,cl}}(q, a, b) - V^{\mathrm{std}}(q, a, b)
       = -\dfrac{q^4 + 1}{6 q (q^2 + 1)}\,a$,
    6. $V^{\mathrm{full},q}(q, a, b) - V^{\mathrm{full,cl}}(q, a, b)
       = \dfrac{(q^2 - 1)^2 (q^4 + 1)}{6 q (q^2 + 1)(q^4 + 4q^2 + 1)}\,a$. -/
theorem mass_tower_channel_reconciliation (q a b : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + 4 * q ^ 2 + 1 ≠ 0) (hh6 : (heckeH q) ^ 2 + 6 ≠ 0) :
    vFullChannelQ q a b = zEffectiveFullQ q * a + b ∧
    vFullChannelCl q a b = zEffectiveFullCl q * a + b ∧
    tauRegChannelCl q a b = (heckeH q / 2) * a + b ∧
    vFullChannelQ q a b - vStdChannel q a b =
      -(q * (q ^ 4 + 1) / ((q ^ 2 + 1) * (q ^ 4 + 4 * q ^ 2 + 1))) * a ∧
    vFullChannelCl q a b - vStdChannel q a b =
      -((q ^ 4 + 1) / (6 * q * (q ^ 2 + 1))) * a ∧
    vFullChannelQ q a b - vFullChannelCl q a b =
      ((q ^ 2 - 1) ^ 2 * (q ^ 4 + 1) /
        (6 * q * (q ^ 2 + 1) * (q ^ 4 + 4 * q ^ 2 + 1))) * a := by
  have h1 : vFullChannelQ q a b = zEffectiveFullQ q * a + b := by
    have hsum :
        vFullChannelQ q a b =
          ((heckeH q + ((heckeH q) ^ 2 + 4) * markovZD q) / ((heckeH q) ^ 2 + 6)) * a + b := by
      have hsym_alt : vSymChannel q a b + vAltChannel q a b = a * heckeH q + 2 * b := by
        unfold vSymChannel vAltChannel heckeH; ring
      have hv :
          vFullChannelQ q a b =
            plancherelWeight1DQ q * (vSymChannel q a b + vAltChannel q a b) +
              plancherelWeight2DQ q * vStdChannel q a b := by
        unfold vFullChannelQ; ring
      rw [hv, hsym_alt]
      unfold plancherelWeight1DQ plancherelWeight2DQ vStdChannel
      field_simp [hh6]
      ring
    have hz :
        (heckeH q + ((heckeH q) ^ 2 + 4) * markovZD q) / ((heckeH q) ^ 2 + 6) =
          zEffectiveFullQ q := by
      unfold zEffectiveFullQ markovZD
      rw [div_eq_div_iff hh6 hq4]
      unfold heckeH
      field_simp [hq, hq2]
      ring
    rw [hsum, hz]
  have h2 : vFullChannelCl q a b = zEffectiveFullCl q * a + b := by
    unfold vFullChannelCl plancherelWeight1DCl plancherelWeight2DCl
      vSymChannel vStdChannel vAltChannel zEffectiveFullCl markovZD
    field_simp [hq, hq2]
    ring
  have h3 : tauRegChannelCl q a b = (heckeH q / 2) * a + b := by
    unfold tauRegChannelCl vSymChannel vAltChannel heckeH
    field_simp [hq]
    ring
  refine ⟨h1, h2, h3, ?_, ?_, ?_⟩
  · rw [h1]
    have hsub :
        zEffectiveFullQ q * a + b - vStdChannel q a b =
          (zEffectiveFullQ q - markovZD q) * a := by
      unfold vStdChannel; ring
    rw [hsub]
    congr 1
    unfold zEffectiveFullQ markovZD
    rw [div_sub_div _ _ hq4 hq2, ← neg_div]
    have hden1 : (q ^ 4 + 4 * q ^ 2 + 1) * (q ^ 2 + 1) ≠ 0 := mul_ne_zero hq4 hq2
    have hden2 : (q ^ 2 + 1) * (q ^ 4 + 4 * q ^ 2 + 1) ≠ 0 := mul_ne_zero hq2 hq4
    rw [div_eq_div_iff hden1 hden2]
    ring
  · rw [h2]
    have hsub :
        zEffectiveFullCl q * a + b - vStdChannel q a b =
          (zEffectiveFullCl q - markovZD q) * a := by
      unfold vStdChannel; ring
    rw [hsub]
    congr 1
    unfold zEffectiveFullCl markovZD
    field_simp [hq, hq2]
    ring
  · rw [h1, h2]
    have hsub :
        zEffectiveFullQ q * a + b - (zEffectiveFullCl q * a + b) =
          (zEffectiveFullQ q - zEffectiveFullCl q) * a := by ring
    rw [hsub]
    congr 1
    unfold zEffectiveFullQ zEffectiveFullCl
    have h6q : 6 * q * (q ^ 2 + 1) ≠ 0 := mul_ne_zero (mul_ne_zero (by norm_num) hq) hq2
    rw [div_sub_div _ _ hq4 h6q]
    have hden1 : (q ^ 4 + 4 * q ^ 2 + 1) * (6 * q * (q ^ 2 + 1)) ≠ 0 := mul_ne_zero hq4 h6q
    have hden2 : 6 * q * (q ^ 2 + 1) * (q ^ 4 + 4 * q ^ 2 + 1) ≠ 0 := mul_ne_zero h6q hq4
    rw [div_eq_div_iff hden1 hden2]
    ring

end FieldAlgebraic

/-! ## Section 3: Order-Tier Positivity & Two-Rival `α_EM` Conjecture Reconciliation (`qou-aemx`) -/

section RealArchimedean

open QOU.Archimedean
open QOU.Archimedean.BringSchwingerNormalizationDerivation

/-- **Strict positivity of the intra-nucleon ordering shift (`grouped` > `borromean`) for $q > 1$:**
    For every real $q > 1$, $h = q - q^{-1} > 0$, so both the proton and neutron
    Convention-D Markov traces are strictly larger on the historical `grouped` word
    than on the canonical alternating (`borromean`) word:
    $\mathrm{tr}_M^{z_D}(p_{\mathrm{grp}})(q) > \mathrm{tr}_M^{z_D}(p_{\mathrm{Bor}})(q)$ and
    $\mathrm{tr}_M^{z_D}(n_{\mathrm{grp}})(q) > \mathrm{tr}_M^{z_D}(n_{\mathrm{Bor}})(q)$. -/
theorem trM_grouped_gt_borromean_of_one_lt (q : ℝ) (hq : 1 < q) :
    trMProtonBorromean q < trMProtonGrouped q ∧
    trMNeutronBorromean q < trMNeutronGrouped q := by
  have hq0 : q ≠ 0 := by linarith
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hh_pos : 0 < heckeH q := by
    have hq_pos : 0 < q := by linarith
    have hq_sub : 0 < q - 1 := by linarith
    have hfac : heckeH q = (q - 1) * (q + 1) / q := by
      unfold heckeH; field_simp [hq0]; ring
    rw [hfac]
    positivity
  have hh4 : (heckeH q) ^ 2 + 4 ≠ 0 := by positivity
  obtain ⟨hp, hn⟩ := trM_grouped_sub_borromean_eq_heckeH q hq0 hq2 hh4
  constructor
  · rw [← sub_pos, hp]
    positivity
  · rw [← sub_pos, hn]
    positivity

/-- The classical limit ($q \to 1$) of the derived Layer-2/3 bare prefactor
    $T_{\mathrm{bare}}(q) = q\,[9]_q\,[10]_q$ is $1 \cdot 9 \cdot 10 = 90$. -/
def emBarePrefactorClassicalLimit : ℝ := 1 * 9 * 10

/-- The classical limit ($q \to 1$) of the superseded PSLQ gluon-octet prefactor
    $45\,[3]_q$ is $45 \cdot 3 = 135$. -/
def gluonOctetPrefactorClassicalLimit : ℝ := 45 * 3

/-- **Theorem (`qou-aemx` — Algebraic Incompatibility of the Two Rival Prefactors):**
    The derived Layer-2/3 bare prefactor $T_{\mathrm{bare}}(q) = q\,[9]_q\,[10]_q$
    and the superseded gluon-octet prefactor $45\,[3]_q$ have distinct classical limits
    at $q = 1$ ($90 \neq 135$, with exact ratio $2 : 3$), proving that the two formulas
    do not share a common tree-level prefactor under any reparametrization of $\kappa$. -/
theorem emBarePrefactor_classical_ne_gluonOctet :
    emBarePrefactorClassicalLimit ≠ gluonOctetPrefactorClassicalLimit ∧
    gluonOctetPrefactorClassicalLimit / emBarePrefactorClassicalLimit = 3 / 2 := by
  unfold emBarePrefactorClassicalLimit gluonOctetPrefactorClassicalLimit
  constructor <;> norm_num

/-- Chern–Simons invariant $\mathrm{CS}(T_{m,n}) = \pi^2 (m^2 - 1)(n^2 - 1) / (12 m n)$
    of the torus knot $T_{m,n}$. -/
noncomputable def torusChernSimons (m n : ℕ) : ℝ :=
  Real.pi ^ 2 * (((m : ℝ) ^ 2 - 1) * ((n : ℝ) ^ 2 - 1)) / (12 * (m : ℝ) * (n : ℝ))

/-- **Exact rational-multiple-of-$\pi^2$ evaluation of the force-carrier Chern–Simons sum:**
    $$
      \mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})
      = \frac{10\,\pi^2}{9} + \frac{16\,\pi^2}{15}
      = \frac{98\,\pi^2}{45}.
    $$ -/
theorem forceCarrier_chernSimons_sum_eq :
    torusChernSimons 2 9 = 10 * Real.pi ^ 2 / 9 ∧
    torusChernSimons 3 5 = 16 * Real.pi ^ 2 / 15 ∧
    torusChernSimons 2 9 + torusChernSimons 3 5 = 98 * Real.pi ^ 2 / 45 := by
  unfold torusChernSimons
  refine ⟨by ring, by ring, by ring⟩

/-- The additive Chern–Simons numerator shift
    $\Delta_{\mathrm{CS}}(q) := (\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5}))\cdot \frac{q + q^{-1}}{2}\cdot (1 - q^{-1})^2
    = \frac{49\,\pi^2}{45}\,(q + q^{-1})\,(1 - q^{-1})^2$, which is independent of the bare
    prefactor $T_{\mathrm{bare}}(q)$. -/
noncomputable def deltaCSAdditive (q : ℝ) : ℝ :=
  (torusChernSimons 2 9 + torusChernSimons 3 5) * ((q + q⁻¹) / 2) * (hbarQ q) ^ 2

/-- **Additive Decomposition of the Resummed Chern–Simons Formula (`qou-aemx`):**
    For any bare prefactor $T_{\mathrm{bare}} \neq 0$ and relative correction
    $\delta_{\mathrm{CS}} = \Delta_{\mathrm{CS}} / T_{\mathrm{bare}}$, the multiplicative
    resummed Chern–Simons expression $T_{\mathrm{bare}}\cdot (1 + \delta_{\mathrm{CS}} / (1 - \kappa\,\delta_{\mathrm{CS}}))$
    rewrites identically into the additive shift form:
    $$
      T_{\mathrm{bare}} \cdot \Bigl(1 + \frac{\delta_{\mathrm{CS}}}{1 - \kappa\,\delta_{\mathrm{CS}}}\Bigr)
      = T_{\mathrm{bare}} + \frac{\Delta_{\mathrm{CS}}}{1 - \kappa\,\delta_{\mathrm{CS}}}.
    $$ -/
theorem chernSimons_resummed_eq_bare_add_shift (T_bare Delta_CS κ : ℝ) (hT : T_bare ≠ 0) :
    let δ := Delta_CS / T_bare
    T_bare * (1 + δ / (1 - κ * δ)) = T_bare + Delta_CS / (1 - κ * δ) := by
  dsimp only
  by_cases hden : 1 - κ * (Delta_CS / T_bare) = 0
  · simp [hden]
  · field_simp [hT, hden]

/-- **Reconciliation Theorem between `conj:em-coupling-chern-simons` and
    `prop:em-coupling-bring-zero-mode` (`qou-aemx`):**
    Suppose $\alpha \neq 0$ satisfies the Bring–Schwinger fixed-point relation
    `IsUnifiedBringFixedPoint 1 T_bare 4 q c α` at Bring genus $G = 4$, i.e.
    $$
      \frac{1}{\alpha}
      = T_{\mathrm{bare}} + \frac{2}{3\pi} + \alpha \cdot \mathcal{H}(q) \cdot (1 - c\alpha).
    $$
    Then the live Chern–Simons resummed tower $T_{\mathrm{bare}} + \Delta_{\mathrm{CS}} / (1 - \kappa\,\delta_{\mathrm{CS}})$
    coincides with $1/\alpha$ **if and only if** the resummed Chern–Simons shift equals
    the tiling-derived Bring–Schwinger shift:
    $$
      \frac{\Delta_{\mathrm{CS}}}{1 - \kappa\,\delta_{\mathrm{CS}}}
      = \frac{2}{3\pi} + \alpha \cdot \mathcal{H}(q) \cdot (1 - c\alpha).
    $$ -/
theorem chernSimons_eq_bringSchwinger_iff_shift_eq
    (T_bare Delta_CS κ q c α : ℝ) (hT : T_bare ≠ 0)
    (hfp : IsUnifiedBringFixedPoint 1 T_bare 4 q c α) :
    let δ := Delta_CS / T_bare
    T_bare * (1 + δ / (1 - κ * δ)) = 1 / α ↔
      Delta_CS / (1 - κ * δ) =
        bringZeroModeValue + α * habiroNorm q * (1 - c * α) := by
  dsimp only
  rw [chernSimons_resummed_eq_bare_add_shift T_bare Delta_CS κ hT]
  unfold IsUnifiedBringFixedPoint at hfp
  have hzero : (2 * (4 : ℝ)) / bringSurfaceArea = bringZeroModeValue := by
    exact bring_group_homology_ratio_exact
  rw [hzero] at hfp
  rw [hfp]
  constructor <;> intro h <;> linarith

end RealArchimedean

end QOU.MassTheory.ConventionDProtonConstituentClosedForm
