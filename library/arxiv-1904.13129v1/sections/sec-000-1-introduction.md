---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.888
latex_coverage_ratio: 0.957
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
Knots have always played an important role in arts and crafts, commerce and trade, as well as in our everyday life. Therefore they naturally became a topic of interest for mathematicians. During the 19th century the study of knots strongly influenced the development of topology [@TvdG96]. Today the theory of knots appears in several branches of mathematics such as in calculus of variations, geometric analysis, topology as well as in applications to modern quantum physics (e.g. [@K05]) and biochemistry (e.g. protein molecules [@KS98] or DNA [@CKS98; @GM99]).

A knot in mathematical terms is a Jordan curve in the three-dimensional Euclidean space (i.e. a continuous embedding of the circle $\mathbb{R}/ \mathbb{Z}$ into $\mathbb{R}^3$). We say that two given knots belong to the same knot class if one knot can be deformed into the other without any 'cuttings and gluings' nor any self-intersections. Within this context, the following two questions arise: Is it possible to determine 'nicely' shaped representatives of each knot class? And if so, how 'nice' are they?

The first question was originally addressed by Fukuhara [@F88] in the context of polygonal knots. In order to detect optimal shapes of a polygonal knot, an energy modelling a form of self-avoidance on the space of polygonal knots was introduced---from which optimal shapes can be identified as energy minimizers. Subsequently, O'Hara [@OH91; @OH92-2] extended Fukuhara's approach to geometric knots. For any Jordan curve $\gamma: \mathbb{R}/ \mathbb{Z}\rightarrow\mathbb{R}^3$, he introduced the potential energies $$\begin{aligned}
\label{defn:O'Hara's knot energies}
\mathcal{E}^{\alpha,p}(\gamma) = \iint_{(\mathbb{R}/ \mathbb{Z})^2} \left(\frac{1}{|\gamma(x)-\gamma(y) |^\alpha} - \frac{1}{\mathcal{D}(\gamma(x),\gamma(y))^\alpha} \right)^p |\dot{\gamma}(x)| |\dot{\gamma}(y)| \mathrm{d}x \mathrm{d}y.
\end{aligned}$$ Here the quantity $\mathcal{D}(\gamma(x),\gamma(y))$ denotes the intrinsic distance between the points $\gamma(x)$ and $\gamma(y)$ along the curve, i.e. for $|x-y|\leq \frac{1}{2}$ we have $$\begin{aligned}
\mathcal{D}(\gamma(x),\gamma(y)) = \min \{\mathcal{L}(\gamma|_{[x,y]}), \mathcal{L}(\gamma) - \mathcal{L}(\gamma|_{[x,y]}) \},
\end{aligned}$$ where $\mathcal{L}(\gamma) = \int_0^1 |\dot{\gamma} (t)| \mathrm{d}t$ denotes the length of the curve $\gamma$. All values of $\mathcal{E}^{\alpha,p}$ are non-negative due to the fact that the intrinsic distance between two points of the curve is always greater than the Euclidean distance. The factor $|\gamma'(x)| |\gamma'(y)|$ guarantees the invariance of $\mathcal{E}^{\alpha,p}$ under reparametrization of the curve. In addition, $\mathcal{E}^2=\mathcal{E}^{2,1}$ is called Möbius energy since it is invariant under Möbius transformations (cf. [@FHW94 Theor. 2.1]). For $p \geq 1$ and $0 < \alpha p < 2p +1$ the energies $\mathcal{E}^{\alpha,p}$ are globally minimized by circles, whereas for $\alpha p \geq 2p +1$ their values become infinite for every closed regular curve (cf. [@ACFGH03 Corol. 3]).

To distinguish between knot classes, it is desirable for a knot energy to be self-repulsive (i.e.  to penalize self-intersections) and tight (i.e.  to blow up on a sequence of small knots that pull tight). O'Hara showed that the knot energies $\mathcal{E}^{\alpha,p}$ are indeed self-repulsive for the cases $p \geq \tfrac 2\alpha$, $0< \alpha \leq 2$ and $\tfrac{1}{\alpha-2}> p \geq  \tfrac 2\alpha$, $2< \alpha \leq 4$ (cf. [@OH94 Theor. 1.1]) and tight if and only if $\alpha p >2$ (cf. [@OH92-2 Theor. 3.1]). Moreover, [@OH94 Theor. 3.2] showed that for $\alpha p > 2$ there exist minimizers of the energies within every knot class among all curves with fixed length. In case of the Möbius energy, we also have self-repulsiveness but not tightness (cf. [@OH94 Theor. 3.1]) and we only know that there exist minimizers in prime knot classes (cf. [@FHW94 Theor. 4.3]). We see that due to the well-definedness and existence of minimizers of a certain range of O'Hara's energies $\mathcal{E}^{\alpha,p}$, this approach for answering our first question looks promising.

In the following we want to focus on the second question by determining the regularity properties of minimizers of the knot energies. For that reason we restrict ourselves to examining O'Hara's energies $\mathcal{E}^\alpha = \mathcal{E}^{\alpha,1}$ for $2\leq \alpha <3$ as they are well-defined in a knot-theoretic sense and have a non-degenerate first variation (in contrast to the $p>1$ case). For the Möbius energy, one of the first regularity results goes back to He [@H00 Chap. 5] who states, based on Freedman, He and Wang's work [@FHW94 Theor. 5.4], that any local minimizer $\gamma$ of $\mathcal{E}^2$ with respect to the $L^\infty$-topology belongs to $C^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R}^3)$. Reiter [@R12] generalized this result to the class of O'Hara's knot energies $\mathcal{E}^\alpha$ for $2\leq \alpha <3$ and $n\geq 3$ by showing that any critical point $\gamma$ of $\mathcal{E}^\alpha$ in the class $H^\alpha(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ with $\gamma ''\in L^2(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ is smooth. A subsequent improvement on the energy space conditions furnishes the following $C^\infty$-result.

::: thm
[]{#smooth label="smooth"} Let $\gamma:\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n$ be a simple closed Lipschitz-continuous arc-length parametrized curve with $\gamma \in H^{\frac{\alpha +1}{2},2}(\mathbb R / \mathbb Z, \mathbb R^n)$ for any $2< \alpha<3$. If $\gamma$ is a critical point of $\mathcal{E}^\alpha + \lambda \mathcal{L}$, i.e. $$\begin{aligned}
    \delta \mathcal{E}^\alpha(\gamma;h) + \lambda \int_{\mathbb{R}/ \mathbb{Z}} \langle \dot{\gamma}, \dot{h} \rangle \mathrm{d} x = 0 
    \quad \text{for all} \quad h\in H^{\frac{\alpha +1}{2},2}(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n),
    
\end{aligned}$$ then $\gamma$ belongs to $C^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$.
:::

An important characterization of curves with finite O'Hara energy goes back to Blatt [@B12] who showed that curves $\gamma$ have finite energy $\mathcal{E}^{\alpha}(\gamma) < \infty$ if and only if they belong to the fractional Sobolev space $H^{\frac{\alpha +1}{2},2}(\mathbb R / \mathbb Z, \mathbb R^n)$. This result, combined with Theorem [\[smooth\]](#smooth){reference-type="ref" reference="smooth"}, raises the question whether critical points of O'Hara's energies $\mathcal{E}^\alpha$ of finite energy are not only smooth but also analytic. For the Möbius energy $\mathcal{E}^2$ this question was solved in the affirmative by [@BV19]. One might conjecture that it is possible to transfer this result to the energy classes $\mathcal{E}^\alpha$ for $2< \alpha<3$. Unlike the Möbius energy case, the first variation of $\mathcal{E}^\alpha$ for $2< \alpha<3$ leads to the appearance of a fractional derivative of the product of two functions. The latter is subsequently analyzed via a new fractional Leibniz rule instead of the bilinear Hilbert transform, which was used in the Möbius energy case.

The main result of this article confirms the above analyticity conjecture, namely:

::: thm
[]{#main label="main"} Let $\gamma :\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n$ be a closed simple arc-length parametrized curve in $C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$. If $\gamma$ is a critical point of O'Hara's energy $\mathcal{E}^\alpha$, $2< \alpha<3$, with a length term $\mathcal{L}$, i.e. $\mathcal{E}^\alpha + \lambda \mathcal{L}$, then the curve $\gamma$ is analytic.
:::

This theorem, together with the characterization of the energy spaces in [@B12] and Theorem [\[smooth\]](#smooth){reference-type="ref" reference="smooth"}, implies the following:

::: cor
[]{#maincor label="maincor"} Let $\gamma :\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n$ be a closed simple arc-length parametrized curve with $\mathcal{E}^\alpha (\gamma) < \infty$ for $2< \alpha<3$. If $\gamma$ is a critical point of $\mathcal{E}^\alpha + \lambda \mathcal{L}$, then the curve $\gamma$ is analytic.
:::

Note that we study critical points of O'Hara's energy $\mathcal{E}^\alpha$ subject to a Lagrange multiplier length term since $\mathcal{E}^\alpha$ for $2<\alpha <3$ is not scale-invariant in contrast to the Möbius energy case.

### **Exposé of the present work.**

The main goal of this article is to give a rigorous proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. We adapt the methods from the Möbius energy case in [@BV19] to generate a proof which is as elementary as possible. For the convenience of the reader we will provide detailed proofs in this article on the one hand to emphasize the differences to [@BV19] and, on the other hand, to make the article comprehensible without the need for a detailed reading of [@BV19].

In Section [\[sec:preliminaries\]](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"} we recall some basic definitions and properties of fractional Sobolev spaces and Fourier series. We also characterize analytic functions and state an ordinary differential equation (ODE)-version of the theorem of Cauchy-Kovalevskaya. We close the preliminaries with recapitulating Faà di Bruno's formula. In Section [\[section:decomposition\]](#section:decomposition){reference-type="ref" reference="section:decomposition"} we decompose the first variation of O'Hara's energies into the orthogonal projection of a main part $Q^\alpha$ and two remaining parts $R_1^\alpha$ and $R_2^\alpha$ of lower order. The main part $Q^\alpha$ and its derivatives are estimated in Section [\[sec:maintermQ\]](#sec:maintermQ){reference-type="ref" reference="sec:maintermQ"}. Since the orthogonal projection of $Q^\alpha$ appears in the first variation of O'Hara's energies, we estimate the tangential part of $Q^\alpha$ using new estimates for a kind of fractional derivative of a product of two functions that, in Section [\[sec:bilinearHilberttransform\]](#sec:bilinearHilberttransform){reference-type="ref" reference="sec:bilinearHilberttransform"}, that behave like a fractional Leibniz rule. In Section [\[sec:bilinearHilberttransform\]](#sec:bilinearHilberttransform){reference-type="ref" reference="sec:bilinearHilberttransform"} and Section [\[sec:remaining parts\]](#sec:remaining parts){reference-type="ref" reference="sec:remaining parts"} we cut-off the singularities of the singular integrals involved and derive uniform estimates. More precisely, in Section [\[sec:remaining parts\]](#sec:remaining parts){reference-type="ref" reference="sec:remaining parts"} we rewrite the orthogonal projection of the truncated remaining terms so that they may be expressed by integrals over analytic functions. In Section [\[sec:mainpart\]](#sec:mainpart){reference-type="ref" reference="sec:mainpart"} we realize that estimates do not depend on the cut-off parameter and hold for the orthogonal projections of $Q^\alpha$, $R_1^\alpha$, $R_2^\alpha$, and its derivatives. Finally, we will use the estimates to prove Theorem [\[main\]](#main){reference-type="ref" reference="main"} using Cauchy's method of majorants.
