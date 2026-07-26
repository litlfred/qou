/-
# H₄(q) as a genuine `Ring`/`Algebra` — the n=4 `MarkovTrace` class instance

W4 slice 1 of the epic `qou-utb3`, closing route (b) of
`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md` §3: the n=4
mirror of `HeckeH3AlgebraInstance`.  `HeckeH4AlgebraLaws` certified the Fin-24
NF module's algebra-object laws (unit, generator commutation, associativity;
bilinearity lives in `MarkovTraceH4`); `MarkovTraceH4Gram` closed trace
cyclicity sorry-free (`trM_cyclic_proved`).  This file packages them as
typeclass instances, producing:

* `H4A R h` — a wrapper type for the H₄(q) NF module (parameter `h = q − q⁻¹`
  pins the product), with `AddCommGroup`, `Module R`, **`Ring`**, and
  **`Algebra R`** instances whose multiplication is the proved `mulNF`;
* **the n=4 instance of the `MarkovTrace` class** —
  `markovTrace_H4A : MarkovTrace R (H4A R h) (trace z)` — every field
  (cyclicity, additivity, R-homogeneity) discharged by the proved H₄ laws:
  (M2) from `trM_cyclic_proved` (Gram closure), (M1a) from `trM_add`,
  (M1b) from `trM_smul`.  The class is now inhabited at n = 2, 3, 4.

Per the W1 audit, the class needs **cyclicity + R-linearity only** — Wenzl
positivity is surplus (not a field, not expressible over `[CommRing R]`), so
nothing archimedean enters here.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): instantiating
`MarkovTrace` at n=4 is proved content, not a conjecture-class discharge.
The OPEN items are unchanged: general-n `HeckeBraidedPresentation` /
`MarkovStabilization` (H_∞ binders — no finite-level instance possible, per
`HeckeH3AlgebraLaws`), and n ≥ 5 instances via the Ocneanu
conditional-expectation tower (W2/W3, beans `qou-2017` / `qou-r765`).
Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): generic `[CommRing R]` throughout — no `ℝ`, no positivity.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.MarkovTraceH4Gram
import QOU.Machinery.HeckeH4AlgebraLaws
import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.Algebra.Module.Pi

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-- Wrapper for the H₄(q) NF module: a distinct type carrying the `mulNF h`
ring structure. The parameter `h = q − q⁻¹` pins the product. -/
@[ext]
structure H4A (R : Type*) [CommRing R] (h : R) where
  /-- NF coordinates on the 24-element GB normal-form basis of `H₄(q)`. -/
  v : Fin 24 → R

namespace H4A

variable {h : R}

instance : Zero (H4A R h) := ⟨⟨0⟩⟩
instance : Add (H4A R h) := ⟨fun x y => ⟨x.v + y.v⟩⟩
instance : Neg (H4A R h) := ⟨fun x => ⟨-x.v⟩⟩
instance : Sub (H4A R h) := ⟨fun x y => ⟨x.v - y.v⟩⟩
instance : SMul ℕ (H4A R h) := ⟨fun n x => ⟨n • x.v⟩⟩
instance : SMul ℤ (H4A R h) := ⟨fun n x => ⟨n • x.v⟩⟩
instance : SMul R (H4A R h) := ⟨fun c x => ⟨c • x.v⟩⟩

@[simp] lemma zero_v : (0 : H4A R h).v = 0 := rfl
@[simp] lemma add_v (x y : H4A R h) : (x + y).v = x.v + y.v := rfl
@[simp] lemma neg_v (x : H4A R h) : (-x).v = -x.v := rfl
@[simp] lemma smul_v (c : R) (x : H4A R h) : (c • x).v = c • x.v := rfl

lemma v_injective : Function.Injective (v : H4A R h → Fin 24 → R) :=
  fun a b hab => by cases a; cases b; simpa using hab

instance : AddCommGroup (H4A R h) :=
  v_injective.addCommGroup v rfl (fun _ _ => rfl) (fun _ => rfl)
    (fun _ _ => rfl) (fun _ _ => rfl) (fun _ _ => rfl)

/-- The additive-group hom onto NF coordinates (transport vehicle). -/
def vHom : H4A R h →+ (Fin 24 → R) :=
  { toFun := v, map_zero' := rfl, map_add' := fun _ _ => rfl }

instance : Module R (H4A R h) :=
  v_injective.module R vHom (fun _ _ => rfl)

instance : Mul (H4A R h) := ⟨fun x y => ⟨mulNF h x.v y.v⟩⟩
instance : One (H4A R h) := ⟨⟨unitNF⟩⟩

@[simp] lemma mul_v (x y : H4A R h) : (x * y).v = mulNF h x.v y.v := rfl
@[simp] lemma one_v : (1 : H4A R h).v = unitNF := rfl

/-- **The H₄(q) NF module is a `Ring`** — multiplication `mulNF`, unit γ,
all laws discharged by `HeckeH4AlgebraLaws` + the `MarkovTraceH4`
bilinearity block. -/
instance : Ring (H4A R h) where
  __ := (inferInstance : AddCommGroup (H4A R h))
  mul := (· * ·)
  one := 1
  mul_assoc a b c := H4A.ext (mulNF_assoc h a.v b.v c.v)
  one_mul a := H4A.ext (mulNF_one_left h a.v)
  mul_one a := H4A.ext (mulNF_one_right h a.v)
  left_distrib a b c := H4A.ext (mulNF_add_right h a.v b.v c.v)
  right_distrib a b c := H4A.ext (mulNF_add_left h a.v b.v c.v)
  zero_mul a := H4A.ext (mulNF_zero_left h a.v)
  mul_zero a := H4A.ext (mulNF_zero_right h a.v)

/-- **The H₄(q) NF module is an `R`-algebra** — scalar action compatible
with `mulNF` on both sides (the proved homogeneity laws). -/
instance : Algebra R (H4A R h) :=
  Algebra.ofModule
    (fun c x y => H4A.ext (mulNF_smul_left h c x.v y.v))
    (fun c x y => H4A.ext (mulNF_smul_right h c x.v y.v))

/-- The Markov trace on the wrapper, at Markov parameter `z`. -/
def trace (z : R) (x : H4A R h) : R := trM z h x.v

/-- **The n=4 instance of the `MarkovTrace` class** — the concrete H₄(q)
Markov trace on `H4A R h` satisfies every class field: (M2) cyclicity from
the Gram closure `trM_cyclic_proved`, (M1a) additivity from `trM_add`,
(M1b) homogeneity from `trM_smul`.  Together with `H2A`/`H3A` the class is
inhabited at n = 2, 3, 4; the general-n route (Ocneanu tower) is W2/W3. -/
instance markovTrace_H4A (z : R) :
    QOU.Machinery.MarkovTrace R (H4A R h) (trace (h := h) z) where
  cyclic x y := trM_cyclic_proved z h x.v y.v
  map_add x y := trM_add z h x.v y.v
  map_smul c x := trM_smul z h c x.v

end H4A

end QOU.Machinery.H4
