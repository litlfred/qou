The information-theoretic time $\mathcal{T}(q)$ ([information-theoretic time](#def:information-theoretic-time)) rescales to the continuous Reeb time coordinate. It passes through three regimes—discrete, statistical, and continuous—acting as a statistical-mechanical coarse-graining. One treats its microscopic Julia-set dynamics ([Julia-set iteration as the microscopic theory](#rem:information-theoretic-time-julia-microscopic)) and its arrow of time ([arrow of time from the braiding order](#rem:information-theoretic-time-arrow)) separately.

**Reeb time coordinate.**
The continuous time coordinate $t$ of the $q$-Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)) is the rescaled operation count:

$$
  t =  \frac{\mathcal{T}}{t_P(q)}
  =  \hbar_q \cdot \mathcal{T}
$$

where $t_P(q) = q/(q-1)$ is the Planck time ([Planck time](#def:planck-time)). The denominator $t_P(q)$ is the number of discrete $f_q$ iterations per Reeb circuit ([iterations per Reeb circuit](#prop:reeb-operations-per-planck)). Dividing by it converts the integer step count $\mathcal{T}$ into a continuous flow parameter.

**Three regimes.**

1. **Discrete regime** ($q \to \infty$, deep-quantum).
   $t_P \to 1$, so $t = \mathcal{T}$. The Reeb time coordinate equals the integer step count. Each tick represents one braiding, one jet prolongation, or one link resolved in the exceptional divisor. There is no sub-step structure and no averaging. Time is a natural number.

2. **Statistical regime** ($q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), the observed universe).
   $t_P \approx 10$. Approximately $10$ Reeb operations compose each Planck unit. Individual operations are not separately resolvable at the Planck scale. One observes their aggregate: the statistical average of $\sim 10$ braiding evaluations. The Reeb flow parameter $t$ becomes a coarse-grained time that smooths over discrete steps, just as thermodynamic quantities smooth over microscopic states.

3. **Continuous regime** ($q \to 1$, classical limit).
   $t_P \to \infty$. Infinitely many operations occur per unit. The discrete structure vanishes. The parameter $t$ is a smooth real variable and the Reeb flow $\phi_t^q$ is a genuine one-parameter group of diffeomorphisms. Time is $\mathbb{R}$-valued.

**The thermodynamic bridge.**
The passage from regime 1 to regime 3 is the statistical mechanical coarse-graining of time. For any smooth observable $g$ on the Reeb flow, the discrete time-average over one circuit ($t_P$ steps) is a Riemann sum:

$$
  \frac{1}{t_P} \sum_{n=0}^{t_P - 1} g\!\left(\frac{n}{t_P}\right)
  \xrightarrow{t_P \to \infty}
  \int_0^1 g(s)ds.
$$

The left side is the average of $g$ over $t_P$ discrete Reeb operations. The right side is the continuous-flow time-average. They agree to $O(1/t_P) = O(\hbar_q)$. The error vanishes precisely as the quantum Planck constant goes to zero.

At $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), one has $t_P \approx 10$. The Riemann approximation has $O(1/10) \approx 10\%$ relative error. This marks the scale where discreteness is marginally detectable, aligning with quantum-gravitational corrections as $O(\hbar_q)$ effects.
