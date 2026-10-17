---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-022-51-a-normal-form-for-3braids
section_title: "A normal form for 3–braids"
section_number: 5.1
pages: 27-28
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.979
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
We begin with some notation. Let $\sigma_1$ and $\sigma_2$ be generators for $B_3$, the braid group on three strands, as in Figure [\[fig:3braid-generators\]](#fig:3braid-generators){reference-type="ref" reference="fig:3braid-generators"}. Thus a positive word in $\sigma_1$ and $\sigma_2^{-1}$ represents an alternating braid diagram. Let $C =
(\sigma_1 \sigma_2)^3$ denote a full twist of all three strands; $C$ generates the center of $B_3$. For a braid $w \in B_3$, let $\hat{w}$ denote the link obtained as the closure of $w$. Note that $\hat{w}$ only depends on the conjugacy class of $w$. We denote the conjugacy relation by $\sim$.

In the 1920s, Schreier developed a normal form for this braid group [@schreier]. In particular, he showed the following.

::: theorem
[]{#thm:schreier-normal label="thm:schreier-normal"} Let $w \in B_3$ be a braid on 3 strands. Then $w$ is conjugate to a braid in exactly one of the following forms:

1.  $C^k \sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s}
    \sigma_2^{-q_s}$, where $k \in {\mathbb{Z}}$ and $p_i$, $q_i$, and $s$ are all positive integers,

2.  $C^k \sigma_1^p$, for $k, p \in {\mathbb{Z}}$

3.  $C^k \sigma_1 \sigma_2$, for $k \in {\mathbb{Z}}$

4.  $C^k \sigma_1 \sigma_2 \sigma_1$, for $k \in {\mathbb{Z}}$, or

5.  $C^k \sigma_1 \sigma_2 \sigma_1 \sigma_2$, for $k \in {\mathbb{Z}}$.

This form is unique up to cyclic permutation of the word following $C^k$. Braids in form $(1)$ above are called *generic*.
:::

Birman and Menasco have shown that nearly every oriented link obtained as the closure of a 3--braid can be represented by a unique conjugacy class in $B_3$, with an explicit list of exceptions [@birman-menasco:3braids]. Thus their theorem, combined with Schreier's normal form, gives a classification of closed oriented $3$--braids. Their paper also contains a modern exposition of Schreier's algorithm for placing braids in normal form.

Let $K = \hat{w}$ be a closed 3--braid defined by the word $w$, and let $A$ be the braid axis of $K$. That is, $A$ is an unknot with the property that the solid torus $S^3 {\smallsetminus}A$ is swept out by meridian disks, with each disk intersecting $K$ in 3 points. Then $M_w
:= S^3 {\smallsetminus}(K \cup A)$ is a 4--punctured sphere bundle over the circle. It is well--known, essentially due to work of Thurston [@thurston:hypII], that the Schreier normal form of $w$ predicts the geometry of $M_w$. We include a proof for completeness.

::: theorem
[]{#thm:hyperbolic-bundle label="thm:hyperbolic-bundle"} $M_w$ is hyperbolic if and only if $w$ is generic. Moreover, $M_w$ has nonzero Gromov norm if and only if $w$ is generic.
:::

::: proof
*Proof.* The braid generators $\sigma_1$ and $\sigma_2^{-1}$ act on the 4--punctured sphere as the standard generators $L$ and $R$ of $SL_2({\mathbb{Z}})$: $$\sigma_1 \: \mapsto \: L :=
\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad
\sigma_2^{-1} \: \mapsto \: R :=
\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \qquad
C \: \mapsto \: I =
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.$$

Thus generic 3--braids with normal form (1) correspond to positive words employing both letters $L$ and $R$, hence to pseudo-Anosov monodromies. Thurston showed that a bundle over $S^1$ with pseudo-Anosov monodromy is hyperbolic [@thurston:hypII]. More concretely, Guéritaud showed how to construct the hyperbolic metric from a positive word in $L$ and $R$ [@gf:two-bridge]. (See Sections [\[sec:ptorus\]](#sec:ptorus){reference-type="ref" reference="sec:ptorus"} and [\[sec:4ps\]](#sec:4ps){reference-type="ref" reference="sec:4ps"} above for a review of the connection between the monodromy word and the canonical ideal triangulation of $M_w$.)

The braids with normal form (2) correspond to reducible monodromies of the form $L^p$. In this case, $M_w$ is a graph manifold obtained by gluing two 3--punctured sphere bundles along a torus. The braids with normal forms (3--5) correspond to periodic monodromies, hence $M_w$ is Seifert fibered. Thus all non-generic normal forms yield non-hyperbolic manifolds with Gromov norm 0. ◻
:::
