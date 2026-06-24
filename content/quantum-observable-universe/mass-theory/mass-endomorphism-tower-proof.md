The Hecke mass element $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def\:hecke-mass-element)) decomposes via the
:refterm[descent]{#descent} involution into descended and transient contributions.  The
transient trace localises to blow-up centres $p$ in the brane tower
([topological decomposition](#thm\:topological-mass)); integrating the
$q$-deformed expansion flow $\ln_q(1+t)/t$ along the radial
coordinate of the Briggs--Klein chart
([Briggs--Klein chart](#def\:briggs-klein-chart)) over each resolved
defect $E_i \cong \mathbb{P}^1(\mathbb{C})$ yields the symmetric
q-dilogarithm:

$$
  \int_0^{V} \frac{\ln_q(1+t)}{t}\,dt
  \;=\; -\mathrm{Li}_2^q(-V),
  \qquad
  \mathrm{Li}_2^q(z) := \sum_{n \geq 1} \frac{z^n}{n \cdot [n]_q},
$$

*where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the symmetric
q-integer.*

*Subproof.*  The q-deformed natural log has Taylor series
$\ln_q(1-z) = -\sum_{n\geq 1} z^n/[n]_q$ (\[definition of q-log]).
Termwise differentiation of $\mathrm{Li}_2^q$ gives\*

$$
  \frac{d}{dz}\mathrm{Li}_2^q(z)
  = \sum_{n \geq 1} \frac{z^{n-1}}{[n]_q}
  = -\frac{\ln_q(1-z)}{z}.
$$

*Integrating from $0$ to $z$ (with $\mathrm{Li}_2^q(0) = 0$):
$\mathrm{Li}_2^q(z) = -\int_0^z (\ln_q(1-u)/u)\,du$.  Substituting
$u = -t$, $z = -V$:*

$$
  \mathrm{Li}_2^q(-V)
  = -\int_0^{-V}\!\frac{\ln_q(1-u)}{u}du
  = -\int_0^{V}\!\frac{\ln_q(1+t)}{t}dt
$$

*so $\int_0^V (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$.  $
$\qquad\blacksquare$
