---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
toc_source: outline
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.901
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — We calculate limits of the colored Jones polynomials of the ﬁgure- eight knot and conclude that in most cases they determine"
---
Let $K$ be a knot and $J_N(K;t)$ be the colored Jones polynomial of $K$ in the three-sphere $S^3$ corresponding to the $N$-dimensional representation of $sl_2(\mathbb{C})$ (see for example [@Kirby/Melvin:INVEM91]). We normalize it so that $J_N(\text{unknot};t)=1$.

In [@Kashaev:LETMP97], R. Kashaev introduced a series of numerical link invariants and proposed a conjecture that a limit of his invariants would determines the hyperbolic volume of the complement of a knot if it has a complete hyperbolic structure. On the other hand in [@Murakami/Murakami:ACTAM101] J. Murakami and the first author proved that Kashaev's invariant is equal to the absolute value of $J_N\bigl(K;\exp(2\pi\sqrt{-1}/N)\bigr)$. Moreover in [@Murakami/Murakami/Okamoto/Takata/Yokota:EXPMA02] J. Murakami, M. Okamoto, T. Takata and the authors studies several knots and proposed the following complexification of Kashaev's conjecture.

::: conj
Let $K$ be a hyperbolic knot (that is, the complement of $K$ possesses a complete hyperbolic structure). Then $$2\pi\lim_{N\to\infty}\frac{\log{J_N\bigl(K;\exp(2\pi\sqrt{-1}/N)\bigr)}}{N}
  =
  \operatorname{Vol}(S^3\setminus{K})+\sqrt{-1}\operatorname{CS}(S^3\setminus{K}),$$ where $\operatorname{Vol}$ is the hyperbolic volume and $\operatorname{CS}$ is the Chern--Simons invariant for knots [@Meyerhoff:density].
:::

See [@Murakami:ALDT_VI; @Murakami:Nagoya99; @D.Thurston:Grenoble; @Yokota:Murasugi70; @Yokota:volume00; @Yokota:Topology_Symposium2000; @Yokota:GTM02; @Yokota:INTIS03] for related topics.

On the other hand the first author studied in [@Murakami:KYUMJ2004] other limits of the colored Jones polynomials of the figure-eight knot and showed the following theorem.

::: thm
[]{#thm:real label="thm:real"} Let $E$ be the figure-eight knot and $r$ a irrational number satisfying ${5/6}<{r}<{7/6}$ or $r=1$. Then $$2\pi{r}\lim_{N\to\infty}
  \frac{\log\left|J_N\left(E;\exp(2\pi{r}\sqrt{-1}/N)\right)\right|}{N}$$ is the volume of the cone manifold with cone angle $2\pi|1-r|$ whose singularity is the figure-eight knot.
:::

He also calculated [@Murakami:SURIK00] 'fake' limits (optimistic limits) of the Witten--Reshetikhin--Turaev invariants of three-manifolds obtained from $S^3$ by integral Dehn surgeries along the figure-eight knot and observed they give the volumes and the Chern--Simons invariants of those manifolds.

The purpose of this paper is to show that limits of the colored Jones polynomials of the figure-eignt give the volume and the Chern--Simons invariants of the three-manifold obtained by general surgeries. To do that we study the asymptotic behavior of $J_N(E;\exp(2\pi{r}\sqrt{-1}/N))$ for large $N$ by using the saddle point method with $E$ the figure-eight knot. Then it turns out that it determines the potential function introduced by W. Neumann and D. Zagier [@Neumann/Zagier:TOPOL85] to study the volumes of Dehn surgered spaces along knots. (See also [@Gukov:COMMP2005].) The we apply T. Yoshida's theorem [@Yoshida:INVEM85] to show that the limit of $\log\Bigl(J_N\bigl(E;\exp(2\pi{r}\sqrt{-1}/N)\bigl)\Bigr)/N$ ($N\to\infty$) gives the volume and the Chern--Simons invariant when $r\in\mathbb{C}$ is close to $1$.

::: ack
Part of this work was done during the authors were attending the workshops 'Physics and Geometry of three-dimensional Quantum Gravity' at the International Centre for Mathematical Sciences (ICMS) in Edinburgh, 29 June-5 July 2003, and 'Hyperbolic volume conjecture' at University of Geneva, 8-14 September 2003. The authors thank the organizers and the participants.

Thanks are also due to Hiroshi Isozaki and Rinat Kashaev for their useful conversations.
:::
