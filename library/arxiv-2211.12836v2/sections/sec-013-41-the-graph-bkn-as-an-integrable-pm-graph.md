---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-013-41-the-graph-bkn-as-an-integrable-pm-graph
section_title: "The graph Bk,n as an integrable PM-graph"
section_number: 4.1
pages: 22-25
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.932
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
Recall from Section [\[sec:intro_model\]](#sec:intro_model){reference-type="ref" reference="sec:intro_model"} that $L^2(B_{k,n})=\bigoplus_{I\in B_{k,n}}\mathbb{C} e_{I}$ denotes the Hilbert space of functions on $B_{k,n}$ with the scalar product $\langle e_{I},e_{J}\rangle=\delta_{I,J}$, where $\mathcal{B}_0=(e_{I})_{I\in B_{k,n}}$ is the canonical basis on $L^2(B_{k,n})$. Then, the graph structure on $B_{k,n}$ is encoded in the adjacency matrix $A\in \mathcal{B}(L^2(B_{k,n}))$ given by $$Ae_I=\sum_{I\nearrow J}e_J.$$

In the sequel, we will use a specialization of the quantum cohomology of the Grassmannian $QH(G_{k,n})$ to prove that $B_{k,n}$ is an integrable PM-graph as defined in Definition [\[def:PM-graph\]](#def:PM-graph){reference-type="ref" reference="def:PM-graph"}. The reader should refer to Appendix [\[sec:quantum_cohomology\]](#sec:quantum_cohomology){reference-type="ref" reference="sec:quantum_cohomology"} for any background on $QH(G_{k,n})$. We mainly need the fact that $QH(G_{k,n})=Sym[x_1,\ldots,x_k]\otimes \mathbb{C}[q]/Sym[x_1,\ldots,x_k]/\langle (x_1,\ldots,x_k)=q^{1/k}\left(e^{it_1},\ldots e^{it_k}\right), \vec{t}\in T_{k,n}\rangle$, see Appendix [\[sec:quantum_cohomology\]](#sec:quantum_cohomology){reference-type="ref" reference="sec:quantum_cohomology"}, and we will consider the specialization $$QH_{1}(G_{k,n}):=QH(G_{k,n})/\langle q=1\rangle=Sym[x_1,\ldots,x_k]/\langle(x_1,\ldots,x_k)=\left(e^{it_1},\ldots e^{it_k}\right), \vec{t}\in T_{k,n}\rangle.$$ The algebra $QH_{1}(G_{k,n})$ is spanned by the basis $\{s_{\lambda},\lambda\in \Lambda_{k,n}\}$, and we denote by $\ell:QH_1(G_{k,n})\rightarrow L^2(B_{k,n})$ the isomorphism defined by $$\ell(s_{\lambda})=e_{I_{\lambda}}.$$ Then, $B_{k,n}$ is a PM-graph in the sense of Definition [\[def:PM-graph\]](#def:PM-graph){reference-type="ref" reference="def:PM-graph"} with an enveloping algebra $\mathcal{A}\simeq QH_{1}(G_{k,n})$, as the next proposition shows.

::: proposition
[]{#prop:equiv_graph_qh label="prop:equiv_graph_qh"} There is a commutative algebra $\mathcal{A}\subset \mathcal{B}(L^2(B_{k,n}))$ containing $\mathbb{C}[A]$ which is isomorphic to $QH_{1}(G_{k,n})$ through an isomorphism $T:QH_{1}(G_{k,n})\rightarrow\mathcal{A}$ such that $T(s_{\lambda})e_{I_0}=e_{I_{\lambda}}$ and $T(s_{(1)})=A$.

As a consequence $B_{k,n}$ is a PM-graph rooted at $I_0$.
:::

::: proof
*Proof.* Remark first that since $\dim L^2(B_{k,n})=\vert B_{k,n}\vert=\binom nk$, for any commutative subalgebra $\mathcal{A}$ of $\mathcal{B}(L^2(B_{k,n}))$ we have $\dim \mathcal{A}\leq \binom nk$. Recall that we defined $$QH_1(G_{k,n})=Sym[x_1,\ldots,x_k]/\langle (x_1,\ldots,x_k)=\left(e^{it_1},\ldots e^{it_k}\right), \vec{t}\in T_{k,n}\rangle.$$ Since $T_{k,n}$ has cardinal $\binom nk$ and the map $(t_1,\ldots,t_k)\mapsto\left(e^{it_1},\ldots e^{it_k}\right)$ is injective on $T_{k,n}$, $QH_1(G_{k,n})$ is isomorphic to the space of functions on $\binom nk$ elements and thus $\dim QH_1(G_{k,n})=\binom nk$. Since $QH_1(G_{k,n})$ is spanned by $\{s_{\lambda}\}_{\lambda\in \Lambda_{k,n}}$, by a dimension argument the latter set is actually a basis of $QH_1(G_{k,n})$. Recall that $\ell:QH_1(G_{k,n})\rightarrow L^2(B_{k,n})$ is the isomorphism sending $s_\lambda$ to $e_{I_{\lambda}}$, and define $T:QH_1(G_{k,n})\rightarrow \mathcal{B}(L^2(B_{k,n}))$ by $$T(x)e_{I}=\ell(x\ell^{-1}(e_I)),\,x\in QH_1(G_{k,n}),\,  I\in B_{k,n}.$$ Then, $T$ is an injective morphism of algebra, since it can be written as the composition of the multiplication map $m:QH_1(G_{k,n})\rightarrow \mathcal{B}(QH_1(G_{k,n}))$ with the conjugation map $C_{\ell}:\mathcal{B}(QH_1(G_{k,n}))\rightarrow \mathcal{B}(L^2(B_{k,n}))$ given by $M\mapsto \ell\circ M\circ \ell^{-1}$, both maps being injective morphisms of algebras. Since $QH_{1}(G_{k,n})$ is commutative, $T(QH_{1}(G_{k,n}))$ is a commutative subalgebra of $\mathcal{B}(L^2(B_{k,n}))$.

Since $\ell^{-1}(e_{I})=s_{\lambda_I}$, we have $$T(s_{(1)})e_{I}=\ell(s_{(1)}s_{\lambda_{I}}).$$ The multiplication by $s_{(1)}$ in $QH(G_{k,n})$ is given by the quantum Pieri rule [@BCF Eq. (22)], which gives for $\lambda\in \Lambda_{k,n}$ after specializing $q=1$ $$s_{(1)}s_{\lambda}=\sum_{\lambda\nearrow \mu}s_{\mu}+\delta_{\lambda_1=n-k,\lambda_k>0}qs_{\tilde{\lambda}}=\sum_{\lambda\nearrow \mu}s_{\mu}+\delta_{\lambda_1=n-k,\lambda_k>0}s_{\tilde{\lambda}},$$ where $\tilde{\lambda}=(\lambda_2-1,\ldots,\lambda_k-1,0)$. Hence, by Lemma [\[lem:equivalence_graph_pieri\]](#lem:equivalence_graph_pieri){reference-type="ref" reference="lem:equivalence_graph_pieri"}, $s_{(1)}s_{\lambda}=\sum_{I_{\lambda}\nearrow I}s_{\lambda_{I}}$, which yields for $I\in B_{k,n}$ $$T(s_{(1)})e_{I}=\ell(s_{(1)}s_{\lambda_{I}})=\sum_{I\nearrow J}\ell(s_{\lambda_{J}})=\sum_{I\nearrow J}e_{J},$$ and finally $T(s_{(1)})=A$, so that $\mathbb{C}[A]\subset T(QH_{1}(G_{k,n}))$.

For all $I\in B_{k,n}$, $$T(s_{\lambda_I})e_{I_0}=\ell(s_{\lambda_I}s_{\emptyset})=\ell(s_{\lambda_I})=e_{I},$$ which implies that the map $T(QH_{1}(G_{k,n}))\rightarrow L^2(B_{k,n})$ given by $x\mapsto x(e_{I_0})$ is injective. Then, since $$\left[AT(s_{\lambda_I})\right]e_{I_0}=Ae_{I}=\sum_{I\nearrow J}e_{J}=\left(\sum_{I\nearrow J} T(s_{\lambda_J})\right)e_{I_0},$$ we deduce that $$AT(s_{\lambda_I})=\sum_{I\nearrow J} T(s_{\lambda_J})=\sum_{J\in B_{k,n}}A_{JI} T(s_{\lambda_J}).$$ Finally, by [\[eq:multiplication_quantum\]](#eq:multiplication_quantum){reference-type="eqref" reference="eq:multiplication_quantum"}, for all $\lambda,\mu \in \Lambda_{k,n}$ we have $$T(s_{\lambda})T(s_{\mu})=T(s_{\lambda}s_{\mu})=\sum_{d\geq 0,\nu\in \Lambda_{k,n}}\langle\lambda,\mu,\nu^c\rangle_dT(s_{\nu})$$ with each term $\langle\lambda,\mu,\nu^c\rangle_d\geq 0$.

By the previous results, $B_{k,n}$ is a PM-graph whose enveloping algebra is $\mathcal{A}=T(QH_1(G_{k,n}))$ and the corresponding basis is $\{T(s_{\lambda_I}),I\in B_{k,n}\}$. ◻
:::

As a consequence of the latter result and the presentation of $QH_1(G_{k,n})$, we will prove that $B_{k,n}$ is an integrable PM-graph. Let us simply write $A_{I}=T(s_{\lambda_I})$. In the case of $B_{k,n}$, there is a natural indexation of left and right common eigenvectors of $\{A_I\}_{I\in B_{k,n}}$ by the set $B_{k,n}$ itself. We do not known if such natural indexation holds for any integrable PM-graph. As we will see in the next proposition, we are in the particular case where the adjacency matrix $A$ is normal, so that left and right eigenvectors $u^{(I)}$ and $w^{(I)}$, $I\in B_{k,n}$ of all operators $A_{I}$ coincide up to a constant, see [\[eq:normal_adjacency\]](#eq:normal_adjacency){reference-type="eqref" reference="eq:normal_adjacency"}. For $I\in B_{k,n}$, set $$\label{eq:def_vI}
w^{(I)}=\sum_{J\in B_{k,n}}\overline{S_{J}(\xi_{n}(I))}e_{J},$$ where $S_J(\vec{u})=s_{\lambda_J}\left(e^{iu_1},\ldots,e^{iu_k}\right)$ for $\vec{u}\in \mathbb{R}^k$, and let $V(u_1,\ldots,u_k)=\prod_{j<j'}\left(e^{iu_{j'}}-e^{iu_{j}}\right)$ be the Vandermonde determinant of $\left(e^{iu_j}\right)_{1\leq j\leq k}$.

::: lemma
[]{#lem:action_s_mu label="lem:action_s_mu"} The set $\{w^{(I)}\}_{I\in B_{k,n}}$ is an orthogonal basis of $L^2(B_{k,n})$, and for all $J\in B_{k,n}$, $$A_{J}(w^{(I)})=S_{J}(\xi_{n}(I))w^{(I)}\quad
\text{   and    } \quad A_{J}^*(w^{(I)})=\overline{S_{J}(\xi_{n}(I))}w^{(I)}.$$
:::

::: proof
*Proof.* The orthogonality relation is given by the following Cauchy type formula from [@Ri Proposition 4.3]: for $I,I'\in B_{k,n}$, $$\label{eq:first_ortho_rietsch}
\sum_{J \in B_{k,n}}S_{J}(\xi_{n}(I))\overline{S_{J}(\xi_{n}(I'))}=\delta_{I,I'}\frac{n^k}{\vert V(\xi_{n}(J))\vert^2},$$ which directly yields $$\begin{aligned}
\langle w^{(I)},w^{(I')}\rangle=&\delta_{I,I'}\frac{n^k}{\vert V(\xi_{n}(J))\vert^2}\label{eq:orthogonality_relation}
\end{aligned}$$ for $I,I'\in B_{k,n}$.

To prove the eigenvector property, it is easier to work on $QH_1(B_{k,n})$. Indeed, by Proposition [\[prop:equiv_graph_qh\]](#prop:equiv_graph_qh){reference-type="ref" reference="prop:equiv_graph_qh"}, it suffices to prove that $s_{\lambda_{J}}\cdot\ell^{-1}(w^{(I)})=S_{J}(\xi_{n}(I))\ell^{-1}(w^{(I)})$, where $\cdot$ denotes the product in $QH_{1}(G_{k,n})$. From the proof of Proposition [\[prop:equiv_graph_qh\]](#prop:equiv_graph_qh){reference-type="ref" reference="prop:equiv_graph_qh"}, $QH_{1}(B_{k,n})$ is the space of functions on $\mathcal{Z}_{k,n}=\{\exp(i\vec{u}), \vec{u}\in T_{k,n}\}$, where $\exp(i\vec{u})=\left(e^{iu_1},\ldots,e^{iu_k}\right)$ for $\vec{u}\in \mathbb{R}^k$. Hence, we need to show that the values of $s_{\lambda_{J}}\cdot\ell^{-1}(w^{(I)})$ and $S_{J}(\xi_{n}(I))\ell^{-1}(w^{(I)})$ agree on $\mathcal{Z}_{k,n}$. First, we have by the usual evaluation of multiplication of functions $$\begin{aligned}
\left[s_{\lambda_{J}}\cdot\ell^{-1}\left(w^{(I)}\right)\right](\exp(i\xi_{n}(I)))=&s_{\lambda_{J}}(\exp(i\xi_{n}(I)))\left[\ell^{-1}\left(w^{(I)}\right)\right](\exp(i\xi_{n}(I)))\\
=&\left[S_{J}(\xi_{n}(I))\ell^{-1}(w^{(I)})\right](\exp(i\xi_{n}(I))).
\end{aligned}$$ Then, for $I'\not=I$, $$\begin{aligned}
&\left[s_{\lambda_{J}}\cdot\ell^{-1}(w^{(I)})\right](\exp(i\xi_{n}(I')))-\left[S_{J}(\xi_{n}(I))\ell^{-1}(w^{(I)})\right](\exp(i\xi_{n}(I')))\\
&\hspace{3cm}=\left(S_{J}(\xi_{n}(I'))-S_{J}(\xi_{n}(I))\right)\left[\sum_{J'\in B_{k,n}}\overline{S_{J'}(\xi_{n}(I))} s_{\lambda_{J'}}\right](\exp(i\xi_{n}(I')))\\
&\hspace{3cm}=\left(S_{J}(\xi_{n}(I'))-S_{J}(\xi_{n}(I))\right)\sum_{J'\in B_{k,n}}\overline{S_{J'}(\xi_{n}(I))} S_{J'}(\xi_{n}(I'))=0
\end{aligned}$$ by [\[eq:orthogonality_relation\]](#eq:orthogonality_relation){reference-type="eqref" reference="eq:orthogonality_relation"}. Hence, we deduce that $s_{\lambda_{J}}\cdot\ell^{-1}(w^{(I)})=S_{J}(\xi_{n}(I))\ell^{-1}(w^{(I)})$, and the result is deduced by applying $\ell$. Since $A_{J}$ is diagonalized on an orthogonal basis, it is actually normal and we thus have $$A_{J}^*\left(w^{(I)}\right)= \overline{S_{J}(\xi_{n}(I))}w^{(I)}.$$ ◻
:::

Note that as a corollary of [\[eq:orthogonality_relation\]](#eq:orthogonality_relation){reference-type="eqref" reference="eq:orthogonality_relation"}, we have $$\Vert w^{(I)}\Vert_2=\frac{n^{k/2}}{\vert V(\xi_{n}(I))\vert}.$$ Hence, following the notation of Section [\[sec:pm_graph\]](#sec:pm_graph){reference-type="ref" reference="sec:pm_graph"}, we set $$\label{eq:def_uI_Bkn}
u^{(I)}=\frac{\vert V(\xi_{n}(I))\vert^2}{n^k}w^{(I)},$$ so that $\langle w^{(I)},u^{(J)}\rangle=\delta_{IJ}$.
