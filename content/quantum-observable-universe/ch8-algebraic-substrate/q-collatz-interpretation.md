The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
places the Collatz problem inside the paper's universal
obstruction framework as a **fifth evaluation** of the Euler
class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$.

### Five evaluations of $\kappa_0$

The one-dimensionality of $HH^2(\mathrm{Ad}) \cong k$
([QOU obstruction reduction](#thm:qou-obstruction-reduction))
means every obstruction is a restriction of the Euler class
$\kappa_0$ to a sub-locus of the state bundle $\mathcal{S}$:

| Evaluation | Locus $\mathcal{S}_\bullet$ | Horizon | Classical shadow |
|------------|---------------------------|---------|-----------------|
| Spectral | $\mathrm{Spec}(\xi_q)$ | spectral gaps | Riemann Hypothesis |
| Collision | $\Sigma$ (vortex collision) | blowup locus | NS regularity |
| Elliptic | $\mathcal{E}_q$ (Descartes curve) | rank jump | Birch--Swinnerton-Dyer |
| Computational | $\mathcal{R}(L)$ (resolution tree) | $\mathcal{H}_c$ | P $\neq$ NP |
| **Collatz** | $\mathcal{S}_{C_q}$ (iteration locus) | $\mathcal{H}_{Col}$ | **Collatz conjecture** |

### The Collatz horizon as boundary condition

The formulation parallels the P $\neq$ NP boundary
([P vs NP boundary](#conj:p-vs-np-boundary)):

| | P $\neq$ NP | Collatz |
|---|---|---|
| Space | Resolution tree $\mathcal{R}(L)$ | Iteration locus $\mathcal{S}_{C_q}$ |
| Observable part | $\mathcal{R}^{\circ}$ (poly-time computable) | $A^{\mathrm{conv}}_q$ (convergent orbits) |
| Horizon | $\mathcal{H}_c = \overline{\mathcal{R}^{\circ}} \setminus \mathcal{R}^{\circ}$ | $\mathcal{H}_{Col} = \overline{A^{\mathrm{conv}}_q} \setminus A^{\mathrm{conv}}_q$ |
| Obstruction | $\kappa_c^{\mathrm{comp}} \neq 0$ | $\kappa_C = 0$ (conj.) |
| Criterion | $\mathcal{H}_c \neq \varnothing$ (P $\neq$ NP) | $\mathcal{H}_{Col} = \varnothing$ (convergence) |

The P $\neq$ NP horizon is **non-empty** (the obstruction
persists, $c \neq 0$).  The Collatz horizon is conjectured
**empty** ($c_C = 0$) — the iteration locus lies entirely
in the convergent regime.

### The algebraic engine: $[2]_q^2 - [3]_q = q$

The contraction estimate rests on a single algebraic identity:

$$
  [2]_q^2 - [3]_q = (q+1)^2 - (q^2+q+1) = q.
$$

This has three consequences:

1. **Strict inequality** $[3]_q < [2]_q^2$ for all $q > 0$.
   The gap is $q$ itself — the substrate parameter.

2. **Geometric mean contraction.** At equal Reeb distribution
   ($f_+ = 1/2$), the per-step Lyapunov multiplier is
   $\lambda_q = \sqrt{[3]_q/[2]_q^2} < 1$.

3. **Critical fraction below $1/2$.**  Convergence requires
   only $f_+ > f_+^* = \log([3]_q/[2]_q)/\log[3]_q < 1/2$.
   The Reeb rotation generically gives $\langle f_+ \rangle = 1/2$,
   providing a $13\%$ excess margin at $q_0$.

### Reeb rotation vs. classical parity alternation

The Reeb flow $\phi_t^q$ rotates each element of $A$
through the weight decomposition
$A = A_H \oplus A_V$ with period $\Omega_q$.
This rotation is the categorical mechanism
behind the classical observation that Collatz orbits
alternate between even and odd values:

| Classical | Categorical |
|-----------|------------|
| $3n+1$ maps odd to even | $\phi^q_{t_P}$ rotates $A_V \to A_H$ |
| Parity changes under arithmetic | Reeb flow advances eigenphase |
| Even steps occur with frequency $\approx 1/2$ | $\langle f_+ \rangle_{\mathrm{Reeb}} = 1/2$ |
| $3/4 < 1$ (geometric mean) | $[3]_q/[2]_q^2 < 1$ (algebraic identity) |

At $q = 1$ the Reeb period collapses ($\Omega_1 = 1$),
the rotation degenerates to the parity switch
$(-1)^n$, and the smooth Reeb dynamics become the
discrete even/odd branching.

### Information-theoretic bound

Each Collatz step generates operational entropy
$\eta_q = (2q-1)/q^3$
([operational entropy](#def:operational-entropy)) per Reeb
circuit.  The total information processed by a
convergent orbit of stopping time $\sigma_q(a)$ is:

$$
  I_C(a, q)
  \;=\;
  \sigma_q(a) \cdot \eta_q
  \quad\text{nats}.
$$

The convergence conjecture ($\mathcal{H}_{Col} = \varnothing$)
is equivalent to $I_C(a, q) < \infty$ for all $a$ — every
orbit is an **information-bounded** computation on the
substrate, fitting within the Planck bandwidth
([bandwidth bound](#prop:p-bandwidth-bound)).

### Stopping-time zeta function

The stopping-time distribution is encoded by the
Dirichlet series
([local $q$-zeta](#def:local-q-zeta-function)):

$$
  Z_C(s, q)
  \;=\;
  \sum_{a \in A^+} \sigma_q(a)\,\|a\|^{-s}.
$$

The Reeb flow bridge
([bridge](#rem:reeb-flow-bridge)) identifies $C_q$-periodic
orbits with closed Reeb trajectories.  If the
[$q$-Riemann hypothesis](#conj:classical-riemann-hypothesis)
holds, stopping times are equidistributed modulo the
$[2]_q$-adic valuation and $Z_C(s, q)$ admits analytic
continuation to $\mathrm{Re}(s) > 1/2$.
