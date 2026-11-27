The categorical [$q$-chromaticity construction](#rem:q-chromaticity) yields a falsifiable prediction regarding human color perception. This challenges the Riemannian paradigm \cite{schrodinger1920color} and aligns with the modern psychophysical results of Bujack et al. \cite{bujack2022}.

**The empirical result (Bujack et al., 2022).**

Bujack et al. \cite{bujack2022} report experimental evidence that perceived color differences violate Riemannian additivity along geodesics. The observed differences satisfy the strict inequality:

$$
  \Delta E(A, B) + \Delta E(B, C) > \Delta E(A, C).
$$

This diminishing-returns principle contradicts the assumptions of Riemann, Helmholtz, and Schrödinger \cite{schrodinger1920color}. A crowdsourced color-triad experiment ($75{,}896$ training trials across ten splits, $R^2 = 0.556$, $F(3, 60) = 25.00$, $p < 0.001$) yielded a negative average-difference coefficient ($\beta_{\bar d} = -0.005$, $t(60) = -5.566$, $p < 0.001$) \cite[Results, Table~1]{bujack2022}. Among the parameterized scaling candidates in \cite[Eq.~(18)]{bujack2022}, the logarithmic model $f_{\log}(\Delta\psi) = b\log(a\Delta\psi + 1)/\log(a + 1)$ matched the flexible monotonic spline in predictive accuracy, leading Bujack et al. to propose a second-order Weber–Fechner law in which perceived differences grow logarithmically at large stimulus separations \cite[Discussion]{bujack2022}. Prior psychophysical studies fit perceived color differences to a power law with an exponent near $0.5$.

**The categorical prediction.**

The Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ deforms the distance on the $q$-chromaticity simplex. The distance inherits a non-Riemannian correction matching the quantum-integer arc-length:

$$
  \Delta E_{\mathrm{perc}}(d)
  \;=\;
  \frac{1}{\eta}\,\mathrm{arsinh}\!\bigl(\eta\,d\bigr),
  \qquad
  \eta := \frac{q - q^{-1}}{2}.
$$

Here $d$ denotes the Riemannian chord length, and $\Delta E_{\mathrm{perc}}$ denotes the perceived geodesic difference. This function constitutes the unique analytic one-parameter extension of $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ to a projective chromaticity 2-simplex metric. The limit $\eta \to 0$ recovers the purely Riemannian metric $\Delta E_{\mathrm{perc}} = d$.

See [Table 1](#tbl:schrodinger-color-falsifiability-table1-data).

The large-$d$ logarithmic asymptote precisely matches the second-order Weber–Fechner law suggested by \cite{bujack2022}. The empirical power-law exponent of $\approx 0.5$ captures the intermediate-$d$ behavior of $\mathrm{arsinh}(\eta d)/\eta$, mapping the transition between the linear and logarithmic regimes.

**Numerical prediction from the substrate parameter.**

Evaluation at the proton-pinned substrate value $q_0 = 1.1099785827513808\ldots$ determines $\eta$ and the crossover scale $d^{\,*}$:

$$
  \eta = \frac{q_0 - q_0^{-1}}{2} = 0.10453015\ldots \approx 0.1045,
  \qquad
  d^{\,*} := 1/\eta = 9.5666179\ldots \approx 9.57.
$$

On this reading the transition from Riemannian to Weber–Fechner scaling occurs near $\Delta E \approx 9.57$ on a normalized $L^{*}$-style scale. The cited experiment does not measure a crossover scale, so it neither corroborates nor refutes this value. In its regression the two coefficients indexed by the difference of differences, $\beta_{\Delta d = 5} = 0.048$ ($t(60) = 2.815$, $p = 0.010$) and $\beta_{\Delta d = 10} = 0.119$ ($t(60) = 6.632$, $p < 0.001$), are level effects of $\Delta d$, not the onset of diminishing returns at a particular scale. The only diminishing-returns coefficient is $\beta_{\bar d} = -0.005$, and the authors read its negativity as weak support for nonadditivity, conditional on the $L^{*}$ axis being nearly perceptually uniform, an assumption they note may not hold due to background crispening \cite[Results, Table~1; Fig.~7]{bujack2022}. The crossover scale $d^{\,*} \approx 9.57$ therefore has no empirical comparison in that source.

**Falsifiability protocol.**

The categorical prediction forms a one-parameter family $\Delta E_{\mathrm{perc}}(d) = \mathrm{arsinh}(\eta d)/\eta$. A high-precision color-perception experiment can fit $\eta$ to a confidence interval $[\eta_-, \eta_+]$. This forces three possible outcomes:

See [Table 2](#tbl:schrodinger-color-falsifiability-table2-data).

An inconsistent measurement falsifies the hypothesis that retinal $\Delta E$ directly measures the Skein metric on the Bring-surface chromaticity simplex. It leaves the broader framework intact, because color perception operates several decoherence layers above the substrate.

**Sign and functional-form predictions.**

The framework makes three qualitative predictions already confirmed by \cite{bujack2022}, independent of numerical fitting:

See [Table 3](#tbl:schrodinger-color-falsifiability-table3-data).

The final empirical test lies in measuring the magnitude of $\eta$.

**Connection to confinement.**

The deformation parameter $q - q^{-1} = 2\eta$ determines the magnitude of the forced negative coefficients driving [color confinement](#rem:q-chromaticity). Measuring $\eta \approx 0.10$ via macroscopic color perception provides an independent measurement of the substrate deformation governing quark confinement.
