A nucleus displaced from the valley of stability
([integer stability](#prop:integer-stability)) undergoes beta decay
toward the stable configuration.  The **half-life** — the time for
half of a population to decay — is controlled by the substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter))
through the $q$-deformed transition amplitude.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate
parameter $q = 1.110$.  A nucleus $\mathcal{N}(p, n)$
([stable nucleus](#def:stable-nucleus)) with proton displacement
$\delta p = p - p_{\mathrm{stab}}(A)$ from the valley of stability
has beta-decay half-life

$$
  t_{1/2}(p, A)
  \;=\;
  \frac{\ln 2}{\Gamma_\beta(p, A)}
$$

where the decay rate $\Gamma_\beta$ is given by the $q$-deformed
Fermi golden rule

$$
  \Gamma_\beta(p, A)
  \;=\;
  \frac{G_F^2}{2\pi^3\hbar}
  \;\cdot\;
  [q]_2
  \;\cdot\;
  |\mathcal{M}_q|^2
  \;\cdot\;
  f(Q_\beta)
$$

with the following $q$-dependent factors:

1. **$q$-integer modulation**: $[2]_q = q + q^{-1}$ appears as the
   categorical dimension of the $\mathrm{SU}_q(2)$ fundamental
   representation, replacing the classical factor of $2$ in the
   weak-interaction vertex.

2. **$q$-deformed matrix element**: The squared matrix element
   decomposes via the Skein binding Lagrangian
   ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) as

   $$
     |\mathcal{M}_q|^2
     \;=\;
     g_V^2 \cdot \frac{q + q^{-1}}{2}
     \;+\;
     g_A^2 \cdot \frac{q - q^{-1}}{q + q^{-1}} \cdot \sigma_{\mathrm{GT}}
   $$

   where $g_V = 1$ (vector coupling, protected by CVC), $g_A \approx
   1.27$ (axial coupling), and $\sigma_{\mathrm{GT}}$ is the
   Gamow--Teller strength.  The ratio $(q - q^{-1})/(q + q^{-1}) =
   \tanh(\ln q)$ modulates the spin-flip amplitude.

3. **Phase-space integral**: The Fermi function
   $f(Q_\beta)$ depends on the $Q$-value

   $$
     Q_\beta(p, A)
     \;=\;
     \frac{\partial E}{\partial p}\bigg|_A
     \;=\;
     2\alpha(A) \cdot \delta p
     \;=\;
     2\left(\frac{a_C}{A^{1/3}} + \frac{a_A}{A}\right) \delta p
   $$

   where $\alpha(A)$ is the curvature of the binding-energy parabola
   ([integer stability](#prop:integer-stability)).  The fifth-power
   Sargent rule gives $f(Q_\beta) \propto Q_\beta^5$ for allowed
   transitions.

**Combined $q$-dependence (heavy-nucleus approximation).**
For heavy nuclei ($A \gtrsim 40$) the Coulomb curvature
$a_C / A^{1/3}$ dominates the Pauli term $a_A / A$ in $Q_\beta$,
so substituting $a_C = (q - q^{-1}) \cdot \lambda_C$ and
keeping only the leading $q$-dependent piece:

$$
  \Gamma_\beta
  \;\propto\;
  (q + q^{-1})
  \;\cdot\;
  \left[
    \frac{q + q^{-1}}{2}
    + g_A^2 \,\tanh(\ln q) \cdot \sigma_{\mathrm{GT}}
  \right]
  \;\cdot\;
  \left[
    (q - q^{-1}) \cdot \frac{\lambda_C \, \delta p}{A^{1/3}}
  \right]^5.
$$

The half-life therefore scales as

$$
  t_{1/2}
  \;\propto\;
  \frac{1}{(q + q^{-1}) \cdot (q - q^{-1})^5}
  \;\cdot\;
  \frac{A^{5/3}}{|\delta p|^5}.
$$

**Interpretation.** The decay rate factorises into a purely
$q$-dependent prefactor and a geometric factor $A^{-5/3} |\delta p|^5$
measuring displacement from the valley.  The $q$-dependent prefactor
$(q + q^{-1})(q - q^{-1})^5$ vanishes as $q \to 1$ (no beta decay in
the classical limit: Coulomb repulsion vanishes, so all isobars are
degenerate) and diverges as $q \to \infty$ (instantaneous decay: the
Coulomb splitting overwhelms the strong binding).

The half-life is *not* a new observable — it is derived from the same
Skein binding Lagrangian that determines the valley of stability.  The
parameter $q$ controls both *which* nuclei are stable (the static
valley) and *how fast* unstable nuclei decay toward it (the dynamical
half-life).
