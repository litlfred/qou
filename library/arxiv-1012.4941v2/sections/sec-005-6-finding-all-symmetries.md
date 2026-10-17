---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-005-6-finding-all-symmetries
section_title: "Finding All Symmetries"
section_number: 6
pages: 13-16
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.98
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:finding label="sec:finding"} For the algorithms presented it is never necessary to know the entire group of automorphisms of $\operatorname{LP}(A,b,c)$ or $\operatorname{ILP}(A,b,c)$. Generally, any subgroup will do, the larger the better. Yet here we would like to discuss the question of how to find automorphisms of integer linear programs. From the input data we will construct a labeled graph $\operatorname{G}(A,b,c)$ whose group of labeled automorphisms coincides with $\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,c))$.

Expressing symmetry in optimization via graph automorphisms is not a new idea: the linear automorphism group of a polytope and of a linear program can be obtained by computing the automorphism group of a certain graph as described by Bremner, Dutour Sikirić, and Schürmann [@PolyRepConv]. The combinatorial automorphisms of a polytope are the (labeled) graph automorphisms of the bipartite graph encoded by the vertex-edge-incidences. This directly follows from the fact that the face lattice of a polytope is atomic and coatomic; see Kaibel and Schwartz [@KaibelSchwartz03]. Liberti studies automorphisms of optimization problems which are more general than integer linear programs [@Liberti10]. His approach, however, deals with expression trees obtained from a specific encoding of the optimization problem. None of these concepts seems to be directly related to the kind of symmetry studied here. An idea similar to ours, however, has been applied by Berthold and Pfetsch [@BertholdPfetsch09] to find symmetries of $0/1$-ILPs.

The complexity status of the graph isomorphism problem is notoriously open. While the known algorithms for determining the automorphism group of a graph require exponential time, there exist software packages, for instance, `nauty` [@nauty] or `SymPol` [@SymPol], that can solve this problem very well in practice.

For a given matrix $A\in{\mathbb{R}}^{m\times n}$, right hand side $b\in{\mathbb{R}}^m$, and objective function $c\in{\mathbb{R}}^n$ we will now associate two undirected simple graphs, the *ILP graph* $\operatorname{G}(A,b,c)$, and the *restricted ILP graph* $\operatorname{G}'(A,b,c)$. For the sake of a simplified exposition we start out by describing the restricted ILP graph. Throughout we assume that the rows of the extended matrix $(A|b)$ are normalized as described in Remark [\[rem:scale\]](#rem:scale){reference-type="ref" reference="rem:scale"}. We have one node $\alpha_{ij}$ for each position in the matrix $A$, one node $\rho_i$ for each row, and one node $\zeta_j$ for each column, that is, $(i,j)\in [m]\times[n]$, where $[n]=\{1,2,\dots,n\}$. Further, we have one node $\kappa_u$ for each distinct coefficient $u$ in the matrix $A$, one node $\lambda_v$ for each distinct coefficient $v$ of $b$, and one node $\mu_w$ for each distinct coefficient $w$ of $c$. This gives a total of $mn+m+n+n_A+n_b+n_c$ nodes, where $n_A$, $n_b$, and $n_c$ denotes the respective number of different entries in $A$, $b$, and $c$. The nodes receive labels in the following way: all positions share the same label, the rows receive a second, and the columns a third label. Each node corresponding to one of the coefficients receives an individual label. This way we arrive at $n_A+n_b+n_c+3$ labels altogether. The edges of $\operatorname{G}'(A,b,c)$ are defined as follows: the node $\alpha_{ij}$ is adjacent to $\rho_i$ and $\zeta_j$ as well as to the coefficient node which represents the coefficient $a_{ij}$ of the matrix $A$. Moreover, the row node $\rho_i$ is adjacent to the node $\lambda_{b_i}$, and the node $\zeta_j$ is adjacent to the node $\mu_{c_j}$. This totals to $3mn+m+n$ edges.

Let $\gamma$ be an automorphism of $\operatorname{G}'(A,b,c)$ which respects all node labels. Since the common label of the column nodes is preserved $\gamma$ induces a column permutation $\psi_\gamma\in\mathop{\mathrm{Sym}}(n)$. Now $\psi_\gamma$ acts on the standard basis $\{e_1,e_2,\dots,e_n\}$, and by linear extension we obtain a linear transformation which we denote $\psi_\gamma^*$.

::: lemma
[]{#lem:phi_psi label="lem:phi_psi"} The linear transformation $\psi_\gamma^*$ is a symmetry of $\operatorname{ILP}(A,b,c)$.
:::

::: proof
*Proof.* As above let $\gamma$ be a labeled automorphism of $\operatorname{G}'=\operatorname{G}'(A,b,c)$ with induced column permutation $\psi=\psi_\gamma$ and linear transformation $\psi^*\in\mathop{\mathrm{Sym}}(n)\le{\operatorname{GL}}_n{\mathbb{R}}$. As for the column nodes the graph automorphism $\gamma$ also induces a permutation $\phi\in\mathop{\mathrm{Sym}}(m)$ of the row nodes of $\operatorname{G}'$. The position nodes $\alpha_{ij}$ form a label class of their own, and so they are permuted by $\gamma$ as well. Since each position node is adjacent to precisely one row and one column node we infer that $\gamma(\alpha_{ij})=\alpha_{\phi(i),\psi(j)}$. Each position node is adjacent to precisely one matrix coefficient node, each of which forms a singleton label class. This implies that the coefficient $a_{ij}$ corresponding to the node $\alpha_{ij}$ is the same as the coefficient $a_{\phi(i),\psi(j)}$. Likewise we obtain $b_i=b_{\phi(i)}$ and $c_j=c_{\psi(j)}$. This means that $\psi_\gamma^*$ is a symmetry of $\operatorname{ILP}(A,b,c)$. ◻
:::

::: proposition
[]{#prop:reduced_iso label="prop:reduced_iso"} The map $\gamma\mapsto\psi_\gamma^*$ is an isomorphism from the group of labeled automorphisms of the graph $\operatorname{G}'(A,b,c)$ to the group $\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,c))\cap\mathop{\mathrm{Sym}}(n)$.
:::

::: proof
*Proof.* We describe the inverse map. To this end let $\sigma$ be a symmetry of $\operatorname{ILP}(A,b,c)$ which acts on the standard basis of ${\mathbb{R}}^n$. Hence $\sigma$ induces a permutation $\phi$ of the rows of the extended matrix $(A|b)$ and a permutation $\psi$ of the columns of $A$. It is obvious how $\phi$ and $\psi$ induce permutations of the row nodes and of the column nodes of $\operatorname{G}'$. By the same reasoning as in the proof of Lemma [\[lem:phi_psi\]](#lem:phi_psi){reference-type="ref" reference="lem:phi_psi"} the pair $(\phi,\psi)$ uniquely extends to a labeled graph automorphism $\gamma(\sigma)$ of the reduced ILP graph.

We omit the straightforward proofs that the equations $\gamma(\psi_\gamma^*)=\gamma$ and $\psi_{\gamma(\sigma)}^*=\sigma$ both hold. From these it follows that the map $\gamma\mapsto\psi_\gamma^*$ is bijective. In both groups the multiplications are given by concatenations of maps. A direct computation yields $\psi_{\gamma_1\gamma_2}^*=\psi_{\gamma_1}^*\psi_{\gamma_2}^*$; all maps are acting on the left. Hence the group structures are preserved. ◻
:::

We now explain how the full ILP graph $\operatorname{G}(A,b,c)$ differs from the restricted ILP graph $\operatorname{G}'(A,b,c)$. The key to the construction of $\operatorname{G}'(A,b,c)$ is the map $\gamma\mapsto\psi_\gamma^*$ yielding a linear transformation which acts as a permutation of the standard basis of ${\mathbb{R}}^n$. In order to allow for signed permutations certain nodes have to be duplicated: each column node $\zeta_j$ in $\operatorname{G}'(A,b,c)$ gets a *twin node* $\hat\zeta_j$ in $\operatorname{G}(A,b,c)$, each matrix coefficient node $\alpha_{ij}$ corresponding to a non-zero coefficient gets a twin node $\hat\alpha_{ij}$. Moreover, we add further nodes representing negatives of non-zero coefficients in the matrix $A$ and the objective function $c$ unless nodes with these labels already exist. This way $\operatorname{ILP}(A,b,c)$ has less than twice as many nodes as $\operatorname{ILP}'(A,b,c)$; it is always strictly less as the nodes corresponding to the coefficients in $b$ are never duplicated. We also add edges such that first $\hat\alpha_{ij}$ is adjacent to $\rho_i$ and $\hat\zeta_j$ for all $i$ and $j$, second $\hat\zeta_j$ is adjacent to $\mu_{-c_j}$, third $\hat\alpha_{ij}$ is adjacent to $\kappa_{-a_{ij}}$, and, finally, the twins are matched up: $\alpha_{ij}$ is adjacent to $\hat\alpha_{ij}$ and $\hat\zeta_j$ is adjacent to $\zeta_j$. The labeling is extended in a way such that twins share the same label; the nodes newly introduced for negatives of coefficients receive new singleton labels.

Each labeled graph automorphism of $\operatorname{G}'(A,b,c)$ uniquely extends to a labeled graph automorphism of $\operatorname{G}(A,b,c)$, but the automorphism group of the non-reduced ILP graph is larger, in general. We have the following result.

::: theorem
The group of labeled graph automorphisms of $\operatorname{G}(A,b,c)$ is isomorphic to the group of symmetries of $\operatorname{ILP}(A,b,c)$.
:::

::: proof
*Proof.* One can follow the strategy in the proof of Proposition [\[prop:reduced_iso\]](#prop:reduced_iso){reference-type="ref" reference="prop:reduced_iso"}. We know that a labeled graph automorphism of $\operatorname{G}'(A,b,c)$ encodes a symmetry of $\operatorname{ILP}(A,b,c)$ which permutes the set $\{e_1,e_2,\dots,e_n\}$. Now a labeled graph automorphism of $\operatorname{G}(A,b,c)$ may map a column node $\zeta_j$ to some node $\hat\zeta_k$. But then it follows that $\hat\zeta_j$ is mapped to $\zeta_k$ since $\hat\zeta_j$ is the only column node adjacent to $\zeta_j$, and $\zeta_k$ is the only column node adjacent to $\hat\zeta_k$. This shows that the permutation of the column nodes can be extended to a linear transformation. As in the proof of Proposition [\[prop:reduced_iso\]](#prop:reduced_iso){reference-type="ref" reference="prop:reduced_iso"} one can show that this linear transformation is a symmetry of the integer linear program. Conversely, each such symmetry acts like a signed permutation on the signed standard basis and yields a labeled isomorphism of the graph $\operatorname{G}(A,b,c)$. ◻
:::

Roughly speaking, a class $\mathcal{C}$ of graphs is *graph isomorphism complete* if the problem of deciding isomorphy for any two graphs in $\mathcal{C}$ is as difficult as for general graphs, up to a polynomial time transformation. For a precise definition, for instance, see the monograph [@KoeblerSchoeningToran93]. The next result is not only of theoretical interest. To the contrary, for practical applications it can be read as: finding the symmetries of an integer linear program via reducing to automorphisms of suitable (labeled) graphs, is the right thing to do.

::: theorem
The classes of ILP graphs and reduced ILP graphs are both graph isomorphism complete.
:::

::: proof
*Proof.* We only prove that the class of reduced ILP graphs is graph isomorphism complete. It is known that the class of bipartite graphs is graph isomorphism complete. Hence it suffices to encode an arbitrary bipartite graph as a reduced ILP graph, which is not too large.

Let $G=(V,E)$ be an undirected bipartite graph with $m+n$ nodes $V=U\cup
  W=\{u_1,\dots,u_m\}\cup\{w_1,\dots,w_n\}$. As our matrix $A_G=(a_{ij})\in{\mathbb{R}}^{m\times
    n}$ we take the bipartite adjacency matrix of $G$, that is, $$a_{ij} \ = \
  \begin{cases}
    1 & \text{if $\{u_i,w_j\}\in E$}\\
    0 & \text{otherwise \, .}
  \end{cases}$$ For a second bipartite graph $G'$ it is easy to see that the reduced ILP graph of $\operatorname{ILP}(A_G,\mathbbm{1},\mathbbm{1})$ is isomorphic to the reduced ILP graph of $\operatorname{ILP}(A_{G'},\mathbbm{1},\mathbbm{1})$ if and only if $G$ is isomorphic to $G'$. ◻
:::

::: remark
[]{#rem:GLnZ label="rem:GLnZ"} Rehn investigates arbitrary automorphisms of the integer lattice ${\mathbb{Z}}^n$ in the context of polyhedral geometry [@Rehn10]. In particular, his modification of a backtracking algorithm of Plesken and Souvignier [@PleskenSouvignier97] allows to obtain matrix generators of the group of symmetries. For practical applications this should be superior to our approach via graph automorphisms if the number $m$ of constraints is much larger than the dimension $n$.
:::
