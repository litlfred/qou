---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-034-112-the-ptolemy-varieties-pt
section_title: "The Ptolemy varieties P(T)"
section_number: 11.2
pages: 22-24
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.917
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:PSLexample label="sec:PSLexample"}

An elementary cohomology computation shows that $H^2(\widehat M;\mathbb Z/2\mathbb Z)=\mathbb Z/2\mathbb Z\oplus\mathbb Z/2\mathbb Z$ and that the three non-trivial classes are represented by cocycles $\sigma^i\in C^2(\widehat M;\mathbb Z/2\mathbb Z)$ whose restrictions $\sigma^i_k$ to the $k$th simplex of $\mathcal T$ are given by $$\begin{aligned}

\sigma^1_0&=f_{0}^*+f_{2}^*,\quad&\sigma^1_1&=f_{0}^*+f_{1}^*,\quad&\sigma^1_2&=0,\\
\sigma^2_0&=f_{0}^*+f_{1}^*,\quad&\sigma^2_1&=f_{0}^*+f_{3}^*,\quad&\sigma^2_2&=f_{0}^*+f_{1}^*,\\
\sigma^3_0&=f_{1}^*+f_{2}^*,\quad&\sigma^3_1&=f_{1}^*+f_{3}^*,\quad&\sigma^3_2&=f_{0}^*+f_{1}^*,
\end{aligned}$$ where $f_{i}^*\in C^2(\Delta;\mathbb Z/2\mathbb Z)$ denotes the cochain taking the face $f_{i}$ opposite vertex $i$ to $-1$ and all other faces to $1$. The cocycle $\sigma^3$ is indicated in Figure [\[fig:Trigm009\]](#fig:Trigm009){reference-type="ref" reference="fig:Trigm009"}.

One easily checks that $\sigma^i_k=\delta(\eta_k^i)$, where $\eta^i_k$ is given by $$\begin{aligned}
\eta^1_0&=\varepsilon_{13}^*,\quad&\eta^1_1&=\varepsilon_{23}^*,\quad&\eta^1_2&=0,\\
\eta^2_0&=\varepsilon_{23}^*,\quad&\eta^2_1&=\varepsilon_{12}^*,\quad&\eta^2_2&=\varepsilon_{23}^*,\\
\eta^3_0&=\varepsilon_{03}^*,\quad&\eta^3_1&=\varepsilon_{02}^*,\quad&\eta^3_2&=\varepsilon_{23}^*,
\end{aligned}$$ where $\varepsilon_{ij}^*\in C^1(\Delta;\mathbb Z/2\mathbb Z)$ is the cochain taking $\varepsilon_{ij}$ to $-1$ and all other edges to $1$. The Ptolemy variety for the trivial obstruction class is equal to $\overline P(\mathcal T)$, which is trivial, as we saw earlier. Recall that the reduced Ptolemy variety is obtained by setting the Ptolemy coordinate $z$ of edge 3 equal to 1.

### Ptolemy variety for $\sigma^1$

The identification relations [\[eq:EdgeIdentificationsSigma\]](#eq:EdgeIdentificationsSigma){reference-type="eqref" reference="eq:EdgeIdentificationsSigma"} are $$\begin{gathered}
c_{23,0}=-c_{23,2}=-c_{01,1}=c_{01,2}=-c_{01,0}=c_{23,1}\\
c_{13,0}=-c_{12,1}=c_{13,2}=c_{03,1}=c_{13,0}\\
c_{13,1}=c_{03,2}=c_{02,0}=c_{12,2}=-c_{02,1}=c_{03,0}=c_{02,2}=c_{12,0}.
\end{gathered}$$ Again, letting $x=c_{23,0}$, $y=c_{13,0}$ and $z=c_{13,1}$, the Ptolemy relations become $$\label{eq:m009PtolemyPSL1}
z^2-x^2=zy,\qquad -y^2-x^2=-z^2,\qquad z^2-x^2=zy.$$ Setting $z=1$, the equations then have the three solutions $$(x,y,z)=(0,1,1),\qquad (x,y,z)=(-1,0,1),\qquad (x,y,z)=(1,0,1).$$ However, not all of these solutions are valid, since the edge equations may not be satisfied. The edge relation [\[eq:EdgeOneRelation\]](#eq:EdgeOneRelation){reference-type="eqref" reference="eq:EdgeOneRelation"} around edge 1 (defined when $y$ and $z$ are nonzero) is $$\frac{x}{-zy}+\frac{-x}{y(-z)}+\frac{x}{z(-z)}+\frac{x}{z(-y)}+\frac{x}{yz}+\frac{x}{-zz}=\frac{-2x}{z^2}=0$$ which is satisfied when $x$ is zero. Similarly, the edge relation [\[eq:EdgeTwoRelation\]](#eq:EdgeTwoRelation){reference-type="eqref" reference="eq:EdgeTwoRelation"} around edge 2 (defined when $z$ and $x$ are nonzero) is $$\frac{z}{-xz}+\frac{-y}{-zx}+\frac{-z}{-x(-z)}+\frac{-y}{z(-x)}=\frac{2y}{zx}-\frac{2}{x}=0,$$ which is not satisfied. Hence, the reduced Ptolemy variety for $\sigma^1$ consists of a single point given by $(x,y,z)=(0,1,1)$.

### Ptolemy variety for $\sigma^2$

The Ptolemy relations are $$z^2+x^2=yz,\qquad y^2+x^2=-z^2,\qquad z^2+x^2=-yz,$$ which have no non-trivial solution. Hence, the Ptolemy variety $\overline P^{\sigma^2}(\mathcal T)$ is empty.

### Ptolemy variety for $\sigma^3$

The Ptolemy relations are $$z^2+x^2=yz,\qquad y^2+x^2=-z^2,\qquad z^2+x^2=-yz,$$ and setting $z=1$ they are equivalent to $$x^2 + y + 1=0,\qquad y^2 + y + 2=0,\qquad z=1$$ Hence, there are no solutions with $x$ or $y$ being $0$, and $\overline P^{\sigma^3}(\mathcal T)_{\mathop{\mathrm{red}}}$ is defined over the number field $\mathbb Q(w)$, where $w^4+w^2+2=0$, and is given by $x=w$, $y=-w^2-1$, $z=1$.
