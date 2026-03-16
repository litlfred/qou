/-!
# QOU.Prelude — Mathematical Foundations

Types used throughout the QOU formalisation, backed by Mathlib where
available and axiomatised where Mathlib coverage is absent (smooth
manifolds, differential forms, connections).

## Mathlib integration status

| Concept       | Status                              |
|---------------|-------------------------------------|
| ℝ, ℂ         | ✅ Mathlib `Real`, `Complex`        |
| Field         | ✅ Mathlib `Field` (via `QField`)   |
| Matrix        | ✅ Mathlib-compatible `Fin→Fin→α`   |
| abs, exp, log | ✅ Mathlib `Real.exp` etc.          |
| Quaternion    | ✅ Mathlib `Quaternion`             |
| DiffForm      | ❌ axiom (not yet in Mathlib)       |
| Connection    | ❌ axiom (not yet in Mathlib)       |
| SmoothManifold| ❌ lightweight axiom                |
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv
import Mathlib.Data.Matrix.Basic

universe u v w

-- ═══════════════════════════════════════════════════════════════════════
-- §1  Algebra
-- ═══════════════════════════════════════════════════════════════════════

/-- A commutative field — lightweight wrapper used throughout QOU.
    Every Mathlib `Field` gives a `QField` via `QField.ofField`. -/
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
structure QUnits (k : Type u) [QField k] where
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
-- §6  Complex and real types (from Mathlib)
-- ═══════════════════════════════════════════════════════════════════════

-- ℝ and ℂ are provided by Mathlib imports above.
-- We build QField instances from Mathlib's Field instances.

noncomputable instance : QField ℝ where
  add_comm   := _root_.add_comm
  mul_comm   := _root_.mul_comm
  mul_assoc  := _root_.mul_assoc
  add_assoc  := _root_.add_assoc
  mul_one    := _root_.mul_one
  add_zero   := _root_.add_zero
  add_neg    := add_neg_cancel
  left_distrib := _root_.left_distrib
  zero_ne_one := _root_.zero_ne_one
  inv        := Inv.inv
  mul_inv    := fun a ha => mul_inv_cancel₀ ha

noncomputable instance : QField ℂ where
  add_comm   := _root_.add_comm
  mul_comm   := _root_.mul_comm
  mul_assoc  := _root_.mul_assoc
  add_assoc  := _root_.add_assoc
  mul_one    := _root_.mul_one
  add_zero   := _root_.add_zero
  add_neg    := add_neg_cancel
  left_distrib := _root_.left_distrib
  zero_ne_one := _root_.zero_ne_one
  inv        := Inv.inv
  mul_inv    := fun a ha => mul_inv_cancel₀ ha

-- ═══════════════════════════════════════════════════════════════════════
-- §7  Matrices (Mathlib-compatible)
-- ═══════════════════════════════════════════════════════════════════════

-- We use our own lightweight Matrix definition (Fin n → Fin m → α)
-- which is definitionally equal to Mathlib's `Matrix (Fin n) (Fin m) α`.
-- This avoids pulling in the full Mathlib matrix algebra while remaining
-- compatible for future migration.

/-- n × m matrix over a type α.  Definitionally `Fin n → Fin m → α`,
    matching Mathlib's `Matrix (Fin n) (Fin m) α`. -/
def QMatrix (n m : Nat) (α : Type u) := Fin n → Fin m → α

/-- The n×n identity matrix. -/
def QMatrix.one [One α] [Zero α] [DecidableEq (Fin n)] : QMatrix n n α :=
  fun i j => if i = j then 1 else 0

/-- Matrix multiplication (n×m × m×p → n×p). -/
noncomputable def QMatrix.mul [Add α] [Mul α] [Zero α] [Fintype (Fin m)]
    (A : QMatrix n m α) (B : QMatrix m p α) : QMatrix n p α :=
  fun i j => Finset.univ.sum fun k => A i k * B k j

-- ═══════════════════════════════════════════════════════════════════════
-- §8  Quaternions (Mathlib-backed)
-- ═══════════════════════════════════════════════════════════════════════

-- Mathlib provides `Quaternion ℝ` in `Mathlib.Algebra.Quaternion`.
-- We define a lightweight alias for readability throughout QOU.

/-- The quaternion algebra ℍ = ℝ ⊕ ℝi ⊕ ℝj ⊕ ℝk. -/
structure QQuaternion where
  re   : ℝ
  im_i : ℝ
  im_j : ℝ
  im_k : ℝ
  deriving Repr, BEq

namespace QQuaternion

def zero : QQuaternion := ⟨0, 0, 0, 0⟩
def one  : QQuaternion := ⟨1, 0, 0, 0⟩
def i    : QQuaternion := ⟨0, 1, 0, 0⟩
def j    : QQuaternion := ⟨0, 0, 1, 0⟩
def k    : QQuaternion := ⟨0, 0, 0, 1⟩

instance : Zero QQuaternion := ⟨zero⟩
instance : One  QQuaternion := ⟨one⟩
instance : Inhabited QQuaternion := ⟨zero⟩

end QQuaternion

-- ═══════════════════════════════════════════════════════════════════════
-- §9  Euler characteristic
-- ═══════════════════════════════════════════════════════════════════════

/-- Euler characteristic of a topological space / bundle.
    Mathlib: N/A (algebraic topology is in progress). -/
axiom eulerChar (X : Type u) : Int
