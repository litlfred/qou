---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-015-44-strengthening-the-generalized-quantum-modular
section_title: "Strengthening the generalized quantum modularity conjecture"
section_number: 4.4
pages: 27-28
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.989
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.4.4 label="sub.4.4"}

So far we have generalized the original quantum modularity conjecture [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"} in two very different ways: in Section [\[sub.GQMC\]](#sub.GQMC){reference-type="ref" reference="sub.GQMC"}, we extended it from the Kashaev invariant $J=J^{(\sigma_0)}$ to the functions defined in [\[cherries\]](#cherries){reference-type="eqref" reference="cherries"}, and in the last three subsections we refined it by adding additional terms of lower order to the right-hand side. Not surprisingly, these two can be combined, but with some new aspects.

If we repeat the calculations described in the previous subsection (using smooth truncation for all the $\Phi$-series occurring) but with the function $J^{(K)}=J^{(K,\sigma_0)}$ replaced by the function defined in [\[cherries\]](#cherries){reference-type="eqref" reference="cherries"} with $\sigma\ne\sigma_0$, then instead of [\[strongRQMC\]](#strongRQMC){reference-type="eqref" reference="strongRQMC"} we find $$\label{RQMCa}
{\rm e}^{-v(\sigma)\lambda_\gamma(X)}
J^{(K,\sigma)}\left(\frac{aX+b}{cX+d}\right)
 \overset?\approx
\sum_{\substack{\sigma'\in\mathcal P_K^{\text{red}}}}
J^{(K,\sigma,\sigma')}(X)
 \widehat\Phi^{(K,\sigma')}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right) ,$$ where $J^{(K,\sigma,\sigma')}$ are 1-periodic functions on $\mathbb Q$ with $J^{(K,\sigma,\sigma_1)}(x) =J^{(K,\sigma)}(x)$ (cf. [\[GQMC\]](#GQMC){reference-type="eqref" reference="GQMC"}). There are, however, three main differences with [\[strongRQMC\]](#strongRQMC){reference-type="eqref" reference="strongRQMC"}. The first is that the automorphy factor ${(cX+d)^{3/2}}$ is replaced for $\sigma\ne\sigma_0$ by the factor ${\rm e}^{-v(\sigma)\lambda_\gamma(X)}$ involving the $\sigma$-th volume $v(\sigma)$ (which is zero for ${\sigma=\sigma_0}$). The second is that the Habiro power series , which in [\[strongRQMC\]](#strongRQMC){reference-type="eqref" reference="strongRQMC"} had the coefficient 1, now does not occur at all. The third is that the new functions $J^{(K,\sigma,\sigma')}(x)$ are now no longer elements of the Habiro ring when considered as functions of $q=\mathbf{e}(x)$, as was the case for the functions . But they are still $\overline{\mathbb Q}$-valued and have various "Habiro-like" properties, including the following:

-   $J^{(K,\sigma,\sigma')}(x)$ for $x\in\mathbb Q/\mathbb Z$ is the constant term of a power series  lying in the same space as the power series , as discussed briefly after [\[as41at5\]](#as41at5){reference-type="eqref" reference="as41at5"} and in more detail in Section [\[sec.arithmetic\]](#sec.arithmetic){reference-type="ref" reference="sec.arithmetic"}, i.e., it belongs to $\mu \delta^{-1/2}\sqrt[m]{\varepsilon} F_\sigma(\zeta_m)[[h]]$ with the same root of unity $\mu$, the same element $\delta_\sigma$ of $F_\sigma^\times$, the same set $S$ of primes of $F_\sigma$ (independent of $x$) and the same $S$-unit $\varepsilon=\varepsilon_x$ of $F_\sigma(\zeta_m)$ as for .

-   one can interpret $\Phi^{(K,\sigma,\sigma')}_x(h)$ as $\mathcal{Q}\big(\mathbf{e}(x){\rm e}^{-h}\big)$ where $\mathcal{Q}$ is an element of a Habiro ring $\mathcal H_{F_\sigma}$ generalizing the ordinary Habiro ring $\mathcal H=\mathcal H_\mathbb Q$ whose definition and arithmetic properties will be discussed in a planned joint paper with Peter Scholze and Campbell Wheeler [@GSZ:habiro]. In particular, for primes $p$ that split completely in $F_\sigma$, there are congruence properties modulo $p$ relating, for instance, the first $p$ coefficients of $\mathcal{Q}\big({\rm e}^{-h}\big)$ to the value of $\mathcal{Q}(\zeta_p)$.

We can write equation [\[RQMCa\]](#RQMCa){reference-type="eqref" reference="RQMCa"} more uniformly by allowing the case of $\sigma=\sigma_0$, but remembering that there is then an automorphy factor $(cX+d)^{-3/2}$ that is not present for $\sigma\in\mathcal P_K$. Then all of the formulas found so far can be collected into a single conjectural formula $$\begin{gathered}
\label{RQMC}
{\rm e}^{-v(\sigma)\lambda_\gamma(X)} (cX+d)^{-\kappa(\sigma)}

J^{(K,\sigma)}\left(\frac{aX+b}{cX+d}\right)
 \overset?\approx
\sum_{\sigma'\in\mathcal P_K}

J^{(K,\sigma,\sigma')}(X)
\widehat\Phi^{(K,\sigma')}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)\!\!\!
\end{gathered}$$ valid for all $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$ and all $\sigma\in\mathcal P_K$ for $X\to\infty$ with bounded denominator, where are periodic functions belonging to a generalized Habiro ring and satisfying  and (as introduced in the previous section), with the weight $\kappa_\sigma$ and the multiplier $\lambda_\gamma(X)$ defined as in [\[tweakdef\]](#tweakdef){reference-type="eqref" reference="tweakdef"} and [\[Defwsigma\]](#Defwsigma){reference-type="eqref" reference="Defwsigma"}.

As a concrete illustration of the refined QMC [\[RQMC\]](#RQMC){reference-type="eqref" reference="RQMC"} we take once again the figure 8 knot with $\sigma=\sigma_1$. Here, [\[RQMC\]](#RQMC){reference-type="eqref" reference="RQMC"} involves three terms $\sigma'=\sigma_0,\sigma_1,\sigma_2$, with two of the three coefficients already known (the first vanishes and the second is $J^{(4_1,\sigma_1)}(X)$) but with the third one being a new periodic function on $\mathbb Q$ given explicitly by $$\begin{gathered}
J^{(4_1,\sigma_1,\sigma_2)}(x)
= \frac {\rm i}{2\sqrt[4]{3}\sqrt{c}}
\sum_{Z^c = \zeta_6} \big(Z q -Z^{-1} q^{-1}
\big) \prod_{j=1}^c \bigl|1 - q^jZ\bigr|^{2j/c},\nonumber
\\
c=\mathrm{den}(x),\quad q=\mathbf{e}(x) ,\label{Q1for41}
\end{gathered}$$ which is related to the function given in [\[Def41J1\]](#Def41J1){reference-type="eqref" reference="Def41J1"} in exactly the same way as $Q^{(4_1)}_{\sigma_2}(x)$ and $J^{(4_1)}(x)$ are related by [\[Q0for41\]](#Q0for41){reference-type="eqref" reference="Q0for41"} and [\[Hab41\]](#Hab41){reference-type="eqref" reference="Hab41"}. Likewise, the refined QMC [\[RQMC\]](#RQMC){reference-type="eqref" reference="RQMC"} for $4_1$ and for $\sigma=\sigma_2$ leads to the periodic function $J^{(4_1,\sigma_2,\sigma_2)}(x) =-{\rm i} J^{(4_1,\sigma_1,\sigma_2)}(-x)$. We also find the *bilinear identity* $$\label{FirstBilin}

J^{(4_1,\sigma_1,\sigma_1)}(x)  J^{(4_1,\sigma_2,\sigma_2)}(x)  - 
J^{(4_1,\sigma_1,\sigma_2)}(x)  J^{(4_1,\sigma_2,\sigma_1)}(x)  = 1$$ for all $x\in\mathbb Q/\mathbb Z$. (Note also that $J^{(\sigma_1,\sigma_1)}(x)=J^{(\sigma_1)}(x)$ and $J^{(\sigma_2,\sigma_1)}(x)=J^{(\sigma_2)}(x)$.) This identity will be generalized to all knots in Section [\[sec.Matrix\]](#sec.Matrix){reference-type="ref" reference="sec.Matrix"}.
