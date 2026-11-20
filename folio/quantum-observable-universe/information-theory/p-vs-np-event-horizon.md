One formally establishes a structural identity between computational complexity and jet horizon information loss. Reformulating $\mathrm{P}$ vs $\mathrm{NP}$ as the boundary condition $\mathcal{H}_c \stackrel{?}{=} \varnothing$ equates the computational boundary with a jet horizon. The identical horizon geometry $\mathcal{H} = V(\mathfrak{h})$ that blocks degree-$0$ photon data between aeons simultaneously blocks the degree-$0$ answer of an NP-complete problem.

**The dictionary.**
The physical QOU observer corresponds to an element of the observable subcategory $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$. Here, the degree-$0$ algebra $A_0$ is non-trivial and the Frobenius pairing is non-degenerate. The complement ($A_0 = 0$) defines the jet horizon. The computational analog maps directly onto this geometry.
See [Table 1](#tbl:p-vs-np-event-horizon-table1-data).

**The observer in $\mathrm{Bun}^{\circ}$ versus the observer in $\mathcal{R}^{\circ}$.**
In the physical QOU, observation requires $\Gamma(\mathcal{S}, A_0) \neq 0$. The observer performs degree-$0$ measurements because the Frobenius pairing is non-degenerate on $A_0$. At the jet horizon, $A_0 = 0$. The observer loses all degree-$0$ capability. It still detects degree $\geq 1$ data, capturing thermal winding and curvature as Hawking radiation, but it cannot identify individual particles.

In the computational setting, the observer is a polynomial-time algorithm inhabiting $\mathcal{R}^{\circ}$. It accesses degree-$0$ sections, evaluating $P_L(q)$, strictly from nodes within $\mathcal{R}^{\circ}$. At the computational boundary $\mathcal{H}_c$, the algorithm loses degree-$0$ capability. It retains the ability to verify witnesses via degree-$1$ linear transport and detect structural correlations via degree-$2$ curvature data, but it cannot extract the answer. A physics-side precedent links horizons and computational hardness directly: Harlow and Hayden argue that the quantum computation needed to decode the relevant degrees of freedom from Hawking radiation takes time exponential in the entropy of the black hole, and relate the decoding task to error correction and to zero-knowledge proofs \cite[\S3, \S4.4]{arxiv-1301.4504v4}.

**Information flow across the boundary.**
The jet horizon leakage table applies directly to computation.
See [Table 2](#tbl:p-vs-np-event-horizon-table2-data).

The degree-$1$ leakage embodies NP verification. Traversing a resolution path in $O(c)$ Planck steps constitutes linear transport. It represents the first jet beyond the constant term. This checks consistency but reveals nothing concerning the global sum $P_L(q_0)$. The degree-$2$ leakage embodies heuristic computation. Pairwise correlations between resolution paths reveal structural properties like clause-variable correlations. Heuristic algorithms exploit this curvature leakage without worst-case guarantees.

**The Planck step as the tick of a Turing machine.**
Each application of the $q$-connection $\nabla_q$ constitutes one Planck step. In the computational setting, this mirrors one discrete clock tick of a Turing machine. The Planck time $t_P(q) = q/(q-1)$ sets the fundamental clock rate. The operational entropy $\eta_q$ sets the information generated per tick.

A polynomial-time computation generates $I = \mathrm{poly}(c) \cdot \eta_q / \hbar_q$ $q$-bits. For P-class problems, this suffices. Destructive interference collapses the effective resolution tree to polynomial size. For NP-complete problems, the effective tree retains exponential size. The computation generates polynomial $q$-bits but demands exponential $q$-bits of aggregated information. The bandwidth $\mathfrak{B}(q)$ cannot bridge this deficit in polynomial time.

**Boundary condition versus resource bound.**
Standard complexity theory evaluates $\mathrm{P}$ vs $\mathrm{NP}$ as a resource bound. The QOU translates this to a geometric statement: the interior $\mathcal{R}^{\circ}$ is either closed (P $=$ NP) or carries a non-trivial frontier $\mathcal{H}_c$ (P $\neq$ NP).

This matches the physical jet horizon. If $\mathrm{Bun}^{\circ}$ is closed, no jet horizons exist. The universe operates as a single transparent aeon without information loss. If $\mathrm{Bun}^{\circ}$ is not closed, genuine frontiers exist. The physical QOU structurally possesses jet horizons. The conjecture asserts the computational QOU similarly possesses horizons, with $\mathcal{H}_c \neq \varnothing$ for NP-complete braids.

**The arrow of computational time.**
The Big Bang state initiates with $A_0|_{\mathcal{S}_0} = 0$. The universe begins outside $\mathrm{Bun}^{\circ}$, behind its own jet horizon. As Planck steps accumulate, the jet tower builds degree-$0$ sections, moving the universe into $\mathrm{Bun}^{\circ}$.

Computation mirrors this geometric arrow. A Turing machine begins with degree $\geq 1$ input data. It terminates with degree-$0$ output data. The computation traverses from $\mathcal{R} \setminus \mathcal{R}^{\circ}$ into $\mathcal{R}^{\circ}$. For P-class problems, $\mathcal{H}_c = \varnothing$. The algorithm starts in $\mathcal{R}^{\circ}$ and never leaves. For NP-complete problems, $\mathcal{H}_c \neq \varnothing$. The algorithm must forcefully cross the boundary, paying the exponential depth of the resolution tree as the crossing cost. The $\mathrm{P}$ vs $\mathrm{NP}$ question becomes geometric: whether the computational observable subcategory covers the full resolution tree.
