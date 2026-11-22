---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-019-a1-braids-and-two-bridge-links
section_title: "A.1 Braids and two-bridge links"
section_number: null
pages: 30-31
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Braids and two-bridge links
Let S be a 4–punctured sphere, visualized concretely as a square pillowcase with
the corners removed. A 4–string braid between two pillowcases, one interior and
one exterior, deﬁnes a so-called product region S×I. We will restrict our attention to
alternating braids in which the top right strand is free of crossings. (See Figure 13 (a).)

(a)
(b)
Figure 13: (a) An alternating braid between two pillowcases, described by the word Ω= R3L2R
(b) The corresponding two-bridge link K(Ω)
The mapping class ϕ: S →S induced by this braid can be described by a word
Ω:=
 Ra1La2 · · · Ran
or
La1Ra2 · · · Lan
with odd n, or
Ra1La2 · · · Lan
or
La1Ra2 · · · Ran
with even n.
Here, R encodes a crossing on the bottom pair of strands, and L encodes a crossing
on the left pair of strands, as in Figure 14. Each syllable of Ω(that is, each maximal
subword Rai or Lai ) corresponds to a twist region in which two strands of the braid
wrap around each other ai times. As we read Ωfrom left to right, we scan the crossings
from the outside in. Note that, unlike the case of punctured torus bundles, our word Ω
has a beginning and an end. For concreteness, we will focus on the case when Ωstarts
with R, as in Figure 13 (a); the L–case is similar.

R
L
Figure 14: The letters R and L acting on strands of a braid
Geometry & Topology 10 (2006)
Canonical triangulations
1269
An alternating braid of this sort can be completed to a link diagram, as follows. Outside
the outer pillowcase, we connect the bottom left strand to the top right, and the bottom
right strand to the top left, adding an extra crossing. (Up to isotopy of S2, there is a
unique way to do this while keeping an alternating projection. In Figure 13 (b), the
extra crossing was arbitrarily placed at the bottom of the diagram.) Similarly, inside the
inner pillowcase we connect the strands in a diagonal fashion, adding an extra crossing
while preserving the alternating projection. This creates an alternating link K(Ω), as in
Figure 13 (b).
K is called a two-bridge link because this diagram can be isotoped so that the pillowcases
are horizontal, and the connecting strands form two bridges between the strands of
the braid. It is well-known that, apart from the trivial link of one or two components,
every two-bridge link can be constructed in this way. (See, for example, Murasugi [19,
Theorems 9.3.1 and 9.3.2].)
William Menasco’s theorem about hyperbolic alternating links [15] contains the follow-
ing special case.
Theorem A.1 The two-bridge link K(Ω) is hyperbolic if and only if Ωhas two or
more syllables.
Just as with punctured torus bundles, we will give a direct proof of the “if” direction of
this theorem by ﬁnding a geometric ideal triangulation of the link complement. The
“only if” direction is immediate: a word with a single syllable produces a link with a
single twist region, which must be a torus link.
