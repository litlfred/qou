---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-016-45-the-refined-quantum-modularity-conjecture
section_title: "The refined quantum modularity conjecture"
section_number: 4.5
pages: 28-30
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.4.5 label="sub.4.5"}

The refinement of the quantum modularity conjecture that we have obtained so far, equation [\[RQMC\]](#RQMC){reference-type="eqref" reference="RQMC"}, has two noteworthy aspects. One is that, although we find new collections of "Habiro-like" functions $J^{(\sigma,\sigma')}$ for the asymptotic expansion as $X\to\infty$ of the functions $J^{(\sigma_0,\sigma)}(\gamma X)$ for different $\sigma\in\mathcal P_K$ (here we continue the practice of omitting the knot from all notations when it is not varying), these arise as coefficients of the *same* completed formal power series $\widehat\Phi^{(\sigma')}(h)$ as we found for the initial Galois-extended Kashaev invariant $J^{(\sigma_0)}$. The other is that among the new coefficients $J^{(K,\sigma,\sigma')}$, the subset corresponding to $\sigma'=\sigma_1$ coincides precisely with the set of functions $J^{(\sigma)}$ whose asymptotic behavior near fixed rational points is being studied. It is therefore natural to ask whether the functions $J^{(K,\sigma,\sigma')}$ for $\sigma'$ different from $\sigma_1$ also have a quantum modularity property, and if so, what new power series are involved. In this final subsection, we will study both questions and give our (nearly) final version of the QMC.

As usual, we look first at the $4_1$ knot. Here, as well as the three periodic functions $J^{(\sigma_0,\sigma_1)}(x)\allowbreak:=J(x)$ and $J^{(\sigma_0,\sigma_1)}(x) := J^{(\sigma_1)}$ and $J^{(\sigma_0,\sigma_2)}:=J^{(\sigma_2)}$ we had studied earlier, we found two new periodic functions $J^{(\sigma_1,\sigma_2)}(x)$ and $J^{(\sigma_2,\sigma_2)}(x)$, given explicitly by formulas [\[Q1for41\]](#Q1for41){reference-type="eqref" reference="Q1for41"} and related to the others by [\[FirstBilin\]](#FirstBilin){reference-type="eqref" reference="FirstBilin"}. If we look numerically at the asymptotics of both functions with $x=-1/X$ for $X\to\infty$ with bounded denominator, we find $$\begin{gathered}
X^{-3/2}J^{(\sigma_0,\sigma_2)}\left(-\frac1X\right)  \sim  J^{(\sigma_0,\sigma_1)}(X)
\widehat\Psi^{(1)}\left(\frac{2\pi {\rm i}}{X}\right) , \\
{\rm e}^{-v(\sigma_1)\lambda_S(X)}  J^{(\sigma_1,\sigma_2)}\left(-\frac1X\right)  \sim
J^{(\sigma_1,\sigma_1)}(X) \widehat\Psi^{(1)}\left(\frac{2\pi {\rm i}}{X}\right)
\end{gathered}$$ with the *same* completed power series $$\widehat\Psi^{(1)}(h) = {\rm e}^{\mathbf V(4_1)/h} \Psi^{(1)}(h),\qquad
\Psi^{(1)}(h)= \frac{{\rm i} \sqrt[4]3}{2}
\left(1  - \frac{37}{72\sqrt{-3}} h  - \frac{1511}{2(72\sqrt{-3})^2} h^2+\cdots\right)$$ in both cases. Based on the analogy with the asymptotics of the functions $J^{(\sigma_1,\sigma_1)}(-1/X)$ as given in [\[41RQMC\]](#41RQMC){reference-type="eqref" reference="41RQMC"}, we would now expect the more accurate approximations $$\begin{aligned}
 & X^{-3/2}J^{(\sigma_0,\sigma_2)}\left(-\frac{1}{X}\right) \approx \widehat\Psi^{(0)}\left(\frac{2\pi {\rm i}}{X}\right) +
 J^{(\sigma_0,\sigma_1)}(X) \widehat\Psi^{(1)}\left(\frac{2\pi {\rm i}}{X}\right)
 + J^{(\sigma_0,\sigma_2)}(X) \widehat\Psi^{(2)}\left(\frac{2\pi {\rm i}}{X}\right) ,
 \nonumber\\
 & {\rm e}^{-v(\sigma_1) \lambda_S(X)} J^{(\sigma_1,\sigma_2)}\left(-\frac{1}{X}\right) \approx
 J^{(\sigma_1,\sigma_1)}(X) \widehat\Psi^{(1)}\left(\frac{2\pi {\rm i}}{X}\right) +J^{(\sigma_1,\sigma_2)}(X) \widehat\Psi^{(2)}\left(\frac{2\pi {\rm i}}{X}\right) ,\nonumber
 \\
 & {\rm e}^{-v(\sigma_2) \lambda_S(X)} J^{(\sigma_2,\sigma_2)}\left(-\frac{1}{X}\right) \approx
 J^{(\sigma_2,\sigma_1)}(X) \widehat\Psi^{(1)}\left(\frac{2\pi {\rm i}}{X}\right) +J^{(\sigma_2,\sigma_2)}(X) \widehat\Psi^{(2)}\left(\frac{2\pi {\rm i}}{X}\right) ,
 \label{FirstMatrix}
\end{aligned}$$ where $\widehat\Psi^{(2)}(h)$ is the completed series ${\rm e}^{-\mathbf V(4_1)/h} \Psi^{(2)}(h)$ with $\Psi^{(2)}(h)=-{\rm i}\Psi^{(1)}(-h)$ and where $\widehat\Psi^{(0)}(h)$ is the completed series $(h/2\pi {\rm i})^{3/2} \Phi^{(0)}(h)$ (cf. [\[DefPhi0h\]](#DefPhi0h){reference-type="eqref" reference="DefPhi0h"}) with $$\Phi^{(0)}(h) = -h + \frac{11}6 h^3  - \frac{1261}{120} h^5
+ \frac{611771}{5040} h^7  - \cdots$$ the power series in $h \mathbb Q\big[\big[h^2\big]\big]$ obtained by replacing $q=\mathbf{e}(X)$ by $q={\rm e}^{-h}$ in formula [\[Q0for41\]](#Q0for41){reference-type="eqref" reference="Q0for41"}, as well of course as similar formulas for for other matrices $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)$ in $\mathrm{SL}_2(\mathbb Z)$ with the completed power series replaced by suitable new completed power series $$\widehat\Psi_{a/c}^{(j)}(h)={\rm e}^{\mathbf V(\sigma_j)/ch}(h/2\pi {\rm i})^{\kappa(\sigma_j)}\Psi_{a/c}^{(j)}(h)$$ but with the same periodic coefficients.

To test [\[FirstMatrix\]](#FirstMatrix){reference-type="eqref" reference="FirstMatrix"} or its generalizations to other $\gamma\in\mathrm{SL}_2(\mathbb Z)$ directly we would need to find many terms of the power series and carry out the smoothed optimal truncation as described earlier in this section, because the different exponential growths of their completions would mean that the contributions with $j\ne1$ would not be numerically visible at the level of mere formal power series. This could be done, but an easier test of the prediction is to take linear combinations of the first two or last two lines in [\[FirstMatrix\]](#FirstMatrix){reference-type="eqref" reference="FirstMatrix"} to eliminate the dominant $\widehat\Psi^{(1)}$-term. This (together with [\[FirstBilin\]](#FirstBilin){reference-type="eqref" reference="FirstBilin"}) produces the two new asymptotic predictions $$\begin{aligned}
 &X^{-3/2} J^{(\sigma_1,\sigma_1)}(X) J^{(\sigma_0,\sigma_2)}\left(-\frac{1}{X}\right)  - 
 {\rm e}^{-v(\sigma_1) \lambda_S(X)}J^{(\sigma_0,\sigma_1)}(X)
 J^{(\sigma_1,\sigma_2)}\left(-\frac{1}{X}\right)\\
 &\qquad\approx J^{(\sigma_1,\sigma_1)}(X) \widehat\Psi^{(0)}\left(\frac{2\pi {\rm i}}{X}\right) , \\
 &{\rm e}^{-v(\sigma_1) \lambda_S(X)} J^{(\sigma_2,\sigma_1)}(X) J^{(\sigma_1,\sigma_2)}\left(-\frac{1}{X}\right) - 
 {\rm e}^{-v(\sigma_2) \lambda_S(X)} J^{(\sigma_1,\sigma_1)}(X) J^{(\sigma_2,\sigma_2)}\left(-\frac{1}{X}\right)\\
 &\qquad \approx \widehat\Psi^{(2)}\left(\frac{2\pi {\rm i}}{X}\right) ,
\end{aligned}$$ both of which can be tested directly since they do not involve functions of different orders of growth on the right, and both of which we confirmed numerically to very high precision. We omit the details, having given more than enough descriptions of analogous numerical calculations in this section already.

Generalizing the above discussion to other knots, we find as our nearly-final version of the QMC the asymptotic statement $$\begin{gathered}
(cX+d)^{-\kappa(\sigma)} {\rm e}^{-v(\sigma)\lambda_\gamma(X)}
J^{(K,\sigma,\sigma')}\left(\frac{aX+b}{cX+d}\right)\\
\qquad \overset?\approx
\sum_{\sigma'' \in \mathcal P_K}J^{(K,\sigma,\sigma'')}(X)
\widehat\Phi^{(K,\sigma'',\sigma')}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)
\end{gathered}$$ for $X\in\mathbb Q$ tending to infinity with bounded denominator and for every $\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$ with ${c>0}$, where the functions are the "Habiro-like" functions that we found in Section [\[sub.4.4\]](#sub.4.4){reference-type="ref" reference="sub.4.4"}, given as the constant terms of certain power series , and where are the completions defined by $$\widehat\Phi^{(K,\sigma,\sigma')}_\alpha(h) = (ch/2\pi {\rm i})^{\kappa(\sigma)} {\rm e}^{\mathbf V(\sigma)/c^2h}
\Phi^{(K,\sigma,\sigma')}_\alpha(h), \qquad \sigma,\sigma' \in \mathcal P_K .$$ To get the final version, we upgrade this statement about constant terms to a statement about the full (completed) power series in the same way as we did in [\[sub.QMCwithh\]](#sub.QMCwithh){reference-type="ref" reference="sub.QMCwithh"}, obtaining:

**Refined quantum modularity conjecture (RQMC):** *For fixed $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$ with ${c>0}$, we have $$\widehat\Phi^{(K,\sigma,\sigma')}_{\gamma X}(h^*)  \overset?\approx
(cx+d)^{\kappa(\sigma)} \sum_{\sigma'' \in \mathcal P_K}\widehat\Phi^{(K,\sigma,\sigma'')}_X(h)
\widehat\Phi^{(K,\sigma'',\sigma')}_{a/c}\left(\frac{2\pi {\rm i}}{c(cx+d)}\right)$$ to all orders in $1/X$ as $X\in\mathbb Q$ tending to $+\infty$ with bounded denominator, where* $$x=X-\hbar$ and~${h^*=h/(cx+d)(cX+d)}.$$

We end this section by observing that the two versions of the refined quantum modularity conjecture that we just stated can both be written more succinctly in matrix form as $$\label{dQPhi}
\mathbf{J}^{(K)}(\gamma X)
 \approx \widetilde{\mathbf{j}}_\gamma(X) \mathbf{J}^{(K)}(X) \mathbf{\widehat\Phi}^{(K)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cX+d)}\right)$$ and $$\label{MatQMC}
\mathbf{\widehat\Phi}^{(K)}_{\gamma X}(h^*)  \overset?\approx  \mathbf{j}_\gamma(x)
\mathbf{\widehat\Phi}^{(K)}_X(h) \mathbf{\widehat\Phi}^{(K)}_{a/c}\left(\frac{2\pi {\rm i}}{c(cx+d)}\right)$$ as $X\to\infty$ with bounded denominator for a fixed knot $K$ and element $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$, where  and denote the matrices of Habiro-like functions and completed formal power series, with columns and rows indexed by $\mathcal P_K$, with entries and , respectively, and where $\mathbf{j}$ and $\widetilde{\mathbf{j}}$ are the matrix-valued automorphy factors defined by $$\label{autofactor}
\mathbf{j}_\gamma(x) = \operatorname{\mathbf{diag}}\bigl(|cx+d|^{\kappa(\sigma)}\bigr) ,\qquad
\widetilde{\mathbf{j}}_\gamma(x) = \operatorname{\mathbf{diag}}\bigl({\rm e}^{v(\sigma) \lambda_\gamma(x)} |cx+d|^{\kappa(\sigma)}\bigr) ,$$ the second of which is the "tweaked" version of the first. Note that both of these factors are unchanged if we replace $\gamma$ by $-\gamma$, and hence are actually automorphy factors on $\mathrm{PSL}_2(\mathbb Z)$. Also, from the fact that $\lambda$ is an additive cocycle (see Lemma [\[lem.lambda\]](#lem.lambda){reference-type="ref" reference="lem.lambda"}) we deduce that both $\mathbf{j}$ and $\widetilde{\mathbf{j}}$ are matrix-valued cocycles on $\mathrm{PSL}_2(\mathbb Z)$, meaning that they satisfy $$\label{jcoc}
 \mathbf{j}_{\gamma\gamma'}(x) = \mathbf{j}_{\gamma'}(x)  \mathbf{j}_\gamma(\gamma' x) , \qquad
\widetilde{\mathbf{j}}_{\gamma\gamma'}(x) = \widetilde{\mathbf{j}}_{\gamma'}(x)  \widetilde{\mathbf{j}}_\gamma(\gamma' x) ,$$ for all $\gamma, \gamma'\in \mathrm{PSL}_2(\mathbb Z)$. This will be important in the next section.
