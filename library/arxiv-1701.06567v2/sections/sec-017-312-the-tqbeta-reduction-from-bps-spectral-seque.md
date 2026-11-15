---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-017-312-the-tqbeta-reduction-from-bps-spectral-seque
section_title: "The $t=q^{\beta}$ reduction from BPS spectral sequence"
section_number: 3.1.2
pages: 30-32
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.991
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:Spec label="sec:Spec"}

One interesting property of the invariants [\[Index-UN-free\]](#Index-UN-free){reference-type="eqref" reference="Index-UN-free"} and [\[CI\]](#CI){reference-type="eqref" reference="CI"} is their behavior under the specialization $t=q^{\beta}$ with $\beta\in {\mathbb Z}$. First, they all become polynomial after taking this limit. For example, $${\mathcal I}_{r,f=1} (q,t) \quad \overset{t=q^\beta}{\longrightarrow}\quad \prod_{j=0}^{\infty} \frac{1 - q^{1-r/2-\beta+j}}{1- q^{r/2+\beta+j}}=(q^{1-r/2-\beta};q)_{r+2\beta-1},$$ is simply a polynomial (as opposed to a power series). Second, they exhibit "positivity" in the sense that if one adds a minus sign setting $t=-q^{\beta}$, one finds a polynomial with only positive coefficients: $${\mathcal I}_{r,f=1}(q,t=-q^\beta)=\prod_{j=0}^{r+2\beta-2} \left(1+q^{1-r/2-\beta+j}\right).$$ Here, these phenomena originate from the fact that, upon setting $t=q^\beta$, there is a lot of cancellation between contributions from bosonic and fermionic generators, with only $\overline{\psi}_+$,$\partial \overline{\psi}_+$,..., $\partial_+^{2\beta}\overline{\psi}_+$ remaining. However, as we will see in later part of this paper, these phenomena are actually very universal and also appear in a wide variety of 3d ${\mathcal N}=2$ theories $T[M_3]$ with the symmetry $U(1)_{\beta}$. Therefore, it is interesting to understand the $t=q^\beta$ reduction at the categorified level.

The natural uplift of the reduction of superconformal indices $${\mathcal I}_{T[M_3]}(q,t) \quad \leadsto \quad {\mathcal I}_{T[M_3]}^{(\beta)}(q)={\mathcal I}(q,q^\beta)$$ is a BPS spectral sequence [@Gukov:2015gmm]: $$\label{BPSSpec}
{\mathcal H}_{Q}^{\text{BPS}} \quad \leadsto \quad {\mathcal H}_{Q+Q'}^{\text{BPS}},$$ which starts with the space of BPS states of $T[M_3]$ on $S^2$ and converges to the space of $Q+Q'$-cohomology with a deformed supercharge. For concreteness, we will focus on the example of a single chiral $\Phi=(\phi,\psi)$ with R-charge $r=2$, which can be understood as the theory $T[S^3, U(1)]$. The first step is to explicitly identify the space of BPS states ${\mathcal H}_{S^2}$ found in the previous section as the $Q$-cohomology for a supercharge in the following way.

All four supercharges of a 3d ${\mathcal N}=2$ theory can be preserved on $S^2\times {\mathbb R}$. We pick a supercharge $Q=\overline{Q}_-$ parametrized by a Killing spinor $\overline{\zeta}_+$ with $$j_3(\overline{\zeta}_+)=\frac{1}{2},\quad R(\overline{\zeta}_+)=-1.$$ The supergravity background is given by $$V_\mu=A_\mu^{(R)}=-i\delta_{\mu 3},$$ with the other components of the background multiplet set to zero.[^1] Then, the on-shell SUSY variation given by $\overline{Q}_-$ is $$\begin{aligned}\label{QTrans}
\delta\phi&=0\\
\delta\overline{\psi}&=0\\
\delta\overline{\phi}&=\sqrt{2} \overline{\zeta}_+\overline{\psi}_-,\\
\delta\psi&=-\sqrt{2} i\gamma^\mu \overline{\zeta}_+ D_\mu \phi+\sqrt{2} i \sigma \phi \overline{\zeta}_+,
\end{aligned}$$ where we have included a background $U(1)_{\beta}$ vector multiplet $(A_\mu,\lambda,\overline{\lambda},\sigma,D)$, and $D_\mu$ is a covariant derivative that involves the Levi-Civita connection, $A_\mu$ and $A_\mu^{(R)}$. Then the $Q$-closed states are $\phi$, $\overline{\psi}_\pm$ and their derivatives. Among them $\overline{\psi}_-$, $D_3\phi$ and $\partial_-\phi$ are $Q$-exact, while $D_3\overline{\psi}_+$ and $\partial_-\overline{\psi}_+$ are eliminated by the equation of motion. So we have found that the space of BPS states is exactly the cohomology of $Q=\overline{Q}_-$.

One might expect a spectral sequence to arise when $Q$ is deformed into $Q+Q'$, whose second page is given by $$E_2^{\bullet,\bullet}=H^{\bullet}({\mathcal H}^{\bullet}_Q,Q').$$ The simplest scenario is to have only non-trivial differentials on the second page, enabling us to read off ${\mathcal H}^{\bullet}_{Q+Q'}$ from the third page, like most examples studied in [@Gukov:2015gmm].

When we take $t=q^\beta$, we are effectively shifting the $U(1)_R$ charge by $2\beta$ multiple of the $U(1)_{\beta}$ charge. As a result, the operators $\phi$ and $\partial_+^{2\beta+1}\overline{\psi}_+$ have the same $R/2+j_3$ quantum number and their contribution to the index cancels. Then, naively, we expect to have the following action of $Q'$ on $\phi$: $$\sim\partial_+^{2\beta+1}\overline{\psi}_+.$$ However, no supercharges can achieve this, even if we turn on more general supergravity backgrounds, as $\phi$ and $\overline{\psi}$ live in different representations of the supersymmetry algebra and don't mix.

Another possibility is to have $\phi$ and $\partial_+^{2\beta+1}\overline{\psi}_+$ to be eliminated separately. This can be achieved by turning on $-2\beta+1$ units of $U(1)_{\beta}$ flux along $S^2={\mathbb{C}}{\mathbf{P}}^1$.[^2] Now $\phi$ and $\overline{\psi}_+$ are holomorphic sections of $$\phi\in H^0({\mathbb{C}}{\mathbf{P}}^1,O(-2\beta+1)),\quad \overline{\psi}_+\in H^0({\mathbb{C}}{\mathbf{P}}^1,O(2\beta)).$$ The former has no sections, while the latter has $2\beta+1$ sections given by $\overline{\psi}_+$, $\partial_+\overline{\psi}_+,\ldots, \partial_+^{2\beta}\overline{\psi}_+$.

At the level of SUSY transformations, we now have a term in $\delta \psi$ of the following form $$(\delta \psi)_- \sim \gamma^-\overline{\zeta}_+ D_-\phi,$$ making all modes of $\phi$ exact under $Q+Q'$. On the other hand, the equation of motion for $\overline{\psi}_+$ will impose $$D_-\overline{\psi}_+=0,$$ but there are solutions to this equation, because $\overline{\psi}$ have negative charge under $U(1)_{\beta}$. It would be interesting to pursue this analysis further in non-trivial examples and also make contact with [@Beem:2013sza] and [@Dedushenko:2016jxl], where similar phenomena were studied in theories with larger supersymmetry.

## ${M_3=L(p,1)}$ {#sec:Lp1}

[^1]: We have chosen the round metric and the veilbein $$e_1=d\theta,\quad e_2=\sin \theta d\varphi, \quad e_3=dx_3.$$

[^2]: In order for the background to be supersymmetric, one also needs to turn on a constant $\sigma$ for the background gauge multiplet, which won't affect the analysis in this section.
