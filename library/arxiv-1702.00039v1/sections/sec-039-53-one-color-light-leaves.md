---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-039-53-one-color-light-leaves
section_title: "One color light leaves"
section_number: 5.3
pages: 34-35
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.983
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
A *One Color Light Leaf* is a morphism built-up only with birdcages and dots. In the right-most position one can admit a hanging birdcage as in the picture.

<figure id="LL1">
<div class="center">
<img src="onecolorLL.png" />
</div>
<figcaption>Example of a one-color light leaf</figcaption>
</figure>

<figure id="LL2">
<div class="center">
<img src="onecolorLL2.png" />
</div>
<figcaption>Another example</figcaption>
</figure>

By definition a light leaf has two possible targets (as shown in figures [1](#LL1){reference-type="ref" reference="LL1"} and [2](#LL2){reference-type="ref" reference="LL2"}). It can be $B_s$ if it ends with a hanging birdcage or $R$ if not. We will call $LL_n(s)$ the light leaves with source $\underbrace{B_sB_sB_s\cdots}_{n \ \mathrm{times}}:=B_{s}^n$ and with target $B_s$, and $LL_n(e)$ the light leaves with the same source and target $R$.

For any morphism $f$ represented by a picture, one can flip the picture upside-down and thus obtain what we call the adjoint $f^a$, and this is again a well defined morphism with source and target flipped. For example, the adjoint of the morphism in Figure [2](#LL2){reference-type="ref" reference="LL2"} is the following

<figure>
<div class="center">
<img src="flip.png" />
</div>
</figure>

Now we can state the "one color" Double Leaves Theorem. This is a particular case of a Theorem proved for any Coxeter system in [@li3].

::: thm
[]{#DL label="DL"} The set $$LL_m(s)^a\circ LL_n(s)\bigcup LL_m(e)^a\circ LL_n(e)$$ is a basis of $\mathrm{Hom}(B_s^n,B_s^m)$ as a right $R$-module. The elements of this basis are called *double leaves.*
:::
