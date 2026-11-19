*Interpretation of the [one-dimensional channel](#def:one-dim-qou-channel).*

A photon is represented on a fibre by a strand $\gamma$ that is knot-trivial under Markov closure, advancing without topological crossings along an $n$-strand channel. A bounded channel of $n$ strands supports $n$ discrete propagating modes, providing a topological counterpart to waveguide mode quantization in a step-index optical fibre.

Propagation is referenced to the [information speed of light](#def:information-speed-of-light) $c_q = 1/(q - 1)$. Expressing mode propagation in terms of the symmetric $q$-phase requires a **dimensionless** argument: a photon of physical energy $\mathfrak{E}_\gamma = \hbar c\,k$ on a channel with ultraviolet cutoff energy $\mathfrak{E}_*$ enters through the dimensionless energy ratio $x = \mathfrak{E}_\gamma / \mathfrak{E}_*$ (substituting an unscaled integer $x = m \in \{1, 2, \dots\}$ evaluates ultraviolet cutoff excitations $\mathfrak{E}_\gamma = m\,\mathfrak{E}_*$ rather than infrared photons $x \ll 1$). For $q > 1$, the bar-even symmetric $q$-phase is
$$
  \phi_q(x)
  \;=\;
  \frac{q^x - q^{-x}}{q - q^{-1}}
  \;=\;
  \frac{\sinh(x \ln q)}{\sinh(\ln q)},
$$
satisfying exact bar-invariance $\phi_{q^{-1}}(x) = \phi_q(x)$ and oddness $\phi_q(-x) = -\phi_q(x)$. Differentiating $c_q\,\phi_q(x)$ with respect to $x$ yields the exact mode group velocity
$$
  v_g(\mathfrak{E}_\gamma)
  \;=\;
  c_q\,\frac{d\phi_q}{dx}\!\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\right)
  \;=\;
  c_{\mathrm{phys}}(q)\,\cosh\!\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\ln q\right),
  \qquad
  c_{\mathrm{phys}}(q) \;:=\; c_q\,\frac{\ln q}{\sinh(\ln q)}.
$$

Two structural consequences govern sub-cutoff propagation:

1. **Zero infrared $O(\hbar_q)$ dispersion:** As $\mathfrak{E}_\gamma / \mathfrak{E}_* \to 0$, every mode shares the single frequency-independent speed of light $v_g(0) = c_{\mathrm{phys}}(q)$ (at $q_0 \approx 1.1100$, the bar-even factor $\frac{\ln q_0}{\sinh(\ln q_0)} \approx 0.998188$ renormalizes $c_q$ uniformly across all low-energy frequencies without inducing dispersion).
2. **Identical vanishing of linear ($n = 1$) dispersion and quadratic bound:** Because $v_g(\mathfrak{E}_\gamma)$ is even in $\mathfrak{E}_\gamma$, its first energy derivative vanishes identically at zero energy, $\left.\frac{dv_g}{d\mathfrak{E}_\gamma}\right|_{\mathfrak{E}_\gamma = 0} = 0$. Whenever $\bigl|\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\ln q\bigr| \le 1$, the fractional group-velocity shift is strictly non-negative and purely quadratic at leading order:
$$
  0
  \;\le\;
  \frac{v_g(\mathfrak{E}_\gamma) - c_{\mathrm{phys}}(q)}{c_{\mathrm{phys}}(q)}
  \;=\;
  \cosh\!\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\ln q\right) - 1
  \;=\;
  \frac{1}{2}(\ln q)^2\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\right)^2
  + O\!\left(\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\right)^4\right)
  \;\le\;
  \frac{\cosh 1}{2}\left(\frac{\mathfrak{E}_\gamma}{\mathfrak{E}_*}\ln q\right)^2.
$$
