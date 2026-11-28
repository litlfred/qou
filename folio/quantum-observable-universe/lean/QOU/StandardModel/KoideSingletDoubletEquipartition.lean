/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases
import QOU.BraidsAndKnots.ElectronWordCandidates
import QOU.Observations.LeptonChargeClassTrace
import QOU.Observations.LeptonWordsCatMap

/-!
# Division-Free $S_3 / \mathbb{Z}_3$ Singlet–Doublet Koide Equipartition & Least-Crossing Lepton Link Invariants

Bean `qou-cw8i` (Stability Epic `qou-s028` & Compute-Accuracy Epic `qou-myts`).
Discharges **100% of the algebraic core** previously bundled inside `KoideTopologicalProtectionHypothesis`
and `KoideCirculantEquipartitionHypothesis`, working **strictly over a generic `[CommRing R]`**
(`0 sorry`, `0` custom `axiom`s, `0` `[Field]` binders, `0` `field_simp` calls, `0` transcendental
APIs, `0` empirical literals — `AGENTS.md §7c`), and formalizes the `[CommRing R]` crossing,
linking, Burau / `SL(2, R)`, and skein-difference invariants of the 2026-11-28 ruled least-crossing
2-component lepton link ladder (`owner-rulings.md` row 17).

## Main Results

1. **§1 — Division-Free $S_3$ Singlet–Doublet Projectors on $V_{\mathrm{gen}} = R^3$ & Bring's $R^5$:**
   - Scaled projectors `threeProjSinglet3 R` ($3 P_{\mathbf{1}} = J_3$) and `threeProjDoublet3 R`
     ($3 P_{\mathrm{std}} = 3 I_3 - J_3$): scaled idempotency, orthogonality, completeness
     $3 P_{\mathbf{1}} + 3 P_{\mathrm{std}} = 3 I_3$, and trace split $(3, 6)$.
   - Vector Pythagorean split $9\|v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + \|3 P_{\mathrm{std}} v\|_3^2$
     and exact division-free Koide norm-equipartition equivalence
     `singlet_doublet_equipartition_iff_koide_ring`: over any $3$-torsion-free `[CommRing R]`,
     $\|3 P_{\mathbf{1}} v\|_3^2 = \|3 P_{\mathrm{std}} v\|_3^2 \iff 3\|v\|_3^2 = 2(v_0 + v_1 + v_2)^2$.
   - Division-free ambient-$R^5$ metric stretch (`4 * normSq3` on singlet vs `normSq3` on doublet)
     on Bring's $g - 1 = 3$ generation subspace inside $V_{\mathrm{std}} \subset R^5$.

2. **§2 — Matrix Trace Equipartition, $S_3 / \mathbb{Z}_3$ Circulant Fourier Moments & $V^{\otimes 3}$ Schur–Weyl $4 = 4$ Split:**
   - Arbitrary $3\times 3$ matrix identity `matrix_trace_singlet_traceless_koide_identity`:
     $\mathrm{tr}((3A - (\mathrm{tr}\,A)I_3)^2) = \mathrm{tr}(((\mathrm{tr}\,A)I_3)^2) + 3(3\,\mathrm{tr}(A^2) - 2(\mathrm{tr}\,A)^2)$.
   - Symmetric $S_3$-circulant $M^{1/2} = a_0 I_3 + a_1(C + C^2)$:
     $3\,\mathrm{tr}((M^{1/2})^2) = 2(\mathrm{tr}\,M^{1/2})^2 \iff 2 a_1^2 = a_0^2$.
   - Unconditional Fourier-mode spectral moment theorem `circulant3FourierSpec_moments`: for any
     circulant $S(a_0, b, c)$ and $\omega \in R$ with $1 + \omega + \omega^2 = 0$, the first two
     spectral power sums $\sum \lambda_k = 3 a_0$ and $\sum \lambda_k^2 = 3(a_0^2 + 2bc)$ hold
     **automatically** without hypothesis, plus the algebraic Chebyshev / Brannen–Koide root-mass
     family (`twoBrannenVec`).
   - Exact 3-strand Schur–Weyl quantum-dimension identity `q3SchurWeyl_partition_and_classical_equipartition`:
     $q^3 [4]_q + 2 q^3 [2]_q = (q^2 + 1)^3$, proving **unconditional $4 = 4$ singlet–doublet
     dimension equipartition** on $(\mathbb{C}^2)^{\otimes 3} = (\mathbf{4}\otimes\mathbf{1}) \oplus (\mathbf{2}\otimes\mathbf{2})$
     at $q^2 = 1$ (forcing Koide $Q = 2/3$) and exact $(q^2 + 1)(q^2 - 1)^2$ drift for $q^2 \neq 1$.

3. **§3 — Homogeneous Quadratic Resolvent, Discriminant Positivity & Radical-Free Quartic Mass Polynomial:**
   - Ordered-ring discriminant positivity `koide_discriminant_pos_and_upper_root_dominance`
     ($12((u + v)^2 + 2uv) > 0$) and upper-root hierarchy dominance $x_+ > 2(u + v) > \max(u, v)$.
   - Radical-eliminated saddle equation `koide_saddle_quartic_eliminating_v` and the symmetric
     radical-free degree-$4$ Koide mass polynomial `koideMassQuarticPoly` ($K_4(m_1, m_2, m_3) = 0$),
     factored over `[CommRing R]` as the product of all four signed root-mass quadratics.

4. **§4 — Irreducible Rule-13a Physical Bridge (`KoideSingletDoubletEquipartitionBridge`) & Consistency Witnesses:**
   - Isolates the **sole** remaining physical assumption (`normSq3 (threeSingletVec λ) = normSq3 (threeDoubletVec λ)`),
     with Pattern-3.3 `def trivialModel` and non-zero `def brannenAlgebraicModel` (`def`, never `instance`).

5. **§5 — 2026-11-28 Least-Crossing 2-Component Lepton Link Ladder (`e = σ₀σ₁σ₀`, `μ = σ₀⁴σ₁⁻¹`, `τ = σ₀²σ₁⁻¹σ₀σ₁⁻¹`):**
   - Constructive 2-component strand-tracking `interWritheFrom` & `selfWritheFrom`:
     proves `writhe = inter + self`, `2 * lk = (2, 4, 0)` (`lk = (1, 2, 0)`, $U(1) = (3, 6, 0)$),
     and crossing numbers `(2, 4, 5)`.
   - Reduced Burau representation over `[CommRing R]` (`t : Rˣ`): proves `burauWord (-1) w = imgZ w`
     and the **universal 3-braid determinant-trace identity**
     `det(1 - burauWord (-1) w) = 2 - tr(imgZ w)` for **all** `w : Word`, plus Morton–Birman
     $(1 - t^3)\Delta_L(t)$ factorizations on $(e, \mu, \tau)$ and $-(1 + t + t^2)\Delta_{4_1}(t)$ on $4_1$,
     and cleared-denominator two-colour Casimir invariants $6\kappa_2 = \mathrm{lk}^2 = (1, 4, 0)$,
     $9\kappa_3 = (0, -6, 12)$.
   - Cleared-denominator $N = 2$ ring-mass skein differences $q^{12}(m_e - m_\mu) = q^{12} - 1$ and
     $q^{12}(m_\tau - m_e) = q^4(q^{12} - 1)$, proving pure singlet collapse at $q = 1$.

-- Ref: [koide1983prd] Y. Koide, Phys. Rev. D 28 (1983) 252–254, doi:10.1103/PhysRevD.28.252
-- Ref: [foot1994] R. Foot, arXiv:hep-ph/9402242, doi:10.48550/arXiv.hep-ph/9402242
-- Ref: [morton1986] H. R. Morton, Math. Proc. Cambridge Philos. Soc. 99 (1986) 107–109
-- Ref: [kassel2008] C. Kassel, V. Turaev, Braid Groups, GTM 247 (2008)
-/

set_option autoImplicit false

namespace QOU.StandardModel.KoideSingletDoubletEquipartition

open Matrix
open QOU.BraidKnot.ElectronWordCandidates
open QOU.Observations.LeptonChargeClassTrace
open QOU.Observations.LeptonWordsCatMap

/-! ## §1. Division-Free $S_3$ Singlet–Doublet Projectors on $V_{\mathrm{gen}} = R^3$ & Bring's $R^5$ -/

section SingletDoubletProjectors

variable {R : Type*} [CommRing R]

/-- Squared Euclidean norm on `Fin 3 → R`. -/
def normSq3 (v : Fin 3 → R) : R :=
  v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2

/-- Standard bilinear dot product on `Fin 3 → R`. -/
def dot3 (u v : Fin 3 → R) : R :=
  u 0 * v 0 + u 1 * v 1 + u 2 * v 2

/-- Squared Euclidean norm on Bring's ambient `Fin 5 → R`. -/
def normSq5 (v : Fin 5 → R) : R :=
  v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2

/-- Scaled $S_3$-trivial singlet projector $3 P_{\mathbf{1}} = J_3 = I_3 + C + C^2$ over `[CommRing R]`. -/
def threeProjSinglet3 (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  !![1, 1, 1; 1, 1, 1; 1, 1, 1]

/-- Scaled $S_3$-standard 2D doublet projector $3 P_{\mathrm{std}} = 3 I_3 - J_3 = 2 I_3 - C - C^2$. -/
def threeProjDoublet3 (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  !![2, -1, -1; -1, 2, -1; -1, -1, 2]

/-- **Division-free $S_3$ projector algebra over any `[CommRing R]`:**
completeness $3 P_{\mathbf{1}} + 3 P_{\mathrm{std}} = 3 I_3$, scaled idempotency
$(3 P_{\mathbf{1}})^2 = 3(3 P_{\mathbf{1}})$ and $(3 P_{\mathrm{std}})^2 = 3(3 P_{\mathrm{std}})$,
mutual annihilation $(3 P_{\mathbf{1}})(3 P_{\mathrm{std}}) = 0$, and rank-scaled traces $(3, 6)$. -/
theorem threeProj_idempotent_orthog_and_trace :
    threeProjSinglet3 R + threeProjDoublet3 R = (3 : R) • (1 : Matrix (Fin 3) (Fin 3) R) ∧
      (threeProjSinglet3 R) ^ 2 = (3 : R) • threeProjSinglet3 R ∧
      (threeProjDoublet3 R) ^ 2 = (3 : R) • threeProjDoublet3 R ∧
      threeProjSinglet3 R * threeProjDoublet3 R = 0 ∧
      threeProjDoublet3 R * threeProjSinglet3 R = 0 ∧
      (threeProjSinglet3 R).trace = 3 ∧
      (threeProjDoublet3 R).trace = 6 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [threeProjSinglet3, threeProjDoublet3] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [sq, threeProjSinglet3, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [sq, threeProjDoublet3, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [threeProjSinglet3, threeProjDoublet3, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [threeProjSinglet3, threeProjDoublet3, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · simp [threeProjSinglet3, Matrix.trace_fin_three]; ring
  · simp [threeProjDoublet3, Matrix.trace_fin_three]; ring

/-- Scaled singlet vector $3 P_{\mathbf{1}} v = (v_0 + v_1 + v_2)(1, 1, 1) \in R^3$. -/
def threeSingletVec (v : Fin 3 → R) : Fin 3 → R :=
  (threeProjSinglet3 R).mulVec v

/-- Scaled zero-sum doublet vector $3 P_{\mathrm{std}} v = 3 v - (v_0 + v_1 + v_2)(1, 1, 1) \in R^3$. -/
def threeDoubletVec (v : Fin 3 → R) : Fin 3 → R :=
  (threeProjDoublet3 R).mulVec v

/-- Explicit coordinate formulas for `threeSingletVec` and `threeDoubletVec`. -/
theorem threeSingletVec_and_doubletVec_apply (v : Fin 3 → R) :
    threeSingletVec v = ![v 0 + v 1 + v 2, v 0 + v 1 + v 2, v 0 + v 1 + v 2] ∧
      threeDoubletVec v =
        ![2 * v 0 - v 1 - v 2, 2 * v 1 - v 0 - v 2, 2 * v 2 - v 0 - v 1] := by
  refine ⟨?_, ?_⟩
  · ext i; fin_cases i <;>
      simp [threeSingletVec, threeProjSinglet3, Matrix.mulVec, dotProduct, Fin.sum_univ_three]
  · ext i; fin_cases i <;>
      simp [threeDoubletVec, threeProjDoublet3, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring

/-- **Division-Free Orthogonal Pythagorean Split on $R^3$:**
$3 P_{\mathbf{1}} v + 3 P_{\mathrm{std}} v = 3 v$, $\sum_i (3 P_{\mathrm{std}} v)_i = 0$,
$\langle 3 P_{\mathbf{1}} v, 3 P_{\mathrm{std}} v \rangle = 0$, and
$9\|v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + \|3 P_{\mathrm{std}} v\|_3^2$. -/
theorem threeSinglet_doublet_pythagorean (v : Fin 3 → R) :
    threeSingletVec v + threeDoubletVec v = (3 : R) • v ∧
      threeDoubletVec v 0 + threeDoubletVec v 1 + threeDoubletVec v 2 = 0 ∧
      dot3 (threeSingletVec v) (threeDoubletVec v) = 0 ∧
      9 * normSq3 v = normSq3 (threeSingletVec v) + normSq3 (threeDoubletVec v) := by
  rcases threeSingletVec_and_doubletVec_apply v with ⟨hs, hd⟩
  rw [hs, hd]
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i; fin_cases i <;> simp <;> ring
  · simp; ring
  · simp [dot3]; ring
  · simp [normSq3]; ring

/-- **Division-Free Koide Projector Norm Identity over any `[CommRing R]`:**
$\|3 P_{\mathrm{std}} v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + 3\bigl(3\|v\|_3^2 - 2(v_0 + v_1 + v_2)^2\bigr)$. -/
theorem doublet_normSq3_eq_singlet_add_three_koide (v : Fin 3 → R) :
    normSq3 (threeDoubletVec v) =
      normSq3 (threeSingletVec v) + 3 * (3 * normSq3 v - 2 * (v 0 + v 1 + v 2) ^ 2) := by
  rcases threeSingletVec_and_doubletVec_apply v with ⟨hs, hd⟩
  rw [hs, hd]
  simp [normSq3]
  ring

/-- **Exact Singlet–Doublet Norm Equipartition Equivalence over `[CommRing R]`:**
whenever $3$ is a non-zero-divisor in $R$, $\|3 P_{\mathbf{1}} v\|_3^2 = \|3 P_{\mathrm{std}} v\|_3^2$
holds **if and only if** $3(v_0^2 + v_1^2 + v_2^2) = 2(v_0 + v_1 + v_2)^2$. -/
theorem singlet_doublet_equipartition_iff_koide_ring
    (h3 : ∀ z : R, 3 * z = 0 → z = 0) (v : Fin 3 → R) :
    normSq3 (threeSingletVec v) = normSq3 (threeDoubletVec v) ↔
      3 * normSq3 v = 2 * (v 0 + v 1 + v 2) ^ 2 := by
  have hid := doublet_normSq3_eq_singlet_add_three_koide v
  constructor
  · intro heq
    have hz : 3 * (3 * normSq3 v - 2 * (v 0 + v 1 + v 2) ^ 2) = 0 := by
      linear_combination -heq - hid
    have hcore := h3 _ hz
    linear_combination hcore
  · intro hk
    have hz : 3 * normSq3 v - 2 * (v 0 + v 1 + v 2) ^ 2 = 0 := by
      linear_combination hk
    rw [hid, hz, mul_zero, add_zero]

/-- Division-free embedding of `3 v` into Bring's 3-generation subspace inside $V_{\mathrm{std}} \subset R^5$,
decomposed into scaled singlet `threeSingletBring5 v` along $(1, 1, 1, -3, 0)$ and zero-sum doublet
`threeDoubletBring5 v`. -/
def threeSingletBring5 (v : Fin 3 → R) : Fin 5 → R :=
  let s := v 0 + v 1 + v 2
  ![s, s, s, -3 * s, 0]

def threeDoubletBring5 (v : Fin 3 → R) : Fin 5 → R :=
  ![2 * v 0 - v 1 - v 2, 2 * v 1 - v 0 - v 2, 2 * v 2 - v 0 - v 1, 0, 0]

/-- **Division-Free Bring Ambient-$R^5$ Metric Stretch Theorem:**
both `threeSingletBring5 v` and `threeDoubletBring5 v` lie in Bring's hyperplane $\sum_{i=0}^4 x_i = 0$,
preserve the doublet norm identically, and stretch the singlet norm squared by an **exact factor
of $4$** (`12 = 4 * 3`) without division. -/
theorem bring5_singlet_doublet_metric_stretch (v : Fin 3 → R) :
    threeSingletBring5 v 0 + threeSingletBring5 v 1 + threeSingletBring5 v 2 +
        threeSingletBring5 v 3 + threeSingletBring5 v 4 = 0 ∧
      threeDoubletBring5 v 0 + threeDoubletBring5 v 1 + threeDoubletBring5 v 2 +
          threeDoubletBring5 v 3 + threeDoubletBring5 v 4 = 0 ∧
      normSq5 (threeDoubletBring5 v) = normSq3 (threeDoubletVec v) ∧
      normSq5 (threeSingletBring5 v) = 4 * normSq3 (threeSingletVec v) := by
  rcases threeSingletVec_and_doubletVec_apply v with ⟨hs, hd⟩
  rw [hs, hd]
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp [threeSingletBring5, threeDoubletBring5, normSq5, normSq3] <;> ring

end SingletDoubletProjectors

/-! ## §2. Operator Trace Equipartition, $S_3 / \mathbb{Z}_3$ Circulant Moments & $V^{\otimes 3}$ Schur–Weyl $4 = 4$ Split -/

section OperatorTraceAndSchurWeyl

variable {R : Type*} [CommRing R]

/-- Scaled trace-singlet scalar matrix $3 A_{\mathbf{1}} := (\mathrm{tr}\,A) I_3$. -/
def threeSingletMat (A : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  A.trace • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Scaled traceless $\mathfrak{sl}_3$ matrix $3 A_{\mathrm{std}} := 3 A - (\mathrm{tr}\,A) I_3$. -/
def threeTracelessMat (A : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  (3 : R) • A - A.trace • (1 : Matrix (Fin 3) (Fin 3) R)

/-- **Universal $3\times 3$ Matrix Trace Decomposition over any `[CommRing R]`:**
for **every** $A \in \mathrm{Mat}_{3\times 3}(R)$ (not even assuming $A$ is circulant!),
$9\,\mathrm{tr}(A^2) = \mathrm{tr}((3 A_{\mathbf{1}})^2) + \mathrm{tr}((3 A_{\mathrm{std}})^2)$,
$\mathrm{tr}((3 A_{\mathbf{1}})(3 A_{\mathrm{std}})) = 0$, and
$\mathrm{tr}((3 A_{\mathrm{std}})^2) = \mathrm{tr}((3 A_{\mathbf{1}})^2) + 3(3\,\mathrm{tr}(A^2) - 2(\mathrm{tr}\,A)^2)$. -/
theorem matrix_trace_singlet_traceless_koide_identity (A : Matrix (Fin 3) (Fin 3) R) :
    (threeTracelessMat A).trace = 0 ∧
      (threeSingletMat A * threeTracelessMat A).trace = 0 ∧
      9 * (A ^ 2).trace =
        ((threeSingletMat A) ^ 2).trace + ((threeTracelessMat A) ^ 2).trace ∧
      ((threeTracelessMat A) ^ 2).trace =
        ((threeSingletMat A) ^ 2).trace + 3 * (3 * (A ^ 2).trace - 2 * A.trace ^ 2) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [threeTracelessMat, Matrix.trace_fin_three]; ring
  · simp [threeSingletMat, threeTracelessMat, Matrix.trace_fin_three]; ring
  · simp [sq, threeSingletMat, threeTracelessMat, Matrix.trace_fin_three, Matrix.mul_apply,
      Fin.sum_univ_three, Matrix.one_apply]; ring
  · simp [sq, threeSingletMat, threeTracelessMat, Matrix.trace_fin_three, Matrix.mul_apply,
      Fin.sum_univ_three, Matrix.one_apply]; ring

/-- **Operator Trace Equipartition Equivalence over `[CommRing R]`:**
whenever $3$ is a non-zero-divisor in $R$,
$\mathrm{tr}(((\mathrm{tr}\,A)I_3)^2) = \mathrm{tr}((3A - (\mathrm{tr}\,A)I_3)^2)
\iff 3\,\mathrm{tr}(A^2) = 2(\mathrm{tr}\,A)^2$. -/
theorem matrix_trace_equipartition_iff_koide_ring
    (h3 : ∀ z : R, 3 * z = 0 → z = 0) (A : Matrix (Fin 3) (Fin 3) R) :
    ((threeSingletMat A) ^ 2).trace = ((threeTracelessMat A) ^ 2).trace ↔
      3 * (A ^ 2).trace = 2 * A.trace ^ 2 := by
  have hid := (matrix_trace_singlet_traceless_koide_identity A).2.2.2
  constructor
  · intro heq
    have hz : 3 * (3 * (A ^ 2).trace - 2 * A.trace ^ 2) = 0 := by
      linear_combination -heq - hid
    linear_combination h3 _ hz
  · intro hk
    have hz : 3 * (A ^ 2).trace - 2 * A.trace ^ 2 = 0 := by linear_combination hk
    rw [hid, hz, mul_zero, add_zero]

/-- General $3\times 3$ $\mathbb{Z}_3$-circulant matrix $S(a_0, b, c) = a_0 I_3 + b C + c C^2$. -/
def genCirculant3 (a₀ b c : R) : Matrix (Fin 3) (Fin 3) R :=
  !![a₀, b, c; c, a₀, b; b, c, a₀]

/-- Symmetric $S_3$-circulant matrix $M^{1/2} = a_0 I_3 + a_1(C + C^{-1}) = S(a_0, a_1, a_1)$. -/
def symCirculant3 (a₀ a₁ : R) : Matrix (Fin 3) (Fin 3) R :=
  genCirculant3 a₀ a₁ a₁

/-- **Projector Eigenspace & Trace Equipartition for `genCirculant3` and `symCirculant3`:**
1. `genCirculant3 a₀ b c` scales `threeProjSinglet3 R` by $a_0 + b + c$;
2. $3\,\mathrm{tr}(S(a_0, b, c)^2) + 9 a_0^2 = 2(\mathrm{tr}\,S(a_0, b, c))^2 + 18 bc$;
3. For $M^{1/2} = a_0 I_3 + a_1(C + C^{-1})$, under $3$-torsion-freeness,
   $3\,\mathrm{tr}((M^{1/2})^2) = 2(\mathrm{tr}\,M^{1/2})^2 \iff 2 a_1^2 = a_0^2$. -/
theorem genCirculant3_and_symCirculant3_equipartition
    (a₀ b c a₁ : R) :
    genCirculant3 a₀ b c * threeProjSinglet3 R = (a₀ + b + c) • threeProjSinglet3 R ∧
      (genCirculant3 a₀ b c).trace = 3 * a₀ ∧
      (genCirculant3 a₀ b c ^ 2).trace = 3 * (a₀ ^ 2 + 2 * b * c) ∧
      3 * (genCirculant3 a₀ b c ^ 2).trace + 9 * a₀ ^ 2 =
        2 * (genCirculant3 a₀ b c).trace ^ 2 + 18 * b * c ∧
      ((∀ z : R, 3 * z = 0 → z = 0) →
        (3 * (symCirculant3 a₀ a₁ ^ 2).trace = 2 * (symCirculant3 a₀ a₁).trace ^ 2 ↔
          2 * a₁ ^ 2 = a₀ ^ 2)) := by
  have htr : (genCirculant3 a₀ b c).trace = 3 * a₀ := by
    simp [genCirculant3, Matrix.trace_fin_three]; ring
  have hsq : (genCirculant3 a₀ b c ^ 2).trace = 3 * (a₀ ^ 2 + 2 * b * c) := by
    simp [sq, genCirculant3, Matrix.trace_fin_three]; ring
  refine ⟨?_, htr, hsq, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [genCirculant3, threeProjSinglet3, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · rw [htr, hsq]; ring
  · intro h3
    have htr1 : (symCirculant3 a₀ a₁).trace = 3 * a₀ := by
      simp [symCirculant3, genCirculant3, Matrix.trace_fin_three]; ring
    have hsq1 : (symCirculant3 a₀ a₁ ^ 2).trace = 3 * (a₀ ^ 2 + 2 * a₁ ^ 2) := by
      simp [symCirculant3, sq, genCirculant3, Matrix.trace_fin_three]; ring
    rw [htr1, hsq1]
    constructor
    · intro h
      have h9 : 3 * (3 * (2 * a₁ ^ 2 - a₀ ^ 2)) = 0 := by linear_combination h
      linear_combination h3 _ (h3 _ h9)
    · intro h
      linear_combination 9 * h

/-- Fourier-mode eigenvalue vector $(\lambda_0, \lambda_1, \lambda_2)$ of $S(a_0, b, c)$ over any
`[CommRing R]` carrying a primitive cube root $\omega$ ($1 + \omega + \omega^2 = 0$). -/
def circulant3FourierSpec (a₀ b c ω : R) : Fin 3 → R :=
  ![a₀ + b + c, a₀ + b * ω + c * ω ^ 2, a₀ + b * ω ^ 2 + c * ω]

/-- **Unconditional Discharge of Circulant Spectral Moments over `[CommRing R]`:**
whenever $1 + \omega + \omega^2 = 0$, `circulant3FourierSpec a₀ b c ω` satisfies
$\sum \lambda_k = 3 a_0$, $\sum \lambda_k^2 = 3(a_0^2 + 2bc)$,
$\lambda_0 \lambda_1 \lambda_2 = a_0^3 + b^3 + c^3 - 3 a_0 b c = \det S(a_0, b, c)$, and
$3\|\lambda\|_3^2 + 9 a_0^2 = 2(\sum \lambda_k)^2 + 18 bc$ **without any extra hypothesis**. -/
theorem circulant3FourierSpec_moments (a₀ b c ω : R) (hω : 1 + ω + ω ^ 2 = 0) :
    let lam := circulant3FourierSpec a₀ b c ω
    lam 0 + lam 1 + lam 2 = 3 * a₀ ∧
      normSq3 lam = 3 * (a₀ ^ 2 + 2 * b * c) ∧
      lam 0 * lam 1 * lam 2 = (genCirculant3 a₀ b c).det ∧
      3 * normSq3 lam + 9 * a₀ ^ 2 = 2 * (lam 0 + lam 1 + lam 2) ^ 2 + 18 * b * c := by
  dsimp only
  have hdet : (genCirculant3 a₀ b c).det = a₀ ^ 3 + b ^ 3 + c ^ 3 - 3 * a₀ * b * c := by
    simp [genCirculant3, Matrix.det_fin_three]; ring
  have hs1 :
      circulant3FourierSpec a₀ b c ω 0 +
        circulant3FourierSpec a₀ b c ω 1 +
        circulant3FourierSpec a₀ b c ω 2 = 3 * a₀ := by
    simp [circulant3FourierSpec]
    linear_combination (b + c) * hω
  have hs2 : normSq3 (circulant3FourierSpec a₀ b c ω) = 3 * (a₀ ^ 2 + 2 * b * c) := by
    simp [circulant3FourierSpec, normSq3]
    linear_combination
      (2 * a₀ * b + 2 * a₀ * c + (b ^ 2 + c ^ 2) * (1 - ω + ω ^ 2) + 4 * b * c * (ω - 1)) * hω
  refine ⟨hs1, hs2, ?_, ?_⟩
  · rw [hdet]
    simp [circulant3FourierSpec]
    linear_combination
      (a₀ ^ 2 * (b + c) + a₀ * (b ^ 2 + c ^ 2) * ω +
        a₀ * b * c * (ω ^ 2 - ω + 3) + (b ^ 3 + c ^ 3) * (ω - 1) +
        b * c * (b + c) * ω ^ 2) * hω
  · rw [hs2, hs1]
    ring

/-- Scaled algebraic Chebyshev / Brannen–Koide root-mass vector over `[CommRing R]`:
$2\tilde{\lambda} = (2 - r_2 c - r_2 r_3 s,\; 2 - r_2 c + r_2 r_3 s,\; 2 + 2 r_2 c)$ for
$c^2 + s^2 = 1$, $r_2^2 = 2$, $r_3^2 = 3$ (clearing the factor $1/2$ in $\cos(\theta \pm 2\pi/3)$). -/
def twoBrannenVec (c s r₂ r₃ : R) : Fin 3 → R :=
  ![2 - r₂ * c - r₂ * r₃ * s, 2 - r₂ * c + r₂ * r₃ * s, 2 + 2 * r₂ * c]

/-- **Algebraic Brannen–Koide Identity over any `[CommRing R]`:**
whenever $c^2 + s^2 = 1$, $r_2^2 = 2$, and $r_3^2 = 3$, `twoBrannenVec c s r₂ r₃` has exact sum $6$,
squared norm $24$, and satisfies **exact** singlet–doublet norm equipartition ($108 = 108$). -/
theorem twoBrannenVec_exact_equipartition (c s r₂ r₃ : R)
    (hcs : c ^ 2 + s ^ 2 = 1) (hr2 : r₂ ^ 2 = 2) (hr3 : r₃ ^ 2 = 3) :
    let v := twoBrannenVec c s r₂ r₃
    v 0 + v 1 + v 2 = 6 ∧
      normSq3 v = 24 ∧
      3 * normSq3 v = 2 * (v 0 + v 1 + v 2) ^ 2 ∧
      normSq3 (threeSingletVec v) = normSq3 (threeDoubletVec v) := by
  dsimp only
  have hsum : twoBrannenVec c s r₂ r₃ 0 + twoBrannenVec c s r₂ r₃ 1 + twoBrannenVec c s r₂ r₃ 2 = 6 := by
    simp [twoBrannenVec]; ring
  have hnorm : normSq3 (twoBrannenVec c s r₂ r₃) = 24 := by
    simp [twoBrannenVec, normSq3]
    linear_combination
      6 * c ^ 2 * hr2 + 2 * s ^ 2 * r₂ ^ 2 * hr3 + 6 * s ^ 2 * hr2 + 12 * hcs
  have hkoide : 3 * normSq3 (twoBrannenVec c s r₂ r₃) =
      2 * (twoBrannenVec c s r₂ r₃ 0 + twoBrannenVec c s r₂ r₃ 1 + twoBrannenVec c s r₂ r₃ 2) ^ 2 := by
    rw [hnorm, hsum]; ring
  refine ⟨hsum, hnorm, hkoide, ?_⟩
  rw [doublet_normSq3_eq_singlet_add_three_koide, hkoide, sub_self, mul_zero, add_zero]

/-- Cleared-$q^3$ quantum dimension of the $S_3$-singlet Schur–Weyl sector $V_{3/2} \otimes \mathbf{1}$
inside $V^{\otimes 3}$: $q^3 [4]_q \cdot 1 = q^6 + q^4 + q ^ 2 + 1$. -/
def q3SchurWeylSingletDim (q : R) : R :=
  q ^ 6 + q ^ 4 + q ^ 2 + 1

/-- Cleared-$q^3$ quantum dimension of the $S_3$-doublet Schur–Weyl sector $V_{1/2} \otimes V_{\mathrm{std}}$
inside $V^{\otimes 3}$: $q^3 \cdot 2 [2]_q = 2 q^2 (q^2 + 1)$. -/
def q3SchurWeylDoubletDim (q : R) : R :=
  2 * q ^ 2 * (q ^ 2 + 1)

/-- Cleared-$q^3$ total quantum dimension of $V^{\otimes 3}$: $q^3 [2]_q^3 = (q^2 + 1)^3$. -/
def q3SchurWeylTotalDim (q : R) : R :=
  (q ^ 2 + 1) ^ 3

/-- **3-Strand Schur–Weyl $V^{\otimes 3} = (\mathbf{4}\otimes\mathbf{1}) \oplus (\mathbf{2}\otimes\mathbf{2})$
Dimension Partition & Unconditional Classical $4 = 4$ Equipartition Theorem:**
1. $q^3 [4]_q + 2 q^3 [2]_q = (q^2 + 1)^3$ over any `[CommRing R]`;
2. Exact finite-$q$ singlet–doublet excess:
   $q^3 [4]_q = 2 q^3 [2]_q + (q^2 + 1)(q^2 - 1)^2$;
3. At the classical point $q = 1$ (and $q = -1$), $V^{\otimes 3}$ (`dim = 8`) splits into **exact
   $4 = 4$ singlet–doublet equipartition**, which forces $3\|v\|_3^2 = 2(v_0 + v_1 + v_2)^2$ for
   every vector $v \in R^3$ weighted by the classical $V^{\otimes 3}$ sector dimensions. -/
theorem q3SchurWeyl_partition_and_classical_equipartition (q : R) :
    q3SchurWeylSingletDim q + q3SchurWeylDoubletDim q = q3SchurWeylTotalDim q ∧
      q3SchurWeylSingletDim q = q3SchurWeylDoubletDim q + (q ^ 2 + 1) * (q ^ 2 - 1) ^ 2 ∧
      q3SchurWeylSingletDim (1 : R) = 4 ∧
      q3SchurWeylDoubletDim (1 : R) = 4 ∧
      q3SchurWeylTotalDim (1 : R) = 8 ∧
      (∀ (v : Fin 3 → R),
        (∀ z : R, 12 * z = 0 → z = 0) →
        normSq3 (threeDoubletVec v) * q3SchurWeylSingletDim (1 : R) =
          normSq3 (threeSingletVec v) * q3SchurWeylDoubletDim (1 : R) →
        3 * normSq3 v = 2 * (v 0 + v 1 + v 2) ^ 2) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · unfold q3SchurWeylSingletDim q3SchurWeylDoubletDim q3SchurWeylTotalDim; ring
  · unfold q3SchurWeylSingletDim q3SchurWeylDoubletDim; ring
  · unfold q3SchurWeylSingletDim; ring
  · unfold q3SchurWeylDoubletDim; ring
  · unfold q3SchurWeylTotalDim; ring
  · intro v h12 hw
    have hs1 : q3SchurWeylSingletDim (1 : R) = 4 := by unfold q3SchurWeylSingletDim; ring
    have hd1 : q3SchurWeylDoubletDim (1 : R) = 4 := by unfold q3SchurWeylDoubletDim; ring
    rw [hs1, hd1] at hw
    have hid := doublet_normSq3_eq_singlet_add_three_koide v
    have hz : 12 * (3 * normSq3 v - 2 * (v 0 + v 1 + v 2) ^ 2) = 0 := by
      linear_combination hw - 4 * hid
    linear_combination h12 _ hz

end OperatorTraceAndSchurWeyl

/-! ## §3. Homogeneous Monic Quadratic Resolvent, Ordered-Ring Positivity & Radical-Free Quartic Mass Polynomial -/

section ResolventAndQuarticMassPolynomial

/-- Homogeneous monic quadratic Koide resolvent in $x$ with coefficients in $R[u, v]$:
$P_{\mathrm{Koide}}(u, v; x) = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv)$. -/
def homogKoideResolvent {R : Type*} [CommRing R] (u v x : R) : R :=
  x ^ 2 - 4 * (u + v) * x + (u ^ 2 + v ^ 2 - 4 * u * v)

/-- **Homogeneous Resolvent, Completed Square & Sum-of-Squares Discriminant Core over `[CommRing R]`:**
1. $3(u^2 + v^2 + x^2) = 2(u + v + x)^2 + P_{\mathrm{Koide}}(u, v; x)$;
2. $(x - 2(u + v))^2 = P_{\mathrm{Koide}}(u, v; x) + 3(u^2 + 4uv + v^2)$;
3. $u^2 + 4uv + v^2 = (u + v)^2 + 2uv = (u - v)^2 + 6uv$. -/
theorem homogKoideResolvent_identities {R : Type*} [CommRing R] (u v x : R) :
    3 * (u ^ 2 + v ^ 2 + x ^ 2) = 2 * (u + v + x) ^ 2 + homogKoideResolvent u v x ∧
      (x - 2 * (u + v)) ^ 2 = homogKoideResolvent u v x + 3 * (u ^ 2 + 4 * u * v + v ^ 2) ∧
      u ^ 2 + 4 * u * v + v ^ 2 = (u + v) ^ 2 + 2 * u * v ∧
      u ^ 2 + 4 * u * v + v ^ 2 = (u - v) ^ 2 + 6 * u * v := by
  unfold homogKoideResolvent
  exact ⟨by ring, by ring, by ring, by ring⟩

/-- **Ordered-Ring Koide Discriminant Positivity & Hierarchy Branch Dominance**
(over any `[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]`, requiring **zero** field structure):
1. Whenever $0 \le u$, $0 \le v$, and $0 < u + v$, the quadratic discriminant
   $\Delta(u, v) = 12(u^2 + 4uv + v^2)$ is **strictly positive**;
2. For any positive root $0 < s$ with $s^2 = 3(u^2 + 4uv + v^2)$ and $0 \le u, 0 \le v$, the upper
   root $x_+ = 2(u + v) + s$ annihilates `homogKoideResolvent u v` and strictly dominates
   $2(u + v)$, $u$, and $v$. -/
theorem koide_discriminant_pos_and_upper_root_dominance
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (u v : R) (hu : 0 ≤ u) (hv : 0 ≤ v) (huv : 0 < u + v) :
    0 < 12 * (u ^ 2 + 4 * u * v + v ^ 2) ∧
      ∀ s : R, s ^ 2 = 3 * (u ^ 2 + 4 * u * v + v ^ 2) → 0 < s →
        homogKoideResolvent u v (2 * (u + v) + s) = 0 ∧
          2 * (u + v) < 2 * (u + v) + s ∧
          u < 2 * (u + v) + s ∧
          v < 2 * (u + v) + s := by
  have hsq_pos : 0 < (u + v) ^ 2 := by rw [sq]; exact mul_pos huv huv
  have hmul_nonneg : 0 ≤ 2 * u * v := by
    have h2u : 0 ≤ 2 * u := by linarith
    exact mul_nonneg h2u hv
  have hcore_eq : u ^ 2 + 4 * u * v + v ^ 2 = (u + v) ^ 2 + 2 * u * v := by ring
  have hcore_pos : 0 < u ^ 2 + 4 * u * v + v ^ 2 := by linarith
  refine ⟨by linarith, ?_⟩
  intro s hs hs_pos
  refine ⟨?_, by linarith, by linarith, by linarith⟩
  unfold homogKoideResolvent
  linear_combination hs

/-- **Division-Free Saddle Elimination of $v = \sqrt{m_\mu}$ over `[CommRing R]`:**
if $3(u^2 + v^2 + x^2) = 2(u + v + x)^2$ and $v^2 (q - 1)^2 = q^2 \cdot \mathrm{vol41} \cdot u^2$
(the cleared-denominator form of $(v/u)^2 (1 - q^{-1})^2 = \mathrm{vol41}$), then $x$ satisfies the
exact division-free, $v$-free quartic equation over $R$:
$\bigl((q - 1)^2 (x^2 - 4ux + u^2) + q^2 \cdot \mathrm{vol41} \cdot u^2\bigr)^2
= 16 (q - 1)^2 q^2 \cdot \mathrm{vol41} \cdot u^2 (x + u)^2$. -/
theorem koide_saddle_quartic_eliminating_v {R : Type*} [CommRing R]
    (u v x q vol41 : R)
    (hkoide : 3 * (u ^ 2 + v ^ 2 + x ^ 2) = 2 * (u + v + x) ^ 2)
    (hmuon : v ^ 2 * (q - 1) ^ 2 = q ^ 2 * vol41 * u ^ 2) :
    (x ^ 2 - 4 * u * x + u ^ 2 + v ^ 2) ^ 2 = 16 * (x + u) ^ 2 * v ^ 2 ∧
      ((q - 1) ^ 2 * (x ^ 2 - 4 * u * x + u ^ 2) + q ^ 2 * vol41 * u ^ 2) ^ 2 =
        16 * (q - 1) ^ 2 * q ^ 2 * vol41 * u ^ 2 * (x + u) ^ 2 := by
  have hlin : x ^ 2 - 4 * u * x + u ^ 2 + v ^ 2 = 4 * (x + u) * v := by
    linear_combination hkoide
  have hsq : (x ^ 2 - 4 * u * x + u ^ 2 + v ^ 2) ^ 2 = 16 * (x + u) ^ 2 * v ^ 2 := by
    rw [hlin]; ring
  refine ⟨hsq, ?_⟩
  have hsub :
      (q - 1) ^ 2 * (x ^ 2 - 4 * u * x + u ^ 2) + q ^ 2 * vol41 * u ^ 2 =
        (q - 1) ^ 2 * (x ^ 2 - 4 * u * x + u ^ 2 + v ^ 2) := by
    linear_combination -hmuon
  rw [hsub]
  linear_combination (q - 1) ^ 4 * hsq + 16 * (q - 1) ^ 2 * (x + u) ^ 2 * hmuon

/-- **Radical-Free Symmetric Quartic Koide Mass Polynomial over `[CommRing R]`:**
eliminates all square roots $(\sqrt{m_1}, \sqrt{m_2}, \sqrt{m_3})$ so Koide's relation lives
purely in the polynomial ring $R[m_1, m_2, m_3]$ (`owner-rulings.md` rows 24, 206, 212):
$K_4(m_1, m_2, m_3) := \bigl((m_1 + m_2 + m_3)^2 - 16(m_1 m_2 + m_2 m_3 + m_3 m_1)\bigr)^2
- 1536 (m_1 + m_2 + m_3) m_1 m_2 m_3$. -/
def koideMassQuarticPoly {R : Type*} [CommRing R] (m₁ m₂ m₃ : R) : R :=
  ((m₁ + m₂ + m₃) ^ 2 - 16 * (m₁ * m₂ + m₂ * m₃ + m₃ * m₁)) ^ 2 -
    1536 * (m₁ + m₂ + m₃) * m₁ * m₂ * m₃

/-- **Exact 4-Branch Galois Factorization of `koideMassQuarticPoly` over `[CommRing R]`:**
$K_4(u^2, v^2, x^2)$ equals the product of the four signed root-mass Koide quadratics
$\prod_{\varepsilon_1, \varepsilon_2 \in \{\pm 1\}} \bigl(3(u^2 + v^2 + x^2) - 2(u + \varepsilon_1 v + \varepsilon_2 x)^2\bigr)$,
and therefore vanishes identically whenever $3(u^2 + v^2 + x^2) = 2(u + v + x)^2$. -/
theorem koideMassQuarticPoly_galois_factorization {R : Type*} [CommRing R] (u v x : R) :
    koideMassQuarticPoly (u ^ 2) (v ^ 2) (x ^ 2) =
      (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v + x) ^ 2) *
        (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v - x) ^ 2) *
        (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u - v + x) ^ 2) *
        (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (-u + v + x) ^ 2) ∧
      (3 * (u ^ 2 + v ^ 2 + x ^ 2) = 2 * (u + v + x) ^ 2 →
        koideMassQuarticPoly (u ^ 2) (v ^ 2) (x ^ 2) = 0) := by
  have hfac :
      koideMassQuarticPoly (u ^ 2) (v ^ 2) (x ^ 2) =
        (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v + x) ^ 2) *
          (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v - x) ^ 2) *
          (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u - v + x) ^ 2) *
          (3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (-u + v + x) ^ 2) := by
    unfold koideMassQuarticPoly
    ring
  refine ⟨hfac, ?_⟩
  intro hk
  rw [hfac]
  have hz : 3 * (u ^ 2 + v ^ 2 + x ^ 2) - 2 * (u + v + x) ^ 2 = 0 := by linear_combination hk
  rw [hz, zero_mul, zero_mul, zero_mul]

end ResolventAndQuarticMassPolynomial

/-! ## §4. Narrowed Rule-13a Physical Bridge (`KoideSingletDoubletEquipartitionBridge`) & Consistency Witnesses -/

section NarrowedPhysicalBridge

/-- **Narrowed Rule-13a Zero-Instance Physical Bridge (`KoideSingletDoubletEquipartitionBridge`):**
With 100% of the $S_3 / \mathbb{Z}_3$ projector algebra, Fourier spectral moments, classical
$V^{\otimes 3} = (\mathbf{4}\otimes\mathbf{1}) \oplus (\mathbf{2}\otimes\mathbf{2})$ $4 = 4$
equipartition, quadratic resolvent, and radical-free quartic mass polynomial proved unconditionally
over `[CommRing R]` in §§1–3, this class isolates the **single irreducible physical assumption**
remaining in `qou-cw8i`: that the physical charged-lepton root-mass vector
$\lambda = (u_e, u_\mu, u_\tau) \in R^3$ preserves exact singlet–doublet norm equipartition
$\|3 P_{\mathbf{1}} \lambda\|_3^2 = \|3 P_{\mathrm{std}} \lambda\|_3^2$ (undressed by the
$(q^2 - 1)^2$ quantum-dimension deformation). Zero global `instance`s exist. -/
class KoideSingletDoubletEquipartitionBridge (R : Type*) [CommRing R] where
  /-- Charged-lepton root-mass triple $\lambda = (u_e, u_\mu, u_\tau) \in R^3$. -/
  leptonRootMass : Fin 3 → R
  /-- Irreducible physical singlet–doublet norm equipartition $\|3 P_{\mathbf{1}} \lambda\|_3^2 = \|3 P_{\mathrm{std}} \lambda\|_3^2$. -/
  singlet_eq_doublet :
    normSq3 (threeSingletVec leptonRootMass) = normSq3 (threeDoubletVec leptonRootMass)

/-- **Trivial model (Pattern-3.3 consistency witness):**
proves `KoideSingletDoubletEquipartitionBridge R` is consistent over every `[CommRing R]`.
Declared as `def` (never `instance`) so typeclass search is never polluted. -/
-- Ref: [koide1983prd] Phys. Rev. D 28 (1983) 252
def trivialModel (R : Type*) [CommRing R] :
    KoideSingletDoubletEquipartitionBridge R where
  leptonRootMass := fun _ => 0
  singlet_eq_doublet := by
    simp [threeSingletVec, threeDoubletVec, threeProjSinglet3, threeProjDoublet3,
      Matrix.mulVec, dotProduct, normSq3]

/-- **Non-zero algebraic Brannen–Koide consistency witness (`def`, not `instance`):**
any ring carrying $c^2 + s^2 = 1$, $r_2^2 = 2$, $r_3^2 = 3$ realizes
`KoideSingletDoubletEquipartitionBridge R` with non-vanishing trace sum $6$ and norm squared $24$. -/
-- Ref: [foot1994] arXiv:hep-ph/9402242
def brannenAlgebraicModel {R : Type*} [CommRing R] (c s r₂ r₃ : R)
    (hcs : c ^ 2 + s ^ 2 = 1) (hr2 : r₂ ^ 2 = 2) (hr3 : r₃ ^ 2 = 3) :
    KoideSingletDoubletEquipartitionBridge R where
  leptonRootMass := twoBrannenVec c s r₂ r₃
  singlet_eq_doublet := (twoBrannenVec_exact_equipartition c s r₂ r₃ hcs hr2 hr3).2.2.2

/-- **Unconditional Consequences of `KoideSingletDoubletEquipartitionBridge` over `[CommRing R]`:**
over any $3$-torsion-free `[CommRing R]`, `[B : KoideSingletDoubletEquipartitionBridge R]`
forces the homogeneous monic quadratic resolvent `homogKoideResolvent u v x = 0` AND the
radical-free quartic mass polynomial `koideMassQuarticPoly (u²) (v²) (x²) = 0`. -/
theorem bridge_implies_resolvent_and_quartic {R : Type*} [CommRing R]
    (h3 : ∀ z : R, 3 * z = 0 → z = 0)
    [B : KoideSingletDoubletEquipartitionBridge R] :
    let u := B.leptonRootMass 0
    let v := B.leptonRootMass 1
    let x := B.leptonRootMass 2
    3 * (u ^ 2 + v ^ 2 + x ^ 2) = 2 * (u + v + x) ^ 2 ∧
      homogKoideResolvent u v x = 0 ∧
      koideMassQuarticPoly (u ^ 2) (v ^ 2) (x ^ 2) = 0 := by
  dsimp only
  have hk3 : 3 * normSq3 B.leptonRootMass =
      2 * (B.leptonRootMass 0 + B.leptonRootMass 1 + B.leptonRootMass 2) ^ 2 :=
    (singlet_doublet_equipartition_iff_koide_ring h3 B.leptonRootMass).mp B.singlet_eq_doublet
  have hk :
      3 * (B.leptonRootMass 0 ^ 2 + B.leptonRootMass 1 ^ 2 + B.leptonRootMass 2 ^ 2) =
        2 * (B.leptonRootMass 0 + B.leptonRootMass 1 + B.leptonRootMass 2) ^ 2 := by
    simpa [normSq3] using hk3
  have hres : homogKoideResolvent (B.leptonRootMass 0) (B.leptonRootMass 1) (B.leptonRootMass 2) = 0 := by
    have hid := (homogKoideResolvent_identities
      (B.leptonRootMass 0) (B.leptonRootMass 1) (B.leptonRootMass 2)).1
    linear_combination hk - hid
  exact ⟨hk, hres,
    (koideMassQuarticPoly_galois_factorization
      (B.leptonRootMass 0) (B.leptonRootMass 1) (B.leptonRootMass 2)).2 hk⟩

end NarrowedPhysicalBridge

/-! ## §5. 2026-11-28 Ruled Least-Crossing 2-Component Lepton Link Ladder Invariants (`[CommRing R]`) -/

section LeastCrossingLinkLadder

/-- Signed writhe of a 3-strand braid word `w : Word` (`true` = `+1`, `false` = `-1`). -/
def wordWrithe : Word → ℤ
  | [] => 0
  | (_, s) :: rest => (if s then 1 else -1) + wordWrithe rest

/-- Strand-component assignment `Fin 3 → Bool` transported through a single generator `i : Fin 2`
(swapping slots `0, 1` for `i = 0` and slots `1, 2` for `i = 1`). -/
def swapLabels (i : Fin 2) (lbl : Fin 3 → Bool) : Fin 3 → Bool :=
  fun k => lbl (gen i k)

/-- Inter-component signed crossing sum (equal to $2\,\mathrm{lk}(L_1, L_2)$ when `lbl` labels the
two closure components at the right/bottom end of `w`, since letters on the right act first in
`permOf` / `imgZ`). -/
def interWritheFrom : Word → (Fin 3 → Bool) → ℤ
  | [], _ => 0
  | (i, s) :: rest, lbl =>
      let lbl' := rest.foldr (fun x acc => swapLabels x.1 acc) lbl
      let a := if i = 0 then lbl' 0 else lbl' 1
      let b := if i = 0 then lbl' 1 else lbl' 2
      (if a != b then (if s then 1 else -1) else 0) + interWritheFrom rest lbl

/-- Intra-component (self-crossing) writhe sum along `w`. -/
def selfWritheFrom : Word → (Fin 3 → Bool) → ℤ
  | [], _ => 0
  | (i, s) :: rest, lbl =>
      let lbl' := rest.foldr (fun x acc => swapLabels x.1 acc) lbl
      let a := if i = 0 then lbl' 0 else lbl' 1
      let b := if i = 0 then lbl' 1 else lbl' 2
      (if a == b then (if s then 1 else -1) else 0) + selfWritheFrom rest lbl

/-- Exact partition of total braid writhe into inter-component ($2\,\mathrm{lk}$) and self-writhe
contributions for every 3-braid word `w` and component colouring `lbl`. -/
theorem wordWrithe_eq_inter_add_self (w : Word) (lbl : Fin 3 → Bool) :
    wordWrithe w = interWritheFrom w lbl + selfWritheFrom w lbl := by
  induction w with
  | nil => rfl
  | cons x rest ih =>
    rcases x with ⟨i, s⟩
    simp only [wordWrithe, interWritheFrom, selfWritheFrom]
    rw [ih]
    set a := (if i = 0 then (List.foldr (fun x acc => swapLabels x.1 acc) lbl rest) 0
              else (List.foldr (fun x acc => swapLabels x.1 acc) lbl rest) 1)
    set b := (if i = 0 then (List.foldr (fun x acc => swapLabels x.1 acc) lbl rest) 1
              else (List.foldr (fun x acc => swapLabels x.1 acc) lbl rest) 2)
    cases a <;> cases b <;> cases s <;> simp <;> ring

/-- Canonical 2-component strand labels (`true` = isolated 1-cycle strand, `false` = 2-cycle strands)
for the 2026-11-28 least-crossing lepton words:
- `wE = σ₀σ₁σ₀` and `wTau = σ₀²σ₁⁻¹σ₀σ₁⁻¹` fix strand `1` (`lbl1Cycle1`),
- `wMu = σ₀⁴σ₁⁻¹` fixes strand `0` (`lbl1Cycle0`). -/
def lbl1Cycle1 : Fin 3 → Bool := ![false, true, false]
def lbl1Cycle0 : Fin 3 → Bool := ![true, false, false]

/-- Minimal link crossing numbers `(2, 4, 5)` of the closures `(Hopf, T(2,4), Whitehead)`
(`owner-rulings.md` row 17). -/
def leastCrossingLinkCount : Fin 3 → ℕ := ![2, 4, 5]

/-- **Exact Combinatorial, Closure-Component, Writhe & Linking Invariants of the 2026-11-28
Least-Crossing 2-Component Lepton Link Ladder (`owner-rulings.md` row 17):**
- `wE = σ₀σ₁σ₀` (Hopf): word length `3`, `2` closure components, writhe `+3`, `2·lk = +2` (`lk = 1`, `self = +1`), crossing number `2`;
- `wMu = σ₀⁴σ₁⁻¹` ($T(2,4)$): word length `5`, `2` closure components, writhe `+3`, `2·lk = +4` (`lk = 2`, `self = -1`), crossing number `4`;
- `wTau = σ₀²σ₁⁻¹σ₀σ₁⁻¹` (Whitehead): word length `5`, `2` closure components, writhe `+1`, `2·lk = 0` (`lk = 0`, `self = +1`), crossing number `5`;
- Minimal link crossing numbers strictly ascend (`2 < 4 < 5`), whereas $U(1) = 3\,\mathrm{lk} = (3, 6, 0)$ is non-monotone. -/
theorem least_crossing_ladder_combinatorial_invariants :
    wE.length = 3 ∧ wMu.length = 5 ∧ wTau.length = 5 ∧
      numCycles (permOf (wE.map Prod.fst)) = 2 ∧
      numCycles (permOf (wMu.map Prod.fst)) = 2 ∧
      numCycles (permOf (wTau.map Prod.fst)) = 2 ∧
      List.foldr (fun x acc => swapLabels x.1 acc) lbl1Cycle1 wE = lbl1Cycle1 ∧
      List.foldr (fun x acc => swapLabels x.1 acc) lbl1Cycle0 wMu = lbl1Cycle0 ∧
      List.foldr (fun x acc => swapLabels x.1 acc) lbl1Cycle1 wTau = lbl1Cycle1 ∧
      wordWrithe wE = 3 ∧ wordWrithe wMu = 3 ∧ wordWrithe wTau = 1 ∧
      interWritheFrom wE lbl1Cycle1 = 2 ∧
      interWritheFrom wMu lbl1Cycle0 = 4 ∧
      interWritheFrom wTau lbl1Cycle1 = 0 ∧
      selfWritheFrom wE lbl1Cycle1 = 1 ∧
      selfWritheFrom wMu lbl1Cycle0 = -1 ∧
      selfWritheFrom wTau lbl1Cycle1 = 1 ∧
      leastCrossingLinkCount 0 < leastCrossingLinkCount 1 ∧
      leastCrossingLinkCount 1 < leastCrossingLinkCount 2 := by
  refine ⟨rfl, rfl, rfl,
    numCycles_permOf_of_odd _ rfl,
    numCycles_permOf_of_odd _ rfl,
    numCycles_permOf_of_odd _ rfl,
    ?_, ?_, ?_,
    by decide, by decide, by decide,
    by decide, by decide, by decide,
    by decide, by decide, by decide,
    by decide, by decide⟩
  · ext k; fin_cases k <;> decide
  · ext k; fin_cases k <;> decide
  · ext k; fin_cases k <;> decide

/-- Cleared-denominator two-colour Casimir coefficients ($6\kappa_2 = \mathrm{lk}^2$ and
$9\kappa_3 = \mathrm{lk}^3 - \mathrm{lk} - 12 a_3$, extending `#9983` / `2026-11-28-muon-mass-relation.md` §6):
for $(e, \mu, \tau)$ with $\mathrm{lk} = (1, 2, 0)$ and Conway $z^3$-coefficients $a_3 = (0, 1, -1)$,
$6\kappa_2 = (1, 4, 0)$ and $9\kappa_3 = (0, -6, 12)$. -/
theorem two_colour_casimir_kappa2_kappa3_integers :
    let lk : Fin 3 → ℤ := ![1, 2, 0]
    let a3 : Fin 3 → ℤ := ![0, 1, -1]
    let sixKappa2 : Fin 3 → ℤ := fun i => (lk i) ^ 2
    let nineKappa3 : Fin 3 → ℤ := fun i => (lk i) ^ 3 - lk i - 12 * a3 i
    sixKappa2 0 = 1 ∧ sixKappa2 1 = 4 ∧ sixKappa2 2 = 0 ∧
      nineKappa3 0 = 0 ∧ nineKappa3 1 = -6 ∧ nineKappa3 2 = 12 := by
  decide

/-! ### Reduced Burau Representation over `[CommRing R]` (`t : Rˣ`) & Universal `t = -1` Determinant-Trace Identity -/

section ReducedBurauCommRing

variable {R : Type*} [CommRing R]

/-- Reduced $2\times 2$ Burau generators of $B_3$ over any `[CommRing R]` for a unit `t : Rˣ`
(requiring **zero** `[Field]` structure). -/
def burauGen (t : Rˣ) : Fin 2 → Bool → Matrix (Fin 2) (Fin 2) R
  | 0, true => !![-(t : R), 1; 0, 1]
  | 0, false => !![-(↑t⁻¹ : R), (↑t⁻¹ : R); 0, 1]
  | 1, true => !![1, 0; (t : R), -(t : R)]
  | 1, false => !![1, 0; 1, -(↑t⁻¹ : R)]

/-- Reduced Burau matrix of a 3-strand signed braid word `w : Word`. -/
def burauWord (t : Rˣ) : Word → Matrix (Fin 2) (Fin 2) R
  | [] => 1
  | (i, s) :: rest => burauGen t i s * burauWord t rest

/-- **Invertibility & Artin Braid Relation for `burauGen` over any `[CommRing R]`:**
$\sigma_i \sigma_i^{-1} = I_2 = \sigma_i^{-1} \sigma_i$ and
$\sigma_0 \sigma_1 \sigma_0 = \sigma_1 \sigma_0 \sigma_1$. -/
theorem burauGen_inv_and_artin_braid (t : Rˣ) :
    (∀ i : Fin 2, burauGen t i true * burauGen t i false = 1 ∧
        burauGen t i false * burauGen t i true = 1) ∧
      burauGen t 0 true * burauGen t 1 true * burauGen t 0 true =
        burauGen t 1 true * burauGen t 0 true * burauGen t 1 true := by
  refine ⟨?_, ?_⟩
  · intro i
    fin_cases i <;> refine ⟨?_, ?_⟩ <;> ext a b <;> fin_cases a <;> fin_cases b <;>
      simp [burauGen, Matrix.mul_apply, Fin.sum_univ_two]
  · ext a b; fin_cases a <;> fin_cases b <;>
      simp [burauGen, Matrix.mul_apply, Fin.sum_univ_two]

/-- Every generator in `genZ` has determinant `1`, hence `det (imgZ w) = 1` for **all** `w : Word`. -/
theorem det_imgZ_eq_one (w : Word) : (imgZ w).det = 1 := by
  induction w with
  | nil => simp [imgZ]
  | cons x rest ih =>
    rcases x with ⟨i, s⟩
    simp only [imgZ, Matrix.det_mul, ih, mul_one]
    fin_cases i <;> cases s <;> simp [genZ, Matrix.det_fin_two]

/-- **Specialization of Reduced Burau at `t = -1 : Rˣ` to `SL(2, ℤ)`:**
for **every** 3-braid word `w : Word` over **any `[CommRing R]`**,
`burauWord (-1) w = (imgZ w).map (Int.castRingHom R)`. -/
theorem burauWord_neg_one_eq_imgZ (w : Word) :
    burauWord (-1 : Rˣ) w = (imgZ w).map (Int.castRingHom R) := by
  have hgen : ∀ (i : Fin 2) (s : Bool),
      burauGen (-1 : Rˣ) i s = (genZ i s).map (Int.castRingHom R) := by
    intro i s
    fin_cases i <;> cases s <;> ext a b <;> fin_cases a <;> fin_cases b <;>
      simp [burauGen, genZ]
  induction w with
  | nil => simp [burauWord, imgZ, Matrix.map_one]
  | cons x rest ih =>
    rcases x with ⟨i, s⟩
    simp only [burauWord, imgZ, Matrix.map_mul, hgen, ih]

/-- **Universal 3-Braid Determinant-vs-Trace Theorem at `t = -1` over `[CommRing R]`:**
for **every** 3-strand braid word `w : Word` (closing the general statement noted as checked only
on three words in `LeptonMassAtI.lean`),
$\det(I_2 - B_w(-1)) = 2 - \mathrm{tr}(\mathrm{imgZ}\,w)$. -/
theorem det_one_sub_burau_neg_one_eq_two_sub_trace (w : Word) :
    (1 - burauWord (-1 : Rˣ) w).det = 2 - ((imgZ w).trace : R) := by
  rw [burauWord_neg_one_eq_imgZ]
  set M := (imgZ w).map (Int.castRingHom R)
  have hdet_int : (((imgZ w).det : ℤ) : R) = 1 := by rw [det_imgZ_eq_one]; simp
  have hdetM : M.det = 1 := by
    simpa [M, Matrix.det_fin_two] using hdet_int
  have htrM : M.trace = ((imgZ w).trace : R) := by
    simp [M, Matrix.trace_fin_two]
  have hcayley : (1 - M).det = 1 - M.trace + M.det := by
    simp [Matrix.det_fin_two, Matrix.trace_fin_two]; ring
  rw [hcayley, hdetM, htrM]
  ring

/-- **Morton–Birman Reduced Burau Traces & Alexander Factorizations on `(e, μ, τ, 4₁)` over `[CommRing R]`:**
for any unit `t : Rˣ` in `[CommRing R]`:
- `e = σ₀σ₁σ₀` (2-component Hopf, $\Delta_L = 1$): $\mathrm{tr}\,B_e(t) = 0$ and $\det(I_2 - B_e(t)) = 1 - t^3$;
- `μ = σ₀⁴σ₁⁻¹` (2-component $T(2,4)$, $\Delta_L = 1 + t^2$):
  $t \cdot \mathrm{tr}\,B_\mu(t) = t^5 - t^4 + t^3 - t^2 + t - 1$ and
  $t \cdot \det(I_2 - B_\mu(t)) = (1 - t^3)(1 + t^2)$;
- `τ = σ₀²σ₁⁻¹σ₀σ₁⁻¹` (2-component Whitehead, $\Delta_L = (t - 1)^2$):
  $t^2 \cdot \mathrm{tr}\,B_\tau(t) = -t^5 + 2 t^4 - 2 t^3 + 2 t^2 - 2 t + 1$ and
  $t^2 \cdot \det(I_2 - B_\tau(t)) = (t^3 - 1)(t - 1)^2$;
- `4₁ = (σ₀σ₁⁻¹)²` (1-component figure-eight knot, $\Delta_K = t^2 - 3t + 1$, lacking the second-component $(1 - t)$ factor):
  $t^2 \cdot \det(I_2 - B_{4_1}(t)) = -(1 + t + t^2)(t^2 - 3t + 1)$;
- Specializing to `t = -1 : Rˣ` recovers $\det(I_2 - B_w(-1)) = (2, -4, -8, -5)$ (`|det| = (2, 4, 8, 5)`). -/
theorem morton_birman_burau_ladder_invariants (t : Rˣ) :
    (burauWord t wE).trace = 0 ∧
      (1 - burauWord t wE).det = 1 - (t : R) ^ 3 ∧
      (t : R) * (burauWord t wMu).trace =
        (t : R) ^ 5 - (t : R) ^ 4 + (t : R) ^ 3 - (t : R) ^ 2 + (t : R) - 1 ∧
      (t : R) * (1 - burauWord t wMu).det = (1 - (t : R) ^ 3) * (1 + (t : R) ^ 2) ∧
      (t : R) ^ 2 * (burauWord t wTau).trace =
        -(t : R) ^ 5 + 2 * (t : R) ^ 4 - 2 * (t : R) ^ 3 + 2 * (t : R) ^ 2 - 2 * (t : R) + 1 ∧
      (t : R) ^ 2 * (1 - burauWord t wTau).det = ((t : R) ^ 3 - 1) * ((t : R) - 1) ^ 2 ∧
      (t : R) ^ 2 * (1 - burauWord t wFig8).det =
        -(1 + (t : R) + (t : R) ^ 2) * ((t : R) ^ 2 - 3 * (t : R) + 1) ∧
      (1 - burauWord (-1 : Rˣ) wE).det = 2 ∧
      (1 - burauWord (-1 : Rˣ) wMu).det = -4 ∧
      (1 - burauWord (-1 : Rˣ) wTau).det = -8 ∧
      (1 - burauWord (-1 : Rˣ) wFig8).det = -5 := by
  have ht : (t : R) * (↑t⁻¹ : R) = 1 := Units.mul_inv t
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp [wE, burauWord, burauGen, Matrix.trace_fin_two]
  · simp [wE, burauWord, burauGen, Matrix.det_fin_two]; ring
  · simp [wMu, burauWord, burauGen, Matrix.trace_fin_two]
    linear_combination -1 * ht
  · simp [wMu, burauWord, burauGen, Matrix.det_fin_two]
    linear_combination (1 + (t : R) ^ 3 - (t : R) ^ 4) * ht
  · simp [wTau, burauWord, burauGen, Matrix.trace_fin_two]
    linear_combination ((t : R) ^ 2 + (t : R) * (↑t⁻¹ : R) - 2 * (t : R) + 1) * ht
  · simp [wTau, burauWord, burauGen, Matrix.det_fin_two]
    linear_combination
      (-(t : R) ^ 4 * (↑t⁻¹ : R) + (t : R) ^ 4 + (t : R) ^ 3 * (↑t⁻¹ : R) -
        2 * (t : R) ^ 3 - (t : R) ^ 2 - (t : R) * (↑t⁻¹ : R) + 2 * (t : R) - 1) * ht
  · simp [wFig8, wL, burauWord, burauGen, Matrix.det_fin_two]
    linear_combination
      ((t : R) ^ 3 * (↑t⁻¹ : R) - (t : R) ^ 3 - (t : R) ^ 2 * (↑t⁻¹ : R) +
        2 * (t : R) ^ 2 - (t : R) * (↑t⁻¹ : R) + 2 * (t : R) - 1) * ht
  · rw [det_one_sub_burau_neg_one_eq_two_sub_trace, traces.1]; simp
  · rw [det_one_sub_burau_neg_one_eq_two_sub_trace, traces.2.1]; simp; ring
  · rw [det_one_sub_burau_neg_one_eq_two_sub_trace, traces.2.2.1]; simp; ring
  · rw [det_one_sub_burau_neg_one_eq_two_sub_trace, traces.2.2.2]; simp; ring

/-- Cleared-denominator $N = 2$ ring masses $q^{12} m_e(q)$, $q^{12} m_\mu(q)$, $q^{12} m_\tau(q)$
of the 2026-11-28 least-crossing ladder (`LeptonLinkLadderReadings`) over any `[CommRing R]`. -/
def q12MassE (q : R) : R := q ^ 6 * (q ^ 2 + 1) * (q ^ 4 + 1)
def q12MassMu (q : R) : R := (q ^ 2 + 1) * (q ^ 8 + q ^ 4 - q ^ 2 + 1)
def q12MassTau (q : R) : R := q ^ 4 * (q ^ 2 + 1) * (q ^ 10 - q ^ 8 + 2 * q ^ 6 - q ^ 4 + 2 * q ^ 2 - 1)

/-- **Exact $q^{12}$-Skein Differences & Classical $q = 1$ Pure-Singlet Collapse on the Least-Crossing Ladder:**
1. $q^{12} m_e(q) = q^{12} m_\mu(q) + (q^{12} - 1)$ (so $m_e(q) - m_\mu(q) = 1 - q^{-12}$);
2. $q^{12} m_\tau(q) = q^{12} m_e(q) + q^4 (q^{12} - 1)$ (so $m_\tau(q) - m_e(q) = q^4 (m_e(q) - m_\mu(q))$);
3. At $q = 1$, $(q^{12} m_e, q^{12} m_\mu, q^{12} m_\tau) = (4, 4, 4)$ has **identically zero**
   $S_3$-doublet component (`threeDoubletVec ![4, 4, 4] = 0`), proving over `[CommRing R]` why
   bare $q \to 1$ ring traces yield $Q = 1/3$ rather than Koide's equipartitioned $Q = 2/3$. -/
theorem q12_ring_mass_skein_differences_and_singlet_collapse (q : R) :
    q12MassE q = q12MassMu q + (q ^ 12 - 1) ∧
      q12MassTau q = q12MassE q + q ^ 4 * (q ^ 12 - 1) ∧
      q12MassTau q - q12MassE q = q ^ 4 * (q12MassE q - q12MassMu q) ∧
      q12MassE (1 : R) = 4 ∧
      q12MassMu (1 : R) = 4 ∧
      q12MassTau (1 : R) = 4 ∧
      threeDoubletVec ![q12MassE (1 : R), q12MassMu (1 : R), q12MassTau (1 : R)] = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · unfold q12MassE q12MassMu; ring
  · unfold q12MassTau q12MassE; ring
  · unfold q12MassTau q12MassE q12MassMu; ring
  · unfold q12MassE; ring
  · unfold q12MassMu; ring
  · unfold q12MassTau; ring
  · ext i; fin_cases i <;>
      simp [threeDoubletVec, threeProjDoublet3, q12MassE, q12MassMu, q12MassTau,
        Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> ring

end ReducedBurauCommRing

end LeastCrossingLinkLadder

end QOU.StandardModel.KoideSingletDoubletEquipartition
