**Remark (Clausen function `Cl_2` as repo-internal Mathlib filler).**

Mathlib does not currently expose the Clausen function

$$
  \mathrm{Cl}_2(\theta)
  \;:=\;
  \sum_{k = 1}^\infty \frac{\sin(k\theta)}{k^2}
  \;=\; \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta}),
$$

which is the imaginary part of the dilogarithm on the unit circle
and the standard ingredient in hyperbolic-volume formulas:

$$
  \mathrm{Vol}(4_1)\;=\;2\,\mathrm{Cl}_2(\pi/3)\;\approx\;:val[Vol_4_1]{precision=6},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3)\;=\;8\,\mathrm{Cl}_2(\pi/4)\;=\;8G\;\approx\;7.327724.
$$

The Lean file [`clausen-function-mathlib-filler.lean`](clausen-function-mathlib-filler.lean)
provides:

See [Table 1](#tbl:clausen-function-mathlib-filler-table1-data).

This unconditionalises the BW values used throughout the α_EM
chain, replacing the previous opaque-or-cited references with
explicit Lean carriers. Downstream blocks
[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode),
[`figure-8-archimedean-illustration`](../braids-and-knots/figure-8-archimedean-illustration.md),
[`bring-hyperbolic-knot-bloch-decomposition`](#prop:bring-hyperbolic-knot-bloch-decomposition),
and
[`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)
can now reference $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and
$\mathrm{Vol}(\mathcal{B}_3)$ via the Lean carriers in this file.

## Mathlib gaps still open after this filler

See [Table 2](#tbl:clausen-function-mathlib-filler-table2-data).

The four §3b-cond classes (BlochSuslinUniqueness, ArchimedeanLimit,
BringZeroModeBlochClass, BringHyperbolicDecomposition,
BWQIndependence, BlochWignerInjective) remain as the residual
mathematical infrastructure gaps — closing them in Lean requires
either upstream Mathlib contributions (the natural place) or
repo-internal substantial formalisations.

## Pattern

Each Mathlib gap is a separate, scoped task. The Cl_2 filler
above shows the cleanest case: one well-known function, defined as
a `tsum`, with two unconditional boundary lemmas and four
sketched-but-open extensions awaiting Fourier-series
infrastructure. The same pattern can be applied to:

* a `Real.dilog` filler (extending the existing `LiTwo` to the
  complex domain via `Complex.dilog`);
* a minimal `BlochGroup F` filler (free abelian group quotient by
  5-term pentagon relations) — substantial, ~200 lines.

These are not addressed here; the present file restricts to the
single-function $\mathrm{Cl}_2$ filler that directly supports the
α_EM and figure-8 chains.
