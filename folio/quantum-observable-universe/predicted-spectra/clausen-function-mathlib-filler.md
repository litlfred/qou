**Remark (Clausen function `Cl_2` as repo-internal Mathlib filler).**

Mathlib lacks the Clausen function

$$
  \mathrm{Cl}_2(\theta)
  \;:=\;
  \sum_{k = 1}^\infty \frac{\sin(k\theta)}{k^2}
  \;=\; \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta}).
$$

This function evaluates the imaginary part of the dilogarithm on the unit circle. It dictates standard hyperbolic volume formulas:

$$
  \mathrm{Vol}(4_1)\;=\;2\,\mathrm{Cl}_2(\pi/3)\;\approx\;{{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3)\;=\;8\,\mathrm{Cl}_2(\pi/4)\;=\;8G\;\approx\;7.327724.
$$

The Lean library file [`QOU/Archimedean/ClausenFunctionMathlibFiller.lean`](../lean/QOU/Archimedean/ClausenFunctionMathlibFiller.lean) provides the `Cl_2` series definition and the boundary/volume carriers; the integral-side definition, the derivative `Cl_2'(\theta) = -\log(2\sin(\theta/2))`, and the series–integral bridge (the classical Zagier identity) are machine-proved in [`QOU/Knot/Clausen.lean`](../lean/QOU/Knot/Clausen.lean) (fundamental theorem of calculus plus an Abel-regularised assembly). Building on this infrastructure, the figure-eight case of the Kashaev volume conjecture — the limit $(2\pi/N)\log\langle 4_1\rangle_N \to 2\,\mathrm{Cl}_2(\pi/3) = \mathrm{Vol}(4_1)$ — is itself machine-proved, in [`QOU/Knot/FigureEightVolumeSqueeze.lean`](../lean/QOU/Knot/FigureEightVolumeSqueeze.lean) by a Riemann-sum squeeze of the Kashaev log-sum against the Clausen primitive, with the exact transcendental target $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$.

See [Table 1](#tbl:clausen-function-mathlib-filler-table1-data).

This construction unconditionalizes the Bloch-Wigner values in the $\alpha_{\text{EM}}$ chain. Explicit Lean carriers replace opaque references. The framework references $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and $\mathrm{Vol}(\mathcal{B}_3)$ via these carriers in [`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode), [`figure-8-archimedean-illustration`](../mass-theory/figure-8-archimedean-illustration.md), [`bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition), and [`binding-scale-catalan`](../mass-theory/binding-scale-catalan.md).

## Mathlib gaps

See [Table 2](#tbl:clausen-function-mathlib-filler-table2-data).

Six conditional classes remain as mathematical infrastructure gaps: `BlochSuslinUniqueness`, `ArchimedeanLimit`, `BringZeroModeBlochClass`, `BringHyperbolicDecomposition`, `BWQIndependence`, and `BlochWignerInjective`. Closing these classes requires upstream Mathlib contributions or internal formalization.

## Pattern

Each Mathlib gap forms a scoped task. The $\mathrm{Cl}_2$ filler defines a single function as a `tsum`. It provides two unconditional boundary lemmas. Four sketched extensions require Fourier-series infrastructure. This pattern extends to:

* A `Real.dilog` filler extending `LiTwo` to the complex domain via `Complex.dilog`.
* A `BlochGroup F` filler constructing the free abelian group quotient by 5-term pentagon relations.

This file isolates the $\mathrm{Cl}_2$ filler to support the $\alpha_{\text{EM}}$ and figure-8 chains.
