/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Tactic

/-!
# QOU.QBeta.A3AntiSelfAdjointLift — the A=3 lift is carried by ONE free anti-self-adjoint amplitude; the single door the merged A=3 program left open

**Scope (read this first).**  This file attacks the single surviving route named by
`QOU.QBeta.A3OffBlockDerivation` (ROUTE 2-b, merged 2026-08-02): that file *derived*
the self-adjoint branching off-blocks `B = C = (a−b)/2` and proved (scope-(b),
invariant `sq_nonneg`) that the resulting even-face factor is
`1 − ((a−b)/(a+b))² ≤ 1` — a **reduction**, so the observed lift `r* = μ₃/c₃ ≈ 1.585
> 1` is UNREACHABLE by the self-adjoint branching Schur complement.  It named the
ONLY door left open: an **anti-self-adjoint** off-block (`C ≠ −σB`, an amplitude the
categorical branching does not fix) — the DM q-cubic period / Yekutieli-Stokes datum
`conj:qdifference-kernel-prolongation-symbol` (bean `qou-jqof`).

**What this file adds (the sharp characterisation of the open door).**  Write the
actual off-block as its graded-self-adjoint value plus an *anti-self-adjoint
amplitude*:

  `C = −(σ B) + E`,   `E := C + σ B`  (the deviation from graded self-adjointness).

The self-adjoint branching pins `−(σ B)` (`A3OffBlockDerivation`); `E` is the
**only** freedom a lift can use.  The decisive algebra (Part 1,
`factor_affine_in_amplitude`, sorry-free): the even-face Berezinian factor is
**AFFINE** in `E`,

  `evenFaceCorrection A (crossTerm B (−σB + E) D)`
      `= evenFaceCorrection A (crossTerm B (−σB) D) − B·D⁻¹·E / A`
      `=  factor_sa                                  −  (slope)·E`,

with `factor_sa ≤ 1` the proved self-adjoint reduction and slope `B·D⁻¹/A`.  Three
consequences pin down the open door **exactly**:

* **Part 2 (`lift_forces_nonzero_amplitude`, sorry-free).**  A genuine lift `factor >
  1` FORCES `B·D⁻¹·E ≠ 0`, hence (with `B, D ≠ 0`) `E ≠ 0`
  (`amplitude_nonzero`): the lift is impossible without an anti-self-adjoint
  amplitude.  This is the Lean form of "the self-adjoint route is a reduction; the
  lift lives entirely in the amplitude the branching leaves free."
* **Part 3 (`amplitude_surjective`, sorry-free).**  For fixed background `A, B, D`
  (`≠ 0`) the map `E ↦ factor` is **surjective** onto `R`: EVERY target — `r*`
  included — is reachable by a suitable `E`, witness `E* = (factor_sa − r)·A·D·B⁻¹`.
  So the anti-self-adjoint route is **NOT scope-(b) excluded** (unlike the
  self-adjoint route): it can reach `r*`.
* **Part 4 (`amplitude_injective`, sorry-free).**  That `E` is **unique**; combined
  with Part 3, `E ↦ factor` is a **bijection**.  The A=3 lift therefore has exactly
  **ONE** real degree of freedom — the anti-self-adjoint amplitude `E`.

**Net verdict — scope-(a), honest negative on closure (the door is real, not shut).**
The A=3 lift is carried by a **single free real amplitude** `E`.  Absent an
independent geometric derivation of `E` (the DM q-cubic prolongation symbol,
`conj:qdifference-kernel-prolongation-symbol`, `qou-jqof`), fixing `E` to hit `r*` is
a **FIT** (`E* = (factor_sa − r*)·A·D·B⁻¹`, anchor-inverted).  This does not close
`r*`; it **isolates the wall to one scalar** and proves that scalar is (i)
necessarily nonzero for any lift, (ii) free, (iii) unique.  Deriving `E` from the
Yekutieli non-abelian Stokes datum IS the open keystone; it is recorded as the §3b
dependent conjecture class `DerivedAmplitudeGivesLift` with **NO instance**.

**Why not scope-(b).**  A scope-(b) exclusion would need a proved invariant forbidding
`E ≠ 0` or bounding the amplitude — there is none: the branching under-determines the
anti-self-adjoint sector (`crossTerm_magnitude_surjective` in `SuperBerezinianA3Magnitude`
already showed the off-block is free; this file localises that freedom to the SINGLE
anti-self-adjoint scalar `E` and proves the affine bijection).  A *bounded* amplitude
(a proved `|E| ≤ …` from the writhe cap / a Stokes-constant bound) would upgrade this
to scope-(b) — that bound is exactly what a derivation of the prolongation symbol
would supply, and it is open.

**Honesty (STRICT — AGENTS.md §Axiomatization-is-NOT-a-Proof / §3b / §Strict Lean
Discipline).**  The four structural theorems are genuine algebra (an affine-split
identity, a strict-inequality contradiction, a surjectivity witness, an injectivity
cancellation), sorry-free, no `native_decide`, no trivial-true, no axiom.  The single
conjecture class carries genuine content (an equation + a nonzero-amplitude condition
+ a strict inequality on GEOMETRIC inputs), has **no instance**, and is never
self-assuming: `E_geom` is *checked against* a derived amplitude, never solved from
`κ_phys` (solving it would be `amplitude_surjective`, the forbidden fit).

**Base ring (§7c).**  Parts 1, 3, 4 and the class: generic `{R : Type*} [Field R]`
(scalar inverses `D⁻¹`, `A⁻¹` genuinely required — the §7c `[Field R]` inverse
carve-out).  Part 2 (and the class' `1 < κ`) adds `[LinearOrder R]
[IsStrictOrderedRing R]` — the ordering `> 1` is genuinely archimedean.  No `ℝ`, no
`Real.*`; the numerics `r* ≈ 1.585`, `factor_sa`, `μ₃`, `c₃` live only in the Python
witness / audit, downstream of the substrate→archimedean wall.

## References

- [leitner2026] `conj:qdifference-kernel-prolongation-symbol` (the DM q-cubic period /
  Yekutieli-Stokes datum that would derive the anti-self-adjoint amplitude `E`);
  `QOU.QBeta.A3OffBlockDerivation` (ROUTE 2-b — the self-adjoint reduction this file
  extends: `magnitudeFactor_le_one`, `observed_lift_unreachable`);
  `QOU.QBeta.SuperBerezinianA3Magnitude` (ROUTE 2 — off-block surjectivity);
  `QOU.QBeta.BerezinianSelfAdjointCrossTerm` (self-adjoint ⇒ bar-even cross-term);
  `docs/coordination/option-e.md` (the A=3 magnitude bracket rows); bean `qou-jqof`.
- [wenzl1988] Wenzl, "Hecke algebras of type Aₙ and subfactors", Invent. Math. 92
  (1988) 349-383 (the Markov trace weights on the Wedderburn blocks).
- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1 (the cubic
  condition that would pin the off-block amplitude geometrically).
-/

noncomputable section

namespace QOU.QBeta.A3AntiSelfAdjointLift

/-! ### The scalar model (matches `SuperBerezinianA3Magnitude` / `A3OffBlockDerivation`).

For the leading `(1-even, 1-odd)` super-block with even block `A`, odd block `D`, and
grade-reversing off-blocks `B, C`, the Berezinian even-face factor is the Schur
complement ratio `(A − B·D⁻¹·C)/A`.  The *graded-self-adjoint* value of the off-block
`C` is `−(σ B)` (with `σ` the bar involution); the deviation `E := C + σ B` is the
**anti-self-adjoint amplitude** — the one the self-adjoint branching leaves free. -/

/-- The Berezinian **cross-term** `t = B·D⁻¹·C` (grade-reversing off-blocks `B, C`
    bridged by the odd-block inverse `D⁻¹`). -/
def crossTerm {R : Type*} [Field R] (B C D : R) : R := B * D⁻¹ * C

/-- The multiplicative **even-face correction** `(A − t)/A` the cross-term `t` supplies
    to the bar-even (mass / C1) face. -/
def evenFaceCorrection {R : Type*} [Field R] (A t : R) : R := (A - t) / A

/-! ### Part 1 — the even-face factor is AFFINE in the anti-self-adjoint amplitude `E`. -/

/-- **The even-face factor splits as `factor_sa − (slope)·E` (sorry-free).**  Writing the
    off-block as `C = Csa + E` (`Csa = −(σ B)` the graded-self-adjoint value, `E` the
    anti-self-adjoint amplitude), the even-face correction is affine in `E`:

      `evenFaceCorrection A (crossTerm B (Csa + E) D)`
        `= evenFaceCorrection A (crossTerm B Csa D) − B·D⁻¹·E / A`.

    The first term is the self-adjoint background (`≤ 1`, `A3OffBlockDerivation`); the
    second is the lift the amplitude `E` supplies, linear in `E` with slope `B·D⁻¹/A`.
    The identity is a pure field manipulation — it holds for ALL `A, B, D` (the physical
    regime has `A, D` invertible even/odd blocks; the split needs no side condition). -/
theorem factor_affine_in_amplitude {R : Type*} [Field R] (A B D Csa E : R) :
    evenFaceCorrection A (crossTerm B (Csa + E) D)
      = evenFaceCorrection A (crossTerm B Csa D) - B * D⁻¹ * E / A := by
  unfold evenFaceCorrection crossTerm
  rw [mul_add, ← sub_sub, sub_div]

/-! ### Part 2 — a lift FORCES a nonzero anti-self-adjoint amplitude (the wall). -/

/-- **A genuine lift forces `B·D⁻¹·E ≠ 0` (sorry-free).**  If the self-adjoint
    background factor is `≤ 1` (proved for the branching by
    `A3OffBlockDerivation.magnitudeFactor_le_one`) and the full factor is a lift
    (`> 1`), then the amplitude term `B·D⁻¹·E` is nonzero.  Contrapositive: with `E = 0`
    the factor is the self-adjoint value `≤ 1` — no lift.  The lift lives ENTIRELY in
    the anti-self-adjoint amplitude the branching leaves free. -/
theorem lift_forces_nonzero_amplitude {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (A B D Csa E : R)
    (hsa : evenFaceCorrection A (crossTerm B Csa D) ≤ 1)
    (hlift : 1 < evenFaceCorrection A (crossTerm B (Csa + E) D)) :
    B * D⁻¹ * E ≠ 0 := by
  rw [factor_affine_in_amplitude A B D Csa E] at hlift
  intro h
  rw [h, zero_div, sub_zero] at hlift
  linarith

/-- **A lift requires `E ≠ 0` — the off-block is anti-self-adjoint (sorry-free).**  The
    lift forces the anti-self-adjoint amplitude `E` itself to be nonzero: the derived
    off-block `C = Csa + E ≠ Csa = −(σ B)`.  This is the precise wall `A3OffBlockDerivation`
    named — a lift needs `C ≠ −σ B`.  (The implication `B·D⁻¹·E ≠ 0 ⇒ E ≠ 0` needs no
    side condition: a zero factor kills the product.) -/
theorem amplitude_nonzero {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (A B D Csa E : R)
    (hsa : evenFaceCorrection A (crossTerm B Csa D) ≤ 1)
    (hlift : 1 < evenFaceCorrection A (crossTerm B (Csa + E) D)) :
    E ≠ 0 := by
  intro hE
  exact lift_forces_nonzero_amplitude A B D Csa E hsa hlift
    (by rw [hE, mul_zero])

/-! ### Part 3 — the amplitude is FREE (surjective): NOT scope-(b) excluded. -/

/-- **The anti-self-adjoint amplitude `E` is a FREE parameter (sorry-free).**  For fixed
    nonzero background `A, B, D`, the map `E ↦ evenFaceCorrection A (crossTerm B (Csa + E)
    D)` is **surjective** onto `R`: for ANY target `r` there is an amplitude `E`
    realizing it — witness `E = (factor_sa − r)·A·D·B⁻¹`.  So the anti-self-adjoint
    route CAN reach the observed lift `r* ≈ 1.585` (contrast the self-adjoint route,
    scope-(b) excluded), but only by pinning `E` to the target — a FIT, unless `E` is
    derived from an independent geometric datum. -/
theorem amplitude_surjective {R : Type*} [Field R] (A B D Csa r : R)
    (hA : A ≠ 0) (hB : B ≠ 0) (hD : D ≠ 0) :
    ∃ E : R, evenFaceCorrection A (crossTerm B (Csa + E) D) = r := by
  refine ⟨(evenFaceCorrection A (crossTerm B Csa D) - r) * A * D * B⁻¹, ?_⟩
  rw [factor_affine_in_amplitude A B D Csa _]
  unfold evenFaceCorrection crossTerm
  field_simp
  ring

/-! ### Part 4 — the amplitude is UNIQUE: the lift has exactly one real DOF. -/

/-- **The amplitude realizing a given factor is UNIQUE (sorry-free).**  For fixed
    nonzero background `A, B, D`, `E ↦ factor` is injective.  Together with Part 3 it is
    a **bijection**: the A=3 lift is carried by EXACTLY ONE real degree of freedom — the
    anti-self-adjoint amplitude `E`.  There is no residual multiplicity to hide a
    derivation in; deriving that single scalar from the geometry is the whole of the
    open keystone. -/
theorem amplitude_injective {R : Type*} [Field R] (A B D Csa E₁ E₂ : R)
    (hA : A ≠ 0) (hB : B ≠ 0) (hD : D ≠ 0)
    (h : evenFaceCorrection A (crossTerm B (Csa + E₁) D)
        = evenFaceCorrection A (crossTerm B (Csa + E₂) D)) : E₁ = E₂ := by
  rw [factor_affine_in_amplitude A B D Csa E₁,
      factor_affine_in_amplitude A B D Csa E₂] at h
  have h2 : B * D⁻¹ * E₁ / A = B * D⁻¹ * E₂ / A := sub_right_injective h
  rw [div_eq_div_iff hA hA] at h2
  have h3 : B * D⁻¹ * E₁ = B * D⁻¹ * E₂ := mul_right_cancel₀ hA h2
  exact mul_left_cancel₀ (mul_ne_zero hB (inv_ne_zero hD)) h3

/-! ### Part 5 — the OPEN closure, as an honest §3b dependent conjecture (no instance).

The lift is carried by the single free amplitude `E` (Parts 2–4).  It closes as a
*prediction* only if `E` is pinned by an independent geometric datum — the DM q-cubic
prolongation symbol (`conj:qdifference-kernel-prolongation-symbol`, `qou-jqof`) — rather
than fitted to the target.  We record that open state as a content-bearing §3b
dependent conjecture class with **NO instance**. -/

/-- **§3b dependent conjecture — the A=3 lift closes via a DERIVED anti-self-adjoint
    amplitude.**

    `@conjecture: dependent` (its content depends on the open geometric derivation of the
    anti-self-adjoint amplitude — `conj:qdifference-kernel-prolongation-symbol` / the
    `qou-jqof` wall — supplying `E_geom` as the Yekutieli-Stokes prolongation symbol of
    the SW connection).

    The claim: a geometrically-derived amplitude `E_geom` (an INPUT from the DM q-cubic,
    independent of the physical target) simultaneously (i) **breaks** graded
    self-adjointness (`E_geom ≠ 0`, i.e. the derived off-block `C_geom = −(σ B_geom) +
    E_geom` differs from its self-adjoint value `−(σ B_geom)` — the anti-self-adjoint
    amplitude the branching leaves free) and (ii) drives the even-face correction to a
    physical **lift** `κ_phys > 1` (unreachable by the self-adjoint branching Schur
    complement, `A3OffBlockDerivation.magnitudeFactor_le_one`).

    The bar involution `σ` is quantified as a genuine ring homomorphism applied to the
    derived off-block magnitude `B_geom`; the self-adjoint reference value is `−(σ
    B_geom)`.

    **Why this is content-bearing and NOT a fit.**  In a *fit* `E` is solved from
    `κ_phys` (`amplitude_surjective`, witness `E* = (factor_sa − κ)·A·D·B⁻¹`).  Here
    `E_geom` is a *given* geometric input and the conjunction is a nontrivial *check*
    that the geometry both breaks self-adjointness AND lands the physics — false for a
    generic `E_geom`, and (by `amplitude_nonzero`) the `E_geom ≠ 0` clause is *forced* by
    the strict lift, tying the two fields together.  **No instance is supplied**:
    deriving `E_geom` from the prolongation symbol IS the open keystone; discharging this
    by *choosing* `E_geom` to hit `κ_phys` would be the forbidden fit and is explicitly
    not done. -/
class DerivedAmplitudeGivesLift {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (σ : R →+* R) (A B_geom D E_geom κ_phys : R) : Prop where
  /-- The geometrically-derived amplitude BREAKS graded self-adjointness: `E_geom ≠ 0`,
      i.e. `C_geom = −(σ B_geom) + E_geom ≠ −(σ B_geom)`. -/
  anti_self_adjoint : E_geom ≠ 0
  /-- The derived (not fitted) amplitude drives the even-face correction to the physical
      **lift** `κ_phys`, which strictly EXCEEDS `1` — an enhancement provably outside the
      self-adjoint branching route (`A3OffBlockDerivation.magnitudeFactor_le_one`). -/
  geom_gives_lift :
    evenFaceCorrection A (crossTerm B_geom (-(σ B_geom) + E_geom) D) = κ_phys ∧ 1 < κ_phys

end QOU.QBeta.A3AntiSelfAdjointLift
