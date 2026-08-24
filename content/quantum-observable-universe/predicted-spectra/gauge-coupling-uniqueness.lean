import QOU.Archimedean.EmSpectralCompleteness

/-!
# QOU.Archimedean.gauge_coupling_uniqueness

Up to the global normalisation `lam ∈ R`, there is exactly one
non-trivial scalar coupling `A ⊗ A → 𝟙` on the two-strand sector
of `C`.

LaTeX label: `cor:gauge-coupling-uniqueness`

## Repair note (2026-08-22, bean `qou-lsib`)

This file did not compile, and the triage sweep counted it as a
one-error file. It took **three** sequential repairs to reach the real
defect, because Lean halts at the first parse error and never reports
what is behind it:

1. an unterminated docstring at line 20 swallowed the declaration
   (`unterminated comment`);
2. behind it, `∃ λ : S.R` — `λ` is reserved in Lean 4 and cannot be a
   binder name (the corpus spells this `lam`, `l` or `c`);
3. behind *that*, `GaugeCouplingUniquenessData` was **undefined**. It
   appears nowhere in the corpus — not in this file, not in the imported
   `EmSpectralCompleteness`, not anywhere under `content/`. With
   `autoImplicit` on it was silently auto-bound as a metavariable.

**And the shape it was reaching for was a self-assuming projection.** The
declaration read `d.exists_lambda` — the "corollary" was to be the
projection of a field of its own hypothesis structure, which under
§3b-cond item 5 derives nothing. Restoring the missing structure with an
`exists_lambda` field would have made the file compile while proving
nothing, so it is not what is done below.

## What is proved

The `.md` states: *any `R`-linear, braid-invariant, scalar coupling
`A ⊗ A → 𝟙` is a multiple of `tr_τ(e₋)·e₋`*. The linear-algebra content
of that is one-dimensionality of `Hom_R(R, R)`: an `R`-linear map out of
the free rank-one module is determined by its value at `1`, so any two
of them are proportional as soon as the reference map is a unit at `1`.

That is what `gauge_coupling_uniqueness` derives below — from linearity
and the unit hypothesis, not from a field asserting the conclusion. The
identification of the two-strand coupling space with `Hom_R(R, R)` (via
the `e₋` idempotent of `em_spectral_completeness`) is the categorical
step and is **not** formalised here; it remains the block's open content.
-/

set_option autoImplicit false

namespace QOU.Archimedean

/-- Data for the uniqueness statement: two scalar couplings on the
    two-strand sector, presented as maps of the base ring, together with
    the hypotheses the `.md` states — `R`-linearity of each, and
    non-degeneracy of the reference coupling `psi`.

    Every field is a **hypothesis**. None of them is the conclusion. -/
structure GaugeCouplingUniquenessData (S : SpectralRing) where
  /-- The coupling under consideration. -/
  phi : S.R → S.R
  /-- The reference coupling `tr_τ(e₋)·e₋`. -/
  psi : S.R → S.R
  /-- `phi` is `R`-linear: multiplicative against ring scalars. -/
  phi_linear : ∀ r : S.R, phi r = r * phi 1
  /-- `psi` is `R`-linear. -/
  psi_linear : ∀ r : S.R, psi r = r * psi 1
  /-- The reference coupling is non-degenerate — `psi 1` is a unit.
      This is what makes `psi` a basis of the coupling space rather than
      merely an element of it. -/
  psi_one_unit : IsUnit (psi 1)

/-- **Corollary (gauge coupling uniqueness)** — a genuine corollary of
    `em_spectral_completeness` at the categorical level, and, at the
    level formalised here, of one-dimensionality of `Hom_R(R, R)`.

    Any `R`-linear scalar coupling is a global-normalisation multiple of
    the non-degenerate reference coupling. The witness is
    `lam = phi 1 · (psi 1)⁻¹`, derived from the hypotheses. -/
theorem gauge_coupling_uniqueness (S : SpectralRing)
    (d : GaugeCouplingUniquenessData S) :
    ∃ lam : S.R, ∀ r : S.R, d.phi r = lam * d.psi r := by
  obtain ⟨u, hu⟩ := d.psi_one_unit
  refine ⟨d.phi 1 * (↑u⁻¹ : S.R), fun r => ?_⟩
  rw [d.phi_linear r, d.psi_linear r]
  have hone : (↑u⁻¹ : S.R) * d.psi 1 = 1 := by
    rw [← hu]; exact u.inv_mul
  calc r * d.phi 1
      = d.phi 1 * ((↑u⁻¹ : S.R) * d.psi 1) * r := by rw [hone]; ring
    _ = d.phi 1 * (↑u⁻¹ : S.R) * (r * d.psi 1) := by ring

end QOU.Archimedean
