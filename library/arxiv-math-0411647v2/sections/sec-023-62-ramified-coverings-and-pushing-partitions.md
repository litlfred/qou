---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-023-62-ramified-coverings-and-pushing-partitions
section_title: "Ramified coverings and pushing partitions"
section_number: 6.2
pages: 53-57
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.978
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#subsec:okounkov label="subsec:okounkov"}

### Ramified covering and an admissible sequence

Suppose that an admissible sequence $a_1,\dots,a_n\in\{1,2,\dots,q\}$ is given. Following the idea of Okounkov [@Okounkov2000randompermutations] we consider a two--dimensional sphere ${\mathbb{S}}^2$ with distinguished points $0,1,2,\dots,n,\infty$. Figure [1](#fig:sfera){reference-type="ref" reference="fig:sfera"} depicts a small region on this sphere (unfortunately, some conventions used in the pictures in this article do not coincide with the ones of Okounkov).

![Two homotopic loops on a sphere.](figure28.eps){#fig:sfera}

Let $\mathsf{S}$ be an oriented surface. We shall consider a covering $\mathsf{S}\rightarrow{\mathbb{S}}^2$ with simple ramifications over points $1,2,\dots,n$ and an unspecified ramification over $0$. We consider $n+1$ cuts from points $0,1,2,\dots,n$ to $\infty$. We choose $\mathsf{S}$ in such a way that in the fiber over any point not lying on a cut there are $q+1$ sheets marked $1,2,\dots,q,\ast$. Sheet $\ast$ will be called special sheet. We also require that the monodromy around any point $k\in\{1,\dots,n\}$ be a transposition of the sheet $a_k$ and the sheet $\ast$. Since a loop around $0$ is homotopic to a loop around points $1,2,\dots,n$ hence the monodromy around $0$ is a product of monodromies around $1,\dots,n$ and hence is equal to $(a_1 \ast)\cdots(a_n \ast)$ (cf Figure [1](#fig:sfera){reference-type="ref" reference="fig:sfera"}). The difference with the situation from the paper [@Okounkov2000randompermutations] is that we do not assume that $(a_1 \ast)\cdots (a_n \ast)=e$ and for this reason we might have a non--trivial ramification in $0$ and therefore we need the extra cut between $0$ and $\infty$, not present in [@Okounkov2000randompermutations].

### Shape of the special sheet

Since the sequence $a_1,\dots,a_n$ is admissible, hence the monodromy around $0$ preserves the special sheet. It follows that when we consider only cuts from points $1,2,\dots,n$ to $\infty$ then $\mathsf{S}$ splits into the special sheet and the union of non--special sheets (which are, possibly, glued together along the cut between $0$ and $\infty$). Let us have a look on the shape of the special sheet. Along the cuts from $1,2,\dots,n$ to $\infty$ it is glued with non--special sheets and we are not interested how does this gluing look like. Much more interesting is the vertex $\infty$ since some points on the boundary of the special sheet might be glued there together.

![A loop on a sphere.](figure29.eps){#fig:ugaugauga}

To check if two vertices: the one between $k-1$ and $k$ and the one between $l-1$ and $l$ are glued together or not, we consider a loop as on Figure [2](#fig:ugaugauga){reference-type="ref" reference="fig:ugaugauga"}. To indicate better the shape of the special sheet we inflated slightly the cuts. Our question is equivalent to the following one: is it true that the monodromy along this loop preserves the special sheet. This holds if and only if $$\big((a_{k} \ast)(a_{k+1} \ast)\cdots (a_{l-1} \ast)\big)^{-1}(\ast)=\ast$$ which is equivalent to $$p_k=\big((a_{k} \ast)(a_{k+1} \ast) \cdots (a_{n} \ast)\big)^{-1}(\ast)=
                      \big( (a_{l} \ast)  \cdots (a_{n} \ast) \big)^{-1}(\ast)=p_l,$$ where $p_1,\dots,p_n$ is the corresponding pushing sequence.

<figure id="fig:specjalneprzescieradlo">
<embed src="figure30.eps" />
<figcaption>Shape of the special sheet (the white region).</figcaption>
</figure>

It follows that the special sheet looks as it is depicted on Figure [3](#fig:specjalneprzescieradlo){reference-type="ref" reference="fig:specjalneprzescieradlo"}, where points $p_1,p_2,\dots$ all cover $\infty$ and those of them which carry the same labels should be glued together. The pushing partition $\pi$ corresponding to the pushing sequence $p_1,\dots,p_n$ can be therefore identified as a receipt for gluing vertices $p_1,\dots,p_n$ of the special sheet covering $\infty$. The meaning of the additional labeling of the edges will be explained below.

### Collapsing non--special sheets {#subsec:collapsing}

Let us inflate the point $\infty$ a little bit (or---speaking more precisely---while performing cuts from points $1,2,\dots,n$ to $\infty$ let us leave some neighborhood of $\infty$ untouched). The special sheet becomes now an oriented surface with a boundary which coincides with a construction from Section [\[subsec:zaklejanie\]](#subsec:zaklejanie){reference-type="ref" reference="subsec:zaklejanie"} where we glued a hole in a sphere with the first collection of discs

(see also Figure 22 in [@Okounkov2000randompermutations]).

Let us collapse the union of non--special sheets (for details of this construction we refer to [@Okounkov2000randompermutations]). After this operation the $2n$ edges of the special sheet (denoted by $1,1',2,2',\dots,n,n'$) become glued together in pairs. We know that the vertices $p_1,\dots,p_n$ are glued together according to the pushing partition $\pi$; this implies that the edges of the special sheet are glued according to the pair partition $\pi_{\mathop{\mathrm{fat}}}$. This provides an alternative description of the Okounkov's mapping $\Psi$ from coverings to maps on surfaces.

A careful reader will notice that the above statement is not completely true: the reason is that Okounkov collapses non--special sheets with two edges in a different way than the non--special sheets with three or more edges. This means that in fact in the process of computing $\pi_{\mathop{\mathrm{fat}}}$ we should treat two--element blocks of $\pi$ differently. We leave the details as an exercise to the reader.

### Many Jucys--Murphy elements

In this article we deal with only one Jucys--Murphy element $J$ while in the work [@Okounkov2000randompermutations] one considers products of many such elements $J_1,J_2,\dots$ and therefore a careful reader might wonder if our methods are general enough. However, one can easily translate Okounkov's statements concerning products of many Jucys--Murphy elements into our favorite language of products of moments of a single Jucys--Murphy element which translates easily into properties of corresponding pushing partitions.

### The case $(a_1 \ast) \cdots (a_n \ast)=e$

Suppose now that $(a_1 \ast)\cdots(a_n \ast)=e$. It follows that the construction from Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"} assigns to every cycle $b_s$ of the permutation $\pi_{\mathop{\mathrm{fat}}} \circ c$ the number $k_s=1$ (otherwise $(a_1 \ast)\cdots(a_n \ast)$ would have a non--trivial cycle). Now we see from [\[eq:formulanakk\]](#eq:formulanakk){reference-type="eqref" reference="eq:formulanakk"} that it is equivalent to the statement that every cycle $b_s$ of the product $\pi_{\mathop{\mathrm{fat}}}\circ c$ makes exactly one counterclockwise wind around the circle.

As in Section [0.0.3](#subsec:collapsing){reference-type="ref" reference="subsec:collapsing"} let us collapse the non--special sheets; the $2n$ vertices of the polygon representing the special sheet fall into two classes: those which were covering $\infty$ (and which correspond to glued vertices $p_1,\dots,p_n$) and those corresponding to the ramification points $1,2,\dots,n$. Suppose we are going clockwise around the boundary of the polygon constituting the special sheet and thus we visit vertices in the order $n,p_n,n-1,p_{n-1},\dots,1,p_1$; let us have a look in which order we visit corners which meet in one of the vertices of the second class. One can see that the edges which meet in such a vertex correspond to one of the polygons which constitute the boundary of the special sheet after gluing in $\infty$ or---in other words---to one of the cycles of $\pi_{\mathop{\mathrm{fat}}}\circ c$. From our previous discussion it follows that the corners will be visited in the counterclockwise order; in Okounkov's notation this means that the vertex is left.

Every group of the first class of vertices (covering $\infty$) which is glued together corresponds to one of the blocks of the partition $\pi$.

It follows that they will be visited in a clockwise order; in Okounkov's notation this means that the vertex is right.

The above classification of vertices into the class of left and the class of right ones is one of the key points of the paper [@Okounkov2000randompermutations] and it is interesting that we were able to reconstruct this result by the techniques of pushing partitions.
