---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-009-chiral-yang-mills-theory-as-a-deformed-hurwitz-t
section_title: "Chiral Yang-Mills Theory as a Deformed Hurwitz Theory"
section_number: null
pages: 13-15
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.903
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
[]{#Premise label="Premise"} We have all the necessary tools in hand to define a deformed Hurwitz theory that is manifestly dual to two-dimensional chiral Yang-Mills theory. As suggested at the end of section [\[YMObservables\]](#YMObservables){reference-type="ref" reference="YMObservables"}, we will focus on the degree $d$ sector of chiral Yang-Mills theory and postpone the discussion of the sum over degrees. Firstly, we consider the fixed-degree correlators of the chiral theory in the strict large $N$ limit: $$\begin{aligned}
    Z^{+}_{d}(U_1,\dots,U_k) &=\sum_{\alpha_1,\dots, \alpha_d\in Y^d} \left(\prod_{i=1}^{k} p_{\alpha_i}(U_i)\right)  \sum_{\lambda\in Y_d} \left(\frac{ d_{\lambda}}{d!}\right)^{2-2g} \prod_{i=1}^{k}  f_{\alpha_i}(\lambda)
    \label{StrictLargeN}\\
    &=H_d\left(\sum_{\alpha} p_{\alpha}(U_1) C_{\alpha},\dots,\sum_{\alpha} p_{\alpha}(U_k) C_{\alpha}\right)
    \, .
\end{aligned}$$ The subscript $+$ denotes the chiral correlators. The sum over Young diagrams on the right-hand side is manifestly a linear combination of Hurwitz number with coefficients that are polynomials in the holonomies. As a result, the degree $d$ sector reduces in the strict large $N$ limit to a Hurwitz theory with gauge group $S_d$. The dictionary of observables sends a holonomy class $U$ in the Yang-Mills theory to an operator $\sum_{\alpha} p_{\alpha}(U) C_{\alpha}$ in the Hurwitz theory.

When the $1/N$ corrections are turned on, the right-hand side of equation [\[ExactCorrelators\]](#ExactCorrelators){reference-type="eqref" reference="ExactCorrelators"} features additional terms compared to the limit [\[StrictLargeN\]](#StrictLargeN){reference-type="eqref" reference="StrictLargeN"}: simple branch points on the one hand, and $\Omega$ operators on the other. One difficulty in establishing a correspondence between two-dimensional Yang-Mills theory and Hurwitz theory lies in the treatment of these $\Omega$ factors.

The novelty in our approach will consist in treating these factors as arising from a deformation of Hurwitz theory.[^1]

There is a modification of the moduli space captured by a factor $\Omega^{2-2G}$ in the partition function [@Cordes:1994fc]. The renormalization of the observables accounts for the additional $\Omega^{-k}$ factor that appears in the Gross-Taylor expansion.

We proceed to define the appropriate deformations of Hurwitz theory. We first incorporate the single branch points by adding the extra term $$\mathcal{L}\to \mathcal{L}- g_s t\cdot C_2 \, 
    \label{TransDeformation}$$ to the exponent of the path integral measure formally represented by a Lagrangian $\mathcal{L}$. The factor $g_s$ denotes the string coupling constant in the dual theory and is identified with $1/N$. It is featured in the perturbation to ensure that the deformation is small for small values of $t$. Indeed, as we shall see in section [\[AStringyDeformation\]](#AStringyDeformation){reference-type="ref" reference="AStringyDeformation"}, whether the deformation parameters are large or small is determined by their value relative to the string coupling.

Furthermore, factoring out $g_s$ allows us to interpret the parameter $t$ as the area of the target space in units of the Yang-Mills coupling $g_{YM}$. We now introduce the $\Omega$ deformation. Recall that the operator $\Omega$ has a natural expression as a linear combination of conjugacy classes. Furthermore, we have the first order estimate $\Omega_{g_s u}=1+\mathcal{O}(g_s u)$, which implies that the logarithm of the operator is well-defined perturbatively. We write $$\mathcal{L}\to \mathcal{L}+ \log \Omega_{g_s u}^{2-2G}\, .
    \label{OmegaDeformation}$$ We have introduced the parameter $u$ to highlight the need to implement the regularization description of the inverse exponential distance operator described in section [\[GTExpansion\]](#GTExpansion){reference-type="ref" reference="GTExpansion"}. In terms of $u$, the prescription consists in evaluating the correlators at $u=1-\epsilon$, dropping the exponentially suppressed terms from the expansion, then taking the limit $\epsilon \to 0$.

The above symbolic representations can be made precise by stating that the correlators of the deformed Hurwitz theory at order $d$ read $$\langle \prod_{i=1}^{k} C_{\alpha_i} \rangle_d^{t,u} 
    =\langle \left(\prod_{i=1}^{k} C_{\alpha_i}\right) e^{-g_s t C_2}\, \Omega_{g_s u}^{2-2G}  \rangle_d\, ,
    \label{DeformedHurwitz}$$ where the superscript $t,u$ on the left-hand side indicates that the parameters of the deformation are $t$ and $u$, respectively. To simplify the notations, we shall use a superscript ${\text{def}}$ to denote the Hurwitz theory deformed by the parameters $t=g_{YM}^2 A$ and $u=1$, up to a regularization procedure. Comparing with the expression for the fixed-degree Yang-Mills correlators in the large $N$ limit [\[ExactCorrelators\]](#ExactCorrelators){reference-type="eqref" reference="ExactCorrelators"}, we find that agreement between the correlators of both theories necessitates that the operators of the Hurwitz theory be renormalized as $$C_{\alpha}\to \hat{C}_{\alpha}:=\Omega_{g_s u}^{-1} C_{\alpha}\, .$$ The inverse exponential distance operator $\Omega_{g_s u}^{-1}$ is an element of the conjugacy class algebra $\mathcal{C}_d$. Therefore, the renormalized class $\hat{C}_{\alpha}$ is a well-defined operator in this algebra.

We may finally equate the perturbative expansion of the correlators on both sides of the chiral theory $$Z_{d}^{+}[M_G,U_i]=\langle \prod_{i} \left(\sum_{\alpha\vdash d} p_{\alpha}(U_i) \hat{C}_{\alpha}\right) \rangle_d^{\text{def}}\, ,$$ and conclude that the large $N$ limit of the degree $d$ sector of chiral Yang-Mills theory is dual to the deformed Hurwitz theory for deformation parameters equal to $t=g_{YM}^2 A$ and $u=1$. The dictionary of observables sends a holonomy insertion $U$ in the Yang-Mills theory to an operator $\sum_{\alpha\vdash d} p_{\alpha}(U_i) \hat{C}_{\alpha}$ in the Hurwitz theory.

[^1]: The papers [@Cordes:1994fc; @Horava:1993aq] have treated area terms in the Yang-Mills partition function by perturbing the conjectured dual string theory by an area operator. We modify the treatment and extend the strategy to the $\Omega$ points. Furthermore, we note that the Yang-Mills point in theory space corresponds to finite deformations by transpositions and $\Omega$ points.
