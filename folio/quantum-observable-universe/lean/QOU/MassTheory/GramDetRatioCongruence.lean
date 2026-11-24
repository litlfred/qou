/-
# A Gram determinant RATIO is congruence-invariant

`prop:em-coupling-chern-simons` predicts `1/α_EM` using

    κ = det G_CS^cl / det G_CS^q

and lists **two** ambiguities as reasons the value is not pinned down:

> "The Gram matrix is dimensionally ambiguous. The choice of basis for the
>  rank-2 sublattice and the explicit form of `s_i, ℓ, c_i` in the
>  q-deformed setting are not fixed."

The first of those is not an ambiguity.  A Gram matrix transforms by
congruence, `G ↦ Bᵀ * G * B`, and `det` picks up `(det B)^2` — the *same*
factor on the classical and the q-deformed side — so it cancels in the
ratio.  `κ` is therefore independent of the basis, for **any** invertible
`B`: unimodular, non-unimodular (a finite-index sublattice), or with
irrational entries.

Two things this does and does not say:

* It applies when **one** basis is chosen and both forms are expressed in
  it.  Choosing genuinely different bases for the two sides is not a
  change of basis for the pairing; it is a different pair of matrices, and
  nothing here constrains it.
* It says nothing about whether `κ ≈ 1.7216` is the *right* value.  It
  removes one named source of freedom, leaving the other — the q-reading
  of `s_i, ℓ, c_i` — as the whole of the block's stated ambiguity.  That
  remaining family is finite and is enumerated in
  `computations/alpha/alpha_em_kappa_qdeformation_family_probe.py`.

This is the determinant analogue of `gauge_ratio_invariant` in
`QOU/Archimedean/GaugeGroupThreeScale.lean`, which states the same
degree-0 principle for a ratio of Schur scalars.  That file's warning
carries over verbatim: a gauge law constrains *conventions*; it does not
supply a value.

Base ring: generic per AGENTS.md §7c.  The congruence identity holds over
any `CommRing`; only the ratio needs division, hence a `Field`, and no
archimedean structure is used anywhere.

-- Ref: [serre1977] https://doi.org/10.1007/978-1-4684-9458-7
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace QOU.Archimedean

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Congruence scales a determinant by `(det B)^2`.

Over any commutative ring: `det (Bᵀ * G * B) = (det B)^2 * det G`. -/
theorem det_congr_eq {R : Type*} [CommRing R] (B G : Matrix n n R) :
    (Bᵀ * G * B).det = B.det ^ 2 * G.det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose]
  ring

/-- **The ratio of two Gram determinants is congruence-invariant.**

If both forms are transported by the *same* invertible `B`, the
`(det B)^2` cancels and the ratio is unchanged.  No hypothesis is placed
on `B` beyond `det B ≠ 0` — in particular it need not be unimodular, so a
change of sublattice does not move the ratio either. -/
theorem gramDetRatio_congr_invariant {K : Type*} [Field K]
    (B Gcl Gq : Matrix n n K) (hB : B.det ≠ 0) :
    (Bᵀ * Gcl * B).det / (Bᵀ * Gq * B).det = Gcl.det / Gq.det := by
  rw [det_congr_eq, det_congr_eq, mul_div_mul_left _ _ (pow_ne_zero 2 hB)]

/-- The ratio is the *same* for any two admissible bases: it is a function
of the pair of forms alone.  This is the statement the `.md`'s "the choice
of basis for the rank-2 sublattice is not fixed" would have to contradict
in order to be a source of freedom in `κ`. -/
theorem gramDetRatio_indep_of_basis {K : Type*} [Field K]
    (B B' Gcl Gq : Matrix n n K) (hB : B.det ≠ 0) (hB' : B'.det ≠ 0) :
    (Bᵀ * Gcl * B).det / (Bᵀ * Gq * B).det
      = (B'ᵀ * Gcl * B').det / (B'ᵀ * Gq * B').det := by
  rw [gramDetRatio_congr_invariant B Gcl Gq hB,
    gramDetRatio_congr_invariant B' Gcl Gq hB']

end QOU.Archimedean
