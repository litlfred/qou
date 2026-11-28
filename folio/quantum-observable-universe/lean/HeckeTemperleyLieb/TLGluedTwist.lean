import HeckeTemperleyLieb.TLGlued
import HeckeTemperleyLieb.TLQuotientBraiding

/-!
# The twist as a natural automorphism of the glued Temperley–Lieb category

Bean `hkmt`. `TLGlued` builds the category `GObj` containing every strand count, with
`Hom([a],[b])` the direct limit of the corners `[b] Q_N [a]` under the cup map.
`TLQuotientBraiding` builds the framed twist `θ_N` on each quotient `Q N`, central there and
compatible with the cup map (`twistQ_capQ`).

* `twistG X : X ⟶ X`: the class of the sequence `N ↦ [a] · θ_N`.
* `twistG_naturality`: `f ≫ θ_Y = θ_X ≫ f` for **every** morphism `f`, including those between
  different strand counts.
* `twistIsoG`: `θ` is a natural automorphism of the identity functor of `GObj`, with inverse
  built from `twistInvQ`.

This is the twist datum of `QOU.MathlibExt.BalancedCategory` on `GObj`; the balancing axiom
needs the monoidal structure and is `twistQ_balance` once that exists.

No empirical input; everything is over an arbitrary field with `A ≠ 0`, `δ = A² + A⁻²`.

-- Ref: [kassel1995] Kassel, *Quantum groups*, XIV.3.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLGluedTwist

open CategoryTheory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLSemisimpleQuotient QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLRectHom QOU.HeckeTemperleyLieb.TLGlued
open QOU.HeckeTemperleyLieb.TLQuotientBraiding

variable {K : Type*} [Field K] {δ ε A : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)
  (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

local notation "⟪" f "⟫" => Submodule.Quotient.mk f

/-- Multiplying a corner element by a central element compatible with the cup map. -/
theorem central_seq {a : ℕ} (z : ∀ N, Q T N) (hz : ∀ N (φ : Q T N), z N * φ = φ * z N)
    (hcap : ∀ N (φ : Q T N), z (N + 1 + 1) * capQ T hε N φ = capQ T hε N (z N * φ)) :
    Compat T hε a a (fun N => PQ T a N * z N) a := by
  intro N hN
  refine ⟨?_, ?_⟩
  · show PQ T a N * (PQ T a N * z N) * PQ T a N = PQ T a N * z N
    rw [← mul_assoc, PQ_idem T hε, mul_assoc, hz, ← mul_assoc, PQ_idem T hε]
  · show capQ T hε N (PQ T a N * z N) = PQ T a (N + 1 + 1) * z (N + 1 + 1)
    rw [← hz, ← hcap, capQ_PQ T hε (by omega), hz]

/-- **Central, cup-compatible families**: the data of a natural endomorphism of the identity. -/
structure CentralFam (T : MarkovTower δ ε) (hε : δ * ε = 1) where
  /-- The element on each level. -/
  z : ∀ N, Q T N
  central : ∀ N (φ : Q T N), z N * φ = φ * z N
  cap : ∀ N (φ : Q T N), z (N + 1 + 1) * capQ T hε N φ = capQ T hε N (z N * φ)

variable {T hε}

/-- The sequence `N ↦ [a] · z_N`. -/
noncomputable def CentralFam.seq (F : CentralFam T hε) (a : ℕ) : Seq T hε a a :=
  ⟨fun N => PQ T a N * F.z N, a, central_seq T hε F.z F.central F.cap⟩

/-- The endomorphism of `X` given by a central family. -/
noncomputable def CentralFam.app (F : CentralFam T hε) (X : GObj T hε) : X ⟶ X :=
  (⟪F.seq X.a⟫ : GHom T hε X.a X.a)

include hε in
/-- Twist-type sequences are natural: `[b] z · φ = φ · [a] z` on every corner element. -/
theorem central_mul {N a b : ℕ} {z φ : Q T N} (hz : ∀ ψ : Q T N, z * ψ = ψ * z)
    (hφ : φ ∈ HomSp T N a b) : PQ T b N * z * φ = φ * (PQ T a N * z) := by
  rw [mul_assoc, hz, ← mul_assoc, left_mul_of_mem T hε hφ, ← mul_assoc,
    right_mul_of_mem T hε hφ]

/-- **Naturality**: `f ≫ z_Y = z_X ≫ f` for every morphism `f` of the glued category. -/
theorem CentralFam.naturality (F : CentralFam T hε) {X Y : GObj T hε} (f : X ⟶ Y) :
    f ≫ F.app Y = F.app X ≫ f := by
  obtain ⟨g, rfl⟩ := Submodule.Quotient.mk_surjective _ (show GHom T hε X.a Y.a from f)
  obtain ⟨N0, hg⟩ := compat_of_mem g
  show compH _ _ = compH _ _
  rw [CentralFam.app, CentralFam.app, compH_mk, compH_mk, mk_eq_iff]
  exact ⟨N0, fun N hN => central_mul (hε := hε) (F.central N) (hg N hN).1⟩

/-- Composing two central families. -/
noncomputable def CentralFam.mul (F G : CentralFam T hε) : CentralFam T hε where
  z N := F.z N * G.z N
  central N φ := by rw [mul_assoc, G.central, ← mul_assoc, F.central, mul_assoc]
  cap N φ := by rw [mul_assoc, G.cap, F.cap, mul_assoc]

theorem CentralFam.app_comp (F G : CentralFam T hε) (X : GObj T hε) :
    G.app X ≫ F.app X = (F.mul G).app X := by
  show compH _ _ = _
  rw [CentralFam.app, CentralFam.app, CentralFam.app, compH_mk, mk_eq_iff]
  refine ⟨0, fun N _ => ?_⟩
  show PQ T X.a N * F.z N * (PQ T X.a N * G.z N) = PQ T X.a N * (F.z N * G.z N)
  rw [mul_assoc, ← mul_assoc (F.z N), F.central, mul_assoc, ← mul_assoc, PQ_idem T hε]

theorem CentralFam.app_one (F : CentralFam T hε) (h : ∀ N, F.z N = 1) (X : GObj T hε) :
    F.app X = 𝟙 X := by
  rw [TLGlued.id_def, CentralFam.app, mk_eq_iff]
  exact ⟨0, fun N _ => by show PQ T X.a N * F.z N = PQ T X.a N; rw [h, mul_one]⟩

variable (T hε)

include hA hδ in
/-- **The twist** as a central family. -/
noncomputable def twistFam : CentralFam T hε where
  z := twistQ A T
  central := twistQ_comm hA hδ T
  cap := twistQ_capQ hA hδ T hε

include hA hδ in
/-- **The inverse twist** as a central family. -/
noncomputable def twistInvFam : CentralFam T hε where
  z := twistInvQ A T
  central N φ := by
    set u := twistQ A T N
    set v := twistInvQ A T N
    have huv : u * v = 1 := twistQ_mul_inv hA hδ T N
    have hvu : v * u = 1 := inv_mul_twistQ hA hδ T N
    calc v * φ = v * φ * (u * v) := by rw [huv, mul_one]
      _ = v * (φ * u) * v := by simp only [mul_assoc]
      _ = v * (u * φ) * v := by rw [twistQ_comm hA hδ T N φ]
      _ = φ * v := by rw [← mul_assoc, hvu, one_mul]
  cap N φ := by
    have hvu : twistInvQ A T (N + 1 + 1) * twistQ A T (N + 1 + 1) = 1 :=
      inv_mul_twistQ hA hδ T _
    calc twistInvQ A T (N + 1 + 1) * capQ T hε N φ
        = twistInvQ A T (N + 1 + 1) *
            capQ T hε N (twistQ A T N * (twistInvQ A T N * φ)) := by
          rw [← mul_assoc, twistQ_mul_inv hA hδ, one_mul]
      _ = capQ T hε N (twistInvQ A T N * φ) := by
          rw [← twistQ_capQ hA hδ T hε, ← mul_assoc, hvu, one_mul]

include hA hδ in
/-- **The twist is a natural automorphism of the identity functor** of the glued category. -/
noncomputable def twistIsoG : 𝟭 (GObj T hε) ≅ 𝟭 (GObj T hε) :=
  NatIso.ofComponents
    (fun X => ⟨(twistFam T hε hA hδ).app X, (twistInvFam T hε hA hδ).app X,
      (CentralFam.app_comp _ _ X).trans
        (CentralFam.app_one _ (fun N => inv_mul_twistQ hA hδ T N) X),
      (CentralFam.app_comp _ _ X).trans
        (CentralFam.app_one _ (fun N => twistQ_mul_inv hA hδ T N) X)⟩)
    (fun f => (twistFam T hε hA hδ).naturality f)

include hA hδ in
/-- **Naturality of the twist** on every morphism, between any strand counts. -/
theorem twistG_naturality {X Y : GObj T hε} (f : X ⟶ Y) :
    f ≫ (twistIsoG T hε hA hδ).hom.app Y = (twistIsoG T hε hA hδ).hom.app X ≫ f :=
  (twistFam T hε hA hδ).naturality f

end QOU.HeckeTemperleyLieb.TLGluedTwist
