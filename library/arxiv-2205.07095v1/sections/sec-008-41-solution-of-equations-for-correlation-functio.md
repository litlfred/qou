---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble"
section_id: sec-008-41-solution-of-equations-for-correlation-functio
section_title: "Solution of equations for correlation functions."
section_number: 4.1
pages: 8-10
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.986
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical canonical ensemble is"
---
Rewrite the equation [\[limeq\]](#limeq){reference-type="eqref" reference="limeq"}, [\[ratioPF1\]](#ratioPF1){reference-type="eqref" reference="ratioPF1"} as follows:

$$\label{limeq-1}
 \widetilde{Q}(\rho_j)\rho_j(\eta)\;=\;\varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}
 j(x_1)\int_{\Gamma_0}K(x_1;\xi)\rho_j(\eta^{(\hat{x}_1)}\cup\xi)\lambda_{\sigma}(d\xi),$$ $$\label{ratioPF1-1}
 \widetilde{Q}(\rho_j)\;=\;\int_{\Gamma_0}K(x_1;\xi)\rho_j(\xi)\lambda_{\sigma}(d\xi),$$ where, following [@MP77], a continuous positive function $j: \Bbb R^d \rightarrow \Bbb R_+$ is introduced and $\rho (\eta)$ becomes functional such as $\rho(\eta)\;=\;\rho_j(\eta)|_{j=1}.$

We will look for the solution of these equations in the form: $$\label{SSCA-2}
\rho_j(\eta)\;=\;e(j;\eta)\int_{\Gamma^0}T(\eta|\gamma)e(j;\gamma)\lambda_\sigma(d\gamma),$$ where $e(j;\eta)$ is given by [\[I-lam4\]](#I-lam4){reference-type="eqref" reference="I-lam4"}.

The idea of finding a solution is to consider the left side of the equation [\[limeq-1\]](#limeq-1){reference-type="eqref" reference="limeq-1"} as the product of two generating functionals (see [\[odprod\]](#odprod){reference-type="eqref" reference="odprod"}) and compare it with the right part, which is also written in the form of a generating functional of the form [\[GFf\]](#GFf){reference-type="eqref" reference="GFf"}. So, substituting in [\[ratioPF1-1\]](#ratioPF1-1){reference-type="eqref" reference="ratioPF1-1"} the corresponding expression for $\rho_j (\xi)$ we have: $$\label{ratioPF1-1a}
 \widetilde{Q}(\rho_j)\;=\;\int_{\Gamma_0}\int_{\Gamma_0}e(j;\xi\cup\gamma)K(x_1;\xi)T(\xi|\gamma)\lambda_{\sigma}(d\gamma)\lambda_{\sigma}(d\xi).$$ Apply to the integral on the right side of the [\[ratioPF1-1a\]](#ratioPF1-1a){reference-type="eqref" reference="ratioPF1-1a"} lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} with $$\label{GH1}
   G(\xi\cup\gamma)=e(j;\xi\cup\gamma)\;\;\text{and}\;\;H(\xi;\gamma)= K(x_1;\xi)T(\xi|\gamma).$$ Then $$\label{ratioPF1-2}
 \widetilde{Q}(\rho_j)\;=\;\widetilde{F}_{\psi_1}(j)\;=\;\int_{\Gamma_0} e(j;\gamma)\psi_1(\gamma)\lambda_{\sigma}(d\gamma),$$ with $$\label{ratioPF1-2a}
 \psi_1(\gamma)\;=\;\sum_{\xi\subseteq\gamma}K(x_1;\xi)T(\xi|\gamma\setminus\xi).$$ Write down [\[SSCA-2\]](#SSCA-2){reference-type="eqref" reference="SSCA-2"} in the form of generating functional: $$\label{SSCA-3}
\rho_j(\eta)\;=\; \widetilde{F}_{\psi_2}(j)\;=\;\int_{\Gamma_0} e(j;\gamma)\psi_2(\gamma)\lambda_{\sigma}(d\gamma),$$ with $$\label{ratioPF1-2b}
 \psi_2(\gamma)\;=\;e(j;\eta) T(\eta|\gamma).$$ Left hand side [\[limeq-1\]](#limeq-1){reference-type="eqref" reference="limeq-1"} is: $$\label{limeq-1-left}
 \widetilde{Q}(\rho_j)\rho_j(\eta)\;=\; \widetilde{F}_{\psi_1}(j)\widetilde{F}_{\psi_2}(j)\;=\;\widetilde{F}_{\psi_1*\psi_2}(j)\;
 =\;\int_{\Gamma_0} e(j;\gamma)(\psi_1*\psi_2)(\gamma)\lambda_{\sigma}(d\gamma),$$ where $$\begin{aligned}
\label{help}
(\psi_1*\psi_2)(\gamma)&=\sum_{\xi\subseteq\gamma}\psi_1(\xi)\psi_2(\gamma\setminus\xi)=\sum_{\xi\subseteq\gamma}\psi_2(\gamma\setminus\xi)\psi_1(\xi)=\\
&=e(j;\eta)\sum_{\xi\subseteq\gamma} T(\eta|\gamma\setminus\xi)\sum_{\zeta\subseteq\xi}K(x_1;\zeta)T(\zeta|\xi\setminus\zeta)\notag
\end{aligned}$$

Right hand side [\[limeq-1\]](#limeq-1){reference-type="eqref" reference="limeq-1"} after substitution of $\rho_j(\eta^{(\hat{x}_1)}\cup\xi)$ in the form [\[SSCA-2\]](#SSCA-2){reference-type="eqref" reference="SSCA-2"} will look as: $$\label{limeq-1-right0}
\varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}
 e(j;\eta)\int_{\Gamma_0}\int_{\Gamma_0}e(j;\xi\cup\gamma)K(x_1;\xi)T(\eta^{(\hat{x}_1)}\cup\xi|\gamma)\lambda_{\sigma}(d\gamma)
\lambda_{\sigma}(d\xi).$$ Let us use lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} again with $$\label{GH1}
   G(\xi\cup\gamma)=e(j;\xi\cup\gamma)\;\;\text{and}\;\;H(\xi;\gamma)= K(x_1;\xi)T(\eta^{(\hat{x}_1)}\cup\xi|\gamma).$$ Then right hand side of [\[limeq-1\]](#limeq-1){reference-type="eqref" reference="limeq-1"} will be as $$\label{limeq-1-right}
\varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}
 e(j;\eta)\int_{\Gamma_0} e(j;\gamma)\sum_{\xi\subseteq\gamma} K(x_1;\xi)T(\eta^{(\hat{x}_1)}\cup\xi|\gamma\setminus\xi)\lambda_{\sigma}(d\gamma).$$ We equate the functions near $e(j;\gamma)$ under the integrals of the expressions [\[limeq-1-left\]](#limeq-1-left){reference-type="eqref" reference="limeq-1-left"} and [\[limeq-1-right\]](#limeq-1-right){reference-type="eqref" reference="limeq-1-right"} and, reducing the multiplier $e(j; \eta)$ we get the relation: $$\begin{aligned}
\label{help}
 &\sum_{\xi\subseteq\gamma} T(\eta|\gamma\setminus\xi)\sum_{\zeta\subseteq\xi}K(x_1;\zeta)T(\zeta|\xi\setminus\zeta)\;=\\
 &=\;\varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}\sum_{\xi\subseteq\gamma} K(x_1;\xi)T(\eta^{(\hat{x}_1)}\cup\xi|\gamma\setminus\xi).\notag
\end{aligned}$$ Select the term with $\xi = \emptyset$ in the left side of this relation and take into account that $T(\emptyset | \emptyset) = 1$ and $T (\emptyset | \gamma) = 0$, if $\gamma \neq \emptyset)$, we obtain the following nonlinear recurrent relation: $$\begin{aligned}
\label{final}
T(\eta|\gamma)&= \varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}\sum_{\xi\subseteq\gamma} K(x_1;\xi)T(\eta^{(\hat{x}_1)}\cup\xi|\gamma\setminus\xi)-\notag\\
&-\sum_{\emptyset\neq\xi\subseteq\gamma} T(\eta|\gamma\setminus\xi)\sum_{\emptyset\neq\zeta\subseteq\xi}K(x_1;\zeta)T(\zeta|\xi\setminus\zeta).
\end{aligned}$$

**Initial conditions:** $$\label{incon0}
    T(\emptyset|\emptyset)\;=\;1,\;\;\;T(\emptyset|\gamma)\;=\;0, \text{if}\;\;\gamma\neq\emptyset,$$ $$\label{incon1}
    T(\{\eta|\gamma)\;=\;0,\text{if}\;\;\eta\cap\gamma\neq\;\emptyset.$$
