# StaircaseEWResidual proof attempt — 2026-05-17

## Conjecture statement

The class `StaircaseEWResidual q scale` asserts that for every
`k ≥ 2`, the matrix image of the canonical β_EW Δ_I^minimal word on
the staircase Specht module `V_{ρk}` has two nonzero eigenvalues
whose ratio is `scale k` — formally,

  `HasEigenvalueRatio (wordImage (betaEWWord (staircaseStrands k))) (scale k)`

where `HasEigenvalueRatio M r ↔ ∃ μ ≠ 0, (X-μ)(X-r·μ) ∣ M.charpoly`.

**Empirical content**: at the substrate parameter `q_0 ≈ 1.110`,
with `scale k = q^(1/(2k-1))`, the conjecture holds within:
- `k = 3`: 0.13 % relative error (cot θ_W gap closure)
- `k = 4`: 0.14 % relative error (pairwise-ratio search in dim-768)

## Structural blocker

The existing instance in `StaircaseCornerHook.lean`:

```lean
instance staircase_ew_residual_conjecture
    {R A : Type*} [CommRing R] [Inv R] [Ring A] [Algebra R A]
    (q : R) (scale : ℕ → R) [...] : StaircaseEWResidual q scale where
  spectral_scale_present := fun _ _ => sorry
```

universally quantifies over `scale`. **This is strictly stronger than
the conjecture**: for ARBITRARY `scale`, there's no reason a specific
Hoefsmit-matrix has eigenvalues in that exact ratio.

The actual conjectural content is:

  **∃ scale, ∀ k ≥ 2, HasEigenvalueRatio (wordImage ...) (scale k)**

with `scale k` empirically pinned to `q^(1/(2k-1))`.

## Attempted proof routes

1. **Vacuous witness via degenerate scale**: setting `scale = fun _ => 0`
   reduces the claim to "Hoefsmit matrix has 0 as an eigenvalue + nonzero
   eigenvalue". Generically true for non-degenerate non-zero matrices, but
   we don't have the Hoefsmit-matrix concreteness in Lean to verify.

2. **Special case k = 2**: at k=2 the staircase is ρ_2 = (2,1) with
   strand count 3. The Specht module V_{(2,1)} has dim 2, so the
   characteristic polynomial of any matrix on it has degree 2.
   Divisibility `(X-μ)(X-rμ) ∣ charpoly` becomes equality up to
   leading coefficient, fully determined by det and trace. Empirically
   verified, but Lean port requires explicit Hoefsmit matrices we
   haven't built up.

3. **Existence-only proof**: prove `∃ scale, StaircaseEWResidual q scale`
   by post-hoc choosing `scale k = μ₂/μ₁` from the actual eigenvalues
   of the matrix. This is mathematically vacuous but Lean-provable —
   IF we have concrete Hoefsmit data.

## Verdict

**The conjecture is genuinely open at the Lean level** until either:
- The Hoefsmit matrix construction is concrete (currently axiomatized
  in `QOU/HeckeAlgebra/Hoefsmit.lean`), OR
- The instance signature is refined to `scale = q^(1/(2k-1))` and the
  corresponding `betaEW` operator has a constructed eigenstructure.

Both routes are multi-session Lean port work, not a single-session
discharge.

The `sorry` in `staircase_ew_residual_conjecture` instance correctly
records this — it IS the conjecture per §3b-cond.

## Recommendation

Leave the sorry as-is. The instance signature should be REFINED in a
follow-up to use the specific `q^(1/(2k-1))` scale; that refinement
would make the conjecture proveable conditional on Hoefsmit-matrix
concreteness.

For documentation of the empirical content, see
`computations/staircase-ew-residual-conjecture.witness.json`
and `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`.
