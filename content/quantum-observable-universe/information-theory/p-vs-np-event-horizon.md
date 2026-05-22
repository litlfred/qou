The reformulation of $\mathrm{P}$ vs $\mathrm{NP}$ as
$\mathcal{H}_c \stackrel{?}{=} \varnothing$
([P vs NP as boundary](#conj:p-vs-np-boundary))
reveals a structural identity between **computational
complexity** and **jet horizon information loss**.  The same
jet horizon $\mathcal{H} = V(\mathfrak{h})$ that blocks
degree-$0$ photon data between aeons
([jet horizon](#def:jet-horizon)) blocks the degree-$0$
answer of an NP-complete problem at a computational boundary.

**The dictionary.**

The QOU has its own observer concept: an element of the
**observable subcategory**
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$
([observable subcategory](#def:observable-subcategory)) — a
configuration where the degree-$0$ algebra $A_0$ is
non-trivial and the Frobenius pairing is non-degenerate.
The complement ($A_0 = 0$) is the jet horizon.  The
computational analog is:

| QOU jet horizon | Computational boundary |
|----------------|----------------------|
| Observable subcategory $\mathrm{Bun}^{\circ}$ ($A_0 \neq 0$) | Polynomial observable subcategory $\mathcal{R}^{\circ}$ |
| Jet horizon $\mathcal{H} = V(\mathfrak{h})$ ($A_0 = 0$) | Computational boundary $\mathcal{H}_c = V(\mathfrak{h}_c)$ |
| Observer: object of $\mathrm{Bun}^{\circ}$ | Observer: poly-time algorithm (object of $\mathcal{R}^{\circ}$) |
| Aeon: connected component of $\mathrm{Bun}^{\circ}$ | Complexity class: connected component of $\mathcal{R}^{\circ}$ |
| Degree-$0$ opacity: no fibre value crosses $\mathcal{H}$ | Degree-$0$ opacity: no answer crosses $\mathcal{H}_c$ in poly time |
| Degree $\geq 1$ leakage: winding, curvature cross | Degree $\geq 1$ leakage: witnesses verifiable in poly time |
| Bekenstein bound: $\eta_q$ per operation | Bandwidth bound: $I(t) \leq t \cdot \mathfrak{B}(q)$ |
| Big Bang state: $A_0\rvert_{\mathcal{S}_0} = 0$ | Unsolved NP instance: degree-$0$ answer not yet extracted |

**The observer in $\mathrm{Bun}^{\circ}$ versus the
observer in $\mathcal{R}^{\circ}$.**

In the physical QOU, an observer is any configuration in the
observable subcategory — any state where $\Gamma(\mathcal{S},
A_0) \neq 0$.  The observer can perform degree-$0$ measurements
(identify particle types, read fibre values) because the
Frobenius pairing is non-degenerate on $A_0$.  At the jet
horizon, $A_0 = 0$ and the observer loses all degree-$0$
capability: it can still detect degree $\geq 1$ data (thermal
winding and curvature — the QOU realization of Hawking
radiation, [Hawking radiation](#rem:hawking-radiation)), but
cannot identify individual particles.

In the computational setting, the observer is a
polynomial-time algorithm — an object of $\mathcal{R}^{\circ}$.
It can access degree-$0$ sections (evaluate $P_L(q)$) only
from nodes within $\mathcal{R}^{\circ}$.  At the computational
boundary $\mathcal{H}_c$, the algorithm loses degree-$0$
capability: it can still verify witnesses (degree-$1$ linear
transport through the resolution tree) and detect structural
correlations (degree-$2$ curvature data), but cannot extract
the answer.

**Information flow across the boundary.**

The jet horizon leakage table
([jet horizon](#def:jet-horizon)) transfers directly:

| Jet degree | Physical (jet horizon) | Computational ($\mathcal{H}_c$) |
|:---:|---|---|
| $0$ | Fibre value — **Open** | Answer $P_L(q_0)$ — **Open** |
| $1$ | Winding number — leaks | Single witness — verifiable in $O(c)$ |
| $2$ | Curvature/linking — leaks | Pairwise path correlations — heuristically exploitable |
| $\geq 3$ | Higher topology — leaks | Higher structural data — diminishing returns |

The degree-$1$ leakage is **NP verification**: given a
resolution path (a witness), one traverses it in $O(c)$
Planck steps checking consistency at each crossing.  This is
linear transport — the first jet beyond the constant term.
It tells you *something* about the interior (that this
particular path is valid), but nothing about the global sum
$P_L(q_0)$ over all $3^c$ paths.

The degree-$2$ leakage is **heuristic computation**: pairwise
correlations between resolution paths reveal structural
properties (clause-variable correlations in SAT,
neighborhood structure in graph problems).  These are curvature
data — the second jet.  Heuristic algorithms exploit this
leakage, often successfully in practice, but without
worst-case guarantees.

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
$I = \mathrm{poly}(c) \cdot \eta_q / \hbar_q$ $q$-bits.  For
P-class problems, this suffices to determine $P_L(q_0)$ because
the effective resolution tree has polynomial size — the $3^c$
paths destructively interfere, leaving only polynomially many
survivors.

For NP-complete problems, the effective tree remains
exponential.  The computation generates $\eta_q$ $q$-bits per tick
but needs $c \cdot \log 3$ $q$-bits of aggregated information from
the full tree.  The deficit is exponential: the bandwidth
$\mathfrak{B}(q)$ cannot bridge the gap in polynomial time.

**Why $\mathcal{H}_c$ is a boundary condition, not a
resource bound.**

The standard complexity-theoretic framing treats $\mathrm{P}$
vs $\mathrm{NP}$ as a question about time resources: can
polynomial time suffice?  The QOU reformulation reveals it as
a **geometric** statement about the observable subcategory:
The interior $\mathcal{R}^{\circ}$ is either closed (P $=$ NP) or has a
non-trivial frontier $\mathcal{H}_c$ (P $\neq$ NP).

This parallels the physical jet horizon exactly:

- $\mathrm{Bun}^{\circ}$ closed (no jet horizons) would mean
  all configurations are observable — no aeon boundaries, no
  Big Bang, no information loss.  The QOU is a single
  transparent aeon.

- $\mathrm{Bun}^{\circ}$ not closed (jet horizons exist)
  means the observable subcategory has a genuine frontier —
  aeons separated by horizons, Big Bang states where $A_0 = 0$,
  degree $\geq 1$ leakage as the only cross-horizon data.

The physical QOU has jet horizons ($A_0 = 0$ at Big Bang
states).  The conjecture asserts the computational QOU also
has horizons ($\mathcal{H}_c \neq \varnothing$ for
NP-complete braids).  In both cases, the boundary is the
**vanishing locus of degree-$0$ sections** — a geometric
object, not a resource count.

**The arrow of computational time.**

The Big Bang state ([Big Bang](#def:big-bang-state)) has
$A_0|_{\mathcal{S}_0} = 0$: no degree-$0$ data.  The universe
begins outside $\mathrm{Bun}^{\circ}$ — behind its own jet
horizon.  As Planck steps accumulate, the jet tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$ builds
degree-$0$ sections, and the universe enters
$\mathrm{Bun}^{\circ}$ — it becomes observable.

Computation follows the same arrow.  A Turing machine begins
with input (degree $\geq 1$ data: the encoding of the problem)
and terminates with output (degree-$0$ data: the answer).  The
computation is the process of crossing from $\mathcal{R}
\setminus \mathcal{R}^{\circ}$ into $\mathcal{R}^{\circ}$ —
of converting degree $\geq 1$ information into degree-$0$
information, crossing the computational boundary from inside
to outside.

For P-class problems, $\mathcal{H}_c = \varnothing$:
there is no boundary to cross — the algorithm starts in
$\mathcal{R}^{\circ}$ and stays there.  For NP-complete
problems, $\mathcal{H}_c \neq \varnothing$: the
algorithm must traverse the boundary, and the exponential
depth of the resolution tree behind $\mathcal{H}_c$
is the cost of crossing.

The $\mathrm{P}$ vs $\mathrm{NP}$ question is: **does
$\mathcal{R}^{\circ}$ always equal $\mathcal{R}$, or can the
computational observable subcategory be strictly smaller than
the full resolution tree?**
