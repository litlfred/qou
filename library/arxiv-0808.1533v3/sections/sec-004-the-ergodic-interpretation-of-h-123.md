---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-004-the-ergodic-interpretation-of-h-123
section_title: "The ergodic interpretation of H-123"
section_number: null
pages: 15-19
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.996
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
[]{#sec:ergodic label="sec:ergodic"}

The following statement is often seen in literature [@Cantarella-DeTurck-Gluck01; @Cantarella-DeTurck-Gluck-Teytel00]:

> *Helicity measures the extent to which vector fields twist and coil around each other.*

A beauty of Arnold's ergodic approach to the helicity $\mathsf{H}_{12}(B)$ is that it makes this statement precise, by interpreting $\mathsf{H}_{12}(B)$ as an average asymptotic linking number of orbits of $B$. But, it also has a practical application as it allows us to extend our approach to certain invariant sets of $B$. In this section we apply this philosophy to our newly defined invariant $\mathsf{H}_{123}(B;\mathcal{T})$, and interpret it as the average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $B$ in $\mathcal{T}$. Moreover, this ergodic interpretation leads us to an alternative, more intuitive proof of Helicity Invariance Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}.

We begin by observing that given a volume preserving vector field $B$ on $M$ and its flow $\Phi_t$, we may regard $B$ as three vector fields on $(M)^3$. Thus, $(\Phi,\Phi,\Phi)$ induces a natural $\mbox{\bbb R}^3$ action defined as follows: $$\label{eq:R3-action}
 \mathbf{\Phi}:\mbox{\bbb R}^3\times (M)^3\longrightarrow (M)^3,\qquad \bigl((s,t,u),x,y,z\bigr)\stackrel{\mathbf{\Phi}}{\longrightarrow} (\Phi(s,x),\Phi(t,y), \Phi(u,z)).$$ Observe that $\mathbf{\Phi}$ is a volume preserving action on $(M)^3$. Our analysis is rooted in techniques developed in [@Arnold86; @Laurence-Avellaneda93; @Laurence-Stredulinsky00b; @Vogel03], the main tool is the following

::: theorem
[]{#th:multi-ergodic label="th:multi-ergodic"} For any real valued $L^1$-function $F$ on $(M)^3$, the time averages under the action in [\[eq:R3-action\]](#eq:R3-action){reference-type="eqref" reference="eq:R3-action"}: $$\begin{gathered}
\bar{F}(x,y,z)=\lim_{T\to \infty}\frac{1}{T^3}\int^T_0\int^T_0\int^T_0
 F(\Phi(x,s),\Phi(y,t),\Phi(z,u))\,d s\,d t\,d u
\end{gathered}$$ converge almost everywhere. In addition, the limit function $\bar{F}$ satisfies

-   $\|\bar{F}\|_{L^1((M)^3)}\leq \|F\|_{L^1((M)^3)}$,

-   $\bar{F}$ is invariant under the $\mathbf{\Phi}$-action,

-   if $(M)^3$ is of finite volume then $$\begin{gathered}
    \label{eq:ergodic-integrals-equal}
     \int_{(M)^3}\bar{F} =\int_{(M)^3} F\ .
    \end{gathered}$$
:::

::: definition
Define *invariant unlinked domain* $\mathcal{T}$ of $B$ as an arbitrary $\mathbf{\Phi}$-invariant set, with topological closure $\overline{\mathcal{T}}$ which belongs to a larger product of open sets $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ in $\text{\rm Conf}_3(S^3)$, satisfying the following

-   $\widetilde{\mathcal{T}}$ admits a *short path system* $\mathcal{S}$,

-   Equation [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"} holds on $\widetilde{\mathcal{T}}$,

where by a system of short paths on $\widetilde{\mathcal{T}}$, [@Vogel03; @Khesin98], we understand a collection of curves $\mathcal{S}=\{\sigma_i(x,y)\}$ on each open set $\widetilde{\mathcal{T}}_i$ such that

-   for every pair of points $x,y \in \widetilde{\mathcal{T}}_i$ there is a connecting curve $\sigma_i(x,y):I\mapsto \widetilde{\mathcal{T}}_i$ in $\mathcal{S}$, $\sigma_i(0)=x$ and $\sigma_i(1)=y$,

-   the lengths of paths in $\mathcal{S}$ are uniformly bounded above by a common constant.
:::

Topologically, every $\mathbf{\Phi}$-invariant set is a union of products of orbits of $B$ in $(S^3)^3$. It is often convenient to think of the orbits $\mathbf{\Phi}$-action as a foliation of $(S^3)^3$. Then $\mathbf{\Phi}$-invariant sets are just union of leaves of this foliation. A fundamental example of an invariant unlinked domain is the case of $\mathbf{\Phi}$-invariant set $\mathcal{T}$ contained in the product $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ of disjoint open unlinked handlebodies $\widetilde{\mathcal{T}}_i$. Note that in this case we do not require $B$ to be tangent to $\partial\widetilde{\mathcal{T}}_i$, and $\widetilde{\mathcal{T}}$ always admits a short path system as we describe in the following

::: remark
In [@Vogel03], Vogel shows that on a closed manifold $M$, geodesics always provide a short path system. When $\mathcal{T}$ is contained in the product of unlinked handlebodies $\widetilde{\mathcal{T}}$ we may easily construct such system on $\widetilde{\mathcal{T}}$ as follows Because $\mathcal{\mathcal{T}}_i$ are proper subsets of $S^3$ we generally do not want to use ambient geodesics from $S^3$ as they may not lie entirely in $\mathcal{T}_i$. To obtain $\mathcal{S}$ one puts an artificial Riemannian metric on each $\widetilde{\mathcal{T}}_i$ which makes $\partial\widetilde{\mathcal{T}}_i$ totally geodesic, and choose $\mathcal{S}$ to be geodesics on such Riemannian manifold. Observe that applying a diffeomorphism $g\in \text{Diff}(\widetilde{\mathcal{T}})$ to $\mathcal{S}$ results in the system $g\mathcal{S}$ on $g(\widetilde{\mathcal{T}})$.
:::

The following result is an analog of Arnold's Helicity Theorem in our setting,

::: theorem
[]{#th:ergodic-mu label="th:ergodic-mu"} Given $(B;\mathcal{T})$, the following limit (asymptotic $\bar{\mu}_{123}$-invariant of orbits) exists for almost all $(x,y,z)\in \mathcal{T}$: $$\label{eq:bar-m_B}
 \bar{m}_B(x,y,z)=\lim_{T\to\infty} \frac{1}{T^3}\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{B_1}_T(x),\bar{\mathscr{O}}^{B_2}_T(y),\bar{\mathscr{O}}^{B_3}_T(y)\bigr).$$ Moreover, $$\label{eq:H_123-ergodic}
 \mathsf{H}_{123}(B;\mathcal{T})=\int_{\mathcal{T}} \bar{m}_B(x,y,z)\,\mu(x)\wedge\mu(y)\wedge\mu(z)\ .$$
:::

::: proof
*Proof.* The proof is similar to the one in e.g. [@Vogel03]. Before we start, we must point out the following identity (valid for any 3-form $\beta$ on $M\times M\times M$ and vector fields $B_1,B_2,B_3$ on $M$)

$$\label{eq:iota-volume}
 \begin{split}
(\iota_{B_3}\iota_{B_2}\iota_{B_1}\beta)\wedge\mu_1\wedge\mu_2\wedge\mu_3 & =
\beta(B_1,B_2,B_3)\,\mu_1\wedge\mu_2\wedge\mu_3\\
 & =\beta\wedge\iota_{B_1}\mu_1\wedge\iota_{B_2}\mu_2\wedge\iota_{B_3}\mu_3\ .
 \end{split}$$ The first equation follows from the definition, the second one is a consequence of the fact that $\iota_B$ is an antiderivation i.e. $$\label{eq:iota-antiderivation}
  \iota_B(\alpha\wedge\beta)=(\iota_B\alpha)\wedge\beta+(-1)^{|\alpha|}\alpha\wedge(\iota_B\beta),$$ and $\iota_{B_i}\mu_j=0$, for $i\neq j$ (see Appendix [\[apx:A\]](#apx:A){reference-type="ref" reference="apx:A"}). As a result, $$\begin{aligned}
\notag  \mathsf{H}_{123}(B_1,B_2,B_3) & = & \int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\\
& = & \int_\mathcal{T} \bigl(\iota_{B_3}\iota_{B_2}\iota_{B_1}\bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\bigr)\,\mu_1\wedge\mu_2\wedge\mu_3\\
\label{eq:m-function}  & = & \int_\mathcal{T} m_{B_1,B_2,B_3}(x,y,z)\,\mu_1\wedge \mu_2\wedge \mu_3,
\end{aligned}$$ where $m_{B_1,B_2,B_3}:=\alpha_\omega\wedge d\alpha_\omega(B_1,B_2,B_3)$. For convenience, let us set (see [\[eq:orbits\]](#eq:orbits){reference-type="eqref" reference="eq:orbits"}): $$\bar{\mathscr{O}}(x,y,z;T):=\bar{\mathscr{O}}^{B_1}_T(x)\times \bar{\mathscr{O}}^{B_2}_T(y)\times\bar{\mathscr{O}}^{B_3}_T(y)\ .$$ Observe that if the orbit $\bar{\mathscr{O}}(x,y,z;T)$ is nondegenerate, it represents a Borromean link and we may apply Formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} to get $$\begin{aligned}
\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{B_1}_T(x),\bar{\mathscr{O}}^{B_2}_T(y),\bar{\mathscr{O}}^{B_3}_T(y)\big)
& = & \int_{\bar{\mathscr{O}}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega\\
& = & \int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega+(I),
\end{aligned}$$ where the term $(I)$ involves integrals over short paths in $\mathcal{S}$, (see Appendix [\[apx:B\]](#apx:B){reference-type="ref" reference="apx:B"}). For degenerate orbits (such as fixed points etc.), the above formula still makes sense because $\bar{\mu}_{123}$ is a homotopy invariant of the associated map as proven in Section [\[sec:mu-and-hopf\]](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}. For every $(x,y,z)$ : $$D\mathbf{\Phi}_{(x,y,z)}[\partial_i]=B_i,\quad i=1,2,3,$$ where $\partial_1:=\partial_s$,$\partial_2:=\partial_t$,$\partial_3:=\partial_u$, thus we obtain $$\begin{aligned}
 \mathbf{\Phi}^\ast_{(x,y,z)}(\alpha_\omega\wedge d\alpha_\omega) & = & (\alpha_\omega\wedge d\alpha_\omega(B_1,B_2,B_3)(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\\
 & = & m_{B_1,B_2,B_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .
\end{aligned}$$ Therefore, $$\int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega=\int^T_0\int^T_0\int^T_0 m_{B_1,B_2,B_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .$$ Function $m_{B_1,B_2,B_3}$ is smooth bounded on $\mathcal{T}$ and hence $L^1$. Because short paths do not contribute to the time average (see Appendix [\[apx:B\]](#apx:B){reference-type="ref" reference="apx:B"}): $$\lim_{T\to\infty} \frac{1}{T^3}(I)=0.$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} applied to the function $m_{B_1,B_2,B_3}$ yields almost everywhere existence of the limit [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"}. Hence we obtain the invariant $L^1$-function $\bar{m}_B:=\bar{m}_{B_1,B_2,B_3}$ on $\mathcal{T}$. The identity [\[eq:H_123-ergodic\]](#eq:H_123-ergodic){reference-type="eqref" reference="eq:H_123-ergodic"} follows from $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. ◻
:::

::: theorem
[]{#th:invariance-th-ergodic label="th:invariance-th-ergodic"} On every unlinked domain $\mathcal{T}$ in $S^3$, (i) and (ii) of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} hold for $\mathsf{H}_{123}(B;\mathcal{T})$.
:::

::: proof
*Proof.* The proof of $(i)$ immediately follows from independence of the limit [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"} of the choice of the potential $\alpha_\omega$. For the proof of $(ii)$ we must show the following $$\int_\mathcal{T} m_{B_1,B_2,B_3}\,\mu_1\wedge \mu_2\wedge \mu_3=\int_{g(\mathcal{T})} m_{g_\ast B_1,g_\ast B_2, g_\ast B_3}\,\mu_1\wedge \mu_2\wedge \mu_3\ .$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} tells us that $m_{B_1,B_2,B_3}$ and $m_{g_\ast B_1,g_\ast B_2, g_\ast B_3}$ admit $L^1$-averages $\bar{m}_{B_1,B_2,B_3}$ and $\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}$, under actions of $B_i$ and $g_\ast B_i$ respectively. It suffices to show the following identity $$\label{eq:m=gm}
 \bar{m}_{B_1,B_2,B_3}(x,y,z)=\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}(g(x),g(y),g(z)),\qquad \text{a.e.}$$ then [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"} is an immediate consequence of Equation [\[eq:ergodic-integrals-equal\]](#eq:ergodic-integrals-equal){reference-type="eqref" reference="eq:ergodic-integrals-equal"}, change of variables for integrals, and the fact that $g$ preserves volume (i.e. $\mu_i=g^\ast\mu_i$). Borrowing notation from the previous theorem set $$\begin{aligned}
 g\bar{\mathscr{O}}(x,y,z;T) & := & g(\bar{\mathscr{O}}^{B_1}_T(x))\times g(\bar{\mathscr{O}}^{B_2}_T(y))\times g(\bar{\mathscr{O}}^{B_3}_T(z))\\
 & = & \bar{\mathscr{O}}^{g_\ast B_1}_T(g(x))\times \bar{\mathscr{O}}^{g_\ast B_2}_T(g(y))\times \bar{\mathscr{O}}^{g_\ast B_3}_T(g(z)),
\end{aligned}$$ where the second identity is a consequence of the fact that the flow of $g_\ast B_i$ is obtained as a composition of $g$ and the flow of $B_i$. Since $g$ is isotopic to the identity, $\bar{\mathscr{O}}(x,y,z;T)$ and $g\bar{\mathscr{O}}(x,y,z;T)$ are homotopic as link maps (for nondegenerate orbits they are in fact isotopic Borromean links in $S^3$) and by theorems of Section [\[sec:mu-and-hopf\]](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, we have $$\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))=\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T)).$$ As a result of the above identity and [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"} we derive a.e. $$\begin{aligned}
  \bar{m}_{B_1,B_2,B_3}(x,y,z) & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
   & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T))=\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}(g(x),g(y),g(z)).
\end{aligned}$$ Notice that in the last equation we used the "pushed forward" short paths system: $g\mathcal{S}$. Since the lengths of paths in $g\mathcal{S}$ are bounded as well, they do not contribute to the limit. This proves the identity [\[eq:m=gm\]](#eq:m=gm){reference-type="eqref" reference="eq:m=gm"}, and consequently [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}. ◻
:::

Notice that the above argument does not require the Stokes Theorem, and as such may lead to further generalizations. Clearly, for $\mathsf{H}_{123}(B;\mathcal{T})$ to be nontrivial $\mathcal{T}$ must be of nonzero measure.
