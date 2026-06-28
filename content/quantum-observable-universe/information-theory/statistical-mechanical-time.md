The information-theoretic time $\mathcal{T}$
([information-theoretic time](#def:information-theoretic-time))
is a counting measure on discrete Reeb operations.  The passage
to a smooth time coordinate is a **statistical mechanical
coarse-graining**, entirely analogous to the emergence of
thermodynamic quantities from microscopic dynamics.

**The analogy.**

See [Table](#tbl:statistical-mechanical-time-table-data).

The mapping is not metaphorical — it is structural.  The same
mathematical mechanism (Riemann sum $\to$ integral as the number of
terms diverges) produces both thermodynamic equilibrium from
molecular collisions and continuous time from discrete Reeb
operations.

**Crossover at $\sim 10$ operations.**
At $q = q_0$
([local substrate $q$](#prop:local-substrate-q)),
$t_P \approx 10.1$
([iterations per Reeb circuit](#prop:reeb-operations-per-planck)).
The central limit theorem applies to sums of $\sim 10$
independent operations: the statistical fluctuations in the
aggregate are $O(1/\sqrt{10}) \approx 30\%$.  This is large
enough that individual discrete steps are not yet fully smoothed
— quantum-gravitational discreteness should produce $O(\hbar_q) \approx 10\%$ corrections to the continuous Reeb flow.

By contrast, at $q = 1.01$ ($t_P \approx 101$), fluctuations
are $O(1/\sqrt{101}) \approx 10\%$ and the continuous
approximation is good.  At $q = 1.001$ ($t_P \approx 1001$),
fluctuations are $\sim 3\%$ and time is effectively smooth.

**Exceptional divisor dynamics at each scale.**

At the Big Bang ($t_P = 1$): each Planck unit contains exactly
one braiding evaluation on the exceptional divisor --- one Hecke
generator applied within the Reeb bundle $S^3 \to \mathcal{S}_p$
([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)).
The link-length resolution increases by exactly one crossing per
tick.  The dynamics is fully resolved — the Julia set iteration
$f_q$ is applied once, and the orbit structure of $f_q$ over
$\mathbb{F}_\pp$ is visible step by step.

At $q = q_0$ ($t_P \approx 10$): each Planck unit contains
$\sim 10$ braiding evaluations.  Within one Planck time, the
exceptional divisor undergoes $\sim 10$ iterations of $f_q$,
each advancing the link-length resolution by one crossing.
The aggregate effect — $10$ crossings resolved — is
observable; the individual intermediate states are not
separately resolvable at the Planck scale.  The observable
quantity is the **average information per Planck unit**
$I_P = n_R \cdot h(q)$, not the per-step information $h(q)$.

At the classical limit ($t_P \to \infty$): infinitely many
iterations compose each unit.  The Julia set dynamics becomes
the continuous Reeb flow, the orbit structure becomes the
smooth invariant measure $\mu_J$, and the
per-operation information $h(q) \to 0$ while the aggregate
$I_P = t_P \cdot h(q)$ remains finite — the information rate
of the smooth flow.

**Connection to jet prolongation.**
Each Reeb operation is one jet prolongation
([Planck steps as jet orders](#rem:jet-planck-steps)).  In the
statistical regime, the $\sim 10$ jet prolongations within a
single Planck time produce a **statistical jet**: a
coarse-grained Taylor approximation of the energy function $E$
that averages over the $10$ intermediate polynomial orders.
The continuous limit ($q \to 1$) recovers the full analytic
germ $J^\infty E$: the smooth Taylor series is the
thermodynamic limit of the discrete jet tower.
