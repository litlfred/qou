**Remark (Clausen function $\mathrm{Cl}_2$ and hyperbolic volume special values).**

The Clausen function of order two is defined for $\theta \in \mathbb{R}$ by the convergent Fourier sine series

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

On $(0, 2\pi)$, the integral representation has derivative $\mathrm{Cl}_2'(\theta) = -\log(2\sin(\theta/2))$, and the classical Zagier identity equates the Fourier series above with the integral $-\int_0^\theta \log|2\sin(t/2)|\,dt$ via the fundamental theorem of calculus and Abel summation. Building on this integral bridge, a Riemann-sum squeeze of the Kashaev logarithmic sum against the Clausen primitive yields the figure-eight case of the Kashaev volume limit, $(2\pi/N)\log\langle 4_1\rangle_N \to 2\,\mathrm{Cl}_2(\pi/3) = \mathrm{Vol}(4_1)$.

See [Table 1](#tbl:clausen-function-mathlib-filler-table1-data).

These explicit series and integral representations supply the archimedean values $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and $\mathrm{Vol}(\mathcal{B}_3)$ entering the [Bring-surface zero-mode coupling](#prop:em-coupling-bring-zero-mode), the [figure-8 archimedean illustration](../mass-theory/figure-8-archimedean-illustration.md), the [Bring hyperbolic-knot Bloch decomposition](#conj:bring-hyperbolic-knot-bloch-decomposition), and the [Catalan binding scale](../mass-theory/binding-scale-catalan.md).

## Analytic dependencies

See [Table 2](#tbl:clausen-function-mathlib-filler-table2-data).

Beyond the unit-circle Clausen values and the figure-eight Kashaev limit, the broader archimedean chain relies on six analytic ingredients: Bloch–Suslin pentagon uniqueness, the general $q$-Pochhammer archimedean limit, the Bring zero-mode Bloch class, its hyperbolic-knot decomposition, $\mathbb{Q}$-linear independence of the relevant Clausen values, and injectivity of the rationalized Bloch–Wigner regulator.

## Extension to complex dilogarithms and Bloch groups

Defining $\mathrm{Cl}_2$ directly by its sine series establishes the origin boundary identities immediately while isolating higher functional equations to Fourier-series analysis. The same two-stage separation—explicit series or group presentation first, interior analytic theorems second—governs:

* Extending the real unit-interval dilogarithm $\mathrm{Li}_2$ to the cut complex plane $\mathbb{C} \setminus [1, \infty)$.
* Presenting the Bloch group $B(F)$ as the quotient of $\mathbb{Z}[F \setminus \{0, 1\}]$ by the five-term pentagon relations.

Isolating $\mathrm{Cl}_2$ on the unit circle suffices to anchor both the $\alpha_{\text{EM}}$ zero-mode comparisons and the figure-eight volume chain.
