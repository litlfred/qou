<!-- FILE_START: information-theoretic-time-julia-microscopic.md -->
We ground the information-theoretic time ([information-theoretic time](#def:information-theoretic-time)) in a microscopic dynamical theory: the Julia-set iteration $f_q$. The thermodynamic limit of this iteration yields the continuous Reeb flow.

**Julia set dynamics as the microscopic theory.**
We interpret the iteration $f_q(z) = z^2 + c(q)$ on the exceptional divisor as the microscopic dynamics of time. Each iterate $f_q^{\circ n}(z_0)$ constitutes one microstate of the temporal evolution. The continuous Reeb flow $\phi_t^q$ emerges as the macroscopic limit, obtained by averaging over $t_P(q)$ microscopic iterates per unit.

The Julia set $J(f_q)$ is the boundary separating escaping and bounded orbits. Its Hausdorff dimension $d_H(q)$ measures the complexity of the time evolution at parameter $q$. A higher $d_H$ indicates that the microscopic dynamics explores more phase space per operation, so macroscopic time carries more information per unit.
<!-- FILE_END: information-theoretic-time-julia-microscopic.md -->

<!-- FILE_START: information-theoretic-time-arrow.md -->
The information-theoretic time inherits its direction from the braiding order $\prec_c$. The arrow of time is not re-derived in the continuous limit.

**Consistency with the arrow of time.**
The braiding-induced ordering $\prec_c$ on the Hecke basis ([ordering–jet compatibility](#prop:ordering-jet-compatibility)) propagates through the jet tower. This defines forward and backward time at every brane level. We define the information-theoretic time $\mathcal{T}$ as the counting measure on this well-ordering: $\mathcal{T}(a) < \mathcal{T}(b)$ iff $a \prec_c b$. The rescaling $t = \hbar_q \mathcal{T}$ preserves the order, ensuring the Reeb time coordinate inherits the same arrow. The arrow embeds the discrete algebraic structure.
<!-- FILE_END: information-theoretic-time-arrow.md -->

<!-- FILE_START: statistical-mechanical-time.md -->
The information-theoretic time acts as a strict counting measure on discrete Reeb operations. The passage to a smooth time coordinate entails a statistical coarse-graining, structurally analogous to the emergence of thermodynamic quantities from microscopic dynamics.

**The analogy.**
See [Table](#tbl:statistical-mechanical-time-table-data).

The mechanism of passing from a Riemann sum to an integral drives both the emergence of thermodynamic equilibrium from molecular collisions and the emergence of continuous time from discrete Reeb operations.

**Crossover at $\sim 10$ operations.**
At $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), we have $t_P \approx 10.1$ ([iterations per Reeb circuit](#prop:reeb-operations-per-planck)). The central limit theorem applies to sums of $\sim 10$ independent operations. Statistical fluctuations scale as $O(1/\sqrt{10}) \approx 30\%$. This large variance implies individual discrete steps are not fully smoothed. Quantum-gravitational discreteness reliably produces $O(\hbar_q) \approx 10\%$ corrections to the continuous Reeb flow.

Conversely, at $q = 1.01$ ($t_P \approx 101$), fluctuations drop to $O(1/\sqrt{101}) \approx 10\%$. At $q = 1.001$, they fall to $\sim 3\%$ and time effectively smooths.

**Exceptional divisor dynamics at each scale.**
At the Big Bang ($t_P = 1$), each Planck unit captures exactly one braiding evaluation on the exceptional divisor. The link-length resolution increases by precisely one crossing per tick. Dynamics remain fully resolved. The Julia set iteration $f_q$ executes once.

At $q = q_0$ ($t_P \approx 10$), each Planck unit executes $\sim 10$ braiding evaluations. The exceptional divisor undergoes $\sim 10$ iterations of $f_q$. The aggregate effect resolving $10$ crossings is fully observable. However, the intermediate states cannot be individually resolved at the Planck scale.

At the classical limit ($t_P \to \infty$), infinitely many iterations fill each unit. The Julia set dynamics degenerates into continuous Reeb flow. The orbit structure flattens into the smooth invariant measure $\mu_J$.

**Connection to jet prolongation.**
Each Reeb operation executes exactly one jet prolongation ([Planck steps as jet orders](#rem:jet-planck-steps)). The $\sim 10$ jet prolongations occurring within a single Planck time generate a statistical jet, which averages the intermediate polynomial orders. The continuous limit ($q \to 1$) recovers the analytic germ $J^\infty E$. The smooth Taylor series arises as the thermodynamic limit of the discrete jet tower.
<!-- FILE_END: statistical-mechanical-time.md -->

<!-- FILE_START: big-bang-info.md -->
At $\mathcal{T} = 0$, no Reeb operation has occurred. The initial state ([bundle initial conditions](#def:bundle-initial-conditions)) specifies fiber data without horizontal transport. No information has propagated. Position is known exactly; momentum is entirely undetermined.

At $\mathcal{T} = 1$, the first iteration of $f_q$ connects neighboring fibers. The $q$-connection $\nabla_q$ acts once. Over $\mathbb{F}_\pp$, this reduces to $z_1 = z_0^2 + c(q)$. The Heisenberg commutator $[\hat{X}, \hat{P}]_q = J\hbar_q$ is near-maximal.

Because $t_P \to 1$ at the Big Bang, the information-theoretic time $\mathcal{T}$ and the Reeb time coordinate $t$ coincide: $t = \hbar_q \mathcal{T} \approx \mathcal{T}$. There is no coarse-graining. We resolve each braiding on the exceptional divisor individually. The particle spectrum unfolds step by step through the jet prolongation tower ([Planck steps as jet orders](#rem:jet-planck-steps)).
<!-- FILE_END: big-bang-info.md -->

<!-- FILE_START: planck-computation.md -->
The number of Reeb operations per Planck unit, $n_R(q) = q/(q-1)$ ([Reeb operations per Planck unit](#prop:reeb-operations-per-planck)), determines the **computational capacity** of a Planck-length region.

Each operation evaluates $f_q(z) = z^2 + c(q)$. It resolves one crossing in the braid representation of the local link structure. The total computational work per Planck unit equals $n_R(q)$ polynomial evaluations.

At $q = q_0$, a Planck-length region performs roughly $10$ polynomial evaluations per Planck time. This defines the microscopic computational rate of the universe at our scale. It represents the clock speed of the exceptional divisor dynamics, which coarse-grains into the smooth Reeb flow.
<!-- FILE_END: planck-computation.md -->