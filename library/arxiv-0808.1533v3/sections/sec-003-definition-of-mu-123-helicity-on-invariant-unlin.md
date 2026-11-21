---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-003-definition-of-mu-123-helicity-on-invariant-unlin
section_title: "Definition of ``mu-123-helicity'' on invariant unlinked handlebodies."
section_number: null
pages: 11-15
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.993
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
[]{#sec:handlebody label="sec:handlebody"}

In this section we apply the formulation of the $\bar{\mu}_{123}$-invariant for the 3-component links in $S^3$, obtained in Section [\[sec:mu-and-hopf\]](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, to define the third order helicity of a volume preserving vector field $B$ on certain invariant sets $\mathcal{T}$ of $B$ in $S^3$. In the following paragraphs as a "warm-up" to a more general case treated in Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}, we consider the case of three disjoint unlinked handlebodies: $\mathcal{T}=\mathcal{T}_1\cup     \mathcal{T}_2\cup \mathcal{T}_3$ in $S^3$ each of genus $g(\mathcal{T}_i)$. Henceforth, we use "unlinked" to mean "with pairwise unlinked connected components". When $\mathcal{T}$ represents three unlinked tubes (also known as *flux tubes* [@Khesin98]) in $\mbox{\bbb R}^3$, the third order helicity has been developed by several authors [@Berger90; @Mayer03; @Laurence-Stredulinsky00b] via Massey product formula for the $\bar{\mu}_{123}$-invariant, we compare our approach to these known works in Section [\[sec:massey\]](#sec:massey){reference-type="ref" reference="sec:massey"}.

<figure id="fig:invariant-sets">
<div class="picture">
<p>(400,190) (10,30)<span><img src="T-borr-S" style="width:2in" alt="image" /></span> (180,0)<span><img src="T-borr-2-S" style="width:4in" alt="image" /></span> (20,30)<span><span class="math inline">𝒯<sup>Borr</sup></span></span> (60,140)<span><span class="math inline">𝒯<sub>2</sub></span></span> (25,80)<span><span class="math inline">𝒯<sub>3</sub></span></span> (125,70)<span><span class="math inline">𝒯<sub>1</sub></span></span></p>
</div>
<figcaption>The simplest unlinked handlebodies: flux tubes <span class="math inline">𝒯<sup>Borr</sup></span> modeled on the Borromean rings (left), and unlinked genus <span class="math inline">2</span> handlebodies (right).</figcaption>
</figure>

Assume $\mathcal{T}_i$s have smooth boundary and $B$ to be tangent to $\partial \mathcal{T}_i$, we set $$B_i:=B\bigl|_{\mathcal{T}_i},\qquad i=1,2,3,$$ and denote the flow of $B$ on $S^3$ by $\Phi$, and flows of restrictions $B_i$ by $\Phi^i$. Clearly, such $\mathcal{T}$ is an invariant set of $B$. Given any domain $\mathcal{T}$ with three connected components $\{\mathcal{T}_i\}$ we may always associate a product domain in $\text{\rm Conf}_3(S^3)$ as follows $$\label{eq:admissible-domain}
 \mathcal{T}:=\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\subset \text{\rm Conf}_3(S^3)\subset S^3\times S^3\times S^3\ .$$ Notice that $\mathcal{T}$ is a domain with corners in $\text{\rm Conf}_3(S^3)$, and we use the same notation for the product of $\mathcal{T}_i$ as for the union in $S^3$. Wherever needed, we also assume that $(S^3)^3$ is equipped with a product Riemannian metric. Let a domain $\mathcal{T}$ defined in [\[eq:admissible-domain\]](#eq:admissible-domain){reference-type="eqref" reference="eq:admissible-domain"}, where $\mathcal{T}_i\cap \mathcal{T}_j=$Ø, $i\neq j$ and each $\mathcal{T}_i$ is a handlebody in $S^3$ be called *unlinked handlebody*, if and only if, the 2-form $\omega\in\Omega^2(\text{\rm Conf}_3(S^3))$ defined in Equation [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} is exact on $\mathcal{T}$, i.e. $\omega$ has a local *potential* $\alpha_\omega\in \Omega^1(\mathcal{T})$: $$\label{eq:omega-exact}
 \omega=d\alpha_\omega\ .$$ Denote a volume preserving vector field $B$ and an unlinked handlebody $\mathcal{T}$ as a pair $(B;\mathcal{T})$.

::: remark
Since $\omega$ is a dual cohomology class to the $S^2$ factor in $\text{\rm Conf}_3(S^3)\cong S^3\times S^2$, $\omega$ does not admit a global potential.
:::

Because each handlebody $\mathcal{T}_i$ has a homotopy type of a bouquet of circles, there is a natural choice of the basis for $H_1(\mathcal{T}_i)$ which consists of cycles $\{L^k_i\}_{k=1,\ldots,g(\partial\mathcal{T}_i)}$ corresponding to the circles. We have the following practical characterization of unlinked handlebodies:

::: lemma
[]{#lem:unlinked-handlebody label="lem:unlinked-handlebody"} $\mathcal{T}$ is an unlinked handlebody, if and only if, $$\label{eq:admissible-condition}
  \text{lk}(L^k_i,L^r_j)  = 0,\qquad \text{for all\ }\, i,j,\qquad i\neq j$$
:::

::: proof
*Proof.* The standard integral pairing, [@Bott82], $H^2(\mathcal{T})\times H_2(\mathcal{T})\longrightarrow \mbox{\bbb R}$ implies that a closed $k$-form is exact, if and only if, it evaluates to zero on all $k$-cycles of the domain. By the K$\ddot{\rm u}$nneth formula $H_2(\mathcal{T})=H_2(\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3)$ is generated by $L^k_i\otimes L^r_j$, and by [\[eq:linking-numbers\]](#eq:linking-numbers){reference-type="eqref" reference="eq:linking-numbers"}: $$\text{lk}(L^k_i,L^r_j) = \int_{L^k_i\times L^r_j} \omega\qquad  i\neq j.$$ Therefore the condition [\[eq:admissible-condition\]](#eq:admissible-condition){reference-type="eqref" reference="eq:admissible-condition"} is necessary and sufficient for $\omega$ to be exact on $\mathcal{T}$. ◻
:::

We define the $\bar{\mu}_{123}$-helicity of $(B;\mathcal{T})$ denoted by $\mathsf{H}_{123}(B;\mathcal{T})$ or $\mathsf{H}_{123}(B_1,B_2,B_3)$ as follows: $$\label{eq:mu_123-helicity}
\boxed{\mathsf{H}_{123}(B;\mathcal{T})=\mathsf{H}_{123}(B_1,B_2,B_3)\stackrel{\text{def.}}{=}\int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3, }$$ where $\mu_i$ denotes the pull-back of the volume form $\mu$ on $S^3$ under the projection $$\label{eq:projection-i}
\pi_i:S^3\times S^3\times S^3\longrightarrow S^3,\qquad \pi_i(x_1,x_2,x_3)=x_i,$$ and $\iota_{B_i}$ is a contraction by a vector field $B_i$. Our notational convention is to denote by $\iota_{B_i}\mu_i$ both the forms on the base of $\pi_i$ and the pullbacks: $\pi^\ast_i\bigl(\iota_{B_i}\mu_i\bigr)$. Notice that $\mu=\mu_1\wedge\mu_2\wedge\mu_3$ is a volume form on the product: $S^3\times S^3\times S^3$. There are obvious analogies between Formula [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} above, Formula [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"} for $\mathsf{H}_{12}(B;\mathcal{T})$, and the integral formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} for the $\bar{\mu}_{123}$-invariant. The $3$-form: $$\gamma_\omega:=\alpha_\omega\wedge d\alpha_\omega=\alpha_\omega\wedge \omega,$$ plays a role of the linking form as $\omega$ in Formula [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"}. The main motivation behind definition [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} is the ergodic interpretation of $\mathsf{H}_{123}(B;\mathcal{T})$ as an average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $B$, which will become apparent in Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}. Formula [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} can be also regarded as the third order helicity of three distinct vector fields $B_i$, supported on the handlebodies $\mathcal{T}_i$. In Section [\[sec:energy\]](#sec:energy){reference-type="ref" reference="sec:energy"}, we indicate how to construct the potential $\alpha_\omega$ from the basic elliptic theory of differential forms.

::: theorem
[]{#th:invariance-th label="th:invariance-th"} On every unlinked invariant handlebody $\mathcal{T}$ in $S^3$, $\mathsf{H}_{123}(B;\mathcal{T})$ is

-   independent of a choice of the potential $\alpha_\omega$,

-   invariant under the action of $\text{\rm SDiff}_0(S^3)$, i.e. for every $g\in \text{\rm SDiff}_0(S^3)$: $$\begin{gathered}
    \label{eq:invariance}
     \mathsf{H}_{123}(B;\mathcal{T})=\mathsf{H}_{123}(g_\ast B;g(\mathcal{T}))\ .
    \end{gathered}$$
:::

::: proof
*Proof.* To prove $(i)$ observe for every other potential $\alpha'_\omega$ of $\omega$, the difference $\beta=\alpha_\omega-\alpha'_\omega$ is a closed $1$-form on $\mathcal{T}$ (since $\omega=d\alpha_\omega=d\alpha'_\omega$). Therefore, $$\begin{aligned}
 \mathsf{H}_{123}(B;\mathcal{T})-\mathsf{H}_{123}'(B;\mathcal{T}) & = & \int_{\mathcal{T}} (\beta\wedge\omega)\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\\
 & \stackrel{(1)}{=} & \int_{\mathcal{T}} d\bigl(\beta\wedge \alpha_\omega\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\bigr)\\
 & = & \int_{\partial\mathcal{T}} \beta\wedge \alpha_\omega\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3 \stackrel{(2)}{=} 0,
\end{aligned}$$ where in (1) we applied $d(\iota_{B_i}\mu_i)=0$ (since $B_i$'s are divergence free), and in (2): $$\iota_{B_i}\mu_i\bigl|_{\partial\mathcal{T}_i}=0,$$ (because each vector field $B_i$ is tangent to the boundary $\partial \mathcal{T}_i$), where $$\partial \mathcal{T}=\bigl(\partial \mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \partial\mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \mathcal{T}_2\times \partial\mathcal{T}_3\bigr).$$

The proof of $(ii)$ is in the style of [@Berger90; @Mayer03], but adapted to our setting. For any given $g\in \text{\rm SDiff}(S^3)$, by definition, there exists a path $t\longrightarrow g(t)\in \text{\rm SDiff}_0(S^3)$, such that $$g(0)=\text{id}_{S^3},\qquad g(1)=g\ .$$ Denote by $V$ the divergence free vector field on $S^3$, given by $V(x)=\frac{d}{dt} g(t,x)|_{t=0}$, i.e. $g(t)$ is a flow of $V$, and push-forward fields $B_i$ by $$B^t_i:=g(t)_\ast B_i\ .$$ It is well known (see Appendix [\[apx:A\]](#apx:A){reference-type="ref" reference="apx:A"}, or [@Freedman91-2 p. 224]) that 2-forms: $\iota_{B^t_i}\mu$ are frozen in the flow of $V$, i.e. $$\label{eq:forms-frozen-in}
 \frac{d}{dt}\bigl(g(t)^\ast\iota_{B^t_i}\mu\bigr) =(\partial_t+\mathcal{L}_V) \iota_{B^t_i}\mu = 0.$$ We also have a path $\hat{g}(t)=(g(t),g(t),g(t))$ in $\text{\rm SDiff}_0(S^3\times S^3\times S^3)$, which analogously leads to the vector field $\hat{V}=(V,V,V)$. (Recall that a tangent bundle $T(S^3)^3$ has a natural product structure). Equation [\[eq:forms-frozen-in\]](#eq:forms-frozen-in){reference-type="eqref" reference="eq:forms-frozen-in"} implies $$\label{eq:forms-frozen-in2}
(\partial_t+\mathcal{L}_{\hat{V}}) \bigl(\pi^\ast_i\iota_{B^t_i}\mu\bigr)=(\partial_t+\mathcal{L}_{\hat{V}}) \iota_{B^t_i}\mu_i= 0\ .$$ (In the second equation we merely revoke our notational conventions: $\iota_{B^t_i}\mu_i\equiv\pi^\ast_i\bigl(\iota_{g(t)^\ast B_i}\mu\bigr)$).

Let $\mathcal{T}(t)=\hat{g}(t)(\mathcal{T}(0))\subset \text{\rm Conf}_3(S^3)$, we must show $\frac{d}{dt} 
\mathsf{H}_{123}(B^t_1,B^t_2,B^t_3)=0$. Notice that for small enough $\epsilon$ and $t\in (t_0-\epsilon,t_0+\epsilon)$ we can assume, by $(i)$, that $\alpha_\omega$ is a time independent potential obtained from slightly bigger domain $\widetilde{\mathcal{T}}$ which deformation retracts on $\mathcal{T}(t_0)$, and satisfies $$\mathcal{T}(t)\subset\widetilde{\mathcal{T}},\qquad \text{\rm for}\quad t\in (t_0-\epsilon,t_0+\epsilon)\ .$$ Without loss of generality set $t_0=0$, and $\hat{g}(0)=\text{id}_{(S^3)^3}$, at $t_0$ we calculate: $$\begin{aligned}
 \frac{d}{dt} 
 \Bigl(\mathsf{H}_{123}(g(t)^\ast B_1,g(t)^\ast B_2,g(t)^\ast B_3)\Bigr) & = &
 \frac{d}{dt} \int_{\mathcal{T}(t)} \alpha_\omega\wedge d\alpha_\omega\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3\\
 & = & \int_{\mathcal{T}(0)} \frac{d}{dt} \hat{g}(t)^\ast\bigl(\alpha_\omega\wedge d\alpha_\omega\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3\bigr)\\
 & = & \int_{\mathcal{T}(0)} \bigl(\mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega)\bigr)\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3,
\end{aligned}$$ where in the last identity we applied [\[eq:forms-frozen-in2\]](#eq:forms-frozen-in2){reference-type="eqref" reference="eq:forms-frozen-in2"} and the product rule for the Lie derivative. Now because $\omega\wedge\alpha_\omega$ is time independent (for $t\in (t_0-\epsilon,t_0+\epsilon)$), Cartan magic formula yields $$\begin{aligned}
 \mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) & = & \mathcal{L}_{\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) = \iota_{\hat{V}} d(\alpha_\omega\wedge d\alpha_\omega)+ d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega))\\
 & =  & d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega)),
\end{aligned}$$ where $d(\alpha_\omega\wedge d\alpha_\omega)=\omega\wedge\omega=0$. Since $B^t_i$ are tangent to the boundary of $\mathcal{T}_i(t)$, the same argument as in the proof of $(i)$ shows that the right hand side of the previous equation vanishes. ◻
:::

::: remark
Notice that the above argument indicates that if we replace $\alpha_{\omega}\wedge d\alpha_\omega$ by virtually any closed 3-form $\eta$ on $\text{\rm Conf}_3(S^3)$ (or $(S^3)^3$) we obtain some invariant under frozen-in-field deformations. If $\eta$ is exact we obtain trivial invariants, therefore the only sensible candidates here are cohomology classes of $\text{\rm Conf}_3(S^3)\cong S^3\times S^2$. In dimension $3$ it leaves us with a dual to the $S^3$ factor in $\text{\rm Conf}_3(S^3)$. Based on the considerations in Section [\[sec:mu-and-hopf\]](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"} one may argue that an invariant obtained this way is trivial. Indeed, the cohomology class $\eta$ evaluated on any 3-torus obtained from a 3-component link in $S^3$ via the map $L$ in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} is zero. Therefore, one could apply the ergodic approach of Section [\[sec:ergodic\]](#sec:ergodic){reference-type="ref" reference="sec:ergodic"} to show that $\int \eta\wedge\iota_{B}\mu_1\wedge \iota_{B}\mu_2\wedge \iota_{B}\mu_3$ defines a trivial invariant. The crucial obstacle in extending the formula in [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} to encompass the whole $(S^3)^3$ is the fact that the potential $\alpha_\omega$ cannot be globally defined on $\text{\rm Conf}_3(S^3)$.
:::
