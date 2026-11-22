---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-005-flux-formula-for-h-123
section_title: "Flux formula for H-123."
section_number: null
pages: 19-21
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.994
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
The following formula is a well known property of the ordinary helicity $\mathsf{H}_{12}(B;\mathcal{T})$ of the flux tubes $\mathcal{T}$ modeled on a 2-component link $L=\{L_1,L_2\}$ (see e.g. [@Laurence-Avellaneda93; @Cantarella00])

$$\label{eq:helicity12-flux-tubes}
\mathsf{H}_{12}(B;\mathcal{T})=\mathsf{H}_{12}(B_1,B_2)=\text{lk}(L_1,L_2)\,\text{Flux}(B_1)\,\text{Flux}(B_2).$$ Here we show an analogous property for $\mathsf{H}_{123}(B;\mathcal{T})$, when $\mathcal{T}$ is an invariant unlinked handlebody. Recall that $\{L^k_i\}_{k=1,\ldots,g(\partial\mathcal{T}_i)}$ denotes the basis of $H_1(\mathcal{T})$ defined in Lemma [\[lem:unlinked-handlebody\]](#lem:unlinked-handlebody){reference-type="ref" reference="lem:unlinked-handlebody"}.

::: proposition
$\mathsf{H}_{123}(B_1,B_2,B_3)$ on invariant unlinked handlebodies $\mathcal{T}$ satisfies the following formula $$\label{eq:helicity-fluxes}
 \mathsf{H}_{123}(B_1,B_2,B_3)=\sum_{i, j, k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{Flux}_{\Sigma_i}(B_1)\,\text{Flux}_{\Sigma_j}(B_2)\,\text{Flux}_{\Sigma_k}(B_3),$$ where $\{L^i_1\otimes L^j_2\otimes L^k_3\}$ is a basis of $H_3(\mathcal{T})$, $\text{Flux}(B_i)$ stands for the flux of $B_i$ through a cross sectional surface $\Sigma_k$ of $\mathcal{T}_i$, which represents the homology Poincar$\acute{\rm e}$ dual of $L^k_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.
:::

::: proof
*Proof.* Recall that the flux $\text{Flux}_{\Sigma_k}(B_i)$ of a vector field $B_i$ though a cross-sectional surface $\Sigma_k$ in $\mathcal{T}_i$ is given by: $$\label{eq:flux}
 \begin{split}
  \text{Flux}_{\Sigma_k}(B_i) & =  \int_{\Sigma_k} \iota_{B_i}\mu=\int_{\mathcal{T}_i} h_k\wedge\iota_{B_i}\mu\\
  & =  \int_{\mathcal{T}_i} \iota_{B_i}h_k\wedge\mu =\int_{\mathcal{T}_i} h_k(B_i),
  \end{split}$$ where 1-forms $h_k$ represent cohomology Poincar$\acute{\rm e}$ duals of $\Sigma_k$, and we applied [\[eq:iota-antiderivation\]](#eq:iota-antiderivation){reference-type="eqref" reference="eq:iota-antiderivation"} in the third equation. For every closed curve $\gamma\subset \mathcal{T}$ $h_k$ satisfies $$\int_{\gamma} h_k=\#(\gamma,\Sigma_k)=\text{deg}(\gamma, L_k),$$ where $\text{deg}(\gamma, L^j_k)$ measures how many times $\gamma$ "wraps around" the cycle $L^j_k$.

For simplicity, we first assume that $\mathcal{T}$ is modeled on a Borromean link $L=\{L_1,L_2,L_3\}$ (such as $\mathcal{T}^\text{Borr}$ on Figure [\[fig:invariant-sets\]](#fig:invariant-sets){reference-type="ref" reference="fig:invariant-sets"}). Then, $h=h_1\wedge h_2\wedge h_3\in \Omega^3(\mathcal{T})$ is a cohomology class dual to the cycle $L_1\otimes L_2\otimes L_3$ in $H_3(\mathcal{T})$. Define $$H:=\iota_{B_3}\iota_{B_2}\iota_{B_1} h=h(B_1,B_2,B_3),$$ which is a smooth function, and let $\bar{H}$ be the time average of $H$ as in Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. It suffices to show $$\label{eq:H-equation}
   \bar{m}_{B_1,B_2,B_3}=\bar{\mu}_{123}(L)\,\bar{H},\qquad \text{a.e.}$$ Analogously, as in the proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, Equation [\[eq:H-equation\]](#eq:H-equation){reference-type="eqref" reference="eq:H-equation"} immediately implies Formula [\[eq:helicity-fluxes\]](#eq:helicity-fluxes){reference-type="eqref" reference="eq:helicity-fluxes"}. Assume the notation of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, for given $T$ consider $\bar{\mathscr{O}}(x,y,z;T)$. Thanks to Theorem [\[th:milnor-hopf\]](#th:milnor-hopf){reference-type="ref" reference="th:milnor-hopf"} (see the first paragraph of the proof) we have $$\begin{aligned}
  \bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T)) & = & \bar{\mu}_{123}(L)\,\bigl(\text{deg}(\bar{\mathscr{O}}^{B_1}_T(x),L_1)\,\text{deg}(\bar{\mathscr{O}}^{B_2}_T(y),L_2)\,\text{deg}(\bar{\mathscr{O}}^{B_3}_T(x),L_3)\bigr)\\
  & = & \bar{\mu}_{123}(L)\int_{\bar{\mathscr{O}}(x,y,z;T)} h\ .
 
\end{aligned}$$ Therefore, $$\begin{aligned}
  \bar{m}_{B_1,B_2, B_3}(x,y,z) & = & \lim_{T\to \infty} \frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
  & = & \bar{\mu}_{123}(L)\lim_{T\to \infty} \frac{1}{T^3}\int_{\bar{\mathscr{O}}(x,y,z;T)} H\\
  & =  &\bar{\mu}_{123}(L) \bar{H}(x,y,z),
 
\end{aligned}$$ where the last equality is again the consequence of short paths not contributing to the limit. From the product structure of $\mathcal{T}$ and $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} we get $$\int_\mathcal{T} \bar{H} =\int_\mathcal{T} H=\bigl(\int_{\mathcal{T}_1} h_1(B_1) \bigr)\bigl(\int_{\mathcal{T}_2} h_2(B_2) \bigr)\bigl(\int_{\mathcal{T}_3} h_3(B_3) \bigr),$$ which combined with Equation [\[eq:flux\]](#eq:flux){reference-type="eqref" reference="eq:flux"} for fluxes concludes the proof in the case of Borromean flux tubes. The proof in the case of a general handlebody is analogous, once we show the following

::: lemma
Let $\mathcal{O}=\{\mathcal{O}_1,\mathcal{O}_2, \mathcal{O}_3\}$ be a 3-component link in $S^3$ such that $\mathcal{O}_i\subset \mathcal{T}_i$ for each $i$. Then $\mathcal{O}$ is Borromean and $$\label{eq:mu-in-T}
 \bar{\mu}_{123}(\mathcal{O})=\sum_{i, j, k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{deg}(\mathcal{O}_1, L^i_1)\,\text{deg}(\mathcal{O}_2, L^j_2)\,\text{deg}(\mathcal{O}_3, L^k_1)\ .$$
:::

::: proof
*Proof.* Thanks to the interpretation of the $\bar{\mu}_{123}$-invariant in Section [\[sec:mu-and-hopf\]](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, it is not only a link homotopy invariant, but also a homotopy invariant of the associated map $F_{\mathcal{O}}$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. Observe that each component $\mathcal{O}_i$ can be homotoped inside of its handlebody $\mathcal{T}_i$ to become a bouquet of circles $\widehat{\mathcal{O}}_i\cong S^1\vee S^1\vee\ldots\vee S^1$ so that each factor in $\widehat{\mathcal{O}}_i$ is a multiple of the cycle represented by $\{L^j_i\}$in $H_1(\mathcal{T}_i)$. As a result, we obtain the associated map $F_{\widehat{\mathcal{O}}}$, and $$\bar{\mu}_{123}(\mathcal{O})=\frac{1}{2}\mathscr{H}(F_{\widehat{\mathcal{O}}}).$$ Interpreting $\mathscr{H}(F_{\widehat{\mathcal{O}}})$ as the intersection number and summing up intersection numbers we conclude [\[eq:mu-in-T\]](#eq:mu-in-T){reference-type="eqref" reference="eq:mu-in-T"}. ◻
:::

 ◻
:::

In the case of Borromean flux tubes, Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} reduces to $$\label{eq:helicity12-borro-flux-tubes}
\mathsf{H}_{123}(B_1,B_2,B_3)=\bar{\mu}_{123}(L)\,\text{Flux}_{\Sigma_1}(B_1)
\text{Flux}_{\Sigma_2}(B_2)\text{Flux}_{\Sigma_3}(B_3),$$ where $\Sigma_i$ denotes homology Poincar$\acute{\rm e}$ duals to $L_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.

Since the fluxes are invariant under frozen-in-field deformations, Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} is yet another proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} in the setting of invariant unlinked handlebodies. In [@Laurence-Stredulinsky00b] the authors develop the same formula for the Borromean flux tubes. This clearly must be the case, as we work with the same topological invariants of links via a different approach. Additional advantage of our formulation is that we do not have to separately deal with null points of vector fields as in [@Laurence-Stredulinsky00b].
