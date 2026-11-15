---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-007-5-a-network-flow-approach
section_title: "A network flow approach"
section_number: 5
pages: 13-16
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#nflow label="nflow"}

There is an alternative way to prove Theorem [\[maindual\]](#maindual){reference-type="ref" reference="maindual"} which uses the Max Flow-Min Cut theorem of network flow instead of the duality theorem of linear programming. It should be noted that the difference between the two arguments is largely superficial, since the proof of Theorem [\[maindual\]](#maindual){reference-type="ref" reference="maindual"} can be seen to essentially prove the Max Flow-Min Cut theorem. There are two reasons to set up the question as a result on network flow. The first is that the proof (hopefully) becomes clearer and more intuitive. The second is that the special sorts of linear programs that arise in the theory of network flow have been heavily analyzed from the viewpoint of complexity, which will allow us to give a very satisfactory estimate (section [\[complexsec\]](#complexsec){reference-type="ref" reference="complexsec"}) for the running time of an algorithm to determine whether a structure with prescribed dihedral angles actually exists.

A *network* is a directed (multi)graph $N$, with two distinguished vertices -- $s$ (the source), and $S$ (the sink). Each edge of $N$ has a certain *capacity*, which is a real number, which is an upper bound on the amount of the commodity which can flow from the tail to the head of the edge. A *cutset* $C$ of $N$ is a collection of edges, the removal of which leaves $s$ and $S$ in two different connected components of $N \backslash C$. The *capacity of the cutset* $C$ is simply the sum of the capacities of the edges comprising $C$. The capacity of an empty collection of edges is, of course, $0$.

The Max Flow-Min Cut theorem of network flow (see, for example, [@vlw Chapter 7]) says the following:

::: theorem
[]{#mfmc label="mfmc"} The maximal amount of a commodity that can flow from the source $s$ to the sink $S$ of a network $N$ is equal to the capacity of the smallest cutset in $N$.
:::

This theorem can be proved in a number of ways. The interested reader can adapt the proof of Theorem [\[maindual\]](#maindual){reference-type="ref" reference="maindual"} to show Theorem [\[mfmc\]](#mfmc){reference-type="ref" reference="mfmc"}.

To use Theorem [\[mfmc\]](#mfmc){reference-type="ref" reference="mfmc"} for our purposes, we need to set up a network of a special sort, starting with a triangulation $\mathcal{T}$.

The vertices of this network are divided into four classes: $\{s\}$, $F(\mathcal{T})$, $E(\mathcal{T})$, and $\{S\}$.

The source $s$ is connected to all of the vertices corresponding to the faces of $\mathcal{T}$ with edges of capacity $1$. We call them *edges of level $1$*. Every vertex corresponding to a face $t$ is connected to the three vertices, corresponding to the three edges of $t$ by edges of capacity $1$. These are edges of level $2$. Finally, each $e\in 
E(\mathcal{T})$ is connected to the sink $S$ by an edge of capacity $\delta(e)$. These are edges of level $3.$

The following statement is self-evident:

::: observation
There exists a solution of the linear program $L_{1}$ if and only if the maximal flow through the above-constructed network $N_{1}$ is equal to $|F(\mathcal{T})|$.
:::

::: proof
*of theorem [\[mainthm\]](#mainthm){reference-type="ref" reference="mainthm"}.* Consider a cut $C$ of $N_{1}$. This will have some edges at level $1$, removing which which will disconnect a subset $F_{0}$ of the faces of $\mathcal{T}$ from the source. It is then not necessary to remove any edges of level $2$ emanating from $F_{0}$. Let $F(\mathcal{T}) 
\backslash F_{0} = F_{1}$. Let $F_{2} \subseteq F_{1}$ be those faces $f$ for which the cutset contains all three edges of level $2$ emanating from $f$. Finally, $F_{3} = F_{1} \backslash F_{2}$. All of the edges of level $3$ (indirectly) emanating from $F_{3}$ must be in the cutset $C$. These are precisely the edges corresponding to the edges of the subcomplex of $\mathcal{T}$ whose faces are in $F_{3}$.

What is the capacity of $C$? Evidently, it is equal to

$$\label{thesum}
F_{0}+ 3 F_{2}+ \sum_{e\in E(F_{3})} \delta(e).$$ If we want the flow through $N_{1}$ to be $F$, we must have $$F_{0}+ 3 F_{2}+ \sum_{e\in E(F_{3})} \delta(e) \geq F,$$ Or, noting that $F_{1} = F - F_{0}$, $$3 F_{2}+ \sum_{e\in E(F_{3})} \delta(e) \geq F_{1}.$$

In the special case where $F_{2} = 0$, it follows that $$\label{geq}
\sum_{e\in E(F_{3})} \delta(e) \geq F.$$

Since $F_{3}$ could have been any subset of $F$, it follows that condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} is necessary (this is, in any event, self evident).

On the other hand, if condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} holds for any subcomplex of $\mathcal{T}$, substituting the inequality [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} into [\[thesum\]](#thesum){reference-type="ref" reference="thesum"}, we see that $$c(C)\geq F_{0}+ 3 F_{2}+ F_{3} = F + 2 F_{2} \geq F.$$ ◻
:::

The above result is not quite what is required: the non-strict inequality [\[geq\]](#geq){reference-type="ref" reference="geq"} implies the existence of a consistent assignment of angles to the faces of $\mathcal{T}$, but some of these angles may be equal to $0$. In order to have the angles strictly positive, we must modify the weights in the network $N_{1}$ as follows:

Modify the capacity of level $1$ edges to be $1-3\epsilon$; those of level $2$ to be $1-\epsilon$, and those of level $3$ to be $1-2\epsilon$. Call the resulting network $N_{2}$. The existence of a consistent assignment of angles to the faces of $\mathcal{T}$ where all the angles are no smaller than $\epsilon$ is obviously equivalent to the maximal flow in $N_{2}$ being equal to $F(\mathcal{T})(1-3 \epsilon)$.

Consider now a cut $C$ in $N_{2}$, with notation as before. The capacity of $C$ will be:

$$\label{epseq}
(1-3\epsilon)F_{0} + 3 (1-\epsilon)F_{2} + \sum_{e\in E(F_{3}} 
\delta(e) - 2\epsilon E(F_{3}).$$

Assume that $F_{2} = 0$. The MinCut condition together with expression [\[epseq\]](#epseq){reference-type="ref" reference="epseq"} gives: $$(1-3\epsilon)F_{0} + \sum_{e\in E(F_{3}} 
\delta(e) - 2\epsilon E(F_{3}) \geq (1-3\epsilon) F,$$ or $$\sum_{e\in E(F_{3}} \delta(e) \geq (1-3\epsilon)F_{3} + 2\epsilon 
E(F_{3}).$$ If $\emptyset \subset F_{3}\subset F$, then $E(F_{3}) > 
\frac32 F_{3}$, and so $\sum_{e\in E(F_{3}}\delta(e) > F_{3}.$

Suppose now that $\delta(F') - F' \geq \psi > 0$, for all proper non-empty subsets $F'$ of $F$.

Then the expression [\[epseq\]](#epseq){reference-type="ref" reference="epseq"} is no smaller than $$\label{ineqq}
(1-3\epsilon)F_{0} + 3 (1-\epsilon)F_{2} + F_{3}+\psi- 2\epsilon E(F_{3}).$$

The edges of $F_{3}$ can be divided into two classes: interior edges (those incident to two triangles of $F_{3}$) -- these number $E_{i}(F_{3})$, and boundary edges of $F_{3}$ -- those incident to only one triangle. These number $E_{\partial}(F_{3})$. Since $F_{3}$ is a proper subset of $F$, $E_{\partial}(F_{3})>0$. Clearly, $$2 E(F_{3}) = 3 F_{3} + E_{\partial}(F_{3}).$$ The lower bound [\[ineqq\]](#ineqq){reference-type="ref" reference="ineqq"} can thus be rewritten as $$\begin{aligned}
c(C) & \geq &(1-3\epsilon)F_{0} + 3 (1-\epsilon)F_{2} +
(1-3\epsilon)F_{3}+\psi- \epsilon E_{\partial}(F_{3}) \\
& = & (1-3\epsilon) F + \psi +  (1-3\epsilon)F_{2} - \epsilon
E_{\partial}(F_{3}). 
\end{aligned}$$ Since $\epsilon\leq\frac13$ (a triangle cannot have all angles greater than $\pi/3$), we get $$c(C) -(1-3 \epsilon)F\geq \psi - \epsilon E_{\partial}(F_{3}).$$

In other words, if $\sum_{e\in E(F')} \delta(e) - F'\geq \psi$ for every $\emptyset \subset F'\subset F$, there is a solution of the linear program $L_{1}$ with all face angles of all triangles no smaller than $\psi/E(\mathcal{T})$. 0◻
