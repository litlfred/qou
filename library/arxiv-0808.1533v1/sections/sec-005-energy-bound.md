---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S 3"
section_id: sec-005-energy-bound
section_title: "Energy bound."
section_number: null
pages: 23-27
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.993
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
[]{#sec:energy label="sec:energy"}

In this section we indicate how the quantity $\mathsf{H}_{123}(X;\mathcal{T})$ invariant under frozen-in-field deformations provides a lower bound for the $L^2$-energy $E_2(X)$ of a volume preserving field $X$ on $M=S^3$. For simplicity we restrict our considerations to the case of an invariant unlinked handlebody $\mathcal{T}$, as in Section [\[sec:handlebody\]](#sec:handlebody){reference-type="ref" reference="sec:handlebody"}. For the notation used in this section see Appendix C.

Recall the definition $$\label{eq:energy}
 E_2(X)=\int_M |X|^2 = \|X\|^2_{L^2(M)}\ .$$ The ordinary helicity $\mathsf{H}_{12}(X)$ provides the well known lower bound (see [@Khesin98 p. 123]): $$\frac{1}{\lambda_1}|\mathsf{H}_{12}(X)|\leq  E_2(X),$$ where $\lambda_1$ is the first eigenvalue of the elliptic self adjoint operator $\ast\,d:\Omega^1(M)\mapsto \Omega^1(M)$ (i.e. the curl operator). Importance of such lower energy bounds,

stems from an area of interest in the ideal magneto-hydrodynamics, [@Priest84], as this constrains the phenomenon of "magnetic relaxation". A need for higher helicities can be justified by the fact that one may easily produce examples of vector fields $X$ for which $\mathsf{H}_{12}(X)$ vanishes, but the energy of the field $X$ still cannot be relaxed. For example consider a classical case of borromean flux tubes $\mathcal{T}^\text{Borr}$ with $X$ smooth and vanishing outside the tubes. Moreover assume that orbits of $X$ are just "parallel circles" inside each tube. By taking $X=X_1+X_2+X_3$, bilinearity of $\mathsf{H}_{12}(\,\cdot\,,\,\cdot\,)$ on $\text{Vect}^\text{vol}(S^3)$ and disjoint supports of $X_i$ yield $$\mathsf{H}_{12}(X)=\mathsf{H}_{12}(X,X)=\sum^3_{i=1}\mathsf{H}_{12}(X_i,X_i)+\sum_{i\neq j} \mathsf{H}_{12}(X_i,X_j)=0,$$ because "cross-helicities" $\mathsf{H}_{12}(X_i,X_j)$, $i\neq j$ vanish by Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"}, and self-helicities $\mathsf{H}_{12}(X_i,X_i)$ vanish as well because the average linking number of orbits is zero (orbits are just parallel circles). Nevertheless, Formula [\[eq:helicity-fluxes\]](#eq:helicity-fluxes){reference-type="eqref" reference="eq:helicity-fluxes"} tells us $$\mathsf{H}_{123}(X;\mathcal{T}^\text{Borr})\neq 0,$$ thus we may regard $\mathsf{H}_{123}(X;\mathcal{T})$ as a possible "higher obstruction" to the energy relaxation or the third order cross-helicity of $X$ on $\mathcal{T}$.

To obtain a lower bound for $E_2(X)$ in such situations we notice that $\mathsf{H}_{123}(X;\mathcal{T})$ is the $L^2$-inner product of the $6$-forms: $\ast(\omega\wedge\alpha_\omega)$ and $\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3$. Indeed from [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} we have $$\mathsf{H}_{123}(X;\mathcal{T})=\bigl(\ast(\alpha_\omega\wedge \omega),\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\bigr)_{L^2\Omega^6((S^3)^3)}\ .$$ Let $C_\mathcal{T}=\|\alpha_\omega\wedge \omega\|_{L^2}$, for a fixed Riemannian product metric on $(S^3)^3$ this constant depends on the domain $\mathcal{T}$ in $(S^3)^3$. We estimate using the Cauchy-Schwartz inequality $$\begin{aligned}
\notag |\mathsf{H}_{123}(X;\mathcal{T})| & \leq & \|\alpha_\omega\wedge \omega\|_{L^2}\|\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\|_{L^2}\\
\label{eq:energy-est1} & = & C_\mathcal{T}\Bigl(\int_{\mathcal{T}}(\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3)\wedge \ast(\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3)\Bigr)^\frac{1}{2}\\
\notag & \stackrel{(1)}{=} & C_\mathcal{T}\Bigl(\int_{\mathcal{T}}|X_1|^2|X_2|^2|X_3|^2\,\mu\Bigr)^\frac{1}{2}\\
\notag & \stackrel{(2)}{=} & C_\mathcal{T}\Bigl(\int_{\mathcal{T}_1}|X_1|^2\Bigr)^\frac{1}{2}\Bigl(\int_{\mathcal{T}_2}|X_2|^2\Bigr)^\frac{1}{2}\Bigl(\int_{\mathcal{T}_3}|X_3|^2\Bigr)^\frac{1}{2}\\
\label{eq:energy-est} & \leq &   C_\mathcal{T} E_2(X)^\frac{3}{2},
\end{aligned}$$ where $E_2(X)=\int_{S^3} |X|^2$. To observe (1) first note that for any pair of forms: $\alpha\in \Omega^k(M)$, and $\beta\in \Omega^j(N)$, on Riemannian manifolds $M$ and $N$, on the product $M\times N$ we have $$\label{eq:hodge-product}
  \ast_{M\times N}(\pi^\ast_M(\alpha)\wedge \pi^\ast_N(\beta))=(\ast_M \pi^\ast_M \alpha)\wedge (\ast_N \pi^\ast_N \beta),$$ where $\pi_M:M\times N\longrightarrow M$ and $\pi_N:M\times N\longrightarrow N$ are the natural projections, (the proof is a simple calculation in an orthogonal frame of the product and is left to the reader). Now, identity (1) follows by applying [\[eq:hodge-product\]](#eq:hodge-product){reference-type="eqref" reference="eq:hodge-product"} to the integrand in [\[eq:energy-est1\]](#eq:energy-est1){reference-type="eqref" reference="eq:energy-est1"}, and observing in the coframe $\{\eta^i_k\}$ on the $i$-th factor of $(S^3)^3$ ($X_i=(a_1,a_2,a_3)$): $$\begin{aligned}
 \iota_{X_i}\mu_i\wedge \ast \iota_{X_i}\mu_i & = & (a_1\eta^i_2\wedge\eta^i_3-a_2\eta^i_1\wedge\eta^i_3+a_3\eta^i_1\wedge\eta^i_2)\wedge (a_1\eta^i_1-a_2\eta^i_2+a_3\eta^i_3)\\
 & = & (a^2_1+a^2_2+a^2_3)\, \eta^i_1\wedge\eta^i_2\wedge\eta^i_3 = |X_i |^2 \eta^i_1\wedge\eta^i_2\wedge\eta^i_3=|X_i |^2 \mu_i\ .
\end{aligned}$$ The next identity (2) follows from the Fubini's Theorem.

Our next goal is to provide an estimate for $C_\mathcal{T}$. For this purpose we review some basic $L^2$-theory of the operator $d^{-1}$ (i.e. inverse of the exterior derivative $d$). The main goal is to estimate an $L^2$-norm of the potential $\alpha_\omega$ of $\omega$ in [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"}.

Following the standard elliptic theory of differential forms, [@Schwarz95], the potential $\alpha_\omega$ in [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"} can be obtained via a solution to the Neumann problem for $2$-forms on $\widetilde{\mathcal{T}}$ (see Appendix C) $$\label{eq:neumann-problem}
 \begin{cases}
  \Delta \phi_N=\omega,\qquad \text{in } \widetilde{\mathcal{T}}\\
  \mathbf{n}\,\phi_N=\mathbf{n}\,d\phi_N=0,\qquad \text{on } \partial \widetilde{\mathcal{T}},
 \end{cases}$$ where $\mathbf{n}$ stands for the normal component of a differential form, and $\Delta=d\delta+\delta d$. Because $\mathcal{T}$ is a domain with corners we replace it by a slightly larger domain $\widetilde{\mathcal{T}}$ in $(S^3)^3$ with the same topology (i.e. $\mathcal{T}$ is a deformation retract of $\widetilde{\mathcal{T}}$) but with smooth boundary $\partial\widetilde{\mathcal{T}}$. Notice that because of the "gauge invariance" $(i)$ of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, in the definition of $\mathsf{H}_{123}(X;\mathcal{T})$ we my use the restriction of $$\label{eq:potential-neumann}
\alpha_\omega=\delta\phi_N,$$ to $\mathcal{T}$ (see Appendix C for justification of [\[eq:potential-neumann\]](#eq:potential-neumann){reference-type="eqref" reference="eq:potential-neumann"}). Associated to [\[eq:neumann-problem\]](#eq:neumann-problem){reference-type="eqref" reference="eq:neumann-problem"} is the Neumann Laplacian $$\Delta_N:H^2\Omega^2_N(\widetilde{\mathcal{T}})\longrightarrow L^2\Omega^2(\widetilde{\mathcal{T}}),$$ which has a discrete positive spectrum $\{\lambda_{i,N}\}$ and eigenvalues satisfy the variational principle called *Rayleigh-Ritz quotient*, [@Chavel84]. The first (principal) eigenvalue $\lambda_{1,N}$ may be expressed as $$\lambda_{1,N}=\inf\left(   \frac{\|d\varphi\|^2_{L^2}+\|\delta\varphi\|^2_{L^2}}{\|\varphi\|^2_{L^2}}\ \Bigl|\ \varphi\in H^1\Omega^2_N(M)\cap \mathcal{H}^2_N(M)^\perp\right)$$ We denote the inverse of $\Delta_N$ by $$G_N:L^2\Omega^2(\widetilde{\mathcal{T}})\longrightarrow H^2\Omega^2_N(\widetilde{\mathcal{T}}),$$ which restricts to a compact, self-adjoint operator on $L^2$. As a result spectrum of $G_N$ is discrete and given as $\{1/\lambda_{i,N}\}$. Note that based on these considerations we may define $d^{-1}:=\delta G_N$.

::: theorem
For every volume preserving vector field $X$ which has an invariant unlinked domain $\mathcal{T}$, the $L^2$-energy of $X$ on $S^3$ is bounded below by the third order helicity $\mathsf{H}_{123}(X;\mathcal{T})$, as follows $$|\mathsf{H}_{123}(X;\mathcal{T})|\leq C_\mathcal{T} (E_2(X))^\frac{3}{2}.$$ Moreover, we may estimate the constant $C_\mathcal{T}$: $$\label{eq:C_T-estimate}
  C_\mathcal{T}\leq \frac{1}{\sqrt{\lambda_{1,N}}}\|\omega\|^2_{L^\infty\Omega^2(\widetilde{\mathcal{T}})}(\text{Vol}(S^3))^3,$$ where $\lambda_{1,N}$ is the first eigenvalue of the Neumann Laplacian on $\Omega^2(\widetilde{\mathcal{T}})$.
:::

::: proof
*Proof.* We estimate $$\begin{aligned}
 \|\alpha_\omega\|^2_{L^2} = \|\delta \phi_N\|^2_{L^2} & \leq & \|d\phi_N\|^2_{L^2}+\|\delta\phi_N\|^2_{L^2}\\
 & = & |(\Delta \phi_N,\phi_N)| \leq  \|\omega\|_{L^2}\|\phi_N\|_{L^2},
\end{aligned}$$ where we used the Green's formula [@Schwarz95 p. 60] and boundary conditions of [\[eq:neumann-problem\]](#eq:neumann-problem){reference-type="eqref" reference="eq:neumann-problem"} in the second identity. Now, because $\phi_N=G_N\omega$, and it is a well known fact that $\|G_N\|_{L^2}=\frac{1}{\lambda_{1,N}}$, ($G_N$ is compact self-adjoint on $L^2$) we obtain: $$\|\alpha_\omega\|_{L^2}\leq \frac{1}{\sqrt{\lambda_{1, N}}} \|\omega\|_{L^2}\ .$$ As a result we estimate $C_\mathcal{T}$: $$\begin{aligned}
 C_\mathcal{T}=\|\alpha_\omega\wedge\omega\|_{L^2} & \leq & \|\omega\|_{L^\infty}\|\alpha_\omega\|_{L^2}\\
 & \leq &  \frac{1}{\sqrt{\lambda_{1, N}}} \|\omega\|_{L^2}\|\omega\|_{L^\infty}.
\end{aligned}$$ ◻
:::

Notably the best energy estimate has been obtained by Freedman and He, [@Freedman91-2], for the $L^{3/2}$-energy of $X$, in the case when $X$ admits an invariant domain $\mathcal{T}$ modeled on an $n$-component link $L=\{L_1,\ldots,L_n\}$ in $\mbox{\bbb R}^3$. Their estimate is based on the asymptotic crossing number and reads $$\label{eq:energy-free-he}
 E_{3/2}(X)\geq \Bigl(\frac{\pi}{16}\Bigr)^{1/4}\left(\sum^n_{k=1} \text{ac}(L_k,L)|\text{Flux}(X_k)|\right)\cdot \min_{1\leq k\leq n}\{|\text{Flux}(X_k)|\},$$ where the asymptotic crossing numbers $\text{ac}(L_k,L)$ for borromean links can be estimated below by a smallest genus among surfaces in $\mbox{\bbb R}^3\setminus \{L_1\cup\ldots\cup\hat{L}_k\cup\ldots\cup L_n\}$ with a single boundary component $L_i$. Since $L^{3/2}$-energy of $X$ bounds the $L^2$-energy, via the H$\ddot{\rm o}$lder Inequality, thus [\[eq:energy-free-he\]](#eq:energy-free-he){reference-type="eqref" reference="eq:energy-free-he"} leads to a lower estimate purely in terms of fluxes and topological data. It is not clear to the author if this approach can be extended to the case of invariant handlebodies considered in Section [\[sec:handlebody\]](#sec:handlebody){reference-type="ref" reference="sec:handlebody"}. A different, more optimal estimate, has been obtained by Laurence and Stredulinsky, via the Massey product formula, in [@Laurence-Stredulinsky00a], but the proof is provided only in a special case of the vector field $X$.

Contrary to these lower bounds which are given in terms of topological data the estimate in [\[eq:C_T-estimate\]](#eq:C_T-estimate){reference-type="eqref" reference="eq:C_T-estimate"} depends on the geometry of the domain $\mathcal{T}$, and also $\|\omega\|_{L^\infty}$. Unfortunately, $\omega$ blows up on the diagonals $\mathbf{\Delta}\subset (S^3)^3$, and as a result the estimate is meaningless when the handlebodies $\mathcal{T}_i$ get close to each other during the evolution of the magnetic field $X$. At this point, we need an assumption for $\mathcal{T}_i$ to stay *1cm* apart during the evolution. Another drawback is that $\lambda_{1,N}$ is a geometric constant which is altered during the evolution as well.
