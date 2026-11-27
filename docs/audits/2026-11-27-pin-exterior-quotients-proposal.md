# Proposal: pin `Λ²V` and `Λ³W` as antisymmetric quotients

Status: **proposal, no axiom changed.** Bean `qou-x08k`. Follows PRs #9688 and #9702.

## The decision

Should the core axioms require the exterior quotients to be *antisymmetric*? Today
`exteriorSquare` (for `V`) and `exteriorCube` (for `W`) only have to be *some* quotient of
`V ⊗ V` and `W ⊗ W ⊗ W`. If nothing is added, the dimension statements `dim V = 2` and
`dim W = 3` hold only at the fibre reading, not in the categorical axioms.

## Why it matters (measured)

- `QOU.FlavourLabelCarrier.unit_flavour_meets_axioms` (#9688): a **one-dimensional** `W`
  (the unit with a `ℤ/3` label) meets every categorical flavour field.
- `QOU.FlavourVolumeForcesDimThree.exteriorCubeDim_eq_one_iff` (#9702): at a fibre where the
  quotient really is `Λ³`, `Λ³W ≅ 𝟙` gives `C(N,3) = 1`, which holds only for `N = 3`. The
  one-dimensional `W` has `C(1,3) = 0`.
- `V` has the same feature. `exteriorSquare := V ⊗ V` with `V = 𝟙` meets
  `exteriorSquare_epi` and `volumeIso`, while `C(1,2) = 0` at the fibre.

So the gap is not missing structure on `W`. It is that neither quotient is tied to the
braiding.

## Proposed fields

The twist already fixes `q`: on the defining object `θ_V = q^{1/2}·id_V`
(`rem:sqrt-q-ribbon-structure`, field `balancedInst`). The proposal ties each quotient to the
braiding eigenvalue that the antisymmetric part carries, `−q⁻¹`, with `q` read off the twist
and not added as a field.

```lean
-- QuantumObservableUniverse (for V)
twistScalar : R                                   -- s with θ_V = s • 𝟙 V, so q = s²
twist_fundamental : θ_V = twistScalar • 𝟙 fundamentalObj
twistScalar_isUnit : IsUnit twistScalar
exteriorSquare_antisym :
  (β_ fundamentalObj fundamentalObj).hom ≫ exteriorSquareProj
    = (-(twistScalar ^ 2)⁻¹) • exteriorSquareProj     -- −q⁻¹

-- FlavouredQuantumObservableUniverse (for W): both adjacent crossings act by the same scalar
flavourBraidScalar : R
exteriorCube_antisym₁ : ((β_ W W).hom ▷ W) ≫ exteriorCubeProj
    = flavourBraidScalar • exteriorCubeProj
exteriorCube_antisym₂ : (α_ W W W).hom ≫ (W ◁ (β_ W W).hom) ≫ (α_ W W W).inv ≫ exteriorCubeProj
    = flavourBraidScalar • exteriorCubeProj
```

(The `⁻¹` is via the unit `twistScalar_isUnit`; written loosely above.)

### What it excludes

On `V = 𝟙` the braiding on `𝟙 ⊗ 𝟙` is the identity and `θ_𝟙 = 𝟙`, so `q = 1` and the pin
reads `π = −π`. When `2` is invertible in `R` this forces `π = 0`. Since `π` is epi, the
quotient is zero and cannot be `≅ 𝟙` over a nontrivial ring. That is the counterexample the
pin is meant to remove. This is checked by hand here, not in Lean.

## Costs and risks

- **Blast radius (measured 2026-11-27).** There are no constructed instances of
  `QuantumObservableUniverse` or `FlavouredQuantumObservableUniverse` in the tree. The
  fields appear in two structure definitions, `QOU/Core/CategoricalFoundations.lean` and the
  content-block copy `quantum-observable-universes/quantum-observable-universe.lean`, and in
  `FlavouredQuantumObservableUniverse.lean`. Three further files only read `volumeIso`
  (`su2-emergence.lean`, `qou-exists-axiom-4.lean`, `FlavourCentralPhase.lean`) and are not
  affected by an added field. The narrative `def:quantum-observable-universe` condition
  (iii)/(v) must be updated to match.
- **It drops the "no eigenvalue condition" stance.** The current docstring deliberately
  avoids an eigenvalue so as not to impose `q = 1`. The proposal avoids that by using `−q⁻¹`
  with `q` from the twist. But it does commit the axioms to the Hecke normalisation of the
  braiding on `V ⊗ V`.
- **The flavour scalar is left free.** On `W ⊗ W` the braiding of `SU_q(3)` has
  eigenvalues `q` and `−q⁻¹` only up to a central factor (`q^{±1/3}` in the usual
  normalisation), and `W`'s twist is not `q^{1/2}`. Fixing `flavourBraidScalar` from `W`'s own
  twist is a sub-question this proposal does not settle. Left free it does **not** exclude the
  one-dimensional `W`: there the braiding is the identity, so the scalar `1` satisfies both
  fields. It excludes it once `1 - flavourBraidScalar` is required to be regular, because
  then `(1 - c) • π = 0` forces `π = 0`.
- **Reversibility.** Adding fields is easy to undo while no instance exists.

## What it commits to

Every future construction of a quantum observable universe must supply the twist scalar and
prove the antisymmetry of its quotients. That is the work that turns the fibre dimension
statements into categorical ones.

## Default if nothing is decided

Nothing changes. The dimension results stay fibre-level, recorded in #9702 and the eightfold
chapter exposition.
