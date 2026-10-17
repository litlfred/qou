---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-002-21-k-configuration-on-a-circle-and-continuous-co
section_title: "k-configuration on a circle and continuous counterpart"
section_number: 2.1
pages: 3-4
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.974
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#subsec:intro_model label="subsec:intro_model"}

For $k,n\in \mathbb{N}^*$ with $k\leq n$, let $B_{k,n}$ denote the set of positions of $k$ nonintersecting and indistinguishable particles on a discrete circle of size $n$. Formally, $B_{k,n}$ is the set of increasing sequences of $\llbracket 0,n-1\rrbracket$ of length $k$: such a sequence gives the position of the $k$ particles in the clockwise direction starting from the origin $0$ of the discrete circle, see Figure [\[figPart\]](#figPart){reference-type="ref" reference="figPart"} and the corresponding $k$-subsets on Figure [1](#figBkn){reference-type="ref" reference="figBkn"} in the case $k=2,n=4$.

The size $\langle I\rangle$ of an element $I=\{I_1>\ldots>I_k\}\in B_{k,n}$ is the sum of its parts (remark that the size is always positive when $I\in B_{k,n}$). The discrete set $B_{k,n}$ is given a graph structure by saying there is an oriented edge from $I$ to $J$ when $\langle J\rangle=\langle I\rangle +1\mod n$ and $\#\{1\leq l,l'\leq k, J_{l'}=I_l\}=k-1$. We then write $I\nearrow J$ when there is such an oriented edge from $I$ to $J$. The edges of $B_{k,n}$ encode the clockwise movement of the $k$ particles around the circle conditioned to never intersect. A distinguished vertex of $B_{k,n}$ is given by the sequence $I_0=\left\lbrace 0,\ldots,k-1\right\rbrace$, which represents $k$ particles stacked after the origin on the discrete circle. See Figure [1](#figBkn){reference-type="ref" reference="figBkn"} for the graph structure of $B_{2,4}$.

![Graph $B_{2,4}$ from a combinatorial perspective. []{#figBkn label="figBkn"}](graph_Bkn_I.pdf){#figBkn}

For fixed $k\geq 1$, the family of graphs $\{B_{k,n},\,n\geq 1\}$ has a continuous counterpart embodied by the set $T_{k}$ of positions of $k$ indistinguishable particles on a continuous circle of radius $1$. Identifying the positions of the particles by their distance from a distinguished point of the circle in the clockwise direction, we formally identify $T_k$ with the subset of vectors $\vec{u}=(u_1,\ldots,u_k)\in [0,2\pi[^k$ such that $$2\pi>u_1\geq u_2\geq\dots\geq u_k\geq 0.$$ Remark that we authorize particles to be at the same position in the continuous case, since this situation may theoretically appear as a limit case of discrete configurations as $n$ goes to infinity (although it will almost surely not be the case).

For $x\in \mathbb{R}$, denote by $\overline{x}$ the unique element of $[0,2\pi[$ such that $x-\overline{x}\in 2\pi\mathbb{Z}$. Then, reflecting the circular nature of the model, there is a shift action of $\mathbb{R}$ on $T_k$ given by $$R_{t}(\vec{u})=Sort(\overline{u_1-2t\pi},\ldots,\overline{u_k-2t\pi}),$$ where $Sort(\vec{u})$ is the sequence obtained from $\vec{u}\in [0,2\pi[^k$ by sorting it in decreasing order. For each $n\geq 1$, the graph $B_{k,n}$ can actually be embedded in $T_{k}$ through the map $$\label{eq:definition_xi_n}
\xi_n:\left\lbrace \begin{aligned}
&B_{k,n}&\rightarrow &\quad T_{k}\\
&I&\mapsto& R_{\frac{k-1}{2n}} \left(\frac{2\pi }{n}I\right)
\end{aligned}\right..$$ Note that there is a shift of $\frac{\pi(k-1)}{n}$ which seems at first sight arbitrary: its role is mainly to simplify later expressions.
