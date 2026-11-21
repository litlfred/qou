---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-003-3-gauge-transformations
section_title: "Gauge Transformations"
section_number: 3
pages: 8-10
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.986
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
---
To prove the theorem stated in the introduction, it remains to identify the category $\text{\bf Rep}_{\text{f}}(R_V)$ for $V$ being the vector representation of $U_q({\widehat{\mathfrak{s}}l}_n)$ with the category of representations of Felder's elliptic quantum group. To construct such an identification is the goal of this section. It is achieved by using the fact that the corresponding dynamical R-matrices are gauge equivalent [@Mou01].

The concept of gauge transformations of quantum dynamical R-matrices of $\mathfrak{gl}_n$ type, that we briefly recall now, was introduced in [@EtVa98].

Let $\mathfrak{h}$ be an abelian $n$-dimensional Lie algebra. A multiplicative $m$-form on $\mathfrak{h}^*$ is a collection of meromorphic functions $\varphi = \{\varphi_{a_1,\dots,a_m}(\lambda)\}$ where $\{a_1, \dots, a_m\}$ runs through all (ordered) subsets of $\{1,\dots,n\}$ such that $$\varphi_{a_1,\dots,a_{i+1},a_i,\dots,a_m}(\lambda)\varphi_{a_1,\dots,a_m}(\lambda)=1$$ Let $\Omega^m$ be the set of all multiplicative $m$-forms. With the obvious definitions one turns $\Omega^m$ into an abelian group where the neutral element is the constant form $\mathbf{1}_{a_1,\dots,a_m}(\lambda) = 1$.

For a given $\gamma \in \text{$\mathbb{C}$}^*$ and $s \in \{1, \dots, n\}$ define the operator $\delta_s$ on the space of meromorphic functions on $\mathfrak{h}^*$ given by $$\delta_s f(\lambda_1, \dots, \lambda_n) = \frac{f(\lambda_1, \dots, \lambda_n)}{f(\lambda_1, \dots,\lambda_s-\gamma,\dots, \lambda_n)}$$ and then the differential homomorphism $d_{\gamma} : \Omega^m \to \Omega^{m+1}$, $\varphi \mapsto d_{\gamma}\varphi$, where $$(d_{\gamma}\varphi)_{a_1,\dots, a_{m+1}}(\lambda) = \prod_{s=1}^{m+1} \big(\delta_{a_s} \varphi_{a_1,\dots,a_{s-1},a_{s+1},\dots, a_{m+1}}(\lambda)\big)^{(-1)^{s+1}}$$ We have $d^2_{\gamma}\varphi =\mathbf{1} \,\forall\,\varphi$. A form $\varphi$ is said to be $\gamma$-closed if $d_{\gamma}\varphi = \mathbf{1}$ and $\gamma$-exact if $\varphi = d_{\gamma}\psi$ for some form $\psi$. When $\gamma =1$ we just say that $\varphi$ is closed or exact and denote $d_1$ simply by $d$.

We list now the gauge transformations that will be important for us. Let $R$ be an R-matrix of $\mathfrak{gl}_n$ type and step $\gamma$ and define the following transformations

$$\label{eq:g4}
R(u,\lambda) \mapsto c(u)R(u,\lambda)$$ where $c(u)$ is a meromorphic scalar function; $$\label{eq:g5}
R(u,\lambda) \mapsto R(au,b\lambda + \mu)$$ where $a,b \in \text{$\mathbb{C}$}^*$ and $\mu \in \mathfrak{h}^*$; $$\begin{gathered}
\notag
R(u,\lambda) \mapsto \\\label{eq:g2}
\sum_{m=0}^{n} \alpha_{m,m}(u,\lambda)E_{m,m}\otimes E_{m,m} + \sum_{m\neq l} \varphi_{m,l}(\lambda)\alpha_{m,l}(u,\lambda) E_{m,m}\otimes E_{l,l} + \beta_{m,l}(u,\lambda) E_{l,m}\otimes E_{m,l}
\end{gathered}$$ where $\varphi=\{\varphi_{m,l}(\lambda)\}$ is a $\gamma$-closed 2-form.

It was proved in [@EtVa98] that if $\tilde R$ is obtained from $R$ by these gauge transformations, then it is a quantum dynamical R-matrix of $\mathfrak{gl}_n$ type and step $\gamma$ (for [\[eq:g4\]](#eq:g4){reference-type="eqref" reference="eq:g4"} and [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"}) or $\gamma/b$ (for [\[eq:g5\]](#eq:g5){reference-type="eqref" reference="eq:g5"}). It is clear that if $\tilde R$ is obtained from $R$ by [\[eq:g4\]](#eq:g4){reference-type="eqref" reference="eq:g4"} and [\[eq:g5\]](#eq:g5){reference-type="eqref" reference="eq:g5"}, then $\text{\bf Rep}_{\text{f}}(\tilde R)$ is equivalent to $\text{\bf Rep}_{\text{f}}(R)$. The following theorem, concerning gauge transformation [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"}, was proved in [@EtVa99] in the language of bialgebroids. We repeat the proof here with the appropriate adaptations for this context.

::: thm
[]{#thm:g2 label="thm:g2"} Let $R$ be a quantum dynamical R-matrix of $\mathfrak{gl}_n$ type and step $\gamma$ and $\varphi$ be a $\gamma$-exact 2-form. If $\tilde R$ is obtained from $R$ by [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"} with this $\varphi$ then $\text{\bf Rep}_{\text{f}}(\tilde R) \cong \text{\bf Rep}_{\text{f}}(R)$
:::

::: proof
*Proof.* Let $\varphi = d_{\gamma}\zeta$ and set $\xi = \sum_a \zeta_a E_{a,a}$. Note first that we can write $$\tilde R(u,\lambda) = (\xi^{(1)}(\lambda-\gamma h^{(2)}))^{-1} (\xi^{(2)}(\lambda))^{-1} R(u,\lambda) \xi^{(1)}(\lambda) \xi^{(2)}(\lambda-\gamma h^{(1)})$$ Then let $(W,L)$ be a representation of $R$ and set $$\tilde L(u,\lambda) = (\xi^{(1)}(\lambda-\gamma h^{(2)}))^{-1}L(u,\lambda)\xi^{(1)}(\lambda)$$ Now it is easy to check that the functor $(W,L) \mapsto (W,\tilde L)$ (identity on morphisms) is an equivalence of tensor categories. ◻
:::

One can regard the exchange matrix $R_{\text{$\mathbb{C}$}^n}$ of example [\[ex:sln\]](#ex:sln){reference-type="ref" reference="ex:sln"} as defined on the whole Cartan sub-algebra of $\mathfrak{gl}_n$. Then, if one looks at the coordinate $k$ as a parameter, it is a quantum dynamical R-matrix of $\mathfrak{gl}_n$ type.

::: thm
[]{#thm:Rk=Rell label="thm:Rk=Rell"}[@Mou01] Let $R^{ell}_{\tau,\gamma}$ be the elliptic quantum dynamical R-matrix of example [\[ex:felder\]](#ex:felder){reference-type="ref" reference="ex:felder"}. Then $R_{\text{$\mathbb{C}$}^n}$ is gauge equivalent to $R^{ell}_{\tau,\gamma}$ for $\gamma = \frac{\log q}{\pi i}$ and $\tau = -\kappa\gamma = -\kappa\frac{\log q}{\pi i}$, where $\kappa = k+n$.
:::

The three gauge transformations we have listed are used in theorem [\[thm:Rk=Rell\]](#thm:Rk=Rell){reference-type="ref" reference="thm:Rk=Rell"}. In particular, the gauge transformation of type [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"} used is given by the following multiplicative 2-form $$\label{eq:varphi}
\varphi_{i,j}(\lambda) = \sigma_{j,i}(\lambda/\gamma-\rho)$$ where, for $m<l$, $$\sigma_{l,m}(\lambda) = q\frac{\Gamma_p(1+\frac{1}{\kappa}(\lambda+\rho)_{l,m}+\frac{1}{\kappa})} {\Gamma_p(1+\frac{1}{\kappa}(\lambda+\rho)_{l,m})} \frac{\Gamma_p(-\frac{1}{\kappa}(\lambda+\rho)_{l,m})} {\Gamma_p(-\frac{1}{\kappa}(\lambda+\rho)_{l,m}+\frac{1}{\kappa})} \quad, \sigma_{m,l}(\lambda) = \frac{1}{\sigma_{l,m}(\lambda)},$$ and $\Gamma_q$ is the q-Gamma function.

::: lem
[]{#lem:exact label="lem:exact"} The multiplicative 2-form [\[eq:varphi\]](#eq:varphi){reference-type="eqref" reference="eq:varphi"} is $\gamma$-exact.
:::

::: proof
*Proof.* It is enough to show that $\tilde{\varphi}_{i,j}(\lambda) = \varphi_{i,j}(\gamma\lambda)$ is exact. Let $\xi = \{\xi_j\}$ be the 1-form given by $\xi_j(\lambda) = \prod_{i<j}q^{\lambda_i}$. Then $\delta_s\xi_j(\lambda) = 1$ if $s>j$ and $\delta_s\xi_j(\lambda) = q$ if $s<j$. Therefore, for $m<l$, $(d\xi)_{m,l}(\lambda) =q$ and $(d\xi)_{l,m}(\lambda) = q^{-1}$. In a similar way one proves that $\tilde{\varphi} = d(\xi\eta\zeta)$ where $$\eta_j(\lambda) = \prod_{i<j}\Gamma_p\Big(\frac{\lambda_{i,j}+1}{\kappa}\Big)^{-1} \qquad\text{and}\qquad \zeta_j(\lambda) = \prod_{i<j}\Gamma_p\Big(1+\frac{\lambda_{j,i}}{\kappa}\Big)^{-1}$$ ◻
:::

Thus, we have constructed the equivalence of categories ${\text{$\mathcal{G}$}}: \text{\bf Rep}_{\text{f}}(R_V)\to \text{\bf Rep}_{\text{f}}(R_{\tau,\gamma}^{ell})$, where $V=\text{$\mathbb{C}$}^n$, and hence, proved the following theorem, which is our main result.

::: thm
[]{#mainth label="mainth"} The functor ${\text{$\mathcal{F}$}}={\text{$\mathcal{G}$}}
\text{$\mathcal{F}$}_V:\text{\bf Rep}_{\text{f}}(U_q(\widehat{\mathfrak{sl}}_n))\otimes_{\text{$\mathbb{C}$}}M_V\to \text{\bf Rep}_{\text{f}}(R^{ell}_{\tau,\gamma})$ is an exact, fully faithful tensor functor, which defines an equivalence of $\text{\bf Rep}_{\text{f}}(U_q({\widehat{\mathfrak{s}}l}_n))\otimes_{\text{$\mathbb{C}$}}M_V$ with a full subcategory of $\text{\bf Rep}_{\text{f}}(R^{ell}_{\tau,\gamma})$.
:::
