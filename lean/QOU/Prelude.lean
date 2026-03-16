/-!
# QOU.Prelude — Mathematical Foundations

Self-contained mathematical types used throughout the QOU formalisation.
Each definition notes the Mathlib4 counterpart so that contributors can
swap in real Mathlib imports when building against `leanprover-community/mathlib4`.

## Design rationale
The QOU paper is a physics / differential-geometry paper.  Its Lean
companion therefore needs:

1. **Algebra** — fields, algebras, modules, tensor products.
2. **Geometry** — smooth manifolds, bundles, connections, differential forms.
3. **Category theory** — monoidal categories, fibre functors.

We axiomatise the minimum needed to *state* the paper's definitions and
theorems with genuine mathematical content.  Proofs are deferred (`sorry`).
-/

universe u v w

-- ═══════════════════════════════════════════════════════════════════════
-- §1  Algebra
-- ═══════════════════════════════════════════════════════════════════════

/-- A commutative field.  Mathlib: `Mathlib.Algebra.Field.Basic`. -/
class QField (k : Type u) extends Add k, Mul k, Neg k, One k, Zero k where
  add_comm   : ∀ a b : k, a + b = b + a
  mul_comm   : ∀ a b : k, a * b = b * a
  mul_assoc  : ∀ a b c : k, a * b * c = a * (b * c)
  add_assoc  : ∀ a b c : k, a + b + c = a + (b + c)
  mul_one    : ∀ a : k, a * 1 = a
  add_zero   : ∀ a : k, a + 0 = a
  add_neg    : ∀ a : k, a + (-a) = 0
  left_distrib : ∀ a b c : k, a * (b + c) = a * b + a * c
  zero_ne_one : (0 : k) ≠ (1 : k)
  inv        : k → k
  mul_inv    : ∀ a : k, a ≠ 0 → a * inv a = 1

/-- Non-zero element of a field.  Mathlib: `Units k` or `kˣ`. -/
structure Units (k : Type u) [QField k] where
  val    : k
  ne_zero : val ≠ 0

/-- An associative k-algebra.  Mathlib: `Mathlib.Algebra.Algebra.Basic`. -/
class QAlgebra (k : Type u) (A : Type v) [QField k] extends
    Add A, Mul A, Zero A, One A, Neg A where
  smul          : k → A → A
  smul_assoc    : ∀ (r s : k) (a : A), smul r (smul s a) = smul (r * s) a
  mul_assoc     : ∀ a b c : A, a * b * c = a * (b * c)
  add_comm      : ∀ a b : A, a + b = b + a
  left_distrib  : ∀ a b c : A, a * (b + c) = a * b + a * c
  right_distrib : ∀ a b c : A, (a + b) * c = a * c + b * c
  one_mul       : ∀ a : A, 1 * a = a
  mul_one       : ∀ a : A, a * 1 = a

-- ═══════════════════════════════════════════════════════════════════════
-- §2  Linear algebra — modules and tensor products
-- ═══════════════════════════════════════════════════════════════════════

/-- A left k-module.  Mathlib: `Mathlib.Algebra.Module.Basic`. -/
class QModule (k : Type u) (M : Type v) [QField k] extends Add M, Zero M, Neg M where
  smul        : k → M → M
  smul_add    : ∀ (r : k) (x y : M), smul r (x + y) = smul r x + smul r y
  add_smul    : ∀ (r s : k) (x : M), smul (r + s) x = smul r x + smul s x
  smul_assoc  : ∀ (r s : k) (x : M), smul r (smul s x) = smul (r * s) x
  one_smul    : ∀ x : M, smul 1 x = x

/-- Tensor product of two k-modules (abstract).
    Mathlib: `Mathlib.LinearAlgebra.TensorProduct.Basic`. -/
axiom TensorProduct (k : Type u) (M N : Type v) [QField k]
  [QModule k M] [QModule k N] : Type v

notation:35 M " ⊗[" k "] " N => TensorProduct k M N

/-- Bilinear map.  Mathlib: `Mathlib.LinearAlgebra.BilinearMap`. -/
structure BilinearMap (k : Type u) (M N P : Type v) [QField k]
    [QModule k M] [QModule k N] [QModule k P] where
  toFun : M → N → P
  map_smul_left  : ∀ (r : k) (m : M) (n : N),
    toFun (QModule.smul r m) n = QModule.smul r (toFun m n)
  map_smul_right : ∀ (r : k) (m : M) (n : N),
    toFun m (QModule.smul r n) = QModule.smul r (toFun m n)

-- ═══════════════════════════════════════════════════════════════════════
-- §3  Category theory (lightweight)
-- ═══════════════════════════════════════════════════════════════════════

/-- A category (simplified — objects and morphisms only).
    Mathlib: `Mathlib.CategoryTheory.Category.Basic`. -/
class QCategory (Obj : Type u) where
  Hom  : Obj → Obj → Type v
  id   : (X : Obj) → Hom X X
  comp : {X Y Z : Obj} → Hom X Y → Hom Y Z → Hom X Z
  id_comp : ∀ {X Y : Obj} (f : Hom X Y), comp (id X) f = f
  comp_id : ∀ {X Y : Obj} (f : Hom X Y), comp f (id Y) = f
  assoc   : ∀ {X Y Z W : Obj} (f : Hom X Y) (g : Hom Y Z) (h : Hom Z W),
            comp (comp f g) h = comp f (comp g h)

/-- A monoidal structure on a category.
    Mathlib: `Mathlib.CategoryTheory.Monoidal.Basic`. -/
class MonoidalCategory (Obj : Type u) extends QCategory Obj where
  tensorObj  : Obj → Obj → Obj
  tensorUnit : Obj
  -- associator, unitors omitted for brevity; see Mathlib

/-- A k-linear structure on a category.
    Mathlib: `Mathlib.CategoryTheory.Linear.Basic`. -/
class LinearCategory (k : Type u) (Obj : Type v) [QField k]
    extends QCategory Obj where
  homModule : (X Y : Obj) → QModule k (QCategory.Hom X Y)

/-- A rigid monoidal category has duals for all objects.
    Mathlib: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`. -/
class RigidMonoidalCategory (k : Type u) (Obj : Type v) [QField k]
    extends MonoidalCategory Obj, LinearCategory k Obj where
  dual : Obj → Obj
  eval : (X : Obj) → QCategory.Hom (tensorObj (dual X) X) tensorUnit
  coeval : (X : Obj) → QCategory.Hom tensorUnit (tensorObj X (dual X))

/-- An exact faithful monoidal functor to Vect_k (fibre functor).
    Mathlib: `Mathlib.CategoryTheory.Monoidal.Functor`. -/
structure FibreFunctor (k : Type u) (Obj : Type v) [QField k]
    [RigidMonoidalCategory k Obj] where
  /-- Object-level map: each object to a k-vector space. -/
  obj : Obj → Type w
  /-- Each image is a k-module. -/
  obj_module : (X : Obj) → QModule k (obj X)
  /-- Morphism-level map. -/
  map : {X Y : Obj} → QCategory.Hom X Y → (obj X → obj Y)
  /-- Faithful: injective on Hom-sets. -/
  faithful : ∀ {X Y : Obj} (f g : QCategory.Hom X Y),
    map f = map g → f = g

-- ═══════════════════════════════════════════════════════════════════════
-- §4  Smooth geometry (abstract)
-- ═══════════════════════════════════════════════════════════════════════

/-- An abstract smooth manifold (placeholder for charts/atlas).
    Mathlib: `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners`. -/
class SmoothManifold (M : Type u) where
  dim    : Nat
  smooth : Prop  -- placeholder for atlas smoothness

/-- The tangent space at a point.  Mathlib: `Mathlib.Geometry.Manifold.TangentBundle`. -/
axiom TangentSpace (M : Type u) [SmoothManifold M] (p : M) : Type u

/-- Smooth sections of a vector bundle.
    Mathlib: `Mathlib.Topology.FiberBundle.Basic`. -/
axiom SmoothSection (M E : Type u) [SmoothManifold M] : Type u

/-- Differential k-forms on M.  Mathlib: `Mathlib.Geometry.Manifold.DeRham`. -/
axiom DiffForm (M : Type u) [SmoothManifold M] (k : Nat) : Type u

/-- The exterior derivative d : Ωᵏ → Ωᵏ⁺¹.
    Mathlib: `Mathlib.Analysis.InnerProductSpace.Calculus`. -/
axiom extDeriv {M : Type u} [SmoothManifold M] {k : Nat} :
  DiffForm M k → DiffForm M (k + 1)

/-- The Lie derivative along a vector field.
    Mathlib: `Mathlib.Geometry.Manifold.VectorField`. -/
axiom LieDeriv {M : Type u} [SmoothManifold M] :
  SmoothSection M M → DiffForm M k → DiffForm M k

/-- The interior product ι_X.
    Mathlib: `Mathlib.Geometry.Manifold.DeRham`. -/
axiom interiorProd {M : Type u} [SmoothManifold M] :
  SmoothSection M M → DiffForm M (k + 1) → DiffForm M k

/-- The wedge product ∧ on differential forms. -/
axiom wedge {M : Type u} [SmoothManifold M] :
  DiffForm M j → DiffForm M k → DiffForm M (j + k)

/-- The Hodge star operator on a Riemannian manifold.
    Mathlib: N/A (not yet in Mathlib). -/
axiom HodgeStar {M : Type u} [SmoothManifold M] (n : Nat) :
  DiffForm M k → DiffForm M (n - k)

-- ═══════════════════════════════════════════════════════════════════════
-- §5  Principal bundles and connections
-- ═══════════════════════════════════════════════════════════════════════

/-- A Lie group (abstract).  Mathlib: `Mathlib.Geometry.Manifold.Instances.UnitsOfNormedAlgebra`. -/
class LieGroup (G : Type u) extends Mul G, One G, Inv G, SmoothManifold G where
  mul_assoc : ∀ a b c : G, a * b * c = a * (b * c)
  one_mul   : ∀ a : G, 1 * a = a
  mul_inv   : ∀ a : G, a * a⁻¹ = 1

/-- A principal G-bundle P → M.
    Mathlib: `Mathlib.Topology.FiberBundle.Basic`. -/
structure PrincipalBundle (G : Type u) (M : Type v) [LieGroup G] [SmoothManifold M] where
  totalSpace : Type w
  proj : totalSpace → M
  action : G → totalSpace → totalSpace

/-- A connection on a principal bundle (Lie-algebra-valued 1-form).
    Mathlib: N/A (not yet in Mathlib). -/
structure Connection (G : Type u) (M : Type v) [LieGroup G] [SmoothManifold M]
    (P : PrincipalBundle G M) where
  /-- The connection 1-form ω ∈ Ω¹(P, 𝔤). -/
  form : DiffForm P.totalSpace 1

/-- The curvature 2-form F_A = dA + A ∧ A. -/
axiom curvature {G : Type u} {M : Type v} [LieGroup G] [SmoothManifold M]
  {P : PrincipalBundle G M} (A : Connection G M P) : DiffForm M 2

-- ═══════════════════════════════════════════════════════════════════════
-- §6  Complex and real types
-- ═══════════════════════════════════════════════════════════════════════

/-- The real numbers (axiomatic).  Mathlib: `Mathlib.Analysis.SpecialFunctions.Basic`. -/
axiom Real : Type
/-- The complex numbers.  Mathlib: `Mathlib.Analysis.SpecialFunctions.Complex.Basic`. -/
axiom Complex : Type

notation "ℝ" => Real
notation "ℂ" => Complex

axiom Real.instQField : QField ℝ
axiom Complex.instQField : QField ℂ

instance : QField ℝ := Real.instQField
instance : QField ℂ := Complex.instQField

/-- Absolute value on ℝ. -/
axiom Real.abs : ℝ → ℝ
/-- Complex modulus. -/
axiom Complex.abs : ℂ → ℝ

/-- The exponential function exp : ℝ → ℝ. -/
axiom Real.exp : ℝ → ℝ
/-- Complex exponential. -/
axiom Complex.exp : ℂ → ℂ
/-- Real logarithm. -/
axiom Real.log : ℝ → ℝ
/-- Complex logarithm. -/
axiom Complex.log : ℂ → ℂ

-- ═══════════════════════════════════════════════════════════════════════
-- §7  Matrices
-- ═══════════════════════════════════════════════════════════════════════

/-- n × n matrix over a type α.  Mathlib: `Mathlib.Data.Matrix.Basic`. -/
def Matrix (n m : Nat) (α : Type u) := Fin n → Fin m → α

/-- The 2×2 identity matrix. -/
def Matrix.one [One α] [Zero α] : Matrix 2 2 α :=
  fun i j => if i = j then 1 else 0

/-- Matrix multiplication (2×2). -/
def Matrix.mul [Add α] [Mul α] [Zero α] (A B : Matrix 2 2 α) : Matrix 2 2 α :=
  fun i j => A i 0 * B 0 j + A i 1 * B 1 j

-- ═══════════════════════════════════════════════════════════════════════
-- §8  Quaternions
-- ═══════════════════════════════════════════════════════════════════════

/-- The quaternion algebra ℍ.  Mathlib: `Mathlib.Algebra.Quaternion`. -/
structure Quaternion where
  re : ℝ
  im_i : ℝ
  im_j : ℝ
  im_k : ℝ

namespace Quaternion

def i : Quaternion := ⟨0, 1, 0, 0⟩  -- using sorry-free ℝ constants via axiom
def j : Quaternion := ⟨0, 0, 1, 0⟩
def k : Quaternion := ⟨0, 0, 0, 1⟩

end Quaternion

-- ═══════════════════════════════════════════════════════════════════════
-- §9  Euler characteristic
-- ═══════════════════════════════════════════════════════════════════════

/-- Euler characteristic of a topological space / bundle.
    Mathlib: N/A (algebraic topology is in progress). -/
axiom eulerChar (X : Type u) : Int
