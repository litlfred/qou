import QOU.Basic


/-!
# QOU.BraidKnot.ConfinementLocalConstancy — local constancy of confinement

The confinement level ℓ(K, q) is locally constant on Q ∖ ℬ; it changes
only at points of the phase-boundary variety ℬ.

LaTeX: `\label{prop:confinement-local-constancy}`
-/

namespace QOU.BraidKnot

universe u

/-- **Local constancy of confinement level off the phase boundary.**

    Let `R` carry a topology (the substrate parameter space `Q`), let
    `B : Set R` be the phase-boundary variety `ℬ`, and let
    `ℓ : R → ℤ` be the confinement level `ℓ(K, ·)` for a fixed knot.
    Away from `ℬ` the level is locally constant: every `q ∉ B` has an
    open neighborhood `U` on which `ℓ` is constant.

    **Hypothesis `hℓ`** is the manuscript's substantive input: off the
    phase boundary `ℬ`, the level is locally constant — every `x ∉ B`
    has `ℓ` eventually equal to `ℓ x` in its neighborhood filter.  This
    is the property "the level changes only at `ℬ`", justified in the
    manuscript by continuity of the shadow prices `u_λ(q)` (the level is
    determined by their sign pattern, locally constant off `ℬ`); that
    justification needs the confinement-level definition over the
    base-ring topology and is not yet formalised.  Given `hℓ`, the
    theorem produces the explicit open neighborhood at any `q ∉ B`. -/
-- Ref: [leitner2026] climax-volume-mass/local-shadow-ordering
theorem ConfinementLocalConstancy
    (R : Type u) [TopologicalSpace R]
    (B : Set R) (ℓ : R → ℤ)
    (hℓ : ∀ x ∉ B, ∀ᶠ y in nhds x, ℓ y = ℓ x)
    (q : R) (hq : q ∉ B) :
    ∃ U : Set R, IsOpen U ∧ q ∈ U ∧ ∀ q' ∈ U, ℓ q' = ℓ q := by
  -- `ℓ` is eventually `ℓ q` near `q` (locally constant off `ℬ`, `hℓ`);
  -- unpack that neighborhood filter fact into an explicit open set.
  -- Ref: [leitner2026] climax-volume-mass/local-shadow-ordering
  obtain ⟨U, hUsub, hUopen, hqU⟩ := mem_nhds_iff.mp (hℓ q hq)
  exact ⟨U, hUopen, hqU, fun q' hq' => hUsub hq'⟩

end QOU.BraidKnot
