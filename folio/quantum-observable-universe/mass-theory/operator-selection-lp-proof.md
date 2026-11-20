*Proof.*
The feasible set is non-empty: any element $\Phi_0$ with
$\mathrm{tr}_M(\Phi_0) > 0$ can be rescaled to satisfy the net constraint,
and the Frobenius positivity constraints admit interior points (the identity
$\gamma = \mathbf{1}$ satisfies $G \cdot e_1 > 0$ componentwise for
generic $q$).  The boundedness constraint $x_i \geq -M$ ensures the
feasible polyhedron is bounded.  By the LP strong duality theorem
(no duality gap for feasible, bounded linear programs), the primal
minimum equals the dual maximum.

## Complementary slackness

At optimality, the complementary slackness conditions hold:

$$
  y_i^* \cdot \left(\sum_{j=1}^{d} G_{ij}\, x_j^* \right) = 0
  \quad \forall\, i
$$

Each dual variable $y_i^*$ is positive only when the corresponding
Frobenius constraint is tight.  The set of tight constraints
$\mathcal{A} = \{i : y_i^* > 0\}$ identifies the **active demand
channels** -- the channels that the optimal operator $\Phi^*$ exactly
saturates.

## Confinement as the special case $n = 3$, $d = 6$

Setting $n = 3$ and $d = 6$ recovers the
[confinement LP](#prop:confinement-lp) exactly:

| General LP | Confinement LP ($n = 3$) |
|:---|:---|
| Basis $\{b_1, \ldots, b_d\}$ | $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ |
| Gram matrix $G \in \mathbb{R}^{d \times d}$ | $6 \times 6$ Gram matrix of $H_3(q)$ |
| Target $n_{\mathrm{target}}$ | $\approx 1.000$ (proton), $\approx 0.811$ (neutron) |
| Optimal $x^*$ | not determined by the program — the minimisers form a face at objective $0$. $\mathrm{NF}(\mathcal{B}_3) \approx (+0.998, -0.010, +0.009, +0.046, -0.044, 0)$ is **feasible but not optimal** ($\mathrm{tr}_M \approx 0.9986$). |
| Active set $\mathcal{A}$ | $\{\sigma_0, L_-\}$ (two active demand channels) |

The confinement LP is the $n = 3$ instantiation: three strands
encoding three quark colors, six NF basis elements spanning the
operator space, and the Borromean link $\mathcal{B}_3$ as the unique
LP vertex.

## Higher-strand generalizations

For $n > 3$, the LP dimensions grow as $d = n!$:

| $n$ | $d = n!$ | Physical regime |
|:---:|:---:|:---|
| $2$ | $2$ | Single-particle states (photon, electron) |
| $3$ | $6$ | Baryonic confinement (proton, neutron) |
| $4$ | $24$ | Tetraquark / exotic meson candidates |
| $5$ | $120$ | Pentaquark states |

At each strand number, the Frobenius Gram matrix $G$ is symmetric, and it is
non-degenerate — for $q \neq 0, 1$ — **on the quotient
$H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, not on $H_n$ itself**, so
that is where the LP is well-posed.

> **The LP dimension is the Catalan number $C_n$, not $n!$ (Convention D).**
> Posed on all of $H_n$ with $d = n!$ the statement above is false: under the
> production convention D the weights $y_\lambda$ vanish for every $\lambda$ with
> $\ell(\lambda) \geq 3$, so $G \in \mathbb{R}^{n! \times n!}$ is **singular** and
> the LP is degenerate rather than well-posed. Its rank is the surviving
> $\sum \dim^2 = C_n$:
>
> | $n$ | $d = n!$ (as tabled) | $\mathrm{rank} G = C_n$ | corank |
> |:---:|:---:|:---:|:---:|
> | $2$ | $2$   | $2$  | $0$ |
> | $3$ | $6$   | $5$  | $1$ |
> | $4$ | $24$  | $14$ | $10 = 3^2 + 1^2$ |
> | $5$ | $120$ | $42$ | $78 = 6^2+5^2+4^2+1^2$ |
>
> So the pentaquark row is a $42$-dimensional program, not a $120$-dimensional
> one, and the tetraquark row is $14$, not $24$. The optimal vertex $x^*$ and the
> active set $\mathcal{A}$ are well defined on the quotient; on $H_n$ the LP has
> a $\mathrm{corank} G$-dimensional space of optima differing by radical
> directions the trace cannot see.

  The optimal vertex $x^*$ identifies the minimum-action
operator, and the active set $\mathcal{A}$ identifies the saturated
demand channels.

## Relation to the spectral decomposition

The LP formulation is dual to the spectral decomposition of
[knot operator selection](#prop:knot-operator-selection), part (i).
The spectral decomposition writes $\Phi = \sum_\lambda d_\lambda(q)
\cdot \Phi_\lambda$ in the irrep basis; the LP writes
$\Phi = \sum_i x_i b_i$ in the NF basis.  The two are related by
the change-of-basis matrix $P$ between the NF basis and the
Wedderburn idempotent basis:

$$
  x_i = \sum_\lambda P_{i\lambda} \, d_\lambda(q) \,
  \mathrm{tr}_\lambda(\Phi_\lambda)
$$

The LP operates in the NF basis because the Gram matrix $G_{ij}$
and the Markov traces $t_i$ are directly computable from the Hecke
algebra relations, without requiring explicit knowledge of the
irrep decomposition.  The spectral decomposition provides the
physical interpretation (which knot operators mediate the
interaction); the LP provides the constructive selection
(which NF coefficients minimize the action).
