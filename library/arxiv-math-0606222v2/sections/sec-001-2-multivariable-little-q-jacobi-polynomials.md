---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-001-2-multivariable-little-q-jacobi-polynomials
section_title: "Multivariable little q-Jacobi polynomials"
section_number: 2
pages: 4-6
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.989
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#qJsection label="qJsection"}

Important in our approach is the fact that (quantum) dimensions of irreducible spherical representations associated to quantum, real/complex and $p$-adic Grassmannians are degenerations of a generalized dimension formula involving multivariable little $q$-Jacobi polynomials, which we now introduce. We work over the field $\mathbb{E}$ (see [\[Fz\]](#Fz){reference-type="eqref" reference="Fz"}), although in the present situation $c$ and $d$ are dummy parameters and could just as well be omitted (in contrast to the Macdonald-Koornwinder and multivariable big $q$-Jacobi case as treated in Section [\[evaluation\]](#evaluation){reference-type="ref" reference="evaluation"}).

The symmetric group $S_n$ in $n$ letters acts on $\mathbb{Z}_+^n$ by permuting the coordinates. The corresponding fundamental domain is the cone $\Lambda_n$ of partitions with at most $n$ parts. The symmetric group $S_n$ acts on $\mathbb{E}[z]=\mathbb{E}[z_1,\ldots,z_n]$ by permuting the independent variables $z_1,\ldots,z_n$. We denote $\mathbb{E}[z]^S$ for the subalgebra of $S_n$-invariant polynomials in $\mathbb{E}[z]$. An $\mathbb{E}$-basis of $\mathbb{E}[z]^S$ is formed by the symmetric monomials $\widetilde{m}_\lambda(z)=\sum_{\mu\in S_n\lambda}z^\mu$ ($\lambda\in\Lambda_n$). The monic multivariable little $q$-Jacobi polynomial $P_\lambda^L(z)=P_\lambda^L(z;a,b;q,t)\in \mathbb{E}[z]^S$ of degree $\lambda\in\Lambda_n$ from [@S0] is of the form $$\label{expansionL}
P_\lambda^L(z)=\widetilde{m}_\lambda(z)+\sum_{\mu\in\Lambda_n: \mu<\lambda}c_{\lambda,\mu}^L\widetilde{m}_{\mu}(z)$$ for certain coefficients $c_{\lambda,\mu}^L=c_{\lambda,\mu}^L(a,b;q,t)\in \mathbb{E}$. The multivariable little $q$-Jacobi polynomials can be characterized as solution of a second-order difference equation, or in terms of orthogonality relations defined with respect to an explicit discrete probability orthogonality measure. The characterization in terms of the difference equation is as follows. For $j=1,\ldots,n$ we write $T_j$ for the multiplicative $q$-shift in $z_j$, $$(T_jf)(z)=f(z_1,\ldots,z_{j-1},qz_j, z_{j+1},\ldots,z_n),\qquad f\in \mathbb{E}[z^{\pm 1}].$$ The characterizing difference equation then reads $D_LP_\lambda^L=E_\lambda^{qJ}P_\lambda^L$ where $$\begin{split}
D_L&=\sum_{j=1}^n\bigl(\phi_{L,j}^+(z)(T_j-\hbox{Id})+\phi_{L,j}^-(z)(T_j^{-1}-\hbox{Id})\bigr),\\
\phi_{L,j}^+(z)&=qt^{n-1}a\bigl(b-\frac{1}{qz_j}\bigr)\prod_{l\not=j}\frac{z_l-tz_j}{z_l-z_j},
\qquad
\phi_{L,j}^-(z)=\bigl(1-\frac{1}{z_j}\bigr)\prod_{l\not=j}\frac{z_j-tz_l}{z_j-z_l}
\end{split}$$ and with eigenvalue $$E_\lambda^{qJ}=\sum_{j=1}^n\bigl(qabt^{2n-j-1}(q^{\lambda_j}-1)+t^{j-1}(q^{-\lambda_j}-1)\bigr).$$ An algebraic formulation of the orthogonality relations of the multivariable little $q$-Jacobi polynomials is as follows. Define an $\mathbb{E}$-linear functional $$h_L=h_L^{a,b;q,t}: \mathbb{E}[z]^S\rightarrow \mathbb{E}$$ by requiring $$h_L\bigl(P_\lambda^L\bigr)=
\begin{cases}
1,\qquad &\hbox{ if } \lambda=0,\\
0,\qquad &\hbox{ if } \lambda\not=0.
\end{cases}$$ Define a form $\langle \cdot,\cdot\rangle_L= \langle
\cdot,\cdot\rangle_L^{a,b;q,t}$ on $\mathbb{E}[z]^S$ by $$\label{Lpairing}
\langle
p_1,p_2\rangle_L=h_L\bigl(p_1(z)\overline{p_2(z)}\bigr),\qquad
p_1,p_2\in \mathbb{E}[z]^S,$$ where $p(z) \mapsto \overline{p(z)}$ stands for the anti-linear algebra involution on $\mathbb{E}[z]$ which extends complex conjugation on $\mathbb{C}$ by requiring that the parameters $a,b,c,d,q,t$ and the variables $z_j$ to be formally real, e.g. $\overline{a}=a$ and $\overline{z_j}=z_j$. The orthogonality relations now take the form $$\langle P_\lambda^L,P_\mu^L\rangle_L=N_L(\lambda)\delta_{\lambda,\mu},
\qquad \lambda,\mu\in\Lambda_n$$ for suitable explicit quadratic norms $N_L(\lambda)=N_L(\lambda;a,b;q,t)\in \mathbb{E}$, which are recalled in Subsection [\[little\]](#little){reference-type="ref" reference="little"}.

The expressions $$\label{Dgeneralized}
D_q(\lambda;a,b;t)=
\frac{\bigl(P_\lambda^L(0;q^{-1}a,q^{-1}b;q,t)\bigr)^2}{N_L(\lambda;q^{-1}a,q^{-1}b;q,t)}
\in \mathbb{E}, \qquad \lambda\in\Lambda_n$$ play a crucial role in the sequel. Note that $D_q(\lambda;a,b;t)$ is the generalized dimension $d(\lambda)$ from the introduction (see [\[tildeD\]](#tildeD){reference-type="eqref" reference="tildeD"}), up to a slight reparametrization of the four auxiliary parameters $a,b,q$ and $t$ (which we justify in a moment).

We show that specializations of the parameters $(a,b,t)$ in $D_q(\lambda)$ give the quantum dimensions of spherical irreducible representations associated to quantum complex Grassmannians. In addition we show that suitable degenerations in $(a,b,q,t)$ lead to the dimensions of spherical irreducible representations associated to complex/real Grassmannians (in which case the four parameters degenerate to one, but with different exponents), and to dimensions of spherical irreducible representations associated to Grassmannians over non-Archimedean local fields (in which case $q$ degenerates to zero while the remaining three parameters $(a,b,t)$ are specialized to $q$-independent values which are explicitly given in terms of the cardinality of the residue field). The latter case thus does not involve degenerating the parameters $(a,b,t)$, which is the reason to use the multivariable little $q$-Jacobi polynomials with parameters $(q^{-1}a, q^{-1}b,t)$ in the definition [\[Dgeneralized\]](#Dgeneralized){reference-type="eqref" reference="Dgeneralized"} of the generalized dimensions.

We derive evaluation formulas for $P_\lambda^L$ in Section [\[evaluation\]](#evaluation){reference-type="ref" reference="evaluation"}, which thus lead to explicit evaluations of $D_q(\lambda)=D_q(\lambda;a,b;t)$ and to explicit evaluations of the (quantum) dimensions for the irreducible spherical irreducible representations associated to different types of (quantum) Grassmannians.
