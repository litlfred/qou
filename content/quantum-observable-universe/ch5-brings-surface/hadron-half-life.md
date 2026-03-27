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
  [2]_q
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
   is determined by the Markov trace ratio between parent and
   daughter Gröbner normal forms
   ([trace ratio observable](#prop:trace-ratio-observable)):

   $$
     |\mathcal{M}_q|^2
     \;\propto\;
     \prod_{i=0}^{p}
     \left|
       \frac{\hat{V}_i^{\,\mathrm{par}}}{\hat{V}_i^{\,\mathrm{dau}}}
     \right|^2
   $$

   where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced
   generator volume
   ([factorization theorem](#thm:markov-trace-factorization)).

3. **Phase-space integral**: The $Q$-value
   $Q_\beta = M(\text{parent}) - M(\text{daughter}) - m_e$
   is the mass difference between parent and daughter atoms.
   The mass of each nucleus is determined by the terminal
   resolution of its composite link
   ([terminal resolution](#prop:terminal-resolution)),
   evaluated at $q$ using the pair Skein mass formula
   $\mathcal{S}_{ab}(q) = (q\,\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$.
   The fifth-power Sargent rule gives $f(Q_\beta) \propto Q_\beta^5$
   for allowed transitions.

**$q$-dependence of the decay rate.**
The decay rate depends on $q$ through three channels:

- $[2]_q = q + q^{-1}$: the weak-vertex dimension.
- $|\mathcal{M}_q|^2$: the Markov trace ratio, which depends on
  the crossing structure of the nuclear braid at $q$.
- $Q_\beta^5$: the mass difference, determined by the pair Skein
  weights $\mathcal{S}_{ab}(q)$ which depend on $q$ through the
  dressed quark masses $\mu_u, \mu_d$.

At $q = 1$ (classical limit): $[2]_1 = 2$, the crossing asymmetry
vanishes, all isobars are degenerate ($Q = 0$), and no beta decay
occurs.  At $q > 1$: the crossing asymmetry splits the isobars,
producing nonzero $Q$ and finite half-lives.

The sensitivity of the decay rate to $q$ is

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  \;=\;
  \frac{q^2 - 1}{q^2 + 1}
  \;+\;
  5\,\frac{q^2 + 1}{q^2 - 1}
  \;\approx\; 48
  \quad\text{at } q = 1.110.
$$

A $1\%$ shift in $q$ changes decay rates by $\sim 50\%$.

The half-life is *not* a new observable — it is derived from the
categorical action $\mathcal{S}_q$ evaluated on the nuclear link,
using the same parameter $q$ that determines the valley of
stability.  The parameter $q$ controls both *which* nuclei are
stable and *how fast* unstable nuclei decay.
