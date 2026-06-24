**Proposition.**
*Let $q \in k^\times \setminus \{1\}$ and let $t_P(q) = q/(q-1)$
be the Planck time ([Planck time](#def:planck-time)).  The number
of discrete $f_q$-iterations — evaluations of
$f_q(z) = z^2 + c(q)$ on the exceptional divisor — that compose
one Reeb circuit is*

$$
  n_R(q) =  t_P(q) =  \frac{q}{q - 1} =  \frac{1}{\hbar_q}.
$$

*Each iteration is one braiding evaluation (one $R$-matrix
application) and one jet prolongation step, advancing the phase
by the fraction $\hbar_q$ of a full circuit.*

**Regime values.**

| $q$ | $n_R$ | Interpretation |
|-----|-------|----------------|
| $\to \infty$ | $\to 1$ | Deep-quantum: one iteration per circuit, fully discrete |
| $q_0$ | $\approx 10.1$ | Our universe ([local substrate $q$](#prop:local-substrate-q)): $\sim 10$ iterations per circuit |
| $2$ | $2$ | Two iterations per circuit |
| $1.01$ | $101$ | Near-classical: $\sim 100$ iterations per circuit |
| $\to 1$ | $\to \infty$ | Classical limit: infinitely many, continuous Reeb flow |

**Physical meaning at $q = q_0$
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
single Planck time at $q = q_0$, the exceptional divisor
completes $\sim 10$ braiding evaluations — enough to resolve
the full electron-positron sector ($c = 3$) with room to spare.

**Information rate.**
The information processed per Planck unit is

$$
  I_P(q) =  n_R(q) \cdot \eta_q
$$

where $\eta_q = (2q-1)/q^3$ is the operational entropy
([operational entropy](#def:operational-entropy)) --- the
information generated per $f_q$-iteration, determined by the
gravitational self-consistency condition.

In the deep-quantum regime ($q \to \infty$): $n_R \to 1$ and $\eta_q \to 0$
(simplest dynamics), so $I_P \to 0$.
At the classical limit ($q \to 1$): $\eta_q \to 1$ nat per step.
At $q = q_0$: $I_P \approx 10.1 \times 0.892 \approx 9.0$
$q$-bits per Planck time.
