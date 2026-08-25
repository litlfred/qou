The categorical [$q$-chromaticity construction](#rem:q-chromaticity) yields a falsifiable prediction regarding human color perception. This challenges the Riemannian paradigm \cite{schrodinger1920color} and aligns with the modern psychophysical results of Bujack et al. \cite{bujack2022}.

**The empirical result (Bujack et al., 2022).**

Bujack et al. \cite{bujack2022} proved that perceived color differences violate Riemannian additivity along geodesics. The observed differences satisfy the strict inequality:

$$
  \Delta E(A, B) + \Delta E(B, C) > \Delta E(A, C).
$$

This diminishing-returns principle contradicts the assumptions of Riemann, Helmholtz, and Schrödinger \cite{schrodinger1920color}. A crowdsourced color-triad experiment yielded a negative average-difference coefficient ($\beta_{\bar d} = -0.005$, $t(60) = -5.566$, $p < 0.001$). The observed scaling function exhibits concave, sub-linear curvature. Bujack et al. suggested a second-order Weber–Fechner law, which applies logarithmic scaling at large differences. Prior psychophysical studies fit perceived color differences to a power law with an exponent near $0.5$.

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

Evaluation at the substrate value $q_0 \approx 1.109978595554181$ determines $\eta$ and the crossover scale $d^{\,*}$:

$$
  \eta = \frac{q_0 - q_0^{-1}}{2} \approx 0.1043,
  \qquad
  d^{\,*} := 1/\eta \approx 9.59.
$$

The transition from Riemannian to Weber–Fechner scaling occurs at $\Delta E \approx 9.6$ on a normalized $L^{*}$-style scale. This closely matches the empirical crossover. Bujack et al. \cite{bujack2022} found the diminishing-returns effect barely significant at $\Delta d = 5$ ($\beta_{\Delta d = 5} = 0.048$, $p = 0.010$) and strongly significant at $\Delta d = 10$ ($\beta_{\Delta d = 10} = 0.119$, $p < 0.001$). The perceptual crossover empirically lies in $[5, 10]$, bracketing the predicted $d^{\,*} \approx 9.6$.

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
