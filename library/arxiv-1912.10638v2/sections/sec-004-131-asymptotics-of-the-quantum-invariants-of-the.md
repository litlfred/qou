---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-004-131-asymptotics-of-the-quantum-invariants-of-the
section_title: "Asymptotics of the quantum invariants of the Whitehead link"
section_number: 1.3.1
pages: 4-5
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.779
latex_coverage_ratio: 0.976
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by M1 and all"
---
Let $M_1$ and $M_2$ be sequences of integers in $N$ with limiting ratios $$s_i = \lim_{N \to \infty}\frac{M_i}{N+\frac{1}{2}}$$ We use $WL$ to denote the Whitehead link and $J_{M_1,M_2}(WL,t)$ to denote the colored Jones polynomials of the Whitehead link with the belt colored by $M_1$ and the clasp colored by $M_2$. In the first part of this paper, we study the asymptotic expansion formula for $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$. Our result can be stated as follows

::: theorem
[]{#mainthmWL label="mainthmWL"} For the $(M_1,M_2)$-th colored Jones polynomials of the Whitehead link evaluated at $t=e^{\frac{2\pi i}{N+\frac{1}{2}}}$,

1.  there exist two functions $\Phi^{\pm(s_1,s_2)}(z_1,z_2)$, a triangulation of ${\mathbb S}^3 \backslash WL$ and an assignment of shape parameters such that

    1.  the critical point equations $$\frac{\partial}{\partial z_1}\Phi^{\pm(s_1,s_2)}(z_1,z_2)
        =\frac{\partial}{\partial z_2}\Phi^{\pm(s_1,s_2)}(z_1,z_2)
        =0$$ coincide with the hyperbolic gluing equations for this particular triangulation.

    2.  there exist two families of critical points $\mathbf{z}^{\pm(s_1, s_2)}$ which holomorphically depend on $s_1,s_2$ such that $$\Phi^{+(s_1,s_2)}(\mathbf{z}^{+(z_1,z_2)})
        = \Phi^{-(s_1,s_2)}(\mathbf{z}^{-(z_1,z_2)})$$ and $$\Re \Phi^{\pm(s_1, s_2)}(\mathbf{z}^{\pm(s_1, s_2)}) = \operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2=4\pi i (1 - s_2)\right) ,$$ where $\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2=4\pi i (1 - s_2)\right)$ is the hyperbolic volume of the Whitehead link complement equipped with the incomplete hyperbolic structure such that the logarithm of the holonomy of the meridian of the belt and the logarithm of the holonomy of the longitude of the clasp are $u_1 = 2\pi i (1 - s_1)$ and $v_2=4\pi i (1 - s_2)$ respectively.

2.  We have $$\begin{aligned}
    \lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log \left| J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}}) \right| 
    &= \Re \Phi^{\pm(s_1, s_2)}(\mathbf{z}^{\pm(s_1, s_2)}) \\
    &= \operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2=4\pi i (1 - s_2)\right)
    \end{aligned}$$
:::

As a corollary, by exchanging the components of the Whitehead link, we obtain the following symmetry for the volume function of the Whitehead link complement.

::: corollary
[]{#WLVolsym label="WLVolsym"} We have $$\begin{aligned}
\label{Volsym1}
\operatorname{Vol}({\mathbb S}^3\backslash WL, u_1 = 2\pi i(1-s_1), v_2= 4\pi i(1-s_2))
= \operatorname{Vol}({\mathbb S}^3\backslash WL, v_1= 4\pi i(1-s_1), u_2 = 2\pi i(1-s_2))
\end{aligned}$$ In particular, $$\begin{aligned}
\label{Volsym2}
\operatorname{Vol}({\mathbb S}^3\backslash WL, u_1 = 2\pi i(1-s_1), u_2=0)
= \operatorname{Vol}({\mathbb S}^3\backslash WL, v_1= 4\pi i(1-s_1), u_2 = 0)
\end{aligned}$$
:::

Theorem [\[mainthmWL\]](#mainthmWL){reference-type="ref" reference="mainthmWL"} and Corollary [\[WLVolsym\]](#WLVolsym){reference-type="ref" reference="WLVolsym"} give a positive answer to Conjecture [\[GVCHL\]](#GVCHL){reference-type="ref" reference="GVCHL"} for the sequences of colors $M_1,M_2$ with either $s_1=1$ or $s_2=1$. In the general case, it is not clear to the author whether Theorem [\[mainthmWL\]](#mainthmWL){reference-type="ref" reference="mainthmWL"} could give a positive (or negative) answer to Conjecture [\[GVCHL\]](#GVCHL){reference-type="ref" reference="GVCHL"}.
