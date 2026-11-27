/-
  # The Goldman–Iwahori involution of `H_n(R, q)` is an outer automorphism

  Part 2 of `docs/audits/2026-11-27-observer-intent-outer-automorphisms.md`.

  `H_n(R, q)` is presented here directly, as the quotient of the free algebra on
  `m = n − 1` generators `σ_i` by

  * the Hecke relation `σ_i² = h·σ_i + 1`, with `h = q − q'` and `q·q' = 1`
    (convention `(σ − q)(σ + q⁻¹) = 0`);
  * far commutation `σ_i σ_j = σ_j σ_i` for `|i − j| ≥ 2`;
  * the braid relation `σ_i σ_j σ_i = σ_j σ_i σ_j` for `|i − j| = 1`.

  Since `σ_i⁻¹ = σ_i − h`, the Goldman–Iwahori map `θ(σ_i) = −σ_i⁻¹` is the
  polynomial map `σ_i ↦ h − σ_i`, so no inverses are needed to define it.

  Results (all sorry-free, generic `CommRing R`, `q` a unit through `q·q' = 1`):

  * `theta`: `θ` is an `R`-algebra automorphism (an involution, `theta_theta`).
  * `trivialChar`: the trivial character `ε₊(σ_i) = q` exists.
  * `trivialChar_theta_gen`: `ε₊(θ σ_i) = −q'` (`= −q⁻¹`).
  * `theta_not_inner`: if `q + q' ≠ 0` and there is at least one generator
    (`n ≥ 2`), `θ` is not of the form `x ↦ u x u⁻¹` for any unit `u`. The argument
    is the one in the owner discussion: inner automorphisms fix every character
    with values in a commutative ring.
  * `trace_theta_invariant_iff`: a linear functional `t` with `t 1 = 1`,
    `t σ_i = z` is `θ`-invariant on that generator only if `2z = h`. With the
    convention-D Markov parameter `z = q³/(q² + 1)` this forces `q⁴ = −1`
    (`convD_theta_forces`). So `θ` fails to preserve `tr_D` already at `n = 2`,
    not only for `n ≥ 3` as the discussion stated.

  -- Ref: [leitner2026] def:observation, rem:two-observer-parallelogram
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import Mathlib.Tactic.NoncommRing

set_option autoImplicit false

namespace QOU.GoldmanIwahori

variable (R : Type*) [CommRing R] (m : ℕ) (q q' : R)

/-- The defining relations of `H_{m+1}(R, q)` on the free algebra over `Fin m`. -/
inductive HeckeRel : FreeAlgebra R (Fin m) → FreeAlgebra R (Fin m) → Prop
  | hecke (i : Fin m) :
      HeckeRel (FreeAlgebra.ι R i * FreeAlgebra.ι R i)
        ((q - q') • FreeAlgebra.ι R i + 1)
  | far (i j : Fin m) (h : (i : ℕ) + 2 ≤ j) :
      HeckeRel (FreeAlgebra.ι R i * FreeAlgebra.ι R j)
        (FreeAlgebra.ι R j * FreeAlgebra.ι R i)
  | braid (i j : Fin m) (h : (i : ℕ) + 1 = j) :
      HeckeRel (FreeAlgebra.ι R i * FreeAlgebra.ι R j * FreeAlgebra.ι R i)
        (FreeAlgebra.ι R j * FreeAlgebra.ι R i * FreeAlgebra.ι R j)

/-- The Iwahori–Hecke algebra `H_{m+1}(R, q)` with `m` generators. -/
abbrev Hecke := RingQuot (HeckeRel R m q q')

variable {R m q q'}

/-- The generator `σ_i`. -/
def gen (i : Fin m) : Hecke R m q q' :=
  RingQuot.mkAlgHom R (HeckeRel R m q q') (FreeAlgebra.ι R i)

/-- The relations hold in `H`. -/
theorem gen_sq (i : Fin m) :
    gen (q := q) (q' := q') i * gen i = (q - q') • gen i + 1 := by
  have := RingQuot.mkAlgHom_rel R (HeckeRel.hecke (R := R) (m := m) (q := q) (q' := q') i)
  simpa [gen, map_mul, map_add, map_smul, map_one] using this

theorem gen_far (i j : Fin m) (h : (i : ℕ) + 2 ≤ j) :
    gen (q := q) (q' := q') i * gen j = gen j * gen i := by
  have := RingQuot.mkAlgHom_rel R (HeckeRel.far (R := R) (q := q) (q' := q') i j h)
  simpa [gen, map_mul] using this

theorem gen_braid (i j : Fin m) (h : (i : ℕ) + 1 = j) :
    gen (q := q) (q' := q') i * gen j * gen i = gen j * gen i * gen j := by
  have := RingQuot.mkAlgHom_rel R (HeckeRel.braid (R := R) (q := q) (q' := q') i j h)
  simpa [gen, map_mul] using this

/-- Algebra maps out of `H` agree when they agree on generators. -/
theorem hom_ext {B : Type*} [Semiring B] [Algebra R B]
    {f g : Hecke R m q q' →ₐ[R] B} (w : ∀ i, f (gen i) = g (gen i)) : f = g := by
  apply RingQuot.ringQuot_ext'
  apply FreeAlgebra.hom_ext
  funext i
  exact w i

/-- Universal property: generators in `B` satisfying the relations give an algebra map. -/
def lift {B : Type*} [Ring B] [Algebra R B] (s : Fin m → B)
    (hsq : ∀ i, s i * s i = (q - q') • s i + 1)
    (hfar : ∀ i j : Fin m, (i : ℕ) + 2 ≤ j → s i * s j = s j * s i)
    (hbr : ∀ i j : Fin m, (i : ℕ) + 1 = j → s i * s j * s i = s j * s i * s j) :
    Hecke R m q q' →ₐ[R] B :=
  RingQuot.liftAlgHom R
    ⟨FreeAlgebra.lift R s, by
      intro x y hxy
      cases hxy with
      | hecke i => simp [hsq]
      | far i j h => simp [hfar i j h]
      | braid i j h => simp [hbr i j h]⟩

@[simp] theorem lift_gen {B : Type*} [Ring B] [Algebra R B] (s : Fin m → B) (hsq hfar hbr)
    (i : Fin m) : lift (q := q) (q' := q') s hsq hfar hbr (gen i) = s i := by
  simp [lift, gen]

/-! ## Algebra in a ring with a Hecke-type generator -/

section Ring

variable {A : Type*} [Ring A] [Algebra R A]

/-- `σ (σ − h) = 1` from the Hecke relation. -/
theorem mul_sub_h {h : R} {a : A} (H : a * a = h • a + 1) :
    a * (a - algebraMap R A h) = 1 := by
  rw [mul_sub, H, ← Algebra.commutes, ← Algebra.smul_def]; abel

theorem sub_h_mul {h : R} {a : A} (H : a * a = h • a + 1) :
    (a - algebraMap R A h) * a = 1 := by
  rw [sub_mul, H, ← Algebra.smul_def]; abel

/-- `h − σ` satisfies the same Hecke relation as `σ`. -/
theorem theta_hecke {h : R} {a : A} (H : a * a = h • a + 1) :
    (algebraMap R A h - a) * (algebraMap R A h - a)
      = h • (algebraMap R A h - a) + 1 := by
  have hc : a * algebraMap R A h = algebraMap R A h * a := (Algebra.commutes h a).symm
  have e : (algebraMap R A h - a) * (algebraMap R A h - a)
      = algebraMap R A h * algebraMap R A h - algebraMap R A h * a
          - a * algebraMap R A h + a * a := by noncomm_ring
  rw [e, H, hc, Algebra.smul_def, Algebra.smul_def, mul_sub]
  abel

/-- The braid relation is preserved by `σ ↦ h − σ` (it is `σ ↦ −σ⁻¹`). -/
theorem theta_braid {h : R} {a b : A} (Ha : a * a = h • a + 1) (Hb : b * b = h • b + 1)
    (Hab : a * b * a = b * a * b) :
    (algebraMap R A h - a) * (algebraMap R A h - b) * (algebraMap R A h - a)
      = (algebraMap R A h - b) * (algebraMap R A h - a) * (algebraMap R A h - b) := by
  -- `x := (a−h)(b−h)(a−h)` is a left inverse of `w := aba`, and
  -- `y := (b−h)(a−h)(b−h)` is a right inverse of `w = bab`; so `x = y`.
  set ai := a - algebraMap R A h
  set bi := b - algebraMap R A h
  have la : ai * a = 1 := sub_h_mul Ha
  have ra : a * ai = 1 := mul_sub_h Ha
  have lb : bi * b = 1 := sub_h_mul Hb
  have rb : b * bi = 1 := mul_sub_h Hb
  have hx : ai * bi * ai * (a * b * a) = 1 := by
    calc ai * bi * ai * (a * b * a) = ai * bi * (ai * a) * b * a := by noncomm_ring
      _ = ai * (bi * b) * a := by rw [la]; noncomm_ring
      _ = 1 := by rw [lb, mul_one, la]
  have hy : (b * a * b) * (bi * ai * bi) = 1 := by
    calc (b * a * b) * (bi * ai * bi) = b * a * (b * bi) * ai * bi := by noncomm_ring
      _ = b * (a * ai) * bi := by rw [rb]; noncomm_ring
      _ = 1 := by rw [ra, mul_one, rb]
  have xy : ai * bi * ai = bi * ai * bi := by
    calc ai * bi * ai = ai * bi * ai * ((b * a * b) * (bi * ai * bi)) := by rw [hy, mul_one]
      _ = (ai * bi * ai * (a * b * a)) * (bi * ai * bi) := by rw [Hab]; noncomm_ring
      _ = bi * ai * bi := by rw [hx, one_mul]
  -- `h − σ = −(σ − h)`, and three sign flips agree on both sides.
  have ea : algebraMap R A h - a = -ai := by simp [ai]
  have eb : algebraMap R A h - b = -bi := by simp [bi]
  rw [ea, eb]; simp only [neg_mul, mul_neg, neg_neg]; rw [xy]

end Ring

/-! ## The involution θ -/

variable (hq : q * q' = 1)

/-- The images `θ(σ_i) = h − σ_i` (= `−σ_i⁻¹`). -/
def thetaGen (i : Fin m) : Hecke R m q q' := algebraMap R _ (q - q') - gen i

theorem thetaGen_sq (i : Fin m) :
    thetaGen (q := q) (q' := q') i * thetaGen i = (q - q') • thetaGen i + 1 :=
  theta_hecke (gen_sq i)

theorem thetaGen_far (i j : Fin m) (h : (i : ℕ) + 2 ≤ j) :
    thetaGen (q := q) (q' := q') i * thetaGen j = thetaGen j * thetaGen i := by
  have hc : ∀ x : Hecke R m q q', algebraMap R _ (q - q') * x = x * algebraMap R _ (q - q') :=
    fun x => Algebra.commutes _ x
  simp only [thetaGen, sub_mul, mul_sub, gen_far i j h, hc]
  abel

theorem thetaGen_braid (i j : Fin m) (h : (i : ℕ) + 1 = j) :
    thetaGen (q := q) (q' := q') i * thetaGen j * thetaGen i
      = thetaGen j * thetaGen i * thetaGen j :=
  theta_braid (gen_sq i) (gen_sq j) (gen_braid i j h)

/-- The Goldman–Iwahori map as an algebra endomorphism. -/
def thetaHom : Hecke R m q q' →ₐ[R] Hecke R m q q' :=
  lift thetaGen thetaGen_sq thetaGen_far thetaGen_braid

@[simp] theorem thetaHom_gen (i : Fin m) :
    thetaHom (q := q) (q' := q') (gen i) = algebraMap R _ (q - q') - gen i := by
  simp [thetaHom, thetaGen]

theorem thetaHom_thetaHom :
    (thetaHom (m := m) (q := q) (q' := q')).comp thetaHom = AlgHom.id R _ := by
  apply hom_ext
  intro i
  simp [map_sub, AlgHom.commutes]

/-- **The Goldman–Iwahori involution `θ(σ_i) = −σ_i⁻¹` is an `R`-algebra automorphism
of `H_n(R, q)`** (for every `n`, generic commutative `R`). -/
def theta : Hecke R m q q' ≃ₐ[R] Hecke R m q q' :=
  AlgEquiv.ofAlgHom thetaHom thetaHom (thetaHom_thetaHom (m := m)) (thetaHom_thetaHom (m := m))

theorem theta_theta (x : Hecke R m q q') : theta (theta x) = x :=
  congrArg (fun f => f x) (congrArg DFunLike.coe (thetaHom_thetaHom (m := m)))

/-- `θ(σ_i) = −σ_i⁻¹`: indeed `σ_i·(−θ σ_i) = 1`. -/
theorem gen_mul_neg_theta (i : Fin m) :
    gen (q := q) (q' := q') i * (-(theta (gen i))) = 1 := by
  show gen i * -(thetaHom (gen i)) = 1
  rw [thetaHom_gen, neg_sub]; exact mul_sub_h (gen_sq i)

/-! ## The trivial character and non-innerness -/

include hq in
/-- The trivial character `ε₊(σ_i) = q`. -/
def trivialChar : Hecke R m q q' →ₐ[R] R :=
  lift (fun _ => q) (fun _ => by
      simp only [smul_eq_mul]; linear_combination hq)
    (fun _ _ _ => by ring) (fun _ _ _ => by ring)

include hq in
@[simp] theorem trivialChar_gen (i : Fin m) : trivialChar hq (gen (q := q) (q' := q') i) = q := by
  simp [trivialChar]

include hq in
/-- `ε₊(θ σ_i) = −q'`, i.e. `θ` moves the trivial character to the sign character. -/
theorem trivialChar_theta_gen (i : Fin m) :
    trivialChar hq (theta (gen (q := q) (q' := q') i)) = -q' := by
  show trivialChar hq (thetaHom (gen i)) = -q'
  rw [thetaHom_gen, map_sub, AlgHom.commutes, trivialChar_gen]
  simp

/-- An algebra map to a commutative ring is invariant under inner automorphisms. -/
theorem char_conj {B : Type*} [Ring B] [Algebra R B] (χ : B →ₐ[R] R) (u : Bˣ) (x : B) :
    χ (u * x * ↑u⁻¹) = χ x := by
  have hu : χ (u : B) * χ (↑u⁻¹ : B) = 1 := by rw [← map_mul, Units.mul_inv, map_one]
  rw [map_mul, map_mul]; linear_combination χ x * hu

include hq in
/-- **The Goldman–Iwahori involution is not inner** as soon as there is one generator
(`n ≥ 2`) and `[2]_q = q + q⁻¹ ≠ 0`. -/
theorem theta_not_inner (hm : 0 < m) (h2 : q + q' ≠ 0) :
    ¬ ∃ u : (Hecke R m q q')ˣ, ∀ x : Hecke R m q q', theta x = (u : Hecke R m q q') * x * ↑u⁻¹ := by
  rintro ⟨u, hu⟩
  let i : Fin m := ⟨0, hm⟩
  have e := congrArg (trivialChar hq) (hu (gen i))
  rw [char_conj, trivialChar_theta_gen, trivialChar_gen] at e
  exact h2 (by linear_combination -e)

/-! ## θ and the Markov trace -/

/-- A linear functional with `t 1 = 1`, `t σ_i = z` is `θ`-invariant at `σ_i` iff `2z = h`. -/
theorem trace_theta_invariant_iff (t : Hecke R m q q' →ₗ[R] R) (i : Fin m) {z : R}
    (h1 : t 1 = 1) (hz : t (gen i) = z) :
    t (theta (gen i)) = t (gen i) ↔ 2 * z = q - q' := by
  show t (thetaHom (gen i)) = _ ↔ _
  rw [thetaHom_gen, map_sub, Algebra.algebraMap_eq_smul_one, map_smul, h1, hz, smul_eq_mul,
    mul_one]
  constructor <;> intro e <;> linear_combination -e

/-- With the convention-D Markov parameter `z = q³/(q² + 1)`, `2z = q − q⁻¹` forces
`q⁴ = −1`. So `θ` does not preserve `tr_D` at any generic `q`, already in `H_2`. -/
theorem convD_theta_forces {K : Type*} [Field K] {q : K} (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (e : 2 * (q ^ 3 / (q ^ 2 + 1)) = q - q⁻¹) : q ^ 4 = -1 := by
  field_simp at e
  linear_combination e

end QOU.GoldmanIwahori
