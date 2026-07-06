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
