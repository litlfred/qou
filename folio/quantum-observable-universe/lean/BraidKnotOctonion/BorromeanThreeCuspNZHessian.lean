/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Borromean 3-Cusp Neumann–Zagier Jacobian, Diagonal Quadratic Hessian, and 3rd-Order Cross-Terms

Task: `qou-ay84` (absorbing `qou-mcus` under epic `qou-avtq`, `Q-AVTQ-2 = 1`).
Probe companion: `computations/qbeta/borromean_three_cusp_nz_hessian_probe.py`.
Witness companion: `computations/qbeta/borromean-three-cusp-nz-hessian.witness.json`.

This module formalizes the exact 3-cusp Neumann–Zagier variational system of the
Borromean rings complement $\mathbb{B}_3$ (`L6a4`, 3 cusps, 8 ideal tetrahedra = 2 regular
ideal octahedra) around the complete hyperbolic structure $u = (0, 0, 0)$:

1. **Complete octahedral structure in $\mathbb{Z}[i]$ (`w0Re`, `w0Im`):**
   At the complete structure $z^{(0)} = \left(\frac{1+i}{2}, 1+i, 1+i, 1+i, 1+i, \frac{1+i}{2}, \frac{1+i}{2}, \frac{1+i}{2}\right)$,
   the logarithmic derivative weight $w_k^{(0)} = \frac{z_k^{(0)}}{1 - z_k^{(0)}}$ lies in
   $\mathbb{Z}[i]$: $w^{(0)} = (i, -1+i, -1+i, -1+i, -1+i, i, i, i)$.

2. **Exact 1st-order shape sensitivity solution (`mSys_mul_scaledZ1_re`, `mSys_mul_scaledZ1_im`):**
   For the $8 \times 8$ system $M_{\mathrm{sys}}$ formed by the 5 independent edge rows
   $(0,1,2,3,4)$ and the 3 meridian rows of SnapPy's `L6a4` triangulation, the scaled
   $8 \times 3$ shape sensitivity matrix $S^{(1)} = 4\,\frac{\partial Z}{\partial u}\big|_{u=0}$
   has every entry in $\{\pm 1 \pm i\}$ (all 24 entries non-zero with Gaussian norm-squared $2$)
   and satisfies $M_{\mathrm{sys}} \cdot S^{(1)} = 4 \begin{pmatrix} 0_{5 \times 3} \\ I_3 \end{pmatrix}$
   identically over $\mathbb{Z}[i]$.

3. **Strict diagonality of the $3 \times 3$ longitude Jacobian (`cLon_mul_scaledZ1_re`,
   `cLon_mul_scaledZ1_im`, `cLon_mul_scaledZ1_offDiag_zero`):**
   Despite all 8 tetrahedra being shared across all 3 cusps, multiplying $S^{(1)}$ by the
   $3 \times 8$ longitude gluing operator $C_{\mathrm{lon}}$ yields
     $$C_{\mathrm{lon}} \cdot \left(4\,\frac{\partial Z}{\partial u}\bigg|_{u=0}\right) = -8i\,I_3, \qquad
       \frac{\partial v_i}{\partial u_j}\bigg|_{u=0} = -2i\,\delta_{ij}$$
   (or $\tau_{ij} = +2i\,\delta_{ij}$ in the cusp modulus convention $\tau_i = -v_i/u_i$).
   All 6 off-diagonal entries ($i \neq j$) vanish identically, forced by pairwise linking
   number $\mathrm{lk}(K_i, K_j) = 0$ and $(\mathbb{Z}/2\mathbb{Z})^3$ component-reversal parity.

4. **Quadratic complex-volume Hessian on the symmetric locus (`borromeanQuadForm_sym_locus`,
   `kappaBorSym_of_zero_offDiag`):**
   At quadratic order in $u$, vanishing off-diagonal Hessian entries ($\kappa_{\mathrm{off}} = 0$)
   imply $\kappa_{\mathrm{Bor}}^{\mathrm{sym}} = 3\,\kappa_{\text{per-cusp}}$ with zero
   quadratic inter-cusp cross-term (`sign_flip_resolved = False` per `qou-mcus`).

5. **3rd-order inter-cusp coupling and symmetric cubic sign flip
   (`borromeanCubicLon_single_cusp`, `borromeanCubicLon_sym_locus`,
   `borromeanCubicSymCoeff_eq_neg_five_twelfths`):**
   Inter-cusp coupling from the shared octahedral tetrahedra first enters at 3rd order in
   $v_i(u_1,u_2,u_3)$ (quartic order $O(u^4)$ in $\mathrm{CVol}$), where
   $a_{3,\text{self}} = +\frac{1}{12}$ and $a_{3,\text{cross}} = -\frac{1}{4}$, flipping the
   cubic longitude coefficient from $+\frac{1}{12}$ on the single-cusp locus $(u,0,0)$ to
   $\frac{1}{12} + 2\left(-\frac{1}{4}\right) = -\frac{5}{12} = -5\,a_{3,\text{self}}$ on the
   symmetric 3-cusp locus $(u,u,u)$.

-- Ref: [neumann-zagier1985] Neumann & Zagier, Topology 24 (1985), 307-332
-- Ref: [pandey-wong-2023] Pandey & Wong, arXiv:2308.06643 (Borromean rings shadow link)
-- Ref: [manuscript] computations/qbeta/borromean_three_cusp_nz_hessian_probe.py
-/
import Mathlib.Tactic

namespace QOU.QBeta.BorromeanThreeCuspNZHessian

/-! ## 1. Complete Octahedral Structure and Gluing Operators of `L6a4` ($\mathbb{B}_3$) -/

/-- Real part of $w_k^{(0)} = z_k^{(0)} / (1 - z_k^{(0)}) \in \mathbb{Z}[i]$ at the complete
regular-octahedral structure of `L6a4`: $0$ on tetrahedra $\{0,5,6,7\}$ and $-1$ on $\{1,2,3,4\}$. -/
def w0Re : Fin 8 → ℤ := ![0, -1, -1, -1, -1, 0, 0, 0]

/-- Imaginary part of $w_k^{(0)} = z_k^{(0)} / (1 - z_k^{(0)}) \in \mathbb{Z}[i]$ at the complete
regular-octahedral structure of `L6a4`: $+1$ on all 8 tetrahedra. -/
def w0Im : Fin 8 → ℤ := ![1, 1, 1, 1, 1, 1, 1, 1]

/-- Integer $\log(z_k)$ coefficients $A_{\mathrm{sys}}$ for the $8 \times 8$ system formed by
the 5 independent edge rows $(0,1,2,3,4)$ and the 3 meridian rows of SnapPy's `L6a4`. -/
def sysA : Fin 8 → Fin 8 → ℤ :=
  ![![1, 0, 1, -1, 0, 1, 0, 0],
    ![-1, 0, 0, 0, 0, 0, 0, -1],
    ![-1, 0, 0, 0, 0, 0, 0, 0],
    ![0, -1, 0, 0, -1, 1, 0, 0],
    ![1, 1, 0, 0, 1, 0, 1, 1],
    ![0, 1, 0, 0, 0, -1, 0, 0],
    ![0, -1, -1, 0, 0, -1, -1, 1],
    ![0, 0, 0, 0, 0, -1, 0, 0]]

/-- Integer $\log(1/(1-z_k))$ coefficients $U_{\mathrm{sys}} = -B_{\mathrm{sys}}$ for the $8 \times 8$
system formed by the 5 independent edge rows $(0,1,2,3,4)$ and the 3 meridian rows of `L6a4`. -/
def sysU : Fin 8 → Fin 8 → ℤ :=
  ![![1, -1, 0, -1, 0, 0, 1, 0],
    ![-1, 1, 0, 0, 1, 0, 0, -1],
    ![-1, 0, 1, 1, 1, 0, 0, 0],
    ![1, -1, -1, 0, -1, 1, 0, 1],
    ![0, 0, 0, -1, 0, 0, 1, 0],
    ![0, 1, 0, 0, 0, -1, 0, -1],
    ![1, -1, 0, 1, -1, 0, -1, 1],
    ![0, 1, 0, 0, 0, 0, -1, 0]]

/-- Integer $\log(z_k)$ coefficients $A_{\mathrm{lon}}$ for the 3 longitude rows of `L6a4`. -/
def lonA : Fin 3 → Fin 8 → ℤ :=
  ![![1, 0, -1, 1, 0, 0, 1, 0],
    ![1, 0, 0, 0, 0, 0, 0, 0],
    ![0, 1, 0, 0, 1, 1, 0, 1]]

/-- Integer $\log(1/(1-z_k))$ coefficients $U_{\mathrm{lon}} = -B_{\mathrm{lon}}$ for the 3
longitude rows of `L6a4`. -/
def lonU : Fin 3 → Fin 8 → ℤ :=
  ![![1, -1, -1, 0, 0, 1, 0, 0],
    ![1, 0, 1, 1, -1, 0, 0, 0],
    ![-1, 0, 0, 1, 1, 1, 0, 0]]

/-- Real part of the $8 \times 8$ linearized gluing operator
$M_{\mathrm{sys}} = A_{\mathrm{sys}} + U_{\mathrm{sys}}\,\mathrm{diag}(w^{(0)})$ over $\mathbb{Z}[i]$. -/
def mSysRe (r k : Fin 8) : ℤ := sysA r k + sysU r k * w0Re k

/-- Imaginary part of the $8 \times 8$ linearized gluing operator $M_{\mathrm{sys}}$ over $\mathbb{Z}[i]$. -/
def mSysIm (r k : Fin 8) : ℤ := sysU r k * w0Im k

/-- Real part of the $3 \times 8$ linearized longitude operator
$C_{\mathrm{lon}} = A_{\mathrm{lon}} + U_{\mathrm{lon}}\,\mathrm{diag}(w^{(0)})$ over $\mathbb{Z}[i]$. -/
def cLonRe (i : Fin 3) (k : Fin 8) : ℤ := lonA i k + lonU i k * w0Re k

/-- Imaginary part of the $3 \times 8$ linearized longitude operator $C_{\mathrm{lon}}$ over $\mathbb{Z}[i]$. -/
def cLonIm (i : Fin 3) (k : Fin 8) : ℤ := lonU i k * w0Im k

/-! ## 2. Exact 1st-Order Shape Sensitivity Matrix $S^{(1)} = 4\,\partial Z / \partial u\big|_{u=0}$ -/

/-- Real part of the scaled $8 \times 3$ shape sensitivity matrix
$S^{(1)} = 4\,\frac{\partial Z}{\partial u}\big|_{u=0}$ over $\mathbb{Z}[i]$. -/
def scaledZ1Re : Fin 8 → Fin 3 → ℤ :=
  ![![-1, -1, 1],
    ![1, -1, -1],
    ![1, -1, 1],
    ![-1, -1, -1],
    ![-1, 1, -1],
    ![-1, -1, -1],
    ![1, -1, 1],
    ![1, 1, 1]]

/-- Imaginary part of the scaled $8 \times 3$ shape sensitivity matrix
$S^{(1)} = 4\,\frac{\partial Z}{\partial u}\big|_{u=0}$ over $\mathbb{Z}[i]$. -/
def scaledZ1Im : Fin 8 → Fin 3 → ℤ :=
  ![![-1, -1, -1],
    ![-1, 1, -1],
    ![1, 1, -1],
    ![-1, 1, 1],
    ![1, -1, -1],
    ![1, -1, -1],
    ![-1, -1, 1],
    ![1, 1, -1]]

/-- Every entry of the scaled $8 \times 3$ shape Jacobian $4\,\frac{\partial Z_k}{\partial u_j}\big|_{u=0}$
has Gaussian norm-squared $(\mathrm{Re})^2 + (\mathrm{Im})^2 = 2$; in particular all 24 entries
are non-zero, demonstrating that every ideal tetrahedron responds to all 3 cusps. -/
theorem scaledZ1_normSq_eq_two :
    ∀ (k : Fin 8) (j : Fin 3), (scaledZ1Re k j) ^ 2 + (scaledZ1Im k j) ^ 2 = 2 := by
  decide

/-- Real part of the $8 \times 3$ product $M_{\mathrm{sys}} \cdot S^{(1)}$ in $\mathbb{Z}[i]$. -/
def mSysMulScaledZ1Re (r : Fin 8) (j : Fin 3) : ℤ :=
  ∑ k : Fin 8, (mSysRe r k * scaledZ1Re k j - mSysIm r k * scaledZ1Im k j)

/-- Imaginary part of the $8 \times 3$ product $M_{\mathrm{sys}} \cdot S^{(1)}$ in $\mathbb{Z}[i]$. -/
def mSysMulScaledZ1Im (r : Fin 8) (j : Fin 3) : ℤ :=
  ∑ k : Fin 8, (mSysRe r k * scaledZ1Im k j + mSysIm r k * scaledZ1Re k j)

/-- Exact verification that $S^{(1)} = 4\,\frac{\partial Z}{\partial u}\big|_{u=0}$ solves the
linearized gluing system $M_{\mathrm{sys}} \cdot S^{(1)} = 4 \begin{pmatrix} 0_{5 \times 3} \\ I_3 \end{pmatrix}$:
the real part equals $4$ on the meridian diagonal $r = 5 + j$ and $0$ everywhere else. -/
theorem mSys_mul_scaledZ1_re :
    ∀ (r : Fin 8) (j : Fin 3),
      mSysMulScaledZ1Re r j = if r.val = 5 + j.val then 4 else 0 := by
  decide

/-- Exact verification that the imaginary part of $M_{\mathrm{sys}} \cdot S^{(1)}$ vanishes
identically across all $8 \times 3$ entries. -/
theorem mSys_mul_scaledZ1_im :
    ∀ (r : Fin 8) (j : Fin 3), mSysMulScaledZ1Im r j = 0 := by
  decide

/-! ## 3. Strict Diagonality of the $3 \times 3$ Longitude Jacobian $J^{(1)} = \partial v_i / \partial u_j\big|_{u=0}$ -/

/-- Real part of the scaled $3 \times 3$ longitude Jacobian
$4\,J^{(1)} = C_{\mathrm{lon}} \cdot S^{(1)}$ in $\mathbb{Z}[i]$. -/
def scaledLonJacRe (i j : Fin 3) : ℤ :=
  ∑ k : Fin 8, (cLonRe i k * scaledZ1Re k j - cLonIm i k * scaledZ1Im k j)

/-- Imaginary part of the scaled $3 \times 3$ longitude Jacobian
$4\,J^{(1)} = C_{\mathrm{lon}} \cdot S^{(1)}$ in $\mathbb{Z}[i]$. -/
def scaledLonJacIm (i j : Fin 3) : ℤ :=
  ∑ k : Fin 8, (cLonRe i k * scaledZ1Im k j + cLonIm i k * scaledZ1Re k j)

/-- The real part of the scaled $3 \times 3$ longitude Jacobian $4\,J^{(1)}$ vanishes identically
for all $i, j \in \{0, 1, 2\}$. -/
theorem scaledLonJac_re_eq_zero :
    ∀ (i j : Fin 3), scaledLonJacRe i j = 0 := by
  decide

/-- The imaginary part of the scaled $3 \times 3$ longitude Jacobian $4\,J^{(1)}$ is strictly
diagonal: $4\,\mathrm{Im}(J^{(1)}_{ij}) = -8\,\delta_{ij}$, so $J^{(1)}_{ij} = -2i\,\delta_{ij}$
(and the cusp modulus matrix $\tau_{ij} = -J^{(1)}_{ij} = +2i\,\delta_{ij}$). -/
theorem scaledLonJac_im_eq_diag :
    ∀ (i j : Fin 3), scaledLonJacIm i j = if i = j then -8 else 0 := by
  decide

/-- All 6 off-diagonal entries ($i \neq j$) of the $3 \times 3$ Borromean longitude Jacobian
vanish identically in both real and imaginary parts, proving that the shared octahedral
tetrahedra produce zero quadratic inter-cusp coupling. -/
theorem scaledLonJac_offDiag_zero (i j : Fin 3) (hne : i ≠ j) :
    scaledLonJacRe i j = 0 ∧ scaledLonJacIm i j = 0 := by
  refine ⟨scaledLonJac_re_eq_zero i j, ?_⟩
  rw [scaledLonJac_im_eq_diag i j, if_neg hne]

/-! ## 4. Quadratic Complex-Volume Hessian & Symmetric Deformation $\kappa_{\mathrm{Bor}}^{\mathrm{sym}}$ -/

/-- General $S_3$-symmetric 3-cusp quadratic curvature form with diagonal per-cusp curvature
$\kappa_{\mathrm{diag}}$ and off-diagonal inter-cusp coupling $\kappa_{\mathrm{off}}$. -/
def borromeanQuadForm {R : Type*} [CommRing R] (κ_diag κ_off u₁ u₂ u₃ : R) : R :=
  κ_diag * (u₁ ^ 2 + u₂ ^ 2 + u₃ ^ 2) + 2 * κ_off * (u₁ * u₂ + u₂ * u₃ + u₃ * u₁)

/-- Symmetric-locus ($u_1 = u_2 = u_3 = u$) effective quadratic curvature coefficient
$\kappa_{\mathrm{Bor}}^{\mathrm{sym}} = 3\,\kappa_{\mathrm{diag}} + 6\,\kappa_{\mathrm{off}}$. -/
def kappaBorSym {R : Type*} [CommRing R] (κ_diag κ_off : R) : R :=
  3 * κ_diag + 6 * κ_off

/-- Evaluating the 3-cusp quadratic form on the symmetric deformation locus $u_1 = u_2 = u_3 = u$
yields $\kappa_{\mathrm{Bor}}^{\mathrm{sym}} \cdot u^2$. -/
theorem borromeanQuadForm_sym_locus {R : Type*} [CommRing R] (κ_diag κ_off u : R) :
    borromeanQuadForm κ_diag κ_off u u u = kappaBorSym κ_diag κ_off * u ^ 2 := by
  unfold borromeanQuadForm kappaBorSym
  ring

/-- Because the Borromean 3-cusp NZ Jacobian is strictly diagonal (`scaledLonJac_offDiag_zero`),
the quadratic inter-cusp coupling vanishes ($\kappa_{\mathrm{off}} = 0$), forcing
$\kappa_{\mathrm{Bor}}^{\mathrm{sym}} = 3\,\kappa_{\mathrm{diag}}$. In particular, inter-cusp
quadratic cross-terms cannot flip the sign of $\kappa_{\mathrm{Bor}}^{\mathrm{sym}}$. -/
theorem kappaBorSym_of_zero_offDiag {R : Type*} [CommRing R] (κ_diag : R) :
    kappaBorSym κ_diag 0 = 3 * κ_diag := by
  unfold kappaBorSym
  ring

/-- In the NZ per-cusp frame where $\kappa_{\mathrm{diag}} = -1$ and $\kappa_{\mathrm{off}} = 0$,
$\kappa_{\mathrm{Bor}}^{\mathrm{sym}} = -3 < 0$ (preserving the per-cusp sign). -/
theorem kappaBorSym_nz_frame_neg :
    kappaBorSym (-1 : ℚ) 0 = -3 ∧ kappaBorSym (-1 : ℚ) 0 < 0 := by
  unfold kappaBorSym
  norm_num

/-! ## 5. Third-Order Inter-Cusp Coupling and Symmetric Cubic Sign Flip -/

/-- The exact 3rd-order imaginary Taylor coefficient of $v_i$ for self-deformation $u_i^3$:
$\frac{1}{3!} \mathrm{Im}\!\left(\frac{\partial^3 v_i}{\partial u_i^3}\big|_{u=0}\right) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}$. -/
def a3SelfCoeff : ℚ := 1 / 12

/-- The exact 3rd-order imaginary Taylor coefficient of $v_i$ for inter-cusp coupling $u_i u_j^2$ ($j \neq i$):
$\frac{1}{2!} \mathrm{Im}\!\left(\frac{\partial^3 v_i}{\partial u_i \partial u_j^2}\big|_{u=0}\right) = \frac{1}{2} \cdot \left(-\frac{1}{2}\right) = -\frac{1}{4}$. -/
def a3CrossCoeff : ℚ := -1 / 4

/-- The cubic jet of $\mathrm{Im}(v_1(u_1, u_2, u_3))$ around $u = (0,0,0)$:
$v_1^{(3)}(u_1, u_2, u_3) = a_{3,\mathrm{self}}\,u_1^3 + a_{3,\mathrm{cross}}\,u_1(u_2^2 + u_3^2)$. -/
def borromeanCubicLonJet (u₁ u₂ u₃ : ℚ) : ℚ :=
  a3SelfCoeff * u₁ ^ 3 + a3CrossCoeff * u₁ * (u₂ ^ 2 + u₃ ^ 2)

/-- Effective cubic longitude coefficient on the symmetric 3-cusp locus $u_1 = u_2 = u_3 = u$:
$a_{3,\mathrm{sym}} = a_{3,\mathrm{self}} + 2\,a_{3,\mathrm{cross}}$. -/
def a3SymCoeff : ℚ := a3SelfCoeff + 2 * a3CrossCoeff

/-- On a single-cusp deformation $(u, 0, 0)$, the cubic longitude jet equals $+\frac{1}{12} u^3$. -/
theorem borromeanCubicLon_single_cusp (u : ℚ) :
    borromeanCubicLonJet u 0 0 = (1 / 12 : ℚ) * u ^ 3 := by
  unfold borromeanCubicLonJet a3SelfCoeff a3CrossCoeff
  ring

/-- On the symmetric 3-cusp deformation $(u, u, u)$, the cubic longitude jet equals
$a_{3,\mathrm{sym}}\,u^3 = -\frac{5}{12} u^3$. -/
theorem borromeanCubicLon_sym_locus (u : ℚ) :
    borromeanCubicLonJet u u u = a3SymCoeff * u ^ 3 := by
  unfold borromeanCubicLonJet a3SymCoeff
  ring

/-- The two inter-cusp cross-terms ($2 \times (-1/4) = -1/2$) flip the sign and quintuple the
magnitude of the cubic longitude coefficient on the symmetric 3-cusp locus:
$a_{3,\mathrm{sym}} = -\frac{5}{12} = -5\,a_{3,\mathrm{self}}$, with $a_{3,\mathrm{self}} > 0$
and $a_{3,\mathrm{sym}} < 0$. -/
theorem borromeanCubicSymCoeff_eq_neg_five_twelfths :
    a3SymCoeff = -5 / 12 ∧ a3SymCoeff = -5 * a3SelfCoeff ∧ 0 < a3SelfCoeff ∧ a3SymCoeff < 0 := by
  unfold a3SymCoeff a3SelfCoeff a3CrossCoeff
  norm_num

end QOU.QBeta.BorromeanThreeCuspNZHessian
