---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-003-22-containment-of-bimodules
section_title: "Containment of bimodules"
section_number: 2.2
pages: 3-4
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.943
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
Let $\mathcal{A}$ be a $\ast$-algebra. By an $\mathcal{A}$--$\mathcal{A}$ bimodule $H$ we mean a Hilbert space together with $\ast$-homomorphisms $\pi_l: \mathcal{A}\rightarrow B(H)$ and $\pi_r: \mathcal{A}^{op} \rightarrow B(H)$ whose images commute. If $\mathcal{A}$ is a von Neumann algebra then we assume moreover that $\pi_l$ and $\pi_r$ are normal.

We write $L_2(M)$ for the trivial bimodule and $L_2(M) \otimes L_2(M)$ for the coarse bimodule with the usual left and right actions. Let $H$ and $K$ be $M$-$M$ bimodules. We say that $H$ is **contained** in $K$ if $H$ is (isomorphic to) a sub-bimodule of $K$; i.e. $H$ is a closed subspace of $K$ that is invariant for the bimodule actions of $M$. We say that $H$ is **quasi-contained** in $K$ if $H$ is contained in $\oplus_{i \in I} H$ for some index set $I$. We use Popa's definition of weak containment [@PopaIncrest].

::: dfn
Let $M$ be a von Neumann algebra and let $H$ and $K$ be $M$-$M$-bimodules. We say that $H$ is **weakly contained** in $K$ if for every $\epsilon > 0$, every finite set $F \subseteq M$ and every $\xi \in H$ there exists finitely many $\eta_j \in K$ indexed by $j \in G$ such that for $x,y \in F$, $$\vert \langle x \xi y , \xi \rangle - \sum_{j \in G} \langle x \eta_j y, \eta_j \rangle \vert < \varepsilon.$$ Notation $H \preceq K$.
:::

The following clarifies the connection to containment in the way we encounter it in this paper.

::: lem
[]{#Lem=Containment label="Lem=Containment"} Let $M$ be a von Neumann algebra and $\mathcal{A}$ a $\sigma$-weakly dense $\ast$-subalgebra of $M$ with norm closure $A$. Let $H$ be an $A$-$A$-bimodule and let $K$ be an $M$-$M$-bimdoule. Suppose that there exists a dense subspace $D \subseteq H$ such that for every $\xi \in D$ there exists an $\eta \in K$ such that for every $x,y \in \mathcal{A}$ we have $$\langle x \xi y, \xi \rangle = \langle x \eta y, \eta \rangle.$$ Then for every $\xi \in D$ the sub-bimodule $H_\xi := \overline{ A \xi A}$ of $H$ is contained in $K$ as $A$-$A$ bimodules. Consequently, $H$ is contained in a (possibly infinite) direct sum of copies of $K$ and further the $A$-$A$ bimodule actions on $H$ extend to normal $M$-$M$-bimodule actions.
:::

::: proof
*Proof.* Take $\xi \in D$. By assumption there exists $\eta \in K$ such that for all $x,y \in \mathcal{A}$ we have that $\langle x \xi y, \xi \rangle = \langle x \eta y, \eta \rangle$. Then set $U: H_\xi \rightarrow K$ by $a \xi b \mapsto a \eta b$ where $a,b \in \mathcal{A}$ and it follows that this map is isometric and intertwines the bimodule actions (of $\mathcal{A}$ and then by continuity of $A$).

Since $UH_\xi$ admits normal $M$-$M$ bimodule actions, we can extend the $A$-$A$ actions on $H_\xi$ to normal $M$-$M$ bimodule actions.

Let $\Sigma$ be the set of all families of unit vectors $(\xi_i)_i$ in $H$ such that each $H_{\xi_i}:=\overline{A \xi_i A}$ is a sub $A$-$A$ bimodule of $K$ and that all $H_{\xi_i}$ are orthogonal with each other. By Zorn's lemma, take a maximal element $(\xi_i)_i$ in $\Sigma$. Let $P_i$ be the orthogonal projection onto $H_{\xi_i}$ and suppose by contradiction that $P:=\sum_i P_i \neq 1_H$. Note that $P$ commutes with $A$-$A$ bimodule actions. Let $\xi\in D$ be such that $(1-P)\xi\neq 0$ and fix $\eta\in K$ such that $\langle a\xi b,\xi\rangle=\langle a\eta b,\eta\rangle$. Then observe that for all finitely many $a_i,b_i \in \mathcal A$, $$\| \sum_i a_i (1-P)\xi b_i \| =   \| (1-P) \sum_i a_i \xi b_i \| \leqslant \| \sum_i a_i \xi b_i \| = \| \sum_i a_i \eta b_i \|.$$ One can define a contraction $v\colon \overline{A \eta A} \to \overline{A (1-P)\xi A}$ by $v (a \eta b ) = a (1-P)\xi b$ for $a,b\in \mathcal A$. Then since $v^*v$ commutes with $A$-$A$ bimodule actions, if we put $\eta':= (v^*v)^{1/2}\eta$, then it satisfies $$\langle a (1-P)\xi b, (1-P)\xi\rangle = \langle a \eta' b,\eta'\rangle, \quad \text{for any }a,b \in \mathcal A.$$ This contradicts the maximality of $(\xi_i)_i$. We conclude that there is an $A$-$A$ bimodule embedding $$H= \bigoplus_i H_{\xi_i} \subset \bigoplus_i K$$ and we can extend the $A$-$A$ actions to normal $M$-$M$ bimodule actions via this embedding. ◻
:::
