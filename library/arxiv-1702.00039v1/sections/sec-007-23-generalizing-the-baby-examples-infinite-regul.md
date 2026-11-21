---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-007-23-generalizing-the-baby-examples-infinite-regul
section_title: "Generalizing the baby examples: (infinite) regular polygons"
section_number: 2.3
pages: 4-7
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.992
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
One natural way to generalize the baby examples is to consider the symmetries of a regular $n$-sided polygon. This is also a finite Coxeter group denoted $I_2(n)$ (the subindex $2$ in this notation denotes the rank of the Coxeter system, as defined in Section [\[Some definitions\]](#Some definitions){reference-type="ref" reference="Some definitions"}). A presentation of this group is given by

\(C\)

:   $I_2(n)= \langle s, r\ \vert \ s^2=r^2=e, \ (sr)^{n}=e\rangle,$

so $\mathrm{Symm}(\Delta)\cong I_2(3)$ and $\mathrm{Symm}(\square)\cong I_2(4).$ Again, one isomorphism here is given by sending $s$ to some reflection and $r$ to any of the "closest reflections to it"

<figure>
<div class="center">
<img src="polygon.png" />
</div>
<figcaption>Example with <span class="math inline"><em>n</em> = 8</span></figcaption>
</figure>

What is the *Infinite regular polygon*, the "limit\" in $n$ of the groups $I_2(n)$? A reasonable way to search for a geometric limit of the sequence of $n-$sided regular polygons, is to picture this sequence having "the same size" as in the figure

![The incorrect mental image](circle.png){width="\\linewidth"}

If we do so, the (pointwise) limit is a circle. On the other hand, the limit when $n$ goes to infinity of $I_2(n)$ is algebraically clear if we consider the presentation given in Example (C). It is the infinite group

::: description
$U_2=\langle s, r\ \vert \ s^2=r^2=e\rangle.$
:::

But the geometric and algebraic descriptions given here do not coincide! The group $\mathrm{Symm}(\bigcirc)$ of symmetries of the circle (usually called the orthogonal group $\mathrm{O}(2)$) is not even finitely generated. We have passed to a continuous group! The best we can do is to see $U_2$ as a dense subgroup of $\mathrm{Symm}(\bigcirc)$ (just consider $s$ and $r$ to be two \"random\" reflections of the circle).

There is a beautiful way to solve this problem: there is a discrete geometric limit of the sequence of $n-$sided regular polygons. Let us picture this sequence with one fixed side (in the figure, the darker one). Let us suppose that the fixed side has vertices in the points $(0,0)$ and $(0,1)$ of the plane.

![A new sequence](trueflower.png){width="\\linewidth"}

Then, if we make a "close up" around the darker side, and we put all the polygons together, we see

![The figure opens like flower](flower.png){width="\\linewidth"}

The (pointwise) limit is $\mathbb{R}$ with the vertices converging to the set $\mathbb{Z}$. The symmetries of this geometric object (that we call $(\mathbb{R}, \mathbb{Z})$) is isomorphic to $U_2$! One isomorphism is given by sending $s$ to the reflection through $0$ and $r$ to the reflection through $1/2$ (again "the closest reflection"). Now our geometric limit and the algebraic limit coincide and we can regain our lost calm.

For our fourth example, we just just raise the rank of $U_2$.

\(D\)

:   The *Universal Coxeter system of rank $n$* is the group $${U}_n=\langle s_1, s_2, \ldots, s_n\ \vert \ s_1^2=s_2^2=\cdots=s_n^2=e\rangle$$

This is the most complicated family of groups in which one can still compute all of the Kazhdan-Lusztig theory explicitly.
