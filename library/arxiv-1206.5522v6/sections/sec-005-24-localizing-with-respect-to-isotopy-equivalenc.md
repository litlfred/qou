---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-005-24-localizing-with-respect-to-isotopy-equivalenc
section_title: "Localizing with respect to isotopy equivalences"
section_number: 2.4
pages: 12-14
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.97
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
Here we explain that the $\infty$-category $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$ is a localization of its un-topologized version $\mathop{\mathrm{{\sf Disk}}}^B_{n/M}$ on the collection of those inclusions of finite disjoint unions of disks $U\subset V$ in $M$ that are isotopic to an isomorphism. This comparison plays a fundamental role in recognizing certain colimit expressions in this theory, for instance those that support the pushforward formula of §[\[sec.push\]](#sec.push){reference-type="ref" reference="sec.push"}.

::: definition
[]{#def.ddisk label="def.ddisk"} The ordinary symmetric monoidal category $\mathop{\mathrm{\mathsf{Mfld}}}_n$ is that for which an object is a topological $n$-manifold, and a morphism is an open embedding between two such; composition is composition of maps, and the symmetric monoidal structure is given by disjoint union. Likewise, the ordinary symmetric monoidal category $\mathop{\mathrm{{\sf Disk}}}_n\subset \mathop{\mathrm{\mathsf{Mfld}}}_n$ is the full subcategory consisting of those topological $n$-manifolds that are homeomorphic to a finite disjoint union of Euclidean spaces.
:::

Notice the natural functors $$\mathop{\mathrm{{\sf Disk}}}_n \longrightarrow \mathop{\mathrm{{\mathcal D}\sf isk}}_n\qquad \text{ and }\qquad  \mathop{\mathrm{\mathsf{Mfld}}}_n \longrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$$ which are symmetric monoidal. We denote the pullback symmetric monoidal $\infty$-categories $$\xymatrix{
\mathop{\mathrm{{\sf Disk}}}_n^B  \ar[d]  \ar[r]  
&
\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B  \ar[d]
&&
\mathop{\mathrm{\mathsf{Mfld}}}_n^B \ar[r]  \ar[d]
&
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B  \ar[d]
\\
\mathop{\mathrm{{\sf Disk}}}_n  \ar[r]
&
\mathop{\mathrm{{\mathcal D}\sf isk}}_n
&\text{ and }&
\mathop{\mathrm{\mathsf{Mfld}}}_n \ar[r]
&
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n.
}$$ For each topological $n$-manifold $M$, we denote the $\infty$-subcategory $$\label{eqn.I_X}
\mathcal I_M~\subset ~\mathop{\mathrm{{\sf Disk}}}^B_{n/M}:= \mathop{\mathrm{{\sf Disk}}}_n^B \underset{\mathop{\mathrm{\mathsf{Mfld}}}_n^B}\times \mathop{\mathrm{\mathsf{Mfld}}}^B_{n/M}$$ consisting of the same objects but only those morphisms $(U\hookrightarrow M) \hookrightarrow (V\hookrightarrow M)$ whose image in $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$ is an equivalence.

::: prop
[]{#EEd-vs-EE label="EEd-vs-EE"} The functor $\mathop{\mathrm{{\sf Disk}}}^B_{n/M} \longrightarrow \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$ witness a localization of $\infty$-categories: $$\bigl(\mathop{\mathrm{{\sf Disk}}}^B_{n/M}\bigr)[\mathcal I_M^{-1}]~\simeq~\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}~.$$
:::

::: proof
*Proof.* Manifestly, the functor is essentially surjective, and it carries the $\infty$-subcategory $\mathcal I_M$ to the maximal $\infty$-subgroupoid $\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}\bigr)^\sim$. There results a functor $\bigl(\mathop{\mathrm{{\sf Disk}}}^B_{n/M}\bigr)[\mathcal I_M^{-1}]\to \mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$ from the localization. We will argue that this functor is an equivalence by showing it is an equivalence on maximal $\infty$-subgroupoids, then that it is an equivalence on spaces of morphisms. After Lemma [\[slice-slice\]](#slice-slice){reference-type="ref" reference="slice-slice"}, it is enough to consider the case of $B=\mathop{\mathrm{\sf BTop}}(n)$. We will adopt the following notation for this proof: $$\mathsf D_M~:=~\mathop{\mathrm{{\sf Disk}}}_{n/M} \qquad\text{ and }\qquad \mathcal D_M~:=~\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}~.$$

The maximal $\infty$-subgroupoid of $\mathsf D_M$ is the classifying space $\mathsf B\mathcal I_M$. In light of the coproduct expression in Lemma [\[EE-equivs\]](#EE-equivs){reference-type="ref" reference="EE-equivs"}, fix a cardinality $i\geq 0$. Consider the full subcategory $\mathcal I_M^{i}\subset \mathcal I_M$ consisting of those $(U\hookrightarrow M)$ for which the cardinality of the connected components $|[U]|=i$. We thus seek to show that the resulting functor $\mathcal I_M^{i} \to \mathop{\mathrm{\mathsf{Conf}}}_i(M)_{\Sigma_i}$ witnesses an equivalence from the classifying space. We explain the following sequence of weak homotopy equivalences $$\begin{aligned}
\nonumber
\mathsf B\mathcal I^{i}_M
&
\simeq
&
\underset{(U\hookrightarrow M)\in \mathcal I^{i}_M} \mathop{\mathrm{\sf colim}}~ (\mathbb R^n)^i
\\
\nonumber
&
\xrightarrow{\simeq}
&
\underset{(U\hookrightarrow M)\in \mathcal I^{i}_M} {\sf p.s.colim}~ (\mathbb R^n)^i
\\
\nonumber
&
\xrightarrow{\cong}
&
\mathop{\mathrm{\mathsf{Conf}}}_{i}(M)_{\Sigma_{i}}
\end{aligned}$$ where ${\sf p.s.colim}$ denotes the ordinary point-set colimit of topological spaces. The first equivalence is formal, because each term in the homotopy colimit is contractible. By inspection, the category $\mathcal I_M^i$ forms a basis for the standard Grothendieck topology on $\mathop{\mathrm{\mathsf{Conf}}}_{i}(M)_{\Sigma_{i}}$. The third homeomorphism follows. Because $\mathop{\mathrm{\mathsf{Conf}}}_i(M)_{\Sigma_i}$ is paracompact, Corollary 1.6 of [@dugger-isaksen] gives that the second map is a weak homotopy equivalence. In summary, we have verified that the map of maximal $\infty$-subgroupoids $$\bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{\sim} \xrightarrow{~\simeq~} \bigl(\mathcal D_M\bigr)^{\sim}$$ is an equivalence.

We now show that the functor from the localization induces an equivalence on spaces of morphisms. Consider the diagram of spaces $$\xymatrix{
\bigl(\mathsf D_U[\mathcal I_U^{-1}]\bigr)^{\sim}  \ar[r]  \ar[d]_-{(U\hookrightarrow M)}
&
\mathcal D_U^{\sim}  \ar[d]^-{(U\hookrightarrow M)}
\\
\bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{(1)} \ar[r]  \ar[d]_-{{\sf ev}_1}
&
\mathcal D_M^{(1)}  \ar[d]^-{{\sf ev}_1}
\\
\bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{\sim}  \ar[r]
&
\mathcal D_M^{\sim}
}$$ where a superscript ${}^{(1)}$ indicates a space of morphisms, and the upper vertical arrows are given as $(V\hookrightarrow U)\mapsto \bigl((V\hookrightarrow M)\hookrightarrow (U\hookrightarrow M)\bigr)$. Our goal is to show that the middle horizontal arrow is an equivalence. We will accomplish this by showing that the diagram is a map of homotopy fiber sequences, for we have already shown that the top and bottom horizontal maps are equivalences.

The right vertical sequence is a fiber sequence is because such evaluation maps are coCartesian fibrations, in general. Then, by inspection, the fiber over $(U\hookrightarrow M)$ is the maximal $\infty$-subgroupoid of the over $\infty$-category $(\mathcal D_M)_{/(U\hookrightarrow M)}$. This over $\infty$-category is canonically identified as $\mathcal D_U$.

We now show that the left vertical sequence is a homotopy fiber sequence. The space of morphisms $\bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{(1)}$ is the classifying space of the subcategory of the functor category $\mathop{\mathrm{\sf Fun}}^{\mathcal I_M}\bigl([1],\mathsf D_M\bigr) \subset \mathop{\mathrm{\sf Fun}}\bigl([1],\mathsf D_M\bigr)$ consisting of the same objects but only those natural transformations by $\mathcal I$. We claim the fiber over $(U\hookrightarrow M)$ of the evaluation map is canonically identified as in the sequence $$\bigl(\mathsf D_U[\mathcal I_U^{-1}]\bigr)^{\sim} \xrightarrow{~(U\hookrightarrow M)~}\bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{(1)} \xrightarrow{~{\sf ev}_1~} \bigl(\mathsf D_M[\mathcal I_M^{-1}]\bigr)^{\sim}~.$$ This claim is justified through Quillen's Theorem B, for the named fiber is the classifying space of the over $\infty$-category $(\mathcal I_M)_{/(U\hookrightarrow M)}$ which is canonically isomorphic to $\mathcal I_U$. To apply Quillen's Theorem B we must show that each morphism $(U\hookrightarrow M) \hookrightarrow (V\hookrightarrow M)$ in $\mathcal I$ induces an equivalence of spaces $\mathsf B\bigl((\mathcal I_M)_{/(U\hookrightarrow M)}\bigr) \simeq \mathsf B\bigl((\mathcal I_M)_{/(V\hookrightarrow M)}\bigr)$. This map of spaces is canonically identified as the map $\mathsf B\mathcal I_U \to \mathsf B\mathcal I_V$ induced from the inclusion $U\hookrightarrow V$, which, by design, is a bijection on connected components. Through the previous analysis of this proof, this map is further identified as the map of spaces $U\hookrightarrow V$. The Kister--Mazur Theorem [\[kister\]](#kister){reference-type="ref" reference="kister"} implies this inclusion $U\hookrightarrow V$ is isotopic to an isomorphism, from which it follows that the map of spaces $\mathsf B\mathcal I_U \xrightarrow{\simeq} \mathsf B\mathcal I_V$ is an equivalence. We conclude that Quillen's Theorem B applies. (For an $\infty$-categorical account of Quillen's Theorem B, see for instance Theorem 5.3 of [@barwick].) ◻
:::

::: remark
Proposition [\[EEd-vs-EE\]](#EEd-vs-EE){reference-type="ref" reference="EEd-vs-EE"} implies that, for each symmetric monoidal $\infty$-category $\mathcal V$, the restriction functor $\mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}(\mathcal V) \to \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\sf Disk}}}_n^B}(\mathcal V)$ is fully faithful and the essential image consists of the *locally constant* $\mathop{\mathrm{{\sf Disk}}}_n^B$-algebras. This result also appears in [@dag] as Theorem 5.4.5.9.
:::

Proposition [\[EEd-vs-EE\]](#EEd-vs-EE){reference-type="ref" reference="EEd-vs-EE"} offers the following construction.

::: construction
[]{#def.f-inverse label="def.f-inverse"} Let $f\colon M \to N$ be a continuous map from a $B$-framed $n$-manifold to a $B'$-framed $k$-manifold, possibly with boundary. Given a regularity condition on $f$, we will produce a composite map of colored operads $$f^{-1} \colon \mathop{\mathrm{{\sf Disk}}}^{\partial, B'}_{k/N} \longrightarrow \mathop{\mathrm{\mathsf{Mfld}}}^B_{n/M} \longrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_{n/M}~.$$ The second functor is the standard one. To describe the first functor we make use of Lemma [\[slice-slice\]](#slice-slice){reference-type="ref" reference="slice-slice"} so that we can assume the maps $B\rightarrow\mathop{\mathrm{\sf BTop}}(n)$ and $B'\rightarrow\mathop{\mathrm{\sf BTop}}(k)$ are equivalences. For this case, the first functor is given by $(U\hookrightarrow N)\mapsto (U\underset{N}\times M \hookrightarrow M)$, which is evidently functorial as well as monoidal.

Suppose the two restrictions $$f_|\colon f^{-1}(N\smallsetminus \partial N) \to N\smallsetminus \partial N\qquad \text{ and }\qquad f_|\colon f^{-1}(\partial N) \to \partial N$$ are manifold bundles. Then, by inspection, this functor $f^{-1}$ carries isotopy equivalences to equivalences. Through Proposition [\[EEd-vs-EE\]](#EEd-vs-EE){reference-type="ref" reference="EEd-vs-EE"}, there results a multi-functor $$\label{f-inv}
f^{-1} \colon \mathop{\mathrm{{\mathcal D}\sf isk}}^{B'}_{k/N} \longrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_{n/M}~.$$
:::
