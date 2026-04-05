**Conjecture ($q$-Collatz).**
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with
Frobenius--Hopf substrate $A$
([substrate](#def:frobenius-hopf-substrate)),
categorical Reeb derivation $\xi_q \colon A \to A$
([Reeb derivation](#def:categorical-reeb-derivation)),
and substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$
([torsion avoidance](#rem:substrate-gm-torsion)).

### The $\mathbb{G}_m$-family of Collatz operators

Over the multiplicative group scheme
$\mathbb{G}_m = \mathrm{Spec}\,\mathbb{Z}[q, q^{-1}]$,
define the **universal Hecke--Collatz endomorphism**
$C_q \in \mathrm{End}_{\mathbf{C}}(A)[q^{\pm 1}]$ by:

$$
  C_q \;=\;
  e_+(\xi_q)\,\circ\,\mu^{-1}_{[2]_q}
  \;+\;
  e_-(\xi_q)\,\circ\,\bigl(\mu_{[3]_q} + \eta\bigr),
$$

where:

- $\mu_{[k]_q} \colon A \to A$ denotes scalar multiplication by the
  $q$-integer $[k]_q = (q^k - 1)/(q - 1)$ in the Frobenius algebra,
  and $\mu^{-1}_{[2]_q}$ its inverse (well-defined since
  $q \notin \mu_\infty$ ensures $[2]_q \neq 0$);
- $\eta \colon \mathbf{1} \to A$ is the unit morphism of the
  Frobenius--Hopf algebra;
- $e_\pm(\xi_q)$ are the **Hecke idempotents** of the Reeb
  derivation, defined below.

### Hecke idempotents from the Reeb eigendecomposition

The Hecke algebra $H_1(q)$ with generator $T$ and relation
$(T - q)(T + q^{-1}) = 0$
([skein generation](#prop:skein-generation)) provides two
orthogonal idempotents:

$$
  e_+ = \frac{T + q^{-1}}{q + q^{-1}},
  \qquad
  e_- = \frac{q - T}{q + q^{-1}},
$$

satisfying $e_+ + e_- = \mathrm{id}$, $e_+^2 = e_+$,
$e_-^2 = e_-$, $e_+ e_- = 0$.

The Reeb derivation $\xi_q$ acts on $A$ with eigenvalues
determined by the weight decomposition
$A = A_H \oplus A_V$ (horizontal $\oplus$ vertical).
The Hecke--Reeb projectors are obtained by evaluating $T$
on the $\xi_q$-eigenspaces:

$$
  e_+(\xi_q) = \frac{\xi_q + q^{-1}\,\mathrm{id}_A}{[2]_q},
  \qquad
  e_-(\xi_q) = \frac{q\,\mathrm{id}_A - \xi_q}{[2]_q}.
$$

These project onto the **symmetric** (even, weight-$0$) and
**antisymmetric** (odd, weight-$1$) eigenspaces of the Reeb
action respectively.

### Reeb-driven iteration

Each application of $C_q$ is clocked by one period of the Reeb
flow ([Reeb flow](#def:categorical-q-reeb-flow)).  The
$q$-Collatz orbit of $a \in A$ is the sequence

$$
  a,\; C_q(a),\; C_q^2(a),\; \ldots
$$

where $C_q^k = \underbrace{C_q \circ \cdots \circ C_q}_{k}$,
each step consuming one Reeb circuit of $n_R(q) = q/(q-1)$
discrete substrate iterations
([operations per Planck](#prop:reeb-operations-per-planck)).

### The obstruction in a quantum universe

In a general QU $(\mathbf{C}, A, \tau)$ without the
observability axiom, define the **Collatz obstruction class**:

$$
  \kappa_C \;\in\; H^1\bigl(\mathbb{G}_m^{\mathrm{nt}},\,
  \mathcal{E}\!nd(A)^\times\bigr)
$$

as the cohomology class measuring the failure of $C_q$-orbits
to converge uniformly over the base $\mathbb{G}_m^{\mathrm{nt}}$.
Concretely, $\kappa_C$ is the obstruction to constructing a
global section $\sigma \colon \mathbb{G}_m^{\mathrm{nt}} \to A$
satisfying $C_q(\sigma(q)) = \sigma(q)$ for all $q$ — i.e.,
a universal fixed point of the Collatz family.

**In a QU (no observability):**
The gauge group $G$ is unconstrained, so the Hecke projectors
$e_\pm(\xi_q)$ need not respect the Frobenius pairing.  The
Reeb eigenspaces may overlap with kernel directions of $\mu$,
and $\kappa_C$ can be non-trivial:

$$
  \kappa_C \neq 0
  \quad\Longleftrightarrow\quad
  \exists\, a \in A \text{ whose } C_q\text{-orbit does not converge.}
$$

The obstruction is valued in the Kummer filtration
([root-of-unity truncation](#prop:root-of-unity-truncation)):
at each torsion level $\mu_n \subset \mathbb{G}_m$, the
specialization $\kappa_C|_{\mu_n}$ measures the $n$-periodic
obstructions to convergence.

### Evaluation on a QOU: the conjecture

**In a QOU** $(\mathbf{C}, \theta, G, \mathcal{S})$ — where
the observability axiom, the Tannaka--Krein reconstruction
([TK isomorphism](#thm:tannaka-krein-isomorphism)), and
torsion avoidance ($q \in \mathbb{G}_m^{\mathrm{nt}}$) all
hold — the obstruction vanishes:

$$
  \boxed{\kappa_C = 0
  \quad\text{in}\quad
  H^1\bigl(\mathbb{G}_m^{\mathrm{nt}},\,
  \mathcal{E}\!nd(A)^\times\bigr).}
$$

**Equivalently:** for every $q > 1$ in the substrate range and
every $a \in A$ in the positive cone, the Reeb-clocked
$q$-Collatz orbit $\{C_q^k(a)\}_{k \geq 0}$ converges to
the unit $\eta(\mathbf{1})$.

**Mechanism.** The three QOU axioms conspire:

1. **Torsion avoidance** ($q \notin \mu_\infty$): ensures
   $[2]_q \neq 0$, so $\mu^{-1}_{[2]_q}$ exists and the
   even branch is well-defined.
   The mass gap $\Delta_q = (q - q^{-1})(1 - q^{-1})^2 > 0$
   ([Gm torsion](#rem:substrate-gm-torsion)) guarantees
   spectral separation between the two Hecke channels.

2. **Reeb periodicity** ($\xi_q^{\Omega_q} = \mathrm{id}_A$):
   the Reeb derivation has finite period, so the Hecke
   eigendecomposition is a finite direct sum.  Each orbit
   segment of length $\Omega_q$ experiences both the
   contractive ($e_+$, division by $[2]_q$) and expansive
   ($e_-$, multiplication by $[3]_q$) branches with
   Reeb-weighted frequencies.

3. **Observability** (semisimple $G$, faithful $\tau$):
   the Tannaka--Krein equivalence
   $\mathbf{C} \simeq \mathrm{Rep}(G)$ forces
   $A$ to decompose into irreducible $G$-modules.  The
   Hecke projectors $e_\pm(\xi_q)$ align with the
   $G$-isotypic decomposition, and the contractive
   rate $[2]_q^{-1} < 1/2$ (since $[2]_q = q + q^{-1} > 2$
   for $q > 1$) dominates: averaged over a Reeb period,
   the orbit contracts by a factor
   $\lambda_q = [2]_q^{-1} \cdot [3]_q < 1$.

### Classical limit

At $q = 1$ the $\mathbb{G}_m$-family specializes:
$[2]_1 = 2$, $[3]_1 = 3$, the Reeb derivation trivializes
($\xi_1 = \mathrm{id}$), and the Hecke projectors become
the classical parity projectors
$e_\pm((-1)^n) = (1 \pm (-1)^n)/2$.  The categorical
endomorphism $C_1$ recovers the classical Collatz map:

$$
  C_1(n)
  = \begin{cases}
      n/2 & n \text{ even},\\
      3n + 1 & n \text{ odd}.
    \end{cases}
$$

The obstruction $\kappa_C|_{q=1}$ specializes to the classical
Collatz conjecture.  But $q = 1 \in \mu_1$ is a torsion point:
the mass gap closes ($\Delta_1 = 0$), the Hecke channels
degenerate, and the QOU axioms fail.  The classical Collatz
conjecture is thus the **boundary case** — the $q \to 1$
shadow of a $q$-deformed statement that admits a categorical
proof for $q > 1$.

### Information-theoretic content: the fifth evaluation of $\chi(A)$

The Collatz obstruction $\kappa_C$ is a **fifth evaluation**
of the universal obstruction class $\chi(A) \in HH^2 \cong k$,
alongside the spectral (RH), collision (NS), elliptic (BSD),
and computational (P $\neq$ NP) restrictions
([skein resolution obstruction](#def:skein-resolution-obstruction)).
Define the **Collatz restriction map**:

$$
  \mathrm{res}_C \colon HH^2(\mathrm{Ad})
  \;\longrightarrow\;
  H^1\bigl(\mathbb{G}_m^{\mathrm{nt}},\,
  \mathcal{E}\!nd(A)^\times\bigr),
  \qquad
  \chi(A) \;\longmapsto\; \kappa_C.
$$

Since $HH^2(\mathrm{Ad})$ is one-dimensional, the Collatz
obstruction is proportional to all four other evaluations:
the single integer $\chi(A) = -6$ controls whether Collatz
orbits converge, just as it controls whether the Riemann
zeros align, the NS solutions remain regular, the BSD rank
vanishes, and the skein tree resists polynomial pruning.

**Kummer reduction.**
The Kummer filtration applies
([root-of-unity truncation](#prop:root-of-unity-truncation)):

$$
  \kappa_C \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

At torsion levels $n \mid 6$, the Collatz obstruction vanishes
and orbits converge modulo $n$.  At levels $n \nmid 6$, the
obstruction persists — there exist $n$-periodic Collatz cycles
modulo these torsion points.

**Entropy of the $q$-Collatz orbit.**
Each Collatz step generates operational entropy
$\eta_q = (2q-1)/q^3$
([operational entropy](#def:operational-entropy)) per Reeb
circuit.  The total information processed by a $q$-Collatz
orbit of length $\sigma_q(a)$ is:

$$
  I_C(a, q)
  \;=\;
  \sigma_q(a) \cdot \eta_q
  \;=\;
  \sigma_q(a) \cdot \frac{2q-1}{q^3}
  \quad\text{nats}.
$$

The convergence conjecture ($\kappa_C = 0$) is equivalent to
the statement that $I_C(a, q) < \infty$ for all $a$ — every
orbit processes only finitely many nats before reaching the
fixed point.  The information rate per Planck time is bounded
by the bandwidth
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

The Collatz orbit is information-bounded: each step fits
within the Planck-scale computation budget, and convergence
means the total computation is finite.

### Connection to the $q$-zeta function

The stopping-time distribution of $C_q$-orbits is encoded by
the Dirichlet series
([local $q$-zeta](#def:local-q-zeta-function)):

$$
  Z_C(s, q)
  \;=\;
  \sum_{a \in A^+} \sigma_q(a)\,\|a\|^{-s},
$$

where $\sigma_q(a)$ is the number of Reeb circuits until
convergence.  The Reeb flow bridge
([bridge](#rem:reeb-flow-bridge)) identifies each
$C_q$-periodic orbit with a closed Reeb trajectory — a prime
ideal of the substrate.  If the
[$q$-Riemann hypothesis](#conj:classical-riemann-hypothesis)
holds, the stopping times are equidistributed modulo the
$[2]_q$-adic valuation, and $Z_C(s, q)$ has analytic
continuation to $\mathrm{Re}(s) > 1/2$ with no zeros on the
critical line.

### Summary: five evaluations of $\chi(A)$

| Evaluation | Obstruction | Domain | Classical shadow |
|------------|------------|--------|-----------------|
| Spectral | $\kappa_\zeta$ | $H^1(\mathbb{G}_m, \mathcal{O}^\times)$ | Riemann Hypothesis |
| Collision | $\kappa_{\mathrm{NS}}$ | $H^2(\mathcal{S}, \mathcal{B})$ | NS regularity |
| Elliptic | $\kappa_{\mathrm{BSD}}$ | $H^1(\mathcal{E}_q, \mathbb{G}_m)$ | Birch--Swinnerton-Dyer |
| Computational | $\kappa_c^{\mathrm{comp}}$ | $H^2(\mathcal{R}, \mathbb{G}_m)$ | P $\neq$ NP |
| **Collatz** | $\kappa_C$ | $H^1(\mathbb{G}_m^{\mathrm{nt}}, \mathcal{E}\!nd(A)^\times)$ | **Collatz conjecture** |

All five are images of the single class
$\chi(A) \in HH^2(\mathrm{Ad}) \cong k$ under restriction
maps to different cohomological targets.  In a QOU with
$\chi(A) = -6$, the Kummer filtration determines which
torsion levels obstruct each problem.
