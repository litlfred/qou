---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-024-11-examples
section_title: "Examples"
section_number: 11
pages: 21-25
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
text_source: latex
latex_prose_ratio: 0.615
latex_coverage_ratio: 0.845
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:Examples label="sec:Examples"} Let $M$ be the manifold `m009` from the SnapPy census [@SnapPy]. The census triangulation $\mathcal T$ of $M$ is shown in Figure [1](#fig:Trigm009){reference-type="ref" reference="fig:Trigm009"}.

<figure id="fig:Trigm009" data-latex-placement="htb">

<figcaption>Census triangulation of <code>m009</code>. The signs on the faces indicate the obstruction cocycle <span class="math inline"><em>σ</em><sup>3</sup></span>.</figcaption>
</figure>

We refer to the three edges as *edge 1*, *edge 2*, and *edge 3*, according to the number of arrow heads. By inspecting the figure, one checks that there are four transitive edge sets: The non-degenerate edge set where all edges are nonzero, the edge-degenerate edge set where only edge 1 is zero, the edge-degenerate edge set where only edge 2 is zero, and the totally degenerate edge set (which we ignore, see Section [\[sec:TotallyDegenerate\]](#sec:TotallyDegenerate){reference-type="ref" reference="sec:TotallyDegenerate"}). The edge relation around edge 1 is given by $$\begin{equation}
\label{eq:EdgeOneRelation}
\frac{c_{23,0}}{c_{21,0}c_{13,0}}+\frac{c_{01,1}}{c_{03,1}c_{31,1}}+\frac{c_{10,0}}{c_{12,0}c_{20,0}}+\frac{c_{01,2}}{c_{03,2}c_{31,2}}+\frac{c_{23,1}}{c_{21,1}c_{13,1}}+\frac{c_{32,2}}{c_{30,2}c_{02,2}}=0
\end{equation}$$ and the edge relation around edge 2 is given by $$\begin{equation}
\label{eq:EdgeTwoRelation}
\frac{c_{02,0}}{c_{01,0}c_{12,0}}+\frac{c_{30,1}}{c_{31,1}c_{10,1}}+\frac{c_{20,2}}{c_{23,2}c_{30,2}}+\frac{c_{12,1}}{c_{13,1}c_{32,1}}=0.
\end{equation}$$ Since there is no transitive edge set where edge 3 is zero (except the totally degenerate edge set), Theorem [\[thm:Reduced\]](#thm:Reduced){reference-type="ref" reference="thm:Reduced"} implies that the reduced Ptolemy variety (all variants) is given by setting the Ptolemy coordinate of edge 3 equal to $1$.

## The Ptolemy variety $\overline P(\mathcal T)$ {#sec:SLexample}

The identification relations corresponding to the three edges are $$\begin{equation}
\begin{gathered}
c_{23,0}=-c_{23,2}=-c_{01,1}=c_{01,2}=-c_{01,0}=-c_{23,1}\\
c_{13,0}=c_{12,1}=-c_{13,2}=-c_{03,1}=c_{13,0}\\
c_{13,1}=c_{03,2}=c_{02,0}=c_{12,2}=-c_{02,1}=c_{03,0}=c_{02,2}=c_{12,0}.
\end{gathered}
\end{equation}$$ Letting $x=c_{23,0}$, $y=c_{13,0}$ and $z=c_{13,1}$, the Ptolemy relations $c_{03,i}c_{12,i}+c_{01,i}c_{23,i}=c_{02,i}c_{13,i}$ become $$\begin{equation}
\label{eq:m009PtolemySL}
z^2-x^2=zy,\qquad -y^2+x^2=-z^2,\qquad z^2-x^2=-zy.
\end{equation}$$ One easily checks that the only solution to this is $x=y=z=0$, so the Ptolemy variety $\overline P(\mathcal T)$ is empty. There are thus no irreducible, boundary-unipotent $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations of `m009` (as mentioned in Section [\[sec:PSLPtolemy\]](#sec:PSLPtolemy){reference-type="ref" reference="sec:PSLPtolemy"}, the geometric $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representation has no boundary-unipotent lift to $\mathop{\mathrm{SL}}(2,\mathbb C)$).

## The Ptolemy varieties $\overline P^\sigma(\mathcal T)$ {#sec:PSLexample}

An elementary cohomology computation shows that $H^2(\widehat M;\mathbb Z/2\mathbb Z)=\mathbb Z/2\mathbb Z\oplus\mathbb Z/2\mathbb Z$ and that the three non-trivial classes are represented by cocycles $\sigma^i\in C^2(\widehat M;\mathbb Z/2\mathbb Z)$ whose restrictions $\sigma^i_k$ to the $k$th simplex of $\mathcal T$ are given by $$\begin{equation}
\begin{aligned}

\sigma^1_0&=f_{0}^*+f_{2}^*,\quad&\sigma^1_1&=f_{0}^*+f_{1}^*,\quad&\sigma^1_2&=0,\\
\sigma^2_0&=f_{0}^*+f_{1}^*,\quad&\sigma^2_1&=f_{0}^*+f_{3}^*,\quad&\sigma^2_2&=f_{0}^*+f_{1}^*,\\
\sigma^3_0&=f_{1}^*+f_{2}^*,\quad&\sigma^3_1&=f_{1}^*+f_{3}^*,\quad&\sigma^3_2&=f_{0}^*+f_{1}^*,
\end{aligned}
\end{equation}$$ where $f_{i}^*\in C^2(\Delta;\mathbb Z/2\mathbb Z)$ denotes the cochain taking the face $f_{i}$ opposite vertex $i$ to $-1$ and all other faces to $1$. The cocycle $\sigma^3$ is indicated in Figure [1](#fig:Trigm009){reference-type="ref" reference="fig:Trigm009"}.

One easily checks that $\sigma^i_k=\delta(\eta_k^i)$, where $\eta^i_k$ is given by $$\begin{equation}
\begin{aligned}
\eta^1_0&=\varepsilon_{13}^*,\quad&\eta^1_1&=\varepsilon_{23}^*,\quad&\eta^1_2&=0,\\
\eta^2_0&=\varepsilon_{23}^*,\quad&\eta^2_1&=\varepsilon_{12}^*,\quad&\eta^2_2&=\varepsilon_{23}^*,\\
\eta^3_0&=\varepsilon_{03}^*,\quad&\eta^3_1&=\varepsilon_{02}^*,\quad&\eta^3_2&=\varepsilon_{23}^*,
\end{aligned}
\end{equation}$$ where $\varepsilon_{ij}^*\in C^1(\Delta;\mathbb Z/2\mathbb Z)$ is the cochain taking $\varepsilon_{ij}$ to $-1$ and all other edges to $1$. The Ptolemy variety for the trivial obstruction class is equal to $\overline P(\mathcal T)$, which is trivial, as we saw earlier. Recall that the reduced Ptolemy variety is obtained by setting the Ptolemy coordinate $z$ of edge 3 equal to 1.

### Ptolemy variety for $\sigma^1$

The identification relations [\[eq:EdgeIdentificationsSigma\]](#eq:EdgeIdentificationsSigma){reference-type="eqref" reference="eq:EdgeIdentificationsSigma"} are $$\begin{equation}
\begin{gathered}
c_{23,0}=-c_{23,2}=-c_{01,1}=c_{01,2}=-c_{01,0}=c_{23,1}\\
c_{13,0}=-c_{12,1}=c_{13,2}=c_{03,1}=c_{13,0}\\
c_{13,1}=c_{03,2}=c_{02,0}=c_{12,2}=-c_{02,1}=c_{03,0}=c_{02,2}=c_{12,0}.
\end{gathered}
\end{equation}$$ Again, letting $x=c_{23,0}$, $y=c_{13,0}$ and $z=c_{13,1}$, the Ptolemy relations become $$\begin{equation}
\label{eq:m009PtolemyPSL1}
z^2-x^2=zy,\qquad -y^2-x^2=-z^2,\qquad z^2-x^2=zy.
\end{equation}$$ Setting $z=1$, the equations then have the three solutions $$\begin{equation}
(x,y,z)=(0,1,1),\qquad (x,y,z)=(-1,0,1),\qquad (x,y,z)=(1,0,1).
\end{equation}$$ However, not all of these solutions are valid, since the edge equations may not be satisfied. The edge relation [\[eq:EdgeOneRelation\]](#eq:EdgeOneRelation){reference-type="eqref" reference="eq:EdgeOneRelation"} around edge 1 (defined when $y$ and $z$ are nonzero) is $$\begin{equation}
\frac{x}{-zy}+\frac{-x}{y(-z)}+\frac{x}{z(-z)}+\frac{x}{z(-y)}+\frac{x}{yz}+\frac{x}{-zz}=\frac{-2x}{z^2}=0
\end{equation}$$ which is satisfied when $x$ is zero. Similarly, the edge relation [\[eq:EdgeTwoRelation\]](#eq:EdgeTwoRelation){reference-type="eqref" reference="eq:EdgeTwoRelation"} around edge 2 (defined when $z$ and $x$ are nonzero) is $$\begin{equation}
\frac{z}{-xz}+\frac{-y}{-zx}+\frac{-z}{-x(-z)}+\frac{-y}{z(-x)}=\frac{2y}{zx}-\frac{2}{x}=0,
\end{equation}$$ which is not satisfied. Hence, the reduced Ptolemy variety for $\sigma^1$ consists of a single point given by $(x,y,z)=(0,1,1)$.

### Ptolemy variety for $\sigma^2$

The Ptolemy relations are $$\begin{equation}
z^2+x^2=yz,\qquad y^2+x^2=-z^2,\qquad z^2+x^2=-yz,
\end{equation}$$ which have no non-trivial solution. Hence, the Ptolemy variety $\overline P^{\sigma^2}(\mathcal T)$ is empty.

### Ptolemy variety for $\sigma^3$

The Ptolemy relations are $$\begin{equation}
z^2+x^2=yz,\qquad y^2+x^2=-z^2,\qquad z^2+x^2=-yz,
\end{equation}$$ and setting $z=1$ they are equivalent to $$\begin{equation}
 x^2 + y + 1=0,\qquad y^2 + y + 2=0,\qquad z=1
\end{equation}$$ Hence, there are no solutions with $x$ or $y$ being $0$, and $\overline P^{\sigma^3}(\mathcal T)_{\mathop{\mathrm{red}}}$ is defined over the number field $\mathbb Q(w)$, where $w^4+w^2+2=0$, and is given by $x=w$, $y=-w^2-1$, $z=1$.

## The Ptolemy variety $\mathcal E\overline P(\mathcal T)$ and the $A$-polynomial {#sec:Apolyexample}

A fundamental rectangle for the boundary of $M$ is shown in Figure [2](#fig:FundamentalRectangle){reference-type="ref" reference="fig:FundamentalRectangle"}. Using the rules illustrated in Figure [\[fig:FundRectIdentifications\]](#fig:FundRectIdentifications){reference-type="ref" reference="fig:FundRectIdentifications"} we obtain that the identification relations are given by

<figure id="fig:FundamentalRectangle" data-latex-placement="htb">

<figcaption>Fundamental rectangle for <code>m009</code>.</figcaption>
</figure>

$$\begin{equation}
\begin{gathered}
c_{23,0}\overset{t_2}{=}-m^2c_{23,2}\overset{c}{=}-m^2c_{01,1}\overset{d}{=}m^2c_{01,2}\overset{b}{=}-mc_{01,0}\overset{a}{=}-c_{23,1},\\
c_{13,0}\overset{t_1}{=}c_{12,1}\overset{c}{=}-c_{13,2}\overset{d}{=}-c_{03,1},\\
c_{13,1}\overset{d}{=}c_{03,2}\overset{t_2}{=}m^{-1}lc_{02,0}\overset{b}{=}m^{-1}lc_{12,2}\overset{c}{=}-m^{-1}lc_{02,1}\overset{a}{=}lc_{03,0}\overset{t_2}{=}mc_{02,2}\overset{b}{=}c_{12,0},
\end{gathered}
\end{equation}$$ where the symbol $\overset{\alpha}{=}$ indicates that the identification is via the face pairing $\alpha$. Hence, the Ptolemy relations become $$\begin{equation}
\label{eq:ExmlPtolemy}
mz^2-lx^2-m^2yz,\qquad m^2ly^2-lx^2-m^3z^2,\qquad m^5z^2-lx^2+m^3lyz.
\end{equation}$$ One easily checks that there are no non-trivial solutions with $x=0$. The edge relation [\[eq:EdgeEquationsEnhanced\]](#eq:EdgeEquationsEnhanced){reference-type="eqref" reference="eq:EdgeEquationsEnhanced"} around edge 2 is $$\begin{equation}
\frac{ml^{-1}z}{-m^{-1}xz}+\frac{y}{(-z)m^{-2}x}+\frac{-m^{-1}z}{-m^{-2}x(-z)}+\frac{y}{zx}=0\iff m^2z+m^2ly+mlz-ly=0
\end{equation}$$ Adding this equation to the Ptolemy relations [\[eq:ExmlPtolemy\]](#eq:ExmlPtolemy){reference-type="eqref" reference="eq:ExmlPtolemy"} and substituting $z=1$, one can check (using magma [@Magma]) that the system is equivalent to $$\begin{equation}
\begin{gathered}
        x^2 + yl - m^8 + 3m^6 + m^5l + m^4 - m^3l - 3m^2 - ml=0,\\
        y^2l + yl^2 + m^4l - m^3 - m^2l - ml^2 - m - l=0,\\
        ym + yl + m^4 - m^2 - ml - 1=0,\\
        yl^3 - yl - m^5l + m^4l^2 + m^3l + m^2 - ml^3 + 2ml - l^2=0,\\
        m^6l - 2m^4l - m^3l^2 - m^3 - 2m^2l + l=0.
\end{gathered}
\end{equation}$$ This shows that the $A$-polynomial of `m009` is given by $$\begin{equation}
A(m,l)=m^6l - 2m^4l - m^3l^2 - m^3 - 2m^2l + l.
\end{equation}$$ It also follows that $\mathcal E\overline P(\mathcal T)$ is a branched cover over the $A$-polynomial curve of degree 2. Another magma computation shows that it is given explicitly by $$\begin{equation}
\label{eq:EPOverA}
x^2=-\frac{-m^4-2m^3l+ml}{l^2(m^2-1)},\qquad y=-\frac{m^2+ml}{m^2l - l},\qquad z=1,\qquad A(m,l)=0.
\end{equation}$$ Note that $y$ and $x^2$ are regular functions on the $A$-polymial curve.

## Recovering the representations {#sec:RecoverRepExample}

The dual triangulation of `m009` has an oriented edge for each of the face pairings $a$, $b$, $c$, $d$, $t_1$, and $t_2$. The edges $t_1$ and $t_2$ form a maximal tree, so the fundamental group of `m009` is generated by $a$, $b$, $c$, and $d$. By inspecting Figure [2](#fig:FundamentalRectangle){reference-type="ref" reference="fig:FundamentalRectangle"} we see that $$\begin{equation}
\pi_1(M)=\langle a,b,c,d\bigm \vert cd^{-1}a^{-1},cb^{-1}d^{-1}ba,ca^{-1}bd^{-1}\rangle,
\end{equation}$$ and that the meridian $\mu$ and longitude $\lambda$ are given by $$\begin{equation}
\mu=acb^{-1},\qquad \lambda=d^{-1}cd^{-1}bc^{-1}db^{-1}.
\end{equation}$$ One also checks that the generators may be represented by edge paths in the truncated complex as follows: $$\begin{equation}
\begin{aligned}
a&=\beta^0_{23,0}\alpha_{03,0}\beta^0_{23,1}\alpha_{03,1}\beta^3_{01,1}(\beta^2_{01,0})^{-1}\alpha_{02,0}^{-1}\\
b&=\alpha_{02,0}\beta^2_{01,0}\alpha_{12,0}^{-1}(\beta^0_{23,0})^{-1}\\
c&=\beta^0_{23,0}\alpha_{03,0}\beta^3_{01,0}\alpha_{12,1}^{-1}(\beta^3_{01,2})^{-1}\alpha_{03,2}^{-1}\\
d&=\alpha_{02,0}\beta^2_{01,0}\alpha_{12,0}^{-1}.
\end{aligned}
\end{equation}$$ One can then compute the representations explicitly using the formulas for $\alpha_{ij}$ and $\beta^k_{ij}$ given by Proposition [\[prop:ConcreteFormula\]](#prop:ConcreteFormula){reference-type="ref" reference="prop:ConcreteFormula"}.

### The representation with obstruction class $\sigma^1$ {#sub:Reducible}

We obtain $$\begin{equation}
\label{eq:ReducedRep}
a=c=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad b=d=I,\qquad\mu=-\lambda=I.
\end{equation}$$ This shows that the Ptolemy variety can detect reducible representations. It is boundary-degenerate as it must be by Proposition [\[prop:ReducibleDegenerate\]](#prop:ReducibleDegenerate){reference-type="ref" reference="prop:ReducibleDegenerate"}.

### The representations with obstruction class $\sigma^3$

We obtain $$\begin{equation}
\begin{gathered}
a=\begin{pmatrix}w^3+w&1\\1&-w\end{pmatrix},\qquad b=\begin{pmatrix}1&-w\\-w&w^2+1\end{pmatrix},\qquad c=\begin{pmatrix}w^3&1\\w^2+1&-w\end{pmatrix}\\
d=\begin{pmatrix}1&0\\-w&1\end{pmatrix},\qquad \mu=\begin{pmatrix}1&w\\0&1\end{pmatrix},\qquad \lambda=\begin{pmatrix}-1&2w^3+w\\0&-1\end{pmatrix}.
\end{gathered}
\end{equation}$$ One easily checks that $H^1(\widehat M;\mathbb Z/2\mathbb Z)=\mathbb Z/2\mathbb Z$. Hence, by Theorem [\[thm:MainThmPSL\]](#thm:MainThmPSL){reference-type="ref" reference="thm:MainThmPSL"} there should be only two $\mathop{\mathrm{PSL}}(2,\mathbb C)$ representations, not four. Indeed, replacing $w$ by its Galois conjugate $-w$ corresponds to conjugating the representation by the diagonal matrix with entries $\sqrt{-1}$ and $-\sqrt{-1}$. Note that the fixed field of the Galois isomorphism $w\mapsto -w$ is $\mathbb Q(\sqrt{-7})$, which is the shape field of `m009`. The two representations detected are the geometric representation and its complex conjugate.

### The non-boundary-unipotent representations {#sub:TautologicalRep}

Representing the generators by edge paths in the fattened truncated complex, we have $$\begin{equation}
\begin{aligned}
a&=\beta^0_{23,0}\alpha_{03,0}\beta^0_{23,1}\alpha_{03,1}\beta^3_{01,1}(\beta^2_{01,0})^{-1}\alpha_{02,0}^{-1}\\
b&=\alpha_{02,0}\beta^2_{01,0}\alpha_{12,0}^{-1}M^{-1}L^{-1}(\beta^0_{23,0})^{-1}\\
c&=\beta^0_{23,0}\alpha_{03,0}\beta^3_{01,0}\alpha_{12,1}^{-1}(\beta^3_{01,2})^{-1}\alpha_{03,2}^{-1}L^{-1}\\
d&=\alpha_{02,0}\beta^2_{01,0}\alpha_{12,0}^{-1}L^{-1},
\end{aligned}
\end{equation}$$ where $M=\left(\begin{smallmatrix}m&0\\0&m^{-1}\end{smallmatrix}\right)$ and $L=\left(\begin{smallmatrix}l&0\\0&l^{-1}\end{smallmatrix}\right)$. Using this, we obtain $$\begin{equation}
\begin{gathered}
a=\begin{pmatrix}\frac{-(m+l)x}{m^4-m^2}&\frac{l^2}{m^2}\\\frac{-1}{ml}&\frac{-lx}{m^2}\end{pmatrix},\qquad b=\begin{pmatrix}\frac{1}{m^2}&\frac{l^2x}{m^3}\\\frac{-x}{m^2l}&\frac{m^2+ml}{m^2-1}\end{pmatrix},\qquad c=\begin{pmatrix}\frac{-(ml+1)x}{m^4-m^2}&\frac{l^2}{m}\\\frac{m+l}{l^2(m^2-1)}&\frac{-lx}{m}\end{pmatrix}\\
d=\begin{pmatrix}m^{-1}&0\\\frac{-x}{ml}&m\end{pmatrix},\qquad \mu=\begin{pmatrix}m&\frac{-l^2x}{m^2}\\0&m^{-1}\end{pmatrix},\qquad \lambda=\begin{pmatrix}l&\frac{(-l^3+l)x}{m^3-m}\\0&l^{-1}\end{pmatrix},
\end{gathered}
\end{equation}$$ where $x$ is given by [\[eq:EPOverA\]](#eq:EPOverA){reference-type="eqref" reference="eq:EPOverA"}.

::: remark
[]{#rm:EnhancedPSLExample label="rm:EnhancedPSLExample"} As mentioned in Section [\[sec:PtolemyBrief\]](#sec:PtolemyBrief){reference-type="ref" reference="sec:PtolemyBrief"} one also has a Ptolemy variety $\mathcal E\overline P(\mathcal T)^\sigma_{\mathop{\mathrm{red}}}$. This variant only depends on the image of $\sigma$ in the cokernel of the canonical map $H^1(\partial M;\mathbb Z/2\mathbb Z)\to H^2(M,\partial M;\mathbb Z/2\mathbb Z)$. For `m009` this cokernel is $\mathbb Z/2\mathbb Z$, and $\mathcal E\overline P(\mathcal T)^\sigma_{\mathop{\mathrm{red}}}$ for the generator turns out to have two additional components giving rise to curves of $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representations that don't lift to $\mathop{\mathrm{SL}}(2,\mathbb C)$ (and therefore not detected by $\mathcal E\overline P(\mathcal T)_{\mathop{\mathrm{red}}}$). One of these components is a component of dihedral representations that are deformations of the representation [\[eq:ReducedRep\]](#eq:ReducedRep){reference-type="eqref" reference="eq:ReducedRep"}.
:::

## Acknowledgment {#acknowledgment .unnumbered}

We thank Stavros Garoufalidis, Walter Neumann and Henry Segerman for helpful discussions.
