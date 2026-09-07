/-
# The Ptolemy variety with a μ₃-twist, and the relative step of the Sym² gate

## What this file is for

`ObstructionH2.lean` makes the PGL(3,ℂ) obstruction class well-defined in
`H²(Γ; ℤ/3)` and proves that a class cohomologous to its own negative vanishes.
That is the **absolute** half of the Sym² gate.  The Ptolemy obstruction, however,
is the **relative** class in `H²(M, ∂M; ℤ/3)`, and the step from one to the other
was the last gap.

That gap was closed *computationally* — negating the obstruction cocycle acts on
snappy's Ptolemy equations exactly as `u ↦ u²`, the nontrivial automorphism of
`μ₃` (`computations/ptolemy/ptolemy_duality_galois_check.py`, classes 1/2/3 of
L6a4).  This file lifts that step into Lean.

## What is proved here, and what is not

**Proved.**  For a system of equations of the shape snappy emits — a signed sum of
monomials in the Ptolemy coordinates, each term carrying a power of a primitive
cube root of unity — applying a ring endomorphism `σ` with `σ u = u²` to a solution
of the `c`-twisted system produces a solution of the `(−c)`-twisted system, and
conversely when `σ` is an isomorphism.  So `P^c` and `P^{−c}` have the same
`R`-points up to `σ`, and in particular one is empty iff the other is.

**Assumed, as an explicit hypothesis rather than derived.**  That snappy's
equations *have* this shape.  That is a measured fact about the generator, not a
theorem, and it is carried here as the structure `TwistedEq` rather than asserted.
The measurement:

```
- c_1002_1 * u^2 - c_1011_1 + c_1101_1 * u^2
  c_1002_5 * u^2 + c_1011_1 * u  + c_1101_6 * u^2
```

— 11 of L6a4 class 1's 33 equations carry `u`; every one is a signed sum of
monomials with `μ₃` coefficients.  The underlying Ptolemy relation is GGZ (5.2),
`c_{s+1001} c_{s+0110} + c_{s+1100} c_{s+0011} = c_{s+1010} c_{s+0101}`
(Garoufalidis–Goerner–Zickert, arXiv:1207.6711, Definition 5.1), which carries no
`u`; the cocycle enters through the face identifications.

**NOT established anywhere, here or elsewhere in this tranche.**  That the duality
involution `ρ ↦ ρ^{-T}` on representations *equals* this `σ`-transport on Ptolemy
coordinates.  The two ends meet at the level of *classes* — duality negates the
obstruction class (derived, absolute) and `σ`-transport negates it (proved here,
relative) — but the identification of the two maps on the variety itself is an
additional step that has not been taken.  Do not read `sigmaFixed_isSolution_neg`
below as saying a self-dual representation is a `σ`-fixed Ptolemy point; it says
what happens *if* it is.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Ring.Equiv
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring

namespace QOU.Eightfold.Ptolemy

open Finset

variable {R : Type*} [CommRing R]

/-! ## Powers of a primitive cube root of unity, indexed by `ZMod 3` -/

/-- `u ^ k` for an exponent `k : ZMod 3`, via the canonical representative in `{0,1,2}`.
Well-behaved exactly when `u ^ 3 = 1`. -/
def zpow3 (u : R) (k : ZMod 3) : R := u ^ k.val

@[simp] theorem zpow3_zero (u : R) : zpow3 u 0 = 1 := by
  simp [zpow3]

@[simp] theorem zpow3_one (u : R) : zpow3 u 1 = u := by
  simp [zpow3, show ((1 : ZMod 3)).val = 1 from rfl]

@[simp] theorem zpow3_base_one (k : ZMod 3) : zpow3 (1 : R) k = 1 := by
  simp [zpow3]

/-- **Negating the exponent is squaring.**  Over `μ₃`, `u^{-k} = u^{2k} = (u^k)²`.
This is the arithmetic content of the measured substitution `u ↦ u²`. -/
theorem zpow3_neg (u : R) (hu : u ^ 3 = 1) (k : ZMod 3) :
    zpow3 u (-k) = (zpow3 u k) ^ 2 := by
  have h4 : u ^ 4 = u := by
    have h : u ^ 4 = u ^ 3 * u := by ring
    rw [h, hu, one_mul]
  have hk : ∀ j : ZMod 3, j = 0 ∨ j = 1 ∨ j = 2 := by decide
  rcases hk k with rfl | rfl | rfl
  · simp
  · show u ^ ((-1 : ZMod 3)).val = (u ^ ((1 : ZMod 3)).val) ^ 2
    rw [show ((-1 : ZMod 3)).val = 2 from by decide,
        show ((1 : ZMod 3)).val = 1 from by decide]
    ring
  · show u ^ ((-2 : ZMod 3)).val = (u ^ ((2 : ZMod 3)).val) ^ 2
    rw [show ((-2 : ZMod 3)).val = 1 from by decide,
        show ((2 : ZMod 3)).val = 2 from by decide,
        show ((u : R) ^ 2) ^ 2 = u ^ 4 from by ring, h4, pow_one]

/-- A ring endomorphism sending `u` to `u²` sends `u^k` to `u^{-k}`. -/
theorem map_zpow3 (σ : R →+* R) (u : R) (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2) (k : ZMod 3) :
    σ (zpow3 u k) = zpow3 u (-k) := by
  rw [zpow3_neg u hu]
  simp only [zpow3]
  rw [map_pow, hσ]
  ring

/-! ## Ptolemy equations with a `μ₃` twist -/

/-- One equation of a Ptolemy variety carrying a `μ₃`-twist: a signed sum of monomials
in the Ptolemy coordinates `V`, each term weighted by a power of the primitive cube root
of unity.  The `twist` field **is** the obstruction cocycle's contribution.

This is a *description of the shape* snappy's equations were measured to have — see the
file header.  Nothing here claims that description is complete or canonical; it is the
hypothesis under which the transport theorem below applies. -/
structure TwistedEq (V : Type*) where
  /-- number of terms -/
  card : ℕ
  /-- the integer coefficient of each term (in practice `±1`) -/
  sign : Fin card → ℤ
  /-- the exponent of `u` on each term — the obstruction cocycle -/
  twist : Fin card → ZMod 3
  /-- the monomial of each term, as exponents on the Ptolemy coordinates -/
  mono : Fin card → V → ℕ

namespace TwistedEq

variable {V : Type*} [Fintype V]

/-- Evaluate the equation at a point `x : V → R` with cube root of unity `u`. -/
def eval (E : TwistedEq V) (u : R) (x : V → R) : R :=
  ∑ i : Fin E.card, (E.sign i : R) * zpow3 u (E.twist i) * ∏ v, x v ^ E.mono i v

/-- The same equation with the obstruction cocycle negated: `c ↦ -c`. -/
def negTwist (E : TwistedEq V) : TwistedEq V :=
  { E with twist := fun i => -E.twist i }

omit [Fintype V] in
@[simp] theorem negTwist_card (E : TwistedEq V) : E.negTwist.card = E.card := rfl

omit [Fintype V] in
@[simp] theorem negTwist_negTwist (E : TwistedEq V) : E.negTwist.negTwist = E := by
  cases E
  simp [negTwist]

/-- **The relative step.**  Applying a ring endomorphism that inverts the cube root of
unity to a point of the `c`-twisted equation evaluates the `(−c)`-twisted equation.

This is the Lean form of the measured statement *"substituting `u ↦ u²` throughout `P^c`
reproduces `P^{−c}` exactly as polynomial sets"* — with the substitution acting on the
point rather than on the coefficients, which is the same map read on the other side. -/
theorem eval_negTwist (σ : R →+* R) (u : R) (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2)
    (E : TwistedEq V) (x : V → R) :
    E.negTwist.eval u (fun v => σ (x v)) = σ (E.eval u x) := by
  simp only [eval, negTwist, map_sum, map_mul, map_intCast, map_prod, map_pow]
  refine Finset.sum_congr rfl ?_
  intro i _
  rw [map_zpow3 σ u hu hσ]

end TwistedEq

/-! ## Systems, and transport of solutions -/

variable {V I : Type*} [Fintype V]

/-- A point `x` solves the system `S`. -/
def IsSolution (S : I → TwistedEq V) (u : R) (x : V → R) : Prop :=
  ∀ i, (S i).eval u x = 0

/-- The system with the obstruction cocycle negated — snappy's `P^{−c}`. -/
def negSystem (S : I → TwistedEq V) : I → TwistedEq V := fun i => (S i).negTwist

omit [Fintype V] in
@[simp] theorem negSystem_negSystem (S : I → TwistedEq V) :
    negSystem (negSystem S) = S := by
  funext i
  simp [negSystem]

/-- **Transport.**  `σ` carries a solution of `P^c` to a solution of `P^{−c}`. -/
theorem isSolution_negSystem (σ : R →+* R) (u : R) (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2)
    (S : I → TwistedEq V) (x : V → R) (h : IsSolution S u x) :
    IsSolution (negSystem S) u (fun v => σ (x v)) := by
  intro i
  rw [negSystem, TwistedEq.eval_negTwist σ u hu hσ, h i, map_zero]

/-- `σ` inverts `u`, hence so does `σ⁻¹`: from `σ u = u²` and `u³ = 1`, `σ (u²) = u⁴ = u`. -/
theorem symm_apply_eq_sq (σ : R ≃+* R) (u : R) (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2) :
    σ.symm u = u ^ 2 := by
  have h : σ (u ^ 2) = u := by
    rw [map_pow, hσ, show ((u : R) ^ 2) ^ 2 = u ^ 3 * u from by ring, hu, one_mul]
  calc σ.symm u = σ.symm (σ (u ^ 2)) := by rw [h]
    _ = u ^ 2 := σ.symm_apply_apply _

/-- **Transport is reversible** for an injective `σ`: a point of `P^c` and its image in
`P^{−c}` determine each other, so neither variety is "more empty" than the other. -/
theorem isSolution_negSystem_iff (σ : R →+* R) (hinj : Function.Injective σ) (u : R)
    (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2) (S : I → TwistedEq V) (x : V → R) :
    IsSolution (negSystem S) u (fun v => σ (x v)) ↔ IsSolution S u x := by
  constructor
  · intro h i
    have hi := h i
    rw [show negSystem S i = (S i).negTwist from rfl,
        TwistedEq.eval_negTwist σ u hu hσ] at hi
    exact (map_eq_zero_iff σ hinj).mp hi
  · exact fun h => isSolution_negSystem σ u hu hσ S x h

/-- **Non-emptiness is invariant.**  `P^c` has an `R`-point iff `P^{−c}` does.

This is what retires the compute question for the Sym² gate: whatever is true of one
twist is true of its negative, so the thirteen nontrivial L6a4 classes cannot be
separated from each other by emptiness alone. -/
theorem exists_isSolution_negSystem_iff (σ : R ≃+* R) (u : R) (hu : u ^ 3 = 1)
    (hσ : σ u = u ^ 2) (S : I → TwistedEq V) :
    (∃ x, IsSolution (negSystem S) u x) ↔ (∃ x, IsSolution S u x) := by
  constructor
  · rintro ⟨y, hy⟩
    have hs : ((σ.symm : R ≃+* R) : R →+* R) u = u ^ 2 := symm_apply_eq_sq σ u hu hσ
    have h := isSolution_negSystem ((σ.symm : R ≃+* R) : R →+* R) u hu hs (negSystem S) y hy
    rw [negSystem_negSystem] at h
    exact ⟨_, h⟩
  · rintro ⟨x, hx⟩
    have hs : ((σ : R ≃+* R) : R →+* R) u = u ^ 2 := hσ
    exact ⟨_, isSolution_negSystem ((σ : R ≃+* R) : R →+* R) u hu hs S x hx⟩

/-- **The trivial cocycle is its own negative.**  At `u = 1` — the trivial obstruction
class — the twisted and negatively-twisted systems are literally the same equations, so
transport is the identity and no `σ` is needed.

This is the Lean counterpart of the one fixed point of `c ↦ -c` measured in
`computations/ptolemy/obstruction_gerbe_involution.py`: `H²(M, ∂M; ℤ/3) ≅ (ℤ/3)³` has
order 27 and exactly one element with `c = -c`, the trivial one.  It is also why the
argument concludes what it does — the *only* class a self-dual representation could
carry is the one this lemma is about. -/
theorem eval_negTwist_one (E : TwistedEq V) (x : V → R) :
    E.negTwist.eval (1 : R) x = E.eval (1 : R) x := by
  simp [TwistedEq.eval, TwistedEq.negTwist]

/-- **A `σ`-fixed point lies in both varieties.**  If every Ptolemy coordinate of `x` is
fixed by `σ`, then `x` solves `P^c` and `P^{−c}` simultaneously.

⚠ Read the file header before using this as the Sym² gate.  It says what follows *if* a
self-dual representation gives a `σ`-fixed Ptolemy point; that identification is **not**
established in this corpus.  The gate as actually argued runs through the obstruction
*class* (`ObstructionH2.cls_eq_zero_of_cohomologous_neg`), not through this lemma. -/
theorem sigmaFixed_isSolution_neg (σ : R →+* R) (u : R) (hu : u ^ 3 = 1) (hσ : σ u = u ^ 2)
    (S : I → TwistedEq V) (x : V → R) (hx : ∀ v, σ (x v) = x v)
    (h : IsSolution S u x) :
    IsSolution (negSystem S) u x := by
  have hfx : (fun v => σ (x v)) = x := funext hx
  have := isSolution_negSystem σ u hu hσ S x h
  rwa [hfx] at this

/-! ## A concrete instance: one measured L6a4 class-1 equation

The point of this section is **non-vacuity**.  A transport theorem about an empty or
degenerate structure proves nothing, so here is a real equation from the generator, with
its negated twist computed by `decide` rather than asserted. -/

section Measured

/-- The three Ptolemy coordinates appearing in the measured equation. -/
abbrev L6a4Coord := Fin 3

/-- snappy's `- c_1002_1 * u^2 - c_1011_1 + c_1101_1 * u^2`, one of the 11 `u`-bearing
equations among L6a4 class 1's 33, transcribed as a `TwistedEq`: signs `(-1,-1,+1)`,
cocycle exponents `(2,0,2)`, each monomial a single coordinate. -/
def sampleEq : TwistedEq L6a4Coord where
  card := 3
  sign := ![-1, -1, 1]
  twist := ![2, 0, 2]
  mono := ![fun v => if v = 0 then 1 else 0,
            fun v => if v = 1 then 1 else 0,
            fun v => if v = 2 then 1 else 0]

/-- Negating the cocycle sends the exponents `(2,0,2)` to `(1,0,1)` — i.e. to snappy's
`- c_1002_1 * u - c_1011_1 + c_1101_1 * u`, which is what the generator emits for the
negated class.  Checked by `decide`, not asserted. -/
example : sampleEq.negTwist.twist = ![1, 0, 1] := by
  funext i
  fin_cases i <;> simp only [sampleEq, TwistedEq.negTwist] <;> decide

/-- `negTwist` really negates, at every term. -/
theorem negTwist_twist (E : TwistedEq L6a4Coord) (i : Fin E.negTwist.card) :
    E.negTwist.twist i = -E.twist i := rfl

/-- **The twist genuinely changes.**  `(1,0,1) ≠ (2,0,2)`, so `P^c` and `P^{-c}` are not
the same written system, `negTwist` is not the identity, and the transport theorem is not
vacuous.  This is the Lean counterpart of the measurement that **10 of 33** equations
differ between the two. -/
example : (![1, 0, 1] : Fin 3 → ZMod 3) ≠ ![2, 0, 2] := by
  intro h
  have h0 := congrFun h 0
  simp only [Matrix.cons_val_zero] at h0
  exact absurd h0 (by decide)

end Measured

end QOU.Eightfold.Ptolemy
