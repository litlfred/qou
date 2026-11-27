# Pre-Registration: Bach et al. (2013) Double-Slit Wall-Grazing $q_{\mathrm{local}}(y)$ Aperture Integral & Retirement of Un-Derived $q = 1.020$ (2026-11-23)

Bean `qou-x9tm`. Written and committed **before** running the 80-dps aperture-averaged wall-grazing evaluation.

## 1. Anti-Fit Motivation (`NO FITTING, EXCEPT CAL-1/2/3`)

`folio/quantum-observable-universe/observations/double-slit-analytical.md` previously described its default overlay on the $600\;\mathrm{eV}$ electron diffraction data of Roger Bach, Damian Pope, Sy-Hwang Liou & Herman Batelaan (*New J. Phys.* 15, 033018, 2013) as "$q$-deformed prediction ($q = 1.020$)". Because $q = 1.020$ is neither $q_0 = 1.10997858\dots$ nor derived from CAL-1/2/3, presenting it as a QOU prediction violates the strict three-calibration anti-fit rule.

Instead, under QOU's local substrate-$q$ principle (`prop:local-substrate-q`, `proton-gravity-tests-intro.md`), $q_{\mathrm{local}}(r) \to 1$ in exterior vacuum (independently required by the $3.42\;\mathrm{dex}$ ${}^{238}\mathrm{U}$ $\alpha$-tunneling discriminator) and deviates from $1$ across an open slit of width $a$ only through the evanescent Yukawa / Compton tails of the two slit walls at $y = \pm a/2$.

## 2. Pre-Registered Exact Aperture Integral (`workdps = 80`, `q0Anchor = "proton"`)

For a slit aperture $y \in [-a/2, +a/2]$ bounded by dense gold-coated silicon walls at $y = \pm a/2$ with wall boundary shift $\Delta q_{\mathrm{wall}}$ and evanescent decay length $\ell$:

$$
q_{\mathrm{local}}(y) - 1 = \Delta q_{\mathrm{wall}} \Bigl(e^{-(a/2 - y)/\ell} + e^{-(a/2 + y)/\ell}\Bigr) = 2\,\Delta q_{\mathrm{wall}}\,e^{-a/(2\ell)}\cosh(y/\ell).
$$

The exact analytical aperture average of $q_{\mathrm{local}}(y) - 1$ and of the Hodge envelope factor $q_{\mathrm{local}}(y)^2 - 1$ over $y \in [-a/2, +a/2]$ are:

$$
\langle q_{\mathrm{local}} - 1 \rangle_a
= \frac{1}{a}\int_{-a/2}^{+a/2} \bigl(q_{\mathrm{local}}(y) - 1\bigr)\,dy
= \Delta q_{\mathrm{wall}}\,\frac{2\ell}{a}\bigl(1 - e^{-a/\ell}\bigr),
$$

$$
\langle q_{\mathrm{local}}^2 - 1 \rangle_a
= 2\,\langle q_{\mathrm{local}} - 1 \rangle_a
+ \Delta q_{\mathrm{wall}}^2 \left[\frac{\ell}{a}\bigl(1 - e^{-2a/\ell}\bigr) + 2\,e^{-a/\ell}\right].
$$

We pre-register and evaluate at 80 working dps (`OUT_DPS = 50`, zero `float64`, Form-B $\alpha_q$):
1. **Slit widths:** $a = 50\;\mathrm{nm}$ (simulator default view in `double-slit-analytical.{ts,md}`) and $a = 62\;\mathrm{nm}$ (published Bach et al. 2013 physical slit width, with $d = 272\;\mathrm{nm}$, $L = 0.24\;\mathrm{m}$, $K = 600\;\mathrm{eV}$).
2. **Evanescent Compton/Yukawa decay lengths $\ell$ (strictly CAL-1 & CAL-3):**
   - **L1 (Hadronic Yukawa / CAL-3 pion reduced Compton length):** $r_\pi = \hbar c / m_{\pi^\pm}$ ($m_{\pi^\pm} = 139.57039\;\mathrm{MeV}$, $r_\pi \approx 1.41382\;\mathrm{fm}$).
   - **L2 (Electronic CAL-1 reduced Compton length):** $\bar{\lambda}_{C,e} = \hbar c / m_e \approx 386.159\;\mathrm{fm}$ (alongside full Compton wavelength $\lambda_{C,e} = 2\pi\bar{\lambda}_{C,e} \approx 2426.31\;\mathrm{fm}$).
3. **Wall boundary amplitudes $\Delta q_{\mathrm{wall}}$ (zero fitted parameters):**
   - **W1 (Saturating core upper bound):** $\Delta q_{\max} = q_0 - 1 \approx 0.10997858\dots$ (rigorous upper bound assuming wall surfaces saturate the full hadronic core shift $q_0 - 1$).
   - **W2 (Electroweak/EM vertex-projected wall amplitude, `w-boson-mass-discrepancy.md`):** $\Delta q_{\mathrm{EM}} = (q_0 - 1)\,\frac{\alpha_q}{2\pi}\,\frac{1}{|\chi(\Sigma_4)|}$ with $|\chi(\Sigma_4)| = 6$ and Form-B $\alpha_q$.
4. **Cross-check:** Verify the analytical aperture integrals against 80-dps `mpmath.quad` Gauss–Legendre quadrature on $[-a/2, +a/2]$ (using change of variables $u = (a/2 - y)/\ell$ so boundary layers of width $\sim 10^{-8} a$ are resolved to $< 10^{-70}$!).
5. **Honest reporting:** Report the exact predicted fractional Young fringe shift $\delta \Delta y / \Delta y = \langle q_{\mathrm{local}} - 1 \rangle_a$ and Hodge single-slit envelope shift $\langle q_{\mathrm{local}}^2 - 1 \rangle_a$, quantifying by how many orders of magnitude every parameter-free regime lies below the retired $q - 1 = 2 \times 10^{-2}$ slider value.
