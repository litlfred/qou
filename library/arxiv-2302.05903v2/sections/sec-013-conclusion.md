---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-013-conclusion
section_title: "Conclusion"
section_number: null
pages: 13-15
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.524
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
In this paper we raised the trick of [@2212.04859] to the level of a *method*, applicable to a large variety of functions and providing a unified treatment of the so far sporadic set of amusing identities. We emphasize its conceptual relation to the Borel transform, which is used in physics to explain and put under control the ambiguity of divergent series. As we demonstrate, the abilities of our suggested *combinatorial Borel transform* are much wider and applications are not restricted to divergent series. There are plenty of different directions to develop these ideas, and also a number of conceptual questions to resolve, of which we mention just two.

**Basic open questions:**

-   When (for what conditions $\left<S_R\right> = \alpha_R$) does a simple averaging procedure exist? When is the measure Gaussian?

-   How does a trivial Gaussian measure like ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) converts non-trivial series like $F\{p\}=\sum_R q^{|R|}d_R^2 S_R\{p\}$ into a triviality: $\left<F\{p\}\right> = e^q$? What is the role of triangularity (only $p_k$ with $k\leq |R|$ affect the coefficient of $q^{|R|}$)? To what extent and in what sense can the averaging procedure (the combinatorial Borel transform) be invertible?

    For example, after averaging of $$\begin{aligned}
    \sum_R q^{|R|}d_R^2S_R\{p\} = 1 +qp_1 + \frac{q^2p_1^2}{4} + \frac{q^3(5p_1^3-2p_3)}{4\cdot 27} + \frac{q^4(4p_1^4-\frac{3}{2}p_2^2-p_3p_1)}{2^5\cdot 3^3}
    + \frac{q^5(149p_1^5-80p_3p_1^2-75p_2^2p_1+36p_5)}{2^7\cdot 3^3\cdot 5^3} + \ldots
    \nonumber
    \end{aligned}$$ with measure **A** ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) over all $p_k$ but $p_1$, the last step of averaging is $$\begin{aligned}
    e^q = \int_{-\infty}^\infty \frac{e^{-\frac{(p_1-1)^2}{2}} dp_1}{\sqrt{2\pi}}
    \left(1 +qp_1 + \frac{q^2p_1^2}{4} + \frac{q^3(5p_1^3-2)}{4\cdot 27} + \frac{q^4(4p_1^4-p_1-3)}{2^5\cdot 3^3}
    + \frac{q^5(149p_1^5-80p_1^2-150p_1+36)}{2^7\cdot 3^3\cdot 5^3}
    +\ldots \right)
    \nonumber
    \end{aligned}$$

    Clearly this integration is already radical enough to allow for any simple inversion.

-   In the paper, we only started exploration of the combinatorial Borel transform. In particular, we did not discuss the role of analytic continuation within this context. Moreover, we did not discuss in detail when the sums under consideration have different possible types of growth, in particular, a factorial divergence and other types of divergencies (for exception of comments in sec.6). This is especially important in the case of the Hurwitz $\tau$-functions in order to reveal the non-perturbative nature of the large order behaviour in these.

We hope that this new, more general look on a combinatorial generalization of the Borel transform would lead to new insights or, at least, to new amusing relations and formulas, which look artificial from other points of view. There are many of this kind, besides the ones that we mentioned, and now we have a new option to interpret and understand at least some of them.

# Acknowledgements

We are grateful to the referee of our paper for valuable comments. This work was supported by the Russian Science Foundation (Grant No.23-41-00049).
