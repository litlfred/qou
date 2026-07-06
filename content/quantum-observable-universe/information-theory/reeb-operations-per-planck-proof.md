*Proof.*
The Reeb time coordinate is defined as $t = \hbar_q \cdot \mathcal{T}$ ([information-theoretic time](#def:information-theoretic-time)). Consequently, each discrete $f_q$-iteration (an increment of $\mathcal{T}$ by $1$) corresponds to a continuous time duration of $\hbar_q$. The number of iterations composing one full Reeb circuit (continuous duration $1$) is therefore exactly $1/\hbar_q = t_P(q)$. $\square$

**Regime values.**

| $q$ | $n_R$ | Interpretation |
|---|---|---|
| $\to \infty$ | $\to 1$ | Deep-quantum: one iteration per circuit, fully discrete |
| $q_0$ | $\approx 10.1$ | Our universe ([local substrate $q$](#prop:local-substrate-q)): $\sim 10$ iterations per circuit |
| $2$ | $2$ | Two iterations per circuit |
| $1.01$ | $101$ | Near-classical: $\sim 100$ iterations per circuit |
| $\to 1$ | $\to \infty$ | Classical limit: infinitely many, continuous Reeb flow |

**Physical meaning at $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)).**
At our local substrate parameter, approximately $10$ iterations of the Julia set dynamics $f_q$ occur within each Planck time. Each iteration:
1. Advances the phase of the Reeb vector by $\hbar_q \approx 0.099$ of a full circuit.
2. Applies the $q$-connection $\nabla_q$ once, correlating adjacent fibers.
3. Evaluates one $R$-matrix, resolving one braiding crossing on the exceptional divisor.

The link-length resolution within the exceptional divisor grows with each operation. After $n$ steps, the divisor resolves knots up to crossing number $n$. Within a single Planck time at $q = q_0$, the exceptional divisor completes $\sim 10$ braiding evaluations. This provides ample capacity to resolve the full electron-positron sector ($c = 3$).

**Information rate.**
The information processed per Planck unit is

$$
  I_P(q) =  n_R(q) \cdot \eta_q.
$$

Here $\eta_q = (2q-1)/q^3$ is the operational entropy ([operational entropy](#def:operational-entropy)). This parameter quantifies the information generated per $f_q$-iteration, dictated strictly by the gravitational self-consistency condition.

In the deep-quantum regime ($q \to \infty$), $n_R \to 1$ and $\eta_q \to 0$. The dynamics simplify entirely, yielding $I_P \to 0$. At the classical limit ($q \to 1$), $\eta_q \to 1$ nat per step. At $q = q_0$, $I_P \approx 10.1 \times 0.892 \approx 9.0$ $q$-bits per Planck time.
