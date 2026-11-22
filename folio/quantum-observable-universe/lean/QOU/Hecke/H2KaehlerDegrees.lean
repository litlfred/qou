import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.Tactic
import QOU.Hecke.InstanceH2

/-!
# `QOU.Hecke.H2KaehlerDegrees` — the fibre has no degrees, the tower does (the honest `HH_1` example)

`prop:spectral-sequence-collapse` asserts `HH^k(H_n(q)) = 0` for `k ≥ 1` at generic `q`
(Whitehead's lemma for a semisimple algebra). Its Lean carrier
`QOU.WedderburnMass.centralIdempotent_idem` proves idempotence of central idempotents and never
uses its `[WhiteheadHH]` instance — recorded twice as a defect
(`docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §2a). Mathlib has no
Hochschild (co)homology, so the collapse cannot be *stated* there yet.

This file does the one thing that CAN be stated and proved today, at `n = 2`, and it is the
statement the research doc (`docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`
§7 item 2) asks for: **the semisimple fibre has no first Hochschild degree, and the same algebra
over the tower ring does.**

## The mathematics, and what is cited rather than proved

For the *commutative* algebra `A_h := R[X]/(X² − h·X − 1)` (this is `H₂` with `h = q − q⁻¹`,
`QOU.Hecke.InstanceH2.H2`), the first Hochschild homology is the module of Kähler differentials,
`HH_1(A_h/R) ≅ Ω¹_{A_h/R}` (Hochschild–Kostant–Rosenberg degree one; for a commutative algebra this
is the elementary identification `HH_1 = Ω¹`, Weibel *An Introduction to Homological Algebra*
Prop. 9.4.3 / Loday *Cyclic Homology* 1.1.10), and for a monogenic algebra `R[X]/(f)`

    Ω¹_{A_h/R} ≅ A_h · dX / (f'(X) · dX) ≅ A_h / (f'(x))        with  f'(x) = 2x − h .

**Those two identifications are cited, not proved here** — Mathlib's `KaehlerDifferential` API for
a quotient of a polynomial ring was not exercised in this session, and no Hochschild framework
exists. What IS proved is everything about the module `A_h / (2x − h)` that the identification
turns into a statement about `HH_1`:

* `two_x_sub_h_sq` — the **discriminant identity** `(2x − h)² = h² + 4` in `A_h`. At `h = q − q⁻¹`
  this is `(q + q⁻¹)² = [2]_q²` (`two_x_sub_h_sq_hecke`): the Hochschild degree-one module is
  killed by the square of the quantum integer `[2]_q`.
* `kaehlerIdeal_eq_top_of_isUnit` — **the fibre has no degree**: if `h² + 4` (i.e. `[2]_q²`) is a
  unit of `R`, then `(2x − h) = A_h`, so `A_h/(2x − h) = 0`. This is the `n = 2` case of the
  collapse, over any ring in which `[2]_q` is invertible — in particular at every generic `q`,
  and at the substrate `q₀`.
* `kaehlerIdeal_ne_top_of_hom` — **the tower has one**: if some ring homomorphism `φ : R →+* K` to
  a field (with `2 ≠ 0` in `K`) sends `h² + 4 ↦ 0`, then `(2x − h) ≠ A_h` and the module is
  non-zero. For `R = ℤ[q, q⁻¹]` and `φ : q ↦ i` (a primitive fourth root of unity, `[2]_i = 0`)
  this says exactly that `HH_1(H₂ / ℤ[q^{±1}]) ≠ 0` — the algebra over the ring of the tower is
  **not** formal, and inverting `[2]_q` (passing to the fibre) is what kills the degree.

So the two theorems are the two halves of one sentence: *the degree the derived route needs
exists over `ℤ[q^{±1}]` and is destroyed by specialising to a generic fibre.* That is the
structural content of the research doc's §2, at the one `n` where the corpus has a genuine
`HeckeAlgebra` instance.

## What this does NOT claim

* Nothing about `n ≥ 3` (`H_n` is non-commutative there; `HH_1 ≠ Ω¹` and the corpus has no
  instance).
* Nothing about the *value* of a binding term. A non-zero `HH_1` is a place a many-body term
  could live; it is not a many-body term.
* Nothing about the GB filtration or the spectral sequence — see the GAP note in
  `mass-endomorphism/spectral-sequence-collapse.lean`, which stands.

Ground ring: generic `[CommRing R]` throughout (§7c); the non-vanishing witness needs a field
target only for `IsUnit 0 → False`. Bean `qou-onte` §7 item 2.
-/

namespace QOU.Hecke.H2KaehlerDegrees

open Polynomial

section Generic

variable {R : Type*} [CommRing R]

/-- The Hecke quadratic `X² − h·X − 1` with an arbitrary parameter `h`. At `h = q − q⁻¹` this is
`QOU.Hecke.InstanceH2.heckePoly` syntactically. -/
noncomputable def quadPoly (h : R) : R[X] := X ^ 2 - C h * X - 1

/-- `A_h := R[X]/(X² − h X − 1)` — the two-strand Hecke algebra with parameter `h`. -/
noncomputable abbrev Aq (h : R) : Type _ := AdjoinRoot (quadPoly h)

/-- The generator `x = σ₁`, the image of `X`. -/
noncomputable def x (h : R) : Aq h := AdjoinRoot.root (quadPoly h)

/-- The element `f'(x) = 2x − h` whose principal ideal presents `Ω¹_{A_h/R}`. -/
noncomputable def kaehlerGen (h : R) : Aq h := 2 * x h - algebraMap R (Aq h) h

/-- The ideal `(2x − h) ⊆ A_h`; `A_h / (2x − h) ≅ Ω¹_{A_h/R} ≅ HH_1(A_h/R)` (cited, see header). -/
noncomputable def kaehlerIdeal (h : R) : Ideal (Aq h) := Ideal.span {kaehlerGen h}

/-- The Hecke quadratic relation in `A_h`: `x² = h·x + 1`. -/
theorem x_sq (h : R) : x h * x h = algebraMap R (Aq h) h * x h + 1 := by
  have h0 : AdjoinRoot.mk (quadPoly h) (X ^ 2 - C h * X - 1) = 0 := AdjoinRoot.mk_self
  simp only [map_sub, map_pow, map_mul, map_one, AdjoinRoot.mk_X, AdjoinRoot.mk_C] at h0
  unfold x
  rw [AdjoinRoot.algebraMap_eq]
  linear_combination h0

/-- **The discriminant identity.** `(2x − h)² = h² + 4` in `A_h`. -/
theorem two_x_sub_h_sq (h : R) :
    kaehlerGen h ^ 2 = algebraMap R (Aq h) (h ^ 2 + 4) := by
  have hx := x_sq h
  unfold kaehlerGen
  simp only [map_add, map_pow, map_ofNat]
  linear_combination 4 * hx

/-- **The fibre has no degree.** If `h² + 4` is a unit of `R`, the ideal `(2x − h)` is the whole
of `A_h`, so `A_h/(2x − h) = 0`: `Ω¹ = HH_1 = 0` (cited identification). At `h = q − q⁻¹`, `h² + 4
= [2]_q²`, invertible at every generic `q`. -/
theorem kaehlerIdeal_eq_top_of_isUnit (h : R) (hu : IsUnit (h ^ 2 + 4)) :
    kaehlerIdeal h = ⊤ := by
  unfold kaehlerIdeal
  rw [Ideal.span_singleton_eq_top]
  have hsq : IsUnit (kaehlerGen h ^ 2) := by
    rw [two_x_sub_h_sq]
    exact hu.map (algebraMap R (Aq h))
  exact (isUnit_pow_iff two_ne_zero).mp hsq

/-- **The tower has one.** If a ring homomorphism `φ : R →+* K` into a field with `2 ≠ 0` sends
`h² + 4` to `0`, then `(2x − h) ≠ A_h`, so `A_h/(2x − h) ≠ 0`: `Ω¹ = HH_1 ≠ 0` (cited
identification). The witness is the evaluation `x ↦ φ(h)/2`, under which the quadratic becomes
`(X − φ(h)/2)²` and `2x − h ↦ 0`. -/
theorem kaehlerIdeal_ne_top_of_hom (h : R) {K : Type*} [Field K] (φ : R →+* K)
    (hφ : φ h ^ 2 + 4 = 0) (h2 : (2 : K) ≠ 0) :
    kaehlerIdeal h ≠ ⊤ := by
  -- the root `t = φ h / 2` of the pushed-forward quadratic
  set t : K := φ h / 2 with ht
  have hroot : (quadPoly h).eval₂ φ t = 0 := by
    simp only [quadPoly, eval₂_sub, eval₂_pow, eval₂_mul, eval₂_C, eval₂_X, eval₂_one]
    rw [ht]
    field_simp
    linear_combination (-1 : K) * hφ
  -- the evaluation homomorphism `A_h →+* K`
  let ψ : Aq h →+* K := AdjoinRoot.lift φ t hroot
  have hψ : ψ (kaehlerGen h) = 0 := by
    have e : ψ (kaehlerGen h) = 2 * t - φ h := by
      simp only [ψ, kaehlerGen, x, map_sub, map_mul, map_ofNat, AdjoinRoot.lift_root,
        AdjoinRoot.algebraMap_eq, AdjoinRoot.lift_of]
    rw [e, ht]
    field_simp
    ring
  intro htop
  unfold kaehlerIdeal at htop
  rw [Ideal.span_singleton_eq_top] at htop
  have hunit : IsUnit (ψ (kaehlerGen h)) := htop.map ψ
  rw [hψ] at hunit
  exact not_isUnit_zero hunit

end Generic

section Hecke

variable {K : Type*} [Field K]

/-- At the Hecke parameter `h = q − q⁻¹` (`q ≠ 0`), the discriminant is the square of the quantum
integer: `h² + 4 = (q + q⁻¹)² = [2]_q²`. -/
theorem heckeParam_sq_add_four (q : K) (hq : q ≠ 0) :
    QOU.Hecke.InstanceH2.heckeParam K q ^ 2 + 4 = (q + q⁻¹) ^ 2 := by
  unfold QOU.Hecke.InstanceH2.heckeParam
  field_simp
  ring

/-- The discriminant identity in the corpus's own `H₂(q)`: `(2σ₁ − h)² = [2]_q²`. The two-strand
Hecke algebra of `QOU.Hecke.InstanceH2` is `Aq (heckeParam K q)` definitionally. -/
theorem two_x_sub_h_sq_hecke (q : K) (hq : q ≠ 0) :
    kaehlerGen (QOU.Hecke.InstanceH2.heckeParam K q) ^ 2
      = algebraMap K (Aq (QOU.Hecke.InstanceH2.heckeParam K q)) ((q + q⁻¹) ^ 2) := by
  rw [two_x_sub_h_sq, heckeParam_sq_add_four q hq]

/-- **Generic `q` kills the degree.** If `[2]_q = q + q⁻¹ ≠ 0` (every generic `q`, and the
substrate `q₀`), the Kähler ideal of `H₂(q)` is everything: `HH_1(H₂(q)/K) = 0`. -/
theorem kaehlerIdeal_eq_top_of_qint_ne_zero (q : K) (hq : q ≠ 0) (h2 : q + q⁻¹ ≠ 0) :
    kaehlerIdeal (QOU.Hecke.InstanceH2.heckeParam K q) = ⊤ := by
  apply kaehlerIdeal_eq_top_of_isUnit
  rw [heckeParam_sq_add_four q hq]
  exact (isUnit_pow_iff two_ne_zero).mpr (isUnit_iff_ne_zero.mpr h2)

/-- **A fourth root of unity keeps it.** If `q² = −1` (so `[2]_q = 0`) and `2 ≠ 0` in `K`, the
Kähler ideal of `H₂(q)` is proper: `HH_1(H₂(q)/K) ≠ 0`. This is the `n = 2` shadow of the
non-semisimple root-of-unity fibre, and — read through `ℤ[q^{±1}] → K`, `q ↦ i` — of the
non-formality of the tower ring. -/
theorem kaehlerIdeal_ne_top_of_fourth_root (q : K) (hq2 : q ^ 2 = -1) (h2 : (2 : K) ≠ 0) :
    kaehlerIdeal (QOU.Hecke.InstanceH2.heckeParam K q) ≠ ⊤ := by
  have hq : q ≠ 0 := by
    intro h0
    rw [h0] at hq2
    norm_num at hq2
  apply kaehlerIdeal_ne_top_of_hom _ (RingHom.id K) _ h2
  simp only [RingHom.id_apply]
  rw [heckeParam_sq_add_four q hq]
  have hinv : q⁻¹ = -q := by
    field_simp
    linear_combination hq2
  rw [hinv]
  ring

end Hecke

end QOU.Hecke.H2KaehlerDegrees
