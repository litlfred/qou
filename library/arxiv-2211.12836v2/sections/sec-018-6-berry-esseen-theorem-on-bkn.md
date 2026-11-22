---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-018-6-berry-esseen-theorem-on-bkn
section_title: "Berry-Esseen theorem on Bk,n"
section_number: 6
pages: 46-47
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.97
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#sec:Berry-Esseen label="sec:Berry-Esseen"}

We state and prove in this section the first main result of the manuscript, which consists in a Berry-Esseen type theorem for the measure $\xi_n(*\mathbf{m})$. The complete result is a bit more general than the simplified version written in Theorem [\[thm:Berry-Esseen_simplified\]](#thm:Berry-Esseen_simplified){reference-type="ref" reference="thm:Berry-Esseen_simplified"}, in order to give a more precise constant.

Recall that the shift action of $\mathbb{R}$ on $T_k$ is given for $\vec{u}\in [0,2\pi[^k$ and $t\in \mathbb{R}$ by $$R_t( \vec{u})=Sort(\overline{u_1-t},\ldots,\overline{u_k-t}),$$ where $Sort(\vec{v})$ is the sequence obtained from $\vec{v}\in [0,2\pi[^k$ by sorting it in increasing order, and $R_t( \mu)$ for the image of the measure $\mu\in \mathcal{M}_1( T_{k})$ by the map $\vec{u}\mapsto R_t(\vec{u})$. We then have, for $J\in B_{k}$, $$\begin{aligned}
\Phi[R_t(\mu)](J)=\int_{ T_{k}}S_{J}(\vec{u})\vert V(\vec{u})\vert^2dR_t\mu(\vec{u})=&\int_{ T_{k}}S_{J}(\vec{u}+t\mathbf{1}_{k})\vert V(\vec{u}+t\mathbf{1}_{k})\vert^2d\mu(\vec{u})\nonumber\\
=&\exp(i\langle \lambda_J\rangle t)\int_{ T_{k}}S_{J}(\vec{u})\vert V(\vec{u})\vert^2d\mu(\vec{u})\nonumber\\
=&\exp(i\langle \lambda_J\rangle t)\Phi[\mu](J).\label{eq:effect_rotation_Fourier}
\end{aligned}$$ Comparing Proposition [\[prop:convergence_fourier\]](#prop:convergence_fourier){reference-type="ref" reference="prop:convergence_fourier"} with [\[eq:Fourier_Dyson_Brownian_motion\]](#eq:Fourier_Dyson_Brownian_motion){reference-type="eqref" reference="eq:Fourier_Dyson_Brownian_motion"} suggests a convergence of the distribution of $\xi_n(*\mathbf{m})$, viewed as a probability distribution on $T_{k}$, to the marginal distribution of a unitary Brownian motion $B^{\alpha,\gamma}$ at time $m/n^2$ with adequate parameters $\alpha,\gamma$. We will quantify this convergence in terms of the $1$-Wassertein metric on the space of probability measures on $T_{k}$. Due to the circular nature of $T_{k}$, define the metric $$d_{ T_{k}}(z,z')=\sqrt{\inf_{\sigma\in S_k}\sum_{i=1}^kd_{\mathbb{R}}(z_{i}-z_{\sigma(i)}',2\pi\mathbb{Z})^2}$$ on $T_{k}$. This is indeed a metric, since $d_{ T_{k}}(z,z')=W_2(\delta_{z},\delta_{z'})$, where the Wasserstein distance $W_2$ is taken on the metric space $\mathbb{R}/\mathbb{Z}$ with the natural distance and $\delta_{z}=\sum_{i=1}^k\delta_{z_i}$. Remark that when $z,z'\in ]0,1/2[^k$, one has $d_{ T_{k}}(z,z')=\Vert z-z'\Vert_2$.

We then define the 1-Wasserstein distance $W_{1}^{T_{k}}$ on $T_{k}$ with respect to the metric $d_{ T_{k}}$ as $$W_{1}^{T_{k}}(\mu,\nu)=\sup\left(\left\vert \int_{ T_{k}}f d\mu -\int_{ T_{k}}f d\nu\right\vert, \, f: ( T_{k},d_{ T_{k}})\rightarrow(\mathbb{R},d_{\mathbb{R}}) \,\text{ $1-$Lipschitz}\right),$$ for $\mu,\nu\in  \mathcal{M}_1(T_{k})$.

::: theorem
[]{#thm:Berry-Esseen label="thm:Berry-Esseen"} Let $M>0$ and suppose that $\mathbf{m}=(\mu_r)_{1\leq r\leq m}$ is a sequence of $h$-probability measures on $B_{k,n}$ such that $Var_{3}(\mathbf{m})\leq M Var\langle\mathbf{m}\rangle^{3/2}$ and $\langle\hat{\mathbf{m}}\rangle_3\leq MK(\mathbf{m})^{3/2}$, and set $t_0=\frac{(2\pi)^2m}{n^2}$. Then, there are numeric constants $c_1,c_2>0$ such that for all $I\in  B_{k,n}$, setting $\mu=R_{\frac{m\langle\mathbf{m}\rangle}{kn}}\left(\xi_{n}\left[(\ast \mathbf{m})*\delta_I\right]\right)$ and $\nu=B^{\alpha,\gamma}_{\xi_n(I)}\left(t_0\right)$ (viewed as a distribution on $T_k$), $$W_1^{T_k}\left(\mu, \nu\right)\leq \frac{M}{n}\left(c_1(k^8\gamma+k\alpha)\log n+\frac{c_2k^{9/2}}{\sqrt{t_0}}K_{\gamma t_0/2}^{SU(k)}\left(\xi_n(I),\xi_n(I)\right)^{1/2}\right),$$ for some numeric constants $c_1,c_2>0$, with $$\alpha=\frac{1}{2}Var(\mathbf{m}), \, \gamma=\frac{k}{2(k^2-1)}K(\mathbf{m}).$$
:::

Theorem [\[thm:Berry-Esseen_simplified\]](#thm:Berry-Esseen_simplified){reference-type="ref" reference="thm:Berry-Esseen_simplified"} given in Section [\[sec:intro_model\]](#sec:intro_model){reference-type="ref" reference="sec:intro_model"} is then a simplified version of the latter result, using Lemma [\[lem:bound_K_norm_inf\]](#lem:bound_K_norm_inf){reference-type="ref" reference="lem:bound_K_norm_inf"} to bound $\langle \hat{\mathbf{m}}\rangle_3$ by $2\sqrt{2}k^3\Vert \tilde{\mathbf{m}}\Vert_3$. The main ingredients in the proof of Theorem [\[thm:Berry-Esseen\]](#thm:Berry-Esseen){reference-type="ref" reference="thm:Berry-Esseen"} is Proposition [\[prop:convergence_fourier\]](#prop:convergence_fourier){reference-type="ref" reference="prop:convergence_fourier"} together the adaption of an approach of [@BobLed] relating the Wassertein distance to the Fourier transform.
