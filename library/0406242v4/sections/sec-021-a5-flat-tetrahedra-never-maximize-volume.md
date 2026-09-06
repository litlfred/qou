---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-021-a5-flat-tetrahedra-never-maximize-volume
section_title: "A.5 Flat tetrahedra never maximize volume"
section_number: null
pages: 37-40
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
---
The proof that the maximum ofV occurs in the interior of P closely tracks Section 7–
Section 9 of Gu´eritaud’s paper. We begin by ruling out many types of degeneracies on
∂ ¯P.
Lemma A.4 Let (w1,..., wc−1) be the point of ¯P at which the volume functionalV
attains its maximum. Then (wi) has the following properties:
(1) For each i, if one of xi, yi, zi is 0, then two are 0, ie ∆i is ﬂat.
Geometry &Topology 10 (2006)
1276 Franc ¸ois Gu´eritaud and David Futer
(2) If ∆i is ﬂat, then wi = 0.
(3) If ∆i is ﬂat, then i is a hinge index, not equal to 1 or c− 1.
(4) If ∆i is ﬂat, then i is adjacent to at least two consecutive identical letters.
(5) If both hinge layers at the ends of a syllable Rk or Lk are ﬂat, then k≥ 3.
Proof All the discussion and results of Section 7 apply equally well in our context.
Thus we have conclusion (1) as a restatement of Proposition 7.1. The domino effect of
Proposition 7.2 also applies; in fact, it is clear from the proof of the Proposition that the
domino effect works both forward and backward. Thus it does not matter that our word
Ω is not cyclic.
Almost all the claims of (2)–(5) are proved in Section 7, either in Proposition 7.3
or in the discussion that follows. The one exception is the claim that ∆1 and ∆c−1
cannot ﬂatten. This follows because, in the case of two-bridge links, w0 = wc =π/2.
Thus setting w1 or wc−1 to 0 or π/2 will trigger the domino effect and force all the
tetrahedra to ﬂatten, giving a volume of 0.
It remains to prove that at any point (wi)∈∂ ¯P satisfying the properties of Lemma A.4,
the volume will increase as we move into the interior of P. Following Gu´eritaud, we do
this using the geometrical statement of Lemma 8.2. The proof of this lemma transfers
perfectly to our context when the fan under consideration corresponds to a subword in
the interior of Ω. As it turns out, the same statement is even easier to prove when the
degenerate layer is near the beginning or end of Ω.
Lemma A.5 Recall the word Ω = Ra1La2··· , and suppose that the hinge layer ∆a1
has ﬂattened, with wa1 = 0. Then the fan corresponding to Ra1L admits a complete
Euclidean structure with boundary along Sa1 . Let Q, P, T be the lengths of the
segments of the broken line in which Sa1 intersects the cusp, as in Figure 20. Then
Q< P + T .
Of course, the analogous statement holds near the end of Ω.
Proof Note that, by Lemma A.4, we have a1≥ 2. For all 1 ≤ i≤ a1− 2, the
parameter wi can vary in a small interval, and no generality is lost in assuming that
∂V/∂wi = 0. (Otherwise, volume is easy to increase.) Then, as in the proof of
Lemma 8.2, the criticality of volume with respect to these parameters implies that the
fan of Ra1L has a complete Euclidean structure. If i> 1, the computation is the same
as in Sublemma 6.4. If i = 1, the angle z0 of Figure 7 is replaced by the hairpin turn,
Geometry &Topology 10 (2006)
Canonical triangulations 1277
1
12
a1/NUL1
a1/NUL1 Q
P
T
x
x
x
x
x
y
z
Figure 20: In a fan at the beginning of Ω, Q< P + T .
and the factor sin y0
sin x0
disappears from the computation of exp(−∂V/∂w1). Thus we once
again have 1 = exp(−∂V/∂w1) =|ψ(α)|, where ψ is the reduced holonomy and α is
a loop around the vertex at the hairpin turn.
In our situation, the fan of Ra1L is a (tessellated) Euclidean triangle, as in Figure 20, in
which Q and P + T are two of the sidelengths. In the triangular fan, the angle opposite
Q is x1 +... + xa1−1, while the angle opposite P + T is z1 + x1 +... + xa1−1. Thus,
because its side is opposite the smaller angle, Q< P + T .
Armed with Lemma 8.2 and its analogue in Lemma A.5, we can complete the proof
of Theorem A.1 by following the argument of Section 9. For each hinge index j with
wj = 0, we pick a vector along which to deform the neighboring parameters, in a way
that will maximize the derivative of volume. Deforming in this optimal direction with
speed ε, we can compute ∂V/∂ε in terms of the geometry of the fan(s) that adjoin ∆j.
In most situations, the exponentiated derivative appears as a product of the exact same
sine ratios as in Section 9. The only exception occurs when j = 2 or j = c− 2, because
there are no tetrahedra corresponding to w0 or wc. If (without loss of generality) j = 2,
the angle z0 is replaced by the hairpin turn, while the factor sin y0
sin x0
disappears from the
computation of P/T , just as in the proof of Lemma A.5. Thus ∂V/∂ε has the same
expression in terms of Q, Q′, P, P′, T, T′ as in Section 9.
In every case, the geometric statement Q< P + T , applied to two fans if necessary,
implies that ∂V/∂ε > 0. Therefore V is maximized at a critical point where all
tetrahedron angles are positive, completing the proof of Theorem A.1.
Geometry &Topology 10 (2006)
1278 Franc ¸ois Gu´eritaud and David Futer
