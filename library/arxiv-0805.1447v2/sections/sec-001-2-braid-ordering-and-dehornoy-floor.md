---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-001-2-braid-ordering-and-dehornoy-floor
section_title: "Braid ordering and Dehornoy floor"
section_number: 2
pages: 4-6
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
text_source: latex
latex_prose_ratio: 0.737
latex_coverage_ratio: 0.985
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this section we review some of fundamental facts of Dehornoy ordering and Dehornoy floor. Braid group $B_{n}$ is, by definition, a group which is presented by $$\langle \sigma_{1},\cdots,\sigma_{n-1}| \sigma_{i}\sigma_{j}\sigma_{i}=\sigma_{j}\sigma_{i}\sigma_{j} \textrm{ if } |i-j|=1, \; \sigma_{i}\sigma_{j}=\sigma_{j}\sigma_{i} \textrm{ if } |i-j|\geq 2  \rangle .$$ Geometrically, elements of braid group $\beta \in B_{n}$ are represented by braided $n$-strands which move from above to below, oriented downward. By connecting their endpoints of strands canonically, we obtain an oriented link. We denote this link by $\widehat{\beta}$ and call *closed braid* or *closure* of $\beta$.

We call the braid $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1})(\sigma_{1}\sigma_{2}\cdots\sigma_{n-2})\cdots(\sigma_{1}\sigma_{2})(\sigma_{1})$ *Garside's fundamental braid* and denote it by $\Delta$. The Garside fundamental braid$\Delta$ plays an important role in braid groups. It is known that $\Delta^{2}$ generates the center of $B_{n}$, which is an infinite cyclic group. For these basic facts about braid group, see [@b].

## Dehornoy ordering, Dehornoy floor

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

## The geometric meaning of Dehornoy ordering and Dehornoy floor

Now we give a geometric description of Dehornor ordering given in [@fgrrw]. Let $\Gamma$ be a graph in $D_{n}$ consisting of horizontal line which connects puncture points. See figure [1](#fig:braidorder_meaning){reference-type="ref" reference="fig:braidorder_meaning"}. We identify braid groups as a relative mapping class group $MCG(D_{n},\partial D_{n})$, which is a group of isotopy classes of homeomorphisms of $D_{n}$ whose restriction to boundary $\partial D_{n}$ is an identity. For braid $\alpha, \beta$, consider the image of graph $\Gamma$. By performing isotopy, we can assume $\alpha(\Gamma)$ and $\beta(\Gamma)$ have minimal intersections. If $\alpha \neq \beta$, these graphs must be different, so at some puncture point two graphs will diverge. We say $\beta >_{geom} \alpha$ if at divergence point, $\beta(\Gamma)$ moves left side of $\alpha(\Gamma)$. See figure [1](#fig:braidorder_meaning){reference-type="ref" reference="fig:braidorder_meaning"}. In [@fgrrw] it is proved that this relation $>_{geom}$ coincide with Dehornoy ordering $>$.

Since $\Delta^{2}$ corresponds to rotation of the disc $D_{n}$, Dehornoy floor of $\beta$ is the number of how many times the initial segment of graph $\beta(\Gamma)$ winding around $\partial D_{n}$ under neglecting orientation.

<figure id="fig:braidorder_meaning" data-latex-placement="htbp">
<div class="center">
<embed src="braidorder.eps" style="width:100mm" />
</div>
<figcaption>Graph <span class="math inline"><em>Γ</em></span> and examples</figcaption>
</figure>

## More precious estimation of Dehornoy floor

For later use, we prove slightly more precious estimation of Dehornoy floor than proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1).

::: prop
[]{#prop:newestimation label="prop:newestimation"} If a braid $\beta$ is conjugate to a braid $\alpha$ which is represented by braid word which contains $s$ occurrence of $\sigma_{1}$ and $k$ occurrence of $\sigma_{1}^{-1}$, then $[\beta]_{D} < max\{s,k\}$.
:::

::: proof
*Proof.* We show $\beta < \Delta^{2k}$. The proof of $\Delta^{-2s}< \beta$ is identical. By assumption, we can write $\beta = \gamma^{-1}(W_{0}\sigma_{1}W_{1}\sigma_{1}\cdots W_{k})\gamma$ where $W_{i}$ is a braid word which contains no $\sigma_{1}$ and $\gamma \in B_{n}$. We remark that we can assume $W_{0}$ is empty because we can amalgamate $W_{0}$ into conjugating element $\gamma$.

Let $\Delta' = (\sigma_{2}\sigma_{3}\cdots \sigma_{n-1})^{n-1}$. From property S, we can find a braid $\beta' = \gamma^{-1}(\sigma_{1}\Delta'^{2p}_{(1)}\sigma_{1}\cdots \Delta'^{2p}_{(k)})\gamma > \beta$ by inserting $\sigma_{1},\cdots \sigma_{n-1}$ to braid $\beta$, for sufficiently large $p>0$. We show $\beta' <\Delta^{2k}$, that is equivalent to an inequality $(\sigma_{1}\Delta'^{2p}_{(1)}\sigma_{1}\cdots \Delta'^{2p}_{(k)})\gamma < \Delta^{2k} \gamma$. First we consider the case $k=1$. We use the geometric interpretation of Dehornoy ordering. Let $D'$ be a sub-disc of $D_{n}$ which contains $2,\cdots n$-th puncture of $D_{n}$. Since $\Delta'^{2p}$ is p-times twists around $\partial D'$ and $\Delta^{2}$ is a rotation along $\partial D_{n}$, we conclude that the image of $\Delta^{2}\gamma(\Gamma)$ moves more left than $\sigma_{1}\Delta'^{2p}\gamma(\Gamma)$ for all $p$, thus $\sigma_{1}\Delta'^{2p}\gamma <\Delta^{2}\gamma$. Induction about $k$ gives desired result. ◻
:::

This proposition gives more accurate estimation of Dehornoy floor than using lemma [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1).

::: rem
Proposition [\[prop:newestimation\]](#prop:newestimation){reference-type="ref" reference="prop:newestimation"} makes results in [@mn] a bit stronger form because in [@mn] they use estimation via lemma [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (1). Especially, we conclude that if $\widehat{\beta}$ admit destabilization or exchange move, then $[\beta_{D}]=0$.
:::
