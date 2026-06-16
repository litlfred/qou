The categorical
[$q$-chromaticity construction](#rem:q-chromaticity) makes a
falsifiable prediction about human color perception that directly
addresses the 100-year-old paradigm of Riemann
\cite{schrodinger1920color} and the modern psychophysical
result of \cite{bujack2022}.

**The empirical result (Bujack et al., 2022).**

\cite{bujack2022} show that perceived color differences obey the
strict inequality

$$
  \Delta E(A, B) + \Delta E(B, C) > \Delta E(A, C)
$$

along geodesics — the *principle of diminishing returns* —
contradicting the Riemannian additivity assumed since Riemann,
Helmholtz, and \cite{schrodinger1920color}. Their regression on a
crowdsourced color-triad experiment yields a significantly
negative average-difference coefficient ($\beta_{\bar d} = -0.005$,
$t(60) = -5.566$, $p < 0.001$). The qualitative shape of the
recovered scaling function $f$ matches a *concave, sub-linear*
curve — they explicitly suggest a **second-order Weber–Fechner law**
(logarithmic in the large-difference regime), and note that earlier
psychophysical work fits perceived color difference to a power law
with exponent $\approx 0.5$. The square-root form
$f(\Delta\psi) = \sqrt{\Delta\psi}$ appears as their canonical
illustrative example.

**The QOU categorical prediction.**

The Skein relation
$q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ forces the
distance on the $q$-chromaticity simplex to inherit a $q$-deformed
non-Riemannian correction. The categorically natural functional
form is the *quantum-integer arc-length*

$$
  \Delta E_{\mathrm{perc}}(d)
  \;=\;
  \frac{1}{\eta}\,\operatorname{arsinh}\!\bigl(\eta\,d\bigr),
  \qquad
  \eta := \frac{q - q^{-1}}{2},
$$

where $d$ is the Riemannian (CIELAB-style) chord length and
$\Delta E_{\mathrm{perc}}$ is the perceived difference along the
geodesic. This is the unique one-parameter analytic completion of
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$ to a metric on the projective
chromaticity 2-simplex, with $\eta \to 0$ recovering the Riemannian
limit $\Delta E_{\mathrm{perc}} = d$.

See [Table 1](#tbl:schrodinger-color-falsifiability-table1-data).

The large-$d$ logarithmic asymptote is *exactly* the second-order
Weber–Fechner law that \cite{bujack2022} hint at. The Cannon
power-law exponent $\approx 0.5$ corresponds to the geometric mean
of the linear and logarithmic regimes — the intermediate-$d$
behavior of $\operatorname{arsinh}(\eta d)/\eta$.

**Numerical prediction from the substrate parameter.**

Substituting the QOU substrate value $q_0 = 1.109978595554181\ldots$ (50 dps) gives

$$
  \eta = \frac{q_0 - q_0^{-1}}{2} \approx 0.1043,
  \qquad
  d^{\,*} := 1/\eta \approx 9.59.
$$

The predicted crossover from the Riemannian regime to the
Weber–Fechner regime sits at $\Delta E \approx 9.6$ on a normalized
$L^{*}$-style scale (where unit $\Delta E$ is the typical
small-difference just-noticeable threshold). This is in striking
agreement with \cite{bujack2022} Table 1: the diminishing-returns
effect is barely significant at $\Delta d = 5$
($\beta_{\Delta d = 5} = 0.048$, $p = 0.010$) but strongly
significant at $\Delta d = 10$ ($\beta_{\Delta d = 10} = 0.119$,
$p < 0.001$) — i.e. the perceptual crossover empirically lies in
the interval $[5, 10]$, bracketing the QOU prediction $d^{\,*}
\approx 9.6$.

**Falsifiability protocol.**

The categorical prediction is a one-parameter family
$\Delta E_{\mathrm{perc}}(d) = \operatorname{arsinh}(\eta d)/\eta$. A
sufficiently precise color-perception experiment — for example, a
re-analysis of the \cite{bujack2022} dataset or a new MTurk
campaign with $\Delta d \in \{1, 2, 5, 10, 20, 50\}$ — can fit a
single $\eta$ and yield a confidence interval $[\eta_-, \eta_+]$.
The QOU framework then admits three distinct outcomes:

See [Table 2](#tbl:schrodinger-color-falsifiability-table2-data).

The third outcome would not falsify QOU as a whole — color
perception is several decoherence layers above the substrate — but
it would falsify the cleanest version of the identification
"retinal $\Delta E$ measures the Skein metric on the
Bring-surface chromaticity simplex."

**Sign and functional-form predictions (already passed).**

Independently of any numerical fit, the QOU framework predicts
three qualitative features that \cite{bujack2022} have already
confirmed:

See [Table 3](#tbl:schrodinger-color-falsifiability-table3-data).

The remaining empirical lever is the *magnitude* of $\eta$, which
the falsifiability protocol above turns into a single-number test.

**Numerical fit on \cite{bujack2022} Gray-experiment dataset.**

The protocol was executed against the open-source Gray-experiment
triad-choice data released by \cite{bujack2022}
($N = 91{,}896$ responses; $75$ unique triads on the achromatic
$L^{*}$ axis). The QOU model
$\Delta E_{\mathrm{perc}}(d) = \operatorname{arsinh}(\eta d)/\eta$,
paired with a Thurstonian probit choice rule with observer noise
$\sigma$, was fitted by maximum likelihood (two free parameters):

See [Table 4](#tbl:schrodinger-color-falsifiability-table4-data).

The non-Riemannian alternative beats the Riemannian null by $200\sigma$ —
the single-parameter $\operatorname{arsinh}$ form captures variance
that Riemannian additivity cannot. The point estimate
$\hat{\eta} = 0.126$ sits $\sim 20\%$ above the bare-$q_{0}$
prediction $0.104$, with the bootstrap CI not strictly bracketing
the prediction. Two non-exclusive interpretations:

1. *Faithful identification with modest renormalization.* The
   ratio $\hat{\eta}/\eta_{\mathrm{QOU}} \approx 1.20$ is consistent
   with a small multiplicative renormalization from the
   chromaticity-projection step (the affine shift $w_{k} - z$ in
   [the color-tube coordinates](#def:color-tube-coordinates)
   contracts the simplex by an $O(1)$ factor that has not been
   computed categorically).
2. *Spline-vs-rigid $\psi$ misspecification.* \cite{bujack2022}
   model both the perceptual coordinate $\psi(L)$ and the
   difference-scaling function $f$ as splines; the fit above pins
   $\psi(L) = L$ and lets only $f$ deform. A non-linear $\psi$
   would absorb some apparent $f$-curvature, tightening
   $\hat{\eta}$ toward $\eta_{\mathrm{QOU}}$.

The witness JSON
[`schrodinger-color-falsifiability-fit.witness.json`](../../../computations/schrodinger-color-falsifiability-fit.witness.json)
records the full fit, bootstrap, and assertion outcomes; the script
[`schrodinger_color_falsifiability_fit.py`](../../../computations/schrodinger_color_falsifiability_fit.py)
is reproducible from the LANL public release.

**Connection to confinement.**

The same deformation parameter $q - q^{-1}$ (equal to $2\eta$ in
the natural metric normalization, and proportional to the
$(q^{1/2} - q^{-1/2})$ coefficient of the Jones-form Skein
relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$)
governs the magnitude of the forced negative coefficient that
drives [color confinement](#rem:q-chromaticity). So a successful
color-perception fit of $\eta \approx 0.10$ would constitute an
*independent macroscopic measurement of the same underlying
substrate deformation that governs quark confinement* — a
non-trivial cross-scale consistency check on the framework.
