---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-015-43-fourier-transform-on-tk
section_title: "Fourier transform on Tk"
section_number: 4.3
pages: 28-30
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.918
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#Sec:Fourier_continuous label="Sec:Fourier_continuous"} Let us turn to $T_{k}$, the continuous limit object of the sequence $\{B_{k,n}, n\geq k\}$. Recall that the set of continuous $k$-configurations on a circle $T_{k}$ is the subset of $\mathbb{R}^k$ consisting of vectors $u=(u_1,\ldots,u_k)$ such that $$0\leq u_k\leq u_{k-1}\leq \dots\leq u_1<2\pi.$$ Before describing the relation with $B_{k,n}$, let us describe the Fourier transform on $T_{k}$ coming from representations theory of $U(k)$, the Lie group of unitary matrices of rank $k$. Sending $U\in U(k)$ to the sequence of arguments of its eigenvalues taken in $[0,2\pi[)$ and sorted in decreasing order yields a map $p:U(k)\mapsto  T_{k}$. Characters of $U(k)$ are conjugation invariant functions $\{\chi_I, I\in B_{k}\}$ with the formula $$\label{eq:character_Uk}
\chi_I(U)=S_{I}(p(U))=\frac{a_{I}(u_1,\ldots,u_k)}{a_{I_0}(u_1,\ldots,u_k)},$$ where $\{u_1,\ldots,u_k\}$ are arguments of eigenvalues of $U\in U(k)$ and we recall that $a_{I}(u_1,\ldots,u_k)=\det(e^{iu_lI_m})_{1\leq l,m\leq k}$ for $u\in\mathbb{R}^k$ and $I\in B_{k}$, where we recall that $B_k$ is the set of increasing sequences of integers.

By Weyl integration formula, the image of the Haar measure $\mu_H$ on $U(k)$ through the map $p$ sending a unitary matrix to the decreasing sequence of arguments of its eigenvalues yields a probability measure on $T_{k}$ which is continuous with respect to the Lebesgue measure and has density $$dp_{\star}\mu_H(u_1,\ldots,u_n)=\frac{1}{(2\pi)^k}\prod_{l<m}\left\vert e^{iu_l}-e^{iu_m}\right\vert^2=\frac{1}{(2\pi)^k}\vert V(\vec{u})\vert^2.$$ Reciprocally, any probability measure on $T_{k}$ yields a unique probability measure $p^{\star}\mu$ on $U(k)$ which is invariant by conjugation. Denote by $L^2_{inv}(U(k))$ the vector space of square integrable functions on $U(k)$ which are invariant by conjugation. Each element $f$ of $L^2_{inv}(U(k))$ yields a function $\tilde{f}$ on $L^2( T_{k},dp_{\star}\mu_H)$ by restricting its values to diagonal matrices, and the map $f\mapsto \tilde{f}$ is an isomorphism by Weyl integration formula. By Plancherel theorem, the map $$\Phi:\left\lbrace\begin{aligned} L^2_{inv}(U(k),d\mu_H)&\simeq &L^2( T_{k},dp_{\star}(\mu_H)) &\rightarrow &&\ell^2(B_{k})\\
&f&&\mapsto&&\left(\int_{ T_{k}}S_{J}(u)\tilde{f}(u)dp_{\star}\mu_H(u)\right)_{J\in B_{k}}\end{aligned}\right.$$ is an $L^2$-isometry. For $c=(c(J))\in \ell^2(B_{k})$, the inverse of $\Phi$ at $c$ is given by $$\Phi^{-1}[c](\vec{u})=\sum_{J\in B_{k}}d_{J}c(J)S_J(\vec{u})$$ for $\vec{u}\in  T_{k}$, where the sum almost-surely converges and $d_J=S_J(0,\ldots,0)$ is the dimension of the irreducible representation of $U(k)$ having character $\chi_J=S_J\circ p$.

The map $\Phi$ extends by continuity (in the weak-topology) to a unique map, also denoted $\Phi$ and called the *Fourier transform* on $T_k$, from the set $\mathcal{M}_{f}( T_{k})$ of finite measures on $T_{k}$ to the topological space of maps from $B_{k}$ to $\mathbb{C}$ with the pointwise convergence. We then have for $m\in \mathcal{M}_{f}( T_{k})$ and $J\in B_{k}$ $$\label{eq:fourier_transform_measure_Uk}
\Phi[m](J)=\frac{1}{(2\pi)^k}\int_{ T_{k}}S_{J}(\vec{u})\vert V(\vec{u})\vert^2dm(\vec{u}).$$ As for finite measures on $\mathbb{R}$ or $\mathbb{R}/(2\pi\mathbb{Z})$, the Fourier transform characterizes finite measures and vague convergence on $T_k$. Denote by $\mathcal{M}_{1}( T_{k})$ the subset of $\mathcal{M}_{f}( T_{k})$ consisting in measures $m$ on $T_k$ such that $\Phi[m](I_0)=1$.

If $\nu_1,\nu_2\in \mathcal{M}_{f}(U(k))$, the set of finite measures on $U(k)$, the convolution of $\nu_1$ with $\nu_2$ is the unique finite measure $\nu_1\ast\nu_2$ such that $\int_{U(k)}fd\nu_1\ast\nu_2=\int_{U(k)\times U(k)}f(g_1g_2)d\nu_1(g_1)d\nu_2(g_2)$ for all $f\in C^0(U(k))$. If $\mu_1,\mu_2\in \mathcal{M}_f( T_{k})$, we define $$\nu_1\ast\nu_2=p_{\star}(p^{\star}(\mu_1)\ast p^{\star}(\mu_2)).$$ Then, the convolution product $\ast$ is commutative on $\mathcal{M}_f( T_{k})$, and $$\Phi[\mu_1\ast\mu_2]=\Phi[\mu_1]\cdot \Phi[\mu_2],$$ where the product on the right-hand side is the pointwise product on $M(B_{k})$.

Recall that $B_{k,n}$ embeds in $T_{k}$ through the map $\xi_{n}$ defined in Section [\[subsec:intro_model\]](#subsec:intro_model){reference-type="ref" reference="subsec:intro_model"}. By linearity, this map is extended to a map (also denoted by $\xi_{n}$) from $L^2(B_{k,n})$ to $\mathcal{M}_f( T_{k})$ with the formula $$\xi_{n}\left(\sum_{I\in B_{k,n}}\mu(I)e_I\right)=\left(\frac{2\pi}{n}\right)^k\sum_{I\in B_{k,n}}\mu(I)\delta_{\xi_n(I)}, \quad \mu\in L^2(B_{k,n}).$$ A crucial fact for the sequel is that $\xi_{n}$ intertwines the Fourier transforms $\Phi_n$ and $\Phi$.

::: proposition
[]{#prop:equiv_dft_cft label="prop:equiv_dft_cft"} For all $\mu\in L^2(B_{k,n})$ and $J\in B_{k}$ such that $J_1< J_k+n$. Then, with $J^{(n)}\in B_{k,n}$ such that $\{J^{(n)}_i[n]\}_{1\leq i\leq k}=\{J_i[n]\}_{1\leq i\leq k}$, $$\Phi[\xi_{n}(\mu)] (J)=S_{J}(\xi_{n}(I_0))\Phi_n[\mu](J^{(n)}).$$
:::

::: proof
*Proof.* By linearity, we only have to prove the relation on $\mu=\delta_I$ for $I\in B_{k,n}$, where $\delta_I$ is defined in [\[eq:definition_dirac\]](#eq:definition_dirac){reference-type="eqref" reference="eq:definition_dirac"}. First, [\[eq:Fourier_probability\]](#eq:Fourier_probability){reference-type="eqref" reference="eq:Fourier_probability"} and Lemma [\[lem:formula_inversion_Schur\]](#lem:formula_inversion_Schur){reference-type="ref" reference="lem:formula_inversion_Schur"} yield $$\Phi_n[\delta_I](J^{(n)})=\frac{S_{I}(\xi_{n}(J^{(n)}))}{S_I(\xi_{n}(I_0))}=\frac{S_{J^{(n)}}(\xi_{n}(I))}{S_{J^{(n)}}(\xi_{n}(I_0))}.$$ On the other hand, since $\xi_n(\delta_I)=\left(\frac{2\pi}{n}\right)^k\frac{n^k}{\vert V(\xi_n(I))\vert^2}\delta{\xi_n(I)}=\frac{(2\pi)^k}{\vert V(\xi_n(I))\vert^2}\delta{\xi_n(I)}$, $$\begin{aligned}
\Phi[\xi_{n}(\delta_I)](J)=&\frac{1}{(2\pi)^k}\int_{ T_{k}}S_{J}(\vec{u})\vert V(\vec{u})\vert^2\frac{(2\pi)^kd\delta{\xi_n(I)}}{\vert V(\xi_n(I))\vert^2}(\vec{u})\\
=&S_{J}(\xi_{n}(I))=S_{J^{(n)}}(\xi_{n}(I)),
\end{aligned}$$ The last equality is a consequence to the fact that $J^{(n)}$ has the form $(J_r+(\ell+1)n,\ldots,J_k+(\ell+1)n, J_1+\ell n,\ldots, J_{r-1}+\ell n)$ for some $1\leq r\leq k$ and $\ell\in\mathbb{Z}$ and because of the determinantal formula of $S_J$ and $S_{J'}$. The result is then deduced. ◻
:::
