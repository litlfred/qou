<!-- FILE_START: p-vs-np-boundary-intro.md -->
The jet horizon isolates degree-$0$ data from degree $\geq 1$ leakage. The Skein Turing machine encodes every decision problem as a braid closure. We now unite these two concepts. The answer to an NP-complete decision problem is a degree-$0$ section of the resolution tree. The polynomial-time witnesses are degree-$1$ paths. The gap between them constitutes a jet horizon of purely complexity-theoretic origin.

The computational horizon construction transplants the jet-horizon onto the Skein resolution tree $\mathcal{R}(L)$ of a braid closure. The Skein resolution obstruction $\kappa_c^{\mathrm{comp}}(L, q)$ measures the obstruction to degree-$0$ evaluation via Yekutieli cohomology. Polynomial-time computation saturates the information bandwidth $\mathfrak{B}(q)$ strictly below the horizon. We cast $\mathrm{P} \neq \mathrm{NP}$ as a structural claim about jet horizon opacity. This degree-$0$ opacity parallels Hawking radiation, framing the $\mathrm{P}$ versus $\mathrm{NP}$ gap as information loss and computational irreversibility. Finally, we localize the inequality $\mathrm{P} \neq \mathrm{NP}$ at the non-torsion QOU substrate $q \in \mathbb{G}_m$.

The next section consumes the computational horizon as a discrete spectral cut-off, below which the $q$-heat kernel collapses to a Perron--Frobenius fallback. <!-- draft -->
<!-- FILE_END: p-vs-np-boundary-intro.md -->

<!-- FILE_START: computational-horizon.md -->
We define a computational horizon as a barrier where evaluation outpaces verification. 

Let $L = \hat{\beta}$ be the braid closure of a computation $\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates ([Skein Turing machine](#rem:skein-turing-machine)). The Skein resolution tree $\mathcal{R}(L)$ has $3^c$ leaves corresponding to discrete histories. The Markov trace collapses this tree to the degree-$0$ observable $P_L(q)$.

A **computational horizon** for $L$ is a jet horizon $\mathcal{H}_c \subset \mathcal{R}(L)$ exhibiting three properties:

1. **Degree-$0$ opacity.** The evaluation $P_L(q_0)$ provides the yes/no answer of the decision problem. As a degree-$0$ section of the brane tower, it cannot be extracted from any polynomial-depth subtree of $\mathcal{R}(L)$.
2. **Degree $\geq 1$ leakage.** Individual resolution paths act as witnesses. As degree-$1$ linear transport data, a single path can be verified in $O(\mathrm{poly}(c))$ Planck steps by checking consistency at each crossing.
3. **Bandwidth saturation.** The information bandwidth $\mathfrak{B}(q)$ per Planck time ([information bandwidth](#def:information-bandwidth)) restricts the sampling rate of resolution paths. If $3^c$ paths must be explored to extract the degree-$0$ answer, extracting the answer requires

   $$
     t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)}
      \cdot  3^{c - c_0}
   $$

   Planck steps whenever interference fails to reduce the effective tree size to polynomial.

The computational horizon is a concrete instance of the jet horizon ([jet horizon](#def:jet-horizon)) applied to the resolution tree. It separates degree-$0$ data (the answer) from degree $\geq 1$ data (the witnesses) by a codimension-$1$ barrier. This barrier becomes opaque when the Markov trace fails to factor the Skein polynomial into $O(\mathrm{poly}(c))$ terms.

**Structural parallel with the jet horizon.**

| Jet horizon | Computational horizon |
|-------------|----------------------|
| Degree-$0$ sections vanish on $\mathcal{H}$ | The answer $P_L(q_0)$ is inaccessible in poly time |
| Degree $\geq 1$ data leaks through | Witnesses (resolution paths) are poly-time verifiable |
| Hawking radiation: thermal, no particle identity | Partial computation: statistical correlations, no answer |
| Aeon boundary: separates observable epochs | Complexity class boundary: separates P from NP |
<!-- FILE_END: computational-horizon.md -->

<!-- FILE_START: p-bandwidth-bound.md -->
**Proposition.**
*A decision problem encoded by a link $L = \hat{\beta}$ with $c = 3N$ crossings belongs to $\mathrm{P}$ if and only if its Skein polynomial $P_L(q)$ can be evaluated (its degree-$0$ answer extracted) within*

$$
  t(c) \leq \mathfrak{B}(q)^{-1} \mathrm{poly}(c)
$$

*Planck steps, where $\mathfrak{B}(q) = q\eta_q / (q-1)^2$ is the information bandwidth per Planck time ([information bandwidth](#def:information-bandwidth)).*
<!-- FILE_END: p-bandwidth-bound.md -->

<!-- FILE_START: p-bandwidth-interpretation.md -->
The class $\mathrm{P}$ consists of those computations whose resolution trees admit sufficient destructive interference. There must be enough cancellation among the $3^c$ Skein histories that the Markov trace compresses the tree to $O(\mathrm{poly}(c))$ surviving terms. In each Planck step, the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$ iterations ([Reeb operations](#prop:reeb-operations-per-planck)). Each iteration generates $\eta_q$ $q$-bits of entropy ([operational entropy](#def:operational-entropy)). The total information budget after $t$ Planck steps is:

$$
  I(t) = t \mathfrak{B}(q) = t \frac{q\eta_q}{(q-1)^2} \quad q\text{-bits.}
$$

A $\mathrm{P}$-class computation is one where $I(\mathrm{poly}(c))$ suffices to determine $P_L(q_0)$. The full resolution tree has $3^c$ leaves carrying $c \log_2 3$ $q$-bits of raw information. However, destructive interference reduces the effective information content to $O(\mathrm{poly}(c))$ $q$-bits. This fits within the polynomial bandwidth budget.

**Three regimes.**

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| Sub-horizon (P) | Effective tree $\leq \mathrm{poly}(c)$ | Interference collapses tree; no computational horizon |
| Critical | Effective tree $= c^{O(\log c)}$ | Quasi-polynomial; horizon marginally transparent |
| Super-horizon (NP-hard) | Effective tree $= 2^{\Omega(c)}$ | Horizon opaque; bandwidth saturated exponentially |

In the sub-horizon regime, the Markov trace acts as an efficient information funnel. It channels the $3^c$ resolution paths through the degree-$0$ bottleneck in polynomial time. The computation never encounters a computational horizon: the degree-$0$ answer remains accessible from a polynomial-depth slice of the resolution tree.

In the super-horizon regime, the resolution tree retains irreducible exponential weight. The $3^c$ paths do not cancel. They carry independent information that we must aggregate to determine the degree-$0$ observable. Because the bandwidth $\mathfrak{B}(q)$ is finite per Planck step, the computation requires exponentially many steps. A computational horizon separates the answer from the observer.
<!-- FILE_END: p-bandwidth-interpretation.md -->

<!-- FILE_START: polynomial-observable-subcategory.md -->
Let $\beta$ be a braid on $n$ strands with $c$ crossings. Let $L = \hat{\beta}$ be its closure. Let $\mathcal{R}(L)$ be the Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)). Fix a polynomial bound $p(c) = c^d$.

**Definition.**
The **polynomial observable subcategory** of the resolution tree is the full sub-poset

$$
  \mathcal{R}^{\circ}(L, q)
  = 
  \bigl\{
    x \in \mathcal{R}(L)
     : 
    \Gamma_{\mathrm{poly}}\!(x, A_0) \neq 0
  \bigr\}.
$$

The set $\Gamma_{\mathrm{poly}}(x, A_0)$ consists of degree-$0$ sections at $x$ that the Markov trace computes in at most $p(c)$ Planck steps. This trace restricts to $\mathcal{R}_{p(c)}$. The poset $\mathcal{R}^{\circ}(L, q)$ forms the computational analog of the physical observable subcategory $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ ([observable subcategory](#def:observable-subcategory)). It collects the nodes of the resolution tree from which the degree-$0$ answer $P_L(q)$ is polynomial-time accessible.
<!-- FILE_END: polynomial-observable-subcategory.md -->

<!-- FILE_START: computational-boundary.md -->
Let $\mathcal{R}^{\circ}(L, q)$ be the polynomial observable subcategory of the resolution tree ([polynomial observable subcategory](#def:polynomial-observable-subcategory)).

**Definition.** We define the **computational boundary** as the frontier:

$$
  \mathcal{H}_c(L, q)
  = 
  \overline{\mathcal{R}^{\circ}}
  \setminus
  \mathcal{R}^{\circ}.
$$

Equivalently, it is the vanishing locus of the computational horizon ideal:

$$
  \mathcal{H}_c(L, q)
  = 
  V\!\bigl(\mathfrak{h}_c\bigr),
  \qquad
  \mathfrak{h}_c
  = 
  \bigl\{
    s \in \Gamma\bigl(\mathcal{R}, A_0^{\mathrm{comp}}\bigr)
     : 
    s\big|_{\mathcal{H}_c} = 0
  \bigr\}.
$$

This frontier is the locus in the resolution tree where every polynomial-time degree-$0$ section vanishes. It mirrors the jet horizon $\mathcal{H} = V(\mathfrak{h})$ ([jet horizon](#def:jet-horizon)). We simply replace the brane tower with the resolution tower, and the Frobenius algebra with the Iwahori--Hecke algebra.
<!-- FILE_END: computational-boundary.md -->

<!-- FILE_START: p-vs-np-boundary.md -->
**Setup.**
Let $\beta$ be a braid on $n$ strands with $c$ crossings. Let $L = \hat{\beta}$ be its closure, and let $\mathcal{R}(L)$ be the Skein resolution tree ([Skein Turing machine](#rem:skein-turing-machine)). We fix a polynomial bound $p(c) = c^d$. Let $\mathcal{R}^{\circ}(L, q)$ denote the polynomial observable subcategory ([polynomial observable subcategory](#def:polynomial-observable-subcategory)), and let $\mathcal{H}_c(L, q)$ denote the computational boundary ([computational boundary](#def:computational-boundary)).

**Conjecture ($\mathrm{P}$ versus $\mathrm{NP}$ as boundary emptiness).**

$$
  \boxed{
    \mathrm{P} = \mathrm{NP} \Longleftrightarrow \mathcal{H}_c(L, q) = \varnothing \text{ for every NP link } L
  }
$$

*$\mathrm{P} \neq \mathrm{NP}$ if and only if there exists an NP-complete link $L$ for which the computational horizon is non-empty:*

$$
  \mathrm{P} \neq \mathrm{NP} \Longleftrightarrow \exists L \text{ (NP-complete)} \text{ with } \mathcal{H}_c(L, q) \neq \varnothing.
$$

**The formal conjecture.**
*For the QOU at substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$ (non-torsion, [substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)):*

*There exists a family of braids $\{L_N = \hat{\beta}_N\}_{N \geq 1}$ with $c_N = 3N$ crossings encoding an NP-complete problem \cite{cook1971} such that:*

$$
  \mathcal{H}_c(L_N, q_0) \neq \varnothing \qquad \text{for all } N \geq N_0.
$$

*The computational boundary is non-empty. A genuine event horizon exists in the resolution tree, meaning $\mathrm{P} \neq \mathrm{NP}$ over $\mathbb{R}$ at $q = q_0$ \cite{freedman2003}.*
<!-- FILE_END: p-vs-np-boundary.md -->

<!-- FILE_START: p-vs-np-boundary-interpretation.md -->
**Geometric meaning of each case.**

* **$\mathcal{H}_c = \varnothing$** (P = NP):
  The polynomial observable subcategory $\mathcal{R}^{\circ}$
  is **closed** — it equals its own closure.  Every degree-$0$
  section that exists anywhere in $\mathcal{R}$ already extends
  to polynomial depth.  The computational horizon ideal is
  trivial: $\mathfrak{h}_c = (0)$.  No
  information barrier separates the polynomial slice from the
  full tree.  The resolution tree has no genuine boundary — it
  is a **removable singularity**.

* **$\mathcal{H}_c \neq \varnothing$** (P $\neq$ NP):
  The polynomial observable subcategory $\mathcal{R}^{\circ}$
  is **not closed** — its closure includes points beyond
  polynomial depth.  There exists a non-trivial computational
  boundary: a codimension-$1$ locus where degree-$0$ sections
  vanish.  The horizon ideal
  $\mathfrak{h}_c \neq (0)$ contains non-zero
  sections — polynomial-time algorithms that reach the boundary
  and return $0$.  The resolution tree has a genuine event
  horizon — an **essential singularity**.

**Parallel with the jet horizon and NS obstruction.**

See [Table 1](#tbl:p-vs-np-boundary-table1-data).

**The three equivalent criteria for $\mathcal{H}_c
\neq \varnothing$.**

1. **Ideal-theoretic.**  The horizon ideal is non-trivial:
   $\mathfrak{h}_c \neq (0)$.  There exist
   polynomial-time algorithms that attempt to compute
   $P_L(q_0)$ and return $0$ — they reach the boundary
   and find no degree-$0$ data.

2. **Cohomological.**  The Skein resolution obstruction
   $\kappa_c^{\mathrm{comp}}(L, q) \neq 0$
   ([Skein resolution obstruction](#def:skein-resolution-obstruction)).
   The Yekutieli class obstructs the lift from polynomial
   depth to full resolution.

3. **Information-theoretic.**  The effective tree size after
   interference exceeds the polynomial bandwidth budget
   ([bandwidth bound](#prop:p-bandwidth-bound)):
   $I(\mathrm{poly}(c)) < c \cdot \log 3$ $q$-bits.

All three are equivalent: the ideal is non-trivial iff the
obstruction class is non-vanishing iff the bandwidth is
saturated.

**Connection to quantum computation.**

The :refterm[descent]{#descent} involution $\hat{\tau}$
([quantum universality](#conj:quantum-computational-universality))
acts on the boundary.  At a root of unity $q_k$:

$$
  \mathcal{H}_c(L, q_k)
  = 
  \mathcal{H}_c^{\mathrm{desc}}
  \cup
  \mathcal{H}_c^{\mathrm{trans}}.
$$

The descended boundary $\mathcal{H}_c^{\mathrm{desc}}$
is the classical horizon (opaque at real $q$).  The transient
boundary $\mathcal{H}_c^{\mathrm{trans}}$ is the
quantum correction.  For BQP problems:
$\mathcal{H}_c^{\mathrm{trans}} =
-\mathcal{H}_c^{\mathrm{desc}}$ (exact cancellation),
giving $\mathcal{H}_c = \varnothing$ at the root of
unity — the boundary dissolves under quantum interference.

The standard complexity hierarchy translates to:

See [Table 2](#tbl:p-vs-np-boundary-table2-data).
<!-- FILE_END: p-vs-np-boundary-interpretation.md -->

<!-- FILE_START: p-vs-np-event-horizon.md -->
We establish a structural identity between computational complexity and jet horizon information loss. The reformulation of $\mathrm{P}$ vs $\mathrm{NP}$ as $\mathcal{H}_c \stackrel{?}{=} \varnothing$ ([P vs NP as boundary](#prop:p-vs-np-boundary)) equates the computational boundary with a jet horizon. The same horizon $\mathcal{H} = V(\mathfrak{h})$ that blocks degree-$0$ photon data between aeons ([jet horizon](#def:jet-horizon)) blocks the degree-$0$ answer of an NP-complete problem.

**The dictionary.**

The QOU observer is an element of the observable subcategory $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ ([observable subcategory](#def:observable-subcategory)). In this configuration, the degree-$0$ algebra $A_0$ is non-trivial and the Frobenius pairing is non-degenerate. The complement ($A_0 = 0$) is the jet horizon. The computational analog maps directly to this geometry.

See [Table 1](#tbl:p-vs-np-event-horizon-table1-data).

**The observer in $\mathrm{Bun}^{\circ}$ versus the observer in $\mathcal{R}^{\circ}$.**

In the physical QOU, an observer is any configuration in the observable subcategory. This requires $\Gamma(\mathcal{S}, A_0) \neq 0$. The observer performs degree-$0$ measurements (identifying particle types, reading fibre values) because the Frobenius pairing is non-degenerate on $A_0$. At the jet horizon, $A_0 = 0$. The observer loses all degree-$0$ capability. It still detects degree $\geq 1$ data, such as thermal winding and curvature. This is the QOU realization of Hawking radiation ([Hawking radiation](#rem:hawking-radiation)). However, it cannot identify individual particles.

In the computational setting, the observer is a polynomial-time algorithm, an object of $\mathcal{R}^{\circ}$. It accesses degree-$0$ sections, evaluating $P_L(q)$, only from nodes within $\mathcal{R}^{\circ}$. At the computational boundary $\mathcal{H}_c$, the algorithm loses degree-$0$ capability. It still verifies witnesses via degree-$1$ linear transport through the resolution tree. It still detects structural correlations via degree-$2$ curvature data. It cannot extract the answer.

**Information flow across the boundary.**

The jet horizon leakage table ([jet horizon](#def:jet-horizon)) transfers directly to computation.

See [Table 2](#tbl:p-vs-np-event-horizon-table2-data).

The degree-$1$ leakage is NP verification. Given a resolution path (a witness), we traverse it in $O(c)$ Planck steps, checking consistency at each crossing. This is linear transport. It represents the first jet beyond the constant term. It proves a specific path is valid, but reveals nothing about the global sum $P_L(q_0)$ over all $3^c$ paths.

The degree-$2$ leakage is heuristic computation. Pairwise correlations between resolution paths reveal structural properties, such as clause-variable correlations in SAT or neighborhood structure in graph problems. These represent curvature data, the second jet. Heuristic algorithms exploit this leakage. They operate without worst-case guarantees.

**The Planck step as the tick of a Turing machine.**

Each application of the $q$-connection $\nabla_q$ is one Planck step ([jet-Planck steps](#rem:jet-planck-steps)). In the computational setting, this is one step of a Turing machine: one crossing resolved, one gate applied, one discrete clock tick. The Planck time $t_P(q) = q/(q-1)$ sets the fundamental clock rate. The operational entropy $\eta_q$ ([operational entropy](#def:operational-entropy)) sets the information generated per tick.

A polynomial-time computation runs for $\mathrm{poly}(c)$ ticks. The total information processed is $I = \mathrm{poly}(c) \cdot \eta_q / \hbar_q$ $q$-bits. For P-class problems, this suffices to determine $P_L(q_0)$. The effective resolution tree has polynomial size, because the $3^c$ paths destructively interfere to leave only polynomially many survivors.

For NP-complete problems, the effective tree remains exponential. The computation generates $\eta_q$ $q$-bits per tick but requires $c \cdot \log 3$ $q$-bits of aggregated information from the full tree. The deficit is exponential. The bandwidth $\mathfrak{B}(q)$ cannot bridge this gap in polynomial time.

**Boundary condition versus resource bound.**

Standard complexity theory treats $\mathrm{P}$ vs $\mathrm{NP}$ as a question of time resources. The QOU reformulation treats it as a geometric statement about the observable subcategory. The interior $\mathcal{R}^{\circ}$ is either closed (P $=$ NP) or has a non-trivial frontier $\mathcal{H}_c$ (P $\neq$ NP).

This parallels the physical jet horizon. If $\mathrm{Bun}^{\circ}$ is closed, there are no jet horizons. All configurations are observable. There are no aeon boundaries, no Big Bang, and no information loss. The QOU is a single transparent aeon. If $\mathrm{Bun}^{\circ}$ is not closed, jet horizons exist. The observable subcategory has a genuine frontier. Aeons are separated by horizons, Big Bang states have $A_0 = 0$, and degree $\geq 1$ leakage is the only cross-horizon data.

The physical QOU has jet horizons. The conjecture asserts the computational QOU also has horizons, where $\mathcal{H}_c \neq \varnothing$ for NP-complete braids. In both cases, the boundary is the vanishing locus of degree-$0$ sections. This is a geometric object, not a resource count.

**The arrow of computational time.**

The Big Bang state ([Big Bang](#def:big-bang-state)) has $A_0|_{\mathcal{S}_0} = 0$. It contains no degree-$0$ data. The universe begins outside $\mathrm{Bun}^{\circ}$, behind its own jet horizon. As Planck steps accumulate, the jet tower $A_0 \hookrightarrow A_1 \hookrightarrow \cdots$ builds degree-$0$ sections. The universe enters $\mathrm{Bun}^{\circ}$ and becomes observable.

Computation follows the same arrow. A Turing machine begins with input: degree $\geq 1$ data encoding the problem. It terminates with output: degree-$0$ data providing the answer. The computation crosses from $\mathcal{R} \setminus \mathcal{R}^{\circ}$ into $\mathcal{R}^{\circ}$. It converts degree $\geq 1$ information into degree-$0$ information, crossing the computational boundary from inside to outside.

For P-class problems, $\mathcal{H}_c = \varnothing$. There is no boundary to cross. The algorithm starts in $\mathcal{R}^{\circ}$ and stays there. For NP-complete problems, $\mathcal{H}_c \neq \varnothing$. The algorithm must traverse the boundary. The exponential depth of the resolution tree behind $\mathcal{H}_c$ is the cost of crossing.

The $\mathrm{P}$ vs $\mathrm{NP}$ question is geometric: does $\mathcal{R}^{\circ}$ always equal $\mathcal{R}$, or is the computational observable subcategory strictly smaller than the full resolution tree?
<!-- FILE_END: p-vs-np-event-horizon.md -->

<!-- FILE_START: qou-p-neq-np.md -->
**Conjecture.**
*At the physical substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$ ([substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)), $\mathrm{P} \neq \mathrm{NP}$.*

*Equivalently, the resolution-tree evaluation of the universal obstruction class $\chi(A)$ is non-vanishing:*

$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0
  \qquad\text{at } q = q_0.
$$

**The fourth millennium evaluation.** The [QOU obstruction reduction](#thm:qou-obstruction-reduction) establishes that all classical-limit obstructions in the QOU are images of the single scalar class $\chi(A) \in HH^2 \cong k$. P vs NP joins RH, NS, and BSD as a fourth restriction of the same class via the resolution-tree evaluation map. All four evaluations are proportional and controlled by $\chi(A) = -6$.

**The $\mathbb{G}_m$-torsion dichotomy.** When $q$ is a root of unity (torsion), the Iwahori--Hecke algebra $H_n(q)$ acquires a non-trivial radical. This radical annihilates exponentially many resolution paths and prunes the tree to polynomial effective size. This regime corresponds to BQP. The computational horizon becomes transparent.

When $q$ is non-torsion (including the physical $q_0$), the Iwahori--Hecke algebra is semisimple ($\mathrm{Rad} = 0$). No paths are pruned. The full $3^c$ resolution tree survives. The computational horizon $\mathcal{H}_c(L, q_0) \neq \varnothing$ strictly blocks NP-complete links.

**Kummer persistence.** The Kummer filtration ([Kummer filtration](#rem:kummer-filtration-obstruction)) gives $\kappa_c^{\mathrm{comp}} \bmod n = 0$ if and only if $n \mid 6$. Since $q_0$ is non-torsion ($q_0^k \neq 1$ for all $k \geq 1$), no finite Kummer level applies. The obstruction is perpetual.

**Corollary (from the reduction theorem).** A resolution of P vs NP (in either direction) tightly constrains the other three millennium problems. Conversely, a resolution of RH, NS, or BSD constrains P vs NP. The evaluation maps differ, but the underlying obstruction class is identical.
<!-- FILE_END: qou-p-neq-np.md -->

