# Deriving the exterior-quotient antisymmetry (Λ²V, Λ³W)

Date: 2026-11-27. Bean: `qou-x08k` (session), open gaps in `qou-x09d`.
Lean: `QOU/Core/ExteriorAntisymmetryDerivation.lean` (sorry-free; `#print axioms`
gives `propext, Quot.sound` only). Generic commutative ring `R`; no empirical input.

## The question

Owner, 2026-11-27: *"What is the justification for these axioms physically? Where
are they coming from?"* and *"Are these something derivable as we derived q?"*
PR #9723 adds, as axiom fields, that the braiding acts on `Λ²V ≅ 𝟙` by `−s⁻¹` and on
`Λ³W ≅ 𝟙` by a scalar `c` with `θ_V = s`, `θ_W = t`. This note records what of
that follows from the existing axioms and what does not. #9723 stays held.

## The one identity behind everything

`quotient_balancing`: for `π : X ⊗ X ↠ L`, `L ≅ Y`, `θ_X = s`, `θ_Y = u` and the
braiding acting on `π` by `c`, the balancing axiom gives `(s²c² − u)·π = 0`.

## V

1. **Balancing fixes the braiding scalar on `Λ²V ≅ 𝟙` up to sign:** `s²c² = 1`.
   It does not fix the sign. The antisymmetric reading `c = −s⁻¹` is a choice the
   axioms permit, not one they force. (Scope (a): the symmetric quotient with
   `c = +s⁻¹` satisfies the same axioms.)
2. **The Hecke relation `(σ − q)(σ + q⁻¹) = 0` on all of `V ⊗ V` does NOT follow
   from the existing axioms.** Balancing constrains only the summand `≅ 𝟙`; it is
   silent on `S²V`. Counterexample at paper level: `V` = the spin-1 module of
   `Rep_q(SL₂)`, `V ⊗ V = V₂ ⊕ V₁ ⊕ V₀` with three braiding eigenvalues, and the
   projection onto `V₀ ≅ 𝟙` is an epi with `θ_V` scalar. All existing fields hold;
   no quadratic relation holds. A Lean counterexample needs a non-symmetric
   braided category and is not attempted here.
3. **Derived repair of the twist normalisation.** If one does impose the Hecke
   value `c = −q⁻¹` on `Λ²V ≅ 𝟙`, then `hecke_forces_twist_sq` gives
   `(s² − q²)·𝟙 = 0`: the twist is `θ_V = ±q`, **not** `q^{1/2}`. The corpus pair
   `θ_V = q^{1/2}`, `c = −q⁻¹` forces `q = 1` (`hecke_halfTwist_forces_q_one`, on
   #9723). This is derived, not chosen.
4. **Corpus defect.** `braiding-eigenvalue-extraction` asserts `λ₊λ₋ = −1`
   (`λ₋ = −q⁻¹` with `q := λ₊`). In `Rep_q(SL₂)` with `λ₊ = Q` one has
   `λ₋ = −Q⁻³` and `θ_V = Q³`. The Hecke-normalised braiding belongs to `GL_q`,
   where `Λ²V = det` is not `≅ 𝟙`. So `λ₊λ₋ = −1` together with `Λ²V ≅ 𝟙` is a
   choice of normalisation that the corpus does not derive. Not edited here.

## W

5. **The cube `Λ³W ≅ 𝟙` gives only `(c²t)³ = 1`** (#9723,
   `exteriorCube_balancing_unit`).
6. **A ℤ/3 grading cannot be the source of the root.** Re-braiding by a ℤ/3
   bicharacter `χ` multiplies the braiding on `W ⊗ W` and the twist of `W` by the
   same `ω = χ(g,g)`, and `rebraid_invariant` gives `(ωc)²(ωt) = c²t` when
   `ω³ = 1`. The same argument covers grouplikes, which act through a grading.
   Scope (b): the invariant is `ω³ = 1`.
7. **The dual fixes it.** Reading the square `Λ²W` as the dual `Wᘁ` (as at the
   fibre, where the wedge pairing `W ⊗ Λ²W → Λ³W ≅ 𝟙` is perfect), the ribbon
   axiom `θ_{Xᘁ} = (θ_X)ᘁ` gives `θ_{Λ²W} = t` (`twist_dual_of_scalar`), and
   balancing then gives `c²t = 1` (`flavour_root_eq_one`, `t` a unit). This is
   the Drinfeld–Jimbo normalisation.

## What stays open (bean `qou-x09d`)

- `Λ²W ≅ Wᘁ` is a **hypothesis** in item 7. It is not derived from the current
  axioms; it would follow from a perfect wedge pairing, which is not an axiom.
- The sign in item 1 and the Hecke relation in item 2 are not derived. A
  possible route is the pivotal partial-trace relation
  `θ_V = λ₊(d − d⁻¹) + λ₋ d⁻¹` (`MathlibExt/PivotalCategory.lean`), not tried here.
- The multi-fibre groupoid was not examined as a source for item 6; item 6
  excludes only gradings and grouplikes.
