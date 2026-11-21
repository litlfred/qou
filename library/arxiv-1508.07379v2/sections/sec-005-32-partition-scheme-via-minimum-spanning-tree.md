---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity"
section_id: sec-005-32-partition-scheme-via-minimum-spanning-tree
section_title: "Partition scheme via minimum spanning tree"
section_number: 3.2
pages: 8-11
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity — We establish new lower bounds for the convergence radius of the Mayer series and the Virial series of a continuous"
---
[]{#asas label="asas"}

The key point now is to find a partition scheme $\bm M$ in such a way that is possible to find a good bound for the factor $\exp\{-\b\sum_{\{i,j\}\in E_{\bm{M}(\t)}\backslash E^+_\t}V(x_i-x_j)\}$ appearing in the r.h.s. of ([\[tre\]](#tre){reference-type="ref" reference="tre"}).

\
We will construct explicitly our partition scheme $\bm M: {\mathcal T}_n\to {\mathcal G}_n$ by first defining an auxiliary map $\bm T :{\mathcal G}_n\to {\mathcal T}_n$ and then deriving $\bm M$ from $\bm T$ according to the following proposition.

::: pro
[]{#twomaps label="twomaps"} The following statements are equivalent.

-   There are two maps $$\xymatrix{{\mathcal G}_n \ar@<.5ex>[r]^\Ti & {\mathcal T}_n \ar@<.5ex>[l]^\Mi}$$ such that $\Ti^{-1}(\tau)=\{g \in {\mathcal G}_n:\, \tau \subset g \subset \Mi(\tau)\}$ for every $\tau \in {\mathcal T}_n$.

-   $\Mi$ is a partition scheme in ${\mathcal G}_n$.
:::

\
*Proof*. $1\Rightarrow2$. Since $g \in \Ti^{-1}(\Ti(g))$, we have $\Ti(g) \subset g$ for all $g \in {\mathcal G}_n$. In particular, for every tree $\tau$ we have $\Ti(\tau) \subset \tau$ which implies $\Ti(\tau)=\tau$ because both are trees. I.e., $\Ti$ is surjective and thus the intervals $\Ti^{-1}(\tau)$ are nonempty. This implies that ${\mathcal G}_n$ is the disjoint union of the intervals ${\mathcal G}_n = \bigcup_{\tau \in {\mathcal T}_n} \Ti^{-1}(\tau)=\bigcup_{\tau \in {\mathcal T}_n}[\t, \Mi(\t)]$. Hence in view of Definition [\[partschem\]](#partschem){reference-type="ref" reference="partschem"} we conclude that $\Mi$ is a partition scheme in ${\mathcal G}_n$.

\
$2\Rightarrow1$. If $\Mi$ is a partition scheme then for any $g\in {\mathcal G}_n$ there exists a unique tree $\t\in {\mathcal T}_n$ such that $g\in [\t,\bm M(\t)]$. Therefore we can define the map $\bm T$ from ${\mathcal G}_n$ to ${\mathcal T}_n$ such that, for all $g\in [\t,\bm M(\t)]$, $\bm T(g)=\t$. $\Box$

\
We thus start by first defining the map $\bm T$ from ${\mathcal G}_n$ to ${\mathcal T}_n$. In order to do that, assume we have a function defined on the edges of the complete graph, $f: E_n \to {\mathbb R}^*$. Then, for every connected graph $g \in {\mathcal G}_n$ there is at least a tree $\tau \subset g$, among the trees $\tau' \subset g$, which minimizes the value of $\sum_{e \in E_{\tau'}} f(e)$. This tree is called a minimum spanning tree of $g$ w.r.t. $f$. If $f$ is such that this minimum spanning tree is unique for each graph $g \in {\mathcal G}_n$, then $f$ induces a map, say $\bm T_f$, from ${\mathcal G}_n$ to ${\mathcal T}_n$ which associates to each $g \in {\mathcal G}_n$ this unique minimum spanning tree.

\
Let now $V$ be a stable and tempered pair potential in ${\mathbb{R}}^{dn}$ and let $(x_1,\dots,x_n)\in \mathbb{R}^{dn}$ be given. We would like to consider as the function $f: E_n \to  {\mathbb R}^*$ the one that associates to each $\{i,j\}\in E_n$ the value $V(x_i-x_j)$. The problem is that such $f$, depending on the potential $V$ and the configuration $(x_1,\dots,x_n)\in \mathbb{R}^{dn}$ chosen, in general does not guarantee that each $g\in {\mathcal G}_n$ contains a unique minimum spanning tree w.r.t. to $f$. In order to avoid multiple minima, we will therefore modify the codomain of the function $f$ by adding $n(n-1)/2$ auxiliary "coordinates\" (which will take only integers values), each of them one-to-one associated to an edge of $E_n$. These coordinates will permit to distinguish eventual multiple minimum trees.

\
To carry out this procedure, we need to widen our framework and consider, instead of functions from $E_n$ to $\mathbb{R}^*$, a suitable class of more general functions $f:E_n\to {\mathbb K}$ with ${\mathbb K}$ being a totally ordered Abelian monoid and having the key property that $\sum_{e \in E_{\tau}} f(e)$ is different for different trees $\tau \in {\mathcal T}_n$. We recall that a *totally ordered Abelian monoid* (shortly *tomonid*) is a structure $({\mathbb K}, + ,0, \ge)$ such that $({\mathbb K}, + ,0)$ is an Abelian (i.e. commutative) monoid, $({\mathbb K}, \ge)$ is a totally ordered set and for all $x, y, z\in  {\mathbb K}$ we have that $x\ge y$ implies $x + z \ge y + z$ (i.e. the total order $\ge$ is translational invariant).

::: defi
[]{#fadm label="fadm"} Let $f: E_n \to {\mathbb K}$ where ${\mathbb K}$ is a totally ordered Abelian monoid. We say that $f$ is admissible if for any $\t,\t'\in {\mathcal T}_n$ such that $\t\neq \t'$ we have that $\sum_{e \in E(\tau)} f(e)\neq \sum_{e \in E(\tau')} f(e)$.
:::

\
Once an admissible function $f: E_n \to {\mathbb K}$ has been given, we can define the maps $\bm T_f$ from ${\mathcal G}_n$ to ${\mathcal T}_n$ $\bm M_f$ from ${\mathcal T}_n$ to ${\mathcal G}_n$ as follows.

::: defi
[]{#hyp label="hyp"} Let $\mathbb{K}$ be a totally ordered Abelian monoid. Let $f: E_n \to {\mathbb K}$ be an admissible function. Then, for every $g \in {\mathcal G}_n$ there is a unique spanning tree $\t \subset g$ for which $\sum_{e \in E(\tau)} f(e)$ is minimum. We define the map $\bm T_f: \GG_n\to \TT_n$ such that $\bm T_f(g)$ is this unique minimum spanning tree of $g$.
:::

::: defi
[]{#d4 label="d4"} Let $\mathbb{K}$ be a totally ordered Abelian monoid and let $f: E_n \to {\mathbb K}$ be an admissible function.

We define the map $\bm M_f:{\mathcal T}_n\to{\mathcal G}_n$ such that $\bm M_f( \tau )$ is the graph on the vertices $[n]$ whose edges are the $\{i,j\}$ such that $f(\{i,j\}) \geq f(e)$ for every edge $e \in E_\tau$ belonging to the path from $i$ to $j$ through $\tau$.
:::

\
Thus we have constructed $$\xymatrix{{\mathcal G}_n \ar@<.5ex>[r]^{\bm T_f} & {\mathcal T}_n \ar@<.5ex>[l]^{\bm M_f}}$$ Observe that $\tau \subset \bm M_f(\tau)$ and $\bm T_f(g) \subset g$. Moreover, these two maps ${\bm T_f}$, ${\bm M_f}$ satisfy the hypothesis of the Proposition [\[twomaps\]](#twomaps){reference-type="ref" reference="twomaps"}. This is the content of the following lemma.

::: lem
[]{#l1 label="l1"} Let $f: E_n \to  {\mathbb K}$ be an admissible function and $\tau \in {\mathcal T}_n$. Let $\bm T_f$ and $\bm M_f$ be the maps given in Definitions [\[hyp\]](#hyp){reference-type="ref" reference="hyp"} and [\[d4\]](#d4){reference-type="ref" reference="d4"} respectively. Then $$\bm T_f^{-1}(\tau)=\{g \in {\mathcal G}_n :\, \tau \subset g \subset \bm M_f(\tau)\}$$ and therefore $\bm M_f$ is a partition scheme in ${\mathcal G}_n$.
:::

::: proof
*Proof.* Let $g \in \bm T_f^{-1}(\tau)$. We have $\tau=\bm T_f(g) \subset g$. Now take $\{i,j\} \in E_g$, and let $e \in E_\tau$ be any edge belonging to the path from $i$ to $j$ in $\tau$. Consider $\tau'$ the graph obtained from $\tau$ after replacing the edge $e$ by $\{i,j\}$. Clearly $\tau'$ is connected and has $n-1$ edges, so it is a tree. By minimality of $\tau$ we must have $f(d) \leq f(\{i,j\})$, whence $\{i,j\} \in E_{\bm M_f(\tau)}$. Therefore $g \subset \bm M_f(\tau)$.

\
Conversely, let $\tau \subset g \subset \bm M_f(\tau)$. We must show $\bm T_f(g)=\tau$. By cardinality, it suffices to show $\bm T_f(g) \subset \tau$. Proceeding by contradiction, take $\{i,j\} \in E_{\bm T_f(g)} \setminus E_\tau$. Consider the path $p^\t(\{i,j\})$ in $\tau$ joining $i$ with $j$. Since $\bm T_f(g) \subset \bm M_f(\tau)$, $f(\{i,j\})$ is greater or equal than the corresponding value for any edge in the path $p^\t(\{i,j\})$. If we remove $\{i,j\}$ from $\bm T_f(g)$, the tree splits into two trees. Necessarily, at least one of the edges in the path $p^\t(\{i,j\})$ joins a vertex of one tree with a vertex of the other. Thus, by adding this edge we obtain a connected graph with $n-1$ edges, a new tree, which contradicts the minimality of $\bm T_f (g)$. ◻
:::

\
We now provide an explicit construction for the admissible function $f$ of Definition [\[hyp\]](#hyp){reference-type="ref" reference="hyp"}.

\
We start by specifying the totally ordered Abelian monoid $\mathbb{K}$. Assume to have chosen an order in $E_n$ (e.g. the lexicographic order: $\{i,j\}<\{i',j'\}$ if either $i<i'$ or $i=i'$ and $j<j'$). Let $\mathbb{N}_0=\mathbb{N}\cup\{0\}$ and consider the set $${\mathbb N}_0^{E_n}=\overbrace{{\mathbb N}_0\times \cdots \times \mathbb N_0}^{|E_n|~{\rm  times}}$$ such that the $m^{\rm th}$ entry (with $1\le m\le |E_n|$) of an element $x\in {\mathbb N}_0^{E_n}$ corresponds to the $m^{\rm th}$ edge w.r.t. the order chosen of $E_n$. Now we set []{#tomonoid label="tomonoid"} \^\*\_0\^E_n An element of ${\mathbb{K}}$ is thus an ordered $(|E_n|+1)$-tuple such that the first entry is a real number while the remaining $|E_n|$ entries are natural numbers or zero.

\
The set ${\mathbb{K}}$ defined in ([\[tomonoid\]](#tomonoid){reference-type="ref" reference="tomonoid"}) has a canonical structure of Abelian monoid and can also be endowed with a natural total order by considering the lexicographical order on $\mathbb{R}^*\times \mathbb{N}_0^m$, prioritizing the entries from left to right. It is easy to show that such an order is translational invariant respect to the standard sum in ${\mathbb{K}}$ which is thus a totally ordered Abelian monoid.\
We are now ready to define the function $f:E_n\to \mathbb{K}$. Let $\bm 1_{\{i,j\}}$ be the element of ${\mathbb N}_0^{E_n}$ with all entries zero except the one at the position corresponding to the edge $\{i,j\}$ which is equal to one.

::: defi
[]{#fV label="fV"} Given a pair potential $V$ and given $(x_1,\dots,x_n)\in  \mathbb{R}^{dn}$, define the function []{#effe label="effe"} f:  E_n :  {i,j}V(x_i-x_j)\_{i,j}
:::

\
**Remark**. The function $f$ above is, for every pair potential $V$ and for any $(x_1,\dots,x_n)\in  \mathbb{R}^{dn}$, admissible according to Definition [\[hyp\]](#hyp){reference-type="ref" reference="hyp"} and thus, according to Definition [\[d4\]](#d4){reference-type="ref" reference="d4"} and Lemma [\[l1\]](#l1){reference-type="ref" reference="l1"}, the map $\bm M_f:{\mathcal T}_n\to{\mathcal G}_n$ is a partition scheme in ${\mathcal G}_n$. This is our new partition scheme. The advantage to consider this new partition $\bm M_f$ scheme instead of the one originally proposed by Penrose is manifestly clear in the following key lemma which practically concludes the proof of Proposition [\[pro1\]](#pro1){reference-type="ref" reference="pro1"}.

::: lem
[]{#stabp label="stabp"} Let $V: {\mathbb R}^d \to {\mathbb R}^*$ be a stable pair potential with stability constant $B$, and $\tau \in {\mathcal T}_n$. Then, for every $(x_1,...,x_n) \in {\mathbb R}^{dn}$, []{#Peb label="Peb"} \_{i,j} E\_M_f() E\_\^+ V(x_i-x_j) -Bn where $f$ is the function given in Definition [\[fV\]](#fV){reference-type="ref" reference="fV"}, $\bm M_f(\tau)$ is the graph given in Definition [\[d4\]](#d4){reference-type="ref" reference="d4"} and $E_\tau^+$ is the subset of $E_\t$ defined in ([\[t+\]](#t+){reference-type="ref" reference="t+"}).
:::

::: proof
*Proof.* In the following, $V_{ij}$ denotes $V(x_i - x_j)$, and we will make implicit use of the following trivial fact: $$(x,\sigma) \geq (x',\sigma') \Rightarrow x \geq x' \ \ \mbox{ for } (x,\sigma), (x',\sigma') \in \mathbb{R}^*\times{\mathbb N}_0^{E_n}$$ Now we proceed to show that the inequality ([\[Peb\]](#Peb){reference-type="ref" reference="Peb"}) holds true. The set of edges $E_\t\setminus E_\tau^+$ forms the forest $\{\tau_1,...,\tau_k\}$. Let us denote ${\mathcal V}_{\tau_s}$ the vertex set of the tree $\tau_s$ of the forest. Assume $i \in {\mathcal V}_{\tau_a}$, $j \in {\mathcal V}_{\tau_b}$. If $a \neq b$, the path from $i$ to $j$ through $\tau$ involves an edge $e$ in $E_\tau^+$. Thus, if in addition $\{i.j\} \in
E_{\bm M_f(\tau)}$, we have $V_{ij} \geq V_e \geq 0$. If $a=b$, the path from $i$ to $j$ through $\tau$ is contained in $\tau_a$. Thus, if in addition $\{i,j\} \notin E_{\bm M_f(\tau)}$, we must have $V_{ij} \leq V_e \leq 0$ for some edge $e$ in that path. This allows to bound:

$$\sum_{\{i,j\} \in E_{\bm M_f(\tau)} \setminus E_\tau^+} V_{ij} \geq \sum_{s=1}^k \sum_{\{i,j\} \subset {\mathcal V}_{\tau_s}} V_{ij} \geq
 \sum_{s=1}^k -|\mathcal V_{\tau_s}|B \ge -nB  ~~~~~~~~~~~~~~~~~~\Box$$ ◻
:::
