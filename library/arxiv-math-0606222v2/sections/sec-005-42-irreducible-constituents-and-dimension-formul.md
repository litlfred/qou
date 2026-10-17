---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-005-42-irreducible-constituents-and-dimension-formul
section_title: "Irreducible constituents and dimension formulas: the Archimedean case"
section_number: 4.2
pages: 11-14
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.979
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#cG label="cG"}

The harmonic analysis corresponding to the complex and real Grassmannian is classical by now. It relates to special cases of harmonic analysis on compact symmetric spaces. To emphasize the similarities with the non-Archimedean case and the quantum case, we now shortly describe the relevant results for the complex Grassmannian $\mathcal{G}(n,d;\mathbb{C})$, following closely the presentation in [@DS Section 2]. For the real case, we refer to [@JC] and especially to [@Su] (the presentation in [@Su] is very close to the (quantum) complex case as discussed in this paper).

To avoid confusion with standard notations for the complexification of a compact Lie group, we write $$\label{convention}
(\mathcal{K},\mathcal{M})=(\hbox{U}(d), \hbox{U}(d-n)\times\hbox{U}(n))$$ for the Gelfand pair $(\mathcal{K}_{\mathbb{F}}, \mathcal{M}_{\mathbb{F}})$ when $\mathbb{F}=\mathbb{C}$. The irreducible $\mathcal{K}$-representations are parametrized by the cone $$\label{Pplus}
P_d^+=\{\mu\in\mathbb{Z}^{d} \, | \,
\mu_1\geq\mu_2\geq\cdots\geq\mu_{d}\}\subset \mathbb{Z}^d,$$ by associating to $\mu\in P_d^+$ the $\mathcal{K}$-representation $L_\mu^\mathbb{C}$ of highest weight $\mu\in P_d^+$. The Weyl character formula states that the restriction of the character of $L_\mu^\mathbb{C}$ ($\mu\in
P_d^+$) to the compact $d$-torus of diagonal matrices $\hbox{diag}(u_1,\ldots,u_d)$ in $\hbox{U}(d)$ is the Schur function $$s_\mu(u_1,\ldots,u_{d})=\Delta(u)^{-1}\sum_{w\in
S_{d}}(-1)^{l(w)}u^{w(\mu+\rho_d)}\quad (\mu\in P_d^+),$$ where $\Delta(u)=\prod_{1\leq i<j\leq d}(u_i-u_j)$ is the Vandermonde determinant, $l(w)$ is the length of $w\in S_n$, and $\rho_d=(d-1,d-2,\ldots,0)\in P_d^+$ is the staircase partition. The dimension of $L_\mu^\mathbb{C}$ being the evaluation of its character at the unit element $e\in \mathcal{K}$ thus yields $$\label{Schurdim}
\hbox{Dim}_{\mathbb{C}}(L_\mu^q)=s_\mu(1),\qquad \mu\in P_d^+.$$ The resulting, famous, Weyl dimension formula is $$\label{Weyl}
\hbox{Dim}_{\mathbb{C}}(L_\mu^{\mathbb{C}})=\prod_{1\leq i<j\leq d}\left(
\frac{\mu_i-\mu_j+\delta_i-\delta_j}{\delta_i-\delta_j}\right),
\qquad \mu\in P_d^+,$$ where $$\label{delta}
\delta=\frac{1}{2}\bigl(d-1,d-3,\ldots,3-d,1-d\bigr)$$ is the half sum of positive roots in the standard realization of the $A_{d-1}$-type root system in $\mathbb{R}^d$. We note that other explicit dimension formulas are known, mostly with a combinatorial flavour. For instance, for $\mu\in P_d^+$ with $\mu_d\geq 0$, $\hbox{Dim}_{\mathbb{C}}(L_\mu^\mathbb{C})$ is the number of standard Young tableaux of shape $\mu$. Furthermore, $\hbox{Dim}_{\mathbb{C}}(L_\mu^\mathbb{C})$ can be explicitly expressed in terms of products of hook-lengths of the Young diagram of shape $\mu$ (see [@M]).

We state now a different type of dimension formula for the subclass of spherical irreducible representations associated to the complex Grassmannian $\mathcal{G}(n,d;\mathbb{C})\simeq \mathcal{K}/\mathcal{M}$. This dimension formula is based on the expression [\[dimforclassical\]](#dimforclassical){reference-type="eqref" reference="dimforclassical"} of the dimension in terms of the corresponding zonal spherical functions. The spherical unitary dual $(\mathcal{K}_{\mathbb{F}}/\mathcal{M}_{\mathbb{F}})\hat{~}$ naturally identifies with the set $\Lambda_n$ of partitions of length at most $n$ via the embedding $$\label{natural}
\lambda^\natural=
(\lambda_1,\lambda_2,\ldots,\lambda_n,\underset{d-2n}{\underbrace{0,\ldots,0}},-\lambda_n,\ldots,-\lambda_2,-\lambda_1)$$ of $\Lambda_n$ in $P_d^+$. Consequently the irreducibles $$V_\lambda^{\mathbb{C}}:=L_{\lambda^\natural}^{\mathbb{C}},\qquad
(\lambda\in\Lambda_n)$$ form a complete set of representatives of the irreducible $\mathcal{M}_{\mathbb{F}}$-spherical $\mathcal{K}_{\mathbb{F}}$-representations, and the Grassmann representation $\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{C})\bigr)$ has a multiplicity-free decomposition $$\mathbb{C}\bigl(\mathcal{G}(n,d;\mathbb{C})\bigr)\simeq\bigoplus_{\lambda\in\Lambda_n}V_{\lambda}^{\mathbb{C}}$$ as $\mathcal{K}_{\mathbb{F}}$-module. We write $\varphi_\lambda^{\mathbb{C}}$ for the zonal spherical function corresponding to the irreducible representation $V_{\lambda}^{\mathbb{C}}$ ($\lambda\in\Lambda_n$).

::: prop
[]{#classicalcomplexformula label="classicalcomplexformula"} For $\lambda\in\Lambda_n$ we have $$\begin{split}
\hbox{Dim}_{\mathbb{C}}\bigl(V_{\lambda}^{\mathbb{C}}\bigr)&=
\prod_{i=1}^n
\left(\frac{d-2n+1+2(\lambda_i+\rho_i)}{d-2n+1+2\rho_i}\right)\prod_{j=1}^{d-2n}\left(\frac{j+\lambda_i+\rho_i}{j+\rho_i}\right)^2\\
&\times\prod_{1\leq j<k\leq n}\left(\frac{d-2n+1+\lambda_j+\lambda_k+\rho_j+\rho_k}{d-2n+1+\rho_j+\rho_k}\right)^2
\left(\frac{\lambda_j-\lambda_k+\rho_j-\rho_k}{\rho_j-\rho_k}\right)^2,
\end{split}$$ where $\rho=(n-1,n-2,\ldots,1,0)\in\Lambda_n$ is the staircase partition.
:::

The natural proof of the proposition uses the identification of the radial parts of the zonal spherical functions $\varphi_\lambda^{\mathbb{C}}$ ($\lambda\in\Lambda_n$) as $\hbox{BC}_n$-type Heckman-Opdam polynomials with appropriate multiplicity parameters (see e.g. [@JC] and [@DS Section 2]). The dimension formula [\[dimforclassical\]](#dimforclassical){reference-type="eqref" reference="dimforclassical"} then yields an expression in terms of evaluations and quadratic norms of Heckman-Opdam polynomials, which both have been explicitly evaluated.

Proposition [\[classicalcomplexformula\]](#classicalcomplexformula){reference-type="ref" reference="classicalcomplexformula"} follows also as a direct consequence of the formula $$\label{DclasQ}
\hbox{Dim}_{\mathbb{C}}\bigl(V_\lambda^{\mathbb{C}}\bigr)=
D_{q^2}\bigl(\lambda;q^{2(d-2n+1)},q^2;q^2\bigr)|_{q=1},\qquad
(\lambda\in\Lambda_n),$$ expressing the dimensions in terms of the classical ($q=1$) degeneration of the generalized dimension formula $D_q(\lambda)$ (see [\[Dgeneralized\]](#Dgeneralized){reference-type="eqref" reference="Dgeneralized"}). Formula [\[DclasQ\]](#DclasQ){reference-type="eqref" reference="DclasQ"} is a direct consequence of the identification of multivariable little $q$-Jacobi polynomials with quantum zonal spherical functions on the quantum complex Grassmannian, see Subsection [\[QDF\]](#QDF){reference-type="ref" reference="QDF"} for details. We note also that the classical ($q=1$) degeneration of the multivariable little $q$-Jacobi polynomials have been studied in detail in [@SK], also in the context of harmonic analysis on (quantum) complex Grassmannians (see [@DS]).

::: rema
Proposition [\[classicalcomplexformula\]](#classicalcomplexformula){reference-type="ref" reference="classicalcomplexformula"} can easily be reconfirmed by specializing the Weyl dimension formula [\[Weyl\]](#Weyl){reference-type="eqref" reference="Weyl"} to $\mu=\lambda^\natural$ ($\lambda\in\Lambda_n$).
:::

For the real Grassmannian, $(\mathcal{K}_{\mathbb{R}}/\mathcal{M}_{\mathbb{R}})\hat{~}$ also naturally identifies with $\Lambda_n$, see [@JC], [@OU1] and [@Su]. The harmonic analytic results from [@JC] lead to similar explicit dimension formulas for the associated irreducible $\mathcal{M}_{\mathbb{R}}$-spherical $\mathcal{K}_{\mathbb{R}}$-representations $V_\lambda^{\mathbb{R}}$ ($\lambda\in\Lambda_n$). In particular the dimensions can also be expressed as classical ($q=1$) degenerations of generalized dimensions $$\label{realdim}
\textup{Dim}_{\mathbb{C}}\bigl(V_\lambda^{\mathbb{R}}\bigr)=
D_{q^2}\bigl(\lambda;q^{d-2n+1},q;q\bigr)|_{q=1},\qquad
(\lambda\in\Lambda_n),$$ which follow as in the complex case from the results in [@JC] and [@SK] (see also [@OU1 §2.1.1]).
