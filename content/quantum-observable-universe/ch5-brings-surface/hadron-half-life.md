A nucleus displaced from the valley of stability
([integer stability](#prop:integer-stability)) undergoes beta decay
toward the stable configuration.  The **half-life** — the time for
half of a population to decay — is controlled by the substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter))
through the $q$-deformed transition amplitude.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate
parameter the substrate $q$.  A nucleus $\mathcal{N}(Z, N)$
([stable nucleus](#def:stable-nucleus)) with proton displacement
$\delta p = p - p_{\mathrm{stab}}(A)$ from the valley of stability
has beta-decay half-life

$$
  t_{1/2}(p, A)
  \;=\;
  \frac{\ln 2}{\Gamma_\beta(p, A)}
$$

where the decay rate $\Gamma_\beta$ depends on $q$ and the single
dimensional scale $\mu_0$ ([building blocks](#rem:building-block-knots)).

## Decay rate from $q$ and $\mu_0$

Beta decay is a Skein crossing change
([beta decay as crossing change](#def:beta-decay-skein)) —
there is no separate weak boson.  The fundamental weak coupling
is the **Skein amplitude** $s = q^{1/2} - q^{-1/2}$, which is
the coefficient of the resolved link $L_0$ in the Skein relation.

The decay rate is:

$$
  \Gamma_\beta(p, A)
  \;=\;
  \frac{s^2 \cdot \mu_0}{2\pi^3}
  \;\cdot\;
  [2]_q
  \;\cdot\;
  |\mathcal{M}_q|^2
  \;\cdot\;
  f(\mathcal{Q}_q)
$$

where every factor is determined by $q$:

1. **Skein amplitude** $s^2 = (q^{1/2} - q^{-1/2})^2$: the weak
   vertex coupling.  This is the square of the coefficient in the
   Skein relation $q\,L_+ - q^{-1}L_- = s\,L_0$.  In the classical
   limit $q \to 1$, $s \to 0$ and beta decay shuts off.

2. **$q$-integer modulation** $[2]_q = q + q^{-1}$: the categorical
   dimension of the $\mathrm{SU}_q(2)$ fundamental representation,
   replacing the classical factor of $2$ in the weak-interaction
   vertex.

3. **$q$-deformed matrix element**: The squared matrix element
   is the Markov trace ratio between parent and daughter Gröbner
   normal forms
   ([trace ratio observable](#prop:trace-ratio-observable)):

   $$
     |\mathcal{M}_q|^2
     \;=\;
     s^2
     \;\cdot\;
     \prod_{i=0}^{p}
     \left|
       \frac{\hat{V}_i^{\,\mathrm{par}}}{\hat{V}_i^{\,\mathrm{dau}}}
     \right|^2
   $$

   where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced
   generator volume
   ([factorization theorem](#thm:markov-trace-factorization)).

4. **Phase-space integral**: The $\mathcal{Q}_q$-value
   ([transition energy](#def:q-value-transition)) is the
   categorical action difference
   $\mathcal{Q}_q = S_q(\mathrm{par}) - S_q(\mathrm{dau}) - S_q(e)$.
   This is **not** defined by classical energy conservation
   ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$), which assumes
   $d_q^2 = 0$ and fails at $q \neq 1$.  The action of each
   nucleus is determined by the terminal resolution of its
   composite link
   ([terminal resolution](#prop:terminal-resolution)),
   evaluated at $q$ using the pair Skein mass formula
   $\mathcal{S}_{ab}(q) = (q\,\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$.
   The fifth-power Sargent rule gives $f(\mathcal{Q}_q) \propto \mathcal{Q}_q^5$
   for allowed transitions.

5. **Dimensional scale** $\mu_0$: the single free parameter,
   which converts Skein units to physical units (MeV, seconds).
   This is a unit choice, not a physical parameter.

## Relation to the Fermi constant

The standard Fermi theory writes the decay rate as
$\Gamma = G_F^2\,m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$.
This effective-theory formula packages together two mass scales:

- the **electron mass** $m_e = 3\,\mathfrak{E}_{\times}(q) \cdot \mu_0$
  ([building blocks](#rem:building-block-knots)), where
  $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy;
- the **weak scale** $v \approx 246$ GeV, via $G_F = 1/(\sqrt{2}\,v^2)$.

Both mass scales are determined by $q$ and the single dimensional
unit $\mu_0$, but they arise from **different knot structures**:
$m_e$ from the trefoil's 3 crossings, $v$ from the knot topology
of the electroweak sector.  The ratio $v / m_e \approx 4.8 \times 10^5$
is a pure number that the topology must determine.

The combination that enters the half-life is:

$$
  G_F^2\,m_e^5
  \;=\;
  \frac{m_e^5}{2\,v^4}
  \;=\;
  \frac{(3\,\mathfrak{E}_{\times})^5}{2\,(N_v\,\mathfrak{E}_{\times})^4}
  \;\cdot\; \mu_0
  \;=\;
  \frac{243\,\mathfrak{E}_{\times}}{2\,N_v^4}
  \;\cdot\; \mu_0
$$

where $N_v = v / (\mathfrak{E}_{\times}\,\mu_0)$ is the effective crossing
count of the weak scale.  This is a pure function of $q$ times
$\mu_0$ — the Fermi constant is not an independent parameter.

**Open computation:** Deriving $N_v$ (equivalently, the weak
scale $v$) from the Skein algebra.  In the QOU there is no
separate W boson — the weak interaction is a Skein crossing
change — so $v$ must emerge from the brane tower structure
at the electroweak level.  The Skein amplitude
$s = q^{1/2} - q^{-1/2}$ is the coupling; the mass scale $v$
determines the range.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $s^2 = (q^{1/2} - q^{-1/2})^2$: the weak vertex coupling.
- $[2]_q = q + q^{-1}$: the weak-vertex dimension.
- $|\mathcal{M}_q|^2$: the Markov trace ratio, which depends on
  the crossing structure of the nuclear braid at $q$.
- $\mathcal{Q}_q^5$: the categorical action difference
  ([transition energy](#def:q-value-transition)), determined by
  the pair Skein weights $\mathcal{S}_{ab}(q)$ which depend on $q$
  through the dressed quark masses $\mu_u, \mu_d$.  Note:
  $\mathcal{Q}_q \neq T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}}$
  at $q \neq 1$ (the $q$-anomaly $\delta_q \neq 0$).

At $q = 1$ (classical limit): $s = 0$, $[2]_1 = 2$, the crossing
asymmetry vanishes, all isobars are degenerate
($\mathcal{Q}_q = 0$), and no beta decay occurs.  At $q > 1$:
the crossing asymmetry splits the isobars, producing nonzero
$\mathcal{Q}_q$ and finite half-lives.

The sensitivity of the decay rate to $q$ is

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  \;=\;
  \frac{q^2 - 1}{q^2 + 1}
  \;+\;
  5\,\frac{q^2 + 1}{q^2 - 1}
  \;\approx\; 48
  \quad\text{at } q = q_0.
$$

A $1\%$ shift in $q$ changes decay rates by $\sim 50\%$.

The half-life is *not* a new observable — it is derived from the
categorical action $\mathcal{S}_q$ evaluated on the nuclear link,
using the same parameter $q$ that determines the valley of
stability.  The parameter $q$ controls both *which* nuclei are
stable and *how fast* unstable nuclei decay.

## Parameter count

The half-life formula uses:
- the substrate $q$ — the substrate parameter (fixed by the muon-electron
  mass ratio),
- $\mu_0$ — the dimensional scale (unit choice: MeV, seconds, etc.),
- $(p, n)$ — the nuclear quantum numbers.

Every standard-physics constant decomposes into $q$-dependent
factors times $\mu_0$: the electron mass
$m_e = 3\,\mathfrak{E}_{\times}\,\mu_0$, the weak scale
$v = N_v\,\mathfrak{E}_{\times}\,\mu_0$, and the fine structure constant
$\alpha = q^{-1}/([9]_q \cdot [10]_q)$
([EM coupling projection](#prop:em-coupling-projection)).
The fine structure constant is now fully derived from $q$ alone
(0.14% from CODATA).  The weak scale crossing count $N_v$ remains
open (see [verification](#ex:hadron-half-life-verification)).
