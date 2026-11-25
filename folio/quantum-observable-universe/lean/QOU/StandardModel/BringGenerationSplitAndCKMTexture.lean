import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic
import BraidKnotOctonion.S5CharactersOnBringDeformations
import QCalculus.QIntegerAlexanderTorus

set_option autoImplicit false

/-!
# Bring Curve Canonical Differential Branching, $S_3 \subset S_5$ CKM/PMNS Overlap Algebra, and $(2,7)$-Cabled Figure-Eight Satellite Factorisation

Pure-algebraic Lean 4 formalization for Standard Model Package 1 (`qou-gen3` / `Q-Gap-7`,
aggregating `qou-x4qm`, `qou-xtcl`, `qou-htk4`, `qou-y0mq`), authored strictly over generic
rings and fields (`{R : Type*} [CommRing R]`, `{F : Type*} [Field F]`, and `ℤ` character tables;
AGENTS.md §7c, zero `ℝ`, zero empirical literals, zero `sorry`, standard axioms only):

1. **§1 — Bring Curve Canonical Differential Space $V_{\mathrm{std}}$ Branching & Honest Generation Scope:**
   - Consumes `QOU.Brings.S5Char.chiStd` ($V_{(4,1)} \cong H^0(\mathcal{B}, K_{\mathcal{B}})$ on Bring's
     genus-$4$ curve $\mathcal{B} \subset \mathbb{P}^4$) and proves the exact subgroup character
     branching rules:
     * $\mathrm{Res}^{S_5}_{S_4} V_{(4,1)} = V_{(3,1)} \oplus V_{(4)}$ ($4 \to 3 \oplus 1$),
     * $\mathrm{Res}^{S_5}_{S_3} V_{(4,1)} = V_{(2,1)} \oplus 2\,V_{(3)}$ ($3 \to 2 \oplus 1$ on $V_{(3,1)}$),
     * $\mathrm{Res}^{S_5}_{S_3 \times S_2} V_{(4,1)} = (V_{(2,1)} \boxtimes 1) \oplus (1 \boxtimes 1) \oplus (1 \boxtimes \mathrm{sgn})$ ($4 \to 2 \oplus 1 \oplus 1'$).
   - Constructs the explicit $S_4$-equivariant orthogonal idempotents `projGen3` and `projSing1`
     on $V_{\mathrm{std}} = \{x \in F^5 \mid \sum_i x_i = 0\}$ over any `[Field F]` (`(4 : F) ≠ 0`),
     proving completeness, idempotency, mutual annihilation, $S_4$-intertwining, and explicit
     3-element basis linear independence and spanning of `projGen3`, together with the $S_3$-equivariant
     refinement `projDoublet2 + projDem1 = projGen3` (`(3 : F) ≠ 0`).
   - Proves the Morgan–Voyce continuant harmonic factorisation
     $b_9(h) = b_3(h)(h^6 + 6h^4 + 9h^2 + 1)$ alongside the exact Bézout coprimality identities
     $b_3(h)(h^2 + 2) - b_5(h) = 1$ and $b_3(h)(h^4 + 4h^2 + 2) - b_7(h) = 1$ over any `CommRing R`.
   - **Honest Non-Claim Guardrail**: Formalizes the disagreement among the corpus's generation filters
     (`card = 4` vs `card = 3` vs `card = 2`) and isolates the equivariant spin/chirality singlet
     quotient as a **Rule-13a zero-instance `class BringChiralGenerationSelectionHypothesis`**, deriving
     `Module.finrank F (LinearMap.range chiralProj) = 3` via Mathlib's rank-nullity theorem.

2. **§2 — $S_3 \subset S_5$ Democratic/Tribimaximal Basis, Cabibbo Perturbation, & Unitary Jarlskog CP Invariant:**
   - Proves diagonalization of the rank-1 $S_3$-democratic matrix $D_3$ by the tribimaximal (TBM)
     basis (`(tbmIntMat R)ᵀ * D_3 * tbmIntMat R = diag(0, 9, 0)`) and exact orthogonality of the
     normalized TBM matrix `tbmUnitary` over any `[Field F]` with $s_2^2 = 2, s_3^2 = 3$.
   - Proves the Hoefsmit $(2,1)$ $H_3(q)$ braid relation and exact crossing-angle identity
     $\cos^2\theta_H(q) = 1/[2]_q^2$, $\sin^2\theta_H(q) = [3]_q/[2]_q^2$, plus the exact $2 \times 2$
     Cabibbo perturbation relation $([3]_q^2 + 4(q - q^{-1})^2)\sin^2(2\theta_{12}) = 4(q - q^{-1})^2$.
   - Defines the generic Gaussian extension `QuadI R` ($R[i]$ over any `[CommRing R]`) and proves:
     unitarity of $V = U_u^\dagger U_d$, quark-rephasing invariance of the Jarlskog invariant
     $J(V) = \mathrm{Im}(V_{01} V_{12} V_{02}^* V_{11}^*)$, row-orthogonality plaquette antisymmetry,
     Chau–Keung $3 \times 3$ unitarity, the exact factorisation
     $J = c_{12} s_{12} c_{23} s_{23} c_{13}^2 s_{13} s_\delta$, the integral-domain vanishing
     criterion ($J = 0 \iff$ an angle factor vanishes or $s_\delta = 0$), and CP-conjugation sign flip.

3. **§3 — Seifert–Torres $(2,7)$-Cabled Figure-Eight Satellite Alexander & Burau Factorisation:**
   - Proves the polynomial-framed $B_3$ reduced Burau clasp determinant identity
     $\det(t^2 I_2 - \widetilde{C}(t)^2) = t^2(1 + t + t^2)\Delta_{4_1}^{\mathrm{pos}}(t)$ for
     $\widetilde{C}(t) = t B(\sigma_1 \sigma_2^{-1})$ and $\Delta_{4_1}^{\mathrm{pos}}(t) = -1 + 3t - t^2$.
   - Combines $\Delta_{4_1}^{\mathrm{pos}}(t^2)$ with `QOU.BraidsAndKnots.QIntegerAlexanderTorus.alexanderTorus2`
     to prove the division-free rational form, cabled Burau determinant factorisation, degree-10
     palindromic expansion for the $\tau$ candidate $C_{2,7}(4_1)$, normalization $\Delta(1) = 1$,
     knot determinant $\Delta(-1) = 7$, and sign-indefiniteness witness across the golden-ratio node.

## References
- [fulton1991] W. Fulton, J. Harris, *Representation Theory: A First Course*, Springer (1991), §2.3.
- [jarlskog1985] C. Jarlskog, *Phys. Rev. Lett.* 55 (1985) 1039.
- [rolfsen1976] D. Rolfsen, *Knots and Links*, Publish or Perish (1976), §8.E Theorem 2.
- [leitner2026] QOU Appendix Standard Model (`sm-open-problems`, `sm-params-ckm`, `sm-params-lepton-masses`).
-/

namespace QOU.StandardModel.BringGenerationSplitAndCKMTexture

open scoped BigOperators
open Matrix QOU.Brings QOU.BraidsAndKnots.QIntegerAlexanderTorus

-- ============================================================================
-- §1. Bring Curve Canonical Differential Space Branching & Generation Scope
-- ============================================================================

section BringCanonicalBranching

/-- Conjugacy class sizes of $S_4$ in order $(1^4), (2\cdot 1^2), (2^2), (3\cdot 1), (4)$. -/
def s4ClassSize : Fin 5 → ℤ := ![1, 6, 3, 8, 6]

/-- Inclusion of $S_4 = \mathrm{Stab}_{S_5}(4)$ conjugacy classes into the 7 classes of $S_5$
    (`1⁵, 2·1³, 2²·1, 3·1², 3·2, 4·1, 5` in `QOU.Brings.S5Char`). -/
def s4ToS5Class : Fin 5 → Fin 7 := ![0, 1, 2, 3, 5]

/-- Class-weighted character inner product $24 \langle \chi, \psi \rangle_{S_4}$. -/
def s4Inner (χ ψ : Fin 5 → ℤ) : ℤ :=
  s4ClassSize 0 * χ 0 * ψ 0 + s4ClassSize 1 * χ 1 * ψ 1 +
  s4ClassSize 2 * χ 2 * ψ 2 + s4ClassSize 3 * χ 3 * ψ 3 +
  s4ClassSize 4 * χ 4 * ψ 4

/-- Irreducible characters of $S_4$ (Fulton–Harris §2.3). -/
def s4ChiTriv : Fin 5 → ℤ := ![1, 1, 1, 1, 1]
def s4ChiSign : Fin 5 → ℤ := ![1, -1, 1, 1, -1]
def s4Chi22   : Fin 5 → ℤ := ![2, 0, 2, -1, 0]
def s4ChiStd  : Fin 5 → ℤ := ![3, 1, -1, 0, -1]
def s4Chi211  : Fin 5 → ℤ := ![3, -1, -1, 0, 1]

/-- Restriction of an $S_5$ class function to $S_4 \subset S_5$. -/
def resS5ToS4 (χ : Fin 7 → ℤ) : Fin 5 → ℤ := fun c => χ (s4ToS5Class c)

/-- Orthonormality of the 5 irreducible characters of $S_4$ ($|S_4| = 24$). -/
theorem s4_charTable_orthonormal :
    s4Inner s4ChiTriv s4ChiTriv = 24 ∧ s4Inner s4ChiSign s4ChiSign = 24 ∧
    s4Inner s4Chi22 s4Chi22 = 24 ∧ s4Inner s4ChiStd s4ChiStd = 24 ∧
    s4Inner s4Chi211 s4Chi211 = 24 ∧
    s4Inner s4ChiTriv s4ChiSign = 0 ∧ s4Inner s4ChiTriv s4Chi22 = 0 ∧
    s4Inner s4ChiTriv s4ChiStd = 0 ∧ s4Inner s4ChiTriv s4Chi211 = 0 ∧
    s4Inner s4ChiSign s4Chi22 = 0 ∧ s4Inner s4ChiSign s4ChiStd = 0 ∧
    s4Inner s4ChiSign s4Chi211 = 0 ∧ s4Inner s4Chi22 s4ChiStd = 0 ∧
    s4Inner s4Chi22 s4Chi211 = 0 ∧ s4Inner s4ChiStd s4Chi211 = 0 := by
  decide

/-- **Exact $S_5 \downarrow S_4$ branching of $H^0(\mathcal{B}, K_{\mathcal{B}}) \cong V_{(4,1)}$**:
    $\mathrm{Res}^{S_5}_{S_4} V_{(4,1)} = V_{(3,1)} \oplus V_{(4)}$ ($4 \to 3 \oplus 1$). -/
theorem bring_h0_canonical_branch_s4 :
    (∀ c : Fin 5, resS5ToS4 S5Char.chiStd c = s4ChiStd c + s4ChiTriv c) ∧
    s4Inner (resS5ToS4 S5Char.chiStd) s4ChiStd = 24 ∧
    s4Inner (resS5ToS4 S5Char.chiStd) s4ChiTriv = 24 ∧
    s4Inner (resS5ToS4 S5Char.chiStd) s4ChiSign = 0 ∧
    s4Inner (resS5ToS4 S5Char.chiStd) s4Chi22 = 0 ∧
    s4Inner (resS5ToS4 S5Char.chiStd) s4Chi211 = 0 := by
  decide

/-- Conjugacy class sizes of $S_3$ in order $(1^3), (2\cdot 1), (3)$. -/
def s3ClassSize : Fin 3 → ℤ := ![1, 3, 2]

/-- Inclusion of $S_3 = \mathrm{Stab}_{S_4}(3)$ conjugacy classes into $S_4$. -/
def s3ToS4Class : Fin 3 → Fin 5 := ![0, 1, 3]

/-- Class-weighted character inner product $6 \langle \chi, \psi \rangle_{S_3}$. -/
def s3Inner (χ ψ : Fin 3 → ℤ) : ℤ :=
  s3ClassSize 0 * χ 0 * ψ 0 + s3ClassSize 1 * χ 1 * ψ 1 + s3ClassSize 2 * χ 2 * ψ 2

def s3ChiTriv : Fin 3 → ℤ := ![1, 1, 1]
def s3ChiSign : Fin 3 → ℤ := ![1, -1, 1]
def s3ChiStd  : Fin 3 → ℤ := ![2, 0, -1]

def resS4ToS3 (χ : Fin 5 → ℤ) : Fin 3 → ℤ := fun c => χ (s3ToS4Class c)

/-- Orthonormality of the 3 irreducible characters of $S_3$ ($|S_3| = 6$). -/
theorem s3_charTable_orthonormal :
    s3Inner s3ChiTriv s3ChiTriv = 6 ∧ s3Inner s3ChiSign s3ChiSign = 6 ∧
    s3Inner s3ChiStd s3ChiStd = 6 ∧ s3Inner s3ChiTriv s3ChiSign = 0 ∧
    s3Inner s3ChiTriv s3ChiStd = 0 ∧ s3Inner s3ChiSign s3ChiStd = 0 := by
  decide

/-- **Exact $S_4 \downarrow S_3$ branching of the 3D generation candidate $V_{(3,1)}$**:
    $\mathrm{Res}^{S_4}_{S_3} V_{(3,1)} = V_{(2,1)} \oplus V_{(3)}$ ($3 \to 2 \oplus 1$),
    yielding $\mathrm{Res}^{S_5}_{S_3} V_{(4,1)} = V_{(2,1)} \oplus 2\,V_{(3)}$ ($4 \to 2 \oplus 1 \oplus 1$). -/
theorem bring_s4std_and_h0_branch_s3 :
    (∀ c : Fin 3, resS4ToS3 s4ChiStd c = s3ChiStd c + s3ChiTriv c) ∧
    s3Inner (resS4ToS3 s4ChiStd) s3ChiStd = 6 ∧
    s3Inner (resS4ToS3 s4ChiStd) s3ChiTriv = 6 ∧
    s3Inner (resS4ToS3 s4ChiStd) s3ChiSign = 0 ∧
    (∀ c : Fin 3, resS4ToS3 (resS5ToS4 S5Char.chiStd) c = s3ChiStd c + 2 * s3ChiTriv c) := by
  decide

/-- Conjugacy class sizes of $S_3 \times S_2 \subset S_5$ in order
    $(1^3,1^2), (2\cdot 1, 1^2), (3, 1^2), (1^3, 2), (2\cdot 1, 2), (3, 2)$. -/
def s3xS2ClassSize : Fin 6 → ℤ := ![1, 3, 2, 1, 3, 2]

/-- Inclusion of $S_3 \times S_2$ conjugacy classes into $S_5$ (`1⁵, 2·1³, 2²·1, 3·1², 3·2, 4·1, 5`). -/
def s3xS2ToS5Class : Fin 6 → Fin 7 := ![0, 1, 3, 1, 2, 4]

/-- Class-weighted character inner product $12 \langle \chi, \psi \rangle_{S_3 \times S_2}$. -/
def s3xS2Inner (χ ψ : Fin 6 → ℤ) : ℤ :=
  s3xS2ClassSize 0 * χ 0 * ψ 0 + s3xS2ClassSize 1 * χ 1 * ψ 1 +
  s3xS2ClassSize 2 * χ 2 * ψ 2 + s3xS2ClassSize 3 * χ 3 * ψ 3 +
  s3xS2ClassSize 4 * χ 4 * ψ 4 + s3xS2ClassSize 5 * χ 5 * ψ 5

def s3xS2Chi1Triv : Fin 6 → ℤ := ![1, 1, 1, 1, 1, 1]
def s3xS2Chi1Sign : Fin 6 → ℤ := ![1, 1, 1, -1, -1, -1]
def s3xS2ChiSign1 : Fin 6 → ℤ := ![1, -1, 1, 1, -1, 1]
def s3xS2ChiSignS : Fin 6 → ℤ := ![1, -1, 1, -1, 1, -1]
def s3xS2Chi2Triv : Fin 6 → ℤ := ![2, 0, -1, 2, 0, -1]
def s3xS2Chi2Sign : Fin 6 → ℤ := ![2, 0, -1, -2, 0, 1]

def resS5ToS3xS2 (χ : Fin 7 → ℤ) : Fin 6 → ℤ := fun c => χ (s3xS2ToS5Class c)

/-- **Exact $S_5 \downarrow S_3 \times S_2$ branching of $V_{(4,1)}$**:
    $\mathrm{Res}^{S_5}_{S_3 \times S_2} V_{(4,1)} = (V_{(2,1)} \boxtimes 1) \oplus (1 \boxtimes 1) \oplus (1 \boxtimes \mathrm{sgn})$
    ($4 \to 2 \oplus 1 \oplus 1'$). -/
theorem bring_h0_canonical_branch_s3xS2 :
    (∀ c : Fin 6, resS5ToS3xS2 S5Char.chiStd c =
      s3xS2Chi2Triv c + s3xS2Chi1Triv c + s3xS2Chi1Sign c) ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2Chi2Triv = 12 ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2Chi1Triv = 12 ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2Chi1Sign = 12 ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2ChiSign1 = 0 ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2ChiSignS = 0 ∧
    s3xS2Inner (resS5ToS3xS2 S5Char.chiStd) s3xS2Chi2Sign = 0 := by
  decide

/-! ### Concrete Module-Level Idempotents on $V_{\mathrm{std}} \subset F^5$ over Generic `[Field F]` -/

/-- Left permutation action of $S_5 = \mathrm{Perm}(\mathrm{Fin}\ 5)$ on $F^5$:
    $(\sigma \cdot x)_i = x_{\sigma^{-1}(i)}$. -/
def permAct {F : Type*} (σ : Equiv.Perm (Fin 5)) (x : Fin 5 → F) : Fin 5 → F :=
  fun i => x (σ⁻¹ i)

@[simp] theorem permAct_one {F : Type*} (x : Fin 5 → F) :
    permAct 1 x = x := by
  ext i
  simp [permAct]

theorem permAct_mul {F : Type*} (σ τ : Equiv.Perm (Fin 5)) (x : Fin 5 → F) :
    permAct (σ * τ) x = permAct σ (permAct τ x) := by
  ext i
  simp [permAct, _root_.mul_inv_rev]

/-- Membership in Bring's 4D standard differential hyperplane $V_{\mathrm{std}} = \{\sum_{i=0}^4 x_i = 0\}$. -/
def inBringStd {R : Type*} [AddCommMonoid R] (x : Fin 5 → R) : Prop :=
  ∑ i : Fin 5, x i = 0

/-- $V_{\mathrm{std}}$ is $S_5$-invariant over any commutative additive monoid. -/
theorem inBringStd_permAct {R : Type*} [AddCommMonoid R]
    (σ : Equiv.Perm (Fin 5)) {x : Fin 5 → R} (hx : inBringStd x) :
    inBringStd (permAct σ x) := by
  unfold inBringStd permAct at *
  rw [Equiv.sum_comp σ⁻¹ x]
  exact hx

/-- The $S_4$-invariant vector $(1, 1, 1, 1, -4) \in V_{\mathrm{std}}$. -/
def singletVec4 {R : Type*} [CommRing R] (i : Fin 5) : R :=
  if i = 4 then -4 else 1

theorem inBringStd_singletVec4 {R : Type*} [CommRing R] :
    inBringStd (singletVec4 : Fin 5 → R) := by
  unfold inBringStd singletVec4
  rw [Fin.sum_univ_five]
  simp only [ite_true, ite_false, Fin.reduceEq]
  ring

/-- Every $\sigma \in \mathrm{Stab}_{S_5}(4) \cong S_4$ fixes `singletVec4`. -/
theorem permAct_singletVec4_of_fix4 {R : Type*} [CommRing R]
    {σ : Equiv.Perm (Fin 5)} (hσ : σ 4 = 4) :
    permAct σ (singletVec4 : Fin 5 → R) = singletVec4 := by
  have hinv4 : σ⁻¹ 4 = 4 := σ.injective (by simp [hσ])
  ext i
  by_cases hi : i = 4
  · subst hi; simp [permAct, singletVec4, hinv4]
  · have hji : σ⁻¹ i ≠ 4 := fun h => hi (by simpa [hσ] using congrArg σ h)
    have hji' : σ.symm i ≠ 4 := hji
    simp [permAct, singletVec4, hi, hji, hji']

/-- 1D $S_4$-singlet projector $P_{\mathrm{sing}}(x) = -\frac{x_4}{4}\,(1,1,1,1,-4)$. -/
def projSing1 {F : Type*} [Field F] (x : Fin 5 → F) : Fin 5 → F :=
  fun i => -(x 4 / 4) * singletVec4 i

/-- Complementary 3D $S_4$-standard projector $P_{\mathrm{gen},3}(x) = x - P_{\mathrm{sing}}(x)$. -/
def projGen3 {F : Type*} [Field F] (x : Fin 5 → F) : Fin 5 → F :=
  fun i => x i - projSing1 x i

theorem projGen3_add_projSing1 {F : Type*} [Field F] (x : Fin 5 → F) :
    projGen3 x + projSing1 x = x := by
  ext i
  simp [projGen3]

/-- Exact orthogonal idempotent algebra for `projSing1` and `projGen3` over any `[Field F]`
    with `(4 : F) ≠ 0`, landing in the 3D hyperplane $\{y_0 + y_1 + y_2 + y_3 = 0,\; y_4 = 0\}$. -/
theorem projGen3_projSing1_idempotent_split {F : Type*} [Field F]
    (h4 : (4 : F) ≠ 0) (x : Fin 5 → F) :
    projSing1 (projSing1 x) = projSing1 x ∧
    projGen3 (projGen3 x) = projGen3 x ∧
    projSing1 (projGen3 x) = 0 ∧
    projGen3 (projSing1 x) = 0 ∧
    projGen3 x 4 = 0 ∧
    (inBringStd x →
      projGen3 x 0 + projGen3 x 1 + projGen3 x 2 + projGen3 x 3 = 0) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i; by_cases hi : i = 4
    · subst hi; dsimp [projSing1, singletVec4]; field_simp [h4]; try ring
    · dsimp [projSing1, singletVec4]; rw [if_neg hi]; field_simp [h4]; try ring
  · ext i; by_cases hi : i = 4
    · subst hi; dsimp [projGen3, projSing1, singletVec4]; field_simp [h4]; try ring
    · dsimp [projGen3, projSing1, singletVec4]; rw [if_neg hi]; field_simp [h4]; try ring
  · ext i; by_cases hi : i = 4
    · subst hi; change projSing1 (projGen3 x) 4 = 0
      dsimp [projGen3, projSing1, singletVec4]; field_simp [h4]; try ring
    · change projSing1 (projGen3 x) i = 0
      dsimp [projGen3, projSing1, singletVec4]; rw [if_neg hi]; field_simp [h4]; try ring
  · ext i; by_cases hi : i = 4
    · subst hi; change projGen3 (projSing1 x) 4 = 0
      dsimp [projGen3, projSing1, singletVec4]; field_simp [h4]; try ring
    · change projGen3 (projSing1 x) i = 0
      dsimp [projGen3, projSing1, singletVec4]; rw [if_neg hi]; field_simp [h4]; try ring
  · dsimp [projGen3, projSing1, singletVec4]; field_simp [h4]; try ring
  · intro hx
    unfold inBringStd at hx
    rw [Fin.sum_univ_five] at hx
    dsimp [projGen3, projSing1, singletVec4]
    field_simp [h4]
    linear_combination 4 * hx

/-- Both `projSing1` and `projGen3` commute with every $\sigma \in \mathrm{Stab}_{S_5}(4) \cong S_4$. -/
theorem projGen3_equivariant_of_fix4 {F : Type*} [Field F]
    {σ : Equiv.Perm (Fin 5)} (hσ : σ 4 = 4) (x : Fin 5 → F) :
    projSing1 (permAct σ x) = permAct σ (projSing1 x) ∧
    projGen3 (permAct σ x) = permAct σ (projGen3 x) := by
  have hinv4 : σ⁻¹ 4 = 4 := σ.injective (by simp [hσ])
  have hsing : projSing1 (permAct σ x) = permAct σ (projSing1 x) := by
    ext i
    have hvec := congrFun (permAct_singletVec4_of_fix4 (R := F) hσ) i
    simp only [projSing1, permAct, hinv4] at hvec ⊢
    rw [hvec]
  refine ⟨hsing, ?_⟩
  ext i
  have hi := congrFun hsing i
  simp only [projGen3, permAct] at hi ⊢
  rw [hi]

/-- Explicit root basis of the 3D $S_4$-standard generation subspace $V_{\mathrm{gen},3}$:
    $b_0 = (1,-1,0,0,0)$, $b_1 = (0,1,-1,0,0)$, $b_2 = (0,0,1,-1,0)$. -/
def genBasis {R : Type*} [CommRing R] (k : Fin 3) (i : Fin 5) : R :=
  match k.val, i.val with
  | 0, 0 => 1
  | 0, 1 => -1
  | 1, 1 => 1
  | 1, 2 => -1
  | 2, 2 => 1
  | 2, 3 => -1
  | _, _ => 0

/-- Linear independence of the 3 generation root vectors over any `CommRing R`. -/
theorem genBasis_linear_independent {R : Type*} [CommRing R] (c : Fin 3 → R)
    (hc : c 0 • (genBasis 0 : Fin 5 → R) +
          c 1 • (genBasis 1 : Fin 5 → R) +
          c 2 • (genBasis 2 : Fin 5 → R) = 0) :
    c = 0 := by
  have h0 := congrFun hc 0
  have h1 := congrFun hc 1
  have h2 := congrFun hc 2
  simp [genBasis] at h0 h1 h2
  ext k
  fin_cases k
  · exact h0
  · change c 1 = 0; linear_combination h0 + h1
  · change c 2 = 0; linear_combination h0 + h1 + h2

/-- Every projected canonical differential $y = P_{\mathrm{gen},3}(x)$ ($x \in V_{\mathrm{std}}$)
    expands uniquely in the 3-element basis `genBasis`. -/
theorem projGen3_eq_genBasis_comb {F : Type*} [Field F] (h4 : (4 : F) ≠ 0)
    {x : Fin 5 → F} (hx : inBringStd x) :
    projGen3 x =
      (projGen3 x 0) • (genBasis 0 : Fin 5 → F) +
      (projGen3 x 0 + projGen3 x 1) • (genBasis 1 : Fin 5 → F) +
      (projGen3 x 0 + projGen3 x 1 + projGen3 x 2) • (genBasis 2 : Fin 5 → F) := by
  have hsplit := projGen3_projSing1_idempotent_split h4 x
  have hsum := hsplit.2.2.2.2.2 hx
  have h4z := hsplit.2.2.2.2.1
  ext i
  fin_cases i
  · simp [genBasis]
  · simp [genBasis]
  · simp [genBasis]; ring
  · simp [genBasis]; linear_combination hsum
  · simp [genBasis, h4z]

/-- Further $S_4 \downarrow S_3$ refinement ($\sigma(3) = 3, \sigma(4) = 4$):
    `demVec3 = (1, 1, 1, -3, 0)` spans the 1D $S_3$-invariant democratic line inside $V_{\mathrm{gen},3}$,
    splitting $3 \to 2 \oplus 1$. -/
def demVec3 {R : Type*} [CommRing R] (i : Fin 5) : R :=
  if i = 4 then 0 else if i = 3 then -3 else 1

def projDem1 {F : Type*} [Field F] (y : Fin 5 → F) : Fin 5 → F :=
  fun i => -(y 3 / 3) * demVec3 i

def projDoublet2 {F : Type*} [Field F] (y : Fin 5 → F) : Fin 5 → F :=
  fun i => y i - projDem1 y i

theorem projDoublet2_projDem1_split {F : Type*} [Field F] (h3 : (3 : F) ≠ 0)
    (y : Fin 5 → F) (hy4 : y 4 = 0) (hysum : y 0 + y 1 + y 2 + y 3 = 0) :
    projDoublet2 y + projDem1 y = y ∧
    projDem1 (projDem1 y) = projDem1 y ∧
    projDoublet2 (projDoublet2 y) = projDoublet2 y ∧
    projDoublet2 y 0 + projDoublet2 y 1 + projDoublet2 y 2 = 0 ∧
    projDoublet2 y 3 = 0 ∧
    projDoublet2 y 4 = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i; simp [projDoublet2]
  · ext i; fin_cases i <;>
      (dsimp [projDem1, demVec3]; field_simp [h3]; try ring)
  · ext i; fin_cases i <;>
      (dsimp [projDoublet2, projDem1, demVec3]; field_simp [h3]; try ring)
  · dsimp [projDoublet2, projDem1, demVec3]
    field_simp [h3]
    linear_combination 3 * hysum
  · dsimp [projDoublet2, projDem1, demVec3]
    field_simp [h3]
    try ring
  · dsimp [projDoublet2, projDem1, demVec3]
    rw [hy4]
    ring

/-! ### Morgan–Voyce Harmonic Factorisation vs Coprimality & Honest Four-Filter Disagreement -/

/-- Morgan–Voyce continuant $b_n(h)$ governing $\sigma_0^n = b_{n-1}(h)\mathbf{1} + b_n(h)\sigma_0$
    in $H_2(q)$ ($h = q - q^{-1}$). -/
def morganVoyceB {R : Type*} [CommRing R] (h : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | n + 2 => h * morganVoyceB h (n + 1) + morganVoyceB h n

/-- Exact harmonic factorisation $b_9(h) = b_3(h)(h^6 + 6h^4 + 9h^2 + 1)$ alongside the exact
    Bézout coprimality identities $b_3(h)(h^2 + 2) - b_5(h) = 1$ and
    $b_3(h)(h^4 + 4h^2 + 2) - b_7(h) = 1$ over any `CommRing R`. -/
theorem morganVoyceB_nine_harmonic_and_bezout {R : Type*} [CommRing R] (h : R) :
    morganVoyceB h 3 = h ^ 2 + 1 ∧
    morganVoyceB h 9 = morganVoyceB h 3 * (h ^ 6 + 6 * h ^ 4 + 9 * h ^ 2 + 1) ∧
    morganVoyceB h 3 * (h ^ 2 + 2) - morganVoyceB h 5 = 1 ∧
    morganVoyceB h 3 * (h ^ 4 + 4 * h ^ 2 + 2) - morganVoyceB h 7 = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [morganVoyceB] <;> ring

/-- Candidate 1 (`Seifert genus ≤ 4` on odd $T(2,n)$, $n \ge 3$). -/
def seifertGenusLe4Set : Finset ℕ :=
  (Finset.Icc 3 11).filter (fun n => n % 2 = 1 ∧ (n - 1) / 2 ≤ 4)

/-- Candidate 2 (primitive / non-composite odd windings in `seifertGenusLe4Set`). -/
def primitiveWindingSet : Finset ℕ :=
  seifertGenusLe4Set.filter (fun n => ¬ ∃ a ∈ seifertGenusLe4Set, a < n ∧ a ∣ n)

/-- Candidate 3 ($S_5$-equivariant odd orders $\ge 3$: divides $60 = \mathrm{lcm}(1..5)$ and $\ne 15$). -/
def s5EquivariantOddOrderSet : Finset ℕ :=
  seifertGenusLe4Set.filter (fun n => 60 % n = 0 ∧ n ≠ 15)

/-- **Honest Non-Claim Theorem (`docs/audits/2026-10-10-generation-count-two-independent-countings.md`)**:
    The three torus-knot admissibility filters on Bring's genus-$4$ surface return pairwise
    disjoint counts $4$, $3$, and $2$ (`{3,5,7,9}`, `{3,5,7}`, `{3,5}`), so $N_{\mathrm{gen}} = 3$
    is **not** unconditionally forced without an additional physical selection input. -/
theorem bring_generation_filters_disagree :
    seifertGenusLe4Set = {3, 5, 7, 9} ∧
    primitiveWindingSet = {3, 5, 7} ∧
    s5EquivariantOddOrderSet = {3, 5} ∧
    seifertGenusLe4Set.card = 4 ∧
    primitiveWindingSet.card = 3 ∧
    s5EquivariantOddOrderSet.card = 2 := by
  decide

/-- **Rule-13a Conditional Conjecture Carrier (Zero Instances)**:
    Isolates the open physical selection hypothesis on Bring's canonical differential module
    $H^0(\mathcal{B}, K_{\mathcal{B}})$: an equivariant chiral/spin-structure projection whose
    kernel is the 1D $S_4$-singlet line (`finrank = 1`) inside the 4D canonical differential
    space (`finrank = 4`). Deliberately uninstantiated per owner ruling 2026-10-10. -/
class BringChiralGenerationSelectionHypothesis (F : Type*) [Field F]
    (H0Canonical : Type*) [AddCommGroup H0Canonical] [Module F H0Canonical]
    [FiniteDimensional F H0Canonical] where
  chiralProj : H0Canonical →ₗ[F] H0Canonical
  finrank_canonical_eq_four : Module.finrank F H0Canonical = 4
  finrank_singlet_ker_eq_one : Module.finrank F (LinearMap.ker chiralProj) = 1

/-- **Conditional Generation Multiplicity Theorem**:
    Under `BringChiralGenerationSelectionHypothesis`, rank-nullity on $H^0(\mathcal{B}, K_{\mathcal{B}})$
    forces the surviving chiral generation subspace to have dimension $4 - 1 = 3$. -/
theorem chiral_generation_finrank_eq_three_of_selection
    {F : Type*} [Field F] {H0Canonical : Type*} [AddCommGroup H0Canonical]
    [Module F H0Canonical] [FiniteDimensional F H0Canonical]
    [ctx : BringChiralGenerationSelectionHypothesis F H0Canonical] :
    Module.finrank F (LinearMap.range ctx.chiralProj) = 3 := by
  have h := LinearMap.finrank_range_add_finrank_ker ctx.chiralProj
  rw [ctx.finrank_canonical_eq_four, ctx.finrank_singlet_ker_eq_one] at h
  omega

end BringCanonicalBranching

-- ============================================================================
-- §2. S_3 ⊂ S_5 Democratic/Tribimaximal Basis, Cabibbo Perturbation, & Jarlskog CP
-- ============================================================================

section S3YukawaAndCKMAlgebra

/-- $3 \times 3$ rank-1 $S_3$-invariant democratic Yukawa matrix $D_3$ (all entries $1$). -/
def democraticMat3 (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of fun _ _ => 1

/-- Integer tribimaximal (Harrison–Perkins–Scott) eigenbasis matrix $M_{\mathrm{TBM}}$
    whose columns span the $S_3$ doublet $(2,-1,-1)^T, (0,-1,1)^T$ and singlet $(1,1,1)^T$. -/
def tbmIntMat (R : Type*) [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  !![2, 1, 0; -1, 1, -1; -1, 1, 1]

/-- Exact properties of $D_3$ and $M_{\mathrm{TBM}}$ over any `CommRing R`:
    $D_3^2 = 3 D_3$, $\mathrm{tr}(D_3) = 3$, $M_{\mathrm{TBM}}^T M_{\mathrm{TBM}} = \mathrm{diag}(6,3,2)$,
    and $M_{\mathrm{TBM}}^T D_3 M_{\mathrm{TBM}} = \mathrm{diag}(0,9,0)$ (two massless doublet modes,
    one heavy singlet mode). -/
theorem democraticMat3_and_tbmIntMat_identities {R : Type*} [CommRing R] :
    democraticMat3 R * democraticMat3 R = (3 : R) • democraticMat3 R ∧
    Matrix.trace (democraticMat3 R) = 3 ∧
    (tbmIntMat R)ᵀ * tbmIntMat R = Matrix.diagonal ![6, 3, 2] ∧
    (tbmIntMat R)ᵀ * democraticMat3 R * tbmIntMat R = Matrix.diagonal ![0, 9, 0] := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> simp [democraticMat3, Matrix.mul_apply]
  · simp [democraticMat3, Matrix.trace]; try ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [tbmIntMat, Matrix.mul_apply, Matrix.diagonal, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [tbmIntMat, democraticMat3, Matrix.mul_apply, Matrix.diagonal, Fin.sum_univ_three] <;> ring

/-- Normalized tribimaximal orthogonal matrix $U_{\mathrm{TBM}}(s_2, s_3)$ over any `[Field F]`
    equipped with square roots $s_2^2 = 2$ and $s_3^2 = 3$. -/
def tbmUnitary {F : Type*} [Field F] (s2 s3 : F) : Matrix (Fin 3) (Fin 3) F :=
  (s2 * s3)⁻¹ • !![2, s2, 0; -1, s2, -s3; -1, s2, s3]

/-- Exact orthogonality $U_{\mathrm{TBM}}^T U_{\mathrm{TBM}} = I_3 = U_{\mathrm{TBM}} U_{\mathrm{TBM}}^T$
    and parameter-free rational squared mixing weights $(\frac{1}{3}, \frac{1}{2}, 0)$. -/
theorem tbmUnitary_orthogonal_and_weights {F : Type*} [Field F]
    (h2 : (2 : F) ≠ 0) (h3 : (3 : F) ≠ 0) {s2 s3 : F}
    (hs2 : s2 ^ 2 = 2) (hs3 : s3 ^ 2 = 3) :
    (tbmUnitary s2 s3)ᵀ * tbmUnitary s2 s3 = 1 ∧
    tbmUnitary s2 s3 * (tbmUnitary s2 s3)ᵀ = 1 ∧
    (tbmUnitary s2 s3 0 1) ^ 2 = 1 / 3 ∧
    (tbmUnitary s2 s3 1 2) ^ 2 = 1 / 2 ∧
    (tbmUnitary s2 s3 0 2) ^ 2 = 0 := by
  have hs2nz : s2 ≠ 0 := fun h => h2 (by rw [← hs2, h]; ring)
  have hs3nz : s3 ≠ 0 := fun h => h3 (by rw [← hs3, h]; ring)
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [tbmUnitary, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try field_simp [hs2nz, hs3nz]) <;>
      (try rw [hs2]) <;> (try rw [hs3]) <;> (try ring)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [tbmUnitary, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try field_simp [hs2nz, hs3nz]) <;>
      (try rw [hs2]) <;> (try rw [hs3]) <;> (try ring)
  · simp [tbmUnitary]; field_simp [hs2nz, hs3nz, h3]; rw [hs3]
  · simp [tbmUnitary]; field_simp [hs2nz, hs3nz, h2]; rw [hs2]
  · simp [tbmUnitary]

/-- Hecke skein defect $h = q - q^{-1}$ and symmetric quantum integer $[3]_q = q^2 + 1 + q^{-2}$. -/
def heckeDefect {F : Type*} [Field F] (q : F) : F := q - q⁻¹
def qTwoSym {F : Type*} [Field F] (q : F) : F := q + q⁻¹
def qThreeSym {F : Type*} [Field F] (q : F) : F := q ^ 2 + 1 + (q ^ 2)⁻¹

theorem qThreeSym_eq_heckeDefect_sq_add_three {F : Type*} [Field F] {q : F} (hq : q ≠ 0) :
    qThreeSym q = (heckeDefect q) ^ 2 + 3 ∧ (qTwoSym q) ^ 2 = qThreeSym q + 1 := by
  refine ⟨?_, ?_⟩ <;>
    (dsimp [qThreeSym, heckeDefect, qTwoSym]; field_simp [hq]; ring)

/-- Hoefsmit orthogonal $(2,1)$ doublet generators $T_1, T_2 \in M_2(F)$ of $H_3(q)$ and
    the $T_1 \leftrightarrow T_2$ crossing rotation $R_H$. -/
def hoefsmitT1 {F : Type*} [Field F] (q : F) : Matrix (Fin 2) (Fin 2) F :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => q
    | 1, 1 => -q⁻¹
    | _, _ => 0

def hoefsmitM2 {F : Type*} [Field F] (q s3q : F) : Matrix (Fin 2) (Fin 2) F :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => -(q ^ 2)⁻¹
    | 0, 1 => s3q
    | 1, 0 => s3q
    | _, _ => q ^ 2

def hoefsmitT2 {F : Type*} [Field F] (q s3q : F) : Matrix (Fin 2) (Fin 2) F :=
  (qTwoSym q)⁻¹ • hoefsmitM2 q s3q

def hoefsmitRotCore {F : Type*} [Field F] (s3q : F) : Matrix (Fin 2) (Fin 2) F :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => 1
    | 0, 1 => -s3q
    | 1, 0 => s3q
    | _, _ => 1

def hoefsmitRot {F : Type*} [Field F] (q s3q : F) : Matrix (Fin 2) (Fin 2) F :=
  (qTwoSym q)⁻¹ • hoefsmitRotCore s3q

/-- Exact $H_3(q)$ quadratic laws, $B_3$ braid relation $T_1 T_2 T_1 = T_2 T_1 T_2$, and
    orthogonal intertwining $T_2 = R_H T_1 R_H^T$ with squared angle $\cos^2\theta_H = 1/[2]_q^2$. -/
theorem hoefsmitH3_braid_and_crossing_angle {F : Type*} [Field F] {q s3q : F}
    (hq : q ≠ 0) (hq2 : qTwoSym q ≠ 0) (hs3 : s3q ^ 2 = qThreeSym q) :
    (hoefsmitRot q s3q)ᵀ * hoefsmitRot q s3q = 1 ∧
    hoefsmitT1 q * hoefsmitT1 q = heckeDefect q • hoefsmitT1 q + 1 ∧
    hoefsmitT1 q * hoefsmitT2 q s3q * hoefsmitT1 q =
      hoefsmitT2 q s3q * hoefsmitT1 q * hoefsmitT2 q s3q ∧
    hoefsmitRot q s3q * hoefsmitT1 q * (hoefsmitRot q s3q)ᵀ = hoefsmitT2 q s3q ∧
    (hoefsmitRot q s3q 0 0) ^ 2 = 1 / (qTwoSym q) ^ 2 ∧
    (hoefsmitRot q s3q 1 0) ^ 2 = qThreeSym q / (qTwoSym q) ^ 2 := by
  have hrel : (qTwoSym q) ^ 2 = s3q ^ 2 + 1 := by
    rw [hs3, (qThreeSym_eq_heckeDefect_sq_add_three hq).2]
  have hcore_orth : (hoefsmitRotCore s3q)ᵀ * hoefsmitRotCore s3q = (qTwoSym q) ^ 2 • 1 := by
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [hoefsmitRotCore, Matrix.mul_apply, Fin.sum_univ_two]; try rw [hrel]; ring)
  have hbraid_core :
      qTwoSym q • (hoefsmitT1 q * hoefsmitM2 q s3q * hoefsmitT1 q) =
        hoefsmitM2 q s3q * hoefsmitT1 q * hoefsmitM2 q s3q := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [hoefsmitT1, hoefsmitM2, qTwoSym, Matrix.mul_apply, Fin.sum_univ_two] <;>
      (try field_simp [hq]) <;> (try rw [hs3]) <;> (try dsimp [qThreeSym]) <;>
      (try field_simp [hq]) <;> (try ring)
  have hintertwine_core :
      hoefsmitRotCore s3q * hoefsmitT1 q * (hoefsmitRotCore s3q)ᵀ =
        qTwoSym q • hoefsmitM2 q s3q := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [hoefsmitRotCore, hoefsmitT1, hoefsmitM2, qTwoSym, Matrix.mul_apply, Fin.sum_univ_two] <;>
      (try field_simp [hq]) <;> (try rw [hs3]) <;> (try dsimp [qThreeSym]) <;>
      (try field_simp [hq]) <;> (try ring)
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · unfold hoefsmitRot
    rw [Matrix.transpose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, hcore_orth, smul_smul]
    have hinv : (qTwoSym q)⁻¹ * (qTwoSym q)⁻¹ * (qTwoSym q) ^ 2 = 1 := by field_simp [hq2]
    rw [hinv, one_smul]
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [hoefsmitT1, heckeDefect, Matrix.mul_apply, Fin.sum_univ_two] <;>
      (try field_simp [hq]) <;> (try ring)
  · unfold hoefsmitT2
    rw [Matrix.mul_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
      smul_smul, ← hbraid_core, smul_smul]
    congr 1; field_simp [hq2]
  · unfold hoefsmitRot hoefsmitT2
    rw [Matrix.transpose_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul, smul_smul,
      hintertwine_core, smul_smul]
    congr 1; field_simp [hq2]
  · simp [hoefsmitRot, hoefsmitRotCore]
  · simp [hoefsmitRot, hoefsmitRotCore]; field_simp [hq2]; rw [hs3]

/-- $2 \times 2$ light-generation Yukawa perturbation block $\begin{pmatrix} 0 & \beta \\ \beta & \alpha \end{pmatrix}$
    and planar orthogonal rotation $R_2(c, s)$. -/
def cabibboBlock {R : Type*} [CommRing R] (α β : R) : Matrix (Fin 2) (Fin 2) R :=
  !![0, β; β, α]

def planarRot2 {R : Type*} [CommRing R] (c s : R) : Matrix (Fin 2) (Fin 2) R :=
  !![c, s; -s, c]

/-- **Exact Cabibbo Leading-Angle Perturbation Theorem**:
    Diagonalizing `cabibboBlock α β` by `planarRot2 c s` ($c^2 + s^2 = 1$) forces
    $(c^2 - s^2)\beta = c s \alpha$ ($\tan 2\theta_{12} = 2\beta/\alpha$) and the radical-free
    identity $(\alpha^2 + 4\beta^2)(2 c s)^2 = 4\beta^2$. -/
theorem cabibboBlock_sin2theta_sq {R : Type*} [CommRing R] {α β c s : R}
    (hunit : c ^ 2 + s ^ 2 = 1) :
    (((planarRot2 c s)ᵀ * cabibboBlock α β * planarRot2 c s) 0 1 = 0 ↔
      (c ^ 2 - s ^ 2) * β = c * s * α) ∧
    ((c ^ 2 - s ^ 2) * β = c * s * α →
      (α ^ 2 + 4 * β ^ 2) * (2 * c * s) ^ 2 = 4 * β ^ 2) := by
  constructor
  · simp only [planarRot2, cabibboBlock, Matrix.mul_apply, Matrix.transpose_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
    constructor <;> intro h <;> linear_combination h
  · intro hdiag
    calc (α ^ 2 + 4 * β ^ 2) * (2 * c * s) ^ 2
        = 4 * (c * s * α) ^ 2 + 16 * c ^ 2 * s ^ 2 * β ^ 2 := by ring
      _ = 4 * ((c ^ 2 - s ^ 2) * β) ^ 2 + 16 * c ^ 2 * s ^ 2 * β ^ 2 := by rw [← hdiag]
      _ = 4 * β ^ 2 * (c ^ 2 + s ^ 2) ^ 2 := by ring
      _ = 4 * β ^ 2 := by rw [hunit]; ring

/-- Specialisation to the Hecke skein defect $\beta = q - q^{-1}$ against the $[3]_q$ heavy scale. -/
theorem cabibbo_hecke_qThree_relation {F : Type*} [Field F] {q c s : F}
    (hunit : c ^ 2 + s ^ 2 = 1)
    (hdiag : (c ^ 2 - s ^ 2) * heckeDefect q = c * s * qThreeSym q) :
    ((qThreeSym q) ^ 2 + 4 * (heckeDefect q) ^ 2) * (2 * c * s) ^ 2 =
      4 * (heckeDefect q) ^ 2 :=
  (cabibboBlock_sin2theta_sq hunit).2 hdiag

/-! ### Generic Gaussian Extension `QuadI R` ($R[i]$) and $3 \times 3$ Unitary Jarlskog Algebra -/

/-- Formal Gaussian extension $R[i] = R \oplus i R$ over any `CommRing R` (§7c: avoids `ℂ`/`ℝ`). -/
@[ext]
structure QuadI (R : Type*) where
  re : R
  im : R
  deriving DecidableEq

namespace QuadI

variable {R : Type*} [CommRing R]

/-- Canonical embedding $R \hookrightarrow R[i]$. -/
def ofReal (x : R) : QuadI R := ⟨x, 0⟩

/-- Complex conjugation $(a + b i)^* = a - b i$. -/
def conj (z : QuadI R) : QuadI R := ⟨z.re, -z.im⟩

/-- Squared modulus $|a + b i|^2 = a^2 + b^2 \in R$. -/
def normSq (z : QuadI R) : R := z.re ^ 2 + z.im ^ 2

instance : Zero (QuadI R) := ⟨⟨0, 0⟩⟩
instance : One (QuadI R) := ⟨⟨1, 0⟩⟩
instance : Add (QuadI R) := ⟨fun z w => ⟨z.re + w.re, z.im + w.im⟩⟩
instance : Neg (QuadI R) := ⟨fun z => ⟨-z.re, -z.im⟩⟩
instance : Sub (QuadI R) := ⟨fun z w => ⟨z.re - w.re, z.im - w.im⟩⟩
instance : Mul (QuadI R) := ⟨fun z w => ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩⟩
instance : NatCast (QuadI R) := ⟨fun n => ⟨n, 0⟩⟩
instance : IntCast (QuadI R) := ⟨fun n => ⟨n, 0⟩⟩

@[simp] theorem zero_re : (0 : QuadI R).re = 0 := rfl
@[simp] theorem zero_im : (0 : QuadI R).im = 0 := rfl
@[simp] theorem one_re : (1 : QuadI R).re = 1 := rfl
@[simp] theorem one_im : (1 : QuadI R).im = 0 := rfl
@[simp] theorem add_re (z w : QuadI R) : (z + w).re = z.re + w.re := rfl
@[simp] theorem add_im (z w : QuadI R) : (z + w).im = z.im + w.im := rfl
@[simp] theorem neg_re (z : QuadI R) : (-z).re = -z.re := rfl
@[simp] theorem neg_im (z : QuadI R) : (-z).im = -z.im := rfl
@[simp] theorem sub_re (z w : QuadI R) : (z - w).re = z.re - w.re := rfl
@[simp] theorem sub_im (z w : QuadI R) : (z - w).im = z.im - w.im := rfl
@[simp] theorem mul_re (z w : QuadI R) : (z * w).re = z.re * w.re - z.im * w.im := rfl
@[simp] theorem mul_im (z w : QuadI R) : (z * w).im = z.re * w.im + z.im * w.re := rfl
@[simp] theorem natCast_re (n : ℕ) : (n : QuadI R).re = n := rfl
@[simp] theorem natCast_im (n : ℕ) : (n : QuadI R).im = 0 := rfl
@[simp] theorem intCast_re (n : ℤ) : (n : QuadI R).re = n := rfl
@[simp] theorem intCast_im (n : ℤ) : (n : QuadI R).im = 0 := rfl
@[simp] theorem conj_re (z : QuadI R) : (conj z).re = z.re := rfl
@[simp] theorem conj_im (z : QuadI R) : (conj z).im = -z.im := rfl

instance : CommRing (QuadI R) where
  add_assoc a b c := by ext <;> simp <;> ring
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  nsmul := nsmulRec
  zsmul := zsmulRec
  neg_add_cancel a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  sub_eq_add_neg a b := by ext <;> simp [sub_eq_add_neg]
  mul_assoc a b c := by ext <;> simp <;> ring
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp
  mul_comm a b := by ext <;> simp <;> ring
  natCast := Nat.cast
  natCast_zero := by ext <;> simp
  natCast_succ n := by ext <;> simp
  intCast := Int.cast
  intCast_ofNat n := by ext <;> simp
  intCast_negSucc n := QuadI.ext (by simp [Int.negSucc_eq]) (by simp [Int.negSucc_eq])

theorem mul_conj (z : QuadI R) : z * conj z = ofReal (normSq z) :=
  QuadI.ext (by simp [ofReal, normSq]; ring) (by simp [ofReal, normSq]; ring)

theorem conj_mul (z w : QuadI R) : conj (z * w) = conj z * conj w :=
  QuadI.ext (by simp) (by simp; ring)

theorem conj_sum {ι : Type*} (s : Finset ι) (f : ι → QuadI R) :
    conj (∑ x ∈ s, f x) = ∑ x ∈ s, conj (f x) := by
  classical
  induction s using Finset.induction_on with
  | empty => exact QuadI.ext (by simp) (by simp)
  | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.sum_insert ha]
      exact QuadI.ext (by simp [← ih]) (by simp [← ih]; ring)

end QuadI

/-- Conjugate transpose $M^\dagger$ of a matrix over `QuadI R`. -/
def dagger {m n R : Type*} [CommRing R] (M : Matrix m n (QuadI R)) : Matrix n m (QuadI R) :=
  Matrix.of fun i j => QuadI.conj (M j i)

/-- Two-sided $3 \times 3$ unitarity over `QuadI R`. -/
def IsUnitary3 {R : Type*} [CommRing R] (V : Matrix (Fin 3) (Fin 3) (QuadI R)) : Prop :=
  dagger V * V = 1 ∧ V * dagger V = 1

theorem dagger_dagger {m n R : Type*} [CommRing R] (M : Matrix m n (QuadI R)) :
    dagger (dagger M) = M := by
  refine Matrix.ext fun i j => QuadI.ext ?_ ?_ <;> simp [dagger]

theorem dagger_mul {l m n R : Type*} [Fintype m] [CommRing R]
    (A : Matrix l m (QuadI R)) (B : Matrix m n (QuadI R)) :
    dagger (A * B) = dagger B * dagger A := by
  refine Matrix.ext fun i j => ?_
  simp only [dagger, Matrix.mul_apply, Matrix.of_apply, QuadI.conj_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [QuadI.conj_mul, mul_comm]

/-- **CKM/PMNS Overlap Unitarity**: If $U_u$ and $U_d$ are $3 \times 3$ unitary flavour-basis
    transformations, their overlap $V = U_u^\dagger U_d$ is unitary. -/
theorem isUnitary3_overlap {R : Type*} [CommRing R]
    {Uu Ud : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hu : IsUnitary3 Uu) (hd : IsUnitary3 Ud) :
    IsUnitary3 (dagger Uu * Ud) := by
  constructor
  · rw [dagger_mul, dagger_dagger, ← Matrix.mul_assoc, Matrix.mul_assoc (dagger Ud), hu.2,
      Matrix.mul_one, hd.1]
  · rw [dagger_mul, dagger_dagger, ← Matrix.mul_assoc, Matrix.mul_assoc (dagger Uu), hd.2,
      Matrix.mul_one, hu.1]

/-- **Jarlskog CP-Violation Invariant** $J(V) = \mathrm{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*)$. -/
def jarlskog {R : Type*} [CommRing R] (V : Matrix (Fin 3) (Fin 3) (QuadI R)) : R :=
  (V 0 1 * V 1 2 * QuadI.conj (V 0 2) * QuadI.conj (V 1 1)).im

/-- Quark/lepton diagonal phase redefinition $V'_{jk} = \alpha_j V_{jk} \beta_k^*$. -/
def rephaseMat {R : Type*} [CommRing R] (α β : Fin 3 → QuadI R)
    (V : Matrix (Fin 3) (Fin 3) (QuadI R)) : Matrix (Fin 3) (Fin 3) (QuadI R) :=
  Matrix.of fun j k => α j * V j k * QuadI.conj (β k)

/-- **Rephasing Invariance of $J(V)$**: Independent of all 6 field phases when $|\alpha_j|^2 = |\beta_k|^2 = 1$. -/
theorem jarlskog_rephase_invariant {R : Type*} [CommRing R]
    (α β : Fin 3 → QuadI R)
    (hα : ∀ i, QuadI.normSq (α i) = 1) (hβ : ∀ j, QuadI.normSq (β j) = 1)
    (V : Matrix (Fin 3) (Fin 3) (QuadI R)) :
    jarlskog (rephaseMat α β V) = jarlskog V := by
  have hcc : ∀ z : QuadI R, QuadI.conj (QuadI.conj z) = z := fun z => by ext <;> simp
  have calc_rephase :
      rephaseMat α β V 0 1 * rephaseMat α β V 1 2 *
        QuadI.conj (rephaseMat α β V 0 2) * QuadI.conj (rephaseMat α β V 1 1) =
      (α 0 * QuadI.conj (α 0)) * (α 1 * QuadI.conj (α 1)) *
        (β 1 * QuadI.conj (β 1)) * (β 2 * QuadI.conj (β 2)) *
        (V 0 1 * V 1 2 * QuadI.conj (V 0 2) * QuadI.conj (V 1 1)) := by
    simp only [rephaseMat, Matrix.of_apply, QuadI.conj_mul, hcc]
    ring
  unfold jarlskog
  rw [calc_rephase, QuadI.mul_conj, QuadI.mul_conj, QuadI.mul_conj, QuadI.mul_conj,
    hα 0, hα 1, hβ 1, hβ 2]
  have h1 : QuadI.ofReal (1 : R) = 1 := rfl
  rw [h1, one_mul, one_mul, one_mul, one_mul]

/-- **Universal Unitary Plaquette Antisymmetry**: Row orthogonality
    $\sum_{k=0}^2 V_{0k} V_{1k}^* = 0$ forces $J_{us,cb}(V) = -J_{ud,cb}(V)$. -/
theorem jarlskog_plaquette_antisymm {R : Type*} [CommRing R]
    {V : Matrix (Fin 3) (Fin 3) (QuadI R)} (hu : IsUnitary3 V) :
    jarlskog V = -(V 0 0 * V 1 2 * QuadI.conj (V 0 2) * QuadI.conj (V 1 0)).im := by
  have horth : (V * dagger V) 0 1 = 0 := by rw [hu.2]; rfl
  simp only [Matrix.mul_apply, dagger, Matrix.of_apply, Fin.sum_univ_three] at horth
  have hmul := congrArg (fun z => z * (V 1 2 * QuadI.conj (V 0 2))) horth
  have him := congrArg QuadI.im hmul
  simp only [add_mul, zero_mul, QuadI.add_im, QuadI.zero_im] at him
  have hreal :
      (V 0 2 * QuadI.conj (V 1 2) * (V 1 2 * QuadI.conj (V 0 2))).im = 0 := by
    have h_rearrange :
        V 0 2 * QuadI.conj (V 1 2) * (V 1 2 * QuadI.conj (V 0 2)) =
        (V 0 2 * QuadI.conj (V 0 2)) * (V 1 2 * QuadI.conj (V 1 2)) := by ring
    rw [h_rearrange, QuadI.mul_conj, QuadI.mul_conj]
    simp [QuadI.ofReal]
  unfold jarlskog
  have hcomm1 :
      V 0 1 * QuadI.conj (V 1 1) * (V 1 2 * QuadI.conj (V 0 2)) =
      V 0 1 * V 1 2 * QuadI.conj (V 0 2) * QuadI.conj (V 1 1) := by ring
  have hcomm0 :
      V 0 0 * QuadI.conj (V 1 0) * (V 1 2 * QuadI.conj (V 0 2)) =
      V 0 0 * V 1 2 * QuadI.conj (V 0 2) * QuadI.conj (V 1 0) := by ring
  rw [hcomm0, hcomm1, hreal, add_zero] at him
  linear_combination him

/-- Braid-mirror / CP conjugation $V \mapsto V^*$ negates $J(V)$, and any real mixing matrix has $J = 0$. -/
theorem jarlskog_conj_and_real_vanish {R : Type*} [CommRing R]
    (V : Matrix (Fin 3) (Fin 3) (QuadI R)) :
    jarlskog (Matrix.of fun i j => QuadI.conj (V i j)) = -jarlskog V ∧
    ((∀ i j, (V i j).im = 0) → jarlskog V = 0) := by
  constructor
  · unfold jarlskog
    simp [QuadI.conj]
    ring
  · intro hre
    unfold jarlskog
    simp [hre]

/-- Standard Chau–Keung mixing parameters over a generic `CommRing R`. -/
structure ChauKeungParams (R : Type*) [CommRing R] where
  c12 : R
  s12 : R
  c23 : R
  s23 : R
  c13 : R
  s13 : R
  cδ  : R
  sδ  : R
  unit12 : c12 ^ 2 + s12 ^ 2 = 1
  unit23 : c23 ^ 2 + s23 ^ 2 = 1
  unit13 : c13 ^ 2 + s13 ^ 2 = 1
  unitδ  : cδ ^ 2 + sδ ^ 2 = 1

/-- Constructive existence witness for `ChauKeungParams R` (identity angles). -/
def ChauKeungParams.ofIdentity (R : Type*) [CommRing R] : ChauKeungParams R where
  c12 := 1; s12 := 0; c23 := 1; s23 := 0; c13 := 1; s13 := 0; cδ := 1; sδ := 0
  unit12 := by ring
  unit23 := by ring
  unit13 := by ring
  unitδ  := by ring

/-- Elementary Chau–Keung factor matrices $R_{23}, U_{13}(\delta), R_{12}$ over `QuadI R`. -/
def ckR23 {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    Matrix (Fin 3) (Fin 3) (QuadI R) :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => 1
    | 1, 1 => QuadI.ofReal p.c23
    | 1, 2 => QuadI.ofReal p.s23
    | 2, 1 => QuadI.ofReal (-p.s23)
    | 2, 2 => QuadI.ofReal p.c23
    | _, _ => 0

def ckU13 {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    Matrix (Fin 3) (Fin 3) (QuadI R) :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => QuadI.ofReal p.c13
    | 0, 2 => ⟨p.s13 * p.cδ, -p.s13 * p.sδ⟩
    | 1, 1 => 1
    | 2, 0 => ⟨-p.s13 * p.cδ, -p.s13 * p.sδ⟩
    | 2, 2 => QuadI.ofReal p.c13
    | _, _ => 0

def ckR12 {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    Matrix (Fin 3) (Fin 3) (QuadI R) :=
  Matrix.of fun i j =>
    match i.val, j.val with
    | 0, 0 => QuadI.ofReal p.c12
    | 0, 1 => QuadI.ofReal p.s12
    | 1, 0 => QuadI.ofReal (-p.s12)
    | 1, 1 => QuadI.ofReal p.c12
    | 2, 2 => 1
    | _, _ => 0

/-- Standard PDG Chau–Keung $3 \times 3$ mixing matrix $V = R_{23} U_{13}(\delta) R_{12}$ over `QuadI R`. -/
def chauKeungMat {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    Matrix (Fin 3) (Fin 3) (QuadI R) :=
  ckR23 p * ckU13 p * ckR12 p

theorem ckR23_unitary {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    IsUnitary3 (ckR23 p) := by
  constructor <;>
    (refine Matrix.ext fun i j => ?_; fin_cases i <;> fin_cases j <;>
      refine QuadI.ext ?_ ?_ <;>
      simp [ckR23, dagger, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try linear_combination p.unit23) <;> (try ring))

theorem ckU13_unitary {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    IsUnitary3 (ckU13 p) := by
  have hdiag :
      p.c13 * p.c13 + (p.s13 * p.cδ * (p.s13 * p.cδ) + p.s13 * p.sδ * (p.s13 * p.sδ)) = 1 := by
    calc p.c13 * p.c13 + (p.s13 * p.cδ * (p.s13 * p.cδ) + p.s13 * p.sδ * (p.s13 * p.sδ))
        = p.c13 ^ 2 + p.s13 ^ 2 * (p.cδ ^ 2 + p.sδ ^ 2) := by ring
      _ = 1 := by rw [p.unitδ, mul_one, p.unit13]
  constructor <;>
    (refine Matrix.ext fun i j => ?_; fin_cases i <;> fin_cases j <;>
      refine QuadI.ext ?_ ?_ <;>
      simp [ckU13, dagger, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try linear_combination hdiag) <;> (try ring))

theorem ckR12_unitary {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    IsUnitary3 (ckR12 p) := by
  constructor <;>
    (refine Matrix.ext fun i j => ?_; fin_cases i <;> fin_cases j <;>
      refine QuadI.ext ?_ ?_ <;>
      simp [ckR12, dagger, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three] <;>
      (try linear_combination p.unit12) <;> (try ring))

/-- **Exact Chau–Keung Unitarity and Jarlskog Factorisation Theorem**:
    `chauKeungMat p` is unitary and satisfies $J = c_{12} s_{12} c_{23} s_{23} c_{13}^2 s_{13} s_\delta$. -/
theorem chauKeungMat_unitary_and_jarlskog {R : Type*} [CommRing R] (p : ChauKeungParams R) :
    IsUnitary3 (chauKeungMat p) ∧
    jarlskog (chauKeungMat p) =
      p.c12 * p.s12 * p.c23 * p.s23 * p.c13 ^ 2 * p.s13 * p.sδ := by
  have hr23 := ckR23_unitary p
  have hu13 := ckU13_unitary p
  have hr12 := ckR12_unitary p
  have hu_23_13 : IsUnitary3 (ckR23 p * ckU13 p) := by
    rw [← dagger_dagger (ckR23 p)]
    exact isUnitary3_overlap
      ⟨by rw [dagger_dagger]; exact hr23.2, by rw [dagger_dagger]; exact hr23.1⟩ hu13
  have hu_all : IsUnitary3 (chauKeungMat p) := by
    unfold chauKeungMat
    rw [← dagger_dagger (ckR23 p * ckU13 p)]
    exact isUnitary3_overlap
      ⟨by rw [dagger_dagger]; exact hu_23_13.2, by rw [dagger_dagger]; exact hu_23_13.1⟩ hr12
  refine ⟨hu_all, ?_⟩
  have hv01 : chauKeungMat p 0 1 = ⟨p.s12 * p.c13, 0⟩ :=
    QuadI.ext
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three]; ring)
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three])
  have hv12 : chauKeungMat p 1 2 = ⟨p.s23 * p.c13, 0⟩ :=
    QuadI.ext
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three])
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three])
  have hv02 : chauKeungMat p 0 2 = ⟨p.s13 * p.cδ, -p.s13 * p.sδ⟩ :=
    QuadI.ext
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three])
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three])
  have hv11 : chauKeungMat p 1 1 =
      ⟨p.c12 * p.c23 - p.s12 * p.s23 * p.s13 * p.cδ, -p.s12 * p.s23 * p.s13 * p.sδ⟩ :=
    QuadI.ext
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three]; ring)
      (by simp [chauKeungMat, ckR23, ckU13, ckR12, QuadI.ofReal, Matrix.mul_apply, Fin.sum_univ_three]; ring)
  unfold jarlskog
  rw [hv01, hv12, hv02, hv11]
  simp only [QuadI.conj_re, QuadI.conj_im, QuadI.mul_re, QuadI.mul_im]
  ring

/-- **Integral-Domain Vanishing Criterion for $J$**:
    Over any integral domain `R`, $J(V) = 0$ iff a mixing factor vanishes or the CP phase aligns ($s_\delta = 0$). -/
theorem chauKeungMat_jarlskog_eq_zero_iff {R : Type*} [CommRing R] [IsDomain R]
    (p : ChauKeungParams R) :
    jarlskog (chauKeungMat p) = 0 ↔
      p.c12 = 0 ∨ p.s12 = 0 ∨ p.c23 = 0 ∨ p.s23 = 0 ∨
      p.c13 = 0 ∨ p.s13 = 0 ∨ p.sδ = 0 := by
  rw [(chauKeungMat_unitary_and_jarlskog p).2]
  simp only [mul_eq_zero, sq_eq_zero_iff]
  tauto

end S3YukawaAndCKMAlgebra

-- ============================================================================
-- §3. Seifert–Torres (2,7)-Cabled Figure-Eight Satellite Alexander & Burau Identity
-- ============================================================================

section SatelliteFigureEightTau

/-- Polynomial-framed reduced $B_3$ Burau matrix $\widetilde{C}(t) = t B(\sigma_1 \sigma_2^{-1}) =
    \begin{pmatrix} t - t^2 & -1 \\ t & -1 \end{pmatrix}$ of the chiral clasp $\sigma_1 \sigma_2^{-1}$. -/
def burauClaspScaled {R : Type*} [CommRing R] (t : R) : Matrix (Fin 2) (Fin 2) R :=
  !![t - t ^ 2, -1; t, -1]

/-- Normalized Laurent-free Alexander polynomial $\Delta_{4_1}^{\mathrm{pos}}(t) = -1 + 3t - t^2$
    of the figure-eight knot $4_1 = \widehat{(\sigma_1 \sigma_2^{-1})^2}$ ($\Delta(1) = +1$). -/
def alexanderFigEight {R : Type*} [CommRing R] (t : R) : R :=
  -1 + 3 * t - t ^ 2

/-- **3-Strand Burau Clasp & Figure-Eight Determinant Identity**:
    $\det(\widetilde{C}(t)) = t^2$ and $\det(t^2 I_2 - \widetilde{C}(t)^2) = t^2(1 + t + t^2)\Delta_{4_1}^{\mathrm{pos}}(t)$. -/
theorem burau_figEight_factorisation {R : Type*} [CommRing R] (t : R) :
    (burauClaspScaled t).det = t ^ 2 ∧
    (t ^ 2 • (1 : Matrix (Fin 2) (Fin 2) R) -
      burauClaspScaled t * burauClaspScaled t).det =
      t ^ 2 * (1 + t + t ^ 2) * alexanderFigEight t := by
  constructor
  · simp [burauClaspScaled, Matrix.det_fin_two]
  · simp [burauClaspScaled, alexanderFigEight, Matrix.det_fin_two]
    ring

/-- Seifert–Torres Alexander polynomial of the $(2, 2n+1)$-cabled figure-eight satellite
    $C_{2, 2n+1}(4_1)$: $\Delta_{C_{2, 2n+1}(4_1)}(t) = \Delta_{4_1}^{\mathrm{pos}}(t^2)\,\Delta_{T(2, 2n+1)}(t)$. -/
def alexanderCable2FigEight {R : Type*} [CommRing R] (t : R) (n : ℕ) : R :=
  alexanderFigEight (t ^ 2) * alexanderTorus2 t (2 * n + 1)

/-- **Division-Free Rational Closed Form & Cabled Burau Factorisation**:
    Combines `burau_figEight_factorisation` at $t^2$ with `one_add_mul_alexanderTorus2_odd`
    from `QOU.BraidsAndKnots.QIntegerAlexanderTorus`. -/
theorem cabled_burau_alexander_factorisation {R : Type*} [CommRing R] (t : R) (n : ℕ) :
    (1 + t) * alexanderCable2FigEight t n =
      (-1 + 3 * t ^ 2 - t ^ 4) * (1 + t ^ (2 * n + 1)) ∧
    ((t ^ 4) • (1 : Matrix (Fin 2) (Fin 2) R) -
      burauClaspScaled (t ^ 2) * burauClaspScaled (t ^ 2)).det *
      (1 - (-t) ^ (2 * n + 1)) =
      t ^ 4 * (1 + t ^ 2 + t ^ 4) * (1 + t) * alexanderCable2FigEight t n := by
  have hodd : Odd (2 * n + 1) := ⟨n, by ring⟩
  have htor : (1 + t) * alexanderTorus2 t (2 * n + 1) = 1 + t ^ (2 * n + 1) :=
    one_add_mul_alexanderTorus2_odd t n
  have hbur := (burau_figEight_factorisation (t ^ 2)).2
  have hpow4 : (t ^ 2) ^ 2 = t ^ 4 := by ring
  constructor
  · calc (1 + t) * alexanderCable2FigEight t n
        = alexanderFigEight (t ^ 2) * ((1 + t) * alexanderTorus2 t (2 * n + 1)) := by
            unfold alexanderCable2FigEight; ring
      _ = (-1 + 3 * t ^ 2 - t ^ 4) * (1 + t ^ (2 * n + 1)) := by
            rw [htor]; unfold alexanderFigEight; ring
  · rw [hodd.neg_pow]
    have h1m : (1 : R) - -t ^ (2 * n + 1) = 1 + t ^ (2 * n + 1) := by ring
    rw [h1m, ← htor, ← hpow4, hbur]
    unfold alexanderCable2FigEight
    ring

/-- **Tau Lepton Satellite Specialisation ($n = 3$, $C_{2,7}(4_1)$)**:
    Explicit degree-10 palindromic polynomial expansion, Alexander normalization $\Delta(1) = 1$,
    knot determinant $\Delta(-1) = 7$, and sign-indefiniteness witness across the golden-ratio node
    ($\Delta_{4_1}^{\mathrm{pos}}(1) = +1$, $\Delta_{4_1}^{\mathrm{pos}}(3) = -1$). -/
theorem alexanderCable2FigEight_tau_properties {R : Type*} [CommRing R] (t : R) :
    alexanderCable2FigEight t 3 =
      -1 + t + 2 * t ^ 2 - 2 * t ^ 3 + t ^ 4 - t ^ 5 +
      t ^ 6 - 2 * t ^ 7 + 2 * t ^ 8 + t ^ 9 - t ^ 10 ∧
    alexanderCable2FigEight (1 : R) 3 = 1 ∧
    alexanderCable2FigEight (-1 : R) 3 = 7 ∧
    alexanderFigEight (1 : ℤ) = 1 ∧
    alexanderFigEight (3 : ℤ) = -1 := by
  have hexp :
      ∀ x : R, alexanderCable2FigEight x 3 =
        -1 + x + 2 * x ^ 2 - 2 * x ^ 3 + x ^ 4 - x ^ 5 +
        x ^ 6 - 2 * x ^ 7 + 2 * x ^ 8 + x ^ 9 - x ^ 10 := by
    intro x
    unfold alexanderCable2FigEight alexanderFigEight alexanderTorus2
    simp [Finset.sum_range_succ]
    ring
  refine ⟨hexp t, ?_, ?_, by decide, by decide⟩
  · rw [hexp 1]; ring
  · rw [hexp (-1)]; ring

end SatelliteFigureEightTau

end QOU.StandardModel.BringGenerationSplitAndCKMTexture
