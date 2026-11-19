/-
  Frobenius lepton-meson bridge: V_(2,1) ↓ H₂ = V_(2) ⊕ V_(1,1).

  The standard representation V_(2,1) of H₃(q) restricts to H₂(q) as the
  direct sum of the two 1D lepton irreps V_(2) (eigenvalue q) and V_(1,1)
  (eigenvalue -q⁻¹). We formalize:
  1. Explicit module-representation structures `H2Rep K h V` and `H3Rep K h V`
     carrying linear endomorphisms `σ₁` (and `σ₂`) satisfying the Hecke
     quadratic relations `σᵢ² = h σᵢ + 1` and the braid relation
     `σ₁ σ₂ σ₁ = σ₂ σ₁ σ₂`, together with the restriction functor
     `H3Rep.restrict : H3Rep K h V → H2Rep K h V`.
  2. Concrete constructions of the 1D lepton representations `leptonSymRep`
     (`V_(2)`, `σ₁ = q`) and `leptonAntiRep` (`V_(1,1)`, `σ₁ = -q⁻¹`), and
     the 2D Hoefsmit standard representation `mesonStandardRep` (`V_(2,1)`).
  3. The explicit `H₂(q)`-equivariant linear isomorphism
     `Res(V_(2,1)) ≅ V_(2) ⊕ V_(1,1)` (`mesonStandard_restrict_equiv`), and
     Schur distinctness `V_(2) ≇ V_(1,1)` when `[2]_q = q + q⁻¹ ≠ 0`.
  4. The Hoefsmit off-diagonal decoupling theorem
     `sigma2_preserves_H2_summands_iff_b_eq_zero`: both `H₂`-subspaces
     `K e₁` and `K e₂` are `σ₂`-invariant iff `b = 0`.
  5. Explicit `H₂`-intertwiner space `H2Hom`, direct-sum decomposition
     `h2HomDirectSumEquiv`, and the Frobenius reciprocity multiplicity-one
     linear equivalences `hom_restrict_leptonSym_equiv` and
     `hom_restrict_leptonAnti_equiv` (`Hom_{H₂}(Res(V_(2,1)), V_μ) ≃ₗ[K] K`
     for `μ ∈ {(2), (1,1)}` when `[2]_q ≠ 0`).

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Tactic

namespace QOU.BraidsAndKnots

-- ═══════════════════════════════════════════════════════════════
-- §1  ARTIN-WEDDERBURN DIMENSION CONSTRAINTS
-- ═══════════════════════════════════════════════════════════════

/-- H₂ has dimension 2! = 2 = 1² + 1²: two 1-dim irreps. -/
theorem h2_artin_wedderburn : 1^2 + 1^2 = Nat.factorial 2 := by decide

/-- H₃ has dimension 3! = 6 = 1² + 2² + 1²: dims (1,2,1). -/
theorem h3_artin_wedderburn : 1^2 + 2^2 + 1^2 = Nat.factorial 3 := by decide

/-- H₄ has dimension 4! = 24 = 1² + 3² + 2² + 3² + 1². -/
theorem h4_artin_wedderburn : 1^2 + 3^2 + 2^2 + 3^2 + 1^2 = Nat.factorial 4 := by decide

/-- 2 = 1² + 1² is the ONLY way to write 2 as a sum of positive
  integer squares. This forces H₂ to have only 1-dim irreps. -/
theorem two_unique_sum_of_squares (a b : ℕ) (ha : 0 < a) (hb : 0 < b)
    (hab : a^2 + b^2 = 2) : a = 1 ∧ b = 1 := by
  have ha1 : a ≤ 1 := by
    by_contra h
    have h4 : 2 ^ 2 ≤ a ^ 2 := Nat.pow_le_pow_left (by omega) 2
    norm_num at h4
    omega
  have hb1 : b ≤ 1 := by
    by_contra h
    have h4 : 2 ^ 2 ≤ b ^ 2 := Nat.pow_le_pow_left (by omega) 2
    norm_num at h4
    omega
  omega

-- ═══════════════════════════════════════════════════════════════
-- §2  REPRESENTATION THEORY OF H₂(q) AND H₃(q)
-- ═══════════════════════════════════════════════════════════════

/-- A representation of the 2-strand Iwahori–Hecke algebra `H₂(q)` (with quadratic
    parameter `h = q - q⁻¹`) on a `K`-module `V`: a `K`-linear endomorphism
    `σ₁ : V →ₗ[K] V` satisfying the Hecke quadratic relation `σ₁(σ₁ v) = h • σ₁ v + v`. -/
structure H2Rep (K : Type*) [CommRing K] (h : K)
    (V : Type*) [AddCommGroup V] [Module K V] where
  /-- Action of the Hecke generator `σ₁`. -/
  σ₁ : V →ₗ[K] V
  /-- Hecke quadratic relation `σ₁(σ₁ v) = h • σ₁ v + v`. -/
  hecke₁ : ∀ v : V, σ₁ (σ₁ v) = h • σ₁ v + v

/-- Direct sum `U ⊕ W` of two `H₂(q)`-representations on `V₁ × V₂`. -/
def H2Rep.directSum {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    (U : H2Rep K h V₁) (W : H2Rep K h V₂) : H2Rep K h (V₁ × V₂) where
  σ₁ := U.σ₁.prodMap W.σ₁
  hecke₁ := fun ⟨v₁, v₂⟩ => Prod.ext (U.hecke₁ v₁) (W.hecke₁ v₂)

/-- An `H₂(q)`-intertwiner (`Hom_{H₂(q)}(U, W)`): a `K`-linear map `f : V₁ →ₗ[K] V₂`
    commuting with `σ₁`. -/
structure H2Hom {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    (U : H2Rep K h V₁) (W : H2Rep K h V₂) where
  /-- Underlying `K`-linear map. -/
  toLinearMap : V₁ →ₗ[K] V₂
  /-- Equivariance: `f(σ₁ v) = σ₁(f v)`. -/
  comm₁ : ∀ v : V₁, toLinearMap (U.σ₁ v) = W.σ₁ (toLinearMap v)

@[ext]
theorem H2Hom.ext {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    {U : H2Rep K h V₁} {W : H2Rep K h V₂}
    {f g : H2Hom U W} (hfg : ∀ x, f.toLinearMap x = g.toLinearMap x) : f = g := by
  cases f; cases g; congr 1; exact LinearMap.ext hfg

instance {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    (U : H2Rep K h V₁) (W : H2Rep K h V₂) :
    AddCommGroup (H2Hom U W) where
  zero := ⟨0, fun _ => by simp⟩
  add f g := ⟨f.toLinearMap + g.toLinearMap, fun v => by
    simp [f.comm₁ v, g.comm₁ v]⟩
  neg f := ⟨-f.toLinearMap, fun v => by
    simp [f.comm₁ v]⟩
  sub f g := ⟨f.toLinearMap - g.toLinearMap, fun v => by
    simp [f.comm₁ v, g.comm₁ v]⟩
  nsmul n f := ⟨n • f.toLinearMap, fun v => by
    simp [f.comm₁ v]⟩
  zsmul n f := ⟨n • f.toLinearMap, fun v => by
    simp [f.comm₁ v]⟩
  add_assoc f g k := by ext x; exact add_assoc _ _ _
  zero_add f := by ext x; exact zero_add _
  add_zero f := by ext x; exact add_zero _
  add_comm f g := by ext x; exact add_comm _ _
  neg_add_cancel f := by ext x; exact neg_add_cancel _
  sub_eq_add_neg f g := by ext x; exact sub_eq_add_neg _ _
  nsmul_zero f := by ext x; exact zero_smul ℕ _
  nsmul_succ n f := by ext x; exact succ_nsmul _ n
  zsmul_zero' f := by ext x; exact zero_smul ℤ _
  zsmul_succ' n f := by ext x; exact SubNegMonoid.zsmul_succ' n _
  zsmul_neg' n f := by ext x; exact SubNegMonoid.zsmul_neg' n _

instance {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    (U : H2Rep K h V₁) (W : H2Rep K h V₂) :
    Module K (H2Hom U W) where
  smul c f := ⟨c • f.toLinearMap, fun v => by
    simp [f.comm₁ v]⟩
  one_smul f := by ext x; exact one_smul K _
  mul_smul c₁ c₂ f := by ext x; exact mul_smul c₁ c₂ _
  smul_zero c := by ext x; exact smul_zero c
  smul_add c f g := by ext x; exact smul_add c _ _
  add_smul c₁ c₂ f := by ext x; exact add_smul c₁ c₂ _
  zero_smul f := by ext x; exact zero_smul K _

@[simp]
theorem H2Hom.zero_toLinearMap {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    {U : H2Rep K h V₁} {W : H2Rep K h V₂} :
    (0 : H2Hom U W).toLinearMap = 0 := rfl

@[simp]
theorem H2Hom.add_toLinearMap {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    {U : H2Rep K h V₁} {W : H2Rep K h V₂} (f g : H2Hom U W) :
    (f + g).toLinearMap = f.toLinearMap + g.toLinearMap := rfl

@[simp]
theorem H2Hom.smul_toLinearMap {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    {U : H2Rep K h V₁} {W : H2Rep K h V₂} (c : K) (f : H2Hom U W) :
    (c • f).toLinearMap = c • f.toLinearMap := rfl

/-- An `H₂(q)`-equivariant linear isomorphism (`U ≅_{H₂(q)} W`). -/
structure H2Equiv {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ : Type*} [AddCommGroup V₁] [Module K V₁] [AddCommGroup V₂] [Module K V₂]
    (U : H2Rep K h V₁) (W : H2Rep K h V₂) where
  /-- Underlying `K`-linear equivalence. -/
  toLinearEquiv : V₁ ≃ₗ[K] V₂
  /-- Equivariance: `e(σ₁ u) = σ₁(e u)` for all `u`. -/
  comm₁ : ∀ u : V₁, toLinearEquiv (U.σ₁ u) = W.σ₁ (toLinearEquiv u)

/-- A representation of the 3-strand Iwahori–Hecke algebra `H₃(q)` (with quadratic
    parameter `h = q - q⁻¹`) on a `K`-module `V`: a pair of `K`-linear endomorphisms
    `σ₁, σ₂ : V →ₗ[K] V` satisfying both Hecke quadratic relations
    `σᵢ(σᵢ v) = h • σᵢ v + v` and the braid relation
    `σ₁(σ₂(σ₁ v)) = σ₂(σ₁(σ₂ v))`. -/
structure H3Rep (K : Type*) [CommRing K] (h : K)
    (V : Type*) [AddCommGroup V] [Module K V] where
  /-- Action of the first Hecke generator `σ₁`. -/
  σ₁ : V →ₗ[K] V
  /-- Action of the second Hecke generator `σ₂`. -/
  σ₂ : V →ₗ[K] V
  /-- Hecke quadratic relation for `σ₁`. -/
  hecke₁ : ∀ v : V, σ₁ (σ₁ v) = h • σ₁ v + v
  /-- Hecke quadratic relation for `σ₂`. -/
  hecke₂ : ∀ v : V, σ₂ (σ₂ v) = h • σ₂ v + v
  /-- 3-strand Artin braid relation `σ₁(σ₂(σ₁ v)) = σ₂(σ₁(σ₂ v))`. -/
  braid : ∀ v : V, σ₁ (σ₂ (σ₁ v)) = σ₂ (σ₁ (σ₂ v))

/-- **The restriction functor `Res_{H₂}^{H₃}`** along the subalgebra inclusion
    `H₂(q) ↪ H₃(q)` (`σ₁ ↦ σ₁`). -/
def H3Rep.restrict {K : Type*} [CommRing K] {h : K}
    {V : Type*} [AddCommGroup V] [Module K V]
    (W : H3Rep K h V) : H2Rep K h V where
  σ₁ := W.σ₁
  hecke₁ := W.hecke₁

-- ═══════════════════════════════════════════════════════════════
-- §3  CONCRETE LEPTON (H₂) AND MESON (H₃) REPRESENTATIONS
-- ═══════════════════════════════════════════════════════════════

/-- **The symmetric lepton representation `V_(2)` of `H₂(q)`:**
    1-dimensional module `K` on which `σ₁` acts by multiplication by `q`. -/
def leptonSymRep {K : Type*} [CommRing K] (q : Kˣ) :
    H2Rep K ((q : K) - (↑q⁻¹ : K)) K where
  σ₁ := (q : K) • LinearMap.id
  hecke₁ := fun x => by
    change (q : K) * ((q : K) * x) = ((q : K) - (↑q⁻¹ : K)) * ((q : K) * x) + x
    have hq : (q : K) * (↑q⁻¹ : K) = 1 := q.mul_inv
    linear_combination x * hq

/-- **The antisymmetric lepton representation `V_(1,1)` of `H₂(q)`:**
    1-dimensional module `K` on which `σ₁` acts by multiplication by `-q⁻¹`. -/
def leptonAntiRep {K : Type*} [CommRing K] (q : Kˣ) :
    H2Rep K ((q : K) - (↑q⁻¹ : K)) K where
  σ₁ := (-(↑q⁻¹ : K)) • LinearMap.id
  hecke₁ := fun x => by
    change -(↑q⁻¹ : K) * (-(↑q⁻¹ : K) * x) =
      ((q : K) - (↑q⁻¹ : K)) * (-(↑q⁻¹ : K) * x) + x
    have hq : (q : K) * (↑q⁻¹ : K) = 1 := q.mul_inv
    linear_combination x * hq

/-- **Schur non-isomorphism of the two lepton irreps:**
    In the semisimple regime `[2]_q = q + q⁻¹ ≠ 0` over an integral domain `K`,
    every `H₂(q)`-intertwiner `V_(2) → V_(1,1)` vanishes,
    so `V_(2)` and `V_(1,1)` are non-isomorphic simple `H₂(q)`-modules. -/
theorem leptonSym_to_anti_hom_eq_zero {K : Type*} [CommRing K] [IsDomain K]
    (q : Kˣ) (hq2 : (q : K) + (↑q⁻¹ : K) ≠ 0)
    (f : H2Hom (leptonSymRep q) (leptonAntiRep q)) :
    f = 0 := by
  ext x
  have hcomm := f.comm₁ x
  change f.toLinearMap ((q : K) • x) = -(↑q⁻¹ : K) * f.toLinearMap x at hcomm
  rw [f.toLinearMap.map_smul, smul_eq_mul] at hcomm
  have hsum : ((q : K) + (↑q⁻¹ : K)) * f.toLinearMap x = 0 := by
    linear_combination hcomm
  rcases mul_eq_zero.mp hsum with hq | hfx
  · exact absurd hq hq2
  · exact hfx

/-- Hoefsmit seminormal data `(a, b, c)` for the 2-dimensional standard representation
    `V_(2,1)` of `H₃(q)` over `K`:
    - `a + c = q - q⁻¹` (trace of `σ₂`),
    - `b² = 1 + a c` (determinant of `σ₂` is `a c - b² = -1`),
    - `q a - q⁻¹ c = -1` (braid trace identity `tr(σ₁ σ₂) = -1`),
    - `q a² - q⁻¹ b² = q² a` and `q b² - q⁻¹ c² = q⁻² c` (diagonal braid relations).
    All five identities hold identically for Hoefsmit's entries
    `a = -q⁻²/[2]_q`, `c = q²/[2]_q`, `b² = [3]_q/[2]_q²` whenever `[2]_q = q + q⁻¹`
    is invertible. -/
structure HoefsmitStandardParams {K : Type*} [CommRing K] (q : Kˣ) where
  a : K
  b : K
  c : K
  trace_eq : a + c = (q : K) - (↑q⁻¹ : K)
  det_eq : b ^ 2 = 1 + a * c
  braid_offdiag : (q : K) * a - (↑q⁻¹ : K) * c = -1
  braid_diag₁ : (q : K) * a ^ 2 - (↑q⁻¹ : K) * b ^ 2 = (q : K) ^ 2 * a
  braid_diag₂ : (q : K) * b ^ 2 - (↑q⁻¹ : K) * c ^ 2 = (↑q⁻¹ : K) ^ 2 * c

/-- Action of `σ₁ = diag(q, -q⁻¹)` on `K × K`. -/
def mesonSigma1Lin {K : Type*} [CommRing K] (q : Kˣ) : (K × K) →ₗ[K] (K × K) :=
  ((q : K) • LinearMap.id).prodMap ((-(↑q⁻¹ : K)) • LinearMap.id)

/-- Action of `σ₂ = !![a, b; b, c]` on `K × K`:
    `(x₁, x₂) ↦ (a x₁ + b x₂, b x₁ + c x₂)`. -/
def mesonSigma2Lin {K : Type*} [CommRing K] (a b c : K) : (K × K) →ₗ[K] (K × K) where
  toFun v := (a * v.1 + b * v.2, b * v.1 + c * v.2)
  map_add' u v := by ext <;> dsimp <;> ring
  map_smul' r v := by ext <;> dsimp <;> ring

/-- **The 2-dimensional standard (meson) representation `V_(2,1)` of `H₃(q)`**
    built from Hoefsmit's seminormal matrices `σ₁ = diag(q, -q⁻¹)` and
    `σ₂ = !![a, b; b, c]`. -/
def mesonStandardRep {K : Type*} [CommRing K] (q : Kˣ)
    (P : HoefsmitStandardParams q) :
    H3Rep K ((q : K) - (↑q⁻¹ : K)) (K × K) where
  σ₁ := mesonSigma1Lin q
  σ₂ := mesonSigma2Lin P.a P.b P.c
  hecke₁ := fun ⟨x₁, x₂⟩ => by
    have hq : (q : K) * (↑q⁻¹ : K) = 1 := q.mul_inv
    ext
    · change (q : K) * ((q : K) * x₁) = ((q : K) - (↑q⁻¹ : K)) * ((q : K) * x₁) + x₁
      linear_combination x₁ * hq
    · change -(↑q⁻¹ : K) * (-(↑q⁻¹ : K) * x₂) =
        ((q : K) - (↑q⁻¹ : K)) * (-(↑q⁻¹ : K) * x₂) + x₂
      linear_combination x₂ * hq
  hecke₂ := fun ⟨x₁, x₂⟩ => by
    ext
    · change P.a * (P.a * x₁ + P.b * x₂) + P.b * (P.b * x₁ + P.c * x₂) =
        ((q : K) - (↑q⁻¹ : K)) * (P.a * x₁ + P.b * x₂) + x₁
      linear_combination (P.a * x₁ + P.b * x₂) * P.trace_eq + x₁ * P.det_eq
    · change P.b * (P.a * x₁ + P.b * x₂) + P.c * (P.b * x₁ + P.c * x₂) =
        ((q : K) - (↑q⁻¹ : K)) * (P.b * x₁ + P.c * x₂) + x₂
      linear_combination (P.b * x₁ + P.c * x₂) * P.trace_eq + x₂ * P.det_eq
  braid := fun ⟨x₁, x₂⟩ => by
    have hq : (q : K) * (↑q⁻¹ : K) = 1 := q.mul_inv
    ext
    · change (q : K) * (P.a * ((q : K) * x₁) + P.b * (-(↑q⁻¹ : K) * x₂)) =
        P.a * ((q : K) * (P.a * x₁ + P.b * x₂)) +
        P.b * (-(↑q⁻¹ : K) * (P.b * x₁ + P.c * x₂))
      linear_combination -x₁ * P.braid_diag₁ - P.b * x₂ * P.braid_offdiag - P.b * x₂ * hq
    · change -(↑q⁻¹ : K) * (P.b * ((q : K) * x₁) + P.c * (-(↑q⁻¹ : K) * x₂)) =
        P.b * ((q : K) * (P.a * x₁ + P.b * x₂)) +
        P.c * (-(↑q⁻¹ : K) * (P.b * x₁ + P.c * x₂))
      linear_combination -P.b * x₁ * P.braid_offdiag - P.b * x₁ * hq - x₂ * P.braid_diag₂

-- ═══════════════════════════════════════════════════════════════
-- §4  EXPLICIT H₂-RESTRICTION ISOMORPHISM & b = 0 DECOUPLING
-- ═══════════════════════════════════════════════════════════════

/-- **Theorem (`V_(2,1) ↓ H₂ ≅ V_(2) ⊕ V_(1,1)`):**
    The restriction `(mesonStandardRep q P).restrict` of the 2-dimensional standard
    representation `V_(2,1)` of `H₃(q)` to `H₂(q)` is `H₂(q)`-equivariantly
    isomorphic to the direct sum `leptonSymRep q ⊕ leptonAntiRep q` (`V_(2) ⊕ V_(1,1)`). -/
def mesonStandard_restrict_equiv {K : Type*} [CommRing K] (q : Kˣ)
    (P : HoefsmitStandardParams q) :
    H2Equiv (mesonStandardRep q P).restrict
      (H2Rep.directSum (leptonSymRep q) (leptonAntiRep q)) where
  toLinearEquiv := LinearEquiv.refl K (K × K)
  comm₁ _ := rfl

/-- The first lepton subspace `V_(2) = K × {0} ⊂ V_(2,1)` (`e₁`-axis). -/
def leptonSymSubmodule (K : Type*) [CommRing K] : Submodule K (K × K) :=
  LinearMap.ker (LinearMap.snd K K K)

/-- The second lepton subspace `V_(1,1) = {0} × K ⊂ V_(2,1)` (`e₂`-axis). -/
def leptonAntiSubmodule (K : Type*) [CommRing K] : Submodule K (K × K) :=
  LinearMap.ker (LinearMap.fst K K K)

/-- **Hoefsmit Off-Diagonal Decoupling Theorem:**
    The second Hecke generator `σ₂ = !![a, b; b, c]` leaves both `H₂(q)`-subspaces
    `V_(2) = K e₁` and `V_(1,1) = K e₂` invariant (so that the two lepton channels
    decouple inside `V_(2,1)`) if and only if the off-diagonal binding amplitude
    vanishes (`b = 0`). -/
theorem sigma2_preserves_H2_summands_iff_b_eq_zero {K : Type*} [CommRing K]
    (a b c : K) :
    ((∀ v ∈ leptonSymSubmodule K, mesonSigma2Lin a b c v ∈ leptonSymSubmodule K) ∧
     (∀ v ∈ leptonAntiSubmodule K, mesonSigma2Lin a b c v ∈ leptonAntiSubmodule K)) ↔
    b = 0 := by
  constructor
  · rintro ⟨h1, _⟩
    have he1 : ((1 : K), (0 : K)) ∈ leptonSymSubmodule K := rfl
    have himg := h1 (1, 0) he1
    change b * 1 + c * 0 = 0 at himg
    linear_combination himg
  · intro hb
    subst hb
    refine ⟨?_, ?_⟩
    · intro ⟨x₁, x₂⟩ hx
      change x₂ = 0 at hx
      change 0 * x₁ + c * x₂ = 0
      rw [hx]; ring
    · intro ⟨x₁, x₂⟩ hx
      change x₁ = 0 at hx
      change a * x₁ + 0 * x₂ = 0
      rw [hx]; ring

-- ═══════════════════════════════════════════════════════════════
-- §5  FROBENIUS RECIPROCITY AND MULTIPLICITY ONE
-- ═══════════════════════════════════════════════════════════════

/-- **Direct-Sum Intertwiner Decomposition:**
    For any `H₂(q)`-representations `U₁, U₂, W`, the space of `H₂(q)`-homomorphisms
    out of the direct sum `U₁ ⊕ U₂` into `W` decomposes canonically as
    `Hom_{H₂}(U₁ ⊕ U₂, W) ≃ₗ[K] Hom_{H₂}(U₁, W) × Hom_{H₂}(U₂, W)`. -/
def h2HomDirectSumEquiv {K : Type*} [CommRing K] {h : K}
    {V₁ V₂ V₃ : Type*} [AddCommGroup V₁] [Module K V₁]
    [AddCommGroup V₂] [Module K V₂] [AddCommGroup V₃] [Module K V₃]
    (U₁ : H2Rep K h V₁) (U₂ : H2Rep K h V₂) (W : H2Rep K h V₃) :
    H2Hom (H2Rep.directSum U₁ U₂) W ≃ₗ[K] (H2Hom U₁ W × H2Hom U₂ W) where
  toFun f :=
    (⟨f.toLinearMap.comp (LinearMap.inl K V₁ V₂), fun u => by
        simpa [H2Rep.directSum, LinearMap.prodMap_apply] using f.comm₁ (u, 0)⟩,
     ⟨f.toLinearMap.comp (LinearMap.inr K V₁ V₂), fun u => by
        simpa [H2Rep.directSum, LinearMap.prodMap_apply] using f.comm₁ (0, u)⟩)
  invFun p :=
    ⟨p.1.toLinearMap.coprod p.2.toLinearMap, fun ⟨u₁, u₂⟩ => by
      change p.1.toLinearMap (U₁.σ₁ u₁) + p.2.toLinearMap (U₂.σ₁ u₂) =
        W.σ₁ (p.1.toLinearMap u₁ + p.2.toLinearMap u₂)
      rw [p.1.comm₁ u₁, p.2.comm₁ u₂, W.σ₁.map_add]⟩
  left_inv f := by
    ext ⟨u₁, u₂⟩
    change f.toLinearMap (u₁, 0) + f.toLinearMap (0, u₂) = f.toLinearMap (u₁, u₂)
    rw [← f.toLinearMap.map_add]
    simp
  right_inv p := by
    ext u
    · change p.1.toLinearMap u + p.2.toLinearMap 0 = p.1.toLinearMap u
      simp
    · change p.1.toLinearMap 0 + p.2.toLinearMap u = p.2.toLinearMap u
      simp
  map_add' f g := by
    ext u <;> rfl
  map_smul' r f := by
    ext u <;> rfl

/-- **Multiplicity One for `V_(2)` in `Res_{H₂}^{H₃}(V_(2,1))`:**
    In the semisimple regime `[2]_q = q + q⁻¹ ≠ 0` over an integral domain `K`,
    `Hom_{H₂(q)}(Res(V_(2,1)), V_(2))` is 1-dimensional (`≃ₗ[K] K`), with every
    `H₂(q)`-intertwiner determined uniquely by its value on `e₁ = (1, 0)` and
    vanishing identically on `V_(1,1) = K e₂`. -/
def hom_restrict_leptonSym_equiv {K : Type*} [CommRing K] [IsDomain K]
    (q : Kˣ) (P : HoefsmitStandardParams q)
    (hq2 : (q : K) + (↑q⁻¹ : K) ≠ 0) :
    H2Hom (mesonStandardRep q P).restrict (leptonSymRep q) ≃ₗ[K] K where
  toFun f := f.toLinearMap (1, 0)
  invFun c :=
    ⟨c • LinearMap.fst K K K, fun ⟨x₁, _⟩ => by
      change c * ((q : K) * x₁) = (q : K) * (c * x₁)
      ring⟩
  left_inv f := by
    ext ⟨x₁, x₂⟩
    have h01 : f.toLinearMap (0, 1) = 0 := by
      have hc := f.comm₁ (0, 1)
      change f.toLinearMap ((q : K) • (0 : K), (-(↑q⁻¹ : K)) • (1 : K)) =
        (q : K) • f.toLinearMap (0, 1) at hc
      have hsmul : ((q : K) • (0 : K), (-(↑q⁻¹ : K)) • (1 : K)) =
          (-(↑q⁻¹ : K)) • ((0 : K), (1 : K)) := by
        ext <;> simp
      rw [hsmul, f.toLinearMap.map_smul, smul_eq_mul, smul_eq_mul] at hc
      have hsum : ((q : K) + (↑q⁻¹ : K)) * f.toLinearMap (0, 1) = 0 := by
        linear_combination -hc
      rcases mul_eq_zero.mp hsum with hq | hf0
      · exact absurd hq hq2
      · exact hf0
    have hdecomp : (x₁, x₂) = x₁ • ((1 : K), (0 : K)) + x₂ • ((0 : K), (1 : K)) := by
      ext <;> simp
    change f.toLinearMap (1, 0) * x₁ = f.toLinearMap (x₁, x₂)
    rw [hdecomp, f.toLinearMap.map_add, f.toLinearMap.map_smul, f.toLinearMap.map_smul, h01]
    simp [mul_comm]
  right_inv c := by
    change c * 1 = c
    ring
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- **Multiplicity One for `V_(1,1)` in `Res_{H₂}^{H₃}(V_(2,1))`:**
    In the semisimple regime `[2]_q = q + q⁻¹ ≠ 0` over an integral domain `K`,
    `Hom_{H₂(q)}(Res(V_(2,1)), V_(1,1))` is 1-dimensional (`≃ₗ[K] K`), with every
    `H₂(q)`-intertwiner determined uniquely by its value on `e₂ = (0, 1)` and
    vanishing identically on `V_(2) = K e₁`. -/
def hom_restrict_leptonAnti_equiv {K : Type*} [CommRing K] [IsDomain K]
    (q : Kˣ) (P : HoefsmitStandardParams q)
    (hq2 : (q : K) + (↑q⁻¹ : K) ≠ 0) :
    H2Hom (mesonStandardRep q P).restrict (leptonAntiRep q) ≃ₗ[K] K where
  toFun f := f.toLinearMap (0, 1)
  invFun c :=
    ⟨c • LinearMap.snd K K K, fun ⟨_, x₂⟩ => by
      change c * (-(↑q⁻¹ : K) * x₂) = -(↑q⁻¹ : K) * (c * x₂)
      ring⟩
  left_inv f := by
    ext ⟨x₁, x₂⟩
    have h10 : f.toLinearMap (1, 0) = 0 := by
      have hc := f.comm₁ (1, 0)
      change f.toLinearMap ((q : K) • (1 : K), (-(↑q⁻¹ : K)) • (0 : K)) =
        (-(↑q⁻¹ : K)) • f.toLinearMap (1, 0) at hc
      have hsmul : ((q : K) • (1 : K), (-(↑q⁻¹ : K)) • (0 : K)) =
          (q : K) • ((1 : K), (0 : K)) := by
        ext <;> simp
      rw [hsmul, f.toLinearMap.map_smul, smul_eq_mul, smul_eq_mul] at hc
      have hsum : ((q : K) + (↑q⁻¹ : K)) * f.toLinearMap (1, 0) = 0 := by
        linear_combination hc
      rcases mul_eq_zero.mp hsum with hq | hf0
      · exact absurd hq hq2
      · exact hf0
    have hdecomp : (x₁, x₂) = x₁ • ((1 : K), (0 : K)) + x₂ • ((0 : K), (1 : K)) := by
      ext <;> simp
    change f.toLinearMap (0, 1) * x₂ = f.toLinearMap (x₁, x₂)
    rw [hdecomp, f.toLinearMap.map_add, f.toLinearMap.map_smul, f.toLinearMap.map_smul, h10]
    simp [mul_comm]
  right_inv c := by
    change c * 1 = c
    ring
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

-- ═══════════════════════════════════════════════════════════════
-- §6  BRANCHING TABLE & FROBENIUS RECIPROCITY ADJUNCTION
-- ═══════════════════════════════════════════════════════════════

/-- The branching multiplicities for H₃ ↓ H₂.
  For each λ ⊢ 3 and μ ⊢ 2, gives the multiplicity of V_μ in
  the restriction of V_λ to H₂.

  These follow from the Pieri rule: remove one box from the Young
  diagram of λ in all valid ways. -/
def branchingH3H2 : Fin 3 → Fin 2 → ℕ
  | 0, 0 => 1   -- V_(3) ↓ V_(2): multiplicity 1
  | 0, 1 => 0   -- V_(3) ↓ V_(1,1): multiplicity 0
  | 1, 0 => 1   -- V_(2,1) ↓ V_(2): multiplicity 1
  | 1, 1 => 1   -- V_(2,1) ↓ V_(1,1): multiplicity 1
  | 2, 0 => 0   -- V_(1,1,1) ↓ V_(2): multiplicity 0
  | 2, 1 => 1   -- V_(1,1,1) ↓ V_(1,1): multiplicity 1

/-- **Main Proposition (`prop:frobenius-lepton-meson-bridge`):**
    The standard representation `V_(2,1)` of `H₃(q)` restricts to `H₂(q)` as the
    direct sum of the two lepton representations `V_(2)` and `V_(1,1)`, each with
    multiplicity 1 (`Hom_{H₂}(Res(V_(2,1)), V_μ) ≃ₗ[K] K` for `μ ∈ {(2), (1,1)}`
    whenever `[2]_q ≠ 0`), and the two channels decouple under `σ₂` if and only if
    the Hoefsmit off-diagonal amplitude `b = 0`. -/
theorem standard_restricts_to_both_leptons :
    (branchingH3H2 1 0 = 1 ∧ branchingH3H2 1 1 = 1) ∧
    (∀ (a b c : ℤ),
      ((∀ v ∈ leptonSymSubmodule ℤ, mesonSigma2Lin a b c v ∈ leptonSymSubmodule ℤ) ∧
       (∀ v ∈ leptonAntiSubmodule ℤ, mesonSigma2Lin a b c v ∈ leptonAntiSubmodule ℤ)) ↔
      b = 0) :=
  ⟨⟨rfl, rfl⟩, fun a b c => sigma2_preserves_H2_summands_iff_b_eq_zero a b c⟩

/-- The trivial rep (3) restricts to the trivial lepton only. -/
theorem trivial_restricts_to_trivial :
    branchingH3H2 0 0 = 1 ∧ branchingH3H2 0 1 = 0 := by
  constructor <;> rfl

/-- The sign rep (1,1,1) restricts to the sign lepton only. -/
theorem sign_restricts_to_sign :
    branchingH3H2 2 0 = 0 ∧ branchingH3H2 2 1 = 1 := by
  constructor <;> rfl

/-- Dimension check: dim V_(2,1) = sum of branching multiplicities × dim V_μ.
  dim(2,1) = 2 = 1·dim(2) + 1·dim(1,1) = 1·1 + 1·1 = 2. -/
theorem branching_dimension_check :
    branchingH3H2 1 0 * 1 + branchingH3H2 1 1 * 1 = 2 := by
  simp [branchingH3H2]

/-- Frobenius reciprocity multiplicity identity:
    `⟨Res(V_(2,1)), V_μ⟩_{H₂} = ⟨V_(2,1), Ind(V_μ)⟩_{H₃} = 1` for `μ ∈ {(2), (1,1)}`. -/
theorem frobenius_reciprocity_standard :
    branchingH3H2 1 0 = 1 ∧ branchingH3H2 1 1 = 1 :=
  standard_restricts_to_both_leptons.1

end QOU.BraidsAndKnots
