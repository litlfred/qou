import QOU.SchurWeyl.HeckeSemisimpleGeneral
import QOU.Hecke.IwahoriHecke

/-!
# QOU.SchurWeyl.HeckeCarrierEquiv — the two `RingQuot` presentations are one algebra

Bean `qou-img9` (the presentation pile) and the carrier item of `qou-kwoa`.

`QOU/SchurWeyl/HeckeSemisimpleGeneral.lean` proves `IsSemisimpleRing` at every rank —
but for `QOU.SchurWeyl.Hecke`, whereas the `T_w` basis and `twGram` are built on
`QOU.Hecke.IwahoriHecke`.  That gap was recorded, not closed.  This file closes it.

## The two relations differ in exactly one clause

    SchurWeyl.HeckeRel K q qi n :  σ² = (q − qi)·σ + (q·qi)·1
    QOU.Hecke.HeckeRel  K Q  n  :  σ² = (Q − 1)·σ + Q·1

The braid and far-commutation clauses are **verbatim identical**, on the same
`FreeAlgebra K (Fin n)`.  So the whole content is the quadratic, and it moves under a
generator rescaling.  Write `σ` for the skein generator (source) and `T` for the
Iwahori generator at `Q` (target), and send `σ i ↦ c • T i`.  Squaring the target and
using the Iwahori relation on `T` gives

    (c • T)² = c²(Q − 1) • T + (c² Q) • 1,

while the skein relation demands

    (c • T)² = (q − qi) • (c • T) + (q · qi) • 1 = c(q − qi) • T + (q · qi) • 1.

Matching the two coefficients gives `c²(Q − 1) = c(q − qi)` and `c² Q = q · qi`.  We
take the first in the **division-free, slightly stronger** form `c(Q − 1) = q − qi`,
which implies it by multiplying through by `c`.  Nothing here asks `c` to be a unit:
`toIwahori` is built over a bare `[CommRing K]` from those two identities alone.  An
inverse enters only for the map *back* — `fromIwahori` takes a separate `d` with
`d · c = 1` — and only there because the two directions must compose to the identity.

Those two identities are the hypotheses `hc₁` and `hc₂` below.  The braid and
commutation clauses are homogeneous of the same degree in the generators, so the
rescaling cannot disturb them — proved here rather than asserted.

## The specialisation that matters

At the skein normalisation `qi = q⁻¹` (so `q·qi = 1`), taking

    Q = q²   and   c = q⁻¹

satisfies both identically: `c²Q = q⁻²q² = 1 = q·qi`, and
`c(Q−1) = q⁻¹(q²−1) = q − q⁻¹ = q − qi`.  **The parameter moves, not the ring** —
no square root is adjoined, and nothing leaves a generic `[Field K]`.  This is the
same rescaling `QOU/BraidKnot/HeckeIwahoriConventionBridge.lean` derives for
*generator families*; what is new here is that it is upgraded to an `AlgEquiv` of
the two `RingQuot` carriers, which is what transports a ring-theoretic property.

## What this is not

It is not the `IwahoriHeckeOfSn` bridge — `QOU/BraidKnot/HeckeTypeAPresentationEquiv.lean`
already crosses that pair, and this is a different pair.  Between them, three of the
presentations `qou-img9` counts are now provably one algebra.
-/

namespace QOU.SchurWeyl

open QOU.Hecke (IwahoriHecke)

variable {K : Type*} [CommRing K] {A : Type*} [Ring A] [Algebra K A]

/-! ## A universal property for the `QOU.Hecke.IwahoriHecke` side

`QOU.SchurWeyl.Hecke` already has `lift` / `lift_σ` / `hom_ext`.  The other carrier
has its generators and relations but no lift, so we supply the two halves needed. -/

variable (K) in
/-- `FreeAlgebra.lift` respects the Iwahori relations when the images do. -/
theorem iwahoriLift_respects (Q : K) (n : ℕ) (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (Q - 1) • g i + Q • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i) :
    ∀ ⦃x y : FreeAlgebra K (Fin n)⦄, QOU.Hecke.HeckeRel K Q n x y →
      FreeAlgebra.lift K g x = FreeAlgebra.lift K g y := by
  intro x y h
  induction h with
  | quadratic i =>
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
      exact hquad i
  | braid i hi =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hbraid i hi
  | commute i j hij =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hcomm i j hij

variable (K) in
/-- **Universal property of `IwahoriHecke` (existence).** -/
noncomputable def iwahoriLift (Q : K) (n : ℕ) (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (Q - 1) • g i + Q • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i) :
    IwahoriHecke K Q n →ₐ[K] A :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K g,
    iwahoriLift_respects K Q n g hquad hbraid hcomm⟩

variable (K) in
@[simp]
theorem iwahoriLift_σ (Q : K) (n : ℕ) (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (Q - 1) • g i + Q • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i)
    (i : Fin n) :
    iwahoriLift K Q n g hquad hbraid hcomm (QOU.Hecke.IwahoriHecke.σ K Q n i) = g i :=
  (RingQuot.liftAlgHom_mkAlgHom_apply K (FreeAlgebra.lift K g)
      (iwahoriLift_respects K Q n g hquad hbraid hcomm) (FreeAlgebra.ι K i)).trans
    (FreeAlgebra.lift_ι_apply g i)

variable (K) in
/-- **Universal property of `IwahoriHecke` (uniqueness).** -/
theorem iwahori_hom_ext (Q : K) (n : ℕ) {φ ψ : IwahoriHecke K Q n →ₐ[K] A}
    (h : ∀ i, φ (QOU.Hecke.IwahoriHecke.σ K Q n i)
             = ψ (QOU.Hecke.IwahoriHecke.σ K Q n i)) : φ = ψ := by
  have key : φ.comp (QOU.Hecke.IwahoriHecke.mk K Q n)
      = ψ.comp (QOU.Hecke.IwahoriHecke.mk K Q n) := by
    apply FreeAlgebra.hom_ext
    funext i
    simpa only [AlgHom.comp_apply, QOU.Hecke.IwahoriHecke.mk,
      QOU.Hecke.IwahoriHecke.σ] using h i
  ext z
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective K (QOU.Hecke.HeckeRel K Q n) z
  exact AlgHom.congr_fun key x

/-! ## The rescaling maps

`σ ↦ c • T` in one direction, `T ↦ d • σ` back, with `d * c = 1`. -/

variable (K) in
/-- **Skein presentation → Iwahori presentation**, `σ_i ↦ c • T_i`. -/
noncomputable def toIwahori (q qi Q c : K) (n : ℕ)
    (hc₁ : c * (Q - 1) = q - qi) (hc₂ : c * c * Q = q * qi) :
    Hecke K q qi n →ₐ[K] IwahoriHecke K Q n :=
  Hecke.lift K q qi n (fun i => c • QOU.Hecke.IwahoriHecke.σ K Q n i)
    (by
      intro i
      rw [smul_mul_assoc, mul_smul_comm, QOU.Hecke.IwahoriHecke.σ_quadratic]
      simp only [smul_add, smul_smul]
      congr 1
      · congr 1; linear_combination c * hc₁
      · congr 1; linear_combination hc₂)
    (by
      intro i hi
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
      congr 1
      exact QOU.Hecke.IwahoriHecke.σ_braid K Q n i hi)
    (by
      intro i j hij
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
      congr 1
      exact QOU.Hecke.IwahoriHecke.σ_commute K Q n i j hij)

variable (K) in
/-- **Iwahori presentation → skein presentation**, `T_i ↦ d • σ_i`. -/
noncomputable def fromIwahori (q qi Q c d : K) (n : ℕ)
    (hc₁ : c * (Q - 1) = q - qi) (hc₂ : c * c * Q = q * qi) (hdc : d * c = 1) :
    IwahoriHecke K Q n →ₐ[K] Hecke K q qi n :=
  iwahoriLift K Q n (fun i => d • Hecke.σ K q qi n i)
    (by
      intro i
      rw [smul_mul_assoc, mul_smul_comm, Hecke.σ_quadratic]
      simp only [smul_add, smul_smul]
      congr 1
      · congr 1
        linear_combination (-(d * d)) * hc₁ + (d * (Q - 1)) * hdc
      · congr 1
        linear_combination (-(d * d)) * hc₂ + (Q * (d * c + 1)) * hdc)
    (by
      intro i hi
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
      congr 1
      exact Hecke.σ_braid K q qi n i hi)
    (by
      intro i j hij
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
      congr 1
      exact Hecke.σ_commute K q qi n i j hij)

/-! ## The equivalence -/

variable (K) in
/-- **The two presentations are the same algebra.**  `σ_i ↦ c • T_i`, with inverse
    `T_i ↦ d • σ_i`; the round trips are `d * c = 1` on generators. -/
noncomputable def carrierEquiv (q qi Q c d : K) (n : ℕ)
    (hc₁ : c * (Q - 1) = q - qi) (hc₂ : c * c * Q = q * qi) (hdc : d * c = 1) :
    Hecke K q qi n ≃ₐ[K] IwahoriHecke K Q n :=
  AlgEquiv.ofAlgHom (toIwahori K q qi Q c n hc₁ hc₂)
    (fromIwahori K q qi Q c d n hc₁ hc₂ hdc)
    (iwahori_hom_ext K Q n (by
      intro i
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, fromIwahori, toIwahori,
        iwahoriLift_σ, map_smul, Hecke.lift_σ, smul_smul, hdc, one_smul]))
    (Hecke.hom_ext K q qi n (by
      intro i
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, fromIwahori, toIwahori,
        Hecke.lift_σ, map_smul, iwahoriLift_σ, smul_smul]
      rw [show c * d = 1 by linear_combination hdc, one_smul]))

/-! ## The specialisation: skein at `q` is Iwahori at `q²` -/

/-- **`H^skein_n(q) ≃ₐ H^Iwahori_n(q²)`** over a field, for `q ≠ 0`.

    The parameter moves, not the ring: `Q = q²` and `c = q⁻¹`, both already in `K`. -/
noncomputable def skeinIwahoriEquiv {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ) :
    Hecke K q q⁻¹ n ≃ₐ[K] IwahoriHecke K (q ^ 2) n :=
  carrierEquiv K q q⁻¹ (q ^ 2) q⁻¹ q n
    (by field_simp) (by field_simp) (by field_simp)

/-- **`QOU.Hecke.IwahoriHecke` — the `T_w` / `twGram` carrier — is semisimple at every
    rank (sorry-free).**

    This is the carrier item `QOU/SchurWeyl/HeckeSemisimpleGeneral.lean` recorded as
    *not* reached: that file proves semisimplicity for `QOU.SchurWeyl.Hecke`, and the
    `T_w` basis is built on `QOU.Hecke.IwahoriHecke`.  `skeinIwahoriEquiv` transports it.

    Stated in the Iwahori parameter `Q` directly, which is what consumers of
    `twGram` use. -/
theorem isSemisimpleRing_iwahoriHecke {Q : ℝ} (hQ : 1 < Q) (n : ℕ) :
    IsSemisimpleRing (IwahoriHecke ℝ Q n) := by
  have hQ0 : (0 : ℝ) ≤ Q := by linarith
  have hsq : Real.sqrt Q ^ 2 = Q := Real.sq_sqrt hQ0
  have hq1 : 1 < Real.sqrt Q := by
    have : Real.sqrt 1 < Real.sqrt Q := by
      apply Real.sqrt_lt_sqrt (by norm_num) hQ
    simpa using this
  have hqne : Real.sqrt Q ≠ 0 := by positivity
  have hss := isSemisimpleRing_hecke_of_one_lt hq1 n
  have := (skeinIwahoriEquiv (Real.sqrt Q) hqne n).toRingEquiv.isSemisimpleRing
  rwa [hsq] at this

end QOU.SchurWeyl
