---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-012-4-nonabelian-poincaré-duality
section_title: "Nonabelian Poincaré duality"
section_number: 4
pages: 26-28
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.98
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
Applying Theorem [\[homology\]](#homology){reference-type="ref" reference="homology"}, we offer a slightly different perspective, and proof, of the nonabelian Poincaré duality of Salvatore [@salvatore], Segal [@segallocal], and Lurie [@dag], which calculate factorization homology with coefficients in iterated loop spaces as a compactly supported mapping space.

::: definition
For a space $B$, the $\infty$-category $\mathop{\mathrm{\sf Spaces}}_B$ is that of retractive spaces over $B$. The $\mathop{\mathrm{\infty}}$-category $\mathop{\mathrm{\sf Spaces}}^{\geq n}_B$ is the full $\mathop{\mathrm{\infty}}$-subcategory of $\mathop{\mathrm{\sf Spaces}}_B$ consisting of those $X\rightleftarrows B$ for which the retraction is $n$-connective, that is, $\pi_* X \rightarrow\pi_* B$ is an isomorphism for $*< n$ with any choice of base-point of $B$.
:::

Equivalently, an object $X\in \mathop{\mathrm{\sf Spaces}}_B^{\geq n}$ may be thought of as a fibration $X\rightarrow B$ with a distinguished section for which, for each $b\in B$, the fiber $X_b$ is $n$-connective.

::: definition
For $X\in \mathop{\mathrm{\sf Spaces}}_B$ and $M \rightarrow B$ a space over $B$, the space $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M,X)$ of compactly supported sections of $X$ over $M$ is the subspace of $\mathop{\mathrm{\sf Map}}_{/B}(M,X)$ consisting of those maps $f\colon M\to X$ over $B$ for which there is a compact subspace $K\subset M$ with the property that the restriction factors through the section: $f_{|M\smallsetminus K} : M \to B\to X$.
:::

For $B\rightarrow\mathop{\mathrm{\sf BTop}}(n)$ as before, note that $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(-,X)$ defines a covariant functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B \rightarrow\mathop{\mathrm{\sf Spaces}}$. By inspection, this functor carries finite disjoint unions to finite products of spaces, which is to say that $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(-,X)$ is symmetric monoidal with respect to the Cartesian monoidal structure on the $\infty$-category of spaces.

To easily state the next result, Theorem [\[spaces\]](#spaces){reference-type="ref" reference="spaces"}, we introduce some terminology. Each point $g\in B$ determines a symmetric monoidal functor $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\mathop{\mathrm{\sf fr}}} \to \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$. Thereafter, each symmetric monoidal functor $A\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \to \mathop{\mathrm{\mathsf{Spaces}}}$ determines the associative monoid $$\pi_0(A,g)\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_1^{\mathop{\mathrm{\sf fr}}} \xrightarrow{\mathbb R^{n-1}\times -} \mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\mathop{\mathrm{\sf fr}}} \longrightarrow \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \xrightarrow{~A~} \mathop{\mathrm{\mathsf{Spaces}}}\xrightarrow{~\pi_0~} {\sf Set} ~.$$ We say $A$ is *group-like* if, for each $g\in B$, this monoid $\pi_0(A,g)$ is a group.

::: example
In the case $B\simeq \ast$ so that a $B$-framing is a framing in the standard sense, a symmetric monoidal functor $A\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\sf fr} \to \mathop{\mathrm{\mathsf{Spaces}}}$ is the data of an $\mathcal E_n$-algebra, and this $\mathcal E_n$-algebra is group-like in the standard sense if and only if $A$ is group-like in the the sense just above.
:::

::: theorem
[]{#spaces label="spaces"} The functor $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}: \mathop{\mathrm{\sf Spaces}}_B \rightarrow\mathop{\mathrm{\sf Fun}}^\otimes(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B, \mathop{\mathrm{\sf Spaces}})$ restricts as a fully faithful functor $$\mathop{\mathrm{\sf Spaces}}_B^{\geq n} ~\hookrightarrow~ \mathbf H(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathop{\mathrm{\sf Spaces}})$$ from $n$-connective retractive spaces over $B$ to homology theories. The essential image consists of those $\mathcal F$ for which the restriction $\mathcal F_{|\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B}$ is group-like.
:::

The following is the core technical detail in the proof of Theorem [\[spaces\]](#spaces){reference-type="ref" reference="spaces"}, that the assignment of compactly supported sections $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(-,X)$ is $\otimes$-excisive in our sense, provided the retraction $X\rightarrow B$ is sufficiently connected. The fullness of the functor above is a parametrized form of May's theorem from [@may], identifying $n$-connective objects as $\mathop{\mathrm{{\mathcal D}\sf isk}}^{\mathop{\mathrm{\sf fr}}}_n$-algebras, which is Theorem 5.1.3.6 of [@dag].  

::: lemma
[]{#gamma-c label="gamma-c"} Let $M$ be $B$-framed manifold, equipped with a collar-gluing $M'\underset{M_0\times\mathbb R}\bigcup M''\cong M$. Let $X\in \mathop{\mathrm{\sf Spaces}}^{\geq n}_B$ be an $n$-connective space over $B$. There is a natural weak homotopy equivalence $$\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X)\underset{\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0\times\mathbb R,X)}\times\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)~\simeq~\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M, X)$$ between the quotient of the product $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X)\times\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)$ by the diagonal action of $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0\times\mathbb R,X)$ and the space of compactly supported sections of $X$ over $M$.
:::

::: proof
*Proof.* Since $M_0\hookrightarrow M$ is a proper embedding, a compactly supported section over $M$ can be restricted to obtain a compactly supported section over $M_0$, as well as over $M\smallsetminus M'$ and over $M\smallsetminus M''$. Namely, there is a diagram among spaces of compactly supported sections $$\xymatrix{
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X) \times \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)  \ar[dr]  \ar[rr]  \ar[dd]
&
&
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)  \ar[d]
\\
&
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M,X)  \ar[r]  \ar[d]  \ar[dr]
&
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M\smallsetminus M',X)  \ar[d]
\\
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X)  \ar[r]
&
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M\smallsetminus M'',X)  \ar[r]
&
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X).
}$$ By inspection, the bottom horizontal sequence is a fiber sequence, as is the right vertical sequence, as is the diagonal sequence. Also, the inner square is pullback because $M'\underset{M_0\times \mathbb R}\bigcup M''\cong M$ is a pushout. Because $M_0\subset M$ is equipped with a regular neighborhood, these fiber sequences are in fact Serre fibration sequences, and so the inner square is a weak homotopy pullback square. In particular, there is a right homotopy coherent action of $\Omega \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X)$ on $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X)$, a left homotopy coherent action of $\Omega \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X)$ on $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)$, and a continuous map of topological spaces $$\label{gammas}
\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M',X)\underset{\Omega \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X)} \times \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M'',X)\longrightarrow \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M,X)$$ from the balanced homotopy coinvariants. Because $X\to B$ is $n$-connective and $M_0$ is $(n-1)$-dimensional, the base $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X)$ is connected. It follows that the map ([\[gammas\]](#gammas){reference-type="ref" reference="gammas"}) is in fact a weak homotopy equivalence. The assertion follows after the canonical identification $\Omega \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0,X) \cong \mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M_0\times \mathbb R,X)$ as group-like $\mathcal E_1$-spaces. ◻
:::

As a consequence, we recover the following theorem of Salvatore [@salvatore], Segal [@segallocal], and Lurie [@dag].

::: cor
[]{#non-abel label="non-abel"} For any $X$ in $\mathop{\mathrm{\sf Spaces}}_B^{\geq n}$, with associated $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n$-algebra $\Omega_B^nX\in \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n}(\mathop{\mathrm{\sf Spaces}})$, there is a natural equivalence $$\int_M \Omega_B^n X ~ \simeq ~\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(M,X)$$ between the factorization homology of a $B$-framed $n$-manifold $M$ with coefficients in $\Omega^n_{B}X$ and the space of compactly supported sections of $X$ over $M$.
:::

::: proof
*Proof.* We apply Theorem [\[homology\]](#homology){reference-type="ref" reference="homology"}: Since $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(-,X)$ is a homology theory, it is equivalent to factorization homology with coefficients in $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(\mathbb R^n,X)$, which is identified as the $n$-fold loop space of the fiber of the map $X\rightarrow B$, $\mathop{\mathrm{{\Gamma}_{\!\sf c}}}(\mathbb R^n,X)\simeq \Omega^n_BX$. ◻
:::

This result specializes to Poincaré duality between twisted homology and compactly supported cohomology, as we will now explain. Given $X\simeq \mathop{\mathrm{\sf BTop}}(n)\times K(A,i)$ a product with an Eilenberg-MacLane space, then $\Omega^n_{\mathop{\mathrm{\sf BTop}}(n)} X \simeq \mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n, K(A,i)) \simeq K(A,i-n)$ is an $n$-disk algebra in spaces, where the multiplication is the usual group structure on $K(A,i-n)$ but is equipped with a nontrivial action of $\mathop{\mathrm{\mathsf{Top}}}(n)$. We then have an equivalence of spaces $$\int_M \mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n, K(A,i)) \simeq \mathop{\mathrm{{\sf Map}_{\sf c}}}(M,K(A,i))$$ which is the space level version of the equivalence $\mathsf H_*^\tau(M,A[i-n])\simeq \mathsf H^*_{\sf c}(M, A[i])$, obtained by applying $\Omega^\infty$ to the spectrum level equivalence given by Atiyah duality. Given an $A$-orientation of $M$, then one can additionally untwist the lefthand side, as usual.

::: remark
The factorization homology $\int_M\Omega^n_BX$ is built from configuration spaces of disks in $M$ with labels defined by $X\to B$, and the preceding result thereby has roots in the configuration space models of mapping spaces dating to the work of Segal, May, McDuff and others in the 1970s, see [@segal], [@may], [@mcduff], and [@bodig]. Factorization homology is not a generalization of the classical configuration spaces with labels, as described in [@bodig], because the configuration space with labels in $X$ models a mapping space with target the $n$-fold suspension of $X$, rather than into $X$ itself. Instead, factorization homology generalizes the configuration spaces with *summable* or *amalgamated* labels of Salvatore [@salvatore] and Segal [@segallocal].
:::

::: proof
*Proof of Theorem [\[spaces\]](#spaces){reference-type="ref" reference="spaces"}.* Corollary [\[non-abel\]](#non-abel){reference-type="ref" reference="non-abel"} identifies the functor $\Gamma_{\sf c} \colon \mathop{\mathrm{\mathsf{Spaces}}}_B^{\geq n} \to  \mathbf H(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathop{\mathrm{\sf Spaces}})$ as the composition $\Gamma_{\sf c} \colon \mathop{\mathrm{\mathsf{Spaces}}}_B^{\geq n} \xrightarrow{\Omega^n_B} \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \xrightarrow{\int}  \mathbf H(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B,\mathop{\mathrm{\sf Spaces}})$. Theorem [\[homology\]](#homology){reference-type="ref" reference="homology"} gives that $\int$ is fully faithful, so it remains to argue that $\Omega_B^n$ is fully faithful with essential image the group-like $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$-algebras in spaces. This is immediate because, for instance, $\mathop{\mathrm{\mathsf{Spaces}}}_{/B}$ is an $\infty$-topos (Theorem 5.1.3.6 of [@dag]). ◻
:::
