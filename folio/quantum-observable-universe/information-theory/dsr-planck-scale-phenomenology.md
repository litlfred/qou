*Interpretation of the [information speed of light](#def:information-speed-of-light).*

The aether light speed $c_q = 1/(q - 1)$ and the symmetric bar-even dispersion relation $v_g(\mathfrak{E}_\gamma) = c_{\mathrm{phys}}(q)\,\cosh\!\bigl(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\ln q\bigr)$ on a [one-dimensional channel](#def:one-dim-qou-channel) ([photon modes](#rem:photon-propagation-1d)) connect directly to doubly special relativity (DSR) and Planck-scale time-of-flight phenomenology \cite{amelinocamelia1998,amelinocamelia2001,amelinocamelia2013}.

**Comparison with doubly special relativity and observer covariance at fixed $q_0 \neq 1$.**
Amelino-Camelia's minimum-length framework \cite{amelinocamelia2001} introduces an observer-independent ultraviolet scale $\mathfrak{E}_{\mathrm{QG}}$ alongside the low-energy speed of light, realised in $\kappa$-Poincaré models by first-order ($n = 1$) energy modifications of the dispersion relation. Two structural features distinguish the bar-even categorical formulation:

1. **Frame-independent $q_0 \neq 1$ without taking $q \to 1$:** Sending $q \to 1$ collapses $\hbar_q = 1 - q^{-1} \to 0$ (the classical $\hbar \to 0$ limit). Inertial boost covariance holds directly at fixed $q_0 \neq 1$ through the state-covariant transformation $(\tau, \xi_\tau) \mapsto (\tau \circ \Lambda^{-1},\; \Lambda \circ \xi_\tau \circ \Lambda^{-1})$, so $q_0$ enters as a Lorentz-invariant dimensionless modulus rather than a preferred-frame parameter.
2. **Exact bar-parity cancellation of linear ($n = 1$) dispersion:** Because $\phi_q(x) = \frac{\sinh(x \ln q)}{\sinh(\ln q)}$ is invariant under $q \leftrightarrow q^{-1}$ and odd in $x = \mathfrak{E}_\gamma / \mathfrak{E}_*$, the factor $\frac{\ln q_0}{\sinh(\ln q_0)} \approx 0.998188$ renormalizes $c_{\mathrm{phys}}(q_0)$ uniformly across all infrared frequencies, while $\left.\frac{\partial v_g}{\partial \mathfrak{E}_\gamma}\right|_{\mathfrak{E}_\gamma = 0} = 0$ eliminates the linear ($n = 1$) dispersion channel identically.

**Astrophysical gamma-ray-burst bounds.**
Fermi-LAT time-of-flight measurements on GRB 090510 (with highest photon energy $\mathfrak{E}_\gamma \approx 31\;\mathrm{GeV}$) exclude linear ($n = 1$) vacuum dispersion $|\Delta v_g / c| \le \mathfrak{E}_\gamma / \mathfrak{E}_{\mathrm{QG},1}$ below $\mathfrak{E}_{\mathrm{QG},1} > 1.2\,E_{\mathrm{Pl}}$ ($E_{\mathrm{Pl}} \approx 1.22089 \times 10^{19}\;\mathrm{GeV}$) \cite{abdo2009}. Substituting unscaled integers $x = 1, 2$ into $[x]_q$ evaluates ultraviolet cutoff excitations $\mathfrak{E}_\gamma = \mathfrak{E}_*, 2\mathfrak{E}_*$ ($\Delta v_g / c_{\mathrm{phys}} \approx 5.45 \times 10^{-3}$ at $x = 1$) rather than astrophysical photons. Under the bar-even law, linear dispersion vanishes identically and the leading quadratic ($n = 2$) coefficient at $q_0$ is $\tfrac{1}{2}(\ln q_0)^2 \approx 5.4435 \times 10^{-3}$. At $\mathfrak{E}_* = E_{\mathrm{Pl}}$, a $31\;\mathrm{GeV}$ photon experiences a fractional velocity shift
$$
  \frac{v_g(31\;\mathrm{GeV}) - c_{\mathrm{phys}}(q_0)}{c_{\mathrm{phys}}(q_0)}
  \;=\;
  \cosh\!\left(\frac{\mathfrak{E}_\gamma}{E_{\mathrm{Pl}}}\ln q_0\right) - 1
  \;\approx\;
  3.51 \times 10^{-38},
$$
more than twenty orders of magnitude below Fermi-LAT time-of-flight sensitivity \cite{abdo2009,amelinocamelia2013}. Deriving the cutoff scale $\mathfrak{E}_* \ge E_{\mathrm{Pl}}$ from the gravitational horizon sector is the remaining open step isolated in the conjecture below.
