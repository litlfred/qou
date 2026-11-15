---
doc_id: arxiv-math-0603217v3
doc_title: "A version of the volume conjecture"
section_id: sec-001-2-a-conjecture
section_title: "A conjecture"
section_number: 2
pages: 1-3
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.854
latex_coverage_ratio: 0.906
doc_brief: "A version of the volume conjecture — We propose a version of the volume conjecture that would relate a certain limit of the colored Jones polynomials of a knot to the volume function deﬁned by a"
---
Let $K$ be a knot in $S^3$. Denote by $J_N(K;q)$ the colored Jones polynomial associated to the $N$-dimensional irreducible representation of the Lie algebra $sl(2,\mathbb{C})$ [@Kirillov/Reshetikhin:1989]. We normalize it so that $J_2(K;q)$ is the Jones polynomial [@Jones:BULAM385] and that $J_N(U;q)=1$, where $U$ is the unknot.

We propose the following conjecture as a version of the volume conjecture.

::: conj
[]{#conj:parameterization label="conj:parameterization"} There exists an open subset $\mathcal{O}_{K}$ of $\mathbb{C}$ such that for any $u\in\mathcal{O}_{K}$ the following limit exists: $$\label{eq:limit}
  \lim_{N\to\infty}
  \frac{\log
        J_N\left(
             K;\exp\left(
                     \left(u+2\pi\sqrt{-1}\right)/N
                   \right)
           \right)}
       {N}.$$ Moreover the function of $u$ $$\label{eq:H}
  H(K;u)
  :=
  \left(u+2\pi\sqrt{-1}\right)
  \lim_{N\to\infty}
  \frac{\log
        J_N\left(
             E;\exp\left(
                     \left(u+2\pi\sqrt{-1}\right)/N
                   \right)
           \right)}
       {N}$$ is analytic on $\mathcal{O}_{K}$. If we put $$v_{K}(u)
  :=
  2\frac{d\,H(K;u)}{d\,u}-2\pi\sqrt{-1},$$ then the following formula holds: $$\label{eq:volume}
  V(K;u)
  =
  \operatorname{Im}\bigl(H(K;u)\bigr)-\pi\operatorname{Re}(u)-\frac{1}{2}\operatorname{Re}(u)\operatorname{Im}\bigl(v_{K}(u)\bigr),$$ where $V(K;u)$ is the volume function corresponding to the representation from $\pi_1(S^3\setminus{K})$ to $SL(2;\mathbb{C})$ sending the meridian and the longitude to the elements the ratios of whose eigenvalues are $\exp(u)$ and $\exp\bigl(v_{K}(u)\bigr)$ respectively [@Cooper/Culler/Gillet/Long/Shalen:INVEM1994 § 4.5].
:::

::: rem
[]{#rem:Dehn label="rem:Dehn"} If there exist coprime integers $p$ and $q$ satisfying $pu+qv_{K}(u)=2\pi\sqrt{-1}$, then $u$ would define the $(p,q)$-Dehn surgery along $K$ [@Thurston:GT3M]. If this is a hyperbolic manifold, $V(K;u)$ is its hyperbolic volume.
:::

::: rem
The open set $\mathcal{O}_{K}$ may not contain $0$. Therefore Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"} is *not* a generalization of the volume conjecture. (Recall that the volume conjecture [@Kashaev:LETMP97; @Murakami/Murakami:ACTAM12001] states that when $u=0$, then the limit [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"} gives the simplicial volume of the knot complement.) In fact the case where $K$ is a torus knot, the limit [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"} is not continuous at $0$ [@Kashaev/Tirkkonen:ZAPNS2000; @Murakami:INTJM62004]. See also [@Garoufalidis/Le:Kauffman Proposition B.2].
:::

::: rem
[]{#rem:Garoufalidis1 label="rem:Garoufalidis1"} S. Garoufalidis and T. Le proved that if $u$ is close enough to $-2\pi\sqrt{-1}$, then $J_N\left(K;\exp\bigl((u+2\pi\sqrt{-1})/N\bigr)\right)$ converges to $1/\Delta(K;\exp(u+2\pi\sqrt{-1})\bigr)$, where $\Delta(K;t)$ is the Alexander polynomial of $K$ [@Garoufalidis/Le:aMMR]. (See also [@Murakami:2005] for the figure-eight knot.) In this case the right hand side of [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"} vanishes and so we have $H(K;u)=0$ and $v_K(u)=-2\pi\sqrt{-1}$. Therefore from [\[eq:volume\]](#eq:volume){reference-type="eqref" reference="eq:volume"} the volume function $V(K;u)$ vanishes. This corresponds to the case where $u$ defines an abelian representation, whose volume function is zero. See [@Garoufalidis/Le:Kauffman Appendix B]. So we exclude such a case in Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"}.
:::

Note that the conjecture above is proved for the figure-eight knot by Yokota and the author [@Murakami/Yokota:JREIA]. In fact we proved [@Murakami/Yokota:JREIA Corollary 2.4] that for the figure-eight knot $E$ $$V(E;u)
  =
  \operatorname{Im}\bigl(H(E;u)\bigr)-\pi\operatorname{Re}(u)-\frac{1}{4}\operatorname{Im}\bigl(u\,v_E(u)\bigr)
  -\frac{\pi}{2}\operatorname{length}(\gamma),$$ where $\operatorname{length}(\gamma)$ is the length of the geodisic $\gamma$ added to complete the incomplete hyperbolic structure of $S^3\setminus{E}$ corresponding to $u$. But since $\operatorname{length}(\gamma)=-\operatorname{Im}\bigl(u\,\overline{v_E(u)}\bigr)/(2\pi)$ from [@Neumann/Zagier:TOPOL85 (34)], we have $$\begin{split}
  V(E;u)
  &=
  \operatorname{Im}\bigl(H(E;u)\bigr)-\pi\operatorname{Re}(u)-\frac{1}{4}\operatorname{Im}\bigl(u\,v_E(u)\bigr)
  +\frac{1}{4}\operatorname{Im}\bigl(u\,\overline{v_E(u)}\bigr)
  \\
  &=
  \operatorname{Im}\bigl(H(E;u)\bigr)-\pi\operatorname{Re}(u)-\frac{1}{2}\operatorname{Re}(u)\operatorname{Im}\bigl(v_E(u)\bigr)
\end{split}$$ as required.

See also [@Murakami:FUNDM2004 (4.1)]. (The sign of $\pi\operatorname{Re}{u}$ in [@Murakami:FUNDM2004 (4.1)] should be negative because the author used a wrong definition of the function $H$ in the old version of [@Murakami/Yokota:JREIA].)

Note also that Gukov uses a different *polarization* in his generalization of the volume conjecture [@Gukov:COMMP2005 (5.12)]. It agrees with Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"} when $\operatorname{Re}(u)=0$. The difference for $\operatorname{Re}(u)\ne0$ can be explained by a choice of polarization. Details will be described in a forthcoming paper.
