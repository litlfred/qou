---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-018-8-the-one-parameter-family-of-quantum-complex-gr
section_title: "The one-parameter family of quantum complex Grassmannians"
section_number: 8
pages: 35-40
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.977
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[]{#quantum label="quantum"}

In this section we consider the one-parameter family of quantum complex Grassmannians from [@NDS], [@DS] and [@OS] (see also [@L] for the general theory of harmonic analysis on quantum compact symmetric spaces). This more general set-up does no longer fit into the framework of quantum Gelfand pairs associated to [CQG]{.sans-serif} algebras as discussed in Section [\[CQG\]](#CQG){reference-type="ref" reference="CQG"}, since the role of the quantum subgroup is replaced by a suitable infinitesimal counterpart, depending on an additional continuous parameter.

In [@NDS] and [@DS] harmonic analysis on the one-parameter family of quantum complex Grassmannians was studied in detail, leading to the interpretation of Macdonald-Koornwinder polynomials and multivariable big and little $q$-Jacobi polynomials as the associated quantum zonal spherical functions. From these results we now derive representation theoretic interpretations of the evaluation formulas and norm formulas for Macdonald-Koornwinder polynomials and multivariable big and little $q$-Jacobi polynomials. The arguments follow closely [@N Section 6], now applied to the one-parameter family of quantum complex Grassmannians. In this more general context we discuss the quantum dimension formulas for irreducible spherical representations in terms of quantum zonal spherical functions. The analysis leads to the quantum dimension formulas [\[qcf\]](#qcf){reference-type="eqref" reference="qcf"} and [\[qcfcons\]](#qcfcons){reference-type="eqref" reference="qcfcons"} for the irreducible $\mathcal{U}_q$-representations $V_\lambda^q$ ($\lambda\in\Lambda_n$).

We now first recall the construction of the quantum zonal spherical functions on a one-parameter family of quantum analogues of the complex Grassmannian $\mathcal{K}/\mathcal{M}$. We will freely use the notations from Section [\[qGrassmannian\]](#qGrassmannian){reference-type="ref" reference="qGrassmannian"}. The role of the subgroup $\mathcal{M}$ is taken over by a two-sided co-ideal $\mathfrak{k}_\sigma\subseteq \mathcal{U}_q$ depending (in a suitable sense continuously) on an additional parameter $\sigma\in\mathbb{R}\cup \{\infty\}$, see e.g. [@NDS], [@DS] for the explicit definition of $\mathfrak{k}_\sigma$. The case $\sigma=\infty$ corresponds to the standard quantum complex Grassmannian from Section [\[qGrassmannian\]](#qGrassmannian){reference-type="ref" reference="qGrassmannian"}.

The space of $\mathfrak{k}_\sigma$-invariants in $\mathbb{C}_q(\mathcal{K})$, $$\mathbb{C}_q^\sigma(\mathcal{K}/\mathcal{M}):=\{f\in\mathbb{C}_q(\mathcal{K}) \,\, | \,\, f(YX)=0,\qquad \forall\, X\in\mathfrak{k}_\sigma,\,\,
\forall\, Y\in\mathcal{U}_q \}$$ is a $\mathcal{U}_q$-submodule of $\mathbb{C}_q(\mathcal{K})$ with respect to the regular $\mathcal{U}_q$-action $$\bigl(X\,f\bigr)(X^\prime)=f(S(X)X^\prime),\qquad f\in\mathbb{C}_q^\sigma(\mathcal{K}/\mathcal{M}),\quad X,X^\prime\in\mathcal{U}_q.$$ The $\mathcal{U}_q$-module $\mathbb{C}_q^\sigma(\mathcal{K}/\mathcal{M})$ serves as a one-parameter family of quantum analogues of the Grassmann representation $\mathbb{C}(\mathcal{K}/\mathcal{M})$. Furthermore, $\mathbb{C}_q^\infty(\mathcal{K}/\mathcal{M})$ is the Grassmann representation $\mathbb{C}_q(\mathcal{K}/\mathcal{M})$ associated to the standard quantum complex Grassmannian from Section [\[qGrassmannian\]](#qGrassmannian){reference-type="ref" reference="qGrassmannian"}. The space $$\bigl(L_\mu^q\bigr)^{\mathfrak{k}_\sigma}=\{v\in L_\mu^q \,\, | \,\, X v=0,\quad \forall\, X\in\mathfrak{k}_\sigma \}$$ for $\mu\in P_d^+$ serves as the one-parameter quantum analogue of the space of $\mathcal{M}$-fixed vectors in $L_\mu^{\mathbb{C}}$. The subspace $\bigl(L_\mu^q\bigr)^{\mathfrak{k}_\sigma}$ is one-dimensional or zero dimensional, and it is one-dimensional if and only if $\mu\in\Lambda_n^\natural$. Consequently, the irreducible spherical representations $V_\lambda^q=L_{\lambda^\natural}^q$ ($\lambda\in\Lambda_n$) associated to the standard quantum complex Grassmannian also serve as complete set of representatives of finite dimensional, irreducible $\mathcal{U}_q$-representations with nonzero (in fact, one-dimensional) space of $\mathfrak{k}_\sigma$-invariants. From the Peter-Weyl decomposition for $\mathbb{C}_q(\mathcal{K})$ we obtain the irreducible decomposition $$\mathbb{C}_q^\sigma(\mathcal{K}/\mathcal{M})\simeq \bigoplus_{\lambda\in\Lambda_n}
V_{\lambda}^q$$ as $\mathcal{U}_q$-modules. Furthermore, for $\mu\in P_d^+$ we recall from [@DS] that $$\bigl(L_\mu^q\bigr)^{\mathfrak{k}_\infty}=\bigl(L_\mu^q\bigr)^{\mathcal{U}_q(\mathfrak{m}_{\mathbb{C}})},$$ cf. Subsection [\[qGr\]](#qGr){reference-type="ref" reference="qGr"}.

We fix generic $\sigma,\tau\in\mathbb{R}$ unless specified differently (the case $\sigma=\infty$ and/or $\tau=\infty$ will subsequently be analyzed as degeneration of the theory for $\sigma, \tau \in\mathbb{R}$). For $\lambda\in\Lambda_n$ we choose a nonzero $\mathfrak{k}_\sigma$-fixed vector $v_\sigma(\lambda)\in \bigl(V_\lambda^q\bigr)^{\mathfrak{k}_\sigma}$ which we normalize by requiring $$v_\sigma(\lambda)=\sum_{\nu\in\mathbb{Z}^{d}}v_\sigma(\lambda;\nu),\qquad
v_\sigma(\lambda;\lambda^\natural)=u_{\lambda^\natural},$$ where $v_\sigma(\lambda;\nu)\in V_\lambda^q$ is the weight $\nu$ component of $v_\sigma(\lambda)$ in $V_\lambda^q$ and $u_{\lambda^\natural}$ is the highest weight vector of $V_\lambda^q=L_{\lambda^\natural}^q$ (it is known that $v_\sigma(\lambda)$ has a weight $\lambda^\natural$ component, hence such a normalization is possible). From the analysis in [@DS Section 6] it furthermore follows that $\bigl(V_\lambda^q\bigr)^{\mathfrak{k}_\sigma^*}$ is spanned by $K^{-\delta}v_{\sigma+d-2n}(\lambda)$ for $\lambda\in\Lambda_n$ (see also [@OS] for the special case $d=2n$).

The normalized quantum zonal spherical functions $\varphi_\lambda^{\sigma,\tau}$ ($\sigma,\tau\in\mathbb{R}$) associated to the one-parameter family of quantum Grassmannians are now defined by $$\label{zsf}
\varphi_\lambda^{\sigma,\tau}(\,\cdot\,)=q^{\langle \delta,\lambda^\natural\rangle}
\frac{\langle \cdot\, v_\sigma(\lambda),
K^{-\delta}v_{\tau+d-2n}(\lambda)\rangle_{\lambda}}
{\langle u_{\lambda^\natural},u_{\lambda^\natural}\rangle_{\lambda}},\qquad \lambda\in\Lambda_n.$$ The $\varphi_\lambda^{\sigma,\tau}$ ($\lambda\in\Lambda_n$) form a basis of $$\mathcal{H}_{\sigma,\tau}:=\{f\in \mathbb{C}_q(\mathcal{K}) \,\, | \,\, f(YZ)=0=f(ZX),\quad
Z\in\mathcal{U}_q,\,\, X\in \mathfrak{k}_\sigma,\,\,
Y\in\mathfrak{k}_\tau \}.$$ The analogue of the quantum dimension formula [\[dimforquantum\]](#dimforquantum){reference-type="eqref" reference="dimforquantum"} in terms of the quantum zonal spherical functions $\varphi_\lambda^{\sigma,\tau}$ ($\lambda\in\Lambda_n$) reads as follows.

::: lem
For $\lambda\in\Lambda_n$ and generic $\sigma,\tau\in\mathbb{R}$ we have $$\label{dimforquantumst}
\textup{Dim}_q\bigl(V_\lambda^q\bigr)=\frac{\varphi_\lambda^{\sigma,\sigma+2n-d}(K^{\delta})\varphi_\lambda^{\tau+d-2n,\tau}(K^\delta)}
{\|\varphi_\lambda^{\sigma,\tau}\|_h^2}.$$
:::

::: proof
*Proof.* By the quantum Schur orthogonality relations (see Proposition [\[Schur\]](#Schur){reference-type="ref" reference="Schur"}**b**) we have $$\label{ato}
\|\varphi_\lambda^{\sigma,\tau}\|_h^2=\frac{q^{2\langle\delta,\lambda^\natural\rangle}}{\textup{Dim}_q(V_\lambda^q)}
\frac{\|v_\sigma(\lambda)\|_\lambda^2 \|v_{\tau+d-2n}(\lambda)\|_\lambda^2}{\|u_{\lambda^\natural}\|_\lambda^4},$$ where $\|v\|_{\lambda}^2:=\langle v, v\rangle_{\lambda}$. On the other hand, from the definition [\[zsf\]](#zsf){reference-type="eqref" reference="zsf"} of the quantum zonal spherical function $\varphi_\lambda^{\sigma,\tau}$ we have $$\label{bto}
\varphi_\lambda^{\sigma,\sigma+2n-d}(K^\delta)=\frac{\|v_\sigma(\lambda)\|_\lambda^2}{\|u_{\lambda^\natural}\|_\lambda^2}\,
q^{\langle\delta,\lambda^\natural\rangle}.$$ The desired quantum dimension formula follows directly from [\[ato\]](#ato){reference-type="eqref" reference="ato"} and [\[bto\]](#bto){reference-type="eqref" reference="bto"}. ◻
:::

To arrive at an explicit evaluation of the quantum dimensions, we now translate [\[dimforquantumst\]](#dimforquantumst){reference-type="eqref" reference="dimforquantumst"} into an expression involving the evaluations and the quadratic norms of Macdonald-Koornwinder polynomials.

The radial part $P_\lambda^{\sigma,\tau}:=\hbox{Res}_T\bigl(\varphi_\lambda^{\sigma,\tau}\bigr)\in
\mathbb{C}[u^{\pm 1}]$ is defined to be the unique Laurent polynomial in $d$ independent variables $u_1,\ldots,u_{d}$ such that $$P_\lambda^{\sigma,\tau}(q^\nu)=
\varphi_\lambda^{\sigma,\tau}(K^{\nu})\qquad\forall\,\nu\in\mathbb{Z}^{d}.$$ We have the following key facts from [@NDS], see also [@DS] and [@OS]. Set $z_j=u_ju_{d+1-j}^{-1}$ ($j=1,\ldots,n$), then $$P_\lambda^{\sigma,\tau}\in \mathbb{C}[z^{\pm 1}]^W,\qquad
\forall\lambda\in \Lambda_n,$$ where $W=S_n\ltimes\{\pm 1\}^n$ as before. From now on we will view $P_\lambda^{\sigma,\tau}$ as $W$-invariant Laurent polynomial in the independent variables $z_1,\ldots,z_n$. The key result is the identification of $P_\lambda^{\sigma,\tau}$ with Macdonald-Koornwinder polynomials, $$P_\lambda^{\sigma,\tau}(z)=
P_\lambda(z;-q^{\sigma+\tau+1},-q^{-\sigma-\tau+1},q^{\sigma-\tau+1},
q^{-\sigma+\tau+2(d-2n)+1};q^2,q^2),\qquad\lambda\in\Lambda_n$$ (the particular normalization of $\varphi_\lambda^{\sigma,\tau}$ ensures that it precisely coincides with the monic Macdonald-Koornwinder polynomial). We denote $\langle \cdot,\cdot\rangle_{\sigma,\tau}$ for the corresponding orthogonality pairing [\[Kpairing\]](#Kpairing){reference-type="eqref" reference="Kpairing"}, with the six parameters $(a,b,c,d,q,t)$ specialized to $$(-q^{\sigma+\tau+1},-q^{-\sigma-\tau+1},q^{\sigma-\tau+1},
q^{-\sigma+\tau+2(d-2n)+1},q^2,q^2).$$ We set $\|p\|_{\sigma,\tau}^2=\langle p,p\rangle_{\sigma,\tau}^2$ for the corresponding quadratic norm of $p\in\mathbb{C}[z^{\pm 1}]^W$.

::: lem
For $\lambda\in\Lambda_n$ and generic $\sigma,\tau\in\mathbb{R}$ we have $$\begin{split}
\varphi_\lambda^{\sigma,\tau}(K^\delta)&=P_\lambda^{\sigma,\tau}(q^{d-2n+1}q^{2\rho}),\\
\|\varphi_{\lambda}^{\sigma,\tau}\|_h^2&=
\|P_\lambda^{\sigma,\tau}\|_{\sigma,\tau}^2.
\end{split}$$ In particular, $$\label{normevaluationcombi}
\hbox{Dim}_q\bigl(V_\lambda^q\bigr)=\frac{P_\lambda^{\sigma,\sigma+2n-d}(q^{d-2n+1}q^{2\rho})
P_\lambda^{\tau+d-2n,\tau}(q^{d-2n+1}q^{2\rho})}
{\|P_\lambda^{\sigma,\tau}\|_{\sigma,\tau}^2}.$$
:::

::: proof
*Proof.* Observe that $u=q^\delta\in \bigl(\mathbb{R}^\times\bigr)^d$ maps to $z=q^{d-2n+1}q^{2\rho}\in\bigl(\mathbb{R}^\times\bigr)^n$ under the assignment $z_j=u_ju_{d+1-j}^{-1}$ ($j=1,\ldots,n$). By the definition of $P_\lambda^{\sigma,\tau}$ as the radial part of $\varphi_\lambda^{\sigma,\tau}$, we obtain the desired expression of $\varphi_\lambda^{\sigma,\tau}(K^\delta)$ in terms of Macdonald-Koornwinder polynomials. The quadratic norm formula follows from [@DS Corollary 8.1]. The quantum dimension formula [\[dimforquantumst\]](#dimforquantumst){reference-type="eqref" reference="dimforquantumst"} then yields [\[normevaluationcombi\]](#normevaluationcombi){reference-type="eqref" reference="normevaluationcombi"}. ◻
:::

We are now in a position to derive the explicit quantum dimension formulas for the spherical $\mathcal{U}_q$-representations $V_\lambda^q$ ($\lambda\in\Lambda_n$).

::: cor
[]{#quantumcomplexformulacor label="quantumcomplexformulacor"} Proposition [\[quantumcomplexformula\]](#quantumcomplexformula){reference-type="ref" reference="quantumcomplexformula"} holds.
:::

::: proof
*Proof.* Observe that the value of the Macdonald-Koornwinder polynomial $$P_\lambda^{\sigma,\sigma+2n-d}(z)=
P_{\lambda}(z;-q^{2\sigma+2n-d+1}, -q^{-2\sigma-2n+d+1},
q^{d-2n+1}, q^{d-2n+1};q^2,q^2),$$ at $z=q^{d-2n+1}q^{2\rho}$ can be evaluated in closed form by the evaluation formula [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} for Macdonald-Koornwinder polynomials. The resulting expression is $$\begin{split}
P_\lambda^{\sigma, \sigma+2n-d}(q^{d-2n+1}q^{2\rho})
&=q^{(2n-d-1)|\lambda|-2\langle\rho,\lambda\rangle}\\
&\times\prod_{1\leq
j<k\leq
n}\frac{(1-q^{2(d-2n+1+\lambda_j+\lambda_k+\rho_j+\rho_k)})
(1-q^{2(\lambda_j-\lambda_k
+\rho_j-\rho_k)})}
{(1-q^{2(d-2n+1+\rho_j+\rho_k)})(1-q^{2(\rho_j-\rho_k)})}\\
\times&\prod_{i=1}^n\frac{\bigl(q^{2(d-2n+1+\rho_i)},q^{2(d-2n+1+\rho_i)},
-q^{2(\sigma+1+\rho_i)},
-q^{2(-\sigma+d-2n+1+\rho_i)};q^2\bigr)_{\lambda_i}}
{\bigl(q^{2(d-2n+1+2\rho_i)};q^2\bigr)_{2\lambda_i}}.
\end{split}$$ On the other hand, by the closed expression [\[normKoorn\]](#normKoorn){reference-type="eqref" reference="normKoorn"} for the quadratic norms of the Macdonald-Koornwinder polynomials we have $$\begin{split}
\|P_\lambda^{\sigma,\tau}\|_{\sigma,\tau}^2&=\prod_{j=1}^n
\left\{\frac{\bigl(q^{2(1+\rho_j)},
q^{2(d-2n+1+\rho_j)};q^2\bigr)_{\lambda_j}^2}{\bigl(q^{2(d-2n+1+2\rho_j)},
q^{2(d-2n+2+2\rho_j)};q^2\bigr)_{2\lambda_j}}\right.\\
&\left.\times\bigl(-q^{2(\sigma+1+\rho_j)},
-q^{2(-\sigma+d-2n+1+\rho_j)}, -q^{2(\tau+d-2n+1+\rho_j)},
-q^{2(-\tau+1+\rho_j)};q^2\bigr)_{\lambda_j}\right\}.
\end{split}$$ Combining these explicit formulas with [\[normevaluationcombi\]](#normevaluationcombi){reference-type="eqref" reference="normevaluationcombi"} we obtain an explicit expression for $\hbox{Dim}_q(V_\lambda^q)$, which results in Proposition [\[quantumcomplexformula\]](#quantumcomplexformula){reference-type="ref" reference="quantumcomplexformula"}. ◻
:::

We end this section by considering the $\sigma\rightarrow \infty$ and $\sigma=\tau\rightarrow\infty$ degenerations in the above representation theoretic formulas. This in particular leads to the interpretation of $D_q(\lambda;a,b;t)$ for special values of the parameters as quantum dimensions of $V_\lambda^q$ ($\lambda\in\Lambda_n$), see [\[qcfcons\]](#qcfcons){reference-type="eqref" reference="qcfcons"}.

In [@DS] the limit $\sigma\rightarrow\infty$ (respectively $\sigma,\tau\rightarrow\infty$) is considered, leading to the interpretation of the multivariable big $q$-Jacobi polynomials $P_\lambda^B(\cdot;1,q^{2(d-2n)},1,q^{2\tau+2(d-2n)};q^2,q^2)$ (respectively the multivariable little $q$-Jacobi polynomials $P_\lambda^L(\cdot;q^{2(d-2n)},1;q^2,q^2)$) as radial parts of quantum zonal spherical functions associated to the standard quantum Grassmann representation $\mathbb{C}_q^\infty(\mathcal{K}/\mathcal{M})=\mathbb{C}_q(\mathcal{K}/\mathcal{M})$. In these degenerations, the quantum dimensions $\hbox{Dim}_q(V_\lambda^q)$ are naturally expressed in terms of the multivariable big and little $q$-Jacobi polynomials as follows.

::: prop
[]{#propdim label="propdim"} We have $$\textup{Dim}_q(V_\lambda^q)=
\bigl(-q^{2\tau+d-2n-1}\bigr)^{|\lambda|}\frac{P_\lambda^L(0;q^{2(d-2n)},1;q^2,q^2)P_\lambda^{\tau+d-2n,\tau}(q^{d-2n+1}q^{2\rho})}
{N_B(\lambda;1,q^{2(d-2n)},1,q^{2\tau+2(d-2n)};q^2,q^2)},\qquad \forall\,\lambda\in\Lambda_n.$$ Furthermore, in terms of the generalized quantum dimension $D_q(\lambda;a,b;t)$, see [\[Dgeneralized\]](#Dgeneralized){reference-type="eqref" reference="Dgeneralized"}, we have $$\textup{Dim}_q(V_\lambda^q)=
\frac{\bigl(P_\lambda^L(0;q^{2(d-2n)},1;q^2,q^2)\bigr)^2}{N_L(\lambda;q^{2(d-2n)},1;q^2,q^2)}=
D_{q^2}(\lambda;q^{2(d-2n+1)}, q^2;q^2),\qquad \forall\,\lambda\in\Lambda_n.$$
:::

::: proof
*Proof.* We degenerate the expression [\[normevaluationcombi\]](#normevaluationcombi){reference-type="eqref" reference="normevaluationcombi"} of the quantum dimension $\hbox{Dim}_q(V_\lambda^q)$ by taking the limit $\sigma\rightarrow\infty$ (respectively $\sigma=\tau\rightarrow\infty$). In order to parallel the particular degeneration scheme from [@DS], we make use of the elementary symmetry $$\label{symmKo}
P_\lambda(-z;-a,-b,-c,-d;q,t)=(-1)^{|\lambda|}P_\lambda(z;a,b,c,d;q,t)$$ for the monic Macdonald-Koornwinder polynomials, which implies the symmetry $$\label{symmnorm}
N_K(\lambda;-a,-b,-c,-d;q,t)=N_K(\lambda;a,b,c,d;q,t),\qquad\lambda\in\Lambda_n$$ for the corresponding quadratic norms (which also immediately follows from its explicit evaluation [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"}). Combined with the limit formula [\[limitBnorms\]](#limitBnorms){reference-type="eqref" reference="limitBnorms"} in base $q^2$, with parameters $(a,b,c,d,t)$ specialized to $(1,q^{2(d-2n)},1,q^{2\tau+2(d-2n)},q^2)$ and with $\epsilon=q^{\sigma+\tau-1}$, we obtain $$\lim_{\sigma\rightarrow\infty}q^{2(\sigma+\tau-1)|\lambda|}\|P_\lambda^{\sigma,\tau}\|_{\sigma,\tau}^2=
N_B(\lambda;1,q^{2(d-2n)},1,q^{2\tau+2(d-2n)};q^2,q^2),\qquad \forall\,\lambda\in\Lambda_n.$$ On the other hand, from [\[L1\]](#L1){reference-type="eqref" reference="L1"} and the explicit evaluation formula from the proof of Corollary [\[quantumcomplexformulacor\]](#quantumcomplexformulacor){reference-type="ref" reference="quantumcomplexformulacor"} we obtain $$\lim_{\sigma\rightarrow\infty}\bigl(-q^{2\sigma}\bigr)^{|\lambda|}P_\lambda^{\sigma,\sigma+2n-d}(q^{d-2n+1}q^{2\rho})=
q^{(d-2n+1)|\lambda|}P_\lambda^L(0;q^{2(d-2n)},1;q^2;q^2),\qquad \forall\,\lambda\in\Lambda_n.$$ Taking the limit $\sigma\rightarrow\infty$ in [\[normevaluationcombi\]](#normevaluationcombi){reference-type="eqref" reference="normevaluationcombi"} now leads to the expression of the quantum dimension as mixture of factors involving Macdonald-Koornwinder, multivariable big and multivariable little $q$-Jacobi polynomials.

Taking $\tau=\sigma$ in [\[normevaluationcombi\]](#normevaluationcombi){reference-type="eqref" reference="normevaluationcombi"} and using the fact that $$\lim_{\sigma\rightarrow\infty}\bigl(q^{-1+2\sigma}\bigr)^{2|\lambda|}\|P_\lambda^{\sigma,\sigma}\|_{\sigma,\sigma}^2=
N_L(\lambda;q^{2(d-2n)},1;q^2,q^2),\qquad
\forall\,\lambda\in\Lambda_n$$ in view of [\[limitLnorms\]](#limitLnorms){reference-type="eqref" reference="limitLnorms"}, we similarly obtain the desired expression of the quantum dimension $\hbox{Dim}_q(V_\lambda^q)$ in terms of $D_q(\lambda;a,b;t)$. ◻
:::

::: rema
[]{#standardrema label="standardrema"} By the arguments from [@DS] one can show that $$\lim_{\sigma\rightarrow\infty}\left(\frac{\varphi_\lambda^{\sigma,\sigma+2n-d}}{\|\varphi_{\lambda}^{\sigma,\sigma+2n-d}\|_h}\right)=
\varphi_\lambda^q,\qquad \lambda\in\Lambda_n$$ in the pre-Hilbert space $\mathbb{C}_q(\mathcal{K})$, where $\varphi_\lambda^q$ ($\lambda\in\Lambda_n$) are the (orthonormal) quantum zonal spherical functions associated to the standard quantum complex Grassmanian. Degenerating [\[dimforquantumst\]](#dimforquantumst){reference-type="eqref" reference="dimforquantumst"} accordingly, we obtain the quantum dimension formula [\[dimforquantum\]](#dimforquantum){reference-type="eqref" reference="dimforquantum"}.
:::
