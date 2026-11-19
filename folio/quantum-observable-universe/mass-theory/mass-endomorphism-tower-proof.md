*Proof.*
The Hecke mass element $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)) decomposes via the
:refterm[descent]{#descent} involution into descended and transient contributions.  The
transient trace localises to blow-up centres $p$ in the brane tower
([topological decomposition](#thm:topological-mass)); integrating the
$q$-deformed expansion flow $\ln_q(1+t)/t$ along the radial
coordinate of the Briggs--Klein chart
([Briggs--Klein chart](#def:briggs-klein-chart)) over each resolved
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

*so $\int_0^V (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$.  $\square_{\text{sub}}$*

*canonical structural verification: the integration value matches
$-\mathrm{Li}_2^q(-V)$ to all displayed digits at $q_0 \approx 1.110$
for $V \in \{0.1, 0.3, 0.5, 0.7, 0.85, 0.95, 0.989\}$.*

*The integral is not the compact quantum dilogarithm
$\Phi_q(V) = \prod_{k\geq 1}(1 - q^{-k}V)^{-1}$, whose logarithm uses
asymmetric q-integers $(q^n - 1)$.  Both $\mathrm{Li}_2^q$ and
$\log\Phi_q$ are q-deformations of the classical dilogarithm, but they
use different q-integer conventions; the Hecke setting requires the
symmetric form $[n]_q$, so $\mathrm{Li}_2^q$ is the correct
identification.*

The NF basis of $H_n(R, q)$ decomposes by generator content.  Each
subset $S \subseteq \{0,\dots,n-2\}$ contributes a blow-up centre
with spectral coordinate $\prod_{i\in S}\hat{V}_i$ and Markov
weight $z^{|S|}$; triples and higher generator subsets are not
independent at level $n$ (they ascend to jet level $n+1$ via the
pentagon closure of $\Phi_q$, see
[quantum Bloch group](#def:quantum-bloch-group)).  The independent
order-1 and order-2 subsets enumerate exactly the singleton and
pair sums above.

For the adjacent pair $\{i, i+1\}$ the NF elements
$\sigma_i\sigma_{i+1}$ and $\sigma_{i+1}\sigma_i$ share the same
spectral support $\hat{V}_i\hat{V}_{i+1}$ (the same blow-up centre,
distinct elements of $H_n(R, q)$ modulo Yang--Baxter); their combined
weight is $z^2$, not $2z^2$.  For a non-adjacent pair
$\{i, j\}$ with $\lvert i-j\rvert\geq 2$ far-commutativity gives
$\sigma_i\sigma_j = \sigma_j\sigma_i$ and
$\mathrm{tr}_M(\sigma_i\sigma_j) = z \cdot z = z^2$ — a single NF
element supporting a single blow-up centre.  In every case the
combined pair weight is $z^2$.  Summing over all pairs $i<j$ gives
the claimed quadratic term.

The element $\sigma_0\sigma_1\sigma_0$ is not an independent blow-up
centre: it decomposes as $\sigma_1\sigma_0\sigma_1$ via Yang--Baxter,
the same transient support as the adjacent pair.  Higher-order
subsets of size $\geq 3$ are similarly subsumed — not into level-$n$
singletons and pairs, but into the level-$(n{+}1)$ jet contribution
via the pentagon identity of the quantum dilogarithm (for the
explicit ascension see [jet-tower reformulation](#rem:mass-endomorphism-jet-tower)).
$\square$
