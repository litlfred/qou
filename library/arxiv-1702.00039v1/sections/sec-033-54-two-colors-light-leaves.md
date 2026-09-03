---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-033-54-two-colors-light-leaves
section_title: "Two colors light leaves"
section_number: 5.4
pages: 35-37
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In this section we will consider only two simple reﬂections, says andr, repre-
sented by two colors, say red and blue. We will explain a version of the Double
Leaves Theorem in two colors but only for reduced expressions (we will see
that the general version of this theorem (Theorem 5.4) does not restrict to re-
duced expressions neither in the source nor in the target). It is for simplicity of
exposition that we use reduced expressions.
We will call a full birdcage a morphism of the following type
Figure 24: Full birdcage
35
from a bimodule of the form BsBrBs··· to R. We call it “full” by using the
metaphor that it is full with “birds” (the dots), even though it is a bit sad to
think this in such terms, poor birds. The color of a full birdcage is the color of
the birdcage, not the color of the birds. In Figure 24 we have a red full birdcage.
A red dot will also be considered a red full birdcage (just think about the empty
cage).
Let us play the following game. Start with a red dot. In each step of the game,
each dot in our ﬁgure can be transformed into another full birdcage of the
same color. For example, we transform the red dot into Figure 24. Then we
transform Figure 24 into
Figure 25: Third step in our game
where we transformed the second and fourth blue dots into different full bird-
cages. Now we repeat this process
Figure 26: Fourth step in our game
were we transformed the ﬁrst, second, third and ﬁfth red dots into different
full birdcages. One can continue this process any number of times and every
map one can obtain in this way will be called a birdcagecage3 (so in particular,
any birdcage and any dot is a birdcagecage). If one adds a string as before,
a birdcagecage is called a hanging birdcagecage (again the degenerate case of a
3Strictly speaking, the map in Figure 26 should be called birdcagecagecage, but it
seems to us a bit impractical this name, so we stick with birdcagecage.
36
straight vertical line, the identity of someBs, will also be considered a hanging
birdcagecage).
Let W be a Dihedral group or a Universal Coxeter group in two generators
(examples C and D). Ifx =srs··· then we deﬁne the Bott-Samelson bimodule
Bx := BsBrBs··· . If we exclude the longest element for the Dihedral case
then every element has only one reduced expression, so we can just call this
bimoduleBx.
A two-color light leaf with source Bx is a morphism built-up in three zones.
The left zone (say zona A) is composed by birdcagecages. The middle zone
(say zone B) is composed by hanging birdcagecages. The right zone (say zone
C) is either empty or composed by just one birdcagecage. One example of a
two color light leaf is
Figure 27: Example of a two-color light leaf
We will call LLx(z) the two color light leaves with source Bx and target Bz .
The following is a version of the Double Leaves Theorem in two colors
Theorem 5.4 LetW be a ﬁnite or inﬁnite Dihedral group and x,y∈W . If W
is ﬁnite, let us pick x ory different fromw0. The set
⋃
z
LLy(z)a◦LLx(z)
is a basis of Hom(Bx,B y) as a rightR-module.
