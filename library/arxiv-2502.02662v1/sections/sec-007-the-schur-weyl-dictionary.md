---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-007-the-schur-weyl-dictionary
section_title: "The Schur-Weyl Dictionary"
section_number: null
pages: 10-12
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 1.0
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
Our aim in this section is to review how the Schur-Weyl duality can be leveraged to explicitly rewrite the observables of two-dimensional Yang-Mills theory in terms of symmetric group quantities[@Gross:1992tu; @Gross:1993hu; @Cordes:1994fc; @Novak:2023bft]. Our goal is to claim that a certain sector of two-dimensional Yang-Mills theory at large $N$ is captured by a deformed Hurwitz theory.

We recall that representations of the symmetric group $S_d$ are indexed by Young diagrams with exactly $d$ boxes, and representations of the unitary group $U(N)$ relevant to the study of two-dimensional Yang-Mills theory are indexed by Young diagrams with at most $N$ rows [@Cordes:1994fc]. The Schur-Weyl duality relates various quantities of unitary group and symmetric group representations indexed by the same Young diagram.

Consider first the equation for the quadratic Casimir of a representation of the unitary group $U(N)$ indexed by a Young diagram $\lambda$ with $d$ boxes : $$c_{2}(\lambda)=dN+2 f_2(\lambda)\, .
    \label{Splitting}$$ The function $f_2(\lambda)$ denotes the Fourier transform of the conjugacy class of transpositions, as defined in equation [\[GeneralizedCharacters\]](#GeneralizedCharacters){reference-type="eqref" reference="GeneralizedCharacters"}. The exponential term may then be split into two parts and the correlators can be rewritten as $$Z[M_G,U_i]=\sum_{d} q^{d} \sum_{\lambda\in Y^d_N} \frac{s_{\lambda}(U_1)\cdots s_{\lambda}(U_k)} {(\dim W_N^{\lambda})^{2g-2+k}} \exp\left(-\frac{g_{YM}^2 A}{N}\, f_{2}(\lambda)\right)\, ,
    \label{NotYetChiral}$$ where $q:=e^{-\frac{g_{YM}^2 A}{2}}$. Next, we write the dimensions of the unitary group representation $W^{\lambda}_N$ as $$\dim W^{\lambda}_N=\frac{N^d}{d!}\Omega_{\frac{1}{N}}(\lambda) \, d_{\lambda}\, ,
    \label{dimension}$$ where $d_{\lambda}$ is the dimension of the irreducible representation of the symmetric group indexed by $\lambda$. The function $\Omega_{s}$ is the Fourier transform of the exponential distance operator defined as [@Novak:2023bft] [^1]

$$\begin{aligned}
    \Omega_s :=&\, \sum_{\eta\vdash d} s^{\lvert \eta \rvert} C_{\eta}\\
    =&\, C_e + s C_2 + s^2 (C_3+C_{2,2})  + \mathcal{O}(s^3)\, \, ,
\end{aligned}$$ where $\lvert \eta \rvert$ denotes the charge of the permutation $\eta$, namely we have $\lvert \eta \rvert := d-l(\eta)$. The operator $\Omega_s$ depends on a free parameter $s$.

For generic values of the parameter $s$, the exponential distance operator is invertible. Indeed, if one writes $\Omega_s=C_e+s \omega$, then $$\Omega_s^{-1} = C_e - s \omega + s^2 \omega^2 + \dots$$ This series can be shown to converge absolutely when $s\neq 1, \dots, d-1$ [@Novak:2023bft]. Conversely, if the parameter $s$ takes one of these values, then the operator $\Omega_s^{-1}$ becomes singular. The value of the operator $\Omega_{s}^{-1}$ on partitions of length smaller than $N$ is still well-defined but it diverges for partitions of length larger than $N$. This is merely a consequence of the fact that we take fictitious representations of $U(N)$ to have vanishing dimension, as can be seen from equation [\[dimension\]](#dimension){reference-type="eqref" reference="dimension"}.

The explicit algebraic description of the operators $\Omega_s^{\pm 1}$ provides a direct hands-on description of the computational consequences of the compactification of Hurwitz spaces suggested in [@Cordes:1994fc].

To complete the Schur-Weyl dictionary, we discuss how insertions in Yang-Mills translate to the Hurwitz theory. We have the identity $$s_{\lambda}(U)=\frac{d_{\lambda}}{d!}\sum_{\alpha\in Y^d} p_{\alpha}(U) f_{\alpha}(\lambda)\, 
    \label{SchurToPower}$$ where the power-sum polynomials $p_\alpha(U)$ are defined as $$p_{\alpha}(U)=\prod_{i=1}^{l(\alpha)} \tr U^{\alpha_i}\, .$$ One recognizes in equation [\[SchurToPower\]](#SchurToPower){reference-type="eqref" reference="SchurToPower"} the change of basis that relates Schur functions and power sum polynomials. Substituting all of these identities in the partition function of the Yang-Mills theory we obtain $$Z[M_G,U_i]=\sum_d (q N^{2-2G-k})^d\, Z_{d}[M_G,U_i]\, ,
    \label{dSum}$$ where we defined the fixed-degree result $$\begin{gathered}
     Z_{d}[M_G,U_i]:= \sum_{\lambda\in Y_N^d} \left(\frac{ d_{\lambda}}{d!}\right)^{2-2G} \prod_{i=1}^{k} \left(\sum_{\alpha\in Y^d} p_{\alpha}(U_i) f_{\alpha}(\lambda) \cdot \Omega_{1/N}^{-1}(\lambda)\right)\\ (\Omega_{1/N}(\lambda))^{2-2G} \exp\left(-\frac{g_{YM}^2 A}{N}f_{2}(\lambda)\right)\, .
     \label{ExactCorrelators}
\end{gathered}$$ Note that this definition of $Z_d$ differs from the one introduced in section [\[YMObservables\]](#YMObservables){reference-type="ref" reference="YMObservables"} by a factor $q^d N^{(2-2G-k)d}$. From now on, $Z_d$ will always denote the factored out fixed-degree correlator. We stress that equation [\[dSum\]](#dSum){reference-type="eqref" reference="dSum"} is an exact expression for the correlators of the full two-dimensional Yang-Mills theory in terms of symmetric group quantities.

[^1]: In practice, we often think of $\Omega$ as a linear combination of conjugacy classes. Nevertheless, one can think instead of its Fourier transform $\Omega(\lambda)$ which is an operator on the set of representations of $S_d$ [@Novak:2023bft]. Our notation does not differentiate these two perspectives on $\Omega$.
