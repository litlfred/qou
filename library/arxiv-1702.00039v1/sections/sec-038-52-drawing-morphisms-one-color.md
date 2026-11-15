---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-038-52-drawing-morphisms-one-color
section_title: "Drawing morphisms: one color"
section_number: 5.2
pages: 31-34
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.973
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
We fix a simple reflection $s\in S.$ We will start by explaining how to represent in a drawing a morphism between "one color Bott-Samelson bimodules", i.e. bimodules having only $s$ in its expression, for example $B_sB_sB_sB_s.$

Morphisms will be drawn inside the strip $\mathbb R\times [0,1]\subset \mathbb R^2.$ This will be done in a bottom-up way, i.e. in the line $\mathbb R\times \{0\}$ we will draw the same number of points as the number of $B_s$ that appear in the source of our morphism and in the line $\mathbb R\times \{1\}$ we will draw the same number of points as the number of $B_s$ that appear in the target of our morphism (the bimodule $R$ is represented by the empty sequence). Here a list of examples were the lower black line is always $\mathbb R\times \{0\}$ and the upper black line is $\mathbb R\times \{1\}$ (recall the morphisms in [\[dec\]](#dec){reference-type="ref" reference="dec"}).

<figure>
<div class="center">
<img src="mor.png" />
</div>
<figcaption>Important morphisms</figcaption>
</figure>

We call $m_s$ and $m_s^a$ the *dots* and $j_s$ and $j_s^a$ the *trivalent vertices*. We will not longer draw the lines$\mathbb R\times \{0\}$ and $\mathbb R\times \{1\}$, but we will assume that they exist. A tensor product of morphisms is represented by glueing pictures, for example

<figure>
<div class="center">
<img src="tensor.png" />
</div>
<figcaption>Tensor product</figcaption>
</figure>

represents the morphism $j_s\otimes \mathrm{id}\otimes m_s\otimes j_s^a:B_sB_sB_sB_sB_s\rightarrow B_sB_sB_sB_s$. Composition is represented by glueing bottom-up in the obvious way. For example

<figure>
<div class="center">
<img src="composition.png" />
</div>
<figcaption>Composition</figcaption>
</figure>

represents the morphism $j_s\circ (j_s\otimes \mathrm{id})$. We introduce the following notation

<figure>
<div class="center">
<img src="capcup.png" />
</div>
<figcaption>Cup and cap</figcaption>
</figure>

The left-hand side morphism will be called the *cup* and the right-hand side the *cap*. It is easy to verify that $j_s\circ (j_s\otimes \mathrm{id})=j_s\circ ( \mathrm{id}\otimes j_s)$, or in pictures

<figure>
<div class="center">
<img src="associativity.png" />
</div>
<figcaption>Associativity</figcaption>
</figure>

This, of course means that any composition of $j_s$ tensored by identities in any order will give the same morphism, for example

<figure>
<div class="center">
<img src="exasso.png" />
</div>
</figure>

Given that there is no ambiguity and all these pictures represent the same morphism, we will denote this morphism by a comon picture that we call the *hanging birdcage* [^1]

<figure>
<div class="center">
<img src="hangingbirdcage.png" />
</div>
<figcaption>Hanging birdcage</figcaption>
</figure>

The identity of $B_s$ (a vertical line) is also considered a hanging birdcage. If we compose this morphism with a dot we obtain the *non-hanging birdcage* or simply, the *birdcage.*

<figure>
<div class="center">
<img src="bc.png" />
</div>
<figcaption>Birdcage</figcaption>
</figure>

The *length* of a birdcage is the number of $B_s$ that it has in its source. In the example, it is a length 5 birdcage. A dot is a length 1 birdcage.

[^1]: The "birdcage" terminology is non-standard and used for the first time in this paper.
