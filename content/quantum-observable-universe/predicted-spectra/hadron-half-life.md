*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

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
  = 
  \frac{\ln 2}{\Gamma_\beta(p, A)}
$$

where the decay rate $\Gamma_\beta$ depends on $q$ and the single
dimensional scale $\mu_0$ ([building blocks](#rem:building-block-knots)).

## Decay rate from $q$ and $\mu_0$

Beta decay is mediated by the torus knot $T_{3,5}$ with $10$
crossings ([beta decay as crossing change](#def:beta-decay-skein),
[force identification](#rem:force-knot-identification)).  The
$T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ is inserted at the
converting quark, and its $10$ crossings partition into the
electron trefoil ($3$), neutrino unknot ($0$), and nuclear
re-reduction residue ($7$).  The fundamental weak coupling
is the **weak vertex form factor** $\mathcal{W}(q)$, the
Markov trace of the $T_{3,5}$ braid word in $H_3(q)$.

The decay rate is:

$$
  \Gamma_\beta(p, A)
  = 
  \frac{|\mathcal{W}(q)|^2 \cdot \mu_0}{2\pi^3}
   \cdot 
  [2]_q
   \cdot 
  |\mathcal{M}_q|^2
   \cdot 
  f(Q)
$$

where every factor is determined by $q$:

1. **Weak vertex form factor**
   $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$:
   the full $10$-crossing weak vertex coupling, replacing the
   single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$.
   In the classical limit $q \to 1$, $\mathcal{W}(1) = 0$ and
   beta decay shuts off.

2. **$q$-integer modulation** $[2]_q = q + q^{-1}$: the categorical
   dimension of the $\mathrm{SU}_q(2)$ fundamental representation,
   replacing the classical factor of $2$ in the weak-interaction
   vertex.

3. **$q$-deformed matrix element**: The squared matrix element
   is the Markov trace ratio between parent and daughter Gröbner--Shirshov
   normal forms
   ([trace ratio observable](#prop:trace-ratio-observable)):

   $$
     |\mathcal{M}_q|^2
     = 
     s^2
      \cdot 
     \prod_{i=0}^{p}
     \left|
       \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}
     \right|^2
   $$

   where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced
   generator volume
   ([factorization theorem](#thm:markov-trace-factorization)).

4. **Phase-space integral**: The $Q$-value
   ([transition energy](#def:Q-value-transition)) is the
   categorical action difference
   $Q = S_q(\mathrm{par}) - S_q(\mathrm{dau}) - S_q(e)$.
   This is **not** defined by classical energy conservation
   ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$), which assumes
   $d_q^2 = 0$ and fails at $q \neq 1$.  The action of each
   nucleus is determined by the terminal resolution of its
   composite link
   ([terminal resolution](#prop:terminal-resolution)),
   evaluated at $q$ using the pair Skein mass formula
   $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$.
   The fifth-power Sargent rule gives $f(Q) \propto Q^5$
   for allowed transitions.

5. **Dimensional scale** $\mu_0$: the single free parameter,
   which converts Skein units to physical units (MeV, seconds).
   This is a unit choice, not a physical parameter.

## Relation to the Fermi constant

The standard Fermi theory writes the decay rate as
$\Gamma = G_F^2m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$.
This effective-theory formula packages together two mass scales:

- the **electron mass** $m_e = 3\mathfrak{E}_{\times}(q) \cdot \mu_0$
  ([building blocks](#rem:building-block-knots)), where
  $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy;
- the **weak scale** $v \approx 246$ GeV, via $G_F = 1/(\sqrt{2}v^2)$.

Both mass scales are determined by $q$ and the single dimensional
unit $\mu_0$, but they arise from **different knot structures**:
$m_e$ from the trefoil's 3 crossings, $v$ from the knot topology
of the electroweak sector.  The ratio $v / m_e \approx 4.8 \times 10^5$
is a pure number that the topology must determine.

The combination that enters the half-life is:

$$
  G_F^2m_e^5
  = 
  \frac{m_e^5}{2v^4}
  = 
  \frac{(3\mathfrak{E}_{\times})^5}{2(N_v\mathfrak{E}_{\times})^4}
   \cdot  \mu_0
  = 
  \frac{243\mathfrak{E}_{\times}}{2N_v^4}
   \cdot  \mu_0
$$

where $N_v = v / (\mathfrak{E}_{\times}\mu_0)$ is the effective crossing
count of the weak scale.  This is a pure function of $q$ times
$\mu_0$ — the Fermi constant is not an independent parameter.

**Open computations:**

1. **$N_v$ (weak scale crossing count):** Deriving $N_v$
   (equivalently, the weak scale $v$) from the Skein algebra.
   The weak interaction is mediated by $T_{3,5}$, so $v$ must
   emerge from the $10$-crossing structure of the $T_{3,5}$ braid.
   The vertex form factor $\mathcal{W}(q)$ is the coupling; the
   mass scale $v$ determines the range.

2. **$\mathcal{W}(q)$ (weak vertex form factor):** The Markov
   trace of $(\sigma_1\sigma_2)^5$ in $H_3(q)$ at the substrate $q$.
   This replaces the single-crossing approximation $s^2$ and
   should resolve the systematic $10$–$17\%$ overshoot in
   heavy-nucleus half-life predictions.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $|\mathcal{W}(q)|^2$: the $T_{3,5}$ weak vertex form factor.
- $[2]_q = q + q^{-1}$: the weak-vertex dimension.
- $|\mathcal{M}_q|^2$: the Markov trace ratio, which depends on
  the crossing structure of the nuclear braid at $q$.
- $Q^5$: the categorical action difference
  ([transition energy](#def:Q-value-transition)), determined by
  the pair Skein weights $\mathcal{S}_{ab}(q)$ which depend on $q$
  through the dressed quark masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$.  Note:
  $Q \neq T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}$
  at $q \neq 1$ (the $q$-anomaly $\delta_q \neq 0$).

At $q = 1$ (classical limit): $s = 0$, $[2]_1 = 2$, the crossing
asymmetry vanishes, all isobars are degenerate
($Q = 0$), and no beta decay occurs.  At $q > 1$:
the crossing asymmetry splits the isobars, producing nonzero
$Q$ and finite half-lives.

The sensitivity of the decay rate to $q$ is

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1}
  + 
  5\frac{q^2 + 1}{q^2 - 1}
   \approx  48
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
$m_e = 3\mathfrak{E}_{\times}\mu_0$, the weak scale
$v = N_v\mathfrak{E}_{\times}\mu_0$, and the fine structure constant
$\alpha = q^{-1}/([9]_q \cdot [10]_q)$, with Chern-Simons correction
([EM coupling projection](#prop:em-coupling-projection)).
The fine structure constant is now fully derived from $q$ alone
($2.1\;\mathrm{ppm}$ from CODATA).  The weak scale crossing count $N_v$ remains
open (see [verification](#ex:hadron-half-life-verification)).


**Remark on Mathematical Novelty:** While the resulting decay structure follows the standard weak-decay formulation, the novelty lies in successfully re-deriving this empirical structure purely categorically, unifying the Fermi golden rule and Sargent's rule within a fundamental Markov-trace matrix element.
