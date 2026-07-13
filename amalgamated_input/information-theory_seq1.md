<!-- FILE_START: info-time-computation-intro.md -->
This section establishes the framework for time and computation. The following blocks trace the construction from `time-info` onward.
<!-- FILE_END: info-time-computation-intro.md -->

<!-- FILE_START: time-info.md -->
Time in the QOU is not an external parameter. It is the dynamics. The fundamental time variable is **information-theoretic time** $\mathcal{T}$. This measures the cumulative count of Reeb operations (iterations of the Julia set map $f_q(z) = z^2 + c(q)$ on the exceptional divisor). Each operation represents one braiding evaluation, one jet prolongation, and one tick of the braiding-induced ordering $\prec_c$ on the Hecke basis.

The continuous time coordinate $t$ of the Reeb flow $\phi_t^q$ emerges from $\mathcal{T}$ via statistical mechanical coarse-graining: $t = \hbar_q \mathcal{T}$. The quantum Planck constant $\hbar_q = 1 - q^{-1}$ plays the role of Boltzmann's constant. At the Big Bang ($q \to \infty$, $\hbar_q \to 1$), $t = \mathcal{T}$ and time is a natural number. Each tick is individually meaningful. At our local substrate parameter ($q = q_0$, $\hbar_q \approx 0.1$), approximately $10$ discrete operations compose each Planck unit. The continuous approximation carries an $O(\hbar_q) \approx 10\%$ error. At the classical limit ($q \to 1$, $\hbar_q \to 0$), infinitely many operations per unit make time smooth.

This section formalizes the Planck time. It counts the Reeb operations per Planck unit as a function of $q$. It defines information-theoretic time. Finally, it constructs the statistical mechanical bridge from discrete computation to continuous flow.
<!-- FILE_END: time-info.md -->

<!-- FILE_START: planck-time.md -->
**Definition.**
Let $q \in k^\times \setminus \{1\}$ denote the substrate parameter ([substrate parameter](#def:substrate-parameter)). Let $\hbar_q = 1 - q^{-1}$ denote the quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)). We define the **Planck time** as

$$
  t_P(q)  :=  \frac{1}{\hbar_q}
  =  \frac{q}{q - 1}.
$$

This rational function of $q$ is defined over any field $k$ where $q \neq 1$.

**Interpretation.**
One Planck time equals the period of a single full circuit of the $q$-Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)). We measure this in discrete $f_q$-iterations on the exceptional divisor ([Julia set of Reeb flow](#rem:julia-set-reeb)). One circuit comprises $t_P(q)$ iterations of $f_q(z) = z^2 + c(q)$. At the deep-quantum limit ($t_P = 1$), one iteration completes one circuit. At the physical substrate value $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), roughly $10$ iterations compose one circuit. The reciprocal $\hbar_q = 1/t_P$ represents the angular velocity: the fraction of a full circuit completed per $f_q$-iteration.

**Regime table.**

| Regime | $q$ | $\hbar_q$ | $t_P$ | Interpretation |
|--------|-----|-----------|-------|----------------|
| Deep-quantum | $q \to \infty$ | $\to 1$ | $\to 1$ | One $f_q$-step per circuit; fully discrete |
| Physical | $q = q_0$ | $0.0988$ | $\approx 10.1$ | $\sim 10$ $f_q$-steps per Reeb circuit |
| Classical | $q \to 1$ | $\to 0$ | $\to \infty$ | Infinitely many steps; continuous flow |

**Field realisations.**

- Over $\mathbb{F}_\pp$: $t_P = q/(q-1) \in \mathbb{F}_\pp$ for $q \in \mathbb{F}_\pp^\times \setminus \{1\}$. One Planck step evaluates $f_q(z) = z^2 + c(q)$ once.
- Over $\mathbb{Q}_\pp$: The valuation $v_\pp(t_P) = v_\pp(q) - v_\pp(q-1)$ encodes the $\pp$-adic proximity of $q$ to the classical limit.
- Over $\mathbb{C}$: This reproduces the angular period $T = 2\pi/\hbar_q$, up to the conventional factor $2\pi$.

**Planck length.**
After one Planck time of Reeb flow, the angular displacement is

$$
  \ell_P(q) =  \hbar_q \cdot t_P =  1
$$

This identity holds over any field. The Planck length strictly equals $1$. The parameter $q$ varies only the number of discrete operations $t_P(q)$ composing that unit displacement.
<!-- FILE_END: planck-time.md -->

<!-- FILE_START: reeb-operations-per-planck.md -->
*Let $q \in k^\times \setminus \{1\}$. Let $t_P(q) = q/(q-1)$ be the Planck time ([Planck time](#def:planck-time)). The number of discrete $f_q$-iterations (evaluations of $f_q(z) = z^2 + c(q)$ on the exceptional divisor) comprising one Reeb circuit is*

$$
  n_R(q) =  t_P(q) =  \frac{q}{q - 1} =  \frac{1}{\hbar_q}.
$$

*Each iteration executes one braiding evaluation (a single $R$-matrix application) and one jet prolongation step. Together, these advance the phase by exactly the fraction $\hbar_q$ of a full circuit.*
<!-- FILE_END: reeb-operations-per-planck.md -->

<!-- FILE_START: information-theoretic-time.md -->
**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with braiding-induced ordering $\prec_c$ ([ordering–jet compatibility](#prop:ordering-jet-compatibility)). Let $f_q(z) = z^2 + c(q)$ be the Julia set iteration on the exceptional divisor ([Julia set of Reeb flow](#rem:julia-set-reeb)).

The **information-theoretic time** at substrate parameter $q$ is the cumulative Reeb operation count:

$$
  \mathcal{T}(q)  :=  \sum_{n=0}^{N-1} 1
  =  N
$$

where $N$ is the total number of iterations of $f_q$ applied since a reference configuration $\mathcal{S}_0$ ([bundle initial conditions](#def:bundle-initial-conditions)). Each iteration advances the admissible ordering by one step. The count $\mathcal{T}$ determines the position in the braiding-induced ordering $\prec_c$ propagated through the jet tower.
<!-- FILE_END: information-theoretic-time.md -->

<!-- FILE_START: information-theoretic-time-properties.md -->
The information-theoretic time $\mathcal{T}(q)$ ([information-theoretic time](#def:information-theoretic-time)) rescales to the continuous Reeb time coordinate. It passes through three regimes—discrete, statistical, and continuous—acting as a statistical-mechanical coarse-graining. We treat its microscopic Julia-set dynamics ([Julia-set iteration as the microscopic theory](#rem:information-theoretic-time-julia-microscopic)) and its arrow of time ([arrow of time from the braiding order](#rem:information-theoretic-time-arrow)) separately.

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

2. **Statistical regime** ($q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), our universe).
   $t_P \approx 10$. Approximately $10$ Reeb operations compose each Planck unit. Individual operations are not separately resolvable at the Planck scale. We observe their aggregate: the statistical average of $\sim 10$ braiding evaluations. The Reeb flow parameter $t$ becomes a coarse-grained time that smooths over discrete steps, just as thermodynamic quantities smooth over microscopic states.

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

At $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)), we have $t_P \approx 10$. The Riemann approximation has $O(1/10) \approx 10\%$ relative error. This marks the scale where discreteness is marginally detectable, aligning with quantum-gravitational corrections as $O(\hbar_q)$ effects.
<!-- FILE_END: information-theoretic-time-properties.md -->

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

