---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S 3"
section_id: sec-004-the-ergodic-interpretation-of-h123xt
section_title: "The ergodic interpretation of H123(X;T)"
section_number: null
pages: 18-23
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.994
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
[]{#sec:ergodic label="sec:ergodic"}

The following statement is often seen in literature [@Cantarella-DeTurck-Gluck01; @Cantarella-DeTurck-Gluck-Teytel00]:

> *Helicity measures the extend to which vector fields twist and coil around each other.*

A beauty of Arnold's ergodic approach to the helicity $\mathsf{H}_{12}(X)$ is that it makes this statement precise, by interpreting $\mathsf{H}_{12}(X)$ as an average asymptotic linking number of orbits of $X$. But it also has a practical application as it allows us to extend our approach to certain invariant sets of $X$. In this section we apply this philosophy to our newly defined invariant $\mathsf{H}_{123}(X;\mathcal{T})$, and interpret it as the average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $X$. Moreover this ergodic interpretation leads us to an alternative, more intuitive proof of Helicity Invariance Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}.

We begin by observing that given a volume preserving vector field $X$ on $M$ and its flow $\Phi_t$, we may regard $X$ as three vector fields on $(M)^3$. Therefore $(\Phi,\Phi,\Phi)$ induces a natural $\mbox{\bbb R}^3$ action defined as $$\label{eq:R3-action}
 \mathbf{\Phi}:\mbox{\bbb R}^3\times (M)^3\longrightarrow (M)^3:\qquad \bigl((s,t,u),x,y,z\bigr)\stackrel{\mathbf{\Phi}}{\longrightarrow} (\Phi(s,x),\Phi(t,y), \Phi(u,z)).$$ Observe that $\mathbf{\Phi}$ is a volume preserving action on $(M)^3$. Our analysis is rooted in techniques developed in [@Arnold86; @Laurence-Avellaneda93; @Laurence-Stredulinsky00b], the main tool is the the following

::: theorem
[]{#th:multi-ergodic label="th:multi-ergodic"} For any real valued $L^1$-function $F$ on $(M)^3$, the time averages under the action in [\[eq:R3-action\]](#eq:R3-action){reference-type="eqref" reference="eq:R3-action"}: $$\begin{gathered}
\bar{F}(x,y,z)=\lim_{T\to \infty}\frac{1}{T^3}\int^T_0\int^T_0\int^T_0
 F(\Phi(x,s),\Phi(y,t),\Phi(z,u))\,d s\,d t\,d u
\end{gathered}$$ converge almost everywhere. Moreover, the limit function $\bar{F}$ satisfies

-   $\|\bar{F}\|_{L^1((M)^3)}\leq \|F\|_{L^1((M)^3)}$,

-   $\bar{F}$ is invariant under the $\mathbf{\Phi}$-action,

-   if $(M)^3$ is of finite volume then $$\begin{gathered}
    \label{eq:ergodic-integrals-equal}
     \int_{(M)^3}\bar{F} =\int_{(M)^3} F\ .
    \end{gathered}$$
:::

We may now define *invariant unlinked domain* $\mathcal{T}$ of $X$ as an arbitrary $\mathbf{\Phi}$-invariant set, with topological closure $\overline{\mathcal{T}}$ which belongs to a larger product of open sets $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ in $\text{Conf}(S^3,3)$, satisfying the following

-   $\widetilde{\mathcal{T}}$ admits a *short path system* $\mathcal{S}$,

-   Equation [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"} holds on $\widetilde{\mathcal{T}}$.

By a system of short paths on $\widetilde{\mathcal{T}}$, [@Vogel03; @Khesin98], we understand a collection of curves $\mathcal{S}=\{\sigma(x,y)\}$ on each open set $\widetilde{\mathcal{T}}_i$ such that

-   for every pair of points $x,y \in \widetilde{\mathcal{T}}_i$ there is a curve $\sigma(x,y):I\mapsto \widetilde{\mathcal{T}}_i$ in $\mathcal{S}$, such that $\sigma(0)=x$ and $\sigma(1)=y$,

-   the lengths of paths in $\mathcal{S}$ are uniformly bounded above by a common constant.

Topologically, every $\mathbf{\Phi}$-invariant set is a union of products of orbits of $X$ in $(S^3)^3$, it is often convenient to think of the orbits $\mathbf{\Phi}$-action as a foliation of $(S^3)^3$, then $\mathbf{\Phi}$-invariant sets are just union of leaves of such foliation. A fundamental example of an invariant unlinked domain is the case of $\mathbf{\Phi}$-invariant set $\mathcal{T}$ contained in the product $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ of disjoint open unlinked handlebodies $\widetilde{\mathcal{T}}_i$. Notice that we do not require $X$ to be tangent to $\partial\widetilde{\mathcal{T}}_i$ in this case, and $\widetilde{\mathcal{T}}$ always admits a short path system as we describe in the following

::: remark
In [@Vogel03], Vogel shows that on a closed manifold $M$, geodesics always provide a short path system. When $\mathcal{T}$ is contained in the product of unlinked handlebodies $\widetilde{\mathcal{T}}$ we may easily construct such system on $\widetilde{\mathcal{T}}$. Because $\mathcal{\mathcal{T}}_i$ are proper subsets of $S^3$ we generally do not want to use ambient geodesics from $S^3$ as they may not lie entirely in $\mathcal{T}_i$. To obtain $\mathcal{S}$ one may always put an artificial Riemannian metric on each $\widetilde{\mathcal{T}}_i$ which makes it a complete Riemannian manifold (e.g. by making $\partial\widetilde{\mathcal{T}}_i$ totally geodesic) and choose $\mathcal{S}$ to be geodesics on such Riemannian manifold. We also observe that one may apply a diffeomorphism $g\in \text{Diff}(\widetilde{\mathcal{T}})$ to $\mathcal{S}$ which results in the new system $g\mathcal{S}$ on $g(\widetilde{\mathcal{T}})$.
:::

Next theorem shows that the definition of $\mathsf{H}_{123}(X;\mathcal{T})$ in Equation [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"} is valid for invariant unlinked domains of $X$ and is an analog of Arnold's Helicity Theorem in our setting

::: theorem
[]{#th:ergodic-mu label="th:ergodic-mu"} Given $(X;\mathcal{T})$, the following limit (asymptotic $\bar{\mu}_{123}$-invariant of orbits) exists for almost all $(x,y,z)\in \mathcal{T}$: $$\label{eq:bar-m_X}
 \bar{m}_X(x,y,z)=\lim_{T\to\infty} \frac{1}{T^3}\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{X_1}_T(x),\bar{\mathscr{O}}^{X_2}_T(y),\bar{\mathscr{O}}^{X_3}_T(y)\bigr).$$ Moreover, $$\label{eq:H_123-ergodic}
 \mathsf{H}_{123}(X;\mathcal{T})=\int_{\mathcal{T}} \bar{m}_X(x,y,z)\,\mu(x)\wedge\mu(y)\wedge\mu(z)\ .$$
:::

::: proof
*Proof.* The proof is similar to the one in e.g. [@Vogel03]. Before we start we must point out the following identity (valid for any 3-form $\gamma$ on $M\times M\times M$ and vector fields $X_1,X_2,X_3$ on $M$) $$(\iota_{X_1}\iota_{X_2}\iota_{X_3}\gamma)\wedge\mu\wedge\mu\wedge\mu=
\gamma(X_1,X_2,X_3)\,\mu\wedge\mu\wedge\mu=\gamma\wedge\iota_{X_1}\mu\wedge\iota_{X_2}\mu\wedge\iota_{X_3}\mu\ .$$ The first equation follows from the definition, the second equation is a consequence of the fact that $\iota_X$ is an antiderivation i.e. $$\label{eq:iota-antiderivation}
  \iota_X(\alpha\wedge\beta)=(\iota_X\alpha)\wedge\beta+(-1)^{|\alpha|}\alpha\wedge(\iota_X\beta),$$ and $\iota_{X_i}\mu_j\equiv 0$ for $i\neq j$. As a result $$\begin{aligned}
\notag  \mathsf{H}_{123}(X_1,X_2,X_3) & = & \int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\\
& = & \int_\mathcal{T} \bigl(\iota_{X_1}\iota_{X_2}\iota_{X_3}\bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\bigr)\,\mu_1\wedge\mu_2\wedge\mu_3\\
\label{eq:m-function}  & = & \int_\mathcal{T} m_{X_1,X_2,X_3}(x,y,z)\,\mu_1\wedge \mu_2\wedge \mu_3,
\end{aligned}$$ where $m_{X_1,X_2,X_3}:=\alpha_\omega\wedge d\alpha_\omega(X_1,X_2,X_3)$. For convenience let (see [\[eq:orbits\]](#eq:orbits){reference-type="eqref" reference="eq:orbits"}) $$\bar{\mathscr{O}}(x,y,z;T):=\bar{\mathscr{O}}^{X_1}_T(x)\times \bar{\mathscr{O}}^{X_2}_T(y)\times\bar{\mathscr{O}}^{X_3}_T(y)\ .$$ Clearly, every link $\bar{\mathscr{O}}(x,y,z;T)$ is borromean and by Formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} we obtain $$\begin{aligned}
\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{X_1}_T(x),\bar{\mathscr{O}}^{X_2}_T(y),\bar{\mathscr{O}}^{X_3}_T(y)\big)
& = & \int_{\bar{\mathscr{O}}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega\\
& = & \int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega+(I)
\end{aligned}$$ where the term $(I)$ involves integrals over short paths in $\mathcal{S}$, (see Appendix B). Next, notice that for every $(x,y,z)$ : $D\mathbf{\Phi}_{(x,y,z)}[\partial_i]=X_i$, $i=s,t,u$ we obtain $$\begin{aligned}
 \mathbf{\Phi}^\ast_{(x,y,z)}(\alpha_\omega\wedge d\alpha_\omega) & = & (\alpha_\omega\wedge d\alpha_\omega(X_1,X_2,X_3)(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\\
 & = & m_{X_1,X_2,X_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .
\end{aligned}$$ Thus $$\int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega=\int^T_0\int^T_0\int^T_0 m_{X_1,X_2,X_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .$$ Function $m_{X_1,X_2,X_3}$ is smooth on $\mathcal{T}$ and therefore $L^1$. Because short paths do not contribute to the time average i.e. $$\lim_{T\to\infty} \frac{1}{T^3}(I)=0$$ (see Appendix B), Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} applied to the function $m_{X_1,X_2,X_3}$ yields almost everywhere existence of the limit [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} and the invariant $L^1$-function $\bar{m}_X:=\bar{m}_{X_1,X_2,X_3}$ on $\mathcal{T}$. The identity [\[eq:H_123-ergodic\]](#eq:H_123-ergodic){reference-type="eqref" reference="eq:H_123-ergodic"} follows from $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. ◻
:::

::: theorem
[]{#th:invariance-th-ergodic label="th:invariance-th-ergodic"} On every unlinked domain $\mathcal{T}$ in $S^3$, (i) and (ii) of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} hold for $\mathsf{H}_{123}(X;\mathcal{T})$.
:::

::: proof
*Proof.* The proof of $(i)$ immediately follows from independence of the limit [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} on the choice of the potential $\alpha_\omega$. For the proof of $(ii)$ we must show the following $$\int_\mathcal{T} m_{X_1,X_2,X_3}\,\mu_1\wedge \mu_2\wedge \mu_3=\int_{g(\mathcal{T})} m_{g_\ast X_1,g_\ast X_2, g_\ast X_3}\,\mu_1\wedge \mu_2\wedge \mu_3\ .$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}, tells us that $m_{X_1,X_2,X_3}$ and $m_{g_\ast X_1,g_\ast X_2, g_\ast X_3}$ admit $L^1$-averages $\bar{m}_{X_1,X_2,X_3}$ and $\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}$, under actions of $X_i$ and $g_\ast X_i$ respectively. If the following holds: $$\label{eq:m=gm}
 \bar{m}_{X_1,X_2,X_3}(x,y,z)=\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}(g(x),g(y),g(z)),\qquad \text{a.e.},$$ then [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"} is an immediate consequence of [\[eq:ergodic-integrals-equal\]](#eq:ergodic-integrals-equal){reference-type="eqref" reference="eq:ergodic-integrals-equal"}, change of variables for integrals, and the fact that $g$ preserves the volume, i.e. $\mu_i=g^\ast\mu_i$. Borrowing notation from the previous theorem we set $$\begin{aligned}
 g\bar{\mathscr{O}}(x,y,z;T) & := & g(\bar{\mathscr{O}}^{X_1}_T(x))\times g(\bar{\mathscr{O}}^{X_2}_T(y))\times g(\bar{\mathscr{O}}^{X_3}_T(z))\\
 & = & \bar{\mathscr{O}}^{g_\ast X_1}_T(g(x))\times \bar{\mathscr{O}}^{g_\ast X_2}_T(g(y))\times \bar{\mathscr{O}}^{g_\ast X_3}_T(g(z)),
\end{aligned}$$ where the second identity is a consequence of the fact that the flow of $g_\ast X_i$ is obtained as a composition of $g$ and the flow of $X_i$. Since $g$ is isotopic to the identity, $\bar{\mathscr{O}}(x,y,z;T)$ and $\bar{\mathscr{O}}(x,y,z;T)$ are isotopic borromean links in $S^3$, and for every $T$: $$\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))=\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T)).$$ As a result of the above identity and [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} we derive a.e. $$\begin{aligned}
  \bar{m}_{X_1,X_2,X_3}(x,y,z) & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
   & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T))=\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}(g(x),g(y),g(z)).
\end{aligned}$$ Notice that in the last equation we used in the "pushed forward" short paths system: $g\mathcal{S}$. But since lengths of paths in $g\mathcal{S}$ are bounded as well, they do not contribute to the limit. This proves the identity [\[eq:m=gm\]](#eq:m=gm){reference-type="eqref" reference="eq:m=gm"}, and consequently [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}. ◻
:::

Notice that the above argument does not require the Stokes Theorem, and thus may lead to further generalizations. Clearly, for $\mathsf{H}_{123}(X;\mathcal{T})$ to be nontrivial $\mathcal{T}$ must be of nonzero measure.

The following formula is a well known property of the ordinary helicity $\mathsf{H}_{12}(X;\mathcal{T})$ of the flux tubes $\mathcal{T}$ modeled on a 2-component link $L=\{L_1,L_2\}$ (see e.g. [@Laurence-Avellaneda93; @Cantarella00])

$$\label{eq:helicity12-flux-tubes}
\mathsf{H}_{12}(X;\mathcal{T})=\mathsf{H}_{12}(X_1,X_2)=\text{lk}(L_1,L_2)\,\text{Flux}(X_1)\,\text{Flux}(X_2).$$ Next we show that an analogous property holds $\mathsf{H}_{123}(X;\mathcal{T})$, for invariant unlinked handlebodies $\mathcal{T}$ investigated in the previous section.

::: proposition
$\mathsf{H}_{123}(X_1,X_2,X_3)$ on invariant unlinked handlebodies $\mathcal{T}$ satisfies the following formula $$\label{eq:helicity-fluxes}
 \mathsf{H}_{123}(X_1,X_2,X_3)=\sum_{i\neq j\neq k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{Flux}_{\Sigma_i}(X_1)\,\text{Flux}_{\Sigma_j}(X_2)\,\text{Flux}_{\Sigma_k}(X_3)\ .$$ where $\{L^i_1\otimes L^j_2\otimes L^k_3\}$ is a basis of basic cycles of $H_1(\mathcal{T}_1)\otimes H_1(\mathcal{T}_2)\otimes H_1(\mathcal{T}_3)$, $\text{Flux}(X_i)$ stands for the flux of $X_i$ through a cross sectional surface $\Sigma_k$ of $\mathcal{T}_i$, which represents a homology Poincar$\acute{\rm e}$ dual of $L^k_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.
:::

::: proof
*Proof.* Recall that a flux $\text{Flux}_{\Sigma_k}(X_i)$ of a vector field $X_i$ though a cross-sectional surface $\Sigma_k$ is given by: $$\begin{aligned}
  \text{Flux}_{\Sigma_k}(X_i) & = & \int_{\Sigma_k} \iota_{X_i}\mu=\int_{\mathcal{T}_i} h_k\wedge\iota_{X_i}\mu\\
  & = & \int_{\mathcal{T}_i} \iota_{X_i}h_k\wedge\mu =\int_{\mathcal{T}_i} h_k(X_i),
 
\end{aligned}$$ where 1-forms $h_k$ represent cohomology Poincar$\acute{\rm e}$ duals of $\Sigma_k$ and we applied [\[eq:iota-antiderivation\]](#eq:iota-antiderivation){reference-type="eqref" reference="eq:iota-antiderivation"} in the third equation. Clearly, $h_i\in \Omega^1(\mathcal{T}_i)$ satisfy $$\int_{\gamma} h_k=\#(\gamma,\Sigma_k)=\text{deg}(\gamma, L_k),$$ where $\text{deg}(\gamma, L^j_k)$ measures how many times $\gamma$ "wraps around" in the cycle $L^j_k$.

For simplicity we first assume that $\mathcal{T}$ is modeled on a borromean link $L=\{L_1,L_2,L_3\}$ (see Figure [\[fig:invariant-sets\]](#fig:invariant-sets){reference-type="ref" reference="fig:invariant-sets"}). Then $h=h_1\wedge h_2\wedge h_3\in \Omega^3(\mathcal{T})$ is a cohomology class dual of the cycle $L=L_1\times L_2\times L_3$ in $\mathcal{T}$. We set $$H:=\iota_{X_1}\iota_{X_2}\iota_{X_3} h=h(X_1,X_2,X_3),$$ which is a smooth function, and let $\bar{H}$ be the time average of $H$ as in Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. It suffices to show $$\label{eq:H-equation}
   \bar{m}_{X_1,X_2,X_3}=\bar{\mu}_{123}(L)\,\bar{H},\qquad \text{a.e.}$$ Analogously as in Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, Equation [\[eq:H-equation\]](#eq:H-equation){reference-type="eqref" reference="eq:H-equation"} immediately implies Formula [\[eq:helicity-fluxes\]](#eq:helicity-fluxes){reference-type="eqref" reference="eq:helicity-fluxes"}. Assume the notation of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, for given $T$ consider $\bar{\mathscr{O}}(x,y,z;T)$. By the fundamental property of the $\bar{\mu}_{123}$-invariant (see Corollary [\[th:general-mu_123\]](#th:general-mu_123){reference-type="ref" reference="th:general-mu_123"}) we have $$\begin{aligned}
  \bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T)) & = & \bar{\mu}_{123}(L)\,\bigl(\text{deg}(\bar{\mathscr{O}}^{X_1}_T(x),L_1)\,\text{deg}(\bar{\mathscr{O}}^{X_2}_T(y),L_2)\,\text{deg}(\bar{\mathscr{O}}^{X_3}_T(x),L_3)\bigr)\\
  & = & \bar{\mu}_{123}(L)\int_{\bar{\mathscr{O}}(x,y,z;T)} h\ .
 
\end{aligned}$$ Thus we obtain $$\begin{aligned}
  \bar{m}_{X_1,X_2, X_3}(x,y,z) & = & \lim_{T\to \infty} \frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
  & = & \bar{\mu}_{123}(L)\lim_{T\to \infty} \frac{1}{T^3}\int_{\bar{\mathscr{O}}(x,y,z;T)} H\\
  & =  &\bar{\mu}_{123}(L) \bar{H}(x,y,z),
 
\end{aligned}$$ where the last equality is again the consequence of short paths not contributing to the limit.

Now, from the product structure and $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} we have $$\int_\mathcal{T} \bar{H} =\int_\mathcal{T} H=\bigl(\int_{\mathcal{T}_1} h_1(X_1) \bigr)\bigl(\int_{\mathcal{T}_2} h_2(X_2) \bigr)\bigl(\int_{\mathcal{T}_3} h_3(X_3) \bigr).$$ The proof in the case of a general handlebody is analogous, once we show the following

::: lemma
Let $\mathcal{O}=\{\mathcal{O}_1,\mathcal{O}_2, \mathcal{O}_3\}$ be a 3-component link in $S^3$ such that $\mathcal{O}_i\subset \mathcal{T}_i$ for each $i$. Then $\mathcal{O}$ is borromean and $$\label{eq:mu-in-T}
 \bar{\mu}_{123}(\mathcal{O})=\sum_{i\neq j\neq k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{deg}(\mathcal{O}_1, L^i_1)\,\text{deg}(\mathcal{O}_2, L^j_2)\,\text{deg}(\mathcal{O}_3, L^k_1)\ .$$
:::

::: proof
*Proof.* Notice that thanks to our new interpretation, the $\bar{\mu}_{123}$-invariant is not only a link homotopy invariant but a homotopy invariant of the associated map $F_{\mathcal{O}}$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. Observe that each component $\mathcal{O}_i$ can be homotopied inside of its handlebody $\mathcal{T}_i$ to be come a bouquet of circles $\widehat{\mathcal{O}}_i\cong S^1\vee S^1\vee\ldots\vee S^1$. Such that each factor in $\widehat{\mathcal{O}}_i$ is a basic cycle in $H_1(\mathcal{T}_i)$. As a result we obtain the associated map $F_{\widehat{\mathcal{O}}}$, and $$\bar{\mu}_{123}(\mathcal{O})=\frac{1}{2}\mathscr{H}(F_{\widehat{\mathcal{O}}}).$$ Interpreting, $\mathscr{H}(F_{\widehat{\mathcal{O}}})$ as the intersection number and summing up intersection numbers we conclude [\[eq:mu-in-T\]](#eq:mu-in-T){reference-type="eqref" reference="eq:mu-in-T"}. ◻
:::

 ◻
:::

In the case of borromean flux tubes modeled on $L$, [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} reduces to $$\label{eq:helicity12-borro-flux-tubes}
\mathsf{H}_{123}(X_1,X_2,X_3)=\bar{\mu}_{123}(L)\,\text{Flux}_{\Sigma_1}(X_1)
\text{Flux}_{\Sigma_2}(X_2)\text{Flux}_{\Sigma_3}(X_3),$$ where $\Sigma_i$ denotes homology Poincar$\acute{\rm e}$ duals to $L_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.

Since the fluxes are invariant under frozen-in-field deformations Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} is yet another proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} in the setting of invariant unlinked handlebodies. In [@Laurence-Stredulinsky00b] the authors develop the same formula for the borromean flux tubes. This clearly must be the case as we deal with the same topological invariants of links via a different approach. Additional advantage of our formulation is that we do not have to separately deal with null points of vector fields as in [@Laurence-Stredulinsky00b]. We also note that in [@Laurence-Stredulinsky00b] the authors prove the helicity invariance only via Formula [\[eq:helicity12-borro-flux-tubes\]](#eq:helicity12-borro-flux-tubes){reference-type="eqref" reference="eq:helicity12-borro-flux-tubes"}.
