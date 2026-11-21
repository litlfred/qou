---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-011-53-classification-by-cech-cohomology
section_title: "Classification by Cech Cohomology"
section_number: 5.3
pages: 31-33
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.942
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
In this section we prove that Versions I (\v Cech $\Gamma$-1-cocycles) and III ($\Gamma$-bundle gerbes) are equivalent. For this purpose, 
we extract a \v Cech cocycle from a $\Gamma$-bundle gerbe $\mathcal{G}$ over $M$, and prove that this procedure defines a bijection on the level of equivalence classes (Theorem \ref{th:gerbesclass}). First we have to ensure the existence of appropriate open covers.

\begin{lemma}
\label{lem:goodcover}
For every $\Gamma$-bundle gerbe $\mathcal{G}=(Y,P,\mu)$ over $M$ there exists an open cover $\mathscr{U}=\left \lbrace U_i \right \rbrace_{i\in I}$ of $M $with sections $\sigma_i : U_i \to Y$, such that the principal $\Gamma$-bundles $(\sigma_{i} \times \sigma_j)^{*}P$ over $U_i \cap U_j$ are trivializable. \end{lemma}

\begin{proof}
One can choose an open cover such that the 2-fold intersections $U_i \cap U_j$ are contractible. Since every Lie 2-group is a crossed module $\act GH$ (Remark \ref{rem:crossedmodule}), and $\act GH$-bundles are ordinary $H$-bundles (Lemma \ref{actionbundles}), these  admit sections over contractible smooth manifolds. But a section is enough to trivialize the original $\Gamma$-bundle (Lemma \ref{lem:loctriv}).
\end{proof}


Let $\mathcal{G}$ be a $\Gamma$-bundle gerbe over $M$, and let $\mathscr{U} = \left \lbrace U_i \right \rbrace_{i\in I}$ be an open cover with the properties of Lemma \ref{lem:goodcover}. We denote by $M_\mathscr{U}$ the disjoint union of all the open sets $U_i$, and by $\sigma:M_{\mathscr{U}} \to Y$ the union of the sections $\sigma_i$. Then, $\sigma$ is a refinement of $\pi:Y \to M$, and we have a $\Gamma$-bundle gerbe $\mathcal{G}_{\mathscr{U},\sigma}$ that is isomorphic to $\mathcal{G}$ (Proposition \ref{prop:pullback}). 

The principal $\Gamma$-bundle $P_{ij}$ of $\mathcal{G}_{\mathscr{U},\sigma}$ over the component $U_i \cap U_j$ is by assumption trivializable. Thus there exists a trivialization
$t_{ij}: P_{ij} \to \trivlin_{f_{ij}}$
for  smooth functions $f_{ij}:U_i \cap U_j \to \Gamma_0$. We define an isomorphism $\mu_{ijk}$ between trivial bundles such that the diagram
\begin{equation*}
\alxydim{@=1.3cm}{P_{jk} \otimes P_{ij} \ar[r]^-{\mu} \ar[d]_{t_{jk} \otimes t_{ij}} & P_{ik} \ar[d]^{t_{ik}} \\ \trivlin_{f_{jk}} \otimes \trivlin_{f_{ij}} \ar[r]_-{\mu_{ijk}} & \trivlin_{f_{ik}}}
\end{equation*}
is commutative. Now we are in the situation of Lemma \ref{lem:nonstablemorphisms}, which implies that the $\Gamma$-bundle gerbe $\mathcal{G}_{\mathscr{U},\sigma,t} \df (M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ is still isomorphic to $\mathcal{G}$. 


Combining Lemma \ref{homsets} with Example \ref{ex:tensorproduct} \erf{ex:tensorproduct:trivial}, we see that the  isomorphisms $\mu_{ijk}$ correspond to smooth maps $g_{ijk}:U_i \cap U_j \cap U_k \to \Gamma_1$ such that $s(g_{ijk})=f_{jk} \cdot f_{ij}$ and $t(g_{ijk})=f_{ik}$. The associativity condition for $\mu_{ijk}$ implies moreover that
\begin{equation*}
g_{\alpha\gamma\delta} \circ (g_{\alpha\beta\gamma} \cdot \id_{f_{\gamma \delta}}) = 
g_{\alpha \beta \delta} \circ (\id_{f_{\alpha \beta}} \cdot g_{\beta \gamma \delta})\text{.}
\end{equation*}
Hence, the collection $\left \lbrace f_{ij},g_{ijk} \right \rbrace$ is a $\Gamma$-1-cocycle on $M$ with respect to the open cover $\mathscr{U}$. 

\begin{theorem}
\label{th:gerbesclass}
Let $M$ be a smooth manifold and let $\Gamma$ be a Lie 2-group. The above construction defines a bijection
\begin{equation*}
\bigset{3.7cm}{Isomorphism classes of $\Gamma$-bundle gerbes over $M$} \cong \h^1(M,\Gamma)\text{.}
\end{equation*}
\end{theorem}


\begin{proof}
We claim  that $\Gamma$-bundle gerbes $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ and $(M_{\mathscr{V}},\trivlin_{h_{ij}},\nu_{ijk})$ are isomorphic if and only if the corresponding $\Gamma$-1-cocycles are equivalent. This proves at the same time that the choices of open covers and sections we have made during the construction do not matter,  that the resulting map is well-defined on isomorphism classes, and that this map is injective. Surjectivity follows by assigning to a $\Gamma$-1-cocycle $(f_{ij},g_{ijk})$ with respect to some cover $\mathscr{U}$ the $\Gamma$-bundle gerbe $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ with $\mu_{ijk}$ determined by Lemma \ref{homsets}.

It remains to prove that claim. We assume $\mathcal{A}=(Z,Q,\alpha)$ is a 1-isomorphism between the $\Gamma$-bundle gerbes $(M_{\mathscr{U}},\trivlin_{f_{ij}},\mu_{ijk})$ and $(M_{\mathscr{V}},\trivlin_{h_{ij}},\nu_{ijk})$. Similarly to Lemma \ref{lem:goodcover} one can show that there exists a cover $\mathscr{W}$ of $M$ by open sets $W_i$ that refines both $\mathscr{U}$ and $\mathscr{V}$, and that allows smooth sections $\omega_i:W_i \to Z$ for which the $\Gamma$-bundle $\omega_i^{*}Q$ is trivializable. In the terminology of the above construction, choosing a trivialization $t: \omega^{*}Q \to \trivlin_{h_i}$ with smooth maps $h_i: W_i \to \Gamma_0$ over $M_{\mathscr{W}}$ converts the isomorphism $\alpha$ into smooth functions $s_{ij}: W_i \cap W_j \to \Gamma_1$ satisfying $s(s_{ij}) = g_{ij}' \cdot h_{i}$ and $t(s_{ij}) = h_{j} \cdot g_{ij}$. The compatibility diagram \erf{compgerbemorph} implies the remaining condition that makes $(h_{i},s_{ij})$ an equivalence between the $\Gamma$-2-cocycles $(f_{ij},g_{ijk})$ and $(f_{ij}',g_{ijk}')$.
\end{proof}
