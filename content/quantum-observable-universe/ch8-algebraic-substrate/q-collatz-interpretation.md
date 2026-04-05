The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
places the Collatz problem inside the paper's universal
obstruction framework as a **fifth evaluation** of the Euler
class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$.

### Five evaluations of $\kappa_0$

The one-dimensionality of $HH^2(\mathrm{Ad}) \cong k$
([QOU obstruction reduction](#thm:qou-obstruction-reduction))
means every obstruction in the paper is a scalar multiple
$c \cdot \chi(A)$, where $c$ is determined by the
restriction map to the relevant sub-locus of $\mathcal{S}$:

| Evaluation | Locus $\mathcal{S}_\bullet$ | $c$ | Classical shadow |
|------------|---------------------------|-----|-----------------|
| Spectral | $\mathrm{Spec}(\xi_q)$ | $\neq 0$ | Riemann Hypothesis |
| Collision | $\Sigma$ (vortex collision) | $\neq 0$ | NS regularity |
| Elliptic | $\mathcal{E}_q$ (Descartes curve) | $\neq 0$ | Birch--Swinnerton-Dyer |
| Computational | $\mathcal{R}(L)$ (resolution tree) | $\neq 0$ | P $\neq$ NP |
| **Collatz** | $\mathcal{S}_{C_q}$ (iteration locus) | $= 0$ (conj.) | **Collatz conjecture** |

The first four evaluations have $c \neq 0$: the obstruction
persists through $q \to 1$ and the classical problem is
genuinely hard.  The Collatz evaluation is conjectured to
have $c_C = 0$ — a qualitatively different situation.

### Why $c_C = 0$: contractibility of the iteration locus

The mechanism proposed in the conjecture is **geometric
triviality** of $\mathcal{S}_{C_q}$.  The Hecke--Collatz
endomorphism $C_q$ traces orbits in $A$ that are confined
to a one-dimensional sub-bundle of the state bundle
$\mathcal{S}$, because:

1. **Torsion avoidance** ($q \notin \mu_\infty$): the mass
   gap $\Delta_q > 0$
   ([Gm torsion](#rem:substrate-gm-torsion)) ensures the
   Hecke channels $e_\pm(\xi_q)$ are spectrally separated.
   The orbit cannot stagnate at the boundary between channels.

2. **Reeb periodicity** ($\xi_q^{\Omega_q} = \mathrm{id}_A$):
   the finite period forces the orbit to sample both branches
   over each Reeb cycle.  The contractive rate
   $[2]_q^{-1} < 1/2$ (since $[2]_q = q + q^{-1} > 2$ for
   $q > 1$) dominates the expansive rate $[3]_q$, giving a
   net contraction $\lambda_q = [2]_q^{-1} \cdot [3]_q < 1$
   per period.

3. **Observability** (Tannaka--Krein, semisimple $G$):
   the decomposition $A \cong \bigoplus_\rho V_\rho^{\oplus m_\rho}$
   ([TK isomorphism](#thm:tannaka-krein-isomorphism)) ensures
   $C_q$ acts irreducibly on each isotypic component.  The
   iteration locus lies within a single component — it does
   not "spread" across the full state bundle.

The upshot: $\mathcal{S}_{C_q}$ is homotopy-equivalent to a
point (contractible), so
$H^2(\mathcal{S}_{C_q}, \mathbb{G}_m) = 0$ and the
restriction map kills $\kappa_0$ regardless of $\chi(A)$.

This contrasts with the NS collision locus $\Sigma$ or the
skein resolution tree $\mathcal{R}(L)$, which are
topologically non-trivial (higher-genus surfaces, exponentially
branching trees) and carry non-vanishing $H^2$.

### Contrast with the other four: why Collatz is easier

The four hard problems share a feature: their loci carry
**non-trivial topology** that supports a non-zero
restriction of $\kappa_0$.  The Kummer filtration
([root-of-unity truncation](#prop:root-of-unity-truncation))
then controls which torsion levels obstruct:

$$
  \kappa_\bullet \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A) = -6.
$$

The obstruction persists at all levels $n \nmid 6$
(density $1$ in the Kummer tower).

For Collatz, the contractibility of $\mathcal{S}_{C_q}$
means $\kappa_C = 0$ at **every** Kummer level — not by
divisibility of $\chi(A)$ but by the vanishing of the
target group.  The Collatz conjecture, in the QOU
framework, is not a sibling of the millennium problems
but a qualitatively simpler problem that happens to be
hard classically because the $q \to 1$ degeneration
destroys the contractibility (the Hecke channels merge,
the smooth interpolation becomes a hard parity switch,
and the iteration locus acquires non-trivial topology).

### Information-theoretic bound

Each Collatz step generates operational entropy
$\eta_q = (2q-1)/q^3$
([operational entropy](#def:operational-entropy)) per Reeb
circuit.  The total information processed by a $q$-Collatz
orbit of stopping time $\sigma_q(a)$ is:

$$
  I_C(a, q)
  \;=\;
  \sigma_q(a) \cdot \eta_q
  \;=\;
  \sigma_q(a) \cdot \frac{2q-1}{q^3}
  \quad\text{nats}.
$$

The convergence conjecture ($\kappa_C = 0$) is equivalent to
$I_C(a, q) < \infty$ for all $a$ — every orbit processes
finitely many nats.  The per-step rate is bounded by the
Planck bandwidth
([bandwidth bound](#prop:p-bandwidth-bound)):

$$
  \frac{I_C(a,q)}{t_P \cdot \sigma_q(a)}
  \;=\;
  \frac{\eta_q}{\hbar_q}
  \;=\;
  \frac{(2q-1)}{q^2(q-1)}
  \;\leq\;
  \mathcal{B}(q).
$$

Each step fits within the Planck-scale computation budget.
Convergence means the total computation is finite — the
orbit is an **information-bounded process** on the substrate.

### Stopping-time zeta function

The stopping-time distribution is encoded by a Dirichlet
series ([local $q$-zeta](#def:local-q-zeta-function)):

$$
  Z_C(s, q)
  \;=\;
  \sum_{a \in A^+} \sigma_q(a)\,\|a\|^{-s},
$$

where $\sigma_q(a)$ counts Reeb circuits to convergence.
The Reeb flow bridge
([bridge](#rem:reeb-flow-bridge)) identifies $C_q$-periodic
orbits with closed Reeb trajectories — prime ideals of
the substrate.  If the
[$q$-Riemann hypothesis](#conj:classical-riemann-hypothesis)
holds, stopping times are equidistributed modulo the
$[2]_q$-adic valuation and $Z_C(s, q)$ admits analytic
continuation to $\mathrm{Re}(s) > 1/2$.
