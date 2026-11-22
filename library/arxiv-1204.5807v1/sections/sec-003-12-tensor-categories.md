---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-003-12-tensor-categories
section_title: "Tensor categories"
section_number: 1.2
pages: 3-4
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.921
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
We refer to [@BK; @McL; @EGNO; @ENO; @EO] for basic results and terminology on tensor and monoidal categories. A monoidal category is one with tensor product and unit, denoted ${\bf 1}$; thus $\operatorname{End}({\bf 1})$ is a monoid. A monoidal category is rigid when it has right and left dualities. In this article, we understand by tensor category a monoidal rigid abelian $\Bbbk$-linear category, with $\operatorname{End}({\bf 1})\simeq \Bbbk$. A particular important class of tensor categories is that of fusion categories, that is semisimple tensor categories with finite set of isomorphism classes of simple objects, that includes the unit object, and finite-dimensional spaces of morphisms. Another important class of tensor categories is that of braided tensor categories, i. e. those with a commutativity constraint $c_{V,W}: V \otimes W \to W {\otimes}V$ for every objects $V$ and $W$. A braided vector space is a pair $(V, c)$ where $V$ is a vector space and $c\in GL(V{\otimes}V)$ satisfies $(c{\otimes}\operatorname{id})(\operatorname{id}{\otimes}c)(c{\otimes}\operatorname{id}) = (\operatorname{id}{\otimes}c)(c{\otimes}\operatorname{id})(\operatorname{id}{\otimes}c)$; this notion is closely related to that of braided tensor category.

## Hopf algebras {#subsec:hopf}

We use standard notation for Hopf algebras (always assumed with bijective antipode); $\Delta$, $\varepsilon$, ${\mathcal S}$, denote respectively the comultiplication, the counit, and the antipode. For the first, we use the Heyneman-Sweedler notation $\Delta(x) = x_{\left( 1 \right)}\otimes x_{\left( 2 \right)}$. The tensor category of finite-dimensional representations of a Hopf algebra $H$ is denoted $\operatorname{Rep}H$ instead of ${{H} {\text -}\operatorname{mod}}$, to stress the tensor structure. There are two duality endo-functors of $\operatorname{Rep}H$ composing the transpose of the action with either the antipode or its inverse: if $M \in \operatorname{Rep}H$, then $M^* = \operatorname{Hom}(M, \Bbbk) = {}^*M$, with actions $$\begin{aligned}
\langle h\cdot f, m\rangle &= \langle f, {\mathcal S}(h)\cdot m\rangle, &
\langle h\cdot g, m\rangle &= \langle g, {\mathcal S}^{-1}(h)\cdot m\rangle,
\end{aligned}$$ for $h\in H$, $f\in M^*$, $g\in {}^*M$, $m\in M$.

The tensor category of finite-dimensional corepresentations of a Hopf algebra $H$, i. e. right comodules, is denoted $\operatorname{Corep}H$. The coaction map of $V\in \operatorname{Corep}H$ is denoted $\rho =\rho_V:V\to V\otimes H$; in Heyneman-Sweedler notation, $\rho(v) = v_{\left( 0 \right)}\otimes v_{\left( 1 \right)}$, $v\in V$. Also, the coaction map of a left comodule $W$ is denoted $\delta =\delta_W: W\to W\otimes H$; that is, $\delta(w) = w_{\left( -1 \right)}\otimes w_{\left( 0 \right)}$, $w\in W$.

A Yetter-Drinfeld module $V$ over a Hopf algebra $H$ is simultaneously a left $H$-module and a left $H$-comodule, subject to the compatibility condition $\delta(h\cdot v) = h_{\left( 1 \right)} v_{\left( -1 \right)}{\mathcal S}(h_{\left( 3 \right)}) {\otimes}h_{\left( 2 \right)}\cdot v_{\left( 0 \right)}$ for $v\in V$, $h\in H$. The category ${}^H_H\mathcal{YD}$ of Yetter-Drinfeld modules over $H$ is a braided tensor category with braiding $c(v{\otimes}w) = v_{\left( -1 \right)}\cdot w {\otimes}v_{\left( 0 \right)}$, see e. g. [@AS-cambr; @Mo]; when $\dim H < \infty$, ${}^H_H\mathcal{YD}$ coincides with the category of representations of the Drinfeld double $D(H)$.

Let $H$ be a Hopf algebra. A basic list of $H$-invariants is

-   The group $G(H)$ of group-like elements of $H$,

-   the coradical $H_0 =$ largest cosemisimple subcoalgebra of $H$,

-   the coradical filtration of $H$.

Assume that $H_0$ is a Hopf subalgebra of $H$. In this case, another fundamental invariant of $H$ is the *infinitesimal braiding*, a Yetter-Drinfeld module $V$ over $H_0$, see [@AS-cambr]. We shall consider two particular cases:

-   The Hopf algebra $H$ is *pointed* if $H_0 = \Bbbk G(H)$.

-   The Hopf algebra $H$ is *copointed* if $H_0 = \Bbbk^G$ for a finite group $G$.

Recall that $x\in H$ is $(g,1)$ skew-primitive when $\Delta(x) = x{\otimes}1 + g{\otimes}x$; necessarily, $g\in G(H)$. If $H$ is generated as an algebra by group-like and skew-primitive elements, then it is pointed.

We shall need the description of *Yetter-Drinfeld modules* over $\Bbbk G$, $G$ a finite group; these are $G$-graded vector spaces $M = \oplus_{g\in G} M_g$ provided with a $G$-module structure such that $g\cdot M_t = M_{gtg^{-1}}$ for any $g,t\in G$. The category $^{\Bbbk G}_{\Bbbk G}\mathcal{YD}$ of Yetter-Drinfeld modules over $G$ is semisimple and its irreducible objects are parameterized by pairs $({\mathcal O}, \rho)$, where ${\mathcal O}$ is a conjugacy class of $G$ and $\rho\in \operatorname{Irr}C_{G}(g)$, $g\in {\mathcal O}$ fixed. We describe the corresponding irreducible Yetter-Drinfeld module $M({\mathcal O}, \rho)$. Let $g_1 = g$, ..., $g_{m}$ be a numeration of ${\mathcal O}$ and let $x_i\in G$ such that $x_i \, g\, x_i^{-1} = g_i$ for all $1\le i \le m$. Then $$M({\mathcal O}, \rho) =\operatorname{Ind}^G_{C_G(g)}V=\oplus_{1\le i \le m} x_i\otimes V.$$ Let $x_iv := x_i\otimes v \in M({\mathcal O},\rho)$, $1\le i \le m$, $v\in V$. The Yetter-Drinfeld module $M({\mathcal O},\rho)$ is a braided vector space with braiding given by $$\label{yd-braiding}
c(x_iv\otimes x_jw) = g_i\cdot(x_jw)\otimes x_iv =
x_h\,\rho(\gamma)(w) \otimes x_iv$$ for any $1\le i,j\le m$, $v,w\in V$, where $g_ix_j = x_h\gamma$ for unique $h$, $1\le h \le m$, and $\gamma \in C_{G}(g)$. Now the categories $^{\Bbbk G}_{\Bbbk G}\mathcal{YD}$ and $^{\Bbbk^G}_{\Bbbk^G}\mathcal{YD}$ are tensor equivalent, so that a similar description of the objects of the latter holds, see e. g. [@AV].

The following notion is appropriate to describe all braided vector spaces arising as Yetter-Drinfeld modules over some finite abelian group. A braided vector space $(V,c)$ is of *diagonal type* if there exist $q_{ij}\in \Bbbk^{\times}$ and a basis $\{x_i\}_{i\in I}$ of $V$ such that $c(x_i {\otimes}x_j)= q _{ij} x_j {\otimes}x_i$, for each pair $i,j\in I$. In such case, we say that $i,j\in I$ are *connected* if there exist $i_k\in I$, $k=0,1,\ldots,n$, such that $i_0=i$, $i_n=j$, and $q_{i_{k-1},i_k}q_{i_k,i_{k-1}}\neq 1$, $1\le k \le n$. It establishes an equivalence relation on $I$. The equivalence classes are called connected components, and $V$ is *connected* if it has a unique component.

When $H=\Bbbk\Gamma$, where $\Gamma$ is a finite abelian group, each $V\in {}^{H}_{H}\mathcal{YD}$ is a braided vector space of diagonal type. Indeed, $V = \oplus_{g\in
\Gamma, \chi\in \widehat{\Gamma}}V_{g}^{\chi}$, where $V_{g} = \{v\in V \mid \delta(v) = g\otimes
v\}$, $V^{\chi} = \{v\in V \mid  g \cdot v = \chi(g)v \text{ for all
} g \in \Gamma\}$, $V_{g}^{\chi}
= V^{\chi} \cap V_{g}$. Note that $c(x\otimes y) =\chi(g) y\otimes x$, for each $x\in V_{g}$, $g \in \Gamma$, $y\in
V^{\chi}$, $\chi \in \widehat{\Gamma}$. On the other hand, we can realize every braided vector space of diagonal type as a Yetter-Drinfeld module over the group algebra of an appropriate abelian group.
