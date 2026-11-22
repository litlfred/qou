---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-046-63-path-morphisms
section_title: "Path morphisms"
section_number: 6.3
pages: 40-41
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.786
latex_coverage_ratio: 0.974
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#f label="f"}

::: defi
For $(W,S)$ a Coxeter system and $x\in W$ we define the *Reduced expressions graph of $x$* or simply *Rex($x$)* as the graph with nodes the set of reduced expressions of $x$ and two reduced expressions are joined by an edge if they differ by a single braid relation.
:::

For every reduced expression $\underline{s}$ we have associated a Bott-Samelson bimodule $B_{\underline{s}}.$ If two Bott-Samelson bimodules $B, B'$ differ by just one braid relation one has a morphism of the type $\mathrm{id}\otimes f_{sr}\otimes \mathrm{id}\in \mathrm{Hom}(B,B')$. For example, for the braid move $pq\,\, srs\,\, u\rightarrow pq\,\, rsr\,\, u$ (here we suppose $srs=rsr$) we have an associated morphism between the corresponding Bott-Samelson bimodules $$\mathrm{id^2}\otimes f_{sr}\otimes \mathrm{id} : B_pB_q (B_sB_rB_s) B_u\rightarrow B_pB_q(B_rB_sB_r) B_u.$$This means that for each path $p$ in Rex($x$) one can uniquely associate a morphism $f(p)$ between the corresponding Bott-Samelson bimodules. We call it a *path morphism.*

::: defi
A *Complete path* in a graph is a path passing through every vertex of the graph at least once.
:::

The following conjecture is due to the author.

::: ques
Let $x\in S_n.$ Let $p$ and $q$ be two complete paths in $\mathrm{Rex}(x)$. Then $f(p)=f(q).$
:::

Some remarks about this conjecture

::: remark
There has been some serious computer checking of this conjecture by the author and Antonio Behn, using Geordie Williamson's programs. That this conjecture was checked in huge cases (Rex graphs of over 100.000 vertices) was extremely surprising for the author. There is no conceptual understanding of why this conjecture could be true. It seems utterly strange.
:::

::: remark
If this conjecture was proved, then one would have a new and natural basis for the Hecke algebra, by applying the character map to the image of this (unique, for any element of $S_n$) projector. The author believes this would give a rich combinatorial basis of the Hecke algebra, and a very natural set of Soergel bimodules that in our dreams should play a role in the understanding of the $p$-canonical basis[^1].
:::

::: remark
The conjecture is not true for any Coxeter group. There are counter-examples for $F_4$ (although not easy to find). Nonetheless, in [@li2.5] the author proves an analogue of the Forking path conjecture for "extra-large Coxeter groups", i.e. groups in which $m(s,r)>3$ for all $s,r\in S,$ so it is quite mysterious for what groups this should be true.
:::

::: remark
There is a 55 pages paper of Elias [@El] published in a fine journal whose central result is that a certain path morphism in Rex($w_0$) is an idempotent, where $w_0$ is the longest element of $S_n$, and that it projects to the indecomposable Soergel bimodule. To prove that this path morphism is an idempotent has aproximately the same level of difficulty as to prove the Forking path conjecture for the particular case of the longest element $w_0$ and for two specific complete paths $p_0$ and $q_0$. This gives an idea of how hard the Forking path conjecture can be, and also the kind of methods one can use to attack it (for example, the beautiful topology appearing in the higher Bruhat order of Manin and Schechtman).
:::

If one has a reduced expression $t_1\cdots t_i$ of some element $x\in W$, then by the important property in Section [\[imp\]](#imp){reference-type="ref" reference="imp"} we know that, if $xs<s$ for some $s\in S$, then there is at least one path in Rex($x$) starting in $t_1\cdots t_i$ and ending in some reduced expression with $s$ in the far-most right position. One considers the path morphism associated to a path like this and call it *a path morphism from $t_1\cdots t_i$ taking $s$ to the right.*

## The tree $\mathbb{T}_{\underline{s}}$ {#T}

Let $(W,\mathcal{S})$ be an arbitrary Coxeter system. In this section we fix a sequence of simple reflections $\underline{s}=(s_1,\ldots, s_n) \in \mathcal{S}^n$ and construct a tree $\mathbb{T}_{\underline{s}}$.

We construct a perfect binary tree (i.e a tree in which all interior nodes have exactly two children and all leaves have the same depth) with nodes colored by Bott-Samelson bimodules and arrows colored by morphisms from parent to child nodes. We construct it by induction on the depth of the nodes. In depth zero and one we have the following tree:

Let $k<n$ and $\underline{t}=(t_1,  \cdots, t_{i})\in  \mathcal{S}^{i}$ be such that a node $N$ of depth $k-1$ is colored by the bimodule $(B_{t_1}  \cdots B_{t_{i}})(B_{s_{k}} \cdots B_{s_n}),$ then we have two cases.

1.  If we have the inequality $l(t_1\cdots t_{i}s_k)>l(t_1\cdots t_{i})$, then the child nodes (of depth $k$) and child edges of $N$ are colored in the following way:

2.  If we have the opposite inequality $l(t_1\cdots t_{i}s_k)<l(t_1\cdots t_{i})$, then the child nodes (of depth $k$) and child edges of $N$ are colored in the following way (arrows are the composition of the corresponding pointed arrows):

The map $F$ is any path morphism from ${t_1}  \cdots {t_{i}}$ taking $s_k$ to the right (see Section [\[f\]](#f){reference-type="ref" reference="f"}). This finishes the construction of $\mathbb{T}_{\underline{s}}.$

By composing the corresponding arrows we can see every leaf of the tree $\mathbb{T}_{\underline{s}}$ colored by $B_{\underline{x}}$ as a morphism in the space $\mathrm{Hom}(B_{\underline{s}},B_{\underline{x}}).$ Consider the set $\mathbb{L}_{\underline{s}}(\mathrm{id}),$ the leaves of $\mathbb{T}_{\underline{s}}$ that are colored by the bimodule $R$. In [@Li1] the set $\mathbb{L}_{\underline{s}}(\mathrm{id})$ is called *light leaves basis* and the following theorem is proved.

::: thm
[]{#LLB label="LLB"} The set $\mathbb{L}_{\underline{s}}(\mathrm{id})$ is a basis of $\mathrm{Hom}(B_{\underline{s}},R)$ as a left $R$-module.
:::

In the paper [@Li1] the leaves colored with $R$ were called light leaves[^2]. Later this notion was changed in the literature and any leaf in the tree $\mathbb{T}_{\underline{s}}$ got to be called a light leaf. We follow this new convention.

[^1]: We will explain in a future paper of this saga what is this basis and why it is so important.

[^2]: The reason for this is that if the "weight" of a leaf is the length of the corresponding Bott-Samelson bimodule, then the leaves colored by $R$ are the "lightest" ones.
