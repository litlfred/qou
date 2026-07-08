<!-- FILE_START: p-vs-np-boundary-intro.md -->
The jet horizon isolates degree-$0$ data from degree $\geq 1$ leakage. Concurrently, the Skein Turing machine encodes every decision problem as a braid closure. Uniting these concepts maps the answer of an NP-complete decision problem to a degree-$0$ section of the resolution tree, while polynomial-time witnesses correspond to degree-$1$ paths. The gap between them constitutes a jet horizon of purely complexity-theoretic origin.

Transplanting the jet horizon onto the Skein resolution tree $\mathcal{R}(L)$ defines the computational horizon. The Skein resolution obstruction $\kappa_c^{\mathrm{comp}}(L, q)$ measures the obstruction to degree-$0$ evaluation via Yekutieli cohomology. Polynomial-time computation saturates the information bandwidth $\mathfrak{B}(q)$ strictly below this horizon. This casts $\mathrm{P} \neq \mathrm{NP}$ as a structural claim regarding jet horizon opacity. Such degree-$0$ opacity parallels Hawking radiation, framing the $\mathrm{P}$ versus $\mathrm{NP}$ gap as information loss and computational irreversibility. This inequality localizes strictly at the non-torsion QOU substrate $q \in \mathbb{G}_m$.
<!-- FILE_END: p-vs-np-boundary-intro.md -->

<!-- FILE_START: computational-horizon.md -->
A computational horizon is a barrier where evaluation outpaces verification. 

Let $L = \hat{\beta}$ be the braid closure of a computation $\beta$ with $c = 3N$ crossings encoding $N$ Toffoli gates. The Skein resolution tree $\mathcal{R}(L)$ contains $3^c$ leaves representing discrete histories. The Markov trace collapses this tree to the degree-$0$ observable $P_L(q)$.

A **computational horizon** for $L$ is a jet horizon $\mathcal{H}_c \subset \mathcal{R}(L)$ exhibiting three properties:

1. **Degree-$0$ opacity.** The evaluation $P_L(q_0)$ provides the yes/no answer of the decision problem. As a degree-$0$ section of the brane tower, it resists extraction from any polynomial-depth subtree of $\mathcal{R}(L)$.
2. **Degree $\geq 1$ leakage.** Individual resolution paths furnish witnesses. As degree-$1$ linear transport data, a single path admits verification in $O(\mathrm{poly}(c))$ Planck steps by checking crossing consistencies.
3. **Bandwidth saturation.** The information bandwidth $\mathfrak{B}(q)$ per Planck time restricts the sampling rate. If extracting the degree-$0$ answer requires exploring all $3^c$ paths, the extraction demands
$$
  t  \geq  \frac{c \cdot \log 3}{\mathfrak{B}(q)} \cdot  3^{c - c_0}
$$
Planck steps whenever interference fails to bound the effective tree size polynomially.

The computational horizon applies the jet horizon directly to the resolution tree. It separates the degree-$0$ answer from the degree $\geq 1$ witnesses via a codimension-$1$ barrier. This barrier turns opaque when the Markov trace fails to factor the Skein polynomial into $O(\mathrm{poly}(c))$ terms.

**Structural parallel with the jet horizon.**

| Jet horizon | Computational horizon |
|-------------|----------------------|
| Degree-$0$ sections vanish on $\mathcal{H}$ | The answer $P_L(q_0)$ is inaccessible in poly time |
| Degree $\geq 1$ data leaks through | Witnesses (resolution paths) are poly-time verifiable |
| Hawking radiation: thermal, no particle identity | Partial computation: statistical correlations, no answer |
| Aeon boundary: separates observable epochs | Complexity class boundary: separates P from NP |
<!-- FILE_END: computational-horizon.md -->

<!-- FILE_START: p-bandwidth-bound.md -->
A decision problem encoded by a link $L = \hat{\beta}$ with $c = 3N$ crossings belongs to $\mathrm{P}$ if and only if its Skein polynomial $P_L(q)$ can be evaluated (its degree-$0$ answer extracted) within
$$
  t(c) \leq \mathfrak{B}(q)^{-1} \mathrm{poly}(c)
$$
Planck steps, where $\mathfrak{B}(q) = q\eta_q / (q-1)^2$ is the information bandwidth per Planck time.
<!-- FILE_END: p-bandwidth-bound.md -->

<!-- FILE_START: p-bandwidth-interpretation.md -->
The class $\mathrm{P}$ consists of computations whose resolution trees exhibit sufficient destructive interference. Cancellation among the $3^c$ Skein histories allows the Markov trace to compress the tree to $O(\mathrm{poly}(c))$ surviving terms. In each Planck step, the $q$-connection $\nabla_q$ processes $n_R(q) = 1/\hbar_q$ iterations. Each iteration generates $\eta_q$ $q$-bits of entropy. After $t$ Planck steps, the total information budget is:
$$
  I(t) = t \mathfrak{B}(q) = t \frac{q\eta_q}{(q-1)^2} \quad q\text{-bits.}
$$

A $\mathrm{P}$-class computation succeeds when $I(\mathrm{poly}(c))$ suffices to determine $P_L(q_0)$. Although the full resolution tree carries $c \log_2 3$ $q$-bits of raw information, destructive interference limits the effective content to $O(\mathrm{poly}(c))$ $q$-bits, fitting within the polynomial budget.

**Three regimes.**

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| Sub-horizon (P) | Effective tree $\leq \mathrm{poly}(c)$ | Interference collapses tree; no computational horizon |
| Critical | Effective tree $= c^{O(\log c)}$ | Quasi-polynomial; horizon marginally transparent |
| Super-horizon (NP-hard) | Effective tree $= 2^{\Omega(c)}$ | Horizon opaque; bandwidth saturated exponentially |

In the sub-horizon regime, the Markov trace funnels the $3^c$ paths through the degree-$0$ bottleneck in polynomial time. The computation avoids any computational horizon; the answer remains accessible from a polynomial-depth subtree.

In the super-horizon regime, the resolution tree retains irreducible exponential weight. The uncancelled paths carry independent information requiring full aggregation. Because the bandwidth $\mathfrak{B}(q)$ per Planck step is finite, this demands exponentially many steps. A computational horizon strictly separates the answer from the observer.
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
Let $\mathcal{R}^{\circ}(L, q)$ be the polynomial observable subcategory of the resolution tree.

**Definition.** The **computational boundary** is the frontier:
$$
  \mathcal{H}_c(L, q) = \overline{\mathcal{R}^{\circ}} \setminus \mathcal{R}^{\circ}.
$$

Equivalently, it constitutes the vanishing locus of the computational horizon ideal:
$$
  \mathcal{H}_c(L, q) = V\!\bigl(\mathfrak{h}_c\bigr), \qquad
  \mathfrak{h}_c = \bigl\{ s \in \Gamma\bigl(\mathcal{R}, A_0^{\mathrm{comp}}\bigr) : s\big|_{\mathcal{H}_c} = 0 \bigr\}.
$$

This frontier defines the locus in the resolution tree where every polynomial-time degree-$0$ section vanishes. It structurally mirrors the jet horizon $\mathcal{H} = V(\mathfrak{h})$, substituting the resolution tower for the brane tower and the Iwahori--Hecke algebra for the Frobenius algebra.
<!-- FILE_END: computational-boundary.md -->

<!-- FILE_START: p-vs-np-boundary.md -->
**Conjecture ($\mathrm{P}$ versus $\mathrm{NP}$ as boundary emptiness).**
Let $L = \hat{\beta}$ be the closure of a braid $\beta$ encoding a decision problem. Let $\mathcal{H}_c(L, q)$ denote its computational boundary.
$$
  \mathrm{P} = \mathrm{NP} \Longleftrightarrow \mathcal{H}_c(L, q) = \varnothing \text{ for every NP link } L
$$
Consequently, $\mathrm{P} \neq \mathrm{NP}$ if and only if there exists an NP-complete link $L$ carrying a non-empty computational horizon:
$$
  \mathrm{P} \neq \mathrm{NP} \Longleftrightarrow \exists L \text{ (NP-complete)} \text{ with } \mathcal{H}_c(L, q) \neq \varnothing.
$$

**The formal conjecture.**
For the QOU at a non-torsion substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$, there exists a family of braids $\{L_N = \hat{\beta}_N\}_{N \geq 1}$ with $c_N = 3N$ crossings encoding an NP-complete problem such that:
$$
  \mathcal{H}_c(L_N, q_0) \neq \varnothing \qquad \text{for all } N \geq N_0.
$$
This non-empty boundary establishes a genuine event horizon within the resolution tree, implying $\mathrm{P} \neq \mathrm{NP}$ over $\mathbb{R}$ at $q = q_0$.
<!-- FILE_END: p-vs-np-boundary.md -->

<!-- FILE_START: p-vs-np-boundary-interpretation.md -->
**Geometric meaning of each case.**

* **$\mathcal{H}_c = \varnothing$** (P = NP): The polynomial observable subcategory $\mathcal{R}^{\circ}$ is closed. Every degree-$0$ section existing in $\mathcal{R}$ already extends to polynomial depth. The computational horizon ideal vanishes: $\mathfrak{h}_c = (0)$. No information barrier separates the polynomial slice from the full tree. The resolution tree exhibits no genuine boundary; it harbors a removable singularity.
* **$\mathcal{H}_c \neq \varnothing$** (P $\neq$ NP): The polynomial observable subcategory $\mathcal{R}^{\circ}$ is not closed. A non-trivial computational boundary manifests as a codimension-$1$ locus where degree-$0$ sections vanish. The horizon ideal $\mathfrak{h}_c \neq (0)$ captures polynomial-time algorithms that reach the boundary and return $0$. The resolution tree exhibits a genuine event horizon, forming an essential singularity.

**Parallel with the jet horizon and NS obstruction.**
See [Table 1](#tbl:p-vs-np-boundary-table1-data).

**The three equivalent criteria for $\mathcal{H}_c \neq \varnothing$.**

1. **Ideal-theoretic.** The horizon ideal is non-trivial: $\mathfrak{h}_c \neq (0)$. Polynomial-time algorithms evaluate to $0$ on the boundary.
2. **Cohomological.** The Skein resolution obstruction class does not vanish: $\kappa_c^{\mathrm{comp}}(L, q) \neq 0$. This Yekutieli class obstructs the lift from polynomial depth to full resolution.
3. **Information-theoretic.** The effective tree size, after interference, strictly exceeds the polynomial bandwidth budget: $I(\mathrm{poly}(c)) < c \cdot \log 3$ $q$-bits.

**Connection to quantum computation.**
The descent involution $\hat{\tau}$ acts directly on the boundary. At a root of unity $q_k$:
$$
  \mathcal{H}_c(L, q_k) = \mathcal{H}_c^{\mathrm{desc}} \cup \mathcal{H}_c^{\mathrm{trans}}.
$$
The descended boundary $\mathcal{H}_c^{\mathrm{desc}}$ constitutes the classical horizon, remaining opaque at real $q$. The transient boundary $\mathcal{H}_c^{\mathrm{trans}}$ supplies the quantum correction. For BQP problems, exact cancellation occurs: $\mathcal{H}_c^{\mathrm{trans}} = -\mathcal{H}_c^{\mathrm{desc}}$. This yields $\mathcal{H}_c = \varnothing$ at the root of unity. The boundary completely dissolves under quantum interference.

The standard complexity hierarchy translates to:
See [Table 2](#tbl:p-vs-np-boundary-table2-data).
<!-- FILE_END: p-vs-np-boundary-interpretation.md -->

<!-- FILE_START: p-vs-np-event-horizon.md -->
We formally establish a structural identity between computational complexity and jet horizon information loss. Reformulating $\mathrm{P}$ vs $\mathrm{NP}$ as the boundary condition $\mathcal{H}_c \stackrel{?}{=} \varnothing$ strictly equates the computational boundary with a jet horizon. The identical horizon geometry $\mathcal{H} = V(\mathfrak{h})$ that blocks degree-$0$ photon data between aeons simultaneously blocks the degree-$0$ answer of an NP-complete problem.

**The dictionary.**
The physical QOU observer corresponds to an element of the observable subcategory $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$. Here, the degree-$0$ algebra $A_0$ is non-trivial and the Frobenius pairing is non-degenerate. The complement ($A_0 = 0$) defines the jet horizon. The computational analog maps directly onto this geometry.
See [Table 1](#tbl:p-vs-np-event-horizon-table1-data).

**The observer in $\mathrm{Bun}^{\circ}$ versus the observer in $\mathcal{R}^{\circ}$.**
In the physical QOU, observation requires $\Gamma(\mathcal{S}, A_0) \neq 0$. The observer performs degree-$0$ measurements because the Frobenius pairing is non-degenerate on $A_0$. At the jet horizon, $A_0 = 0$. The observer loses all degree-$0$ capability. It still detects degree $\geq 1$ data, capturing thermal winding and curvature as Hawking radiation, but it cannot identify individual particles.

In the computational setting, the observer is a polynomial-time algorithm inhabiting $\mathcal{R}^{\circ}$. It accesses degree-$0$ sections, evaluating $P_L(q)$, strictly from nodes within $\mathcal{R}^{\circ}$. At the computational boundary $\mathcal{H}_c$, the algorithm loses degree-$0$ capability. It retains the ability to verify witnesses via degree-$1$ linear transport and detect structural correlations via degree-$2$ curvature data, but it cannot extract the answer.

**Information flow across the boundary.**
The jet horizon leakage table applies directly to computation.
See [Table 2](#tbl:p-vs-np-event-horizon-table2-data).

The degree-$1$ leakage embodies NP verification. Traversing a resolution path in $O(c)$ Planck steps constitutes linear transport. It represents the first jet beyond the constant term. This checks consistency but reveals nothing concerning the global sum $P_L(q_0)$. The degree-$2$ leakage embodies heuristic computation. Pairwise correlations between resolution paths reveal structural properties like clause-variable correlations. Heuristic algorithms exploit this curvature leakage without worst-case guarantees.

**The Planck step as the tick of a Turing machine.**
Each application of the $q$-connection $\nabla_q$ constitutes one Planck step. In the computational setting, this mirrors one discrete clock tick of a Turing machine. The Planck time $t_P(q) = q/(q-1)$ sets the fundamental clock rate. The operational entropy $\eta_q$ sets the information generated per tick.

A polynomial-time computation generates $I = \mathrm{poly}(c) \cdot \eta_q / \hbar_q$ $q$-bits. For P-class problems, this suffices. Destructive interference collapses the effective resolution tree to polynomial size. For NP-complete problems, the effective tree retains exponential size. The computation generates polynomial $q$-bits but demands exponential $q$-bits of aggregated information. The bandwidth $\mathfrak{B}(q)$ cannot bridge this deficit in polynomial time.

**Boundary condition versus resource bound.**
Standard complexity theory evaluates $\mathrm{P}$ vs $\mathrm{NP}$ as a resource bound. The QOU translates this to a geometric statement: the interior $\mathcal{R}^{\circ}$ is either closed (P $=$ NP) or carries a non-trivial frontier $\mathcal{H}_c$ (P $\neq$ NP).

This identically matches the physical jet horizon. If $\mathrm{Bun}^{\circ}$ is closed, no jet horizons exist. The universe operates as a single transparent aeon without information loss. If $\mathrm{Bun}^{\circ}$ is not closed, genuine frontiers exist. The physical QOU structurally possesses jet horizons. The conjecture asserts the computational QOU similarly possesses horizons, with $\mathcal{H}_c \neq \varnothing$ for NP-complete braids.

**The arrow of computational time.**
The Big Bang state initiates with $A_0|_{\mathcal{S}_0} = 0$. The universe begins outside $\mathrm{Bun}^{\circ}$, behind its own jet horizon. As Planck steps accumulate, the jet tower builds degree-$0$ sections, moving the universe into $\mathrm{Bun}^{\circ}$.

Computation mirrors this geometric arrow. A Turing machine begins with degree $\geq 1$ input data. It terminates with degree-$0$ output data. The computation traverses from $\mathcal{R} \setminus \mathcal{R}^{\circ}$ into $\mathcal{R}^{\circ}$. For P-class problems, $\mathcal{H}_c = \varnothing$. The algorithm starts in $\mathcal{R}^{\circ}$ and never leaves. For NP-complete problems, $\mathcal{H}_c \neq \varnothing$. The algorithm must forcefully cross the boundary, paying the exponential depth of the resolution tree as the crossing cost. The $\mathrm{P}$ vs $\mathrm{NP}$ question is entirely geometric: does the computational observable subcategory perfectly cover the full resolution tree?
<!-- FILE_END: p-vs-np-event-horizon.md -->

<!-- FILE_START: qou-p-neq-np.md -->
**Conjecture.** At the physical non-torsion substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$, we have $\mathrm{P} \neq \mathrm{NP}$. Equivalently, the resolution-tree evaluation of the universal obstruction class $\chi(A)$ is non-vanishing:
$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0 \qquad\text{at } q = q_0.
$$

**The fourth millennium evaluation.** The QOU obstruction reduction establishes that all classical-limit obstructions map to the scalar class $\chi(A) \in HH^2 \cong k$. Consequently, $\mathrm{P}$ vs $\mathrm{NP}$ acts as a fourth restriction of the same class alongside RH, NS, and BSD. All four evaluations are structurally proportional.

**The $\mathbb{G}_m$-torsion dichotomy.** When $q$ is a torsion root of unity, the Iwahori--Hecke algebra acquires a non-trivial radical. This radical annihilates exponentially many resolution paths, pruning the tree to polynomial effective size. This regime corresponds exactly to BQP, rendering the computational horizon transparent. Conversely, at non-torsion values like $q_0$, the algebra remains semisimple. No paths vanish; the full $3^c$ resolution tree survives. The computational horizon $\mathcal{H}_c(L, q_0) \neq \varnothing$ therefore strictly blocks NP-complete links.

**Kummer persistence.** The Kummer filtration yields $\kappa_c^{\mathrm{comp}} \bmod n = 0$ if and only if $n \mid 6$. Because $q_0$ is strictly non-torsion, no finite Kummer level applies. The obstruction remains perpetual.

**Corollary.** Resolving $\mathrm{P}$ vs $\mathrm{NP}$ strictly constrains RH, NS, and BSD, and vice versa. Although their evaluation maps differ, the underlying obstruction class remains identical.
<!-- FILE_END: qou-p-neq-np.md -->

