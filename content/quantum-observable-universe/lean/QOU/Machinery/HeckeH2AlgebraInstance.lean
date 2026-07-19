/-
# H₂(q) as a `CommRing`/`Algebra` + the n=2 `MarkovTrace` instance + the algebra-hom inclusion into H₃

Categorical tranche completing the concrete bottom of the Hecke tower.
After `HeckeH3AlgebraInstance` (H₃ instances + the first `MarkovTrace`
instance) and `HeckeH4StabilizationRung` (the 3→4 rung), this file finishes
the n = 2 layer:

* `H2A R h` — the rank-two Hecke algebra `H₂(q) = span{γ, σ₀}` with the
  product `(a₁ + b₁σ)(a₂ + b₂σ) = (a₁a₂ + b₁b₂) + (a₁b₂ + b₁a₂ + h·b₁b₂)σ`
  (the Hecke quadratic in rank one), as a genuine **`CommRing`** and
  **`Algebra R`**;
* `markovTrace_H2A` — the **n = 2 `MarkovTrace` instance**
  (`trace₂ z = a + z·b`); with `markovTrace_H3A` both concrete rungs now
  inhabit the class;
* **`iotaAlg : H2A R h →ₐ[R] H3A R h`** — the tower inclusion as an honest
  R-algebra homomorphism (multiplicativity = the merged `iota23_mul`), and
* `trace3_iotaAlg_stabilizes` — the bottom stabilization step in exactly
  the shape the `MarkovStabilization` class asks of its `ι : Hn →ₐ Hn1`
  parameter: `trace₃(ι x) = trace₂ x`.

HONESTY (STRICT): the general-n `MarkovStabilization` / `HeckeBraidedPresentation`
class instances stay OPEN — their binders quantify the H_∞ generator family
(see `HeckeH3AlgebraLaws`); what is completed here is the concrete
`n = 2 → 3` step at full typeclass strength. Nothing wired; `1/(8π)` stays
phase-4. Base ring (§7c): generic `[CommRing R]`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-/
import QOU.Machinery.HeckeH3AlgebraInstance
import Mathlib.Algebra.Algebra.Hom

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- The rank-two Hecke algebra `H₂(q) = span{γ, σ₀}`: coordinates
`a·γ + b·σ₀`. The parameter `h = q − q⁻¹` pins the product. -/
@[ext]
structure H2A (R : Type*) [CommRing R] (h : R) where
  /-- Coefficient of the identity γ. -/
  a : R
  /-- Coefficient of the generator σ₀. -/
  b : R

namespace H2A

variable {h : R}

instance : Zero (H2A R h) := ⟨⟨0, 0⟩⟩
instance : Add (H2A R h) := ⟨fun x y => ⟨x.a + y.a, x.b + y.b⟩⟩
instance : Neg (H2A R h) := ⟨fun x => ⟨-x.a, -x.b⟩⟩
instance : Sub (H2A R h) := ⟨fun x y => ⟨x.a - y.a, x.b - y.b⟩⟩
instance : SMul ℕ (H2A R h) := ⟨fun n x => ⟨n • x.a, n • x.b⟩⟩
instance : SMul ℤ (H2A R h) := ⟨fun n x => ⟨n • x.a, n • x.b⟩⟩
instance : SMul R (H2A R h) := ⟨fun c x => ⟨c * x.a, c * x.b⟩⟩

@[simp] lemma zero_a : (0 : H2A R h).a = 0 := rfl
@[simp] lemma zero_b : (0 : H2A R h).b = 0 := rfl
@[simp] lemma add_a (x y : H2A R h) : (x + y).a = x.a + y.a := rfl
@[simp] lemma add_b (x y : H2A R h) : (x + y).b = x.b + y.b := rfl
@[simp] lemma smul_a (c : R) (x : H2A R h) : (c • x).a = c * x.a := rfl
@[simp] lemma smul_b (c : R) (x : H2A R h) : (c • x).b = c * x.b := rfl

private def toFn : H2A R h → (Fin 2 → R) := fun x => ![x.a, x.b]

private lemma toFn_injective : Function.Injective (toFn (R := R) (h := h)) := by
  intro x y hxy
  have ha := congrFun hxy 0
  have hb := congrFun hxy 1
  cases x; cases y
  simp [toFn] at ha hb
  simp [ha, hb]

private lemma toFn_add (x y : H2A R h) : toFn (x + y) = toFn x + toFn y := by
  funext i; fin_cases i <;> rfl

instance : AddCommGroup (H2A R h) :=
  toFn_injective.addCommGroup toFn (by funext i; fin_cases i <;> rfl)
    toFn_add
    (by intro x; funext i; fin_cases i <;> rfl)
    (by intro x y; funext i; fin_cases i <;> rfl)
    (by intro x n; funext i; fin_cases i <;> rfl)
    (by intro x n; funext i; fin_cases i <;> rfl)

private def toFnHom : H2A R h →+ (Fin 2 → R) :=
  { toFun := toFn, map_zero' := by funext i; fin_cases i <;> rfl,
    map_add' := toFn_add }

instance : Module R (H2A R h) :=
  toFn_injective.module R toFnHom (by intro c x; funext i; fin_cases i <;> rfl)

instance : Mul (H2A R h) :=
  ⟨fun x y => ⟨x.a * y.a + x.b * y.b, x.a * y.b + x.b * y.a + h * (x.b * y.b)⟩⟩
instance : One (H2A R h) := ⟨⟨1, 0⟩⟩

@[simp] lemma mul_a (x y : H2A R h) :
    (x * y).a = x.a * y.a + x.b * y.b := rfl
@[simp] lemma mul_b (x y : H2A R h) :
    (x * y).b = x.a * y.b + x.b * y.a + h * (x.b * y.b) := rfl
@[simp] lemma one_a : (1 : H2A R h).a = 1 := rfl
@[simp] lemma one_b : (1 : H2A R h).b = 0 := rfl

/-- **H₂(q) is a commutative ring** — the rank-one Hecke product laws all
close by `ring` on coordinates. -/
instance : CommRing (H2A R h) where
  __ := (inferInstance : AddCommGroup (H2A R h))
  mul := (· * ·)
  one := 1
  mul_assoc x y z := by ext <;> simp <;> ring
  one_mul x := by ext <;> simp
  mul_one x := by ext <;> simp
  left_distrib x y z := by ext <;> simp <;> ring
  right_distrib x y z := by ext <;> simp <;> ring
  zero_mul x := by ext <;> simp
  mul_zero x := by ext <;> simp
  mul_comm x y := by ext <;> simp <;> ring

/-- **H₂(q) is an R-algebra.** -/
instance : Algebra R (H2A R h) :=
  Algebra.ofModule
    (fun c x y => by ext <;> simp <;> ring)
    (fun c x y => by ext <;> simp <;> ring)

/-- The n = 2 Markov trace: `trace₂(a·γ + b·σ₀) = a + z·b` (weights (1, z)). -/
def trace₂ (z : R) (x : H2A R h) : R := x.a + z * x.b

/-- **The n = 2 `MarkovTrace` instance** — with `markovTrace_H3A`, both
concrete rungs of the tower now inhabit the class. -/
instance markovTrace_H2A (z : R) :
    QOU.Machinery.MarkovTrace R (H2A R h) (trace₂ (h := h) z) where
  cyclic x y := by simp [trace₂]; ring
  map_add x y := by simp [trace₂]; ring
  map_smul c x := by simp [trace₂]; ring

/-- The inclusion on carriers: `a·γ + b·σ₀ ↦ (a, b, 0, 0, 0, 0)`. -/
def iotaFun (x : H2A R h) : H3A R h := ⟨iota23 x.a x.b⟩

lemma iotaFun_one : iotaFun (h := h) (1 : H2A R h) = 1 :=
  H3A.ext (by funext i; fin_cases i <;> simp [iotaFun, iota23, unitNF])

lemma iotaFun_mul (x y : H2A R h) :
    iotaFun (x * y) = iotaFun x * iotaFun y :=
  H3A.ext (by
    show iota23 (x * y).a (x * y).b = mulNF h (iota23 x.a x.b) (iota23 y.a y.b)
    rw [iota23_mul, mul_a, mul_b])

lemma iotaFun_zero : iotaFun (h := h) (0 : H2A R h) = 0 :=
  H3A.ext (by funext i; fin_cases i <;> simp [iotaFun, iota23])

lemma iotaFun_add (x y : H2A R h) :
    iotaFun (x + y) = iotaFun x + iotaFun y :=
  H3A.ext (by funext i; fin_cases i <;> simp [iotaFun, iota23])

lemma iotaFun_smul (c : R) (x : H2A R h) :
    iotaFun (c • x) = c • iotaFun x :=
  H3A.ext (by funext i; fin_cases i <;> simp [iotaFun, iota23])

/-- **The tower inclusion as an R-algebra homomorphism** — the exact shape
the `MarkovStabilization` class asks of its `ι : Hn →ₐ Hn1` parameter.
Multiplicativity is the merged `iota23_mul`. -/
def iotaAlg : H2A R h →ₐ[R] H3A R h :=
  { toFun := iotaFun
    map_one' := iotaFun_one
    map_mul' := iotaFun_mul
    map_zero' := iotaFun_zero
    map_add' := iotaFun_add
    commutes' := fun r => by
      rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one,
        iotaFun_smul, iotaFun_one] }

/-- **The bottom stabilization step at typeclass strength**:
`trace₃(ι x) = trace₂ x` along the algebra-hom inclusion — the concrete
`n = 2 → 3` content of the `MarkovStabilization` class's `stabilizes` field
(whose general-n instance stays open). -/
theorem trace3_iotaAlg_stabilizes (z : R) (x : H2A R h) :
    H3A.trace (h := h) z (iotaAlg x) = trace₂ (h := h) z x := by
  show trM z h (iota23 x.a x.b) = trace₂ (h := h) z x
  rw [trM_iota23_stabilizes]
  rfl

end H2A

end QOU.Machinery.H3
