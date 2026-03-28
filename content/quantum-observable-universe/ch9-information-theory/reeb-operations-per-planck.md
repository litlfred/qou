**Proposition.**
*Let $q \in k^\times \setminus \{1\}$ and let $t_P(q) = q/(q-1)$
be the Planck time ([Planck time](#def:planck-time)).  The number
of discrete $f_q$-iterations — evaluations of
$f_q(z) = z^2 + c(q)$ on the exceptional divisor — that compose
one Reeb circuit is*

$$
  n_R(q) \;=\; t_P(q) \;=\; \frac{q}{q - 1} \;=\; \frac{1}{\hbar_q}.
$$

*Each iteration is one braiding evaluation (one $R$-matrix
application) and one jet prolongation step, advancing the phase
by the fraction $\hbar_q$ of a full circuit.*

*Proof.*
From the definition of the Reeb time coordinate
($t = \hbar_q \cdot \mathcal{T}$,
[information-theoretic time](#def:information-theoretic-time)),
each discrete $f_q$-iteration (an increment of $\mathcal{T}$
by $1$) corresponds to a continuous time duration of $\hbar_q$.
Therefore the number of iterations that compose one full Reeb
circuit (continuous duration $1$) is $1/\hbar_q = t_P(q)$.
$\square$

**Regime values.**

| $q$ | $n_R$ | Interpretation |
|-----|-------|----------------|
| $\to \infty$ | $\to 1$ | Big Bang: one iteration per circuit, fully discrete |
| $1.1097$ | $\approx 10.1$ | Our universe ([local substrate $q$](#prop:local-substrate-q)): $\sim 10$ iterations per circuit |
| $2$ | $2$ | Two iterations per circuit |
| $1.01$ | $101$ | Near-classical: $\sim 100$ iterations per circuit |
| $\to 1$ | $\to \infty$ | Classical limit: infinitely many, continuous Reeb flow |

**Physical meaning at $q = 1.1097$
([local substrate $q$](#prop:local-substrate-q)).**
At our local substrate parameter, approximately $10$ iterations
of the Julia set dynamics $f_q$ occur within each Planck time.
Each iteration:

1. Advances the phase of the Reeb vector by $\hbar_q \approx 0.099$
   of a full circuit
2. Applies the $q$-connection $\nabla_q$ once, correlating
   adjacent fibers
3. Evaluates one $R$-matrix, resolving one braiding crossing on
   the exceptional divisor

The link-length resolution within the exceptional divisor grows
with each operation: after $n$ of the $\sim 10$ steps, the
divisor resolves knots up to crossing number $n$.  Within a
single Planck time at $q = 1.1097$, the exceptional divisor
completes $\sim 10$ braiding evaluations — enough to resolve
the full electron-positron sector ($c = 3$) with room to spare.

**Information rate.**
The information processed per Planck unit is

$$
  I_P(q) \;=\; n_R(q) \cdot h(q)
$$

where $h(q)$ is the information content per Reeb operation,
bounded by the Hausdorff dimension $d_H(q)$ of the Julia set
$J(f_q) \cap S^1$
([Julia set of Reeb flow](#rem:julia-set-reeb)) over
$\mathbb{C}$, or by the orbit complexity of $f_q$ over
$\mathbb{F}_\pp$.

At the Big Bang ($q \to \infty$): $n_R \to 1$ and $h \to 0$
(simplest dynamics), so $I_P \to 0$.
At the golden threshold ($q_{\mathrm{gold}} = 1/\varphi^2$):
$h(q)$ peaks (maximal fractal complexity).
At $q = 1.1097$: $I_P \approx 10.1 \cdot d_H(1.1097)$, the product
of moderate operation count and moderate per-operation information.
