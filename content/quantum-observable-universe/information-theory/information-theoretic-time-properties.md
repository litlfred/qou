The [information-theoretic time $\mathcal{T}(q)$](#def:information-theoretic-time)
rescales to the continuous Reeb time coordinate, passes through three
regimes (discrete, statistical, continuous) as a statistical-mechanical
coarse-graining, has the Julia-set iteration $f_q$ as its microscopic
theory, and inherits the arrow of time from the braiding order $\prec_c$.

**Reeb time coordinate.**
The continuous time coordinate $t$ of the $q$-Reeb flow
([$q$-Reeb flow](#ex:q-reeb-flow)) is the rescaled operation
count

$$
  t =  \frac{\mathcal{T}}{t_P(q)}
  =  \hbar_q \cdot \mathcal{T}
$$

where $t_P(q) = q/(q-1)$ is the Planck time
([Planck time](#def:planck-time)).  The denominator $t_P(q)$
is the number of discrete $f_q$ iterations per Reeb circuit
([iterations per Reeb circuit](#prop:reeb-operations-per-planck)):
dividing by it converts the integer step count $\mathcal{T}$
into a continuous flow parameter.

**Three regimes.**

1. **Discrete regime** ($q \to \infty$, deep-quantum).
   $t_P \to 1$, so $t = \mathcal{T}$: the Reeb time coordinate
   *is* the integer step count.  Each tick is individually
   meaningful — one braiding, one jet prolongation, one link
   resolved in the exceptional divisor.  There is no sub-step
   structure and no averaging.  Time is a natural number.

2. **Statistical regime** ($q = q_0$
   ([local substrate $q$](#prop:local-substrate-q)), our universe).
   $t_P \approx 10$: approximately $10$ Reeb operations compose
   each Planck unit.  Individual operations are no longer
   separately resolvable at the Planck scale; what is observable
   is their **aggregate** — the statistical average of $\sim 10$
   braiding evaluations.  The Reeb flow parameter $t$ becomes a
   coarse-grained time that smooths over discrete steps, exactly
   as thermodynamic quantities smooth over microscopic states.

3. **Continuous regime** ($q \to 1$, classical limit).
   $t_P \to \infty$: infinitely many operations per unit.  The
   discrete structure is invisible; $t$ is a smooth real
   parameter and the Reeb flow $\phi_t^q$ is a genuine
   one-parameter group of diffeomorphisms.  Time is
   $\mathbb{R}$-valued.

**The thermodynamic bridge.**
The passage from regime 1 to regime 3 is the statistical
mechanical coarse-graining of time.  For any smooth observable
$g$ on the Reeb flow, the discrete time-average over one
circuit ($t_P$ steps) is a Riemann sum:

$$
  \frac{1}{t_P} \sum_{n=0}^{t_P - 1} g\!\left(\frac{n}{t_P}\right)
  \xrightarrow{t_P \to \infty}
  \int_0^1 g(s)ds.
$$

The left side is the average of $g$ over $t_P$ discrete Reeb
operations; the right side is the continuous-flow time-average.
They agree to $O(1/t_P) = O(\hbar_q)$ — the error vanishes
precisely as the quantum Planck constant goes to zero.

At $q = q_0$
([local substrate $q$](#prop:local-substrate-q)),
$t_P \approx 10$: the Riemann approximation has
$O(1/10) \approx 10\%$ relative error.  This is the scale at
which discreteness is marginally detectable — consistent with
quantum-gravitational corrections being $O(\hbar_q)$ effects.

**Julia set dynamics as the microscopic theory.**
The iteration $f_q(z) = z^2 + c(q)$ on the exceptional divisor
is the **microscopic dynamics** underlying time.  Each iterate
$f_q^{\circ n}(z_0)$ is one "microstate" of the temporal
evolution.  The continuous Reeb flow $\phi_t^q$ is the
**macroscopic** (thermodynamic) limit: it emerges from averaging
over $t_P(q)$ microscopic iterates per unit.

The Julia set $J(f_q)$ is the boundary between escaping and
bounded orbits — it partitions initial conditions into those
whose temporal evolution diverges and those that remain confined.
The Hausdorff dimension $d_H(q)$ of this boundary measures the
**complexity of the time evolution** at parameter $q$: higher
$d_H$ means the microscopic dynamics explores more of phase space
per operation, and the macroscopic time carries more information
per unit.

**Consistency with the arrow of time.**
The braiding-induced ordering $\prec_c$ on the Hecke basis
([ordering–jet compatibility](#prop:ordering-jet-compatibility))
propagates through the jet tower and defines forward/backward
time at every brane level.  The information-theoretic time
$\mathcal{T}$ is the counting measure on this well-ordering:
$\mathcal{T}(a) < \mathcal{T}(b)$ if and only if $a \prec_c b$.
The rescaling $t = \hbar_q \mathcal{T}$ preserves the order, so
the Reeb time coordinate inherits the same arrow of time.  The
arrow does not need to be re-derived in the continuous limit —
it is inherited from the discrete algebraic structure.
