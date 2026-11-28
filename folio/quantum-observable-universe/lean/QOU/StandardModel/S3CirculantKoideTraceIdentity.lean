/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.Observations.InhomogeneousLeptonLoopResolvent
import QOU.StandardModel.Photon
import QOU.StandardModel.KoideSingletDoubletEquipartition

set_option autoImplicit false

/-!
# $S_3$-Equivariant / $\mathbb{Z}_3$-Circulant Mass Matrix & Algebraic Koide Trace-to-Norm Test

Workstream W6 / Open Gap 2 Backup (Option 2B, bean `qou-j96h`). Formalizes the exact algebraic
structure of $3 \times 3$ $\mathbb{Z}_3$-circulant and $S_3$-equivariant square-root mass operators
$S(a, b, c) = a I_3 + b C + c C^2$ on Bring's 3-generation subspace `projGen3`, proves the Koide
`2/3` trace-to-norm identity and quadratic $\sqrt{m_\tau}$ resolvent over generic commutative rings
and fields, proves the unbroken-$S_3$ doublet degeneracy obstruction, and tests QOU's canonical
$H_3(q)$ / $TL_3(q)$ operators (`stepPlus`, `r21step`, `y3`, `y21`) for finite-$q$ singlet–doublet
equipartition.

Every declaration in this module is stated over a generic `[CommRing R]`, `[Field F]`, or ordered
field `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (`AGENTS.md §7c`: zero `ℝ`, zero empirical
literals, zero `sorry`, zero custom axioms).

## Main Results

1. **§1 — $3 \times 3$ Circulant Square-Root Mass Algebra & Hermitian `QuadI R` Norm (`[CommRing R]`):**
   - Cyclic shift $C$ (`cyclicShift3_cube`, `trace_cyclicShift3`) and circulant matrix
     `circulant3 a b c = a • 1 + b • C + c • C²` (`circulant3_mul`, `circulant3_comm`,
     `trace_circulant3`, `trace_circulant3_sq`, `trace_transpose_mul_circulant3`, `det_circulant3`).
   - Hermitian circulant `hermCirculant3 a b` over the generic Gaussian ring `QuadI R` ($R[i]$):
     `hermCirculant3_isHermitian`, `trace_hermCirculant3`, `trace_hermCirculant3_dagger_mul`,
     `trace_hermCirculant3_sq` ($\mathrm{Tr}(S^\dagger S) = \mathrm{Tr}(S^2) = 3(a^2 + 2|b|^2)$),
     plus Fourier / cube-root-of-unity eigenvector & power-sum identities (`circulant3_eigenvec`,
     `circulant3_eigensum_and_sq_sum`).

2. **§2 — Division-Free Koide Trace-to-Norm Identity & Singlet–Doublet Equipartition on `projGen3`:**
   - Division-free polynomial identity `koide_circulant_poly_identity`:
     $3\,\mathrm{Tr}(S(a, b, c)^2) - 2\,(\mathrm{Tr}\,S(a, b, c))^2 = 9(2bc - a^2)$ over any
     `[CommRing R]`.
   - Generic-field equivalence `koideCirculantRatio_eq_two_thirds_iff`:
     $Q_{\mathrm{Koide}}(a, r^2) = \frac{1 + 2r^2/a^2}{3} = \frac{2}{3} \iff 2r^2 = a^2$.
   - Orthogonal root-mass decomposition $\lambda = \lambda_{\mathrm{dem}} + \lambda_{\mathrm{doublet}}$
     and embedding into Bring's 3-generation subspace `projGen3 = projDem1 + projDoublet2` inside
     $V_{\mathrm{std}} \subset F^5$: `koideVecRatio_eq_two_thirds_iff_equipartition` proves
     $Q_{\mathrm{Koide}}(\lambda) = 2/3 \iff \|\lambda_{\mathrm{doublet}}\|_3^2 = \|\lambda_{\mathrm{dem}}\|_3^2$,
     while `bring_projGen3_ambient_metric_stretch` proves that the ambient $F^5$ dot product stretches
     `demVec3 = (1, 1, 1, -3, 0)` by an exact factor of $4$ (`normSq5 (projDem1 y) = 4 * normSq3 (demProj3 λ)`).

3. **§3 — Unbroken $S_3$-Equivariance Commutant & Doublet Mass Degeneracy Obstruction (`[CommRing R]`):**
   - `commutes_s3_iff_eq_symmetric_circulant`: $M \in \mathrm{Mat}_{3\times 3}(R)$ commutes with the
     full $S_3$ permutation action (`cyclicShift3` and `swap01`) iff $M = S(a, b, b)$.
   - `symmetric_circulant_doublet_degeneracy`: every $S_3$-equivariant operator has a 2D degenerate
     eigenspace at eigenvalue $a - b$ (`(M - (a + 2b)I)(M - (a - b)I) = 0`), proving that splitting
     all three charged-lepton masses strictly requires chiral breaking $S_3 \downarrow A_3 \cong \mathbb{Z}_3$
     ($b \neq c$).

4. **§4 — Exact Koide Quadratic Resolvent Identity (`[CommRing R]` / `[Field F]`):**
   - `koide_quadratic_resolvent_ring_identity` & `koide_quadratic_completed_square_and_discriminant`:
     $3(u^2 + v^2 + x^2) - 2(u + v + x)^2 = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv)
     = (x - 2(u + v))^2 - 3(u^2 + 4uv + v^2)$ with discriminant $\Delta(u, v) = 12(u^2 + 4uv + v^2)$,
     plus `[Field F]` root & Vieta characterization (`koideVecRatio_two_thirds_iff_resolvent_zero`,
     `koide_resolvent_roots_and_vieta`).

5. **§5 — Structural $H_3(q)$ & $TL_3(q)$ Operator Tests & Finite-$q$ Departure (`[Field K]`):**
   - `stepPlus_at_one_eq_cyclicShift3` & `trace_stepPlus_hecke`: QOU's ruled chiral photon vertex
     $\sigma_0 \sigma_1^{-1}$ on $M_{+1}$ (`stepPlus q (q - q⁻¹)`) reduces at $q = 1$ to `cyclicShift3`,
     acquires non-zero trace $-(q - q^{-1})^2$ for $q \neq \pm 1$, and keeps unit-circle doublet
     eigenvalues across the entire cone window $0 < q - q^{-1} < 1$ (`r21step_disc_neg_on_cone`).
   - `tl3_classical_equipartition_at_one` & `tl3_strict_departure_from_two_thirds`: Temperley–Lieb
     Convention-D Wedderburn weights `y3(q)` vs `2 y21(q)` satisfy **exact** singlet–doublet
     equipartition $1/2 = 1/2$ ($Q_{\mathrm{TL3}}(1) = 2/3$) at $q = 1$, but for **every** $q > 1$
     in an ordered field satisfy $2 y_{21}(q) < y_3(q)$ and
     $2/3 - Q_{\mathrm{TL3}}(q) = \frac{(q - q^{-1})^2}{3(q^2 + q^{-2})} > 0$.

6. **§6 — Rule-13a Zero-Instance Hypothesis Class (`KoideCirculantEquipartitionHypothesis`):**
   - Encapsulates any unproved finite-$q$ Hermitian circulant equipartition mechanism without
     instances and derives the quadratic $\sqrt{m_\tau}$ resolvent equation non-vacuously from the
     equipartition and moment axioms.

-- Ref: [koide1983plb] Y. Koide, Phys. Lett. B 120 (1983) 161–165, doi:10.1016/0370-2693(83)90644-5
-- Ref: [koide1983prd] Y. Koide, Phys. Rev. D 28 (1983) 252–254, doi:10.1103/PhysRevD.28.252
-- Ref: [koide1990mpla] Y. Koide, Mod. Phys. Lett. A 5 (1990) 2319–2323, doi:10.1142/S0217732390002663
-- Ref: [foot1994] R. Foot, arXiv:hep-ph/9402242, doi:10.48550/arXiv.hep-ph/9402242
-- Ref: [harrison2002] P. F. Harrison, D. H. Perkins, W. G. Scott, Phys. Lett. B 530 (2002) 167–173, doi:10.1016/S0370-2693(02)01336-9
-- Ref: [rodejohann2011] W. Rodejohann, H. Zhang, Phys. Lett. B 698 (2011) 152–156, doi:10.1016/j.physletb.2011.03.007
-- Ref: [leitner2026] QOU Open Gap 2 Backup, bean qou-j96h
-/

namespace QOU.StandardModel.S3CirculantKoideTraceIdentity

open scoped BigOperators
open Matrix
open QOU.QBeta.WeightSpaceNucleon
open QOU.QBeta.WeightSpaceMarkov
open QOU.Observations.ElectronUnitSplit

/-! ## Section 1: $3 \times 3$ Circulant Square-Root Mass Algebra & Hermitian `QuadI R` Norm -/

section CirculantRingAlgebra

variable {R : Type*} [CommRing R]

/-- Cyclic shift generator $C = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$
of the 3-generation $\mathbb{Z}_3$-circulant algebra. -/
def cyclicShift3 (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  !![0, 1, 0; 0, 0, 1; 1, 0, 0]

/-- Explicit matrix entries of $C^2$. -/
theorem cyclicShift3_sq :
    (cyclicShift3 R) ^ 2 = !![(0 : R), 0, 1; 1, 0, 0; 0, 1, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sq, cyclicShift3, Matrix.mul_apply, Fin.sum_univ_three]

/-- Period-3 identity $C^3 = I_3$. -/
theorem cyclicShift3_cube :
    (cyclicShift3 R) ^ 3 = (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pow_three, cyclicShift3, Matrix.mul_apply, Fin.sum_univ_three]

/-- Orthogonality / inverse transpose relations $C^\top = C^2$ and $(C^2)^\top = C$. -/
theorem cyclicShift3_transpose :
    (cyclicShift3 R)ᵀ = (cyclicShift3 R) ^ 2 ∧
      ((cyclicShift3 R) ^ 2)ᵀ = cyclicShift3 R := by
  rw [cyclicShift3_sq]
  refine ⟨?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> simp [cyclicShift3, Matrix.transpose_apply]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [cyclicShift3, Matrix.transpose_apply]

/-- Traces of $I_3$, $C$, and $C^2$: $\mathrm{Tr}(I_3) = 3$, $\mathrm{Tr}(C) = \mathrm{Tr}(C^2) = 0$. -/
theorem trace_cyclicShift3 :
    (1 : Matrix (Fin 3) (Fin 3) R).trace = 3 ∧
      (cyclicShift3 R).trace = 0 ∧
      ((cyclicShift3 R) ^ 2).trace = 0 := by
  rw [cyclicShift3_sq]
  refine ⟨?_, ?_, ?_⟩
  · simp
  · simp [cyclicShift3, Matrix.trace_fin_three]
  · simp [Matrix.trace_fin_three]

/-- General $3 \times 3$ circulant matrix $S(a, b, c) = a I_3 + b C + c C^2$. -/
def circulant3 (a b c : R) : Matrix (Fin 3) (Fin 3) R :=
  a • (1 : Matrix (Fin 3) (Fin 3) R) + b • cyclicShift3 R + c • (cyclicShift3 R) ^ 2

/-- Explicit $3 \times 3$ array form of $S(a, b, c)$. -/
theorem circulant3_eq_mat (a b c : R) :
    circulant3 a b c = !![a, b, c; c, a, b; b, c, a] := by
  unfold circulant3
  rw [cyclicShift3_sq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [cyclicShift3]

/-- Transpose of a circulant swaps the two off-diagonal shift coefficients:
$S(a, b, c)^\top = S(a, c, b)$. -/
theorem circulant3_transpose (a b c : R) :
    (circulant3 a b c)ᵀ = circulant3 a c b := by
  rw [circulant3_eq_mat, circulant3_eq_mat]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.transpose_apply]

/-- Exact group-ring multiplication law in $\mathcal{C}_3(R) \cong R[\mathbb{Z}_3]$. -/
theorem circulant3_mul (a₁ b₁ c₁ a₂ b₂ c₂ : R) :
    circulant3 a₁ b₁ c₁ * circulant3 a₂ b₂ c₂ =
      circulant3 (a₁ * a₂ + b₁ * c₂ + c₁ * b₂)
        (a₁ * b₂ + b₁ * a₂ + c₁ * c₂)
        (a₁ * c₂ + b₁ * b₂ + c₁ * a₂) := by
  rw [circulant3_eq_mat, circulant3_eq_mat, circulant3_eq_mat]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_three] <;> ring

/-- Commutativity of $3 \times 3$ circulant matrices over any commutative ring. -/
theorem circulant3_comm (a₁ b₁ c₁ a₂ b₂ c₂ : R) :
    circulant3 a₁ b₁ c₁ * circulant3 a₂ b₂ c₂ =
      circulant3 a₂ b₂ c₂ * circulant3 a₁ b₁ c₁ := by
  rw [circulant3_mul, circulant3_mul]
  congr 1 <;> ring

/-- **Exact trace of $S(a, b, c)$:** $\mathrm{Tr}(S(a, b, c)) = 3a$. -/
theorem trace_circulant3 (a b c : R) :
    (circulant3 a b c).trace = 3 * a := by
  rw [circulant3_eq_mat]
  simp [Matrix.trace_fin_three]
  ring

/-- **Exact square of $S(a, b, c)$:**
$S(a, b, c)^2 = S(a^2 + 2bc,\; 2ab + c^2,\; 2ac + b^2)$. -/
theorem circulant3_sq (a b c : R) :
    circulant3 a b c ^ 2 =
      circulant3 (a ^ 2 + 2 * b * c) (2 * a * b + c ^ 2) (2 * a * c + b ^ 2) := by
  rw [sq, circulant3_mul]
  congr 1 <;> ring

/-- **Exact trace of $S(a, b, c)^2$:** $\mathrm{Tr}(S(a, b, c)^2) = 3(a^2 + 2bc)$. -/
theorem trace_circulant3_sq (a b c : R) :
    (circulant3 a b c ^ 2).trace = 3 * (a ^ 2 + 2 * b * c) := by
  rw [circulant3_sq, trace_circulant3]

/-- **Real Frobenius norm squared:** $\mathrm{Tr}(S(a, b, c)^\top S(a, b, c)) = 3(a^2 + b^2 + c^2)$. -/
theorem trace_transpose_mul_circulant3 (a b c : R) :
    ((circulant3 a b c)ᵀ * circulant3 a b c).trace = 3 * (a ^ 2 + b ^ 2 + c ^ 2) := by
  rw [circulant3_transpose, circulant3_mul, trace_circulant3]
  ring

/-- **Exact circulant determinant:** $\det S(a, b, c) = a^3 + b^3 + c^3 - 3abc$. -/
theorem det_circulant3 (a b c : R) :
    (circulant3 a b c).det = a ^ 3 + b ^ 3 + c ^ 3 - 3 * a * b * c := by
  rw [circulant3_eq_mat]
  simp [Matrix.det_fin_three]
  ring

/-- **Fourier / cube-root-of-unity eigenvectors of $S(a, b, c)$** over any `[CommRing R]`
admitting $\omega \in R$ with $\omega^3 = 1$: the vectors $(1, 1, 1)$, $(1, \omega, \omega^2)$, and
$(1, \omega^2, \omega)$ have exact eigenvalues $a + b + c$, $a + b\omega + c\omega^2$, and
$a + b\omega^2 + c\omega$. -/
theorem circulant3_eigenvec (a b c ω : R) (hω3 : ω ^ 3 = 1) :
    (circulant3 a b c).mulVec ![1, 1, 1] = (a + b + c) • ![1, 1, 1] ∧
      (circulant3 a b c).mulVec ![1, ω, ω ^ 2] =
        (a + b * ω + c * ω ^ 2) • ![1, ω, ω ^ 2] ∧
      (circulant3 a b c).mulVec ![1, ω ^ 2, ω] =
        (a + b * ω ^ 2 + c * ω) • ![1, ω ^ 2, ω] := by
  rw [circulant3_eq_mat]
  refine ⟨?_, ?_, ?_⟩
  · ext i; fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  · ext i; fin_cases i
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
      linear_combination -c * hω3
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
      linear_combination -(b + c * ω) * hω3
  · ext i; fin_cases i
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
      linear_combination -(b * ω + c) * hω3
    · simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three]
      linear_combination -b * hω3

/-- **Spectral power-sum matching:** whenever $1 + \omega + \omega^2 = 0$, the three circulant
Fourier eigenvalues $\lambda_0 = a + b + c$, $\lambda_1 = a + b\omega + c\omega^2$, and
$\lambda_2 = a + b\omega^2 + c\omega$ satisfy $\sum_{k=0}^2 \lambda_k = 3a$ and
$\sum_{k=0}^2 \lambda_k^2 = 3(a^2 + 2bc)$. -/
theorem circulant3_eigensum_and_sq_sum (a b c ω : R) (hω : 1 + ω + ω ^ 2 = 0) :
    let lam0 := a + b + c
    let lam1 := a + b * ω + c * ω ^ 2
    let lam2 := a + b * ω ^ 2 + c * ω
    lam0 + lam1 + lam2 = 3 * a ∧
      lam0 ^ 2 + lam1 ^ 2 + lam2 ^ 2 = 3 * (a ^ 2 + 2 * b * c) := by
  dsimp only
  refine ⟨?_, ?_⟩
  · linear_combination (b + c) * hω
  · linear_combination
      (2 * a * b + 2 * a * c + (b ^ 2 + c ^ 2) * (1 - ω + ω ^ 2) + 4 * b * c * (ω - 1)) * hω

end CirculantRingAlgebra

/-! ### Generic Gaussian Extension `QuadI R` ($R[i]$, $i^2 = -1$) for Hermitian Circulants -/

section HermitianCirculantQuadI

/-- Generic Gaussian extension $R[i]$ (`i² = -1`) over any `[CommRing R]`, avoiding `ℂ`/`ℝ` (`§7c`). -/
@[ext]
structure QuadI (R : Type*) where
  re : R
  im : R
  deriving DecidableEq

namespace QuadI

variable {R : Type*} [CommRing R]

def ofReal (x : R) : QuadI R := ⟨x, 0⟩
def conj (z : QuadI R) : QuadI R := ⟨z.re, -z.im⟩
def normSq (z : QuadI R) : R := z.re ^ 2 + z.im ^ 2

instance : Zero (QuadI R) := ⟨⟨0, 0⟩⟩
instance : One (QuadI R) := ⟨⟨1, 0⟩⟩
instance : Add (QuadI R) := ⟨fun z w => ⟨z.re + w.re, z.im + w.im⟩⟩
instance : Neg (QuadI R) := ⟨fun z => ⟨-z.re, -z.im⟩⟩
instance : Sub (QuadI R) := ⟨fun z w => ⟨z.re - w.re, z.im - w.im⟩⟩
instance : Mul (QuadI R) := ⟨fun z w => ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩⟩

@[simp] lemma zero_re : (0 : QuadI R).re = 0 := rfl
@[simp] lemma zero_im : (0 : QuadI R).im = 0 := rfl
@[simp] lemma one_re : (1 : QuadI R).re = 1 := rfl
@[simp] lemma one_im : (1 : QuadI R).im = 0 := rfl
@[simp] lemma add_re (z w : QuadI R) : (z + w).re = z.re + w.re := rfl
@[simp] lemma add_im (z w : QuadI R) : (z + w).im = z.im + w.im := rfl
@[simp] lemma neg_re (z : QuadI R) : (-z).re = -z.re := rfl
@[simp] lemma neg_im (z : QuadI R) : (-z).im = -z.im := rfl
@[simp] lemma sub_re (z w : QuadI R) : (z - w).re = z.re - w.re := rfl
@[simp] lemma sub_im (z w : QuadI R) : (z - w).im = z.im - w.im := rfl
@[simp] lemma mul_re (z w : QuadI R) : (z * w).re = z.re * w.re - z.im * w.im := rfl
@[simp] lemma mul_im (z w : QuadI R) : (z * w).im = z.re * w.im + z.im * w.re := rfl
@[simp] lemma ofReal_re (x : R) : (ofReal x).re = x := rfl
@[simp] lemma ofReal_im (x : R) : (ofReal x).im = 0 := rfl
@[simp] lemma conj_re (z : QuadI R) : (conj z).re = z.re := rfl
@[simp] lemma conj_im (z : QuadI R) : (conj z).im = -z.im := rfl

instance : CommRing (QuadI R) where
  add := (· + ·)
  add_assoc a b c := by ext <;> simp <;> ring
  zero := 0
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  nsmul := nsmulRec
  neg := Neg.neg
  sub := (· - ·)
  sub_eq_add_neg a b := by ext <;> simp [sub_eq_add_neg]
  zsmul := zsmulRec
  neg_add_cancel a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  mul := (· * ·)
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp
  mul_assoc a b c := by ext <;> simp <;> ring
  one := 1
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  mul_comm a b := by ext <;> simp <;> ring

@[simp] theorem conj_conj (z : QuadI R) : conj (conj z) = z := by
  ext <;> simp

@[simp] theorem conj_ofReal (x : R) : conj (ofReal x) = ofReal x := by
  ext <;> simp

theorem mul_conj (z : QuadI R) : z * conj z = ofReal (normSq z) := by
  ext <;> simp [normSq] <;> ring

theorem ofReal_add (x y : R) : ofReal (x + y) = ofReal x + ofReal y := by
  ext <;> simp

theorem ofReal_mul (x y : R) : ofReal (x * y) = ofReal x * ofReal y := by
  ext <;> simp

theorem two_eq_ofReal : (2 : QuadI R) = ofReal 2 := by
  rw [show (2 : QuadI R) = 1 + 1 by norm_num, show (2 : R) = 1 + 1 by norm_num]
  ext <;> simp

theorem three_eq_ofReal : (3 : QuadI R) = ofReal 3 := by
  rw [show (3 : QuadI R) = 1 + 1 + 1 by norm_num, show (3 : R) = 1 + 1 + 1 by norm_num]
  ext <;> simp

end QuadI

variable {R : Type*} [CommRing R]

/-- Conjugate transpose $M^\dagger$ over `QuadI R`. -/
def conjTransposeQuadI {m n : Type*} (M : Matrix m n (QuadI R)) : Matrix n m (QuadI R) :=
  fun i j => QuadI.conj (M j i)

/-- Hermitian $3 \times 3$ circulant square-root mass operator
$S_{\mathrm{Herm}}(a, b) = a I_3 + b C + \bar{b} C^2$ over `QuadI R`. -/
def hermCirculant3 (a : R) (b : QuadI R) : Matrix (Fin 3) (Fin 3) (QuadI R) :=
  circulant3 (QuadI.ofReal a) b (QuadI.conj b)

/-- $S_{\mathrm{Herm}}(a, b)$ is identically Hermitian ($S^\dagger = S$) over any `[CommRing R]`. -/
theorem hermCirculant3_isHermitian (a : R) (b : QuadI R) :
    conjTransposeQuadI (hermCirculant3 a b) = hermCirculant3 a b := by
  unfold hermCirculant3
  rw [circulant3_eq_mat]
  refine Matrix.ext fun i j => ?_
  fin_cases i <;> fin_cases j <;> ext <;> simp [conjTransposeQuadI]

/-- Exact trace $\mathrm{Tr}(S_{\mathrm{Herm}}(a, b)) = 3a$. -/
theorem trace_hermCirculant3 (a : R) (b : QuadI R) :
    (hermCirculant3 a b).trace = QuadI.ofReal (3 * a) := by
  unfold hermCirculant3
  rw [trace_circulant3, QuadI.three_eq_ofReal, ← QuadI.ofReal_mul]

/-- **Exact Frobenius / square-trace identity for Hermitian circulants:**
$\mathrm{Tr}(S^\dagger S) = \mathrm{Tr}(S^2) = 3(a^2 + 2|b|^2)$. -/
theorem trace_hermCirculant3_dagger_mul_and_sq (a : R) (b : QuadI R) :
    (conjTransposeQuadI (hermCirculant3 a b) * hermCirculant3 a b).trace =
        QuadI.ofReal (3 * (a ^ 2 + 2 * QuadI.normSq b)) ∧
      (hermCirculant3 a b ^ 2).trace =
        QuadI.ofReal (3 * (a ^ 2 + 2 * QuadI.normSq b)) := by
  have hh := hermCirculant3_isHermitian a b
  have hsq : (hermCirculant3 a b ^ 2).trace =
      QuadI.ofReal (3 * (a ^ 2 + 2 * QuadI.normSq b)) := by
    unfold hermCirculant3
    rw [trace_circulant3_sq, mul_assoc, QuadI.mul_conj, sq (QuadI.ofReal a),
      ← QuadI.ofReal_mul, QuadI.two_eq_ofReal, ← QuadI.ofReal_mul,
      ← QuadI.ofReal_add, QuadI.three_eq_ofReal, ← QuadI.ofReal_mul]
    congr 1
    ring
  refine ⟨?_, hsq⟩
  rw [hh, ← sq, hsq]

end HermitianCirculantQuadI

/-! ## Section 2: Division-Free Koide Trace-to-Norm Identity & Singlet–Doublet Equipartition -/

section KoideTraceToNorm

/-- **Division-free Koide trace-to-norm polynomial identity over any `[CommRing R]`:**
$3\,\mathrm{Tr}(S(a, b, c)^2) - 2\,(\mathrm{Tr}\,S(a, b, c))^2 = 9(2bc - a^2)$. -/
theorem koide_circulant_poly_identity {R : Type*} [CommRing R] (a b c : R) :
    3 * (circulant3 a b c ^ 2).trace - 2 * (circulant3 a b c).trace ^ 2 =
      9 * (2 * b * c - a ^ 2) := by
  rw [trace_circulant3_sq, trace_circulant3]
  ring

/-- Division-free Hermitian circulant specialization over `QuadI R`:
$3\,\mathrm{Re}\,\mathrm{Tr}(S^\dagger S) - 2\,(\mathrm{Re}\,\mathrm{Tr}\,S)^2 = 9(2|b|^2 - a^2)$. -/
theorem koide_hermCirculant_poly_identity {R : Type*} [CommRing R] (a : R) (b : QuadI R) :
    3 * ((conjTransposeQuadI (hermCirculant3 a b) * hermCirculant3 a b).trace).re -
        2 * ((hermCirculant3 a b).trace).re ^ 2 =
      9 * (2 * QuadI.normSq b - a ^ 2) := by
  rw [(trace_hermCirculant3_dagger_mul_and_sq a b).1, trace_hermCirculant3]
  simp
  ring

/-- Algebraic Koide ratio $\frac{\mathrm{Tr}(S^2)}{(\mathrm{Tr}\,S)^2} = \frac{3(a^2 + 2 r^2)}{(3a)^2}$
over a generic `[Field F]` (`rSq = r² = |b|²`). -/
def koideCirculantRatio {F : Type*} [Field F] (a rSq : F) : F :=
  (3 * (a ^ 2 + 2 * rSq)) / (3 * a) ^ 2

/-- Simplified form $Q_{\mathrm{Koide}}(a, r^2) = \frac{1 + 2 r^2 / a^2}{3}$. -/
theorem koideCirculantRatio_eq {F : Type*} [Field F] {a : F} (rSq : F)
    (h3 : (3 : F) ≠ 0) (ha : a ≠ 0) :
    koideCirculantRatio a rSq = (1 + 2 * rSq / a ^ 2) / 3 := by
  unfold koideCirculantRatio
  field_simp [h3, ha]

/-- **Exact Koide `2/3` Trace-to-Norm Equivalence (`[koide1983prd]`, `[foot1994]`):**
over any `[Field F]` (`char F ≠ 3`, `a ≠ 0`),
$Q_{\mathrm{Koide}}(a, r^2) = \frac{2}{3} \iff 2 r^2 = a^2$ (exact equipartition between the
diagonal democratic self-coupling norm $3a^2$ and the off-diagonal $\mathbb{Z}_3$-hopping norm
$6r^2$). -/
theorem koideCirculantRatio_eq_two_thirds_iff {F : Type*} [Field F] {a : F} (r : F)
    (h3 : (3 : F) ≠ 0) (ha : a ≠ 0) :
    koideCirculantRatio a (r ^ 2) = 2 / 3 ↔ 2 * r ^ 2 = a ^ 2 := by
  unfold koideCirculantRatio
  have h9a : (3 * a) ^ 2 ≠ 0 := pow_ne_zero 2 (mul_ne_zero h3 ha)
  have h9 : (9 : F) ≠ 0 := by
    have e : (9 : F) = 3 * 3 := by norm_num
    rw [e]; exact mul_ne_zero h3 h3
  constructor
  · intro h
    rw [div_eq_div_iff h9a h3] at h
    have hdiff : 9 * (2 * r ^ 2 - a ^ 2) = 0 := by linear_combination h
    have hz := (mul_eq_zero.mp hdiff).resolve_left h9
    linear_combination hz
  · intro h
    rw [div_eq_div_iff h9a h3]
    linear_combination 9 * h

/-! ### Root-Mass Vector Space & Bring's 3-Generation Subspace (`projGen3 = projDem1 + projDoublet2`) -/

/-- Squared Euclidean norm on `Fin 3 → R`. -/
def normSq3 {R : Type*} [CommRing R] (v : Fin 3 → R) : R :=
  v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2

/-- Squared Euclidean norm on Bring's ambient `Fin 5 → R`. -/
def normSq5 {R : Type*} [CommRing R] (v : Fin 5 → R) : R :=
  v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2

/-- Root-mass vector Koide ratio $Q(\lambda) = \frac{\lambda_0^2 + \lambda_1^2 + \lambda_2^2}{(\lambda_0 + \lambda_1 + \lambda_2)^2}$. -/
def koideVecRatio {F : Type*} [Field F] (lam : Fin 3 → F) : F :=
  normSq3 lam / (lam 0 + lam 1 + lam 2) ^ 2

/-- 1D $S_3$-invariant democratic singlet projection $\lambda_{\mathrm{dem}} = \frac{\sum_k \lambda_k}{3}(1,1,1)$. -/
def demProj3 {F : Type*} [Field F] (lam : Fin 3 → F) : Fin 3 → F :=
  fun _ => (lam 0 + lam 1 + lam 2) / 3

/-- 2D $S_3$-standard zero-sum doublet projection $\lambda_{\mathrm{doublet}} = \lambda - \lambda_{\mathrm{dem}}$. -/
def doubletProj3 {F : Type*} [Field F] (lam : Fin 3 → F) : Fin 3 → F :=
  fun i => lam i - demProj3 lam i

/-- Orthogonal Pythagorean split of $\lambda \in F^3$ into 1D democratic singlet and 2D zero-sum doublet. -/
theorem demProj3_doubletProj3_pythagorean_split {F : Type*} [Field F] (h3 : (3 : F) ≠ 0)
    (lam : Fin 3 → F) :
    demProj3 lam + doubletProj3 lam = lam ∧
      doubletProj3 lam 0 + doubletProj3 lam 1 + doubletProj3 lam 2 = 0 ∧
      demProj3 lam 0 * doubletProj3 lam 0 + demProj3 lam 1 * doubletProj3 lam 1 +
          demProj3 lam 2 * doubletProj3 lam 2 = 0 ∧
      normSq3 lam = normSq3 (demProj3 lam) + normSq3 (doubletProj3 lam) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i; simp [doubletProj3]
  · simp only [doubletProj3, demProj3]; field_simp [h3]; ring
  · simp only [doubletProj3, demProj3]; field_simp [h3]; ring
  · simp only [normSq3, doubletProj3, demProj3]; field_simp [h3]; ring

/-- **Geometric Foot–Koide Singlet–Doublet Equipartition Theorem (`[foot1994]`):**
for any root-mass vector $\lambda \in F^3$ with $\sum_{k=0}^2 \lambda_k \neq 0$ (`(3 : F) ≠ 0`),
$Q_{\mathrm{Koide}}(\lambda) = \frac{2}{3} \iff \|\lambda_{\mathrm{doublet}}\|_3^2 = \|\lambda_{\mathrm{dem}}\|_3^2$. -/
theorem koideVecRatio_eq_two_thirds_iff_equipartition {F : Type*} [Field F]
    (h3 : (3 : F) ≠ 0) {lam : Fin 3 → F} (hsum : lam 0 + lam 1 + lam 2 ≠ 0) :
    koideVecRatio lam = 2 / 3 ↔ normSq3 (doubletProj3 lam) = normSq3 (demProj3 lam) := by
  have hpyth := (demProj3_doubletProj3_pythagorean_split h3 lam).2.2.2
  have hdem : normSq3 (demProj3 lam) = (lam 0 + lam 1 + lam 2) ^ 2 / 3 := by
    simp only [normSq3, demProj3]; field_simp [h3]; ring
  unfold koideVecRatio
  rw [hpyth, hdem]
  have hs2 : (lam 0 + lam 1 + lam 2) ^ 2 ≠ 0 := pow_ne_zero 2 hsum
  constructor
  · intro h
    rw [div_eq_div_iff hs2 h3] at h
    field_simp [h3] at h ⊢
    linear_combination h
  · intro h
    rw [h]
    field_simp [h3, hs2]
    ring

/-- Membership in Bring's 4D canonical differential space $V_{\mathrm{std}} = \{\sum_{i=0}^4 x_i = 0\}$. -/
def inBringStd {R : Type*} [CommRing R] (x : Fin 5 → R) : Prop :=
  x 0 + x 1 + x 2 + x 3 + x 4 = 0

/-- $S_4$-invariant singlet vector $(1, 1, 1, 1, -4) \in V_{\mathrm{std}}$ and $S_4$-equivariant
3-generation projector `projGen3` (`4 → 3 ⊕ 1`). -/
def singletVec4 {R : Type*} [CommRing R] : Fin 5 → R := ![1, 1, 1, 1, -4]

def projGen3 {F : Type*} [Field F] (x : Fin 5 → F) : Fin 5 → F :=
  fun i => x i + (x 4 / 4) * singletVec4 i

/-- $S_3$-invariant democratic line generator $(1, 1, 1, -3, 0)$ inside `projGen3` and the
$S_3$-equivariant projectors `projDem1` and `projDoublet2` (`3 → 2 ⊕ 1`). -/
def demVec3 {R : Type*} [CommRing R] : Fin 5 → R := ![1, 1, 1, -3, 0]

def projDem1 {F : Type*} [Field F] (y : Fin 5 → F) : Fin 5 → F :=
  fun i => -(y 3 / 3) * demVec3 i

def projDoublet2 {F : Type*} [Field F] (y : Fin 5 → F) : Fin 5 → F :=
  fun i => y i - projDem1 y i

/-- $S_3$-equivariant embedding of 3-generation coordinates $\lambda \in F^3$ into Bring's 3D
generation subspace `projGen3`: $\iota(\lambda) = (\lambda_0, \lambda_1, \lambda_2, -(\lambda_0 + \lambda_1 + \lambda_2), 0)$. -/
def embedGen3 {R : Type*} [CommRing R] (lam : Fin 3 → R) : Fin 5 → R :=
  ![lam 0, lam 1, lam 2, -(lam 0 + lam 1 + lam 2), 0]

/-- **Bring `projGen3` Embedding & Ambient-$F^5$ Metric Stretch Identity:**
1. `embedGen3 lam` lies in $V_{\mathrm{std}}$ and is fixed by `projGen3`.
2. `projDoublet2` and `projDem1` match `doubletProj3` and `demProj3` on the first three coordinates.
3. Because `demVec3 = (1, 1, 1, -3, 0)` has ambient norm squared $12 = 4 \cdot 3$, the ambient
   $S_5$-invariant inner product on $F^5$ stretches the singlet norm squared by an **exact factor
   of $4$** (`normSq5 (projDem1 (embedGen3 lam)) = 4 * normSq3 (demProj3 lam)`), whereas
   `normSq5 (projDoublet2 (embedGen3 lam)) = normSq3 (doubletProj3 lam)`. Consequently,
   naive ambient-$F^5$ equipartition `normSq5 (projDoublet2 y) = normSq5 (projDem1 y)` would give
   $Q = 5/3 \neq 2/3$! -/
theorem bring_projGen3_ambient_metric_stretch {F : Type*} [Field F]
    (h3 : (3 : F) ≠ 0) (lam : Fin 3 → F) :
    inBringStd (embedGen3 lam) ∧
      projGen3 (embedGen3 lam) = embedGen3 lam ∧
      normSq5 (projDoublet2 (embedGen3 lam)) = normSq3 (doubletProj3 lam) ∧
      normSq5 (projDem1 (embedGen3 lam)) = 4 * normSq3 (demProj3 lam) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold inBringStd embedGen3
    simp
    ring
  · ext i
    fin_cases i <;> simp [projGen3, embedGen3, singletVec4]
  · simp only [normSq5, normSq3, projDoublet2, projDem1, embedGen3, demVec3, doubletProj3, demProj3]
    simp
    field_simp [h3]
    ring
  · simp only [normSq5, normSq3, projDem1, embedGen3, demVec3, demProj3]
    simp
    field_simp [h3]
    ring

end KoideTraceToNorm

/-! ## Section 3: Unbroken $S_3$-Equivariance Commutant & Doublet Degeneracy Obstruction -/

section S3EquivarianceObstruction

variable {R : Type*} [CommRing R]

/-- Permutation transposition $\tau_{01} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$,
which generates $S_3$ together with `cyclicShift3`. -/
def swap01 (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  !![0, 1, 0; 1, 0, 0; 0, 0, 1]

/-- Dihedral relations $\tau_{01}^2 = I_3$ and $\tau_{01} C \tau_{01} = C^2$ in $S_3$. -/
theorem swap01_relations :
    (swap01 R) ^ 2 = 1 ∧ swap01 R * cyclicShift3 R * swap01 R = (cyclicShift3 R) ^ 2 := by
  rw [cyclicShift3_sq]
  refine ⟨?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [sq, swap01, Matrix.mul_apply, Fin.sum_univ_three]
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [swap01, cyclicShift3, Matrix.mul_apply, Fin.sum_univ_three]

/-- **Exact $S_3$-Commutant Characterization:** over any `[CommRing R]`, a $3 \times 3$ matrix $M$
commutes with both `cyclicShift3` and `swap01` (hence with the full $S_3$ permutation action)
**if and only if** $M = S(a, b, b)$ for some $a, b \in R$. -/
theorem commutes_s3_iff_eq_symmetric_circulant (M : Matrix (Fin 3) (Fin 3) R) :
    (M * cyclicShift3 R = cyclicShift3 R * M ∧ M * swap01 R = swap01 R * M) ↔
      ∃ a b : R, M = circulant3 a b b := by
  constructor
  · rintro ⟨hC, hS⟩
    refine ⟨M 0 0, M 0 1, ?_⟩
    have h00 := congr_arg (fun X => X 0 0) hC
    have h01 := congr_arg (fun X => X 0 1) hC
    have h02 := congr_arg (fun X => X 0 2) hC
    have h10 := congr_arg (fun X => X 1 0) hC
    have h11 := congr_arg (fun X => X 1 1) hC
    have h12 := congr_arg (fun X => X 1 2) hC
    have hs20 := congr_arg (fun X => X 2 0) hS
    simp [cyclicShift3, swap01, Matrix.mul_apply, Fin.sum_univ_three] at h00 h01 h02 h10 h11 h12 hs20
    have ha1 : M 1 1 = M 0 0 := h01.symm
    have ha2 : M 2 2 = M 0 0 := h12.symm.trans ha1
    have hb20 : M 2 0 = M 0 1 := h10.symm.trans h02.symm
    have hb21 : M 2 1 = M 0 1 := hs20.trans hb20
    have hb10 : M 1 0 = M 0 1 := h11.trans hb21
    have hb02 : M 0 2 = M 0 1 := h00.trans hb10
    have hb12 : M 1 2 = M 0 1 := h02.symm
    rw [circulant3_eq_mat]
    ext i j
    fin_cases i <;> fin_cases j <;> simp [ha1, ha2, hb20, hb21, hb10, hb02, hb12]
  · rintro ⟨a, b, rfl⟩
    rw [circulant3_eq_mat]
    refine ⟨?_, ?_⟩
    · ext i j; fin_cases i <;> fin_cases j <;>
        simp [cyclicShift3, Matrix.mul_apply, Fin.sum_univ_three]
    · ext i j; fin_cases i <;> fin_cases j <;>
        simp [swap01, Matrix.mul_apply, Fin.sum_univ_three]

/-- **Unbroken $S_3$-Equivariance Forces Doublet Eigenvalue Degeneracy:**
every $S_3$-equivariant matrix $M = S(a, b, b)$ annihilates the quadratic polynomial
$(X - (a + 2b))(X - (a - b))$ and acts as the **same** scalar $a - b$ on both linearly independent
doublet root vectors $(1, -1, 0)$ and $(0, 1, -1)$. Hence unbroken $S_3$ symmetry cannot split
all three lepton generations ($m_e < m_\mu < m_\tau$); breaking $S_3 \downarrow A_3 \cong \mathbb{Z}_3$
($b \neq c$) is strictly required. -/
theorem symmetric_circulant_doublet_degeneracy (a b : R) :
    let M := circulant3 a b b
    M.mulVec ![1, 1, 1] = (a + 2 * b) • ![1, 1, 1] ∧
      M.mulVec ![1, -1, 0] = (a - b) • ![1, -1, 0] ∧
      M.mulVec ![0, 1, -1] = (a - b) • ![0, 1, -1] ∧
      (M - (a + 2 * b) • 1) * (M - (a - b) • 1) = 0 := by
  dsimp only
  rw [circulant3_eq_mat]
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i; fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  · ext i; fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  · ext i; fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> ring

end S3EquivarianceObstruction

/-! ## Section 4: Exact Koide Quadratic Resolvent Identity (`[CommRing R]` / `[Field F]`) -/

section KoideQuadraticResolvent

/-- Monic quadratic Koide resolvent polynomial solving for $x = \sqrt{m_3}$ given
$(u, v) = (\sqrt{m_1}, \sqrt{m_2})$:
$P_{\mathrm{Koide}}(u, v; x) = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv)$. -/
def koideResolventPoly {R : Type*} [CommRing R] (u v x : R) : R :=
  x ^ 2 - 4 * (u + v) * x + (u ^ 2 + v ^ 2 - 4 * u * v)

/-- **Exact Koide Quadratic Resolvent Identity over any `[CommRing R]`:**
$3(u^2 + v^2 + x^2) - 2(u + v + x)^2 = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv)$. -/
theorem koide_quadratic_resolvent_ring_identity {R : Type*} [CommRing R] (u v x : R) :
    3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v + x) ^ 2 = koideResolventPoly u v x := by
  unfold koideResolventPoly
  ring

/-- **Completed-Square & Discriminant Identity over any `[CommRing R]`:**
$P_{\mathrm{Koide}}(u, v; x) = (x - 2(u + v))^2 - 3(u^2 + 4uv + v^2)$ and its quadratic
discriminant is $\Delta(u, v) = (-4(u + v))^2 - 4(u^2 + v^2 - 4uv) = 12(u^2 + 4uv + v^2)$. -/
theorem koide_quadratic_completed_square_and_discriminant {R : Type*} [CommRing R] (u v x : R) :
    koideResolventPoly u v x = (x - 2 * (u + v)) ^ 2 - 3 * (u ^ 2 + 4 * u * v + v ^ 2) ∧
      (-4 * (u + v)) ^ 2 - 4 * 1 * (u ^ 2 + v ^ 2 - 4 * u * v) =
        12 * (u ^ 2 + 4 * u * v + v ^ 2) := by
  unfold koideResolventPoly
  exact ⟨by ring, by ring⟩

/-- **Generic-Field Koide Resolvent Equivalence:** over any `[Field F]` (`(3 : F) ≠ 0`,
$u + v + x \neq 0$), $Q_{\mathrm{Koide}}(u, v, x) = \frac{2}{3}$ holds **if and only if**
$x^2 - 4(u + v)x + (u^2 + v^2 - 4uv) = 0$. -/
theorem koideVecRatio_two_thirds_iff_resolvent_zero {F : Type*} [Field F]
    (h3 : (3 : F) ≠ 0) {u v x : F} (hsum : u + v + x ≠ 0) :
    koideVecRatio ![u, v, x] = 2 / 3 ↔ koideResolventPoly u v x = 0 := by
  dsimp [koideVecRatio, normSq3]
  have hs2 : (u + v + x) ^ 2 ≠ 0 := pow_ne_zero 2 hsum
  rw [div_eq_div_iff hs2 h3]
  constructor
  · intro h
    rw [← koide_quadratic_resolvent_ring_identity]
    linear_combination h
  · intro h
    have hid := koide_quadratic_resolvent_ring_identity u v x
    linear_combination hid + h

/-- **Closed-Form Koide Roots & Vieta Identities:** whenever $s^2 = 3(u^2 + 4uv + v^2)$, both
$x_+ = 2(u + v) + s$ and $x_- = 2(u + v) - s$ annihilate `koideResolventPoly u v` and satisfy
$x_+ + x_- = 4(u + v)$ and $x_+ x_- = u^2 + v^2 - 4uv$. -/
theorem koide_resolvent_roots_and_vieta {R : Type*} [CommRing R] (u v s : R)
    (hs : s ^ 2 = 3 * (u ^ 2 + 4 * u * v + v ^ 2)) :
    let xp := 2 * (u + v) + s
    let xm := 2 * (u + v) - s
    koideResolventPoly u v xp = 0 ∧
      koideResolventPoly u v xm = 0 ∧
      xp + xm = 4 * (u + v) ∧
      xp * xm = u ^ 2 + v ^ 2 - 4 * u * v := by
  dsimp only
  rw [(koide_quadratic_completed_square_and_discriminant u v (2 * (u + v) + s)).1,
    (koide_quadratic_completed_square_and_discriminant u v (2 * (u + v) - s)).1]
  refine ⟨?_, ?_, by ring, ?_⟩
  · linear_combination hs
  · linear_combination hs
  · linear_combination -hs

end KoideQuadraticResolvent

/-! ## Section 5: Structural $H_3(q)$ & $TL_3(q)$ Operator Tests & Finite-$q$ Departure -/

section HeckeAndTemperleyLiebTests

variable {K : Type*} [Field K]

/-- **Classical Limit of the Ruled Chiral Photon Vertex (`QOU.Photon.vertex`):**
on the 3D weight space $M_{+1} \cong V_{(3)} \oplus V_{(2,1)}$, `stepPlus q h` ($\rho_{M_{+1}}(\sigma_0 \sigma_1^{-1})$)
reduces at $q = 1, h = 0$ identically to the cyclic shift `cyclicShift3 K`. -/
theorem stepPlus_at_one_eq_cyclicShift3 :
    stepPlus (1 : K) 0 = cyclicShift3 K := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [stepPlus, cyclicShift3]

/-- At $h = q - q^{-1}$, `stepPlus q (q - q⁻¹)` acquires non-zero trace $-(q - q^{-1})^2$
(departing from traceless `cyclicShift3` whenever $q \neq \pm 1$). -/
theorem trace_stepPlus_hecke (q : K) :
    (stepPlus q (q - q⁻¹)).trace = -(q - q⁻¹) ^ 2 := by
  simp [stepPlus, Matrix.trace_fin_three]
  ring

/-- On the 2D doublet block $V_{(2,1)}$, `r21step q` ($\rho_{(2,1)}(\sigma_0 \sigma_1^{-1})$) has
exact determinant $1$ and trace $-1 - (q - q^{-1})^2$. -/
theorem r21step_det_and_trace (q : K) (hq : q ≠ 0) :
    (r21step q).det = 1 ∧ (r21step q).trace = -1 - (q - q⁻¹) ^ 2 := by
  refine ⟨?_, ?_⟩
  · simp [r21step, Matrix.det_fin_two]
    field_simp [hq]
    ring
  · simp [r21step, Matrix.trace_fin_two]
    field_simp [hq]
    ring

/-- Temperley–Lieb / Convention-D Ocneanu Wedderburn Koide ratio when the singlet norm squared is
weighted by $w_{\mathrm{sing}}(q) = y_{(3)}(q) = 1 - 2/(q + q^{-1})^2$ and the doublet norm squared
by $w_{\mathrm{doub}}(q) = 2 y_{(2,1)}(q) = 2/(q + q^{-1})^2$:
$Q_{\mathrm{TL3}}(q) = \frac{y_{(3)}(q) + 2 y_{(2,1)}(q)}{3 y_{(3)}(q)}$. -/
def tl3KoideNormRatio (q : K) : K :=
  (y3 q + 2 * y21 q) / (3 * y3 q)

/-- Normalization identity $y_{(3)}(q) + 2 y_{(2,1)}(q) = 1$ in $TL_3(q)$. -/
theorem y3_add_two_y21 (q : K) :
    y3 q + 2 * y21 q = 1 := by
  unfold y3 y21
  ring

/-- **Exact Classical Singlet–Doublet Equipartition in $TL_3(1)$:**
at $q = 1$, $y_{(3)}(1) = 1/2 = 2 y_{(2,1)}(1)$, producing **exact** Koide ratio
$Q_{\mathrm{TL3}}(1) = 2/3$. -/
theorem tl3_classical_equipartition_at_one (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    y3 (1 : K) = 1 / 2 ∧
      2 * y21 (1 : K) = 1 / 2 ∧
      tl3KoideNormRatio (1 : K) = 2 / 3 := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  have hy3 : y3 (1 : K) = 1 / 2 := by
    unfold y3
    have e : ((1 : K) + 1⁻¹) ^ 2 = 2 * 2 := by norm_num
    rw [e]
    field_simp [h2]
    ring
  have hy21 : 2 * y21 (1 : K) = 1 / 2 := by
    unfold y21
    have e : ((1 : K) + 1⁻¹) ^ 2 = 2 * 2 := by norm_num
    rw [e]
    field_simp [h2]
  refine ⟨hy3, hy21, ?_⟩
  unfold tl3KoideNormRatio
  rw [hy3, hy21]
  field_simp [h2, h3]
  ring

/-- **Exact Closed Form & Finite-$q$ Deficit of $Q_{\mathrm{TL3}}(q)$:**
$Q_{\mathrm{TL3}}(q) = \frac{(q + q^{-1})^2}{3(q^2 + q^{-2})}$ and
$\frac{2}{3} - Q_{\mathrm{TL3}}(q) = \frac{(q - q^{-1})^2}{3(q^2 + q^{-2})}$. -/
theorem tl3KoideNormRatio_closed_form_and_deficit (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + 1 ≠ 0) (h3 : (3 : K) ≠ 0) :
    tl3KoideNormRatio q = (q + q⁻¹) ^ 2 / (3 * (q ^ 2 + q⁻¹ ^ 2)) ∧
      2 / 3 - tl3KoideNormRatio q = (q - q⁻¹) ^ 2 / (3 * (q ^ 2 + q⁻¹ ^ 2)) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp [hq] at h; linear_combination h
  have hc : q ^ 2 + q⁻¹ ^ 2 ≠ 0 := by
    intro h; apply hq4; field_simp [hq] at h; linear_combination h
  have hy3_eq : y3 q = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
    unfold y3
    field_simp [hq, hs, hq2]
    ring
  have hy3_ne : y3 q ≠ 0 := by
    rw [hy3_eq]
    exact div_ne_zero hq4 (pow_ne_zero 2 hq2)
  have hclosed : tl3KoideNormRatio q = (q + q⁻¹) ^ 2 / (3 * (q ^ 2 + q⁻¹ ^ 2)) := by
    unfold tl3KoideNormRatio
    rw [y3_add_two_y21, hy3_eq]
    field_simp [hq, hq2, hq4, hc, h3]
  refine ⟨hclosed, ?_⟩
  rw [hclosed]
  field_simp [hc, h3]
  ring

end HeckeAndTemperleyLiebTests

section OrderedHeckeAndTemperleyLiebObstructions

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Across the cone window $0 < q - q^{-1} < 1$ (including $q_0 \approx 1.11$), the characteristic
discriminant of `r21step q` is strictly negative, keeping both doublet eigenvalues of
$\sigma_0 \sigma_1^{-1}$ strictly complex conjugates on the unit circle. -/
theorem r21step_disc_neg_on_cone {q : K} (hq : q ≠ 0)
    (hh0 : 0 < q - q⁻¹) (hh1 : q - q⁻¹ < 1) :
    ((r21step q).trace) ^ 2 - 4 * (r21step q).det < 0 := by
  rw [(r21step_det_and_trace q hq).1, (r21step_det_and_trace q hq).2]
  have hsq_pos : 0 < (q - q⁻¹) ^ 2 := sq_pos_of_pos hh0
  have hsq_lt : (q - q⁻¹) ^ 2 < 1 := by nlinarith
  have hfac : (-1 - (q - q⁻¹) ^ 2) ^ 2 - 4 * 1 =
      ((q - q⁻¹) ^ 2 - 1) * ((q - q⁻¹) ^ 2 + 3) := by ring
  rw [hfac]
  exact mul_neg_of_neg_of_pos (by linarith) (by linarith)

/-- **Universal Finite-$q$ Departure Theorem for Un-Dressed $TL_3(q)$ Norm Weights:**
for **every** $q > 1$ in any ordered field, $2 y_{(2,1)}(q) < y_{(3)}(q)$ and
$Q_{\mathrm{TL3}}(q) < \frac{2}{3}$ strictly (with exact positive deficit
$\frac{(q - q^{-1})^2}{3(q^2 + q^{-2})}$). -/
theorem tl3_strict_departure_from_two_thirds {q : K} (hq1 : 1 < q) :
    2 * y21 q < y3 q ∧ tl3KoideNormRatio q < 2 / 3 := by
  have hq0 : 0 < q := by linarith
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + 1 ≠ 0 := by positivity
  have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
  have hh_pos : 0 < q - q⁻¹ := by linarith
  have hdiff_y : y3 q - 2 * y21 q = (q - q⁻¹) ^ 2 / (q + q⁻¹) ^ 2 := by
    unfold y3 y21
    have hs : q + q⁻¹ ≠ 0 := by positivity
    field_simp [hs]
    ring
  have hy_lt : 2 * y21 q < y3 q := by
    have hp : 0 < y3 q - 2 * y21 q := by rw [hdiff_y]; positivity
    linarith
  refine ⟨hy_lt, ?_⟩
  have hdef := (tl3KoideNormRatio_closed_form_and_deficit q hq0.ne' hq2 hq4 three_ne_zero).2
  have hc_pos : 0 < 3 * (q ^ 2 + q⁻¹ ^ 2) := by positivity
  have hdef_pos : 0 < 2 / 3 - tl3KoideNormRatio q := by
    rw [hdef]
    positivity
  linarith

end OrderedHeckeAndTemperleyLiebObstructions

/-! ## Section 6: Rule-13a Zero-Instance Hypothesis Class (`KoideCirculantEquipartitionHypothesis`) -/

section Rule13aHypothesisCarrier

/-- **Rule-13a Zero-Instance Hypothesis Class:** encapsulates an open finite-$q$ mechanism mapping
substrate parameter $q \in F$ to a Hermitian circulant square-root mass operator $S_{\mathrm{Herm}}(a, b)$
over `QuadI F` with singlet–doublet equipartition $2|b|^2 = a^2$ and spectral moments matching its
three real root-mass eigenvalues $(u, v, x)$. Zero instances are declared anywhere in the corpus. -/
class KoideCirculantEquipartitionHypothesis (F : Type*) [Field F] where
  /-- Democratic singlet amplitude $a(q)$ ($a(q) \neq 0$). -/
  singletAmp : F → F
  /-- Complex $\mathbb{Z}_3$-hopping amplitude $b(q) \in F[i]$. -/
  hoppingAmp : F → QuadI F
  /-- Root-mass spectrum $(u(q), v(q), x(q)) = (\sqrt{m_1}, \sqrt{m_2}, \sqrt{m_3})$. -/
  rootSpectrum : F → Fin 3 → F
  /-- Singlet–doublet equipartition law $2|b(q)|^2 = a(q)^2$. -/
  equipartition : ∀ q : F, 2 * QuadI.normSq (hoppingAmp q) = (singletAmp q) ^ 2
  /-- First spectral moment matches $\mathrm{Tr}(S_{\mathrm{Herm}}) = 3a(q)$. -/
  trace_moment : ∀ q : F,
    rootSpectrum q 0 + rootSpectrum q 1 + rootSpectrum q 2 = 3 * singletAmp q
  /-- Second spectral moment matches $\mathrm{Tr}(S_{\mathrm{Herm}}^2) = 3(a(q)^2 + 2|b(q)|^2)$. -/
  sq_trace_moment : ∀ q : F,
    (rootSpectrum q 0) ^ 2 + (rootSpectrum q 1) ^ 2 + (rootSpectrum q 2) ^ 2 =
      3 * ((singletAmp q) ^ 2 + 2 * QuadI.normSq (hoppingAmp q))

/-- **Non-Vacuous Consequence of `KoideCirculantEquipartitionHypothesis`:** combining the
Hermitian circulant trace and square-trace moments with $2|b(q)|^2 = a(q)^2$ forces the third
root-mass eigenvalue $x(q)$ to satisfy the exact monic Koide quadratic resolvent equation
$x^2 - 4(u + v)x + (u^2 + v^2 - 4uv) = 0$ and completed-square identity
$(x - 2(u + v))^2 = 3(u^2 + 4uv + v^2)$ over any `[Field F]`. -/
theorem koide_hypothesis_implies_tau_resolvent {F : Type*} [Field F]
    [H : KoideCirculantEquipartitionHypothesis F] (q : F) :
    let u := H.rootSpectrum q 0
    let v := H.rootSpectrum q 1
    let x := H.rootSpectrum q 2
    koideResolventPoly u v x = 0 ∧
      (x - 2 * (u + v)) ^ 2 = 3 * (u ^ 2 + 4 * u * v + v ^ 2) := by
  dsimp only
  have heq := H.equipartition q
  have hm1 := H.trace_moment q
  have hm2 := H.sq_trace_moment q
  have hpoly : koideResolventPoly (H.rootSpectrum q 0) (H.rootSpectrum q 1) (H.rootSpectrum q 2) = 0 := by
    rw [← koide_quadratic_resolvent_ring_identity, hm2, hm1, heq]
    ring
  refine ⟨hpoly, ?_⟩
  have hcs := (koide_quadratic_completed_square_and_discriminant
    (H.rootSpectrum q 0) (H.rootSpectrum q 1) (H.rootSpectrum q 2)).1
  linear_combination hpoly - hcs

/-- **Unconditional Discharge of Circulant Moment Axioms over `[CommRing R]` (`qou-cw8i`):**
for any circulant $S(a_0, b, c)$ over `[CommRing R]` with $1 + \omega + \omega^2 = 0$, the first
and second spectral moments (`trace_moment` and `sq_trace_moment`) hold **unconditionally** via
`KoideSingletDoubletEquipartition.circulant3FourierSpec_moments`, leaving **only** the single
equipartition equation $2bc = a_0^2$ to force both `koideResolventPoly = 0` and the radical-free
quartic mass polynomial `koideMassQuarticPoly = 0`. -/
theorem fourier_circulant_equipartition_implies_resolvent_ring
    {R : Type*} [CommRing R] (a₀ b c ω : R) (hω : 1 + ω + ω ^ 2 = 0)
    (heq : 2 * b * c = a₀ ^ 2) :
    let lam := KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω
    lam 0 + lam 1 + lam 2 = 3 * a₀ ∧
      lam 0 ^ 2 + lam 1 ^ 2 + lam 2 ^ 2 = 3 * (a₀ ^ 2 + 2 * b * c) ∧
      koideResolventPoly (lam 0) (lam 1) (lam 2) = 0 ∧
      KoideSingletDoubletEquipartition.koideMassQuarticPoly
        (lam 0 ^ 2) (lam 1 ^ 2) (lam 2 ^ 2) = 0 := by
  dsimp only
  have hm := KoideSingletDoubletEquipartition.circulant3FourierSpec_moments a₀ b c ω hω
  have hsq :
      (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 0) ^ 2 +
        (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 1) ^ 2 +
        (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 2) ^ 2 =
      3 * (a₀ ^ 2 + 2 * b * c) := by
    simpa [KoideSingletDoubletEquipartition.normSq3] using hm.2.1
  have hk :
      3 * ((KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 0) ^ 2 +
            (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 1) ^ 2 +
            (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 2) ^ 2) =
        2 * (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 0 +
              KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 1 +
              KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 2) ^ 2 := by
    rw [hsq, hm.1, heq]
    ring
  have hpoly :
      koideResolventPoly
        (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 0)
        (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 1)
        (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 2) = 0 := by
    rw [← koide_quadratic_resolvent_ring_identity, hk, sub_self]
  exact ⟨hm.1, hsq, hpoly,
    (KoideSingletDoubletEquipartition.koideMassQuarticPoly_galois_factorization
      (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 0)
      (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 1)
      (KoideSingletDoubletEquipartition.circulant3FourierSpec a₀ b c ω 2)).2 hk⟩

end Rule13aHypothesisCarrier

end QOU.StandardModel.S3CirculantKoideTraceIdentity
