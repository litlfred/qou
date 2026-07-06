The information-theoretic time $\mathcal{T}$ ([information-theoretic time](#def:information-theoretic-time)) acts as a strict counting measure on discrete Reeb operations. The passage to a smooth time coordinate entails a statistical mechanical coarse-graining, entirely structurally analogous to the emergence of thermodynamic quantities from microscopic dynamics.

**The analogy.**
See [Table](#tbl:statistical-mechanical-time-table-data).

The mapping stands mathematically exact. The single mechanism of passing from a Riemann sum to an integral drives both the emergence of thermodynamic equilibrium from molecular collisions and the emergence of continuous time from discrete Reeb operations.

**Crossover at $\sim 10$ operations.**
At $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), we have $t_P \approx 10.1$ ([iterations per Reeb circuit](#prop:reeb-operations-per-planck)). The central limit theorem applies to sums of $\sim 10$ independent operations. Statistical fluctuations in the aggregate scale as $O(1/\sqrt{10}) \approx 30\%$. This large variance implies individual discrete steps are not fully smoothed. Quantum-gravitational discreteness reliably produces $O(\hbar_q) \approx 10\%$ corrections to the continuous Reeb flow.

Conversely, at $q = 1.01$ ($t_P \approx 101$), fluctuations drop to $O(1/\sqrt{101}) \approx 10\%$. The continuous approximation holds well. At $q = 1.001$ ($t_P \approx 1001$), fluctuations fall to $\sim 3\%$. Time effectively smooths.

**Exceptional divisor dynamics at each scale.**
At the Big Bang ($t_P = 1$), each Planck unit captures exactly one braiding evaluation on the exceptional divisor. This constitutes a single Hecke generator applied within the Reeb bundle $S^3 \to \mathcal{S}_p$ ([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)). Link-length resolution increases by precisely one crossing per tick. Dynamics remain fully resolved. The Julia set iteration $f_q$ executes once, leaving its orbit structure over $\mathbb{F}_\pp$ visible step by step.

At $q = q_0$ ($t_P \approx 10$), each Planck unit executes $\sim 10$ braiding evaluations. Within one Planck time, the exceptional divisor undergoes $\sim 10$ iterations of $f_q$, each advancing the link-length resolution by one crossing. The aggregate effect resolving $10$ crossings is fully observable. However, the intermediate states cannot be individually resolved at the Planck scale. The true observable quantity is the average information per Planck unit, $I_P = n_R \cdot h(q)$, not the per-step information $h(q)$.

At the classical limit ($t_P \to \infty$), infinitely many iterations fill each unit. The Julia set dynamics degenerates into continuous Reeb flow. The orbit structure flattens into the smooth invariant measure $\mu_J$. While per-operation information $h(q) \to 0$, the aggregate $I_P = t_P \cdot h(q)$ remains finite, dictating the information rate of the smooth flow.

**Connection to jet prolongation.**
Each Reeb operation executes exactly one jet prolongation ([Planck steps as jet orders](#rem:jet-planck-steps)). In the statistical regime, the $\sim 10$ jet prolongations occurring within a single Planck time generate a statistical jet. This constitutes a coarse-grained Taylor approximation of the energy function $E$ that effectively averages over the $10$ intermediate polynomial orders. The continuous limit ($q \to 1$) correctly recovers the full analytic germ $J^\infty E$. The smooth Taylor series strictly arises as the thermodynamic limit of the discrete jet tower.
