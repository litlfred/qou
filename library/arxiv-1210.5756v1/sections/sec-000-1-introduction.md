---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.889
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Let $\mathbb{E}^{d}$ denote $d$-dimensional Euclidean space. Then the *contact graph* of an arbitrary finite packing of unit balls (i.e., of an arbitrary finite family of non-overlapping balls having unit radii) in $\mathbb{E}^{d}$ is the (simple) graph whose vertices correspond to the packing elements and whose two vertices are connected by an edge if and only if the corresponding two packing elements touch each other. One of the most basic questions on contact graphs is to find the maximum number of edges that a contact graph of a packing of $n$ unit balls can have in $\mathbb{E}^{d}$. In 1974 Harborth [@Ha] proved the following optimal result in $\mathbb{E}^{2}$: the maximum number of touching pairs in a packing of $n$ congruent circular disks in $\mathbb{E}^{2}$ is precisely $\lfloor 3n-\sqrt{12n-3}\rfloor$. In dimensions three and higher only estimates are known for the maximum number of touching pairs. In particular, just very recently the first named author [@B12] proved that the number of touching pairs in an arbitrary packing of $n$ unit balls in $\mathbb{E}^{3}$ is always less than $6n-0.695n^{\frac{2}{3}}$. Moreover, it is proved in [@B02] that for $d\ge4$ the number of touching pairs in an arbitrary packing of $n$ unit balls in $\mathbb{E}^{d}$ is less than $$\frac{1}{2}\tau_d\, n-\frac{1}{2^{d}}\delta_d^{-\frac{d-1}{d}}\; n^{\frac{d-1}{d}},$$ where $\tau_d$ stands for the kissing number of a unit ball in $\mathbb{E}^{d}$ (i.e., it denotes the maximum number of non-overlapping unit balls of $\mathbb{E}^{d}$ that can touch a given unit ball in $\mathbb{E}^{d}$) and $\delta_d$ denotes the largest possible density for (infinite) packings of unit balls in $\mathbb{E}^{d}$. For a nice survey on recognition-complexity results of ball contact graphs we refer the interested reader to [@HK01].

In this paper, first we improve the above quoted upper bound of [@B12] as follows.

::: Theorem
[]{#improved-estimate label="improved-estimate"}

\(i\) The number of touching pairs in an arbitrary packing of $n\ge 2$ unit balls in $\mathbb{E}^{3}$ is always less than $6n-0.926n^{\frac{2}{3}}$.

\(ii\) The number of touching pairs in an arbitrary lattice packing of $n\ge 2$ unit balls in $\mathbb{E}^{3}$ is always less than $6n-\frac{3\sqrt[3]{18\pi}}{\pi}n^{\frac{2}{3}}=6n-3.665\dots n^{\frac{2}{3}}$.
:::

In connection with Theorem [\[improved-estimate\]](#improved-estimate){reference-type="ref" reference="improved-estimate"} we recall from [@B12] that for all $n=\frac{2k^{3} +k}{3}, k \geq 2$, there are packings of $n$ unit balls in $\mathbb{E}^3$ such that the number of touching pairs is greater than $6n-\sqrt[3]{486}n^{\frac{2}{3}}=6n-7.862\dots n^{\frac{2}{3}}$.

Second, as a natural extension of the above discussed problem on the number of touching pairs, we propose to study the maximum number of touching triplets, quadruples, etc. in an arbitrary packing of $n$ unit balls in $\mathbb{E}^{d}$. Harborth's proof [@Ha] implies in a straightforward way that the maximum number of touching triplets in a packing of $n$ congruent circular disks in $\mathbb{E}^{2}$ is precisely $\lfloor 3n-\sqrt{12n-3}\rfloor-n+1$. In this paper we study the $3$-dimensional case of the problem at hand and prove the following estimates.

::: Theorem
[]{#main-theorem label="main-theorem"}

\(i\) The number of touching triplets (resp., quadruples) in an arbitrary packing of $n\ge 3$ (resp., $n\ge 4$) unit balls in $\mathbb{E}^3$ is at most $\frac{25}{3}n$ (resp., $\frac{11}{4}n$).

\(ii\) The number of touching triplets (resp., quadruples) in an arbitrary lattice packing of $n\ge 2$ unit balls in $\mathbb{E}^{3}$ is at most $8n$ (resp., $2n$).

\(iii\) For all $n=\frac{2k^{3} +k}{3}, k \geq 2$, there are packings of $n$ unit balls (with their centers lying on a face-centered cubic lattice) in $\mathbb{E}^3$ such that the number of touching triplets (resp., quadruples) is $$\frac{4}{3}(k-1)k(4k-5)>8n - 12\left(\frac{3}{2}n\right)^{2/3}+4n^{1/3}\ \ \ \ ({\rm resp}.,\ \frac{4}{3}(k-2)(k-1)k>2n-4(\frac{3}{2}n)^{2/3} + 2n^{1/3})\ .$$
:::

Part $(iii)$ of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} raises the following question.

::: Problem
Prove or disprove the existence of a positive integer $k_3$ (resp., $k_4$) with the property that for any positive integer $k\ge k_3$ (rep., $k\ge k_4$) the number of touching triplets (resp., quadruples) in an arbitrary packing of $\frac{2k^3+k}{3}$ unit balls in $\mathbb{E}^3$ is at most $\frac{4}{3}(k-1)k(4k-5)$ (resp., $\frac{4}{3}(k-2)(k-1)k$).
:::

The proof of $(i)$ in Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} is based on the following statement that might be of independent interest in particular, because one can regard that statement as a spherical analogue of Harborth's theorem [@Ha] for the angular radius $\pi/6$ (on the unit sphere $\mathbb{S}^2$ centered at the origin in $\mathbb{E}^3$).

::: Theorem
[]{#spherical-main-theorem label="spherical-main-theorem"} The number of touching pairs (resp., triplets) in an arbitrary packing of spherical caps of angular radius $\pi/6$ on $\mathbb{S}^2$ is at most $25$ (resp., $11$).
:::

In connection with Theorem [\[spherical-main-theorem\]](#spherical-main-theorem){reference-type="ref" reference="spherical-main-theorem"} we put forward the following question.

::: Problem
[]{#main-conjecture label="main-conjecture"} Prove or disprove that the number of touching pairs (resp., triplets) in an arbitrary packing of spherical caps of angular radius $\pi/6$ on $\mathbb{S}^2$ is at most $24$ (resp., $10$).
:::

We note that a positive answer to Problem [\[main-conjecture\]](#main-conjecture){reference-type="ref" reference="main-conjecture"} implies the following improvement on the estimates in $(i)$ of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"}: the number of touching triplets (resp., quadruples) in an arbitrary packing of $n$ unit balls in $\mathbb{E}^3$ is at most $8n$ (resp., $\frac{5}{2}n$).

Due to the Minkowski difference body method (see for example, Chapter 6 in [@Ro64]) the family ${\cal P}_{\mathbf{K}}:=\{\mathbf{t}_1+\mathbf{K}, \mathbf{t}_2+\mathbf{K}, \dots , \mathbf{t}_n+\mathbf{K}\}$ of $n$ translates of the convex body $\mathbf{K}$ in $\mathbb{E}^3$ is a packing if and only if the family ${\cal P}_{\mathbf{K}_{\mathbf{o}}}:=\{\mathbf{t}_1+\mathbf{K}_{\mathbf{o}}, \mathbf{t}_2+\mathbf{K}_{\mathbf{o}}, \dots , \mathbf{t}_n+\mathbf{K}_{\mathbf{o}}\}$ of $n$ translates of the symmetric difference body $\mathbf{K}_{\mathbf{o}}:=\frac{1}{2}(\mathbf{K}+(-\mathbf{K}))$ of $\mathbf{K}$ is a packing in $\mathbb{E}^3$. Moreover, the number of touching pairs, triplets, and quadruples in the packing ${\cal P}_{\mathbf{K}}$ is equal to the number of touching pairs, triplets, and quadruples in the packing ${\cal P}_{\mathbf{K}_{\mathbf{o}}}$. Thus, for this reason and for the reason that if $\mathbf{K}$ is a convex body of constant width in $\mathbb{E}^3$, then $\mathbf{K}_{\mathbf{o}}$ is a ball of $\mathbb{E}^3$, Theorem [\[improved-estimate\]](#improved-estimate){reference-type="ref" reference="improved-estimate"} as well as Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} extend in a straightforward way to translative packings of convex bodies of constant width in $\mathbb{E}^3$.

The rest of the paper is organized as follows. In Section 2 we prove $(i)$ of Theorem [\[improved-estimate\]](#improved-estimate){reference-type="ref" reference="improved-estimate"}. Section 3 proves $(ii)$ of Theorem [\[improved-estimate\]](#improved-estimate){reference-type="ref" reference="improved-estimate"} as well as $(ii)$ of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"}. In Section 4 we give a short proof of $(i)$ in Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} using Theorem [\[spherical-main-theorem\]](#spherical-main-theorem){reference-type="ref" reference="spherical-main-theorem"}. Sections 5 and 6 present our elementary and somewhat computational proof of Theorem [\[spherical-main-theorem\]](#spherical-main-theorem){reference-type="ref" reference="spherical-main-theorem"}. Finally, Section 7 gives a proof of $(iii)$ in Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} as well as shows that if Problem [\[main-conjecture\]](#main-conjecture){reference-type="ref" reference="main-conjecture"} has a positive answer, then its estimates are tight.
