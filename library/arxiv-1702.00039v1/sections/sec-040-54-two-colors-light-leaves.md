---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-040-54-two-colors-light-leaves
section_title: "Two colors light leaves"
section_number: 5.4
pages: 35-37
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.993
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In this section we will consider only two simple reflections, say $s$ and $r$, represented by two colors, say red and blue. We will explain a version of the Double Leaves Theorem in two colors but only for reduced expressions (we will see that the general version of this theorem (Theorem [\[DL\]](#DL){reference-type="ref" reference="DL"}) does not restrict to reduced expressions neither in the source nor in the target). It is for simplicity of exposition that we use reduced expressions.

We will call a *full birdcage* a morphism of the following type

<figure id="fbc">
<div class="center">
<img src="fbc.png" />
</div>
<figcaption>Full birdcage</figcaption>
</figure>

from a bimodule of the form $B_sB_rB_s\cdots$ to $R$. We call it "full" by using the metaphor that it is full with "birds" (the dots), even though it is a bit sad to think this in such terms, poor birds. The *color* of a full birdcage is the color of the birdcage, not the color of the birds. In Figure [1](#fbc){reference-type="ref" reference="fbc"} we have a red full birdcage. A red dot will also be considered a red full birdcage (just think about the empty cage).

Let us play the following game. Start with a red dot. In each step of the game, each dot in our figure can be transformed into another full birdcage of the same color. For example, we transform the red dot into Figure [1](#fbc){reference-type="ref" reference="fbc"}. Then we transform Figure [1](#fbc){reference-type="ref" reference="fbc"} into

<figure id="fbc2">
<div class="center">
<img src="fbc2.png" />
</div>
<figcaption>Third step in our game</figcaption>
</figure>

where we transformed the second and fourth blue dots into different full birdcages. Now we repeat this process

<figure id="fbc3">
<div class="center">
<img src="fbc3.png" />
</div>
<figcaption>Fourth step in our game</figcaption>
</figure>

were we transformed the first, second, third and fifth red dots into different full birdcages. One can continue this process any number of times and every map one can obtain in this way will be called a *birdcagecage*[^1] (so in particular, any birdcage and any dot is a birdcagecage). If one adds a string as before, a birdcagecage is called a *hanging birdcagecage* (again the degenerate case of a straight vertical line, the identity of some $B_s$, will also be considered a hanging birdcagecage).

Let $W$ be a Dihedral group or a Universal Coxeter group in two generators (examples C and D). If $\underline{x}= srs\cdots$ then we define the Bott-Samelson bimodule $B_{\underline{x}}:=B_sB_rB_s\cdots$. If we exclude the longest element for the Dihedral case then every element has only one reduced expression, so we can just call this bimodule $B_x$.

A *two-color light leaf* with source $B_x$ is a morphism built-up in three zones. The left zone (say zona A) is composed by birdcagecages. The middle zone (say zone B) is composed by hanging birdcagecages. The right zone (say zone C) is either empty or composed by just one birdcagecage. One example of a two color light leaf is

<figure id="tcll">
<div class="center">
<img src="tcll.png" />
</div>
<figcaption>Example of a two-color light leaf</figcaption>
</figure>

We will call $LL_{x}(z)$ the two color light leaves with source $B_x$ and target $B_z$. The following is a version of the Double Leaves Theorem in two colors

::: thm
[]{#DL label="DL"} Let $W$ be a finite or infinite Dihedral group and $x,y\in W$. If $W$ is finite, let us pick $x$ or $y$ different from $w_0$. The set $$\bigcup_{z} LL_y(z)^a\circ LL_x(z)$$ is a basis of $\mathrm{Hom}(B_x,B_y)$ as a right $R$-module.
:::

[^1]: Strictly speaking, the map in Figure [3](#fbc3){reference-type="ref" reference="fbc3"} should be called birdcagecagecage, but it seems to us a bit impractical this name, so we stick with birdcagecage.
