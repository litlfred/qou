import QOU.Brings.BringVandermondeSmoothnessAndGenusThree
import Mathlib.Data.ZMod.Basic
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Projective Fano Plane $\mathbb{P}^2(\mathbb{F}_2)$, Hurwitz Order-168 $\mathrm{GL}(3, \mathbb{F}_2)$, $S_4$ Bridge from Bring's $S_5$, Oriented Fano Octonion Algebra $\mathbb{O}(R)$, and Blichfeldt $\mathrm{SU}(3)$ Embedding

Unconditional Lean 4 formalization of the genus-3 Fano / octonion / colour-$\mathrm{SU}(3)$
structural bridge (`qou-ys29`) building on `QOU.Brings.BringVandermondeSmoothnessAndGenusThree`:

1. **§1 — Projective Fano Plane $\mathbb{P}^2(\mathbb{F}_2)$ & Hurwitz Order-168 Automorphism Group $\mathrm{GL}(3, \mathbb{F}_2)$:**
   - Defines `FanoPoint` (`7` nonzero vectors in $(\mathbb{Z}/2\mathbb{Z})^3$) and `FanoLine`
     (`7` 3-element subsets $\{u, v, u + v\}$ summing to $0$, i.e. 2D $\mathbb{F}_2$-subspaces
     minus $0$).
   - Proves `Fintype.card FanoPoint = 7`, `Fintype.card FanoLine = 7`, and the exact projective
     plane incidence axioms: unique line through every pair of distinct points, unique intersection
     point of every pair of distinct lines, `3` points per line, and `3` lines per point.
   - Proves `Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) = 168` via an explicit
     equivalence with `{M : Matrix (Fin 3) (Fin 3) (ZMod 2) // det3F2 M ≠ 0}` and shows
     `168 = 84 * (3 - 1)` (saturating Hurwitz's $84(g - 1)$ bound at genus $g = 3$).

2. **§2 — Resolving the $S_5 \not\supset \mathrm{PSL}(2,7)$ Obstruction via Common Maximal Subgroup $S_4$ (`qou-ys29`):**
   - Proves `¬ (168 ∣ Nat.factorial 5)` and deduces via Lagrange's theorem that there is no
     injective group homomorphism `Matrix.GeneralLinearGroup (Fin 3) (ZMod 2) →* Equiv.Perm (Fin 5)`.
   - Constructs both the point stabilizer `pointStabilizerSubgroup` of $e_0 = (1, 0, 0)$ and the
     line stabilizer `lineStabilizerSubgroup` of $L_0 = \{v \neq 0 \mid v_2 = 0\}$, proving both
     have exact cardinality `24 = Nat.factorial 4` (`168 = 7 * 24`).
   - Constructs an explicit group isomorphism `lineStabilizerMulEquivPerm4 : lineStabilizerSubgroup ≃* Equiv.Perm (Fin 4)`
     via its faithful affine action on the 4-point complement `FanoPoint \ L_0`, together with the
     canonical injective group homomorphism `perm4EmbedBringS5 : Equiv.Perm (Fin 4) →* Equiv.Perm (Fin 5)`
     (index `5`, `120 = 5 * 24`), exhibiting $S_4$ unconditionally as the common maximal subgroup.

3. **§3 — Oriented Fano Octonion Algebra $\mathbb{O}(R)$ Over Any `CommRing R` (`Fin 8 → R`):**
   - Defines `octMul`, `octConj`, and `octNormSq` over any `CommRing R` from the 7 cyclic oriented
     Fano triples `(1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)`.
   - Proves two-sided identity `e_0`, imaginary squares `e_i * e_i = -e_0`, imaginary
     anti-commutativity `e_i * e_j = -e_j * e_i`, conjugation anti-automorphism, norm identity
     `x * octConj x = octNormSq x • e_0`, **Degen's eight-square identity**
     `octNormSq (octMul x y) = octNormSq x * octNormSq y`, **Artin's left and right alternative
     laws** (plus flexibility), and explicit non-associativity over `ℤ` on `(e_1 * e_2) * e_3 ≠ e_1 * (e_2 * e_3)`.

4. **§4 — Blichfeldt–Klein 3D Embedding $\mathrm{PSL}(2, 7) \hookrightarrow \mathrm{SL}(3, R)$ & Unitary $\mathrm{SU}(3)$ Realization over $\mathbb{C}$:**
   - Proves the quadratic Gauss-sum identity `(gaussSeven ζ)^2 = -7` unconditionally over any
     `CommRing R` from `cyclotomicSeven ζ = 0`.
   - Constructs the explicit $3 \times 3$ Klein–Blichfeldt generators `blichfeldtT ζ`,
     `blichfeldtR`, and `blichfeldtS ζ s` in `Matrix (Fin 3) (Fin 3) R`, proving unimodularity
     (`det = 1`, `trace S = -1`) and the complete Dyck $(2, 3, 7; 4)$ & Frobenius $C_7 \rtimes C_3$
     presentation relations `T^7 = 1`, `R^3 = 1`, `R * T * Rᵀ = T^2`, `S^2 = 1`, `(S * R)^2 = 1`,
     `(S * T)^3 = 1`, and `(S * T^3)^4 = 1`.
   - Instantiates the 7th-root Gauss-sum datum concretely over `ℂ` at
     `zetaSevenC = Complex.exp (2 * Real.pi * Complex.I / 7)` (`0` axioms, `0` uninstantiated
     classes) and proves exact $\mathrm{SU}(3)$ unitarity `Mᴴ * M = 1` and `det M = 1` for all
     three Blichfeldt generators.
-/

namespace QOU.Eightfold.BringGenusThreeFanoOctonionAndBlichfeldtSU3

open scoped BigOperators Matrix

-- ============================================================================
-- §1. Projective Fano Plane P²(F₂) & Hurwitz Order-168 Group GL(3, F₂)
-- ============================================================================

/-- Underlying 3-dimensional vector space $\mathbb{F}_2^3$ over `ZMod 2`. -/
abbrev FanoVec : Type := Fin 3 → ZMod 2

/-- Projective points of the Fano plane $\mathbb{P}^2(\mathbb{F}_2)$: nonzero vectors in $\mathbb{F}_2^3$. -/
abbrev FanoPoint : Type := {v : FanoVec // v ≠ 0}

/-- Boolean test whether a `Finset FanoPoint` is a Fano line: a 3-element subset $\{u, v, w\}$
    whose vector sum vanishes ($u + v + w = 0$, i.e. $w = u + v$, the nonzero vectors of a 2D
    subspace of $\mathbb{F}_2^3$). -/
def isFanoLineBool (L : Finset FanoPoint) : Bool :=
  (L.card == 3) && (Finset.sum L (fun p => p.val) == 0)

/-- Projective lines of the Fano plane $\mathbb{P}^2(\mathbb{F}_2)$. -/
abbrev FanoLine : Type := {L : Finset FanoPoint // isFanoLineBool L = true}

/-- **There are exactly 7 points in the Fano plane $\mathbb{P}^2(\mathbb{F}_2)$.** -/
theorem card_fanoPoint : Fintype.card FanoPoint = 7 := by
  decide

/-- **There are exactly 7 lines in the Fano plane $\mathbb{P}^2(\mathbb{F}_2)$.** -/
theorem card_fanoLine : Fintype.card FanoLine = 7 := by
  decide

/-- **Every Fano line contains exactly 3 Fano points.** -/
theorem fano_line_card_eq_three (L : FanoLine) : L.val.card = 3 := by
  have h := L.property
  unfold isFanoLineBool at h
  rw [Bool.and_eq_true, beq_iff_eq] at h
  exact h.1

/-- **Every Fano point lies on exactly 3 Fano lines.** -/
theorem fano_point_on_three_lines :
    ∀ p : FanoPoint, (Finset.univ.filter (fun L : FanoLine => p ∈ L.val)).card = 3 := by
  decide

/-- Finset cardinality form: every pair of distinct Fano points lies on a single Fano line. -/
theorem fano_filter_lines_through_pair_card :
    ∀ p q : FanoPoint, p ≠ q →
      (Finset.univ.filter (fun L : FanoLine => p ∈ L.val ∧ q ∈ L.val)).card = 1 := by
  decide

/-- **Projective Incidence Axiom I:** Every pair of distinct Fano points lies on a unique Fano line. -/
theorem fano_unique_line_through_two_points (p q : FanoPoint) (hpq : p ≠ q) :
    ∃! L : FanoLine, p ∈ L.val ∧ q ∈ L.val := by
  have hcard := fano_filter_lines_through_pair_card p q hpq
  rcases Finset.card_eq_one.mp hcard with ⟨L, hL⟩
  refine ⟨L, ?_, ?_⟩
  · have hmem : L ∈ Finset.univ.filter (fun L' : FanoLine => p ∈ L'.val ∧ q ∈ L'.val) := by
      rw [hL]; exact Finset.mem_singleton_self L
    exact (Finset.mem_filter.mp hmem).2
  · intro L' hL'
    have hmem : L' ∈ Finset.univ.filter (fun L'' : FanoLine => p ∈ L''.val ∧ q ∈ L''.val) :=
      Finset.mem_filter.mpr ⟨Finset.mem_univ L', hL'⟩
    rw [hL] at hmem
    exact Finset.mem_singleton.mp hmem

/-- Finset cardinality form: every pair of distinct Fano lines meets in a single Fano point. -/
theorem fano_inter_two_lines_card :
    ∀ L₁ L₂ : FanoLine, L₁ ≠ L₂ → (L₁.val ∩ L₂.val).card = 1 := by
  decide

/-- **Projective Incidence Axiom II:** Every pair of distinct Fano lines intersects in a unique Fano point. -/
theorem fano_unique_point_on_two_lines (L₁ L₂ : FanoLine) (hL : L₁ ≠ L₂) :
    ∃! p : FanoPoint, p ∈ L₁.val ∧ p ∈ L₂.val := by
  have hcard := fano_inter_two_lines_card L₁ L₂ hL
  rcases Finset.card_eq_one.mp hcard with ⟨p, hp⟩
  refine ⟨p, ?_, ?_⟩
  · have hmem : p ∈ L₁.val ∩ L₂.val := by
      rw [hp]; exact Finset.mem_singleton_self p
    exact Finset.mem_inter.mp hmem
  · intro p' hp'
    have hmem : p' ∈ L₁.val ∩ L₂.val := Finset.mem_inter.mpr hp'
    rw [hp] at hmem
    exact Finset.mem_singleton.mp hmem

/-- Fast explicit $3 \times 3$ polynomial determinant over `ZMod 2` (avoiding symmetric-group
    sign unfolding during kernel `decide`). -/
def det3F2 (M : Matrix (Fin 3) (Fin 3) (ZMod 2)) : ZMod 2 :=
  M 0 0 * (M 1 1 * M 2 2 - M 1 2 * M 2 1) -
  M 0 1 * (M 1 0 * M 2 2 - M 1 2 * M 2 0) +
  M 0 2 * (M 1 0 * M 2 1 - M 1 1 * M 2 0)

/-- `det3F2` agrees identically with `Matrix.det`. -/
theorem det_eq_det3F2 (M : Matrix (Fin 3) (Fin 3) (ZMod 2)) : M.det = det3F2 M := by
  rw [Matrix.det_fin_three]
  unfold det3F2
  ring

/-- Invertible $3 \times 3$ matrices over `ZMod 2` presented as a subtype of the 512-element
    matrix type `Matrix (Fin 3) (Fin 3) (ZMod 2)`. -/
abbrev InvMat3F2 : Type := {M : Matrix (Fin 3) (Fin 3) (ZMod 2) // det3F2 M ≠ 0}

/-- Over `ZMod 2`, any nonzero scalar equals `1`. -/
theorem zmod2_eq_one_of_ne_zero {x : ZMod 2} (hx : x ≠ 0) : x = 1 := by
  fin_cases x
  · exact False.elim (hx rfl)
  · rfl

/-- Matrix subtype for the point stabilizer of $e_0 = (1, 0, 0)^T$. -/
abbrev PointStabMat3F2 : Type :=
  {M : Matrix (Fin 3) (Fin 3) (ZMod 2) // det3F2 M ≠ 0 ∧ M 0 0 = 1 ∧ M 1 0 = 0 ∧ M 2 0 = 0}

/-- Exact matrix count for the point stabilizer of $e_0$: `24`. -/
theorem card_pointStabMat3F2 : Fintype.card PointStabMat3F2 = 24 := by
  decide

/-- Explicit involutive representative matrix $A(p) \in \mathrm{GL}_3(\mathbb{F}_2)$ for each
    of the 7 Fano points, satisfying $A(p)^2 = I_3$, $\det A(p) = 1$, and $A(p) e_0 = p$. -/
def fanoPointRepMat (p : FanoPoint) : Matrix (Fin 3) (Fin 3) (ZMod 2) :=
  match (p.val 0).val, (p.val 1).val, (p.val 2).val with
  | 1, 0, 0 => !![1, 0, 0; 0, 1, 0; 0, 0, 1]
  | 0, 1, 0 => !![0, 1, 0; 1, 0, 0; 0, 0, 1]
  | 0, 0, 1 => !![0, 0, 1; 0, 1, 0; 1, 0, 0]
  | 1, 1, 0 => !![1, 0, 0; 1, 1, 0; 0, 0, 1]
  | 1, 0, 1 => !![1, 0, 0; 0, 1, 0; 1, 0, 1]
  | 0, 1, 1 => !![0, 1, 0; 1, 0, 0; 1, 1, 1]
  | _, _, _ => !![1, 0, 0; 1, 1, 0; 1, 0, 1]

theorem fanoPointRepMat_props :
    ∀ p : FanoPoint,
      fanoPointRepMat p * fanoPointRepMat p = 1 ∧
      det3F2 (fanoPointRepMat p) = 1 ∧
      (∀ i : Fin 3, fanoPointRepMat p i 0 = p.val i) := by
  decide

/-- First column of any invertible $3 \times 3$ matrix over $\mathbb{F}_2$ as a `FanoPoint`. -/
def invMatCol0 (M : InvMat3F2) : FanoPoint :=
  ⟨fun i => M.val i 0, by
    intro h0
    have h00 : M.val 0 0 = 0 := congrFun h0 0
    have h10 : M.val 1 0 = 0 := congrFun h0 1
    have h20 : M.val 2 0 = 0 := congrFun h0 2
    apply M.property
    simp [det3F2, h00, h10, h20]⟩

/-- Constructive coset decomposition `InvMat3F2 ≃ FanoPoint × PointStabMat3F2`
    realizing $168 = 7 \times 24$ without 168-element kernel enumeration. -/
def invMat3F2EquivFanoProdPointStab : InvMat3F2 ≃ FanoPoint × PointStabMat3F2 where
  toFun M :=
    let p := invMatCol0 M
    let A := fanoPointRepMat p
    let hA := fanoPointRepMat_props p
    (p, ⟨A * M.val, by
      have hdet : det3F2 (A * M.val) ≠ 0 := by
        rw [← det_eq_det3F2, Matrix.det_mul, det_eq_det3F2, det_eq_det3F2, hA.2.1, one_mul]
        exact M.property
      have hcol : ∀ i : Fin 3, (A * M.val) i 0 = (1 : Matrix (Fin 3) (Fin 3) (ZMod 2)) i 0 := by
        intro i
        have hsq : (A * A) i 0 = (1 : Matrix (Fin 3) (Fin 3) (ZMod 2)) i 0 :=
          congrFun (congrFun hA.1 i) 0
        rw [← hsq, Matrix.mul_apply, Matrix.mul_apply]
        refine Finset.sum_congr rfl (fun k _ => ?_)
        dsimp only [A, p]
        rw [hA.2.2 k]
        rfl
      refine ⟨hdet, ?_, ?_, ?_⟩
      · simpa using hcol 0
      · simpa using hcol 1
      · simpa using hcol 2⟩)
  invFun q :=
    let p := q.1
    let N := q.2
    let A := fanoPointRepMat p
    let hA := fanoPointRepMat_props p
    ⟨A * N.val, by
      rw [← det_eq_det3F2, Matrix.det_mul, det_eq_det3F2, det_eq_det3F2, hA.2.1, one_mul]
      exact N.property.1⟩
  left_inv M := by
    apply Subtype.ext
    dsimp only
    rw [← Matrix.mul_assoc, (fanoPointRepMat_props (invMatCol0 M)).1, Matrix.one_mul]
  right_inv q := by
    rcases q with ⟨p, N⟩
    have hA := fanoPointRepMat_props p
    have hp : invMatCol0 ⟨fanoPointRepMat p * N.val, by
        rw [← det_eq_det3F2, Matrix.det_mul, det_eq_det3F2, det_eq_det3F2, hA.2.1, one_mul]
        exact N.property.1⟩ = p := by
      apply Subtype.ext
      ext i
      change (fanoPointRepMat p * N.val) i 0 = p.val i
      rw [Matrix.mul_apply, Fin.sum_univ_three, N.property.2.1, N.property.2.2.1, N.property.2.2.2]
      simp [hA.2.2 i]
    refine Prod.ext hp (Subtype.ext ?_)
    change fanoPointRepMat _ * (fanoPointRepMat p * N.val) = N.val
    rw [hp, ← Matrix.mul_assoc, hA.1, Matrix.one_mul]

/-- **Exact count of invertible $3 \times 3$ matrices over $\mathbb{F}_2$:**
    $(2^3 - 1)(2^3 - 2)(2^3 - 4) = 7 \times 24 = 168$. -/
theorem card_invMat3F2 : Fintype.card InvMat3F2 = 168 := by
  rw [Fintype.card_congr invMat3F2EquivFanoProdPointStab, Fintype.card_prod,
    card_fanoPoint, card_pointStabMat3F2]

/-- Explicit equivalence between `Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)` and `InvMat3F2`. -/
noncomputable def gl3F2EquivInvMat :
    Matrix.GeneralLinearGroup (Fin 3) (ZMod 2) ≃ InvMat3F2 where
  toFun g := ⟨g.val, by
    rw [← det_eq_det3F2]
    intro hdet
    have hmul : (g.val * (g⁻¹).val).det = 1 := by simp
    rw [Matrix.det_mul, hdet, zero_mul] at hmul
    exact zero_ne_one hmul⟩
  invFun M :=
    have hdet : M.val.det = 1 := (det_eq_det3F2 M.val).trans (zmod2_eq_one_of_ne_zero M.property)
    have hu : IsUnit M.val.det := hdet ▸ isUnit_one
    Matrix.GeneralLinearGroup.mk'' M.val hu
  left_inv g := by
    ext i j
    rfl
  right_inv M := by
    ext i j
    rfl

@[simp] theorem gl3F2EquivInvMat_symm_val (M : InvMat3F2) :
    (gl3F2EquivInvMat.symm M).val = M.val :=
  rfl

/-- Canonical `Fintype` structure on `Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)` transferred
    along `gl3F2EquivInvMat`. -/
noncomputable instance instFintypeGL3F2 :
    Fintype (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) :=
  Fintype.ofEquiv InvMat3F2 gl3F2EquivInvMat.symm

/-- **The Fano / Klein automorphism group $\mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2, 7)$
    has exact order 168.** -/
theorem card_gl3_f2 :
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) = 168 := by
  rw [Fintype.card_congr gl3F2EquivInvMat, card_invMat3F2]

/-- **Hurwitz genus-3 bound saturation (`168 = 84 * (3 - 1)`):**
    $|\mathrm{GL}(3, \mathbb{F}_2)| = 168$ equals Hurwitz's maximal automorphism bound $84(g - 1)$
    at genus $g = 3$. -/
theorem gl3_f2_saturates_hurwitz_genus_three :
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) = 84 * (3 - 1) ∧
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) =
      QOU.Brings.BringVandermondeSmoothnessAndGenusThree.hurwitzBound 3 := by
  rw [card_gl3_f2]
  decide

-- ============================================================================
-- §2. Resolving S₅ ⊅ PSL(2,7) via the Common Maximal Subgroup S₄ (qou-ys29)
-- ============================================================================

/-- **Arithmetic Lagrange obstruction:** $168 \nmid 5! = 120$. -/
theorem not_168_dvd_factorial_5 : ¬ (168 ∣ Nat.factorial 5) := by
  decide

/-- **Group-theoretic non-embedding theorem (`qou-ys29`):**
    No injective group homomorphism $\mathrm{GL}(3, \mathbb{F}_2) \hookrightarrow S_5$ exists,
    so the genus-3 Klein/Fano automorphism group cannot sit inside Bring's $\mathrm{Aut}(\Sigma_4) = S_5$. -/
theorem no_injective_hom_gl3_f2_to_s5 :
    ¬ ∃ φ : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2) →* Equiv.Perm (Fin 5),
        Function.Injective φ := by
  rintro ⟨φ, hφ⟩
  have hbij : Function.Bijective φ.rangeRestrict :=
    ⟨fun a b hab => hφ (congrArg Subtype.val hab), φ.rangeRestrict_surjective⟩
  have hcard_range : Nat.card φ.range = 168 := by
    have heq : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2) ≃ φ.range :=
      Equiv.ofBijective φ.rangeRestrict hbij
    rw [Nat.card_eq_fintype_card, ← Fintype.card_congr heq, card_gl3_f2]
  have hdvd : Nat.card φ.range ∣ Nat.card (Equiv.Perm (Fin 5)) :=
    Subgroup.card_subgroup_dvd_card φ.range
  rw [hcard_range, Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin] at hdvd
  exact not_168_dvd_factorial_5 hdvd

/-- Linear action of `Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)` on `FanoPoint`. -/
def fanoAct (g : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) (p : FanoPoint) : FanoPoint :=
  ⟨g.val.mulVec p.val, by
    intro hzero
    have hp : ((g⁻¹).val * g.val).mulVec p.val = 0 := by
      rw [← Matrix.mulVec_mulVec, hzero, Matrix.mulVec_zero]
    have hmul : (g⁻¹).val * g.val = 1 := by simp
    rw [hmul, Matrix.one_mulVec] at hp
    exact p.property hp⟩

@[simp] theorem fanoAct_one (p : FanoPoint) : fanoAct 1 p = p := by
  apply Subtype.ext
  exact Matrix.one_mulVec p.val

@[simp] theorem fanoAct_mul (g h : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) (p : FanoPoint) :
    fanoAct (g * h) p = fanoAct g (fanoAct h p) := by
  apply Subtype.ext
  exact (Matrix.mulVec_mulVec p.val g.val h.val).symm

/-- Distinguished Fano point $e_0 = (1, 0, 0)^T \in \mathbb{P}^2(\mathbb{F}_2)$. -/
def stdFanoPoint0 : FanoPoint := ⟨![1, 0, 0], by decide⟩

/-- Point stabilizer subgroup $\{g \in \mathrm{GL}_3(\mathbb{F}_2) \mid g(e_0) = e_0\}$. -/
def pointStabilizerSubgroup : Subgroup (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) where
  carrier := {g | fanoAct g stdFanoPoint0 = stdFanoPoint0}
  one_mem' := fanoAct_one stdFanoPoint0
  mul_mem' {g h} hg hh := by
    change fanoAct (g * h) stdFanoPoint0 = stdFanoPoint0
    rw [fanoAct_mul, hh, hg]
  inv_mem' {g} hg := by
    change fanoAct g⁻¹ stdFanoPoint0 = stdFanoPoint0
    have h1 : fanoAct g⁻¹ (fanoAct g stdFanoPoint0) = stdFanoPoint0 := by
      rw [← fanoAct_mul, inv_mul_cancel, fanoAct_one]
    rwa [hg] at h1

/-- Matrix characterization of `pointStabilizerSubgroup`: $g$ fixes $e_0 = (1, 0, 0)^T$ iff
    column `0` of $g$ is $(1, 0, 0)^T$. -/
theorem mem_pointStabilizer_iff (g : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) :
    g ∈ pointStabilizerSubgroup ↔ g.val 0 0 = 1 ∧ g.val 1 0 = 0 ∧ g.val 2 0 = 0 := by
  constructor
  · intro hg
    have hv : g.val.mulVec ![1, 0, 0] = ![1, 0, 0] := congrArg Subtype.val hg
    have h0 := congrFun hv 0
    have h1 := congrFun hv 1
    have h2 := congrFun hv 2
    simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h0 h1 h2
    exact ⟨h0, h1, h2⟩
  · rintro ⟨h00, h10, h20⟩
    apply Subtype.ext
    change g.val.mulVec ![1, 0, 0] = ![1, 0, 0]
    ext i
    fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three, h00, h10, h20]

/-- Equivalence between `pointStabilizerSubgroup` and `PointStabMat3F2`. -/
noncomputable def pointStabilizerEquivMat : pointStabilizerSubgroup ≃ PointStabMat3F2 where
  toFun g :=
    have hm := (mem_pointStabilizer_iff g.val).mp g.property
    ⟨g.val.val, (gl3F2EquivInvMat g.val).property, hm.1, hm.2.1, hm.2.2⟩
  invFun M :=
    let g := gl3F2EquivInvMat.symm ⟨M.val, M.property.1⟩
    ⟨g, (mem_pointStabilizer_iff g).mpr M.property.2⟩
  left_inv g := by ext i j; rfl
  right_inv M := by ext i j; rfl

noncomputable instance instFintypePointStabilizer : Fintype pointStabilizerSubgroup :=
  Fintype.ofEquiv PointStabMat3F2 pointStabilizerEquivMat.symm

/-- **The point stabilizer of $e_0$ in $\mathrm{GL}(3, \mathbb{F}_2)$ has order $24 = 4!$ (index 7).** -/
theorem card_pointStabilizerSubgroup :
    Fintype.card pointStabilizerSubgroup = 24 ∧
    Fintype.card pointStabilizerSubgroup = Nat.factorial 4 ∧
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) =
      7 * Fintype.card pointStabilizerSubgroup := by
  have hc : Fintype.card pointStabilizerSubgroup = 24 := by
    rw [Fintype.card_congr pointStabilizerEquivMat, card_pointStabMat3F2]
  rw [hc, card_gl3_f2]
  decide

/-- Standard Fano line $L_0 = \{p \in \mathrm{FanoPoint} \mid p_2 = 0\}
    = \{(1,0,0), (0,1,0), (1,1,0)\}$. -/
def stdFanoLine0Finset : Finset FanoPoint :=
  Finset.univ.filter (fun p : FanoPoint => p.val 2 = 0)

/-- Proof that `stdFanoLine0Finset` is a genuine Fano line (`FanoLine`). -/
theorem stdFanoLine0_isFanoLine : isFanoLineBool stdFanoLine0Finset = true := by
  decide

/-- The distinguished Fano line $L_0 : \mathrm{FanoLine}$. -/
def stdFanoLine0 : FanoLine := ⟨stdFanoLine0Finset, stdFanoLine0_isFanoLine⟩

/-- Membership in `stdFanoLine0` is equivalent to vanishing third coordinate `p.val 2 = 0`. -/
@[simp] theorem mem_stdFanoLine0_iff (p : FanoPoint) :
    p ∈ stdFanoLine0.val ↔ p.val 2 = 0 := by
  simp [stdFanoLine0, stdFanoLine0Finset]

/-- Line stabilizer subgroup $\{g \in \mathrm{GL}_3(\mathbb{F}_2) \mid g(L_0) = L_0\}$. -/
def lineStabilizerSubgroup : Subgroup (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) where
  carrier := {g | ∀ p : FanoPoint, fanoAct g p ∈ stdFanoLine0.val ↔ p ∈ stdFanoLine0.val}
  one_mem' p := by simp
  mul_mem' {g h} hg hh p := by
    rw [fanoAct_mul]
    exact (hg (fanoAct h p)).trans (hh p)
  inv_mem' {g} hg p := by
    have h1 := hg (fanoAct g⁻¹ p)
    have h2 : fanoAct g (fanoAct g⁻¹ p) = p := by
      rw [← fanoAct_mul, mul_inv_cancel, fanoAct_one]
    rw [h2] at h1
    exact h1.symm

/-- Matrix characterization of `lineStabilizerSubgroup`: $g$ stabilizes $L_0 = \{v_2 = 0\}$
    if and only if $g_{2,0} = 0$ and $g_{2,1} = 0$. -/
theorem mem_lineStabilizer_iff (g : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) :
    g ∈ lineStabilizerSubgroup ↔ g.val 2 0 = 0 ∧ g.val 2 1 = 0 := by
  constructor
  · intro hg
    have hp0 : (⟨![1, 0, 0], by decide⟩ : FanoPoint) ∈ stdFanoLine0.val := by decide
    have hp1 : (⟨![0, 1, 0], by decide⟩ : FanoPoint) ∈ stdFanoLine0.val := by decide
    have h0 := (hg ⟨![1, 0, 0], by decide⟩).mpr hp0
    have h1 := (hg ⟨![0, 1, 0], by decide⟩).mpr hp1
    rw [mem_stdFanoLine0_iff] at h0 h1
    change (g.val.mulVec ![1, 0, 0]) 2 = 0 at h0
    change (g.val.mulVec ![0, 1, 0]) 2 = 0 at h1
    simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h0 h1
    exact ⟨h0, h1⟩
  · rintro ⟨h20, h21⟩ p
    rw [mem_stdFanoLine0_iff, mem_stdFanoLine0_iff]
    change (g.val.mulVec p.val) 2 = 0 ↔ p.val 2 = 0
    have hmul2 : (g.val.mulVec p.val) 2 = g.val 2 2 * p.val 2 := by
      simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three, h20, h21]
    have h22_ne : g.val 2 2 ≠ 0 := by
      intro h22
      have hdet_ne : det3F2 g.val ≠ 0 := (gl3F2EquivInvMat g).property
      apply hdet_ne
      simp [det3F2, h20, h21, h22]
    have h22_eq : g.val 2 2 = 1 := zmod2_eq_one_of_ne_zero h22_ne
    rw [hmul2, h22_eq, one_mul]

/-- Matrix subtype for the line stabilizer of $L_0$. -/
abbrev LineStabMat3F2 : Type :=
  {M : Matrix (Fin 3) (Fin 3) (ZMod 2) // det3F2 M ≠ 0 ∧ M 2 0 = 0 ∧ M 2 1 = 0}

/-- Exact matrix count for the line stabilizer of $L_0$: `24`. -/
theorem card_lineStabMat3F2 : Fintype.card LineStabMat3F2 = 24 := by
  decide

/-- Equivalence between `lineStabilizerSubgroup` and `LineStabMat3F2`. -/
noncomputable def lineStabilizerEquivMat : lineStabilizerSubgroup ≃ LineStabMat3F2 where
  toFun g :=
    have hm := (mem_lineStabilizer_iff g.val).mp g.property
    ⟨g.val.val, (gl3F2EquivInvMat g.val).property, hm.1, hm.2⟩
  invFun M :=
    let g := gl3F2EquivInvMat.symm ⟨M.val, M.property.1⟩
    ⟨g, (mem_lineStabilizer_iff g).mpr M.property.2⟩
  left_inv g := by ext i j; rfl
  right_inv M := by ext i j; rfl

noncomputable instance instFintypeLineStabilizer : Fintype lineStabilizerSubgroup :=
  Fintype.ofEquiv LineStabMat3F2 lineStabilizerEquivMat.symm

/-- **The line stabilizer of $L_0$ in $\mathrm{GL}(3, \mathbb{F}_2)$ has order $24 = 4!$ (index 7).** -/
theorem card_lineStabilizerSubgroup :
    Fintype.card lineStabilizerSubgroup = 24 ∧
    Fintype.card lineStabilizerSubgroup = Nat.factorial 4 ∧
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) =
      7 * Fintype.card lineStabilizerSubgroup := by
  have hc : Fintype.card lineStabilizerSubgroup = 24 := by
    rw [Fintype.card_congr lineStabilizerEquivMat, card_lineStabMat3F2]
  rw [hc, card_gl3_f2]
  decide

/-- The 4-element complement `FanoPoint \ L_0 = {p : FanoPoint // p ∉ L_0}`
    (equivalently `{v ∈ F₂³ \ {0} | v₂ = 1}`). -/
abbrev FanoComplement0 : Type := {p : FanoPoint // p ∉ stdFanoLine0.val}

/-- **There are exactly 4 Fano points outside $L_0$ (`7 - 3 = 4`).** -/
theorem card_fanoComplement0 : Fintype.card FanoComplement0 = 4 := by
  decide

/-- Explicit coordinate bijection between `FanoComplement0` ($\{(a, b, 1) : a, b \in \mathbb{F}_2\}$)
    and `Fin 4` via $(a, b, 1) \mapsto a + 2b$. -/
def fanoComplement0EquivFin4 : FanoComplement0 ≃ Fin 4 where
  toFun q := ⟨(q.val.val 0).val + 2 * (q.val.val 1).val, by
    have h0 : (q.val.val 0).val < 2 := ZMod.val_lt (q.val.val 0)
    have h1 : (q.val.val 1).val < 2 := ZMod.val_lt (q.val.val 1)
    omega⟩
  invFun k :=
    match k with
    | ⟨0, _⟩ => ⟨⟨![0, 0, 1], by decide⟩, by decide⟩
    | ⟨1, _⟩ => ⟨⟨![1, 0, 1], by decide⟩, by decide⟩
    | ⟨2, _⟩ => ⟨⟨![0, 1, 1], by decide⟩, by decide⟩
    | ⟨3, _⟩ => ⟨⟨![1, 1, 1], by decide⟩, by decide⟩
  left_inv := by decide
  right_inv := by decide

/-- Action of an element $g \in \mathrm{lineStabilizerSubgroup}$ on a complement point $q \notin L_0$. -/
def lineStabActComplement (g : lineStabilizerSubgroup) (q : FanoComplement0) : FanoComplement0 :=
  ⟨fanoAct g.val q.val, fun hmem => q.property ((g.property q.val).mp hmem)⟩

/-- Group homomorphism from `lineStabilizerSubgroup` to permutations of the 4 complement points `FanoPoint \ L_0`. -/
def lineStabilizerToPermComplement : lineStabilizerSubgroup →* Equiv.Perm FanoComplement0 where
  toFun g :=
    { toFun := lineStabActComplement g
      invFun := lineStabActComplement g⁻¹
      left_inv := fun q => by
        apply Subtype.ext
        change fanoAct g⁻¹.val (fanoAct g.val q.val) = q.val
        rw [← fanoAct_mul]
        simp
      right_inv := fun q => by
        apply Subtype.ext
        change fanoAct g.val (fanoAct g⁻¹.val q.val) = q.val
        rw [← fanoAct_mul]
        simp }
  map_one' := by
    ext q i
    change (fanoAct 1 q.val).val i = q.val.val i
    rw [fanoAct_one]
  map_mul' g h := by
    ext q i
    change (fanoAct (g.val * h.val) q.val).val i = (fanoAct g.val (fanoAct h.val q.val)).val i
    rw [fanoAct_mul]

/-- **Faithfulness of the action of `lineStabilizerSubgroup` on `FanoPoint \ L_0`:**
    Since $c_{00} = (0,0,1)$, $c_{10} = (1,0,1)$, and $c_{01} = (0,1,1)$ lie in `FanoComplement0`
    and span $\mathbb{F}_2^3$ ($e_2 = c_{00}$, $e_0 = c_{10} + c_{00}$, $e_1 = c_{01} + c_{00}$),
    any matrix fixing `FanoComplement0` pointwise is the identity matrix. -/
theorem lineStabilizerToPermComplement_injective :
    Function.Injective lineStabilizerToPermComplement := by
  rw [injective_iff_map_eq_one]
  intro g hg
  have hfix : ∀ q : FanoComplement0, (fanoAct g.val q.val).val = q.val.val := by
    intro q
    have hq : lineStabilizerToPermComplement g q = q := by rw [hg]; rfl
    exact congrArg (fun x : FanoComplement0 => x.val.val) hq
  let c00 : FanoComplement0 := ⟨⟨![0, 0, 1], by decide⟩, by decide⟩
  let c10 : FanoComplement0 := ⟨⟨![1, 0, 1], by decide⟩, by decide⟩
  let c01 : FanoComplement0 := ⟨⟨![0, 1, 1], by decide⟩, by decide⟩
  have hc00 : g.val.val.mulVec ![0, 0, 1] = ![0, 0, 1] := hfix c00
  have hc10 : g.val.val.mulVec ![1, 0, 1] = ![1, 0, 1] := hfix c10
  have hc01 : g.val.val.mulVec ![0, 1, 1] = ![0, 1, 1] := hfix c01
  have hmat : g.val.val = 1 := by
    ext i j
    fin_cases j
    · have hsum : g.val.val.mulVec (![1, 0, 1] + ![0, 0, 1]) = ![1, 0, 1] + ![0, 0, 1] := by
        rw [Matrix.mulVec_add, hc10, hc00]
      have he0 : (![1, 0, 1] + ![0, 0, 1] : FanoVec) = ![1, 0, 0] := by decide
      rw [he0] at hsum
      have hi := congrFun hsum i
      fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at hi ⊢ <;> exact hi
    · have hsum : g.val.val.mulVec (![0, 1, 1] + ![0, 0, 1]) = ![0, 1, 1] + ![0, 0, 1] := by
        rw [Matrix.mulVec_add, hc01, hc00]
      have he1 : (![0, 1, 1] + ![0, 0, 1] : FanoVec) = ![0, 1, 0] := by decide
      rw [he1] at hsum
      have hi := congrFun hsum i
      fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at hi ⊢ <;> exact hi
    · have hi := congrFun hc00 i
      fin_cases i <;> simp [Matrix.mulVec, dotProduct, Fin.sum_univ_three] at hi ⊢ <;> exact hi
  ext i j
  exact congrFun (congrFun hmat i) j

/-- Bijectivity of `lineStabilizerToPermComplement` by injectivity between finite groups of equal
    cardinality `24 = 4!`. -/
theorem lineStabilizerToPermComplement_bijective :
    Function.Bijective lineStabilizerToPermComplement := by
  rw [Fintype.bijective_iff_injective_and_card]
  refine ⟨lineStabilizerToPermComplement_injective, ?_⟩
  rw [card_lineStabilizerSubgroup.1, Fintype.card_perm, card_fanoComplement0]
  decide

/-- Multiplicative group isomorphism induced on `Equiv.Perm` by `fanoComplement0EquivFin4`. -/
def permComplementMulEquivPerm4 : Equiv.Perm FanoComplement0 ≃* Equiv.Perm (Fin 4) :=
  { fanoComplement0EquivFin4.permCongr with
    map_mul' := fun σ τ => by
      ext k
      simp [Equiv.permCongr_apply, Equiv.Perm.mul_apply] }

/-- **Explicit group isomorphism $\mathrm{Stab}_{\mathrm{GL}_3(\mathbb{F}_2)}(L_0) \simeq_* S_4$ (`qou-ys29`):**
    The Fano line stabilizer is isomorphic as a group to `Equiv.Perm (Fin 4)`. -/
noncomputable def lineStabilizerMulEquivPerm4 :
    lineStabilizerSubgroup ≃* Equiv.Perm (Fin 4) :=
  (MulEquiv.ofBijective lineStabilizerToPermComplement lineStabilizerToPermComplement_bijective).trans
    permComplementMulEquivPerm4

/-- Explicit extension of a permutation $\sigma \in S_4$ to $S_5$ fixing sheet `4 : Fin 5`. -/
def extendPerm4Fun (σ : Equiv.Perm (Fin 4)) (k : Fin 5) : Fin 5 :=
  if hk : k.val < 4 then (σ ⟨k.val, hk⟩).castSucc else ⟨4, by decide⟩

/-- Canonical group homomorphism `Equiv.Perm (Fin 4) →* Equiv.Perm (Fin 5)` identifying $S_4$
    with the point stabilizer of sheet `4` inside Bring's automorphism group $S_5$. -/
def perm4EmbedBringS5 : Equiv.Perm (Fin 4) →* Equiv.Perm (Fin 5) where
  toFun σ :=
    { toFun := extendPerm4Fun σ
      invFun := extendPerm4Fun σ⁻¹
      left_inv := fun k => by
        unfold extendPerm4Fun
        by_cases hk : k.val < 4
        · have hlt : ((σ ⟨k.val, hk⟩).castSucc).val < 4 := (σ ⟨k.val, hk⟩).isLt
          simp only [dif_pos hk, dif_pos hlt]
          apply Fin.ext
          change (σ⁻¹ (σ ⟨k.val, hk⟩)).val = k.val
          simp
        · have hk4 : k.val = 4 := by omega
          simp only [dif_neg hk]
          have h4 : ¬ ((⟨4, by decide⟩ : Fin 5).val < 4) := by decide
          simp only [dif_neg h4]
          exact Fin.ext hk4.symm
      right_inv := fun k => by
        unfold extendPerm4Fun
        by_cases hk : k.val < 4
        · have hlt : ((σ⁻¹ ⟨k.val, hk⟩).castSucc).val < 4 := (σ⁻¹ ⟨k.val, hk⟩).isLt
          simp only [dif_pos hk, dif_pos hlt]
          apply Fin.ext
          change (σ (σ⁻¹ ⟨k.val, hk⟩)).val = k.val
          simp
        · have hk4 : k.val = 4 := by omega
          simp only [dif_neg hk]
          have h4 : ¬ ((⟨4, by decide⟩ : Fin 5).val < 4) := by decide
          simp only [dif_neg h4]
          exact Fin.ext hk4.symm }
  map_one' := by
    ext k
    change (extendPerm4Fun 1 k).val = k.val
    unfold extendPerm4Fun
    by_cases hk : k.val < 4
    · simp [dif_pos hk]
    · simp only [dif_neg hk]; omega
  map_mul' σ τ := by
    ext k
    change (extendPerm4Fun (σ * τ) k).val = (extendPerm4Fun σ (extendPerm4Fun τ k)).val
    unfold extendPerm4Fun
    by_cases hk : k.val < 4
    · have hlt : ((τ ⟨k.val, hk⟩).castSucc).val < 4 := (τ ⟨k.val, hk⟩).isLt
      simp only [dif_pos hk, dif_pos hlt]
      rfl
    · have h4 : ¬ ((⟨4, by decide⟩ : Fin 5).val < 4) := by decide
      simp only [dif_neg hk, dif_neg h4]

/-- **Injectivity of $S_4 \hookrightarrow S_5$ (`120 = 5 * 24`).** -/
theorem perm4EmbedBringS5_injective : Function.Injective perm4EmbedBringS5 := by
  intro σ τ h
  ext i
  have hi := congrArg (fun π : Equiv.Perm (Fin 5) => (π i.castSucc).val) h
  change (extendPerm4Fun σ i.castSucc).val = (extendPerm4Fun τ i.castSucc).val at hi
  unfold extendPerm4Fun at hi
  simp only [Fin.coe_castSucc, dif_pos i.isLt] at hi
  exact hi

/-- **Complete $S_4$ Bridge Theorem (`qou-ys29`):**
    1. $\mathrm{GL}(3, \mathbb{F}_2)$ (order `168`) has no injective homomorphism into $S_5$ (order `120`).
    2. `lineStabilizerSubgroup ≤ GL(3, F₂)` is isomorphic via `lineStabilizerMulEquivPerm4` to `S₄`
       (order `24`, index `7` in `GL(3, F₂)`).
    3. `S₄` embeds injectively via `perm4EmbedBringS5` into Bring's automorphism group `S₅`
       (index `5` in `S₅`, `120 = 5 * 24`). -/
theorem s4_common_subgroup_bridge_summary :
    (¬ ∃ φ : Matrix.GeneralLinearGroup (Fin 3) (ZMod 2) →* Equiv.Perm (Fin 5),
        Function.Injective φ) ∧
    Function.Bijective lineStabilizerMulEquivPerm4 ∧
    Function.Injective perm4EmbedBringS5 ∧
    Fintype.card (Equiv.Perm (Fin 5)) = 5 * Fintype.card (Equiv.Perm (Fin 4)) ∧
    Fintype.card (Matrix.GeneralLinearGroup (Fin 3) (ZMod 2)) =
      7 * Fintype.card lineStabilizerSubgroup := by
  refine ⟨no_injective_hom_gl3_f2_to_s5, lineStabilizerMulEquivPerm4.bijective,
    perm4EmbedBringS5_injective, ?_, card_lineStabilizerSubgroup.2.2⟩
  rw [Fintype.card_perm, Fintype.card_perm, Fintype.card_fin, Fintype.card_fin]
  decide

-- ============================================================================
-- §3. Oriented Fano Octonion Algebra O(R) Over Any CommRing R (Fin 8 → R)
-- ============================================================================

/-- Octonion multiplication `octMul x y` on `Fin 8 → R` over any commutative ring `R`,
    defined by unit `e₀ = 1` and the 7 cyclic oriented Fano triples
    `(1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)`. -/
def octMul {R : Type*} [CommRing R] (x y : Fin 8 → R) : Fin 8 → R
  | ⟨0, _⟩ =>
      x 0 * y 0 - x 1 * y 1 - x 2 * y 2 - x 3 * y 3 - x 4 * y 4 - x 5 * y 5 - x 6 * y 6 - x 7 * y 7
  | ⟨1, _⟩ =>
      x 0 * y 1 + x 1 * y 0 + (x 2 * y 4 - x 4 * y 2) + (x 3 * y 7 - x 7 * y 3) + (x 5 * y 6 - x 6 * y 5)
  | ⟨2, _⟩ =>
      x 0 * y 2 + x 2 * y 0 + (x 3 * y 5 - x 5 * y 3) + (x 4 * y 1 - x 1 * y 4) + (x 6 * y 7 - x 7 * y 6)
  | ⟨3, _⟩ =>
      x 0 * y 3 + x 3 * y 0 + (x 4 * y 6 - x 6 * y 4) + (x 5 * y 2 - x 2 * y 5) + (x 7 * y 1 - x 1 * y 7)
  | ⟨4, _⟩ =>
      x 0 * y 4 + x 4 * y 0 + (x 5 * y 7 - x 7 * y 5) + (x 6 * y 3 - x 3 * y 6) + (x 1 * y 2 - x 2 * y 1)
  | ⟨5, _⟩ =>
      x 0 * y 5 + x 5 * y 0 + (x 6 * y 1 - x 1 * y 6) + (x 7 * y 4 - x 4 * y 7) + (x 2 * y 3 - x 3 * y 2)
  | ⟨6, _⟩ =>
      x 0 * y 6 + x 6 * y 0 + (x 7 * y 2 - x 2 * y 7) + (x 1 * y 5 - x 5 * y 1) + (x 3 * y 4 - x 4 * y 3)
  | ⟨7, _⟩ =>
      x 0 * y 7 + x 7 * y 0 + (x 1 * y 3 - x 3 * y 1) + (x 2 * y 6 - x 6 * y 2) + (x 4 * y 5 - x 5 * y 4)

/-- Standard basis elements $e_0, \dots, e_7$ of $\mathbb{O}(R) = (\mathrm{Fin}\, 8 \to R)$. -/
def octBasis (R : Type*) [CommRing R] (i : Fin 8) : Fin 8 → R :=
  fun k => if k = i then 1 else 0

/-- Octonion conjugation $\overline{x} = (x_0, -x_1, \dots, -x_7)$. -/
def octConj {R : Type*} [CommRing R] (x : Fin 8 → R) : Fin 8 → R
  | ⟨0, _⟩ => x 0
  | ⟨1, _⟩ => -x 1
  | ⟨2, _⟩ => -x 2
  | ⟨3, _⟩ => -x 3
  | ⟨4, _⟩ => -x 4
  | ⟨5, _⟩ => -x 5
  | ⟨6, _⟩ => -x 6
  | ⟨7, _⟩ => -x 7

/-- Quadratic norm form $N(x) = \sum_{i=0}^7 x_i^2 \in R$. -/
def octNormSq {R : Type*} [CommRing R] (x : Fin 8 → R) : R :=
  ∑ i : Fin 8, (x i) ^ 2

/-- Explicit sum expansion of `octNormSq`. -/
theorem octNormSq_eq {R : Type*} [CommRing R] (x : Fin 8 → R) :
    octNormSq x =
      x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 + x 4 ^ 2 + x 5 ^ 2 + x 6 ^ 2 + x 7 ^ 2 := by
  unfold octNormSq
  rw [Fin.sum_univ_eight]

/-- **Left identity:** `octMul (e₀) x = x` over any `CommRing R`. -/
theorem octMul_one_left {R : Type*} [CommRing R] (x : Fin 8 → R) :
    octMul (octBasis R 0) x = x := by
  ext k
  fin_cases k <;> (dsimp [octMul, octBasis]; ring)

/-- **Right identity:** `octMul x (e₀) = x` over any `CommRing R`. -/
theorem octMul_one_right {R : Type*} [CommRing R] (x : Fin 8 → R) :
    octMul x (octBasis R 0) = x := by
  ext k
  fin_cases k <;> (dsimp [octMul, octBasis]; ring)

/-- **Oriented Fano cyclic multiplication triples `(1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)`.** -/
theorem octMul_oriented_fano_triples (R : Type*) [CommRing R] :
    octMul (octBasis R 1) (octBasis R 2) = octBasis R 4 ∧
    octMul (octBasis R 2) (octBasis R 3) = octBasis R 5 ∧
    octMul (octBasis R 3) (octBasis R 4) = octBasis R 6 ∧
    octMul (octBasis R 4) (octBasis R 5) = octBasis R 7 ∧
    octMul (octBasis R 5) (octBasis R 6) = octBasis R 1 ∧
    octMul (octBasis R 6) (octBasis R 7) = octBasis R 2 ∧
    octMul (octBasis R 7) (octBasis R 1) = octBasis R 3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (ext k; fin_cases k <;> (dsimp [octMul, octBasis]; norm_num))

/-- **Imaginary squares:** For every imaginary basis unit $e_i$ ($i \neq 0$), $e_i^2 = -e_0$. -/
theorem octMul_imag_sq {R : Type*} [CommRing R] (i : Fin 8) (hi : i ≠ 0) :
    octMul (octBasis R i) (octBasis R i) = -octBasis R 0 := by
  fin_cases i
  · exact False.elim (hi rfl)
  all_goals
    ext k
    fin_cases k <;> (dsimp [octMul, octBasis]; norm_num)

/-- **Imaginary anti-commutativity:** Distinct imaginary units anti-commute, $e_i e_j = - e_j e_i$. -/
theorem octMul_imag_anticomm {R : Type*} [CommRing R] (i j : Fin 8)
    (hi : i ≠ 0) (hj : j ≠ 0) (hij : i ≠ j) :
    octMul (octBasis R i) (octBasis R j) = -octMul (octBasis R j) (octBasis R i) := by
  have hsum : octMul (octBasis R i) (octBasis R j) + octMul (octBasis R j) (octBasis R i) = 0 := by
    ext k
    have hi0 : octBasis R i 0 = 0 := by simp [octBasis, Ne.symm hi]
    have hj0 : octBasis R j 0 = 0 := by simp [octBasis, Ne.symm hj]
    have hij_prod : ∀ m : Fin 8, octBasis R i m * octBasis R j m = 0 := by
      intro m
      by_cases hmi : m = i
      · subst hmi; simp [octBasis, hij]
      · simp [octBasis, hmi]
    fin_cases k
    · change octMul (octBasis R i) (octBasis R j) 0 + octMul (octBasis R j) (octBasis R i) 0 = 0
      dsimp [octMul]
      rw [hi0, hj0, hij_prod 1, hij_prod 2, hij_prod 3, hij_prod 4, hij_prod 5, hij_prod 6, hij_prod 7]
      have hji : ∀ m : Fin 8, octBasis R j m * octBasis R i m = 0 := fun m => by
        rw [mul_comm]; exact hij_prod m
      rw [hji 1, hji 2, hji 3, hji 4, hji 5, hji 6, hji 7]
      ring
    all_goals
      dsimp [octMul]
      rw [hi0, hj0]
      ring
  exact eq_neg_of_add_eq_zero_left hsum

/-- **Conjugation involution:** $\overline{\overline{x}} = x$. -/
theorem octConj_involutive {R : Type*} [CommRing R] (x : Fin 8 → R) :
    octConj (octConj x) = x := by
  ext k
  fin_cases k <;> simp [octConj]

/-- **Conjugation anti-automorphism:** $\overline{x \cdot y} = \overline{y} \cdot \overline{x}$. -/
theorem octConj_octMul {R : Type*} [CommRing R] (x y : Fin 8 → R) :
    octConj (octMul x y) = octMul (octConj y) (octConj x) := by
  ext k
  fin_cases k <;> (dsimp [octConj, octMul]; ring)

/-- **Norm-conjugate identity:** $x \cdot \overline{x} = N(x) e_0$ and $\overline{x} \cdot x = N(x) e_0$. -/
theorem octMul_octConj_self {R : Type*} [CommRing R] (x : Fin 8 → R) :
    octMul x (octConj x) = octNormSq x • octBasis R 0 ∧
    octMul (octConj x) x = octNormSq x • octBasis R 0 := by
  rw [octNormSq_eq]
  constructor <;>
    (ext k; fin_cases k <;> (simp [octMul, octConj, octBasis]; ring))

/-- **Degen's Eight-Square Identity (Norm Multiplicativity over any `CommRing R`):**
    $N(x \cdot y) = N(x) \cdot N(y)$. -/
theorem octNormSq_octMul {R : Type*} [CommRing R] (x y : Fin 8 → R) :
    octNormSq (octMul x y) = octNormSq x * octNormSq y := by
  rw [octNormSq_eq, octNormSq_eq, octNormSq_eq]
  dsimp [octMul]
  ring

/-- **Artin's Left Alternative Law over any `CommRing R`:**
    $x \cdot (x \cdot y) = (x \cdot x) \cdot y$. -/
theorem octMul_left_alternative {R : Type*} [CommRing R] (x y : Fin 8 → R) :
    octMul x (octMul x y) = octMul (octMul x x) y := by
  ext k
  fin_cases k <;> (dsimp [octMul]; ring)

/-- **Artin's Right Alternative Law over any `CommRing R`:**
    $(y \cdot x) \cdot x = y \cdot (x \cdot x)$. -/
theorem octMul_right_alternative {R : Type*} [CommRing R] (x y : Fin 8 → R) :
    octMul (octMul y x) x = octMul y (octMul x x) := by
  ext k
  fin_cases k <;> (dsimp [octMul]; ring)

/-- **Flexible Identity over any `CommRing R`:**
    $x \cdot (y \cdot x) = (x \cdot y) \cdot x$. -/
theorem octMul_flexible {R : Type*} [CommRing R] (x y : Fin 8 → R) :
    octMul x (octMul y x) = octMul (octMul x y) x := by
  ext k
  fin_cases k <;> (dsimp [octMul]; ring)

/-- **Explicit Non-Associativity Witness over `ℤ`:**
    Off a Fano line, $(e_1 \cdot e_2) \cdot e_3 = -e_6$ whereas $e_1 \cdot (e_2 \cdot e_3) = +e_6$,
    so $(e_1 \cdot e_2) \cdot e_3 \neq e_1 \cdot (e_2 \cdot e_3)$ in $\mathbb{O}(\mathbb{Z})$. -/
theorem octMul_not_associative_int :
    octMul (octMul (octBasis ℤ 1) (octBasis ℤ 2)) (octBasis ℤ 3) ≠
      octMul (octBasis ℤ 1) (octMul (octBasis ℤ 2) (octBasis ℤ 3)) := by
  intro h
  have h6 : octMul (octMul (octBasis ℤ 1) (octBasis ℤ 2)) (octBasis ℤ 3) ⟨6, by decide⟩ =
      octMul (octBasis ℤ 1) (octMul (octBasis ℤ 2) (octBasis ℤ 3)) ⟨6, by decide⟩ :=
    congrFun h ⟨6, by decide⟩
  dsimp [octMul, octBasis] at h6
  omega

-- ============================================================================
-- §4. Blichfeldt–Klein 3D Embedding PSL(2,7) ↪ SL(3, R) & SU(3) over ℂ
-- ============================================================================

/-- Seventh cyclotomic polynomial $\Phi_7(\zeta) = 1 + \zeta + \zeta^2 + \zeta^3 + \zeta^4 + \zeta^5 + \zeta^6$. -/
def cyclotomicSeven {R : Type*} [CommRing R] (ζ : R) : R :=
  1 + ζ + ζ ^ 2 + ζ ^ 3 + ζ ^ 4 + ζ ^ 5 + ζ ^ 6

/-- Quadratic Gauss sum $g(\zeta) = \zeta + \zeta^2 + \zeta^4 - \zeta^3 - \zeta^5 - \zeta^6$
    summed with Legendre-symbol signs modulo $7$ (quadratic residues $\{1, 2, 4\}$ vs.
    non-residues $\{3, 5, 6\}$). -/
def gaussSeven {R : Type*} [CommRing R] (ζ : R) : R :=
  ζ + ζ ^ 2 + ζ ^ 4 - ζ ^ 3 - ζ ^ 5 - ζ ^ 6

/-- From $\Phi_7(\zeta) = 0$, $\zeta^7 = 1$. -/
theorem zeta_pow_seven_eq_one {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) : ζ ^ 7 = 1 := by
  unfold cyclotomicSeven at hΦ
  linear_combination (ζ - 1) * hΦ

/-- **Unconditional Quadratic Gauss-Sum Identity (`g(ζ)² = -7`):**
    Over any `CommRing R`, if $\Phi_7(\zeta) = 0$, then
    $(\zeta + \zeta^2 + \zeta^4 - \zeta^3 - \zeta^5 - \zeta^6)^2 = -7$. -/
theorem gaussSeven_sq_eq_neg_seven {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    (gaussSeven ζ) ^ 2 = -7 := by
  unfold gaussSeven cyclotomicSeven at *
  linear_combination
    (ζ ^ 6 + ζ ^ 5 - 3 * ζ ^ 4 + ζ ^ 3 + ζ ^ 2 - 7 * ζ + 7) * hΦ

/-- From $\Phi_7(\zeta) = 0$ and $s \cdot g(\zeta) = 1$, the identity $-7 s^2 = 1$ holds. -/
theorem neg_seven_mul_s_sq_eq_one {R : Type*} [CommRing R] {ζ s : R}
    (hΦ : cyclotomicSeven ζ = 0) (hs : s * gaussSeven ζ = 1) :
    -7 * s ^ 2 = 1 := by
  have hg : (gaussSeven ζ) ^ 2 = -7 := gaussSeven_sq_eq_neg_seven hΦ
  calc -7 * s ^ 2
      = s ^ 2 * (-7) := by ring
    _ = s ^ 2 * (gaussSeven ζ) ^ 2 := by rw [hg]
    _ = (s * gaussSeven ζ) ^ 2 := by ring
    _ = 1 := by rw [hs]; ring

/-- Order-7 diagonal Blichfeldt colour-phase generator $T(\zeta) = \mathrm{diag}(\zeta, \zeta^2, \zeta^4)$. -/
def blichfeldtT {R : Type*} [CommRing R] (ζ : R) : Matrix (Fin 3) (Fin 3) R
  | ⟨0, _⟩, ⟨0, _⟩ => ζ
  | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 2
  | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 4
  | _, _ => 0

/-- Explicit inverse diagonal matrix $T(\zeta)^{-1} = \mathrm{diag}(\zeta^6, \zeta^5, \zeta^3)$. -/
def blichfeldtTInv {R : Type*} [CommRing R] (ζ : R) : Matrix (Fin 3) (Fin 3) R
  | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 6
  | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 5
  | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 3
  | _, _ => 0

/-- Order-3 cyclic colour-permutation generator $R$. -/
def blichfeldtR {R : Type*} [CommRing R] : Matrix (Fin 3) (Fin 3) R
  | ⟨0, _⟩, ⟨1, _⟩ => 1
  | ⟨1, _⟩, ⟨2, _⟩ => 1
  | ⟨2, _⟩, ⟨0, _⟩ => 1
  | _, _ => 0

/-- Unscaled integral-cyclotomic Hankel kernel `blichfeldtRawS ζ` of Klein's involution matrix. -/
def blichfeldtRawS {R : Type*} [CommRing R] (ζ : R) : Matrix (Fin 3) (Fin 3) R
  | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 2 - ζ ^ 5
  | ⟨0, _⟩, ⟨1, _⟩ => ζ - ζ ^ 6
  | ⟨0, _⟩, ⟨2, _⟩ => ζ ^ 4 - ζ ^ 3
  | ⟨1, _⟩, ⟨0, _⟩ => ζ - ζ ^ 6
  | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 4 - ζ ^ 3
  | ⟨1, _⟩, ⟨2, _⟩ => ζ ^ 2 - ζ ^ 5
  | ⟨2, _⟩, ⟨0, _⟩ => ζ ^ 4 - ζ ^ 3
  | ⟨2, _⟩, ⟨1, _⟩ => ζ ^ 2 - ζ ^ 5
  | ⟨2, _⟩, ⟨2, _⟩ => ζ - ζ ^ 6

/-- Klein–Blichfeldt order-2 generator $S(\zeta, s) = (-s) \cdot \mathrm{rawS}(\zeta) \in \mathrm{SL}(3, R)$. -/
def blichfeldtS {R : Type*} [CommRing R] (ζ s : R) : Matrix (Fin 3) (Fin 3) R :=
  (-s) • blichfeldtRawS ζ

/-- Unscaled square identity `rawS(ζ)² = -7 • I₃` over any `CommRing R`. -/
theorem blichfeldtRawS_sq_eq_neg_seven {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    blichfeldtRawS ζ * blichfeldtRawS ζ = (-7 : R) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  unfold cyclotomicSeven at hΦ
  ext i j
  fin_cases i <;> fin_cases j <;>
    (rw [Matrix.mul_apply, Fin.sum_univ_three, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul];
     dsimp [blichfeldtRawS])
  · linear_combination (ζ ^ 6 - ζ ^ 5 + ζ ^ 4 - ζ ^ 3 + ζ ^ 2 - 7 * ζ + 7) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 6 - ζ ^ 5 + ζ ^ 4 - ζ ^ 3 + ζ ^ 2 - 7 * ζ + 7) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 5 - 2 * ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 6 - ζ ^ 5 + ζ ^ 4 - ζ ^ 3 + ζ ^ 2 - 7 * ζ + 7) * hΦ

/-- Determinant of the unscaled matrix `blichfeldtRawS ζ` equals `7 * gaussSeven ζ`. -/
theorem det_blichfeldtRawS {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    (blichfeldtRawS ζ).det = 7 * gaussSeven ζ := by
  unfold cyclotomicSeven at hΦ
  rw [Matrix.det_fin_three]
  dsimp [blichfeldtRawS, gaussSeven]
  linear_combination
    (ζ ^ 12 - ζ ^ 11 + 4 * ζ ^ 9 - 7 * ζ ^ 8 - 4 * ζ ^ 6 +
     14 * ζ ^ 5 - 13 * ζ ^ 4 + 13 * ζ ^ 3 - 7 * ζ) * hΦ

/-- Unscaled intertwining identity `rawS * T * rawS = (- gaussSeven ζ) • (T⁻¹ * rawS * T⁻¹)`. -/
theorem blichfeldtRawS_T_RawS {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    blichfeldtRawS ζ * blichfeldtT ζ * blichfeldtRawS ζ =
      (-gaussSeven ζ) • (blichfeldtTInv ζ * blichfeldtRawS ζ * blichfeldtTInv ζ) := by
  unfold cyclotomicSeven at hΦ
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [blichfeldtRawS, blichfeldtT, blichfeldtTInv, gaussSeven,
      Matrix.mul_apply, Fin.sum_univ_three, Matrix.smul_apply, smul_eq_mul, Fin.isValue]
  · linear_combination (ζ ^ 17 - 2 * ζ ^ 15 + ζ ^ 14 - 2 * ζ ^ 13 + 2 * ζ ^ 12 -
      ζ ^ 11 + 3 * ζ ^ 10 - 2 * ζ ^ 8 - ζ ^ 6 + ζ ^ 4) * hΦ
  · linear_combination (ζ ^ 17 - 2 * ζ ^ 15 + 2 * ζ ^ 14 - 2 * ζ ^ 13 - ζ ^ 12 +
      ζ ^ 11 + 3 * ζ ^ 10 - 2 * ζ ^ 9 + ζ ^ 7 - ζ ^ 6 - ζ ^ 5 + ζ ^ 4) * hΦ
  · linear_combination (-ζ ^ 13 + ζ ^ 12 + 2 * ζ ^ 11 - 4 * ζ ^ 10 + 4 * ζ ^ 9 -
      3 * ζ ^ 8 + 2 * ζ ^ 7 - 2 * ζ ^ 6 + ζ ^ 5) * hΦ
  · linear_combination (ζ ^ 17 - 2 * ζ ^ 15 + 2 * ζ ^ 14 - 2 * ζ ^ 13 - ζ ^ 12 +
      ζ ^ 11 + 3 * ζ ^ 10 - 2 * ζ ^ 9 + ζ ^ 7 - ζ ^ 6 - ζ ^ 5 + ζ ^ 4) * hΦ
  · linear_combination (-ζ ^ 14 + ζ ^ 13 + 2 * ζ ^ 12 - 4 * ζ ^ 11 + 4 * ζ ^ 10 -
      2 * ζ ^ 9 - ζ ^ 4 + ζ ^ 3) * hΦ
  · linear_combination (ζ ^ 13 - 2 * ζ ^ 11 + ζ ^ 10 - ζ ^ 9 + ζ ^ 8 - ζ ^ 7 +
      2 * ζ ^ 6 - ζ ^ 5) * hΦ
  · linear_combination (-ζ ^ 13 + ζ ^ 12 + 2 * ζ ^ 11 - 4 * ζ ^ 10 + 4 * ζ ^ 9 -
      3 * ζ ^ 8 + 2 * ζ ^ 7 - 2 * ζ ^ 6 + ζ ^ 5) * hΦ
  · linear_combination (ζ ^ 13 - 2 * ζ ^ 11 + ζ ^ 10 - ζ ^ 9 + ζ ^ 8 - ζ ^ 7 +
      2 * ζ ^ 6 - ζ ^ 5) * hΦ
  · linear_combination (ζ ^ 12 - ζ ^ 10 + ζ ^ 9 - 2 * ζ ^ 8 - ζ ^ 7 + 2 * ζ ^ 6) * hΦ

/-- **Unimodularity and Order-7 Relations for $T(\zeta)$:**
    $\det T(\zeta) = 1$, $T(\zeta) \cdot T(\zeta)^{-1} = I_3$, and $T(\zeta)^7 = I_3$. -/
theorem blichfeldtT_properties {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    (blichfeldtT ζ).det = 1 ∧
    blichfeldtT ζ * blichfeldtTInv ζ = 1 ∧
    blichfeldtTInv ζ * blichfeldtT ζ = 1 ∧
    (blichfeldtT ζ) ^ 7 = 1 := by
  have h7 := zeta_pow_seven_eq_one hΦ
  let T2 : Matrix (Fin 3) (Fin 3) R :=
    fun i j => match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 2 | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 4 | ⟨2, _⟩, ⟨2, _⟩ => ζ | _, _ => 0
  let T4 : Matrix (Fin 3) (Fin 3) R :=
    fun i j => match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 4 | ⟨1, _⟩, ⟨1, _⟩ => ζ | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 2 | _, _ => 0
  have hT2 : (blichfeldtT ζ) ^ 2 = T2 := by
    rw [sq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [blichfeldtT, T2])
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · linear_combination ζ * h7
  have hT4 : (blichfeldtT ζ) ^ 4 = T4 := by
    have h42 : (blichfeldtT ζ) ^ 4 = (blichfeldtT ζ) ^ 2 * (blichfeldtT ζ) ^ 2 := by
      simp [pow_succ, pow_zero, mul_assoc]
    rw [h42, hT2]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [T2, T4])
    · ring
    · ring
    · ring
    · ring
    · linear_combination ζ * h7
    · ring
    · ring
    · ring
    · ring
  have hT6 : (blichfeldtT ζ) ^ 6 = blichfeldtTInv ζ := by
    have h642 : (blichfeldtT ζ) ^ 6 = (blichfeldtT ζ) ^ 4 * (blichfeldtT ζ) ^ 2 := by
      simp [pow_succ, pow_zero, mul_assoc]
    rw [h642, hT4, hT2]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [T4, T2, blichfeldtTInv]; ring)
  have hT_TInv : blichfeldtT ζ * blichfeldtTInv ζ = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply];
       dsimp [blichfeldtT, blichfeldtTInv])
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
  have hTInv_T : blichfeldtTInv ζ * blichfeldtT ζ = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply];
       dsimp [blichfeldtT, blichfeldtTInv])
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
  refine ⟨?_, hT_TInv, hTInv_T, ?_⟩
  · rw [Matrix.det_fin_three]
    dsimp [blichfeldtT]
    linear_combination h7
  · calc (blichfeldtT ζ) ^ 7
        = blichfeldtT ζ * (blichfeldtT ζ) ^ 6 := by simp [pow_succ, pow_zero, mul_assoc]
      _ = blichfeldtT ζ * blichfeldtTInv ζ := by rw [hT6]
      _ = 1 := hT_TInv

/-- **Unimodularity and Frobenius $C_7 \rtimes C_3$ Relations for $R$:**
    $\det R = 1$, $R^3 = I_3$, $R^T R = I_3$, and $R T(\zeta) R^T = T(\zeta)^2$. -/
theorem blichfeldtR_properties {R : Type*} [CommRing R] {ζ : R}
    (hΦ : cyclotomicSeven ζ = 0) :
    (blichfeldtR (R := R)).det = 1 ∧
    (blichfeldtR (R := R)) ^ 3 = 1 ∧
    (blichfeldtR (R := R)).transpose * blichfeldtR = 1 ∧
    blichfeldtR * blichfeldtT ζ * blichfeldtR.transpose = (blichfeldtT ζ) ^ 2 := by
  have h7 := zeta_pow_seven_eq_one hΦ
  have hR_orth : (blichfeldtR (R := R)).transpose * blichfeldtR = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply];
       dsimp [blichfeldtR, Matrix.transpose_apply];
       ring)
  have hR2 : (blichfeldtR (R := R)) * blichfeldtR = blichfeldtR.transpose := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three];
       dsimp [blichfeldtR, Matrix.transpose_apply];
       ring)
  let RT : Matrix (Fin 3) (Fin 3) R :=
    fun i j => match i, j with
      | ⟨0, _⟩, ⟨1, _⟩ => ζ ^ 2 | ⟨1, _⟩, ⟨2, _⟩ => ζ ^ 4 | ⟨2, _⟩, ⟨0, _⟩ => ζ | _, _ => 0
  have hRT : blichfeldtR * blichfeldtT ζ = RT := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [blichfeldtR, blichfeldtT, RT]; ring)
  let T2 : Matrix (Fin 3) (Fin 3) R :=
    fun i j => match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 2 | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 4 | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 8 | _, _ => 0
  have hT2 : (blichfeldtT ζ) ^ 2 = T2 := by
    rw [sq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [blichfeldtT, T2]; ring)
  refine ⟨?_, ?_, hR_orth, ?_⟩
  · rw [Matrix.det_fin_three]
    dsimp [blichfeldtR]
    ring
  · calc (blichfeldtR (R := R)) ^ 3
        = (blichfeldtR * blichfeldtR) * blichfeldtR := by simp [pow_succ, pow_zero, mul_assoc]
      _ = blichfeldtR.transpose * blichfeldtR := by rw [hR2]
      _ = 1 := hR_orth
  · rw [hRT, hT2]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [RT, T2, blichfeldtR, Matrix.transpose_apply])
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · linear_combination -ζ * h7

/-- **Involution, Unimodularity, Trace, and Symmetry of $S(\zeta, s) \in \mathrm{SL}(3, R)$:**
    $S^T = S$, $S^2 = I_3$, $\det S = 1$, $\mathrm{tr}(S) = -1$, and $(S R)^2 = I_3$. -/
theorem blichfeldtS_properties {R : Type*} [CommRing R] {ζ s : R}
    (hΦ : cyclotomicSeven ζ = 0) (hs : s * gaussSeven ζ = 1) :
    (blichfeldtS ζ s).transpose = blichfeldtS ζ s ∧
    (blichfeldtS ζ s) ^ 2 = 1 ∧
    (blichfeldtS ζ s).det = 1 ∧
    (blichfeldtS ζ s).trace = -1 ∧
    (blichfeldtS ζ s * blichfeldtR) ^ 2 = 1 := by
  have hs2 := neg_seven_mul_s_sq_eq_one hΦ hs
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;> rfl
  · rw [sq, blichfeldtS, Matrix.smul_mul, Matrix.mul_smul, smul_smul,
      blichfeldtRawS_sq_eq_neg_seven hΦ, smul_smul]
    have hcoeff : (-s) * (-s) * (-7) = 1 := by linear_combination hs2
    rw [hcoeff, one_smul]
  · rw [blichfeldtS, Matrix.det_smul, Fintype.card_fin, det_blichfeldtRawS hΦ]
    calc (-s) ^ 3 * (7 * gaussSeven ζ)
        = (-7 * s ^ 2) * (s * gaussSeven ζ) := by ring
      _ = 1 * 1 := by rw [hs2, hs]
      _ = 1 := one_mul 1
  · simp only [blichfeldtS, Matrix.trace, Matrix.diag, Fin.sum_univ_three,
      Matrix.smul_apply, smul_eq_mul]
    dsimp [blichfeldtRawS]
    calc -s * (ζ ^ 2 - ζ ^ 5) + -s * (ζ ^ 4 - ζ ^ 3) + -s * (ζ - ζ ^ 6)
        = -(s * gaussSeven ζ) := by unfold gaussSeven; ring
      _ = -1 := by rw [hs]
  · have hSR : blichfeldtRawS ζ * blichfeldtR * blichfeldtRawS ζ * blichfeldtR =
        blichfeldtRawS ζ * blichfeldtRawS ζ := by
      ext i j
      fin_cases i <;> fin_cases j <;>
        (simp only [blichfeldtRawS, blichfeldtR, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue];
         ring)
    rw [sq, blichfeldtS]
    calc ((-s) • blichfeldtRawS ζ * blichfeldtR) * ((-s) • blichfeldtRawS ζ * blichfeldtR)
        = ((-s) * (-s)) • (blichfeldtRawS ζ * blichfeldtR * blichfeldtRawS ζ * blichfeldtR) := by
            rw [Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
            simp only [mul_assoc]
      _ = (s ^ 2) • ((-7 : R) • (1 : Matrix (Fin 3) (Fin 3) R)) := by
            rw [hSR, blichfeldtRawS_sq_eq_neg_seven hΦ]
            congr 1; ring
      _ = (1 : Matrix (Fin 3) (Fin 3) R) := by
            rw [smul_smul]
            have hcoeff : s ^ 2 * (-7) = 1 := by linear_combination hs2
            rw [hcoeff, one_smul]

/-- **Hurwitz $(2, 3, 7)$ Relation `(S * T)³ = I₃` over any `CommRing R`:**
    Together with $S^2 = I_3$ and $T^7 = I_3$, $(S(\zeta, s) \cdot T(\zeta))^3 = I_3$. -/
theorem blichfeldtS_mul_T_cubed_eq_one {R : Type*} [CommRing R] {ζ s : R}
    (hΦ : cyclotomicSeven ζ = 0) (hs : s * gaussSeven ζ = 1) :
    (blichfeldtS ζ s * blichfeldtT ζ) ^ 3 = 1 := by
  have hSTS : blichfeldtS ζ s * blichfeldtT ζ * blichfeldtS ζ s =
      blichfeldtTInv ζ * blichfeldtS ζ s * blichfeldtTInv ζ := by
    unfold blichfeldtS
    calc ((-s) • blichfeldtRawS ζ) * blichfeldtT ζ * ((-s) • blichfeldtRawS ζ)
        = ((-s) * (-s)) • (blichfeldtRawS ζ * blichfeldtT ζ * blichfeldtRawS ζ) := by
            rw [Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
      _ = (s ^ 2) • ((-gaussSeven ζ) • (blichfeldtTInv ζ * blichfeldtRawS ζ * blichfeldtTInv ζ)) := by
            rw [blichfeldtRawS_T_RawS hΦ]
            congr 1; ring
      _ = (-s) • (blichfeldtTInv ζ * blichfeldtRawS ζ * blichfeldtTInv ζ) := by
            rw [smul_smul]
            have hsc : s ^ 2 * (-gaussSeven ζ) = -s := by
              calc s ^ 2 * (-gaussSeven ζ) = -s * (s * gaussSeven ζ) := by ring
                _ = -s * 1 := by rw [hs]
                _ = -s := mul_one _
            rw [hsc]
      _ = blichfeldtTInv ζ * ((-s) • blichfeldtRawS ζ) * blichfeldtTInv ζ := by
            rw [Matrix.mul_smul, Matrix.smul_mul]
  have hT := blichfeldtT_properties hΦ
  have hS2 : blichfeldtS ζ s * blichfeldtS ζ s = 1 := by
    simpa [sq] using (blichfeldtS_properties hΦ hs).2.1
  calc (blichfeldtS ζ s * blichfeldtT ζ) ^ 3
      = (blichfeldtS ζ s * blichfeldtT ζ * blichfeldtS ζ s) *
          (blichfeldtT ζ * blichfeldtS ζ s * blichfeldtT ζ) := by
          simp [pow_succ, pow_zero, mul_assoc]
    _ = (blichfeldtTInv ζ * blichfeldtS ζ s * blichfeldtTInv ζ) *
          (blichfeldtT ζ * blichfeldtS ζ s * blichfeldtT ζ) := by rw [hSTS]
    _ = blichfeldtTInv ζ * blichfeldtS ζ s * (blichfeldtTInv ζ * blichfeldtT ζ) *
          blichfeldtS ζ s * blichfeldtT ζ := by simp [mul_assoc]
    _ = blichfeldtTInv ζ * (blichfeldtS ζ s * blichfeldtS ζ s) * blichfeldtT ζ := by
          rw [hT.2.2.1]; simp [mul_assoc]
    _ = blichfeldtTInv ζ * blichfeldtT ζ := by rw [hS2, mul_one]
    _ = 1 := hT.2.2.1

/-- **Dyck's Fourth Relation `(S * T³)⁴ = I₃` Completing the Presentation of $\mathrm{PSL}(2, 7)$:**
    $\langle S, T \mid S^2 = T^7 = (ST)^3 = (S T^3)^4 = 1 \rangle \cong \mathrm{PSL}(2, 7)$ of order $168$. -/
theorem blichfeldtS_mul_T_pow_three_pow_four_eq_one {R : Type*} [CommRing R] {ζ s : R}
    (hΦ : cyclotomicSeven ζ = 0) (hs : s * gaussSeven ζ = 1) :
    (blichfeldtS ζ s * (blichfeldtT ζ) ^ 3) ^ 4 = 1 := by
  have h7 := zeta_pow_seven_eq_one hΦ
  let T3 : Matrix (Fin 3) (Fin 3) R :=
    fun i j =>
      match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 3
      | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 6
      | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 5
      | _, _ => 0
  let T4 : Matrix (Fin 3) (Fin 3) R :=
    fun i j =>
      match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 4
      | ⟨1, _⟩, ⟨1, _⟩ => ζ
      | ⟨2, _⟩, ⟨2, _⟩ => ζ ^ 2
      | _, _ => 0
  let T2 : Matrix (Fin 3) (Fin 3) R :=
    fun i j =>
      match i, j with
      | ⟨0, _⟩, ⟨0, _⟩ => ζ ^ 2
      | ⟨1, _⟩, ⟨1, _⟩ => ζ ^ 4
      | ⟨2, _⟩, ⟨2, _⟩ => ζ
      | _, _ => 0
  have hT2 : (blichfeldtT ζ) ^ 2 = T2 := by
    rw [sq]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [blichfeldtT, T2])
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · ring
    · linear_combination ζ * h7
  have hT3 : (blichfeldtT ζ) ^ 3 = T3 := by
    have h32 : (blichfeldtT ζ) ^ 3 = (blichfeldtT ζ) ^ 2 * blichfeldtT ζ := by
      simp [pow_succ, pow_zero, mul_assoc]
    rw [h32, hT2]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three]; dsimp [T2, blichfeldtT, T3];
       ring)
  have hT4T3 : T4 * T3 = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply];
       dsimp [T3, T4])
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
    · ring
    · ring
    · ring
    · linear_combination h7
  have hRawSwap : blichfeldtRawS ζ * T3 * (blichfeldtRawS ζ * T3) =
      T4 * blichfeldtRawS ζ * (T4 * blichfeldtRawS ζ) := by
    have hΦ' := hΦ
    unfold cyclotomicSeven at hΦ'
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp only [blichfeldtRawS, T3, T4, Matrix.mul_apply, Fin.sum_univ_three, Fin.isValue]
    · linear_combination (ζ ^ 15 - ζ ^ 14 - ζ ^ 12 + ζ ^ 10 + ζ ^ 8 - ζ ^ 7) * hΦ'
    · linear_combination (-ζ ^ 16 + 2 * ζ ^ 15 - ζ ^ 14 + ζ ^ 11 - 2 * ζ ^ 10 + ζ ^ 9) * hΦ'
    · linear_combination (ζ ^ 16 - ζ ^ 15 - ζ ^ 14 + ζ ^ 13 - ζ ^ 11 + ζ ^ 10 + ζ ^ 9 - ζ ^ 8) * hΦ'
    · linear_combination (-ζ ^ 13 + 2 * ζ ^ 12 - ζ ^ 11 + ζ ^ 8 - 2 * ζ ^ 7 + ζ ^ 6) * hΦ'
    · linear_combination (2 * ζ ^ 15 - ζ ^ 14 - 3 * ζ ^ 13 + ζ ^ 12 - ζ ^ 10 + 3 * ζ ^ 9 + ζ ^ 8 - 2 * ζ ^ 7) * hΦ'
    · linear_combination (ζ ^ 15 - 2 * ζ ^ 14 + 2 * ζ ^ 13 - 3 * ζ ^ 12 + 4 * ζ ^ 11 - 4 * ζ ^ 10 + 3 * ζ ^ 9 - 2 * ζ ^ 8 + 2 * ζ ^ 7 - ζ ^ 6) * hΦ'
    · linear_combination (ζ ^ 14 - ζ ^ 13 - ζ ^ 12 + ζ ^ 11 - ζ ^ 9 + ζ ^ 8 + ζ ^ 7 - ζ ^ 6) * hΦ'
    · linear_combination (ζ ^ 16 - 2 * ζ ^ 15 + 2 * ζ ^ 14 - 3 * ζ ^ 13 + 4 * ζ ^ 12 - 4 * ζ ^ 11 + 3 * ζ ^ 10 - 2 * ζ ^ 9 + 2 * ζ ^ 8 - ζ ^ 7) * hΦ'
    · linear_combination (ζ ^ 16 - ζ ^ 14 - 2 * ζ ^ 12 + 2 * ζ ^ 10 + ζ ^ 8 - ζ ^ 6) * hΦ'
  have hSwap : blichfeldtS ζ s * T3 * (blichfeldtS ζ s * T3) =
      T4 * blichfeldtS ζ s * (T4 * blichfeldtS ζ s) := by
    unfold blichfeldtS
    calc ((-s) • blichfeldtRawS ζ * T3) * ((-s) • blichfeldtRawS ζ * T3)
        = ((-s) * (-s)) • (blichfeldtRawS ζ * T3 * (blichfeldtRawS ζ * T3)) := by
            rw [Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
      _ = ((-s) * (-s)) • (T4 * blichfeldtRawS ζ * (T4 * blichfeldtRawS ζ)) := by
            rw [hRawSwap]
      _ = (T4 * (-s) • blichfeldtRawS ζ) * (T4 * (-s) • blichfeldtRawS ζ) := by
            rw [Matrix.mul_smul, Matrix.mul_smul, Matrix.smul_mul, smul_smul]
  have hS2 : blichfeldtS ζ s * blichfeldtS ζ s = 1 := by
    simpa [sq] using (blichfeldtS_properties hΦ hs).2.1
  rw [hT3]
  calc (blichfeldtS ζ s * T3) ^ 4
      = (blichfeldtS ζ s * T3 * (blichfeldtS ζ s * T3)) *
          (blichfeldtS ζ s * T3 * (blichfeldtS ζ s * T3)) := by
          simp [pow_succ, pow_zero, mul_assoc]
    _ = (T4 * blichfeldtS ζ s * (T4 * blichfeldtS ζ s)) *
          (blichfeldtS ζ s * T3 * (blichfeldtS ζ s * T3)) := by rw [hSwap]
    _ = T4 * blichfeldtS ζ s * T4 * (blichfeldtS ζ s * blichfeldtS ζ s) *
          T3 * blichfeldtS ζ s * T3 := by simp [mul_assoc]
    _ = T4 * blichfeldtS ζ s * (T4 * T3) * blichfeldtS ζ s * T3 := by
          rw [hS2]; simp [mul_assoc]
    _ = T4 * (blichfeldtS ζ s * blichfeldtS ζ s) * T3 := by
          rw [hT4T3]; simp [mul_assoc]
    _ = T4 * T3 := by rw [hS2, mul_one]
    _ = 1 := hT4T3

-- ============================================================================
-- §4B. Concrete Instantiation Over ℂ: Blichfeldt Group Inside SU(3)
-- ============================================================================

/-- Canonical primitive 7th root of unity $\zeta_7 = \exp(2\pi i / 7) \in \mathbb{C}$. -/
noncomputable def zetaSevenC : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 7)

/-- Concrete Gauss-sum inverse $s_7 = g(\zeta_7)^{-1} \in \mathbb{C}$. -/
noncomputable def sSevenC : ℂ :=
  (gaussSeven zetaSevenC)⁻¹

/-- `zetaSevenC` is a primitive 7th root of unity in `ℂ`. -/
theorem isPrimitiveRoot_zetaSevenC : IsPrimitiveRoot zetaSevenC 7 := by
  simpa [zetaSevenC, mul_div_assoc] using Complex.isPrimitiveRoot_exp 7 (by decide : (7 : ℕ) ≠ 0)

/-- **Concrete Cyclotomic Vanishing over `ℂ`:** $\Phi_7(\zeta_7) = 0$. -/
theorem cyclotomicSeven_zetaSevenC : cyclotomicSeven zetaSevenC = 0 := by
  have hprim := isPrimitiveRoot_zetaSevenC
  have h7 : zetaSevenC ^ 7 = 1 := hprim.pow_eq_one
  have hne1 : zetaSevenC ≠ 1 := hprim.ne_one (by decide : 1 < 7)
  have hfac : (zetaSevenC - 1) * cyclotomicSeven zetaSevenC = 0 := by
    unfold cyclotomicSeven
    calc (zetaSevenC - 1) *
          (1 + zetaSevenC + zetaSevenC ^ 2 + zetaSevenC ^ 3 + zetaSevenC ^ 4 +
            zetaSevenC ^ 5 + zetaSevenC ^ 6)
        = zetaSevenC ^ 7 - 1 := by ring
      _ = 0 := sub_eq_zero.mpr h7
  exact (mul_eq_zero.mp hfac).resolve_left (sub_ne_zero.mpr hne1)

/-- **Concrete Gauss-Sum Inverse Identity over `ℂ`:** $s_7 \cdot g(\zeta_7) = 1$. -/
theorem sSevenC_mul_gaussSeven : sSevenC * gaussSeven zetaSevenC = 1 := by
  unfold sSevenC
  have hg2 : (gaussSeven zetaSevenC) ^ 2 = -7 :=
    gaussSeven_sq_eq_neg_seven cyclotomicSeven_zetaSevenC
  have hne : gaussSeven zetaSevenC ≠ 0 := by
    intro h0
    rw [h0] at hg2
    norm_num at hg2
  exact inv_mul_cancel₀ hne

/-- Complex conjugation maps $\zeta_7 = \exp(2\pi i / 7)$ to $\zeta_7^{-1} = \zeta_7^6$. -/
theorem star_zetaSevenC_eq_pow_six : star zetaSevenC = zetaSevenC ^ 6 := by
  have h7 : zetaSevenC ^ 7 = 1 := zeta_pow_seven_eq_one cyclotomicSeven_zetaSevenC
  have hconj : star zetaSevenC = Complex.exp (-(2 * Real.pi * Complex.I / 7)) := by
    unfold zetaSevenC
    rw [Complex.star_def, ← Complex.exp_conj]
    congr 1
    simp [Complex.conj_ofReal, map_ofNat]
    ring
  have hmul : Complex.exp (-(2 * Real.pi * Complex.I / 7)) * zetaSevenC = 1 := by
    unfold zetaSevenC
    rw [← Complex.exp_add]
    simp
  have hpow : zetaSevenC ^ 6 * zetaSevenC = 1 := by
    calc zetaSevenC ^ 6 * zetaSevenC = zetaSevenC ^ 7 := by ring
      _ = 1 := h7
  have hne : zetaSevenC ≠ 0 := by
    intro hz
    rw [hz] at hpow
    norm_num at hpow
  rw [hconj]
  exact mul_right_cancel₀ hne (hmul.trans hpow.symm)

/-- Conjugate powers $\overline{\zeta_7^k} = \zeta_7^{7 - k}$ for $k = 1, \dots, 6$. -/
theorem star_zetaSevenC_powers :
    star (zetaSevenC ^ 2) = zetaSevenC ^ 5 ∧
    star (zetaSevenC ^ 3) = zetaSevenC ^ 4 ∧
    star (zetaSevenC ^ 4) = zetaSevenC ^ 3 ∧
    star (zetaSevenC ^ 5) = zetaSevenC ^ 2 ∧
    star (zetaSevenC ^ 6) = zetaSevenC := by
  have h7 : zetaSevenC ^ 7 = 1 := zeta_pow_seven_eq_one cyclotomicSeven_zetaSevenC
  simp only [star_pow, star_zetaSevenC_eq_pow_six]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · linear_combination zetaSevenC ^ 5 * h7
  · linear_combination (zetaSevenC ^ 11 + zetaSevenC ^ 4) * h7
  · linear_combination (zetaSevenC ^ 17 + zetaSevenC ^ 10 + zetaSevenC ^ 3) * h7
  · linear_combination (zetaSevenC ^ 23 + zetaSevenC ^ 16 + zetaSevenC ^ 9 + zetaSevenC ^ 2) * h7
  · linear_combination (zetaSevenC ^ 29 + zetaSevenC ^ 22 + zetaSevenC ^ 15 + zetaSevenC ^ 8 + zetaSevenC) * h7

/-- Complex conjugation negates the purely imaginary Gauss sum $g(\zeta_7)$, and hence negates $s_7$. -/
theorem star_sSevenC_eq_neg : star sSevenC = -sSevenC := by
  rcases star_zetaSevenC_powers with ⟨h2, h3, h4, h5, h6⟩
  have hstar_g : star (gaussSeven zetaSevenC) = -gaussSeven zetaSevenC := by
    unfold gaussSeven
    simp only [star_sub, star_add]
    rw [star_zetaSevenC_eq_pow_six, h2, h3, h4, h5, h6]
    ring
  unfold sSevenC
  rw [Complex.star_def, map_inv₀, ← Complex.star_def, hstar_g, inv_neg]

/-- **Concrete Unitary $\mathrm{SU}(3)$ Embedding of the Blichfeldt Generators over $\mathbb{C}$:**
    All three generators $T(\zeta_7), R, S(\zeta_7, s_7) \in M_3(\mathbb{C})$ satisfy
    $M^\dagger M = I_3$ (`conjTranspose M * M = 1`), $\det M = 1$, and the complete Dyck $(2, 3, 7; 4)$
    presentation of $\mathrm{PSL}(2, 7)$. -/
theorem blichfeldt_complex_su3_embedding :
    (blichfeldtT zetaSevenC).conjTranspose * blichfeldtT zetaSevenC = 1 ∧
    (blichfeldtT zetaSevenC).det = 1 ∧
    (blichfeldtR (R := ℂ)).conjTranspose * blichfeldtR = 1 ∧
    (blichfeldtR (R := ℂ)).det = 1 ∧
    (blichfeldtS zetaSevenC sSevenC).conjTranspose * blichfeldtS zetaSevenC sSevenC = 1 ∧
    (blichfeldtS zetaSevenC sSevenC).det = 1 ∧
    (blichfeldtS zetaSevenC sSevenC) ^ 2 = 1 ∧
    (blichfeldtT zetaSevenC) ^ 7 = 1 ∧
    (blichfeldtS zetaSevenC sSevenC * blichfeldtT zetaSevenC) ^ 3 = 1 ∧
    (blichfeldtS zetaSevenC sSevenC * (blichfeldtT zetaSevenC) ^ 3) ^ 4 = 1 := by
  have hΦ := cyclotomicSeven_zetaSevenC
  have hs := sSevenC_mul_gaussSeven
  rcases star_zetaSevenC_powers with ⟨h2, h3, h4, h5, h6⟩
  have hT := blichfeldtT_properties hΦ
  have hR := blichfeldtR_properties hΦ
  have hS := blichfeldtS_properties hΦ hs
  have hconjT : (blichfeldtT zetaSevenC).conjTranspose = blichfeldtTInv zetaSevenC := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.conjTranspose_apply];
       dsimp [blichfeldtT, blichfeldtTInv];
       rw [← Complex.star_def])
    · exact star_zetaSevenC_eq_pow_six
    · exact star_zero ℂ
    · exact star_zero ℂ
    · exact star_zero ℂ
    · exact h2
    · exact star_zero ℂ
    · exact star_zero ℂ
    · exact star_zero ℂ
    · exact h4
  have hconjR : (blichfeldtR (R := ℂ)).conjTranspose = blichfeldtR.transpose := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.conjTranspose_apply, Matrix.transpose_apply];
       dsimp [blichfeldtR];
       rw [← Complex.star_def];
       first | exact star_zero ℂ | exact star_one ℂ)
  have hconjRawS : (blichfeldtRawS zetaSevenC).conjTranspose = -blichfeldtRawS zetaSevenC := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      (rw [Matrix.conjTranspose_apply, Matrix.neg_apply];
       dsimp [blichfeldtRawS];
       rw [← Complex.star_def, star_sub];
       simp only [star_zetaSevenC_eq_pow_six, h2, h3, h4, h5, h6];
       ring)
  have hconjS : (blichfeldtS zetaSevenC sSevenC).conjTranspose = blichfeldtS zetaSevenC sSevenC := by
    unfold blichfeldtS
    rw [Matrix.conjTranspose_smul, star_neg, star_sSevenC_eq_neg, neg_neg, hconjRawS,
      smul_neg, neg_smul]
  refine ⟨?_, hT.1, ?_, hR.1, ?_, hS.2.2.1, hS.2.1, hT.2.2.2,
    blichfeldtS_mul_T_cubed_eq_one hΦ hs, blichfeldtS_mul_T_pow_three_pow_four_eq_one hΦ hs⟩
  · rw [hconjT]; exact hT.2.2.1
  · rw [hconjR]; exact hR.2.2.1
  · rw [hconjS, ← sq]; exact hS.2.1

end QOU.Eightfold.BringGenusThreeFanoOctonionAndBlichfeldtSU3
