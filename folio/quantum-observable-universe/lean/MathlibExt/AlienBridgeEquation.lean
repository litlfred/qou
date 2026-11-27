/-
Copyright (c) 2026 litlfred. All rights reserved.

# Écalle's bridge equation as a hypothesis on the derivation system

[`AlienDerivation.lean`](AlienDerivation.lean) supplies a family of alien
derivations `Δ_ω` with no relation to a distinguished ordinary derivation `∂`.
Écalle's **bridge equation** is exactly such a relation:

    ∂ ∘ Δ_ω  −  Δ_ω ∘ ∂  =  ω · Δ_ω        (equivalently  ⁅∂, Δ_ω⁆ = ω · Δ_ω)

**It is a hypothesis, not a theorem here** — nothing in the present data
determines it, and per AGENTS.md §"Axiomatization is NOT a Proof" writing it as
an `axiom` would not establish it. So it is carried as a **field** on a bundled
system, and everything below is *derived from that field*: each theorem consumes
`bridge` and would fail without it. That is the §3b-cond non-degeneracy test —
the carrier holds the hypothesis, the theorems derive their conclusions.

**What the relation buys, once assumed.** Three consequences, all proved here:

* `weight_shift` — `Δ_ω` moves an `∂`-eigenvector of eigenvalue `λ` to one of
  eigenvalue `λ + ω`.  This is *why* alien derivatives detect instanton sectors:
  the `∂`-eigenvalue is the exponential weight `e^{λz}`, and `Δ_ω` is precisely
  the operator that steps it by `ω`, the location of the Borel singularity.
* `weight_add_of_comp` — weights **add** under composition, so the `Δ_ω` generate
  a weight-graded algebra rather than an unstructured family.
* `ord_dotted_comm` — the *dotted* alien derivative `Δ̇_ω := e_ω · Δ_ω`, where
  `e_ω` is the formal exponential `∂ e_ω = −ω · e_ω`, **commutes with `∂`**.  This
  is the bridge proper: it is what lets the `Δ_ω` be transported to the analytic
  side as ordinary commuting operators.

**And that the hypothesis has teeth:** `alien_eq_zero_of_ord_comm` shows the
bridge relation is *incompatible* with `∂` commuting with `Δ_ω` at nonzero
weight — at weight `ω ≠ 0` (acting injectively) commutation forces `Δ_ω = 0`.
So the field is a genuine constraint, not decoration; a system can satisfy it
non-trivially only by *failing* to commute, in the precise amount `ω`.

**What is NOT claimed.** That any particular analytic construction — in
particular the q-difference module C1 — satisfies this relation.  Recorded in
bean `qou-vkg5`: C1 cannot be confluenced to the classical setting
(`L1 → (x−1)σ²`, not rank 2, per
[`2026-08-08-rsz-c1-infinity-route-closed.md`](../../../../../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)),
so a classical bridge equation would not transfer to it even once proved.  A
q-native form of the relation is open.

§7c: generic `{R A : Type*} [CommSemiring R] [CommRing A] [Algebra R A]` — the
ring needs subtraction for the commutator, but no ordering and no `ℝ`.
Sorry-free.

-- Ref: [ecalle1981] Fonctions résurgentes, tome I
-- Ref: [sauzin2014] https://arxiv.org/abs/1405.0356
-/
import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Tactic

namespace QOU.Mathlib.AlienBridge

variable {R A Ω : Type*} [CommSemiring R] [CommRing A] [Algebra R A]

/-- An **alien derivation system carrying Écalle's bridge equation**: an ordinary
    derivation `∂`, a family of alien derivations `Δ_ω` indexed by `Ω`, a weight
    `ω ↦ weight ω ∈ R` recording each singularity's location, and the relation

    `∂(Δ_ω f) − Δ_ω(∂ f) = weight ω • Δ_ω f`.

    The relation is a **field**, i.e. a hypothesis on the system.  It is not
    derived from the other data and is not claimed of any particular analytic
    construction. -/
structure BridgeSystem (R A Ω : Type*) [CommSemiring R] [CommRing A]
    [Algebra R A] where
  /-- The ordinary derivation `∂`. -/
  ord : Derivation R A A
  /-- The alien derivation at the singularity `ω`. -/
  alien : Ω → Derivation R A A
  /-- The location of the singularity `ω`, as a scalar weight. -/
  weight : Ω → R
  /-- **Écalle's bridge equation.**  `⁅∂, Δ_ω⁆ = ω · Δ_ω`. -/
  bridge : ∀ (ω : Ω) (f : A),
    ord (alien ω f) - alien ω (ord f) = weight ω • alien ω f

namespace BridgeSystem

variable (S : BridgeSystem R A Ω) (ω ω' : Ω) (f : A)

/-- The bridge equation in solved form: `∂ ∘ Δ_ω = Δ_ω ∘ ∂ + ω · Δ_ω`. -/
theorem ord_alien (S : BridgeSystem R A Ω) (ω : Ω) (f : A) :
    S.ord (S.alien ω f) = S.alien ω (S.ord f) + S.weight ω • S.alien ω f :=
  sub_eq_iff_eq_add'.mp (S.bridge ω f)

/-- **The hypothesis has teeth.**  If `∂` commutes with `Δ_ω` and the weight acts
    injectively (in particular, if `weight ω` is a non-zero-divisor and nonzero),
    then `Δ_ω = 0`.

    So the bridge equation is a genuine constraint, not bookkeeping: a system can
    satisfy it with `Δ_ω ≠ 0` only by *failing* to commute, and by exactly the
    amount `ω`.  Recorded because a structure field that any system satisfies
    would make the theorems below vacuous. -/
theorem alien_eq_zero_of_ord_comm (S : BridgeSystem R A Ω) (ω : Ω)
    (hcomm : ∀ g : A, S.ord (S.alien ω g) = S.alien ω (S.ord g))
    (hw : ∀ x : A, S.weight ω • x = 0 → x = 0) (f : A) :
    S.alien ω f = 0 :=
  hw _ (by rw [← S.bridge ω f, hcomm f, sub_self])

/-- **Weight shift.**  `Δ_ω` carries an `∂`-eigenvector of eigenvalue `λ` to an
    `∂`-eigenvector of eigenvalue `λ + ω`.

    This is the structural reason alien derivatives detect instanton sectors: the
    `∂`-eigenvalue is the exponential weight `e^{λz}`, and `Δ_ω` steps it by
    exactly the Borel-singularity location `ω`. -/
theorem weight_shift (S : BridgeSystem R A Ω) (ω : Ω) {lam : R} {f : A}
    (hf : S.ord f = lam • f) :
    S.ord (S.alien ω f) = (lam + S.weight ω) • S.alien ω f := by
  rw [S.ord_alien ω f, hf, Derivation.map_smul, add_smul]

/-- **Weights add under composition.**  Applying `Δ_ω'` then `Δ_ω` shifts by
    `ω + ω'`, so the alien derivations generate a weight-graded algebra rather
    than an unstructured family.

    Derived from the bridge field twice plus `R`-linearity of `Δ_ω`; it is false
    without the field. -/
theorem weight_add_of_comp (S : BridgeSystem R A Ω) (ω ω' : Ω) (f : A) :
    S.ord (S.alien ω (S.alien ω' f))
      = S.alien ω (S.alien ω' (S.ord f))
        + (S.weight ω + S.weight ω') • S.alien ω (S.alien ω' f) := by
  rw [S.ord_alien ω (S.alien ω' f), S.ord_alien ω' f, Derivation.map_add,
    Derivation.map_smul, add_smul]
  abel

/-- **The bridge proper: the dotted alien derivative commutes with `∂`.**

    Let `e_ω` be a formal exponential of weight `−ω`, i.e. `∂ e_ω = −ω · e_ω`
    (think `e^{−ωz}`), and set `Δ̇_ω f := e_ω · Δ_ω f`.  Then

    `∂ ∘ Δ̇_ω = Δ̇_ω ∘ ∂`.

    The `ω` produced by the bridge equation is cancelled exactly by the `−ω` from
    differentiating `e_ω` — which is what the relation is *for*.  This is the
    step that lets the `Δ_ω` be transported to the analytic side as ordinary
    commuting operators.

    **Scope note.**  Unlike the other results here, this hypothesis is *not*
    witnessed by `polyEulerSystem` below: `R[X]` has no element of `∂`-eigenvalue
    `−n`, since the Euler operator's eigenvalues on `R[X]` are the degrees `≥ 0`.
    A witness needs negative weights, i.e. Laurent polynomials `R[t, t⁻¹]` with
    `e = t^{−n}`.  That model is not built here, so the theorem is proved but its
    hypothesis is so far only exhibited abstractly. -/
theorem ord_dotted_comm (S : BridgeSystem R A Ω) (ω : Ω) {e : A}
    (he : S.ord e = -(S.weight ω • e)) (f : A) :
    S.ord (e * S.alien ω f) = e * S.alien ω (S.ord f) := by
  rw [S.ord.leibniz, smul_eq_mul, smul_eq_mul, he, S.ord_alien ω f, mul_add,
    mul_neg, mul_smul_comm, mul_smul_comm, mul_comm (S.alien ω f) e]
  abel

/-- **The dotted derivative is exactly the correction term.**  Stated as the
    vanishing commutator, so the `= 0` shape is available for downstream Lie
    arguments. -/
theorem ord_dotted_comm' (S : BridgeSystem R A Ω) (ω : Ω) {e : A}
    (he : S.ord e = -(S.weight ω • e)) (f : A) :
    S.ord (e * S.alien ω f) - e * S.alien ω (S.ord f) = 0 :=
  sub_eq_zero_of_eq (S.ord_dotted_comm ω he f)

/-- **Weight zero is the degenerate case.**  At `weight ω = 0` the bridge
    equation says precisely that `Δ_ω` commutes with `∂` — the converse direction
    of `alien_eq_zero_of_ord_comm`, and a check that the sign and placement of the
    weight in the field are right. -/
theorem ord_comm_of_weight_zero (S : BridgeSystem R A Ω) (ω : Ω)
    (hw : S.weight ω = 0) (f : A) :
    S.ord (S.alien ω f) = S.alien ω (S.ord f) := by
  rw [S.ord_alien ω f, hw, zero_smul, add_zero]

end BridgeSystem

/-! ### A concrete non-trivial model — the Euler system

    Everything above is conditional on `BridgeSystem` being inhabited by
    something other than the zero family: a structure whose only model has
    `Δ_ω = 0` would make `weight_shift`, `weight_add_of_comp` and
    `ord_dotted_comm` true but empty.

    This section removes that doubt.  Any `(A, D, t)` with `D t = t` — an
    "Euler coordinate" — carries a bridge system on `Ω = ℕ` with `Δ_n := tⁿ · D`
    and weight `n`, and `Δ₁ t = t²` is nonzero whenever `t² ≠ 0`.  A concrete
    witness is `R[X]` with the Euler operator `X·d/dX` and `t = X`, where
    `t² = X² ≠ 0` for any nontrivial `R`.

    So the structure is inhabited at **nonzero** weight by a **nonzero** alien
    family — exactly the regime `alien_eq_zero_of_ord_comm` says commutation
    forbids. -/

/-- `D(tⁿ) = n · tⁿ` for an Euler coordinate `D t = t`.  The eigenvalue of `tⁿ`
    under `D` is its degree, which is what makes the weights come out as `ℕ`. -/
theorem deriv_pow_eq_nsmul (D : Derivation R A A) {t : A} (ht : D t = t) :
    ∀ n : ℕ, D (t ^ n) = n • t ^ n := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, D.leibniz, ih, ht]
    simp only [nsmul_eq_mul, smul_eq_mul, Nat.cast_add, Nat.cast_one]
    ring

/-- **The Euler bridge system.**  `Δ_n := tⁿ · D` with weight `n`, for any
    Euler coordinate `D t = t`.  The bridge equation holds *because* `D` scales
    `tⁿ` by `n`: differentiating past `tⁿ` produces exactly the `n · Δ_n` the
    relation demands. -/
noncomputable def eulerSystem (D : Derivation R A A) {t : A} (ht : D t = t) :
    BridgeSystem R A ℕ where
  ord := D
  alien n := t ^ n • D
  weight n := (n : R)
  bridge := by
    intro n f
    simp only [Derivation.smul_apply, smul_eq_mul, Nat.cast_smul_eq_nsmul]
    rw [D.leibniz, deriv_pow_eq_nsmul D ht n]
    simp only [smul_eq_mul, nsmul_eq_mul]
    ring

@[simp]
theorem eulerSystem_alien_apply (D : Derivation R A A) {t : A} (ht : D t = t)
    (n : ℕ) (f : A) :
    (eulerSystem D ht).alien n f = t ^ n * D f := by
  simp [eulerSystem, Derivation.smul_apply, smul_eq_mul]

/-- **The Euler system is non-trivial at weight 1.**  `Δ₁ t = t²`, so whenever
    `t² ≠ 0` the alien derivation at nonzero weight is nonzero.  This is the
    witness that the theorems above are not vacuous. -/
theorem eulerSystem_alien_one_self (D : Derivation R A A) {t : A} (ht : D t = t) :
    (eulerSystem D ht).alien 1 t = t ^ 2 := by
  rw [eulerSystem_alien_apply, ht]; ring

/-- Ordinary differentiation as a `Derivation` on `R[X]`.  Mathlib has
    `Polynomial.derivative` as a linear map and `derivative_mul` as the Leibniz
    rule, but does not package the two as a `Derivation`. -/
noncomputable def polyDerivation (R : Type*) [CommRing R] :
    Derivation R (Polynomial R) (Polynomial R) where
  toLinearMap := Polynomial.derivative
  map_one_eq_zero' := Polynomial.derivative_one
  leibniz' := fun a b => by
    simp only [Polynomial.derivative_mul, smul_eq_mul]
    ring

/-- The **Euler operator** `X·d/dX` on `R[X]` has `X` as an Euler coordinate. -/
theorem polyEuler_X (R : Type*) [CommRing R] :
    ((Polynomial.X : Polynomial R) • polyDerivation R) Polynomial.X
      = (Polynomial.X : Polynomial R) := by
  simp [Derivation.smul_apply, polyDerivation, smul_eq_mul]

/-- **A concrete inhabitant.**  `R[X]` with the Euler operator and `t = X`.
    Its `Δ₁` sends `X` to `X²`, which is nonzero for nontrivial `R` — so
    `BridgeSystem` has a model with nonzero weight and nonzero alien
    derivation. -/
noncomputable def polyEulerSystem (R : Type*) [CommRing R] :
    BridgeSystem R (Polynomial R) ℕ :=
  eulerSystem ((Polynomial.X : Polynomial R) • polyDerivation R) (polyEuler_X R)

theorem polyEulerSystem_alien_one_X (R : Type*) [CommRing R] [Nontrivial R] :
    (polyEulerSystem R).alien 1 Polynomial.X = (Polynomial.X : Polynomial R) ^ 2 :=
  eulerSystem_alien_one_self _ (polyEuler_X R)

/-- The witness is genuinely nonzero: `Δ₁ X = X² ≠ 0`. -/
theorem polyEulerSystem_alien_one_X_ne_zero (R : Type*) [CommRing R] [Nontrivial R] :
    (polyEulerSystem R).alien 1 Polynomial.X ≠ 0 := by
  rw [polyEulerSystem_alien_one_X]
  intro h
  have := congrArg (fun p => Polynomial.coeff p 2) h
  simp at this

end QOU.Mathlib.AlienBridge
