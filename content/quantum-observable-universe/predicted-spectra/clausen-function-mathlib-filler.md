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
[`bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition),
and
[`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)
can now reference $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and
$\mathrm{Vol}(\mathcal{B}_3)$ via the Lean carriers in this file.
