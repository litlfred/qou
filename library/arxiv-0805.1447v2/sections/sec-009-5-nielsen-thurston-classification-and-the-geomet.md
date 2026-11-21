---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-009-5-nielsen-thurston-classification-and-the-geomet
section_title: "Nielsen-Thurston classification and the geometry of closed braid complements"
section_number: 5
pages: 16-20
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this section, we describe an application of theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} for genus one closed surface, namely, essential torus. A description of essential torus in closed braid complements is studied in [@bm2],[@n] by using braid foliation machinery. Since an essential torus deeply involves the geometry of link complements, we can extract some of geometrical information of closed braids from theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}.

## Nielsen-Thurston classification

First of all, we recall the Nielsen-Thurston classification of braids. Nielsen-Thurston theorem states that an isotopy class of orientation preserving homeomorphism $[f]$ of compact oriented surface $F$, that is, an element of mapping class group $MCG(F)$ of $F$, is classified into following three types:

1.  *periodic*: there exists a positive integer $m$ such that $f^{m}$ is isotopic to the identity.

2.  *reducible*: there exist an essential 1-submanifold $C$ of $F$, which is invariant under $f$.

3.  *pseudo-Anosov*: $f$ is isotopic to a pseudo-Anosov homeomorphism.

We do not describe precise definition of pseudo-Anosov homeomorphism, because we do not use it.(see [@flp] for more details about Nielsen-Thurston theory.) Let $D_{n}$ be a $n$-punctured disc. Since braid group $B_{n}$ is identified with the group of boundary-fixing isotopy class of homeomorphisms of $D_{n}$ which is identity on $\partial D_{n}$, there exist natural projection $\pi:B_{n} \rightarrow MCG(D_{n})$ regarding an element of $B_{n}$ as an isotopy class of homeomorphism of $D_{n}$ whose restriction on $\partial D_{n}$ are not necessarily identity. Therefore we can define the Nielsen-Thurston classification of braids by taking pull-back of the Nielsen-Thurston classification of $MCG(D_{n})$. Concretely, the Nielsen-Thurston classification of $B_{n}$ can be described as following way:

1.  *periodic* : some powers of $\beta$ is equal to some powers of Garside fundamental braid $\Delta$.

2.  *pseudo-Anosov* : its representing homeomorphism is pseudo-Anosov.

3.  *reducible*: its representing homeomorphism is reducible.

Periodic braids are the most simple braids and it is known that periodic braids are conjugate to some powers of braid $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1})$ or $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1}\sigma_{1})$, which represents rotation of disc.

We remark that the Nielsen-Thurston classification of mapping class groups has very beautiful connection to the geometry of its mapping torus. Let $F$ be a closed surface, $\varphi$ be a homeomorphism of $F$ and $F_{\varphi}$ be the mapping torus of $\varphi$. The topology of mapping torus $F_{\varphi}$ only depends on the isotopy class of $\varphi$.

It is known that $F$ admit a complete hyperbolic structure if and only if $\varphi$ is pseudo-Anosov and $F_{\varphi}$ is Seifert-fibered if and only if $\varphi$ is periodic. Moreover, $F_{\varphi}$ contains an essential torus (hence decomposable with respect to geometric decomposition) if and only if $\varphi$ is reducible. Thus, there exist one-to-one correspondence between the Nielsen-Thurston classification of mapping class group and the geometry of its mapping torus. Hence, in this regard, theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} can be seen as some generalization of this well-known fact in the knot theory settings.

## Proof of Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}

First we investigate non-braided satellite knots. Recall that a satellite knot $K$ is called braided-satellite if its complements has essential tori $T$ which is circular foliated under appropriate choice of closed braid representatives of $K$. In general it is difficult to handle non-braided satellite knot in braid theory, but fortunately they do not appear under assumption of theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}.

::: prop
[]{#prop:nbdsatellite label="prop:nbdsatellite"} Let $\beta \in B_{n}$ be a braid such that $K=\widehat{\beta}$ is a non-braided satellite knot. Then, $[\beta ]_{D} < 3$.
:::

::: proof
*Proof.* Assume $[\beta]_{D} \geq 3$. Then theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} shows all of essential tori in the complement of $K$ is circular, contradicts to assumption $K$ is non-braided satellite. ◻
:::

::: rem
In [@mn], it is proved that if a closure of $\beta$ is a composite knot, then $[\beta]_{D}<2$. Proposition [\[prop:nbdsatellite\]](#prop:nbdsatellite){reference-type="ref" reference="prop:nbdsatellite"} can be seen some kind of generalization of this result because composite knots are special types of non-braided satellite knots.
:::

To prove theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}, We need the following result of Menasco concerning about Torus knots.

::: thm
Torus knots are exchange-reducible. That is, For every closed braid representative $\widehat{\beta}$ of $(p,q)$-torus knot, there exists a sequence of closed braids $$\widehat{\beta}= \widehat{\beta_{0}}\rightarrow \widehat{\beta_{1}} \rightarrow \cdots \rightarrow \widehat{\beta_{m}}$$ such that $\widehat{{\beta}_{i+1}}$ is obtained by performing exchange move or destabilization or isotopy of $\widehat{\beta_{i}}$, and $\beta_{m} = (\sigma_{1}\sigma_{2}\cdots\sigma_{p-1})^q$.
:::

We remark that this Menasco's theorem is also proved by braid foliation techniques.

::: proof
*Proof of theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}.* First assume $\beta \in B_{n}$ and $K =\widehat{\beta}$ is a torus knot. If $n$ is not the braid index of knot $K$, that is, if $K$ can be represented as a closure of other braids which have strictly smaller number of strands, then Menasco's theorem says $K$ admit exchange move or destabilization, hence by the proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} (5), we conclude $[\beta]_{D}\leq 1$, which contradicts our assumption $[\beta]_{D} \geq 3$. Therefore we can assume that $n$ is braid index of $K$. In this case, also Menasco's theorem says $\beta$ is conjugate to braid $(\sigma_{1}\sigma_{2}\cdots \sigma_{n-1})^{p}$ for some $p$, hence $\beta$ is periodic.

On the other hand, it is known that periodic braids are conjugate to braids $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1})^{s}$ or $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1}\sigma_{1})^{s}$ for some $s$ , both of which represent rotation of disc. Since closure of $(\sigma_{1}\sigma_{2}\cdots\sigma_{n-1}\sigma_{1})^{s}$ never become a knot, it is obvious that closure of periodic braids represent torus knots.

Next assume $K=\widehat{\beta}$ is a satellite knot. Let $T$ be a essential torus in the complement of $K$. Of course there might be some of choice for such torus, we can take arbitrary one. Our assumption $[\beta]_{D} \geq 3$ and theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} shows $T$ is circular-foliated, so intersection of $T$ with some fiber $H_{\theta}$ gives reducing 1-submanifolds of $\beta$ as a homeomorphism of $D_{n}$, hence $\beta$ is reducible. The converse is trivial.

Since both classifications are exclusive, we conclude that $\widehat{\beta}$ is a hyperbolic knot if and only if $\beta$ is pseudo-Anosov. ◻
:::

As a corollary, we get an infinite, almost disjoint family of hyperbolic knots for each pseudo-Anosov element of mapping class group of punctured disc. Although it is known that \"almost all\" prime knots are hyperbolic knot, in general it is not so easy to determine given not is hyperbolic or not. Especially, most of known family of knots known to be hyperbolic are defined through knot diagrams such as alternativeness. We now construct many families of hyperbolic knot through braid-theoretical approach.

::: cor
[]{#cor:c1 label="cor:c1"} Suppose $[f] \in MCG(D_{n})$ be a pseudo-Anosov element of mapping class group of $n$-punctured disc and $\pi: B_{n} \rightarrow MCG(D_{n})$ be the natural projection. Let $P([f])=\{ \widehat{\beta} \;| \;\beta \in \pi^{-1} ([f]),[\beta]_{D} \geq 3 \}$.

Then $P([f])$ consists of infinite number of distinct hyperbolic knots. Moreover, let $[g] \in MCG(D_{n})$ be another pseudo-Anosov element which is not conjugate to $[f]$ in $MCG(D_{n})$. Then, the intersection of $P([f])$ and $P([g])$ are finite.
:::

::: proof
*Proof of corollary [\[cor:c1\]](#cor:c1){reference-type="ref" reference="cor:c1"}.* Since $P([f])$ consists of pseudo-Anosov braids with Dehornoy floor larger than three, Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} shows their closures are all hyperbolic knots. Proposition [\[prop:dehornoyfloor\]](#prop:dehornoyfloor){reference-type="ref" reference="prop:dehornoyfloor"} $(6)$ says braids having sufficiently large Dehornoy floor is a unique closed representative of its closure in braid index $n$, therefore $P([f])$ consists of infinite number of distinct hyperbolic knots and $P([f])$ and $P([g])$ have finite intersection unless $[g]$ is conjugate to $[f]$. ◻
:::

::: rem
Since every hyperbolic knots are represented as a closure of pseudo-Anosov braids, one might expects our construction of hyperbolic knots produces *all* hyperbolic knots; That is, for every hyperbolic knots, there exists pseudo-Anosov mapping class $[f]$ such that $K \in P([f])$. Unfortunately, this too optimistic conjecture is not true. For example, we can prove figure-eight knot, the most simple hyperbolic knots, do not appear as an element of $P([f])$. More generally, we can show genus one hyperbolic knots cannot be constructed from our method. This is a corollary of results of our subsequent paper [@i].
:::

Finally, we state a special case of theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} which simplifies the situation.

::: cor
[]{#cor:c2 label="cor:c2"} Let $p$ be a prime and $\beta \in B_{p}$ be a braid whose closure is a knot and $[\beta]_{D}\geq 3$. Then $\widehat{\beta}$ is a hyperbolic knot if and only if $\beta$ is non-periodic.
:::

::: proof
*Proof of corollary [\[cor:c2\]](#cor:c2){reference-type="ref" reference="cor:c2"}.* Since $p$ is prime and $\widehat{\beta}$ is a knot, $\beta$ is never reducible braid. Assume $\widehat{\beta}$ is satellite. Then proposition [\[prop:nbdsatellite\]](#prop:nbdsatellite){reference-type="ref" reference="prop:nbdsatellite"}, $\widehat{\beta}$ is braided-satellite, so theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} means $\beta$ is reducible, which contradicts above. Thus, under the assumption of corollary, $\widehat{\beta}$ is either hyperbolic or torus knot and $\beta$ is either periodic or pseudo-Anosov, so theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} establishes the result. ◻
:::

Although there is an algorithm to determine Nielsen-Thurston classification, it requires exponential times with respect to word length of braid. On the other hand, since to determine given braids are periodic or not is easy and it requires only quadratic times, corollary [\[cor:c2\]](#cor:c2){reference-type="ref" reference="cor:c2"} produces very many hyperbolic knots explicitly and rapidly. In particular, we conclude that for prime $p$, closure of braids $\beta \in B_{p}$ satisfying $[\beta]_{D} \geq 2$ are almost all hyperbolic knots.
