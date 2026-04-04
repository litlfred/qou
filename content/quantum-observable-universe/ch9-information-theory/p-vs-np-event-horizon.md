The reformulation of $\mathrm{P}$ vs $\mathrm{NP}$ as a
boundary condition
([P $\neq$ NP as jet horizon opacity](#conj:p-vs-np-boundary))
reveals a structural identity between **computational
complexity** and **gravitational information loss**.  The same
jet horizon that blocks degree-$0$ photon data at a black hole
boundary ([jet horizon](#def:jet-horizon)) blocks the degree-$0$
answer of an NP-complete problem at a computational boundary.

**The dictionary.**

| Black hole physics | Computational complexity |
|--------------------|------------------------|
| Infalling matter (full quantum state) | Input + witness (full resolution tree) |
| Schwarzschild horizon $\mathcal{H}$ | Computational horizon $\mathcal{H}_c$ |
| Exterior observer | Polynomial-time algorithm |
| Degree-$0$ opacity: no photon identity crosses | Degree-$0$ opacity: no answer in poly time |
| Hawking radiation (degree $\geq 1$ thermal data) | Partial computation (degree $\geq 1$ witness verification) |
| Bekenstein bound: $S \leq 2\pi RE/\hbar c$ | Bandwidth bound: $I(t) \leq t \cdot \mathcal{B}(q)$ |
| Information paradox: is infalling data recoverable? | P vs NP: is the answer efficiently recoverable? |
| Planck-scale discreteness resolves the paradox | Planck-step discreteness defines the complexity |

**Information flow at the computational horizon.**

Consider an NP-complete problem encoded as a braid $\beta$ with
$c$ crossings.  The resolution tree $\mathcal{R}(L)$ is the
computational interior — the full space of $3^c$ histories
([Skein Turing machine](#rem:skein-turing-machine)).  A
polynomial-time algorithm is an exterior observer: it can
access $\mathrm{poly}(c)$ resolution paths per Planck step,
bounded by the information bandwidth $\mathcal{B}(q)$
([information bandwidth](#prop:information-speed-of-light)).

The information flow across the computational horizon mirrors
the jet horizon precisely:

1. **Degree-$0$ (the answer).**  The evaluation $P_L(q_0)$
   is a global property of the resolution tree — it depends
   on all $3^c$ paths, weighted by their Skein signs.  Just as
   a photon's identity (degree-$0$ fibre value) cannot cross
   the jet horizon, the answer cannot cross the computational
   horizon in polynomial time.

2. **Degree $\geq 1$ (witness verification).**  A single
   resolution path is degree-$1$ data: linear transport through
   the tree.  It crosses the horizon freely — this is NP
   verification.  Given a witness (a specific path through the
   tree), one checks in $O(c)$ Planck steps that each crossing
   is consistently resolved.  This is Hawking radiation: thermal
   data with no particle identity.  The witness tells you
   *something* about the interior, but not the answer.

3. **Degree $\geq 2$ (structural correlations).**  Pairwise
   correlations between resolution paths — curvature data —
   also leak through.  This corresponds to heuristic algorithms
   that exploit structural properties of the problem (e.g.,
   clause-variable correlations in SAT).  They extract more
   than a single witness but less than the full answer.

**The Planck step as the tick of a Turing machine.**

Each application of the $q$-connection $\nabla_q$ is one Planck
step ([jet-Planck steps](#rem:jet-planck-steps)).  In the
computational setting, this is one step of a Turing machine:
one crossing resolved, one gate applied, one tick of the
discrete clock.  The Planck time $t_P(q) = q/(q-1)$ sets the
fundamental clock rate; the operational entropy $\eta_q$
([operational entropy](#def:operational-entropy)) sets the
information generated per tick.

A polynomial-time computation runs for $\mathrm{poly}(c)$ ticks.
The total information processed is
$I = \mathrm{poly}(c) \cdot \eta_q / \hbar_q$ nats.  For
P-class problems, this suffices to determine $P_L(q_0)$ because
the effective resolution tree has polynomial size — the $3^c$
paths destructively interfere, leaving only polynomially many
survivors.

For NP-complete problems, the effective tree remains
exponential.  The computation generates $\eta_q$ nats per tick
but needs $c \cdot \log 3$ nats of aggregated information from
the full tree.  The deficit is exponential: the bandwidth
$\mathcal{B}(q)$ cannot bridge the gap in polynomial time.

**Why this is a boundary condition, not just a resource bound.**

The standard complexity-theoretic framing treats $\mathrm{P}$
vs $\mathrm{NP}$ as a question about time resources: can
polynomial time suffice?  The QOU reformulation reveals it as
a **geometric** statement: the computational horizon is a
codimension-$1$ surface in the resolution tree, and $\mathrm{P}
\neq \mathrm{NP}$ asserts that this surface is a genuine
boundary — not a removable singularity.

The analogy is exact:

- A **removable singularity** in complex analysis is a point
  where a function appears undefined but can be continuously
  extended.  If $\mathrm{P} = \mathrm{NP}$, every computational
  horizon is removable: the degree-$0$ answer can be
  continuously extended from the polynomial-depth slice.

- A **genuine singularity** is a point where no continuous
  extension exists.  If $\mathrm{P} \neq \mathrm{NP}$, some
  computational horizons are genuine: the degree-$0$ answer
  has an essential discontinuity at polynomial depth.

The jet horizon formalism makes this precise.  The vanishing
ideal $\mathfrak{h} = \{s \in \Gamma(U, A_0) : s|_{\mathcal{H}} = 0\}$
is the set of degree-$0$ sections that extend to the horizon
and vanish.  For a computational horizon, this is the set of
polynomial-time algorithms that *attempt* to compute $P_L(q_0)$
but return $0$ — they reach the horizon and find no degree-$0$
data.  The non-emptiness of $\mathfrak{h}$ (the existence of
NP-complete problems) is the assertion that the horizon is real.

**The arrow of computational time.**

The Big Bang state ([Big Bang](#def:big-bang-state)) has
$A_0|_{\mathcal{S}_0} = 0$: no degree-$0$ data.  The universe
begins behind its own jet horizon.  As Planck steps accumulate,
the jet tower $A_0 \hookrightarrow A_1 \hookrightarrow \cdots$
builds degree-$0$ sections — the universe becomes observable.

Computation follows the same arrow.  A Turing machine begins
with input (degree $\geq 1$ data: the encoding of the problem)
and terminates with output (degree-$0$ data: the answer).  The
computation is the process of converting degree $\geq 1$
information into degree-$0$ information — of crossing the
computational horizon from inside to outside.

For P-class problems, this crossing takes polynomial time: the
horizon is thin, and the information funnel (the Markov trace)
is efficient.  For NP-complete problems, the crossing takes
exponential time: the horizon is thick, and the information
must traverse an exponentially deep interior before reaching
the degree-$0$ exterior.

The $\mathrm{P}$ vs $\mathrm{NP}$ question is: **does every
computation eventually cross its horizon, or are some horizons
so thick that no polynomial-time process can traverse them?**
The jet horizon formalism answers: the thickness of the horizon
is the effective depth of the resolution tree after
interference, and $\mathrm{P} \neq \mathrm{NP}$ is the
assertion that some resolution trees have irreducibly
exponential depth.
