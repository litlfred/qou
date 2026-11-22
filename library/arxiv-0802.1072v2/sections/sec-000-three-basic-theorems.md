---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-000-three-basic-theorems
section_title: "Three basic theorems"
section_number: null
pages: 1-3
source_pdf: 0802.1072v2.pdf
source_sha256: 6f4d93f0b7ba5cd7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.931
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
[]{#S:Three basic theorems label="S:Three basic theorems"}

In this section we present the basic lemmas and theorems about links that are closed three-braids. Initially, we will use the classical presentation for the braid group $B_3$: $$\label{E:classical presentation}
<\sigma_1,\sigma_2; \sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2>$$ In the presentation ([\[E:classical presentation\]](#E:classical presentation){reference-type="ref" reference="E:classical presentation"}) the generator $\sigma_i$ is a positive interchange of strands $i$ and $i+1$, where $i=1$ or $2$.

Before we can state our first theorem, we need a definition. Let $\mathcal L$ be a closed 3-braid, with representative $L\in B_3$. Then:

-   $\mathcal L$ is said to *admit a flype* if the conjugacy class of $L$ has a representative which is in one of the special forms illustrated in each of the four sketches in Figure 1. In particular its associated (open) braids are conjugate to:

    $$\label{E:flype-admissible form} 
    L = \sigma_1^u\sigma_2^v\sigma_1^w\sigma_2^\epsilon,  \  \  {\rm for \ \ some} \ \ u,v,w,\epsilon \in \mathbb N,  \ \ \epsilon = \pm 1.$$

-   A flype is *positive* or *negative*, according as $\epsilon$ is $+1$ or $-1$.

-   A flype is *non-degenerate* when the braids $L= \sigma_1^u\sigma_2^v\sigma_1^w\sigma_2^\epsilon$ and $L' = \sigma_1^w\sigma_2^v\sigma_1^u\sigma_2^\epsilon$ are in distinct conjugacy classes. We are interested only in non-degenerate flypes.

![Positive and Negative 3-braid flypes](flype.eps){#F:flype}

::: theorem
**The classification theorem [@BM-SLVCB-III]:** []{#T:topological label="T:topological"} Let $\mathcal{L}$ be a link type which is represented by the closure of a 3-braid $L$. Then one of the following holds:

1.  $\mathcal L$ has braid index 3 and every 3-braid which represents $\mathcal L$ is conjugate to $L$.

2.  $\mathcal L$ has braid index 3, and is represented by exactly two distinct conjugacy classes of closed 3-braids. This happens if and only if the conjugacy class of $L$ contains a braid which admits a non-degenerate flype.

3.  The braid $L$ is conjugate to $\sigma_1^k\sigma_2^{\pm 1}$ for some $k\in\mathbb{N}$. These are precisely the links which are defined by closed 3-braids, but have braid index less than 3.
:::

**Remark:**  It is immediately clear that in order to use Theorem [\[T:topological\]](#T:topological){reference-type="ref" reference="T:topological"}, the reader will need definitive tests for deciding when two 3-braids are conjugate, and when a conjugacy class admits a non-degenerate flype, and when a conjugacy class contains $\sigma_1^k\sigma_2^{\pm 1}$ for some $k$. These matters will be discussed in $\S$[\[S:conjugacy\]](#S:conjugacy){reference-type="ref" reference="S:conjugacy"} below.

Let $\mathcal K$ be a knot. The standard knot tables classify [unoriented]{.underline} knots. A sharper classification assumes that we fix an orientation on both $S^3$ and on a representative $\overrightarrow{K}$. Let $\overleftarrow{K}$ denote $\overrightarrow{K}$ with its orientation reversed. We then define $\mathcal K$ to be *invertible* if there is an orientation-preserving homeomorphism $h$ of $S^3$ such that $h(\overrightarrow{K})$ is smoothly isotopic to $\overleftarrow{K}$. Our second classification theorem treats the question of when an oriented link of braid index 3 fails to be invertible. As was mentioned earlier, this is an interesting issue, because at this writing there is no effective test that recognizes whether an arbitrary link is or is not invertible. Using the standard presentation ([\[E:classical presentation\]](#E:classical presentation){reference-type="ref" reference="E:classical presentation"}) for $B_3$, we note that if $\overrightarrow{K}$ is defined by a cyclic word in the standard generators, then $\overleftarrow{K}$ will be defined by the same cyclic word, read backwards.

::: theorem
**The invertibility theorem [@BM-SLVCB-III]:** []{#T:invertibility label="T:invertibility"} Let $\mathcal K$ be a link of braid index 3 with oriented 3-braid representative $\overrightarrow{K}$. Then $\mathcal K$ is non-invertible if and only if $\overrightarrow{K}$ and $\overleftarrow{K}$ are in distinct conjugacy classes, and the class of $\overrightarrow{K}$ does not contain a representative which admits a non-degenerate flype.
:::

**Proof:** If $\overrightarrow{K}$ admits a non-degenerate flype, then the isotopy of $S^3$ which realizes the flype takes $\overrightarrow{K} \to \overleftarrow{K}$, so that $\mathcal K$ is invertible. If $\overrightarrow{K}$ does not admit a non-degenerate flype, then by Theorem [\[T:topological\]](#T:topological){reference-type="ref" reference="T:topological"} the class of $\overrightarrow{K}$ is the only class that represents the oriented link $\mathcal K$. The assertion follows. $\|$

A knot is said to be *transversal* if it is everywhere transverse to the standard contact structure in $\mathbb R^3$. A *transversal knot type* is the equivalence class of a transversal knot, under isotopies which are restricted so that every intermediate representative is transversal. Our third classification theorem relates to transversal knot types that are closed 3-braids. It uses Theorem [\[T:topological\]](#T:topological){reference-type="ref" reference="T:topological"} and is related to Theorem [\[T:invertibility\]](#T:invertibility){reference-type="ref" reference="T:invertibility"}, however in Theorem [\[T:transversal\]](#T:transversal){reference-type="ref" reference="T:transversal"} below we are interested explicitly in the conjugacy classes which admit a non-degenerate negative flype and do not at the same time admit a positive flype, because a positive flype can be realized by a transversal isotopy. Recall that a transversal knot type is *transversally simple* if it is determined completely by its topological link type and its Bennequin invariant.

::: theorem
**The transversal classification theorem [@BM-stab-II]:** []{#T:transversal label="T:transversal"} Let $\mathcal{TK}$ be a transversal knot type which is represented by a closed 3-braid $K_1 = \sigma_1^u\sigma_2^v\sigma_1^w\sigma_2^{-1}$. Assume that $\mathcal K_1$ does not also admit a positive flype. Then the braids $K_1$ and $K_2 = \sigma_1^w\sigma_2^v\sigma_1^u\sigma_2^{-1}$ close to distinct transversal knot types $\mathcal{TK}_1, \mathcal{TK}_2$ that are topologically invertible but are not transversally invertible. In particular, $\mathcal{TK}_1$ and $\mathcal {TK}_2$ are not transversally simple.
:::
