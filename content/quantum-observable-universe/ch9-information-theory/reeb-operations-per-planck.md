**Proposition.**
*Let $q \in k^\times \setminus \{1\}$ and let $t_P(q) = q/(q-1)$
be the Planck time ([Planck time](#def:planck-time)).  The number
of Reeb operations — iterations of $f_q(z) = z^2 + c(q)$ on the
exceptional divisor — that fit within one Planck unit is*

$$
  n_R(q) \;=\; t_P(q) \;=\; \frac{q}{q - 1} \;=\; \frac{1}{\hbar_q}.
$$

*Each operation is one braiding evaluation (one $R$-matrix
application), one jet prolongation step, and one circuit of the
$U(1)$ fiber above the exceptional divisor.*

*Proof.*
One Planck unit of Reeb flow displaces by $\ell_P = 1$
([Planck time](#def:planck-time)).  Each iteration of $f_q$
advances the phase by $\hbar_q$ (one angular unit of the
$q$-Reeb flow, since $\mathcal{L}_\xi Z = J\hbar_q Z$).
Therefore the number of full iterations in one Planck unit is
$1/\hbar_q = t_P(q)$.  $\square$

**Regime values.**

| $q$ | $n_R$ | Interpretation |
|-----|-------|----------------|
| $\to \infty$ | $\to 1$ | Big Bang: one braiding per Planck unit, fully resolved |
| $1.1097$ | $\approx 10.1$ | Our universe ([local substrate $q$](#prop:local-substrate-q)): $\sim 10$ braiding operations per Planck time |
| $2$ | $2$ | Two operations per unit |
| $1.01$ | $101$ | Near-classical: $\sim 100$ operations, approaching continuum |
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
