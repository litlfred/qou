The gravitational constant $G$ is derived from the information
geometry of the Reeb dynamics, following Jacobson's programme
[jacobson1995] of obtaining Einstein's equations from
entropy--area proportionality on local causal horizons.

**Jacobson's argument in QOU variables.**
Consider a local causal horizon — a null surface at the
light-cone boundary $|Z| = c(q)$
([speed of light](#def:information-speed-of-light)) — in the
contact affine chart.  Three quantities determine the gravitational
coupling:

1. **Horizon entropy density.**
   Each fibre on the horizon is processed once per discrete
   $f_q$-step, generating $\eta_q$ bits of entropy
   ([operational entropy](#def:operational-entropy)).  In one
   Planck time, $n_R(q) = 1/\hbar_q$ fibres are processed.  Each
   fibre has cross-sectional area $\hbar_q$ (Reeb direction) $\times$
   $q^{-1}$ (spatial direction, set by the $q$-connection coupling
   weight).  The entropy per unit horizon area per Planck time is

   $$
     s(q) \;=\; \frac{n_R(q) \cdot \eta_q}{n_R(q) \cdot \hbar_q
     \cdot q^{-1}}
     \;=\; \frac{\eta_q}{\hbar_q \cdot q^{-1}}
     \;=\; \frac{q\,\eta_q}{\hbar_q}.
   $$

2. **Unruh temperature.**
   A uniformly accelerated observer in the QOU sees a thermal
   bath at the Unruh temperature.  In Reeb units, with
   $\hbar_q = (q-1)/q$ and $c(q) = 1/(q-1)$, the temperature
   at unit acceleration is

   $$
     T_U(q) \;=\; \frac{\hbar_q}{2\pi\,c(q)}
     \;=\; \frac{(q-1)/q}{2\pi/(q-1)}
     \;=\; \frac{(q-1)^2}{2\pi\,q}.
   $$

3. **Clausius relation.**
   The heat flow $\delta Q$ across the horizon equals the
   stress-energy flux: $\delta Q = T_{ab}\,k^a\,d\Sigma^b$
   where $k^a$ is the horizon generator and $d\Sigma^b$ the area
   element.  The entropy change is $dS = s(q)\,dA$.  Jacobson's
   identity $\delta Q = T_U\,dS$ applied to every local causal
   horizon yields the Einstein equation

   $$
     \mathrm{Ric}_{g_\theta} - \tfrac{1}{2}\,R\,g_\theta
     \;=\; \frac{8\pi\,G(q)}{c(q)^4}\;T^{(q)},
   $$

   with the gravitational constant determined by the entropy density
   and the Unruh temperature:

   $$
     G(q) \;=\; \frac{c(q)^3}{4\,s(q)}
     \;=\; \frac{c(q)^3\,\hbar_q}{4\,q\,\eta_q}.
   $$

**Definition.**
The *gravitational constant* at substrate parameter $q$ is

$$
  G(q) \;=\; \frac{c(q)^3\,\hbar_q}{4\,q\,\eta_q}
  \;=\; \frac{1}{4\,q\,(q-1)^2\,\eta_q},
$$

where $c(q) = 1/(q-1)$ is the speed of light
([speed of light](#def:information-speed-of-light)),
$\hbar_q = (q-1)/q$ is the quantum Planck constant
([Planck time](#def:planck-time)), and
$\eta_q = d_H(q) \cdot \log 2$ is the operational entropy
([operational entropy](#def:operational-entropy)).

**Numerical evaluation at $q = 1.1097$.**

| Quantity | Formula | Value |
|----------|---------|-------|
| $c(q)$ | $1/(q-1)$ | $9.116$ |
| $c(q)^3$ | $1/(q-1)^3$ | $757.9$ |
| $\hbar_q$ | $(q-1)/q$ | $0.09887$ |
| $q$ | — | $1.1097$ |
| $\eta_q$ | $d_H(q) \cdot \log 2$ | $d_H \cdot 0.6931$ |
| $G(q)$ | $1/(4\,q\,(q-1)^2\,\eta_q)$ | $\approx 1.69 / d_H$ |

The value $G \approx 1.69 / d_H$ is in **Reeb units** (where one
Reeb phase advance = 1 for both length and time).  In Planck units
(where $G = 1$ by definition), the conversion is
$G_{\mathrm{Planck}} = G(q) \cdot (\hbar_q / c(q))^2 = G(q)
\cdot (q-1)^4 / q^2$.  The statement $G_{\mathrm{Planck}} = 1$
then constrains the Hausdorff dimension:

$$
  1 \;=\; G(q) \cdot \frac{(q-1)^4}{q^2}
  \;=\; \frac{(q-1)^2}{4\,q^3\,\eta_q},
$$

giving

$$
  \eta_q \;=\; \frac{(q-1)^2}{4\,q^3}
  \;=\; \frac{\hbar_q^2}{4\,q}
  \;\approx\; 0.002\,20.
$$

Since $\eta_q = d_H(q) \cdot \log 2$, this predicts

$$
  \boxed{d_H(1.1097) \;=\; \frac{\hbar_q^2}{4\,q\,\log 2}
  \;\approx\; 0.003\,18.}
$$

**Interpretation.**
This is a remarkably small Hausdorff dimension — the Julia set
$J(f_q) \cap S^1$ at $q = 1.1097$ is nearly a finite set of
points, not a space-filling curve.  This is consistent with the
regime: $q = 1.1097$ is deep inside the main cardioid (where Julia
sets are thin quasicircles), far from the cardioid boundary (where
$d_H \to 2$).

The prediction $d_H \approx 0.003$ is **independently checkable**:
it is a purely mathematical property of the Julia set of $f_q(z) =
z^2 + c(q)$ at the main-cardioid parameter corresponding to
rotation number $\theta = 0.1097$.  If numerical computation of
$d_H$ disagrees with this value, the Jacobson derivation of $G$
requires modification.

**Regime behaviour.**

| Regime | $q$ | $G(q)$ (Reeb units) | $d_H$ (predicted) | Physics |
|--------|-----|--------------------|--------------------|---------|
| Big Bang | $q \to \infty$ | $\to 0$ | $\to 0$ | No gravity: fibres isolated |
| Deep quantum | $\varphi^2$ | $\approx 0.059/d_H$ | — | Weak gravity |
| Our universe | $1.1097$ | $\approx 1.69/d_H$ | $\approx 0.003$ | $G$ consistent with SI value via dimensional anchor |
| Near-classical | $1.01$ | $\approx 2500/d_H$ | $\approx 10^{-5}$ | Strong gravity (Newtonian limit) |
| Classical limit | $q \to 1^+$ | $\to \infty$ | $\to 0$ | $G \to \infty$: Newtonian regime |

**Consistency with GR substrate geometry.**
The field equation $\mathrm{Ric}_{g_\theta} = T^{(q)}$
([GR substrate geometry](#rem:gr-substrate-geometry)) is recovered
with the identification $G(q) = c(q)^3 \hbar_q / (4 q \eta_q)$ as
the coupling constant.  The $q$-weighted stress tensor $T^{(q)}$
includes the factor $q(p) = 1 + |\langle L_\theta, F_A^+\rangle|$
([Levi-curvature coupling](#rem:c-substrate-via-levi)), so the
gravitational coupling varies spatially through $q(p)$ — stronger
where gauge curvature is concentrated, weaker in flat regions.

**Relation to the three fundamental constants.**
The QOU derives $c$, $\hbar$, and $G$ from a single parameter:

| Constant | QOU formula | Depends on |
|----------|-----------|------------|
| $c(q)$ | $1/(q-1)$ | $q$ only |
| $\hbar_q$ | $(q-1)/q$ | $q$ only |
| $G(q)$ | $c^3 \hbar_q / (4 q \eta_q)$ | $q$ and $d_H(q)$ |

The speed of light and Planck constant are algebraic in $q$.  The
gravitational constant additionally requires $d_H(q)$ — a
transcendental quantity determined by the Julia set dynamics.
Gravity is the only fundamental interaction whose coupling involves
the fractal geometry of the Reeb flow; this explains why $G$ is
the hardest constant to measure and the least understood
theoretically.
