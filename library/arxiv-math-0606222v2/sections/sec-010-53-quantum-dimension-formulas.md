---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-010-53-quantum-dimension-formulas
section_title: "Quantum dimension formulas"
section_number: 5.3
pages: 20-21
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.964
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#QDF label="QDF"}

The quantum dimensions of the irreducible spherical $\mathcal{U}_q$-representations $V_\lambda^q$ ($\lambda\in\Lambda_n$) have the following explicit closed expressions.

::: prop
[]{#quantumcomplexformula label="quantumcomplexformula"} For $\lambda\in\Lambda_n$ we have $$\label{qcf}
\begin{split}
\hbox{Dim}_{q}\bigl(V_{\lambda}^{q}\bigr)&=q^{2(2n-d-1)|\lambda|-4(\rho,\lambda)}
\prod_{i=1}^n\frac{\bigl(q^{2(1+\lambda_i+\rho_i)};q^2\bigr)_{d-2n}^2}
{\bigl(q^{2(1+\rho_i)};q^2\bigr)_{d-2n}^2}
\frac{(1-q^{2(d-2n+1+2(\lambda_i+\rho_i))})}
{(1-q^{2(d-2n+1+2\rho_i)})}\\
&\qquad\times\prod_{1\leq j<k\leq n}
\frac{(1-q^{2(d-2n+1+\lambda_j+\lambda_k+\rho_j+\rho_k)})^2
(1-q^{2(\lambda_j-\lambda_k+\rho_j-\rho_k)})^2}
{(1-q^{2(d-2n+1+\rho_j+\rho_k)})^2(1-q^{2(\rho_j-\rho_k)})^2}.
\end{split}$$
:::

In Section [\[quantum\]](#quantum){reference-type="ref" reference="quantum"} we derive Proposition [\[quantumcomplexformula\]](#quantumcomplexformula){reference-type="ref" reference="quantumcomplexformula"} from a generalization of the quantum dimension formula [\[dimforquantum\]](#dimforquantum){reference-type="eqref" reference="dimforquantum"} to the setup of the one-parameter family of quantum complex Grassmannians from [@NDS] and [@DS]. By a suitable degeneration procedure we subsequently deduce the quantum dimension formulas $$\label{qcfcons}
\hbox{Dim}_q\bigl(V_\lambda^q\bigr)=
D_{q^2}\bigl(\lambda;q^{2(d-2n+1)},q^2;q^2),\qquad
\lambda\in\Lambda_n$$ in terms of evaluations and quadratic norms of multivariable little $q$-Jacobi polynomials. More directly, [\[qcfcons\]](#qcfcons){reference-type="eqref" reference="qcfcons"} is a direct consequence of the quantum dimension formula [\[dimforquantum\]](#dimforquantum){reference-type="eqref" reference="dimforquantum"} if one uses the fact that the quantum zonal spherical functions $\varphi_\lambda^q$ ($\lambda\in\Lambda_n$) identify with multivariable little $q$-Jacobi polynomials (see [@DS] and Remark [\[standardrema\]](#standardrema){reference-type="ref" reference="standardrema"}).

::: rema
[]{#classicalrema label="classicalrema"} Taking the limit $q\rightarrow 1$ in [\[qcf\]](#qcf){reference-type="eqref" reference="qcf"}, we obtain the explicit dimension formulas for the irreducible $\mathcal{M}$-spherical $\mathcal{K}$-representations $V_\lambda^{\mathbb{C}}$ ($\lambda\in\Lambda_n$) as stated in Proposition [\[classicalcomplexformula\]](#classicalcomplexformula){reference-type="ref" reference="classicalcomplexformula"}.
:::

We end this subsection by discussing the representation theoretic viewpoint on the quantum dimension formula [\[qcf\]](#qcf){reference-type="eqref" reference="qcf"} for $\lambda=\omega_r$, in which case it yields the explicit expression $$\label{dimformulanewrepr}
\hbox{Dim}_q\bigl(V_{\omega_r}^q\bigr)= q^{2r(d-r)}\left({d\atop
r}\right)_{q^{-2}}^2- q^{2(r-1)(d-r+1)}\left({d\atop
r-1}\right)_{q^{-2}}^2$$ for $r=1,\ldots,n$ by a straightforward computation. The following representation theoretic derivation of [\[dimformulanewrepr\]](#dimformulanewrepr){reference-type="eqref" reference="dimformulanewrepr"} bears strong resemblance to the representation theoretic derivation of the dimension formula [\[padicfundamental\]](#padicfundamental){reference-type="eqref" reference="padicfundamental"} in the classical non-Archimedean setup.

Let $\{\epsilon_j\}_{j=1}^d$ be the standard orthonormal basis of $\mathbb{R}^d$. Let $V=L_{\epsilon_1}^q$ be the $d$-dimensional vector-representation of $\mathcal{U}_q$. Its weight spaces are one-dimensional, with weights $\epsilon_j$ ($j=1,\ldots,d$). The irreducible representation $L_{\epsilon_1+\cdots +\epsilon_r}^q$ ($1\leq r\leq n$) can be realized as the $r$th graded part $\Lambda_q^r(V)$ of the $q$-exterior algebra $\Lambda_q(V)$ of $V$ (see [@NYM]). The weight spaces of $\Lambda_q^r(V)$ are again one-dimensional, with weights given by $\sum_{j\in J}\epsilon_j$ for subsets $J\subseteq \{1,\ldots,d\}$ of cardinality $r$. Hence $$\hbox{Dim}_q\bigl(\Lambda_q^r(V)\bigr)=
\hbox{Tr}_{\Lambda_q^r(V)}(K^{2\delta}\cdot)=
\sum_{\stackrel{J\subseteq\{1,\ldots,d\}}{\#J=r}}\prod_{j\in
J}q^{2(d-j)}=
q^{(r-1)r}\frac{\bigl(q^{2(d-r+1)};q^2\bigr)_r}{\bigl(q^2;q^2\bigr)_r},$$ where the third equality follows by an easy induction argument. The dual of $\Lambda_q^r(V)$ is irreducible of highest weight $-\epsilon_{d-r+1}\cdots -\epsilon_d$. In fact, by [@NYM] we have $$\Lambda_q^r(V)^*\simeq \mathbb{C}\hbox{det}_q^{-1}\otimes
\Lambda_{q}^{d-r}(V),$$ with $\mathbb{C}\hbox{det}_q^{-1}\simeq L_{-\epsilon_1\cdots
-\epsilon_d}^q$ the one-dimensional representation realized by the inverse of the quantum determinant $\det_q\in \mathbb{C}_q(\mathcal{K})$, hence $$\hbox{Dim}_q\bigl(\Lambda_q^r(V)^*\bigr)=
q^{(1+r-2d)r}\frac{\bigl(q^{2(r+1)};q^2\bigr)_{d-r}}{\bigl(q^2;q^2\bigr)_{d-r}}.$$ We conclude that $$\hbox{Dim}_q\bigl(U_r\bigr)=
q^{2r(d-r)}\left({d\atop r}\right)_{q^{-2}}^2,$$ where $U_r$ is the $\mathcal{U}_q$-module $$U_r=\Lambda_q^r(V)\otimes \Lambda_q^r(V)^*.$$ By [@DS (6.14)] we have $$U_r\simeq U_{r-1}\oplus V_{\omega_r}^q, \qquad r=1,\ldots,n$$ as $\mathcal{U}_q$-modules (with $U_0$ the trivial representation), which now immediately implies [\[dimformulanewrepr\]](#dimformulanewrepr){reference-type="eqref" reference="dimformulanewrepr"}.
