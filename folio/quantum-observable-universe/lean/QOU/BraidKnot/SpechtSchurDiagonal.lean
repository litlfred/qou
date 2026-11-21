import QOU.BraidKnot.SpechtAbsolutelyIrreducible
import QOU.MathlibExt.RepresentationCharacter

/-!
# QOU.BraidKnot.SpechtSchurDiagonal — `dim_k Hom_G(S^μ, S^μ) = 1`

First brick of **W1+W3** of the Wedderburn epic (`qou-bxw4`), which the epic's own
scouting merged into a single construction. It converts W2
(`SpechtAbsolutelyIrreducible.specht_end_scalar`) into the form the corpus' character
machinery consumes.

`QOU.MathlibExt.RepresentationCharacter` already carries the general identity

  `⅟|G| • Σ_g χ_V(g⁻¹)·χ_W(g) = dim_k Hom_G(V, W)`   (`charPairing_eq_finrank_homG`)

together with `one_le_finrank_homG_self` (the identity is equivariant, so the diagonal is
at least 1) and the vanishing off the diagonal. What it did **not** have is the diagonal
*exactly* 1 — the normalisation Mathlib reaches only via `FDRep.char_orthonormal`, which
carries `[IsAlgClosed k]`. For Specht modules that hypothesis is unnecessary: W2 says the
commutant is the base field over any characteristic-zero field, which pins the diagonal at
1 outright.

So the Specht characters are **orthonormal over `ℚ`**, not merely orthogonal — which is what
turns the classification's counting *bound* into an expansion of `χ_reg`, and that is the
route to `n! = Σ_μ (dim S^μ)²` recorded on bean `qou-3c2j`.

## Scope

This file is the bridge lemma only. It does not compute `χ_reg`, does not decompose the
regular representation, and claims nothing about `sn_isotypic_specht_split`, which remains
open.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]` — no `ℝ`, no ordering.
-/

namespace QOU.BraidKnot.SpechtSchurDiagonal

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.MathlibExt.RepresentationCharacter
open Equiv (Perm)
open Module

variable {k : Type} [Field k] [CharZero k]

/-- `S^μ` is nonzero: it contains a polytabloid, and polytabloids do not vanish in
characteristic zero (`SpechtCrossKappa.polytabloid_ne_zero`). -/
instance nontrivial_spechtSubmodule (μ : YoungDiagram) :
    Nontrivial (SpechtSubmodule (k := k) μ) := by
  classical
  obtain ⟨t⟩ := nonempty_tableau μ
  refine ⟨⟨⟨polytabloid (k := k) t, polytabloid_mem_specht t⟩, 0, ?_⟩⟩
  intro h
  exact SpechtCrossKappa.polytabloid_ne_zero (K := k) μ t (congrArg Subtype.val h)

/-- The identity is a nonzero endomorphism of `S^μ`. -/
theorem id_ne_zero (μ : YoungDiagram) :
    (LinearMap.id : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ) ≠ 0 := by
  intro h
  obtain ⟨x, hx⟩ := exists_ne (0 : SpechtSubmodule (k := k) μ)
  exact hx (by simpa using congrArg (fun m : SpechtSubmodule (k := k) μ →ₗ[k] _ => m x) h)

/-- **`Hom_G(S^μ, S^μ)` is the line through the identity.** The inclusion `⊇` is that the
identity is equivariant; `⊆` is W2. -/
theorem homG_specht_self_eq_span (μ : YoungDiagram) :
    homG (spechtRep (k := k) μ) (spechtRep (k := k) μ)
      = Submodule.span k
          {(LinearMap.id : SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ)} := by
  refine le_antisymm (fun f hf => ?_) ?_
  · obtain ⟨c, hc⟩ :=
      SpechtAbsolutelyIrreducible.specht_end_scalar (k := k) f (mem_homG_iff.mp hf)
    refine Submodule.mem_span_singleton.mpr ⟨c, ?_⟩
    exact (LinearMap.ext fun x => (hc x).symm)
  · rw [Submodule.span_le, Set.singleton_subset_iff]
    exact mem_homG_iff.mpr (fun _ _ => rfl)

/-- **The Schur diagonal is exactly 1, over any characteristic-zero field.**
`dim_k Hom_G(S^μ, S^μ) = 1`.

`one_le_finrank_homG_self` gives `≥ 1` for any nonzero representation; the content here is
`≤ 1`, which is W2 — the commutant is the base field, so there is nothing beyond the scalars.
Mathlib obtains this normalisation only over an algebraically closed base
(`FDRep.char_orthonormal`); no algebraic closure is used here.

`-- Ref: [james1984representation] §4; [sagan2001] §2.4` -/
theorem finrank_homG_specht_self (μ : YoungDiagram) :
    finrank k (homG (spechtRep (k := k) μ) (spechtRep (k := k) μ)) = 1 := by
  rw [homG_specht_self_eq_span (k := k) μ]
  -- The explicit `(K := _) (V := _)` matters: without them elaboration searches over the
  -- unfolded `Submodule k (Mtab μ)` carrier of `S^μ` and times out at `isDefEq`, even at
  -- 10^6 heartbeats. With them it closes in seconds and no option bump is needed.
  exact finrank_span_singleton
    (K := k)
    (V := SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) μ)
    (id_ne_zero (k := k) μ)

/-! ## The off-diagonal, exported

The vanishing `Hom_G(S^μ, S^ν) = 0` for `μ ≠ ν` is used inside
`SpechtClassification.specht_exhausts_irreducibles`'s counting proof but was never stated
as a lemma of its own. Exported here, because orthonormality needs *both* entries and the
diagonal alone is only half of it. -/

/-- **Schur, off the diagonal.** For distinct diagrams of the same size there is no nonzero
equivariant map `S^μ → S^ν`.

Both simplicity hypotheses come from `SpechtClassification.spechtRep_stable_eq_bot_or_top`;
on the `ν` side, stability under every `spechtRepOn h g` is the same condition as stability
under every `spechtRep ν σ`, because `transportPermHom h` is surjective. The
non-isomorphism is `specht_pairwise_noniso`. -/
theorem homG_specht_cross_eq_bot {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (hne : μ ≠ ν) :
    homG (spechtRep (k := k) μ) (spechtRepOn (k := k) h) = ⊥ := by
  refine homG_eq_bot (spechtRep_stable_eq_bot_or_top (k := k) μ) (fun p hp => ?_) ?_
  · refine spechtRep_stable_eq_bot_or_top (k := k) ν p (fun σ v hv => ?_)
    obtain ⟨g, rfl⟩ := transportPermHom_surjective h σ
    exact hp g v hv
  · intro e he
    exact specht_pairwise_noniso (k := k) h hne ⟨e, fun g x => he g x⟩

/-- **The Schur pairing is orthonormal on Specht modules, over any characteristic-zero
field.** `dim_k Hom_G(S^μ, S^ν) = 1` if `μ = ν` and `0` otherwise.

Mathlib's orthonormality (`FDRep.char_orthonormal`) carries `[IsAlgClosed k]`; neither half
of this needs it. The `1` is W2 (`SpechtAbsolutelyIrreducible.specht_end_scalar`); the `0` is
the classification's own Schur argument, exported above. -/
theorem finrank_homG_specht (μ ν : YoungDiagram) (h : Specht.nOf μ = Specht.nOf ν) :
    finrank k (homG (spechtRep (k := k) μ) (spechtRepOn (k := k) h))
      = if μ = ν then 1 else 0 := by
  by_cases hne : μ = ν
  · subst hne
    -- at `μ = ν` the transport `h : nOf μ = nOf μ` acts trivially on the group, so
    -- `spechtRepOn h` is `spechtRep μ` itself.
    have hrep : spechtRepOn (k := k) h = spechtRep (k := k) μ := by
      refine DFunLike.ext _ _ (fun g => ?_)
      show spechtRep (k := k) μ (transportPermHom h g) = spechtRep (k := k) μ g
      congr 1
    rw [hrep, if_pos rfl]
    exact finrank_homG_specht_self (k := k) μ
  · rw [homG_specht_cross_eq_bot (k := k) h hne, if_neg hne]
    -- as in `finrank_homG_specht_self`, name the module or elaboration unfolds the
    -- `Submodule k (Mtab _)` carriers and times out.
    exact finrank_bot k
      (SpechtSubmodule (k := k) μ →ₗ[k] SpechtSubmodule (k := k) ν)

/-- Cross-shape Schur pairing dimension vanishes for distinct partitions `μ ≠ ν` of the same size. -/
theorem finrank_homG_specht_of_ne {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (hne : μ ≠ ν) :
    finrank k (homG (spechtRep (k := k) μ) (spechtRepOn (k := k) h)) = 0 := by
  rw [finrank_homG_specht (k := k) μ ν h, if_neg hne]

end QOU.BraidKnot.SpechtSchurDiagonal
