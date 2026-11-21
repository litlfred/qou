---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-002-21-b-framings
section_title: "B-framings"
section_number: 2.1
pages: 6-9
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.972
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We consider a topological category of $n$-manifolds and embeddings among them. We use this to consider the tangent classifier, which thereafter offers the notion of a $B$-framing on an $n$-manifold, as well as an $\infty$-category of such.

::: definition
[]{#manifold label="manifold"} $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ is the symmetric monoidal topological category for which an object is a topological $n$-manifold that admits a finite *good* cover, which is to say a finite open cover by Euclidean spaces with the property that each non-empty intersection of terms in the cover is itself homeomorphic to a Euclidean space. The morphism spaces are spaces of embeddings, endowed with the compact-open topology. The symmetric monoidal structure is disjoint union.[^1]
:::

In particular, the mapping space is $\mathop{\mathrm{\sf Map}}_{\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n}(M,N) =  \mathop{\mathrm{\mathsf{Emb}}}(M,N)$, the space of embeddings of $M$ into $N$ equipped with the compact-open topology. Note that disjoint union is not the coproduct; $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ has almost no nontrivial colimits.

We will be particularly interested in $n$-manifolds equipped with some extra structure such as an orientation or a framing. Structure of this sort can be swiftly accommodated by way of the *tangent classifier*: each $n$-manifold $M$ has a tangent microbundle, and it is classified by a map $\tau_M \colon M \to \mathop{\mathrm{\sf BTop}}(n)$ to the classifying space of the topological group ${\sf Top}(n)$ of self-homeomorphisms of $\mathbb R^n$; see [@milnorstasheff]. For $B\to \mathop{\mathrm{\sf BTop}}(n)$ a map of spaces, a $B$-framing on $M$ is a homotopy commutative diagram among spaces $$\xymatrix{
&&
B  \ar[d]
\\
M \ar[rr]_-{\tau_M} \ar[urr]^-{g}
&&
\mathop{\mathrm{\sf BTop}}(n).
}$$

::: example
Consider the composite continuous homomorphism $${\sf Top}(n) \xrightarrow{~(-)^+~}{\sf Aut}_\ast(S^n) \xrightarrow{~\pi_0~} \mathbb Z/2\mathbb Z$$ given by applying 1-point compactification to obtain based homotopy automorphisms of a sphere followed by taking path components. For ${\sf STop}(n)\subset {\sf Top}(n)$ the kernel of this homomorphism, a ${\sf BSTop}(n)$-framing on a topological $n$-manifold is precisely an orientation.
:::

Toward formulating an $\infty$-category of $B$-framed $n$-manifolds, we next explain how to make the tangent classifier continuously functorial among open embeddings. We will make ongoing use of the following result of Kister and Mazur.

::: theorem
[]{#kister label="kister"} The continuous homomorphism of topological monoids ${\sf Top}(n) \to {\sf Emb}(\mathbb R^n,\mathbb R^n)$ is a homotopy equivalence.
:::

Now, temporarily consider the full $\infty$-subcategory $\mathcal E{\sf uc}_n\subset \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ consisting solely of $\mathbb R^n$; this $\infty$-category is that associated to the topological monoid $\mathop{\mathrm{\mathsf{Emb}}}(\mathbb R^n,\mathbb R^n)$ of self-embeddings of $\mathbb R^n$. We draw an immediate consequence of the Kister--Mazur Theorem.

::: cor
[]{#euc label="euc"} The canonical functor $$\mathop{\mathrm{\sf BTop}}(n) \longrightarrow \mathcal E{\sf uc}_n$$ is an equivalence of $\infty$-categories. In particular, there is a preferred equivalence of $\infty$-categories $$\mathop{\mathrm{\sf PShv}}(\mathcal E{\sf uc}_n)~\simeq~\mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)}$$ between space-valued presheaves on $\mathcal E{\sf uc}_n$ and spaces over $\mathop{\mathrm{\sf BTop}}(n)$.
:::

After Corollary [\[euc\]](#euc){reference-type="ref" reference="euc"} we have a tangent classifier, functorial in a coherent homotopy sense, given by the restricted Yoneda functor: $$\label{tau}
\tau\colon \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n \longrightarrow \mathop{\mathrm{\sf PShv}}(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n) \longrightarrow \mathop{\mathrm{\sf PShv}}(\mathcal E{\sf uc}_n)~\underset{\rm Cor~\ref{euc}}\simeq~\mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)}~.$$ We will postpone to Corollary [\[tang-class\]](#tang-class){reference-type="ref" reference="tang-class"} justification for this terminology. To define the $\infty$-category of $B$-framed $n$-manifolds as it is equipped with a symmetric monoidal structure, we record a few standard facts about $\infty$-categories together with an observation about the functor $\tau$.

::: lemma
[]{#slice-slice label="slice-slice"} Let $\mathcal S$ be an $\infty$-category and let $S\in \mathcal S$ be an object.

1.  For each morphism $S'\to S$ in $\mathcal S$, the canonical functor among over $\infty$-categories $(\mathcal S_{/S})_{/(S'\to S)} \to \mathcal S_{/S'}$ is an equivalence.

2.  Should $\mathcal S$ admit finite coproducts, the over $\infty$-category $\mathcal S_{/S}$ admits finite coproducts and they are preserved by the projection functor $\mathcal S_{/S} \to \mathcal S$.

In addition, the $\infty$-category of symmetric monoidal $\infty$-categories ${\sf Cat}_\infty^\otimes$ admits limits and they are preserved by the forgetful functor ${\sf Cat}_\infty^{\otimes} \to \mathop{\mathrm{\sf Cat_\infty}}$.
:::

::: proof
*Proof.* Through the defining adjunctions for over $\infty$-categories, the first assertion follows because, for each $\infty$-category $\mathcal K$, the canonical diagram among $\infty$-categories $$\xymatrix{
\{0\}  \ar[r] \ar[d]
&
\{0<1\}   \ar[d]
\\
\mathcal K\star\{0\}   \ar[r]
&
\mathcal K\star \{0<1\}
}$$ is a pushout; here, for $\mathcal K$ and $\mathcal J$ $\infty$-categories, $$\mathcal K\star \mathcal I~ :=~ \mathcal K\underset{\mathcal K\times\{0\}\times \mathcal I} \coprod \mathcal K\times\{0<1\}\times \mathcal I\underset{\mathcal K\times \{1\}\times\mathcal I}\coprod \mathcal I$$ denotes the join of $\infty$-categories. The second assertion follows directly from the universal property of coproducts. The final assertion follows from Proposition 3.2.2.1 of [@dag], which in particular gives that, for each Cartesian closed presentable $\infty$-category $\mathcal C$, the forgetful functor from commutative algebras $\mathop{\mathrm{\mathsf{Alg}}}_{\sf Com}(\mathcal C^\times) \to \mathcal C$ preserves and creates limits. Apply this result to the case $\mathcal C= \mathop{\mathrm{\sf Cat_\infty}}$. ◻
:::

::: observation
Because $\mathbb R^n$ is connected, this tangent classifier $\tau\colon \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n \to \mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)}$ is symmetric monoidal with respect to coproducts in the codomain. In other words, $\tau$ carries finite disjoint unions to finite coproducts over $\mathop{\mathrm{\sf BTop}}(n)$.
:::

::: definition
[]{#bmanifold label="bmanifold"} The symmetric monoidal $\mathop{\mathrm{\infty}}$-category $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B$ of $B$-framed topological $n$-manifolds is the limit in the following diagram: $$\xymatrix{
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n\ar[r]\ar[d]&\mathop{\mathrm{\mathsf{Spaces}}}_{/B}\ar[d]\\
\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n\ar[r]^-\tau&\mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)}.
}$$
:::

Since passage from $\mathop{\mathrm{\infty}}$-categories to their spaces of morphisms preserves limits, there is a corresponding expression for mapping spaces: for two $B$-framed manifolds, $M$ and $N$, the space of $B$-framed embeddings of $M$ to $N$ is the homotopy pullback $$\xymatrix{
\mathop{\mathrm{\mathsf{Emb}}}^B(M,N)\ar[r]\ar[d]&\mathop{\mathrm{\sf Map}}_{/B}(M,N)\ar[d]\\
\mathop{\mathrm{\mathsf{Emb}}}(M,N)\ar[r]&\mathop{\mathrm{\sf Map}}_{/\sf BTop(n)}(M,N),\\}$$ where $\mathop{\mathrm{\sf Map}}_{/X}(M,N)$ is the space of maps of $M$ to $N$ over $X$, a point of which can be taken to be a map $M\rightarrow N$ and a homotopy between the two resulting maps from $M$ to $X$.

The following assures us that these spaces of $B$-framed embeddings have tractable homotopy types.

::: lemma
A $B$-framing $g$ of $\mathbb R^n$ determines a homotopy equivalence $\mathop{\mathrm{\mathsf{Emb}}}^B(\mathbb R^n, \mathbb R^n) \simeq \Omega_g B$ of topological monoids, where $\Omega_g B$ is the loop space of $B$ based at the homotopy point $g: \mathbb R^n \rightarrow B$.
:::

::: proof
*Proof.* By definition, the space $\mathop{\mathrm{\mathsf{Emb}}}^B(\mathbb R^n, \mathbb R^n)$ sits in a homotopy pullback square: $$\xymatrix{
\mathop{\mathrm{\mathsf{Emb}}}^B(\mathbb R^n, \mathbb R^n) \ar[r]\ar[d]& \mathop{\mathrm{\sf Map}}_{/\negthinspace B}(\mathbb R^n, \mathbb R^n)\ar[d]\\
\mathop{\mathrm{\mathsf{Emb}}}(\mathbb R^n, \mathbb R^n) \ar[r]&\mathop{\mathrm{\sf Map}}_{/\mathop{\mathrm{\sf BTop}}(n)}(\mathbb R^n, \mathbb R^n).
}$$ There are evident equivalences of spaces $\mathop{\mathrm{\sf Map}}_{/\mathop{\mathrm{\sf BTop}}(n)}(\mathbb R^n, \mathbb R^n)\simeq \Omega \mathop{\mathrm{\sf BTop}}(n)\simeq \mathop{\mathrm{\mathsf{Top}}}(n)$ and likewise $\mathop{\mathrm{\sf Map}}_{/\negthinspace B}(\mathbb R^n, \mathbb R^n)\simeq \Omega_g B$. It is standard that the the composite map of spaces $$\mathop{\mathrm{\mathsf{Top}}}(n)\longrightarrow \mathop{\mathrm{\mathsf{Emb}}}(\mathbb R^n,\mathbb R^n)\longrightarrow\mathop{\mathrm{\sf Map}}_{/\mathop{\mathrm{\sf BTop}}(n)}(\mathbb R^n,\mathbb R^n)\simeq \Omega \mathop{\mathrm{\sf BTop}}(n)$$ is an equivalence. By Kister--Mazur, Theorem [\[kister\]](#kister){reference-type="ref" reference="kister"}, the first map including $\mathop{\mathrm{\mathsf{Top}}}(n)$ into $\mathop{\mathrm{\mathsf{Emb}}}(\mathbb R^n, \mathbb R^n)$ is a homotopy equivalence. It follows that the middle map in the above display is also an equivalence of spaces. We conclude that the bottom horizontal map in the above homotopy pullback square is an equivalence of spaces. This implies the top horizontal map too is an equivalence of spaces. ◻
:::

[^1]: Thus, any $M\in \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ has finitely many connected components, each of which is the interior of a compact manifold with (possibly empty) boundary. This size restriction is not an essential requirement; since all noncompact manifolds are built as sequential colimits of such smaller manifolds, this smallness condition could be removed and one could instead add to Definition [\[exc\]](#exc){reference-type="ref" reference="exc"} the requirement that a homology theory preserves sequential colimits.
