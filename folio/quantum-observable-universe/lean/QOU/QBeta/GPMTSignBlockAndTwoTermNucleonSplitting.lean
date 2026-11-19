import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.Machinery.HeckeH3BlockRep
import QOU.Machinery.HeckeH3BlockCharacter
import QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-!
# First-Principles GPMT `(1,1,1)` Sign-Block & Two-Term QED Nucleon Splitting (`GPMTSignBlockAndTwoTermNucleonSplitting`)

Formalizes the exact representation-theoretic decomposition of the single-wrap neutron–proton
normal-form difference $\Delta = \frac{1}{2} h^2 \cdot 1 - \frac{1}{2} h (\sigma_0 + \sigma_1)$
and the 11-crossing reselected nucleon difference $\Delta_{\mathrm{resel}}$ across all three
Wedderburn–Specht blocks $(3)$, $(2,1)$, and $(1,1,1)$ of $H_3(q)$, together with the
Geer–Patureau-Mirand–Turaev (GPMT) modified-trace evaluation on the Convention-D killed sign
block $(1,1,1)$ and the Two-Term QCD + QED nucleon mass-splitting and $\mathfrak{Q}_\beta$
decomposition.

## Main Results

1. **Section 1 — Single-Wrap Typed Crossing Normal Forms & Exact $H_3(q)$ Wedderburn–Specht Decomposition of $\Delta$**:
   - Derives the single-wrap proton normal form $L_+ - \frac{h}{2}\sigma_0$ (`singleWrapProtonNF`)
     and single-wrap neutron normal form $L_+ - h\sigma_0 - \frac{h}{2}\sigma_1 + \frac{h^2}{2}\cdot 1$
     (`singleWrapNeutronNF`) directly via $H_3(q)$ multiplication `mulNF`, proving exact Hopf
     cancellation `singleWrapNeutronNF h - singleWrapProtonNF h = deltaSNF h`.
   - Proves the exact block eigenvalues and matrix action of $\Delta = \text{deltaSNF}(q - q^{-1})$:
     * On trivial $(3)$ ($\sigma_i \mapsto q$):
       $\Delta|_{(3)} = \frac{1}{2}h^2 - h q = -\frac{1}{2}(q^2 - q^{-2}) = -\frac{(q - q^{-1})(q + q^{-1})}{2} < 0$ for $q > 1$.
     * On standard 2D $(2,1)$ (`blockOf q (deltaSNF (q - q⁻¹))` in $M_2(K)$):
       **(a)** Exact trace vanishing $\mathrm{tr}_{(2,1)}(\Delta) = 0$ identically for all $q \neq 0$, $q^2 + 1 \neq 0$
       (`blockOf_deltaSNF_trace_eq_zero`);
       **(b)** Non-vanishing off-diagonal matrix action `(blockOf q (deltaSNF (q - q⁻¹))) 0 1 = -(q - q⁻¹)/2`
       (`blockOf_deltaSNF_offDiag_entry`);
       **(c)** Exact determinant $\det_{(2,1)}(\Delta) = -(q - q^{-1})^2 / 4$ and involutive square
       $(\Delta|_{(2,1)})^2 = \frac{(q - q^{-1})^2}{4} I_2$ (`blockOf_deltaSNF_det`, `blockOf_deltaSNF_sq`),
       establishing that $\Delta|_{(2,1)}$ has exact rational opposite eigenvalues $\pm \frac{q - q^{-1}}{2}$.
     * On antisymmetric sign $(1,1,1)$ ($\sigma_i \mapsto -q^{-1}$):
       $\Delta|_{(1,1,1)} = \frac{1}{2}h^2 + h q^{-1} = +\frac{1}{2}(q^2 - q^{-2}) > 0$ for $q > 1$.

2. **Section 2 — Bare Convention-D Trace vs. GPMT $(1,1,1)$ Sign-Block Functional on $\Delta$**:
   - Proves `trM_zD_deltaSNF_sole_trivial_origin`: because $\mathrm{tr}_{(2,1)}(\Delta) = 0$ by trace
     cancellation and $w_{(1,1,1)}(z_D) = 0$ by Temperley–Lieb truncation, $100\%$ of
     $\mathrm{tr}_{z_D}(\Delta)$ originates from $(3)$ alone, evaluating to
     $$\mathrm{tr}_{z_D}(\Delta) = \frac{1}{2}h^2 - h z_D(q) = -\frac{(q - q^{-1})(q^4 + 1)}{2 q (q^2 + 1)}.$$
   - Defines the GPMT sign-block trace functional $\tau_{\mathrm{GPMT}}^{(1^3)}(v) = |d_{\mathrm{mod}}(1,1,1)| \cdot \chi_{(1,1,1)}(v)$
     and proves its exact rational closed forms on $\Delta$:
     $$\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta) = \frac{q^3 (q^2 - q^{-2})}{2(q^2 + 1)(q^4 + q^2 + 1)}
       = \frac{q (q^2 - 1)}{2(q^4 + q^2 + 1)} > 0 \quad (q > 1),$$
     together with exact factored closed forms and strict real ordering for **both** coherent
     combinations $\mathrm{tr}_{z_D}(\Delta) \pm d_{\mathrm{mod}}(1,1,1)\Delta|_{(1,1,1)}$ (`trM_conventionD_gpmtSigned`
     and `trM_conventionD_gpmtPos`).

3. **Section 3 — Full Three-Block Decomposition & GPMT Sign-Block Boost on the 11-Crossing Reselected $\Delta_{\mathrm{resel}}$**:
   - Proves the exact factored $(2,1)$ character `chi21_nucleonDiffCoord` and GPMT $(1,1,1)$
     sign-block contribution `tauGPMT111_nucleonDiffCoord` on `nucleonDiffCoord`, showing that
     $\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta_{\mathrm{resel}}) = -\frac{(q^2 - 1)(q^2 + 1)}{4 q^2 (q^4 + q^2 + 1)} < 0$
     shares the exact negative sign of $\mathrm{tr}_{z_D}(\Delta_{\mathrm{resel}})$ for $q > 1$.

4. **Section 4 — Two-Term QCD + QED Nucleon Mass Splitting & $\mathfrak{Q}_\beta$ Decomposition**:
   - Proves the exact kinematic and two-term operator identities
     $\Delta m_{np} = m_e + \mathfrak{Q}_\beta$, $M_{\mathrm{2t}}(n) - M_{\mathrm{2t}}(p) = \Delta M_{\mathrm{QCD}} + \Delta M_{\mathrm{QED}}^{\mathrm{Bor}}$,
     and $\mathfrak{Q}_\beta^{\mathrm{2t}} = \mathfrak{Q}_\beta^{\mathrm{QCD}} + \Delta M_{\mathrm{QED}}^{\mathrm{Bor}} < \mathfrak{Q}_\beta^{\mathrm{QCD}}$
     for all real $q > 1$ and $m_e > 0$ via the 4th-order connected Borromean $V^3$ QED trace.

Compute companion: `computations/probes/gpmt_sign_block_qbeta_and_np_splitting_probe.py`
Witness: `computations/probes/gpmt-sign-block-qbeta-and-np-splitting.witness.json`
-/

namespace QOU.QBeta.GPMTSignBlockAndTwoTermNucleonSplitting

open Matrix
open QOU.Machinery.H3
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

-- ============================================================================
-- § 1. Single-Wrap Typed Crossing Normal Forms & Exact H_3(q) Specht Action
-- ============================================================================

section SingleWrapAndSpechtDecomposition

variable {K : Type*} [Field K]

/-- Single-wrap typed proton normal form $L_+ - \frac{h}{2}\sigma_0 = \sigma_0 (\sigma_1 - \frac{h}{2})$
in the 6-element $H_3(q)$ basis `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def singleWrapProtonNF (h : K) : Fin 6 → K :=
  ![0, -h / 2, 0, 0, 1, 0]

/-- Single-wrap typed neutron normal form
$L_+ - h\sigma_0 - \frac{h}{2}\sigma_1 + \frac{h^2}{2}\cdot 1 = (\sigma_0 - h)(\sigma_1 - \frac{h}{2})$
in the 6-element $H_3(q)$ basis `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def singleWrapNeutronNF (h : K) : Fin 6 → K :=
  ![h ^ 2 / 2, -h, -h / 2, 0, 1, 0]

/-- Exact $H_3(q)$ normal-form product derivation of the single-wrap proton element:
$\sigma_0 \cdot (\sigma_1 - \frac{h}{2}\cdot 1) = L_+ - \frac{h}{2}\sigma_0$. -/
theorem singleWrapProtonNF_eq_mulNF (h : K) :
    mulNF h ![0, 1, 0, 0, 0, 0] ![-h / 2, 0, 1, 0, 0, 0] = singleWrapProtonNF h := by
  ext i
  fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, singleWrapProtonNF]

/-- Exact $H_3(q)$ normal-form product derivation of the single-wrap neutron element:
$(\sigma_0 - \frac{h}{2}\cdot 1) \cdot (\sigma_1 - h\cdot 1) = \frac{h^2}{2}\cdot 1 - h\sigma_0 - \frac{h}{2}\sigma_1 + L_+$. -/
theorem singleWrapNeutronNF_eq_mulNF (h : K) :
    mulNF h ![-h / 2, 1, 0, 0, 0, 0] ![-h, 0, 1, 0, 0, 0] = singleWrapNeutronNF h := by
  ext i
  fin_cases i <;> (simp [mulNF, mulσ₀, mulσ₁, singleWrapNeutronNF]; try ring)

/-- **Hopf $L_+$ Cancellation in the Single-Wrap $(n - p)$ Difference**:
Subtracting `singleWrapProtonNF h` from `singleWrapNeutronNF h` cancels $L_+ = \sigma_0\sigma_1$
identically and yields $\Delta = \frac{h^2}{2}\cdot 1 - \frac{h}{2}(\sigma_0 + \sigma_1)$ (`deltaSNF h`). -/
theorem singleWrapNeutron_sub_proton_eq_deltaSNF [CharZero K] (h : K) :
    singleWrapNeutronNF h - singleWrapProtonNF h = deltaSNF h := by
  ext i
  fin_cases i <;> (simp [singleWrapNeutronNF, singleWrapProtonNF, deltaSNF]; try (field_simp; ring))

/-- **Trivial $(3)$ Block Eigenvalue of $\Delta$ ($\sigma_i \mapsto q$)**:
On the 1-dimensional trivial representation $(3)$ of $H_3(q)$,
$\Delta|_{(3)} = \frac{1}{2}(q - q^{-1})^2 - (q - q^{-1}) q = -\frac{1}{2}(q^2 - q^{-2}) = -\frac{(q - q^{-1})(q + q^{-1})}{2}$. -/
theorem deltaSNF_trivial_eigenvalue_forms [CharZero K] (q : K) (hq : q ≠ 0) :
    chi3 q (deltaSNF (q - q⁻¹)) = (q - q⁻¹) ^ 2 / 2 - (q - q⁻¹) * q ∧
    (q - q⁻¹) ^ 2 / 2 - (q - q⁻¹) * q = -(q ^ 2 - q⁻¹ ^ 2) / 2 ∧
    -(q ^ 2 - q⁻¹ ^ 2) / 2 = -(q - q⁻¹) * (q + q⁻¹) / 2 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [chi3_deltaSNF q hq two_ne_zero]
    field_simp
    ring
  · field_simp
    ring
  · field_simp
    ring

/-- **Exact Trace Vanishing of $\Delta$ on the 2D Mixed-Symmetry Nucleon Block $(2,1)$**:
Evaluated directly on the explicit $2 \times 2$ Hoefsmit seminormal representation
`blockOf q (deltaSNF (q - q⁻¹))` of $H_3(q)$, $\mathrm{tr}_{(2,1)}(\Delta) = 0$ identically
for all $q \neq 0$ with $q^2 + 1 \neq 0$, because $\mathrm{tr}(I_2) = 2$ and
$\mathrm{tr}(S_0) = \mathrm{tr}(S_1) = q - q^{-1} = h$ give
$\frac{1}{2} h^2 (2) - \frac{1}{2} h (h + h) = 0$. -/
theorem blockOf_deltaSNF_trace_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (blockOf q (deltaSNF (q - q⁻¹))).trace = 0 := by
  simp [blockOf, deltaSNF, S0, S1, Matrix.trace_fin_two]
  field_simp
  ring

/-- **Non-Vanishing Matrix Action of $\Delta$ on $(2,1)$**:
Although $\mathrm{tr}_{(2,1)}(\Delta) = 0$, the matrix `blockOf q (deltaSNF (q - q⁻¹))` is
non-zero for $q \neq \pm 1$: its $(0,1)$ entry equals $-(q - q^{-1})/2$. -/
theorem blockOf_deltaSNF_offDiag_entry (q : K) :
    blockOf q (deltaSNF (q - q⁻¹)) 0 1 = -(q - q⁻¹) / 2 := by
  simp [blockOf, deltaSNF, S0, S1]

/-- **Exact Determinant of $\Delta$ on the 2D $(2,1)$ Block**:
$\det(\Delta|_{(2,1)}) = -(q - q^{-1})^2 / 4$, showing that $\Delta|_{(2,1)}$ has exact
opposite rational eigenvalues $+\frac{1}{2}(q - q^{-1})$ and $-\frac{1}{2}(q - q^{-1})$. -/
theorem blockOf_deltaSNF_det [CharZero K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (blockOf q (deltaSNF (q - q⁻¹))).det = -((q - q⁻¹) ^ 2) / 4 := by
  simp [blockOf, deltaSNF, S0, S1, Matrix.det_fin_two]
  field_simp
  ring

/-- **Scalar Square Identity on the 2D $(2,1)$ Block**:
$(\Delta|_{(2,1)})^2 = \frac{(q - q^{-1})^2}{4} I_2$, confirming algebraically that the two
eigenvalues of $\Delta$ on $(2,1)$ are $\pm \frac{q - q^{-1}}{2}$ and sum to zero. -/
theorem blockOf_deltaSNF_sq [CharZero K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    blockOf q (deltaSNF (q - q⁻¹)) * blockOf q (deltaSNF (q - q⁻¹)) =
      ((q - q⁻¹) ^ 2 / 4) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [blockOf, deltaSNF, S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **Antisymmetric $(1,1,1)$ Sign-Block Eigenvalue of $\Delta$ ($\sigma_i \mapsto -q^{-1}$)**:
On the 1-dimensional antisymmetric sign representation $(1,1,1)$ of $H_3(q)$,
$\Delta|_{(1,1,1)} = \frac{1}{2}(q - q^{-1})^2 + (q - q^{-1}) q^{-1} = +\frac{1}{2}(q^2 - q^{-2}) = +\frac{(q - q^{-1})(q + q^{-1})}{2}$. -/
theorem deltaSNF_sign_eigenvalue_forms [CharZero K] (q : K) (hq : q ≠ 0) :
    chi111 q (deltaSNF (q - q⁻¹)) = (q - q⁻¹) ^ 2 / 2 + (q - q⁻¹) * q⁻¹ ∧
    (q - q⁻¹) ^ 2 / 2 + (q - q⁻¹) * q⁻¹ = (q ^ 2 - q⁻¹ ^ 2) / 2 ∧
    (q ^ 2 - q⁻¹ ^ 2) / 2 = (q - q⁻¹) * (q + q⁻¹) / 2 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [chi111_deltaSNF q hq two_ne_zero]
    field_simp
    ring
  · field_simp
    ring
  · field_simp
    ring

/-- **Strict Positivity of $\Delta|_{(1,1,1)}$ and Negativity of $\Delta|_{(3)}$ for Real $q > 1$**:
For every real $q > 1$, $\Delta|_{(1,1,1)} > 0$ and $\Delta|_{(3)} < 0$. -/
theorem deltaSNF_sign_pos_and_trivial_neg {q : ℝ} (hq : 1 < q) :
    0 < chi111 q (deltaSNF (q - q⁻¹)) ∧ chi3 q (deltaSNF (q - q⁻¹)) < 0 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq4 : 1 < q ^ 4 := one_lt_pow₀ hq (by norm_num)
  rw [chi111_deltaSNF q (ne_of_gt hq0) two_ne_zero,
      chi3_deltaSNF q (ne_of_gt hq0) two_ne_zero]
  refine ⟨?_, ?_⟩
  · exact div_pos (sub_pos.mpr hq4) (mul_pos (by norm_num) (pow_pos hq0 2))
  · rw [neg_div]
    exact neg_lt_zero.mpr (div_pos (sub_pos.mpr hq4) (mul_pos (by norm_num) (pow_pos hq0 2)))

end SingleWrapAndSpechtDecomposition

-- ============================================================================
-- § 2. Bare Convention-D Trace vs. GPMT (1,1,1) Sign-Block Functional on Δ
-- ============================================================================

section BareConventionDVsGPMTSignBlock

variable {K : Type*} [Field K]

/-- **Sole-$(3)$-Block Origin of Bare $\mathrm{tr}_{z_D}(\Delta)$**:
Under Convention D ($z_D = q^3/(q^2+1)$), $(2,1)$ vanishes by $\mathrm{tr}_{(2,1)}(\Delta) = 0$
and $(1,1,1)$ vanishes by $w_{(1,1,1)}(z_D) = 0$, so $\mathrm{tr}_{z_D}(\Delta)$ reduces solely
to $w_{(3)}(z_D) \cdot \Delta|_{(3)}$ and equals
$\frac{1}{2}(q - q^{-1})^2 - (q - q^{-1}) z_D(q) = -\frac{(q - q^{-1})(q^4 + 1)}{2 q (q^2 + 1)}$. -/
theorem trM_zD_deltaSNF_sole_trivial_and_closed_form [CharZero K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹)) =
      w3 q (zD q) * chi3 q (deltaSNF (q - q⁻¹)) ∧
    trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹)) =
      (q - q⁻¹) ^ 2 / 2 - (q - q⁻¹) * zD q ∧
    trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹)) =
      -(q - q⁻¹) * (q ^ 4 + 1) / (2 * q * (q ^ 2 + 1)) := by
  have htwoRow := trM_conventionD_eq_twoRow_sum q hq hq2 hq4 (deltaSNF (q - q⁻¹))
  rw [chi21_deltaSNF_eq_zero q hq hq2 two_ne_zero, mul_zero, add_zero] at htwoRow
  refine ⟨?_, ?_, ?_⟩
  · rw [htwoRow, w3_conventionD q hq2 hq4]
  · rw [htwoRow, chi3_deltaSNF q hq two_ne_zero]
    unfold zD
    field_simp
    ring
  · rw [htwoRow, chi3_deltaSNF q hq two_ne_zero]
    field_simp
    ring

/-- The positive-weight Geer–Patureau-Mirand–Turaev sign-block trace functional on $H_3(q)$:
$\tau_{\mathrm{GPMT}}^{(1^3)}(q, v) := |d_{\mathrm{mod}}(1,1,1)| \cdot \chi_{(1,1,1)}(v) = -t_{\mathrm{Mod}}^{(1^3)}(q, v)$. -/
def tauGPMT111 (q : K) (v : Fin 6 → K) : K :=
  dMod111Abs q * chi111 q v

/-- Bridge between `tauGPMT111` and the two GPMT-completed Convention-D functionals:
`trM_conventionD_gpmtPos q v = trM (zD q) (q - q⁻¹) v + tauGPMT111 q v` and
`trM_conventionD_gpmtSigned q v = trM (zD q) (q - q⁻¹) v - tauGPMT111 q v`. -/
theorem trM_gpmt_decompositions_via_tauGPMT111 (q : K) (v : Fin 6 → K) :
    trM_conventionD_gpmtPos q v = trM (zD q) (q - q⁻¹) v + tauGPMT111 q v ∧
    trM_conventionD_gpmtSigned q v = trM (zD q) (q - q⁻¹) v - tauGPMT111 q v := by
  unfold trM_conventionD_gpmtPos trM_conventionD_gpmtSigned tauGPMT111 dMod111Abs tMod111
  refine ⟨by ring, by ring⟩

/-- **Exact Rational Closed Forms of $\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta)$**:
$$\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta) = \frac{q^3 (q^2 - q^{-2})}{2(q^2 + 1)(q^4 + q^2 + 1)}
  = \frac{q (q^2 - 1)}{2(q^4 + q^2 + 1)} = \frac{q - q^{-1}}{2(q^2 + 1 + q^{-2})}.$$ -/
theorem tauGPMT111_deltaSNF_closed_forms [CharZero K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    tauGPMT111 q (deltaSNF (q - q⁻¹)) =
      q ^ 3 * (q ^ 2 - q⁻¹ ^ 2) / (2 * (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) ∧
    tauGPMT111 q (deltaSNF (q - q⁻¹)) =
      q * (q ^ 2 - 1) / (2 * (q ^ 4 + q ^ 2 + 1)) := by
  unfold tauGPMT111
  rw [dMod111Abs_eq_div q, chi111_deltaSNF q hq two_ne_zero]
  generalize hD : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
  refine ⟨?_, ?_⟩
  · field_simp
  · field_simp
    ring

/-- **Strict Positivity of $\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta)$ for Real $q > 1$**:
$\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta) > 0$ for every real $q > 1$. -/
theorem tauGPMT111_deltaSNF_pos {q : ℝ} (hq : 1 < q) :
    0 < tauGPMT111 q (deltaSNF (q - q⁻¹)) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4_pos : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
  have hcf := (tauGPMT111_deltaSNF_closed_forms q (ne_of_gt hq0) hq2 (ne_of_gt hq4_pos)).2
  rw [hcf]
  have hqsq : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
  exact div_pos (mul_pos hq0 (sub_pos.mpr hqsq)) (mul_pos (by norm_num) hq4_pos)

/-- **Exact Closed Forms of Both Coherent $(3) \oplus (1,1,1)_{\mathrm{GPMT}}$ Trace Sums on $\Delta$**:
1. Signed sum `trM_zD(Δ) + dMod111(q) · Δ|_{(1^3)}` (`trM_conventionD_gpmtSigned`):
   $$-\frac{(q^2 - 1)(q^8 + q^6 + q^5 + 2 q^4 + q^3 + q^2 + 1)}{2 q^2 (q^2 + 1)(q^4 + q^2 + 1)}.$$
2. Positive-weight sum `trM_zD(Δ) - dMod111(q) · Δ|_{(1^3)}` (`trM_conventionD_gpmtPos`):
   $$-\frac{(q^2 - 1)(q^8 + q^6 - q^5 + 2 q^4 - q^3 + q^2 + 1)}{2 q^2 (q^2 + 1)(q^4 + q^2 + 1)}.$$ -/
theorem trM_gpmt_both_signs_deltaSNF_closed_forms [CharZero K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trM_conventionD_gpmtSigned q (deltaSNF (q - q⁻¹)) =
      -(q ^ 2 - 1) * (q ^ 8 + q ^ 6 + q ^ 5 + 2 * q ^ 4 + q ^ 3 + q ^ 2 + 1) /
        (2 * q ^ 2 * (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) ∧
    trM_conventionD_gpmtPos q (deltaSNF (q - q⁻¹)) =
      -(q ^ 2 - 1) * (q ^ 8 + q ^ 6 - q ^ 5 + 2 * q ^ 4 - q ^ 3 + q ^ 2 + 1) /
        (2 * q ^ 2 * (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have hsplit := trM_gpmt_decompositions_via_tauGPMT111 q (deltaSNF (q - q⁻¹))
  have hbare := (trM_zD_deltaSNF_sole_trivial_and_closed_form q hq hq2 hq4).2.2
  have htau := (tauGPMT111_deltaSNF_closed_forms q hq hq2 hq4).2
  refine ⟨?_, ?_⟩
  · rw [hsplit.2, hbare, htau]
    generalize hD : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
    field_simp
    subst hD
    ring
  · rw [hsplit.1, hbare, htau]
    generalize hD : q ^ 4 + q ^ 2 + 1 = D at hq4 ⊢
    field_simp
    subst hD
    ring

/-- **Strict Ordering of Both Coherent Magnitude Sums on Single-Wrap $\Delta$ for Real $q > 1$**:
For all real $q > 1$:
$$0 < |\mathrm{tr}_{z_D}(\Delta) - d_{\mathrm{mod}}(1^3)\Delta|_{(1^3)}|
  < |\mathrm{tr}_{z_D}(\Delta)|
  < |\mathrm{tr}_{z_D}(\Delta) + d_{\mathrm{mod}}(1^3)\Delta|_{(1^3)}|.$$ -/
theorem abs_trM_gpmt_ordering_on_deltaSNF {q : ℝ} (hq : 1 < q) :
    0 < |trM_conventionD_gpmtPos q (deltaSNF (q - q⁻¹))| ∧
    |trM_conventionD_gpmtPos q (deltaSNF (q - q⁻¹))| <
      |trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹))| ∧
    |trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹))| <
      |trM_conventionD_gpmtSigned q (deltaSNF (q - q⁻¹))| := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4_pos : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
  have hqsq : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
  have htau_pos : 0 < tauGPMT111 q (deltaSNF (q - q⁻¹)) := tauGPMT111_deltaSNF_pos hq
  have hsplit := trM_gpmt_decompositions_via_tauGPMT111 q (deltaSNF (q - q⁻¹))
  have hcf := trM_gpmt_both_signs_deltaSNF_closed_forms q (ne_of_gt hq0) hq2 (ne_of_gt hq4_pos)
  have hpoly_pos : 0 < q ^ 8 + q ^ 6 - q ^ 5 + 2 * q ^ 4 - q ^ 3 + q ^ 2 + 1 := by
    have hrew : q ^ 8 + q ^ 6 - q ^ 5 + 2 * q ^ 4 - q ^ 3 + q ^ 2 + 1 =
        q ^ 8 + q ^ 5 * (q - 1) + q ^ 3 * (2 * q - 1) + q ^ 2 + 1 := by ring
    rw [hrew]
    have hq1 : 0 < q - 1 := sub_pos.mpr hq
    have h2q1 : 0 < 2 * q - 1 := by linarith
    positivity
  have hpos_neg : trM_conventionD_gpmtPos q (deltaSNF (q - q⁻¹)) < 0 := by
    rw [hcf.2, neg_mul, neg_div]
    apply neg_lt_zero.mpr
    apply div_pos (mul_pos (sub_pos.mpr hqsq) hpoly_pos)
    positivity
  have hbare_neg : trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹)) < 0 := by
    linarith [hsplit.1]
  have hsigned_neg : trM_conventionD_gpmtSigned q (deltaSNF (q - q⁻¹)) < 0 := by
    linarith [hsplit.2]
  rw [abs_of_neg hpos_neg, abs_of_neg hbare_neg, abs_of_neg hsigned_neg]
  refine ⟨by linarith, by linarith [hsplit.1], by linarith [hsplit.2]⟩

end BareConventionDVsGPMTSignBlock

-- ============================================================================
-- § 3. Full Three-Block Decomposition & GPMT Boost on 11-Crossing Δ_resel
-- ============================================================================

section ElevenCrossingReselectedNucleonDiff

variable {K : Type*} [Field K]

/-- **Exact Factored $(2,1)$ Mixed-Symmetry Character on the 11-Crossing Reselected $\Delta_{\mathrm{resel}}$**:
Unlike single-wrap $\Delta$ (where $\chi_{(2,1)}(\Delta) = 0$), on the 11-crossing nucleon
difference `nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)` the $(2,1)$ character is non-zero
and factors into
$$\chi_{(2,1)}(\Delta_{\mathrm{resel}}) =
  \frac{(q^2 - 1)(q^4 + 1)(2 q^{12} - 5 q^{10} + 5 q^8 - 5 q^6 + 5 q^4 - 5 q^2 + 2)}{4 q^9}.$$ -/
theorem chi21_nucleonDiffCoord_closed_form [CharZero K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    chi21 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * (q ^ 4 + 1) *
        (2 * q ^ 12 - 5 * q ^ 10 + 5 * q ^ 8 - 5 * q ^ 6 + 5 * q ^ 4 - 5 * q ^ 2 + 2) /
        (4 * q ^ 9) := by
  unfold nucleonDiffCoord chi21
  rw [chiM_eq_closed q hq hq2]
  have hlin :
      chiM q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2) -
          protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
        chi21 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
          chi21 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) := by
    unfold chi21
    rw [chiM_eq_closed q hq hq2, chiM_eq_closed q hq hq2, chiM_eq_closed q hq hq2]
    simp [Pi.sub_apply]
    ring
  rw [← chiM_eq_closed q hq hq2, hlin,
      chi21_neutronCoord q hq hq2 two_ne_zero,
      chi21_protonCoord q hq hq2 two_ne_zero]
  field_simp
  ring

/-- **Exact GPMT $(1,1,1)$ Sign-Block Contribution on 11-Crossing $\Delta_{\mathrm{resel}}$**:
$$\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta_{\mathrm{resel}})
  = |d_{\mathrm{mod}}(1,1,1)| \cdot \chi_{(1,1,1)}(\Delta_{\mathrm{resel}})
  = -\frac{(q^2 - 1)(q^2 + 1)}{4 q^2 (q^4 + q^2 + 1)}.$$ -/
theorem tauGPMT111_nucleonDiffCoord_closed_form [CharZero K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauGPMT111 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      -(q ^ 2 - 1) * (q ^ 2 + 1) / (4 * q ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  unfold tauGPMT111
  rw [dMod111Abs_eq_div q, chi111_nucleonDiffCoord q hq two_ne_zero]
  field_simp

/-- **Constructive Sign-Coherence on 11-Crossing $\Delta_{\mathrm{resel}}$ for Real $q > 1$**:
For real $q > 1$, $\tau_{\mathrm{GPMT}}^{(1^3)}(\Delta_{\mathrm{resel}}) < 0$, matching the
negative sign of $\chi_{(3)}(\Delta_{\mathrm{resel}})$; whenever $\mathrm{tr}_{z_D}(\Delta_{\mathrm{resel}}) < 0$,
restoring the $(1,1,1)$ block via `trM_conventionD_gpmtPos` strictly increases the magnitude:
$$|\mathrm{tr}_{M}^{D,\mathrm{GPMT}+}(\Delta_{\mathrm{resel}})|
  = |\mathrm{tr}_{z_D}(\Delta_{\mathrm{resel}})| + \frac{(q^2 - 1)(q^2 + 1)}{4 q^2 (q^4 + q^2 + 1)}.$$ -/
theorem abs_trM_gpmtPos_nucleonDiffCoord_boost {q : ℝ} (hq : 1 < q)
    (hbare : trM (zD q) (q - q⁻¹) (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) < 0) :
    |trM_conventionD_gpmtPos q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2))| =
      |trM (zD q) (q - q⁻¹) (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2))| +
        (q ^ 2 - 1) * (q ^ 2 + 1) / (4 * q ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hqsq : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
  have hsplit := (trM_gpmt_decompositions_via_tauGPMT111 q
    (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2))).1
  have htau := tauGPMT111_nucleonDiffCoord_closed_form q (ne_of_gt hq0) hq2
  have hmag_pos : 0 < (q ^ 2 - 1) * (q ^ 2 + 1) / (4 * q ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
    apply div_pos (mul_pos (sub_pos.mpr hqsq) (by positivity))
    positivity
  have htau_neg : tauGPMT111 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) < 0 := by
    rw [htau, neg_mul, neg_div]
    exact neg_lt_zero.mpr hmag_pos
  have htot_neg : trM_conventionD_gpmtPos q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) < 0 := by
    linarith
  rw [abs_of_neg htot_neg, abs_of_neg hbare, hsplit, htau]
  ring

end ElevenCrossingReselectedNucleonDiff

-- ============================================================================
-- § 4. Two-Term QCD + QED Nucleon Mass Splitting & Q_β Decomposition
-- ============================================================================

section TwoTermNucleonSplittingAndQBeta

variable {K : Type*} [Field K]

/-- Tower-resummed hadronic energy scale
$E_0^{(\infty)}(m_e, q) = \frac{m_e}{q (q - 1) (1 - (1 - q^{-1})^2)}$. -/
def hadronicScaleE0Tower (me q : K) : K :=
  me / (q * (q - 1) * (1 - (1 - q⁻¹) ^ 2))

/-- Exact rational simplification of the tower-resummed hadronic energy scale:
$$E_0^{(\infty)}(m_e, q) = \frac{m_e q}{(q - 1)(2 q - 1)}.$$ -/
theorem hadronicScaleE0Tower_closed_form (me q : K) (hq : q ≠ 0)
    (hq1 : q - 1 ≠ 0) :
    hadronicScaleE0Tower me q = me * q / ((q - 1) * (2 * q - 1)) := by
  have hden : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by
    field_simp
    ring
  unfold hadronicScaleE0Tower
  rw [hden]
  field_simp

/-- Proton connected fourth-order Borromean $V^3 = (\sigma_0 \sigma_1^{-1})^3$ electromagnetic
self-energy $M_{\mathrm{QED}}^{\mathrm{Bor}}(p) = -\frac{m_e}{3} \mathrm{tr}((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3)$. -/
def borromeanProtonQEDSelfEnergy (me q : K) : K :=
  -(me / 3) * trace ((Q12p + Q23p) * borromeanV3A q)

/-- Neutron connected fourth-order Borromean $V^3 = (\sigma_0 \sigma_1^{-1})^3$ electromagnetic
self-energy $M_{\mathrm{QED}}^{\mathrm{Bor}}(n) = -\frac{m_e}{3} \bigl(\mathrm{tr}((Q_{12}^{(n)} + Q_{23}^{(n)}) V_n^3) + \frac{2}{9}\mathrm{tr}(V_n^3)\bigr)$. -/
def borromeanNeutronQEDSelfEnergy (me q : K) : K :=
  -(me / 3) * (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q))

/-- Connected fourth-order Borromean $V^3$ electromagnetic $(n - p)$ mass-splitting shift
$\Delta M_{\mathrm{QED}}^{\mathrm{Bor}}(m_e, q) = M_{\mathrm{QED}}^{\mathrm{Bor}}(n) - M_{\mathrm{QED}}^{\mathrm{Bor}}(p)$. -/
def borromeanConnectedDeltaMQED (me q : K) : K :=
  borromeanNeutronQEDSelfEnergy me q - borromeanProtonQEDSelfEnergy me q

/-- Two-term $\beta^-$-decay $Q$-value $\mathfrak{Q}_\beta^{\mathrm{2t}}(m_e, q, \tau_\Delta)
= (-\tau_\Delta) \cdot E_0^{(\infty)}(m_e, q) + \Delta M_{\mathrm{QED}}^{\mathrm{Bor}}(m_e, q)$
associated to a dimensionless $H_3(q)$ $(n - p)$ trace evaluation $\tau_\Delta$. -/
def twoTermNeutronQBeta (me q tauDelta : K) : K :=
  (-tauDelta) * hadronicScaleE0Tower me q + borromeanConnectedDeltaMQED me q

/-- Two-term neutron–proton mass splitting $\Delta m_{np}^{\mathrm{2t}}(m_e, q, \tau_\Delta)
= \bigl(m_e + (-\tau_\Delta) \cdot E_0^{(\infty)}(m_e, q)\bigr) + M_{\mathrm{QED}}^{\mathrm{Bor}}(n) - M_{\mathrm{QED}}^{\mathrm{Bor}}(p)$. -/
def twoTermNucleonSplitting (me q tauDelta : K) : K :=
  (me + (-tauDelta) * hadronicScaleE0Tower me q) +
    borromeanNeutronQEDSelfEnergy me q - borromeanProtonQEDSelfEnergy me q

/-- **Exact Two-Term Nucleon Mass-Splitting & $\mathfrak{Q}_\beta$ Decomposition**:
1. Kinematic Beta-Decay Relation: $\Delta m_{np}^{\mathrm{2t}} = m_e + \mathfrak{Q}_\beta^{\mathrm{2t}}$,
2. Two-Term QCD + QED Splitting Sum: $\Delta m_{np}^{\mathrm{2t}} = \Delta M_{\mathrm{QCD}} + \Delta M_{\mathrm{QED}}^{\mathrm{Bor}}$
   where $\Delta M_{\mathrm{QCD}} = m_e + (-\tau_\Delta) \cdot E_0^{(\infty)}(m_e, q)$. -/
theorem twoTermNucleonSplitting_eq_me_add_qbeta_and_qcd_qed (me q tauDelta : K) :
    twoTermNucleonSplitting me q tauDelta = me + twoTermNeutronQBeta me q tauDelta ∧
    twoTermNucleonSplitting me q tauDelta =
      (me + (-tauDelta) * hadronicScaleE0Tower me q) + borromeanConnectedDeltaMQED me q := by
  unfold twoTermNucleonSplitting twoTermNeutronQBeta borromeanConnectedDeltaMQED
  refine ⟨by ring, by ring⟩

/-- **Exact Rational Closed Forms of Proton, Neutron, and $(n - p)$ Borromean $V^3$ QED Energies**:
1. $M_{\mathrm{QED}}^{\mathrm{Bor}}(p) = +\frac{2 m_e (q^2 - 1)^4 (q^4 + q^2 + 1)}{27 q^6}$,
2. $M_{\mathrm{QED}}^{\mathrm{Bor}}(n) = -\frac{m_e (q^2 - 1)^4 (2 q^4 - q^2 + 2)}{27 q^6}$,
3. $\Delta M_{\mathrm{QED}}^{\mathrm{Bor}} = -\frac{m_e (q^2 - 1)^4 (4 q^4 + q^2 + 4)}{27 q^6}$. -/
theorem borromeanQED_proton_neutron_and_diff_closed_forms [CharZero K] (me q : K) (hq : q ≠ 0) :
    borromeanProtonQEDSelfEnergy me q =
      2 * me * (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6) ∧
    borromeanNeutronQEDSelfEnergy me q =
      -me * (q ^ 2 - 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6) ∧
    borromeanConnectedDeltaMQED me q =
      -me * ((q ^ 2 - 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4)) / (27 * q ^ 6) := by
  have h3 : (3 : K) ≠ 0 := three_ne_zero
  have hfac : (q - 1) ^ 4 * (q + 1) ^ 4 = (q ^ 2 - 1) ^ 4 := by ring
  refine ⟨?_, ?_, ?_⟩
  · unfold borromeanProtonQEDSelfEnergy
    rw [trace_QAdjp_borromeanV3 q hq h3]
    have hrew : -2 * (q - 1) ^ 4 * (q + 1) ^ 4 = -2 * ((q - 1) ^ 4 * (q + 1) ^ 4) := by ring
    rw [hrew, hfac]
    field_simp
    ring
  · unfold borromeanNeutronQEDSelfEnergy
    rw [trace_QAdjn_borromeanV3_connected q hq h3, hfac]
    field_simp
    ring
  · unfold borromeanConnectedDeltaMQED borromeanNeutronQEDSelfEnergy borromeanProtonQEDSelfEnergy
    have hdiff :
        -(me / 3) * (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) -
          -(me / 3) * trace ((Q12p + Q23p) * borromeanV3A q) =
        -(me / 3) * ((trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) -
          trace ((Q12p + Q23p) * borromeanV3A q)) := by ring
    rw [hdiff, trace_QAdj_connected_diff_borromeanV3 q hq h3, hfac]
    field_simp
    ring

/-- **Repulsive Proton QED Self-Energy, Attractive Connected Neutron QED Self-Energy, and Negative $\Delta M_{\mathrm{QED}}^{\mathrm{Bor}}$ for Real $q > 1$**:
For all real $q > 1$ and $m_e > 0$:
1. $M_{\mathrm{QED}}^{\mathrm{Bor}}(p) > 0$,
2. $M_{\mathrm{QED}}^{\mathrm{Bor}}(n) < 0$,
3. $\Delta M_{\mathrm{QED}}^{\mathrm{Bor}} < 0$, so $\mathfrak{Q}_\beta^{\mathrm{2t}} < (-\tau_\Delta) \cdot E_0^{(\infty)}(m_e, q)$. -/
theorem borromeanQED_signs_and_qbeta_lowering {me q : ℝ} (hme : 0 < me) (hq : 1 < q)
    (tauDelta : ℝ) :
    0 < borromeanProtonQEDSelfEnergy me q ∧
    borromeanNeutronQEDSelfEnergy me q < 0 ∧
    borromeanConnectedDeltaMQED me q < 0 ∧
    twoTermNeutronQBeta me q tauDelta < (-tauDelta) * hadronicScaleE0Tower me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hqsq : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
  have hcf := borromeanQED_proton_neutron_and_diff_closed_forms me q (ne_of_gt hq0)
  have hpow4 : 0 < (q ^ 2 - 1) ^ 4 := pow_pos (sub_pos.mpr hqsq) 4
  have hn_quad : 0 < 2 * q ^ 4 - q ^ 2 + 2 := by
    have hrew : 2 * q ^ 4 - q ^ 2 + 2 = q ^ 4 + q ^ 2 * (q ^ 2 - 1) + 2 := by ring
    rw [hrew]
    have hq2m1 : 0 < q ^ 2 - 1 := sub_pos.mpr hqsq
    positivity
  have hp_pos : 0 < borromeanProtonQEDSelfEnergy me q := by
    rw [hcf.1]
    apply div_pos
    · exact mul_pos (mul_pos (mul_pos (by norm_num) hme) hpow4) (by positivity)
    · positivity
  have hn_neg : borromeanNeutronQEDSelfEnergy me q < 0 := by
    rw [hcf.2.1, neg_mul, neg_mul, neg_div]
    apply neg_lt_zero.mpr
    apply div_pos
    · exact mul_pos (mul_pos hme hpow4) hn_quad
    · positivity
  have hdiff_neg : borromeanConnectedDeltaMQED me q < 0 := by
    unfold borromeanConnectedDeltaMQED
    linarith
  refine ⟨hp_pos, hn_neg, hdiff_neg, ?_⟩
  unfold twoTermNeutronQBeta
  linarith

end TwoTermNucleonSplittingAndQBeta

end QOU.QBeta.GPMTSignBlockAndTwoTermNucleonSplitting
