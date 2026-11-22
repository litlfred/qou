---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-002-21-dehornoy-ordering-dehornoy-floor
section_title: "Dehornoy ordering, Dehornoy floor"
section_number: 2.1
pages: 4-6
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.982
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this section we give a brief exposition of left-invariant total ordering of braid groups called Dehornoy ordering, and define Dehornoy floor. Dehornoy floor is first introduced in [@mn], though they do not use term Dehornoy floor. This is a measure of how far braid is from the identity elements with respect to Dehornoy ordering and can be seen as some kinds of complexity of braids. We describe fundamental results about Dehornoy floor, proved in [@mn],[@ma].

A braid $\beta \in B_{n}$ is called $\sigma$-$positive$ if $\beta$ can be represented by a word which contains at least one $\sigma_{i}$, and contains no $\sigma_{1}^{\pm1},\sigma_{2}^{\pm1}\cdots,\sigma_{i-1}^{\pm 1},\sigma_{i}^{-1}$ for some $1\leq i \leq n-1$. we say $\alpha < \beta$ is true if and only if the braid $\alpha^{-1}\beta$ is $\sigma$-positive. It is known that the relation $<$ defines left-invariant total ordering of $B_{n}$; That is, $<$ is total ordering and if braids $\alpha,\beta \in B_{n}$ satisfy $\alpha < \beta$ , then for all braid $\gamma \in B_{n}$, $\gamma \alpha < \gamma \beta$ holds. We call this ordering *Dehornoy ordering*. Dehornoy ordering has following nice property, called *property $S$* or *Subword property*.

::: prop
[]{#prop:Property-S label="prop:Property-S"} For any braids $\beta_{1},\beta_{2} \in B_{n}$ and $1\leq i \leq n-1$, $$\beta_{1}\sigma_{i}\beta_{2} > \beta_{1}\beta_{2} > \beta_{1}\sigma_{i}^{-1}\sigma_{2}$$ holds.
:::

As we mentioned at introduction, there are many other interpretation and definition of Dehornoy ordering. See [@ddrw] for those other definitions and meanings. We will describe one of the geometrical definition later. Using Dehornoy ordering, we define Dehornoy floor of braids $[\beta]_{D}$ as follows.

::: defn
Dehornoy floor $[\beta]_{D}$ of braid $\beta \in B_{n}$ is a minimal non-negative integer $m$ which satisfies $\beta \in (\Delta^{-2m-2},\Delta^{2m+2})$, where $(\Delta^{-2m-2},\Delta^{2m+2})= \{ \alpha \in B_{n} \;| \; \Delta^{-2m-2} < \alpha  <\Delta^{2m+2} \}$.
:::

Now we remark one important facts. We must be careful that when we think about Dehornoy floor, which $B_{n}$ a braid $\beta$ belongs to is very important. For example, for a braid $\beta = (\sigma_{1}\sigma_{2})^{4}$, $[\beta]_{D}=1$ if we consider $\beta \in B_{3}$, and $[\beta]_{D}=0$ if we consider $\beta \in B_{4}$. Fortunately, if we use braid groups to describe links, the number of strands are always implicit, so there might be no confusion about the number of braid strands. So in most cases, we omit to write which $B_{n}$ a braid $\beta$ belongs to. we also remark that Dehornoy floor is not a conjugacy invariant of braids. For example, 3-braid $\Delta^{2}\sigma_{1}\sigma_{2}^{-1}$ has Dehornoy floor $1$ but its conjugation $\Delta^{-1}(\Delta^{2}\sigma_{1}\sigma_{2}^{-1})\Delta = \Delta^{2}\sigma_{2}\sigma_{1}^{-1}$ has zero Dehornoy floor. This is mainly because Dehornoy ordering is not right-invariant; That is, it does not hold that for every $\gamma \in B_{n}$, $\alpha\gamma < \beta\gamma$ whenever $\alpha < \beta$. Thus, Dehornoy floor is far from knot invariant.

The most important property of Dehornor floor is that it can be seen as some kinds of restriction for admissibility of braid moves. We summarize the basic properties of Dehornoy floor, all of which are proved in [@mn], or [@ma].

::: prop
[]{#prop:dehornoyfloor label="prop:dehornoyfloor"} Let $\alpha,\beta \in B_{n}$. Then following holds.

1.  If braid $\beta \in B_{n}$ is represented by braid word which contains $s$ occurrence of $\sigma_{1}$ and $k$ occurrence of $\sigma_{1}^{-1}$, then $[\beta]_{D} < max\{s,k\}$.

2.  $|[\beta]_{D}-[\beta']_{D}|\leq 1$ if $\beta$ and $\beta'$ are conjugate.

3.  $[\alpha \beta]_{D} \leq 1+[\alpha]_{D}+[\beta]_{D}$.

4.  If closure of braid $\beta \in B_{n}$ admit destabilization or exchange move, $[\beta]_{D} \leq 1$.

5.  For every $n$, there exist positive integer $r(n)$ such that for every $\beta \in B_{n}$, if $[\beta]_{D}>r(n)$ then $\widehat{\beta}$ is the unique closed $n$-braid representative of link types represented by its closure. That is, if $\widehat{\beta} = \widehat{\beta'}$ holds for some $\beta' \in B_{n}$, $\beta$ and $\beta'$ are conjugate.
:::

We remark that Dehornoy floor is not a conjugacy invariant but proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (2) shows taking conjugate changes Dehornoy floor at most by one.

::: rem
Our definition of Dehornoy floor is slightly different from one in [@ma]. Our definition is rather after [@mn]. We adopt this definition because for application of knot theory, this formulation seems to be more natural and makes statement of results simple.
:::

::: rem
There exist an infinite family of left-invariant total ordering of braid groups, containing Dehornoy ordering, called *Thurston-type ordering* (See [@ddrw] or [@sw]). Most of results in this paper can be stated by using Thurston-type ordering instead of using Dehornoy ordering, especially using \"Thurston floor\" defined by the similar way.
:::
