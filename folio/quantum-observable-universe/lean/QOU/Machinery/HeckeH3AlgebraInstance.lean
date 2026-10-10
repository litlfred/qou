/-
# H₃(q) as a genuine `Ring`/`Algebra` — and the FIRST `MarkovTrace` class instance

Categorical tranche, continuation of `HeckeH3AlgebraLaws` (merged): that file
certified the NF module's algebra-object *laws* (bilinearity, unit,
associativity, braid relation); this file packages them as typeclass
*instances*, producing:

* `H3A R h` — a wrapper type for the H₃(q) NF module (parameter `h = q − q⁻¹`
  pins the product), with `AddCommGroup`, `Module R`, **`Ring`**, and
  **`Algebra R`** instances whose multiplication is the proved `mulNF`;
* **the first instance of the `MarkovTrace` class** —
  `markovTrace_H3A : MarkovTrace R (H3A R h) (trace z)` — every field
  (cyclicity, additivity, R-homogeneity) discharged by the proved H₃ laws.
  Until now the class had NO instance anywhere in the corpus; the concrete
  n=3 rung now inhabits it with real content.

Consequences wired downstream (derived, not assumed): via
`TauFunctorReduction.observationFrame_cyclic`, the observation frame
`τ_∞ = ev ∘ tr_M` on `H3A` is now *unconditionally* cyclic — the F3 slice at
n=3 holds at the typeclass level, no hypothesis threading needed.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): `MarkovTrace` is an
interface with real laws — instantiating it at n=3 is proved content, not a
conjecture-class discharge. The OPEN items are unchanged: general-n
`HeckeBraidedPresentation` / `MarkovStabilization` (H_∞ binders — no
finite-level instance possible, per `HeckeH3AlgebraLaws`), and the
`TauRhoHodgeLift` wall. Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[CommRing R]` throughout — no `ℝ`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-/
import QOU.Machinery.HeckeH3AlgebraLaws
import Mathlib.Algebra.Module.Pi

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- Wrapper for the H₃(q) NF module: a distinct type carrying the `mulNF h`
ring structure. The parameter `h = q − q⁻¹` pins the product. -/
@[ext]
structure H3A (R : Type*) [CommRing R] (h : R) where
  /-- NF coordinates on the basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`. -/
  v : Fin 6 → R

namespace H3A

variable {h : R}

instance : Zero (H3A R h) := ⟨⟨0⟩⟩
instance : Add (H3A R h) := ⟨fun x y => ⟨x.v + y.v⟩⟩
instance : Neg (H3A R h) := ⟨fun x => ⟨-x.v⟩⟩
instance : Sub (H3A R h) := ⟨fun x y => ⟨x.v - y.v⟩⟩
instance : SMul ℕ (H3A R h) := ⟨fun n x => ⟨n • x.v⟩⟩
instance : SMul ℤ (H3A R h) := ⟨fun n x => ⟨n • x.v⟩⟩
instance : SMul R (H3A R h) := ⟨fun c x => ⟨c • x.v⟩⟩

@[simp] lemma zero_v : (0 : H3A R h).v = 0 := rfl
@[simp] lemma add_v (x y : H3A R h) : (x + y).v = x.v + y.v := rfl
@[simp] lemma neg_v (x : H3A R h) : (-x).v = -x.v := rfl
@[simp] lemma smul_v (c : R) (x : H3A R h) : (c • x).v = c • x.v := rfl

lemma v_injective : Function.Injective (v : H3A R h → Fin 6 → R) :=
  fun a b hab => by cases a; cases b; simpa using hab

instance : AddCommGroup (H3A R h) :=
  v_injective.addCommGroup v rfl (fun _ _ => rfl) (fun _ => rfl)
    (fun _ _ => rfl) (fun _ _ => rfl) (fun _ _ => rfl)

/-- The additive-group hom onto NF coordinates (transport vehicle). -/
def vHom : H3A R h →+ (Fin 6 → R) :=
  { toFun := v, map_zero' := rfl, map_add' := fun _ _ => rfl }

instance : Module R (H3A R h) :=
  v_injective.module R vHom (fun _ _ => rfl)

instance : Mul (H3A R h) := ⟨fun x y => ⟨mulNF h x.v y.v⟩⟩
instance : One (H3A R h) := ⟨⟨unitNF⟩⟩

@[simp] lemma mul_v (x y : H3A R h) : (x * y).v = mulNF h x.v y.v := rfl
@[simp] lemma one_v : (1 : H3A R h).v = unitNF := rfl

private lemma mulNF_zero_left (h : R) (u : Fin 6 → R) : mulNF h 0 u = 0 := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁]

private lemma mulNF_zero_right (h : R) (u : Fin 6 → R) : mulNF h u 0 = 0 := by
  funext i; fin_cases i <;> simp [mulNF]

/-- **The H₃(q) NF module is a `Ring`** — multiplication `mulNF`, unit γ,
all laws discharged by the merged `HeckeH3AlgebraLaws`. -/
instance : Ring (H3A R h) where
  __ := (inferInstance : AddCommGroup (H3A R h))
  mul := (· * ·)
  one := 1
  mul_assoc a b c := H3A.ext (mulNF_assoc h a.v b.v c.v)
  one_mul a := H3A.ext (mulNF_one_left h a.v)
  mul_one a := H3A.ext (mulNF_one_right h a.v)
  left_distrib a b c := H3A.ext (mulNF_add_right h a.v b.v c.v)
  right_distrib a b c := H3A.ext (mulNF_add_left h a.v b.v c.v)
  zero_mul a := H3A.ext (mulNF_zero_left h a.v)
  mul_zero a := H3A.ext (mulNF_zero_right h a.v)

/-- **The H₃(q) NF module is an `R`-algebra** — scalar action compatible
with `mulNF` on both sides (the proved homogeneity laws). -/
instance : Algebra R (H3A R h) :=
  Algebra.ofModule
    (fun c x y => H3A.ext (mulNF_smul_left h c x.v y.v))
    (fun c x y => H3A.ext (mulNF_smul_right h c x.v y.v))

/-- The Markov trace on the wrapper, at Markov parameter `z`. -/
def trace (z : R) (x : H3A R h) : R := trM z h x.v

/-- **The FIRST instance of the `MarkovTrace` class** — the concrete n=3
Markov trace on `H3A R h` satisfies every class field: (M2) cyclicity from
`trM_cyclic`, (M1a) additivity from `trM_add`, (M1b) homogeneity from
`trM_smul`. The interface's "eventual instance" now exists, with real
content. -/
instance markovTrace_H3A (z : R) :
    QOU.Machinery.MarkovTrace R (H3A R h) (trace (h := h) z) where
  cyclic x y := trM_cyclic z h x.v y.v
  map_add x y := trM_add z h x.v y.v
  map_smul c x := trM_smul z h c x.v

end H3A

end QOU.Machinery.H3
