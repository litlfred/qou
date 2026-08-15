---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-012-appendix-b-braid-closures
section_title: "Appendix B. Braid closures"
section_number: null
pages: 21-23
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
In this section we explain how to find a flattening of the collapsed triangulation T˚D when
˚D is given by a closure of a braid, more precisely, when ˚D is an open diagram obtained
22 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
x1
∞
x5
x2
x3
x4
0
1
1
1
1
Figure 18. An open diagram of the knot 6 1.
from a braid by taking the closure of all strands except the first one. See Figure 18 for an
example.
The triplef given in Equation (10) still satisfies Lemma 4.2, but not Lemma 4.3. Precisely,
if we repeat the proof of Lemma 4.3, we obtain the following: for an R-edge e, we have
⟨f,e⟩ = 0 if e corresponds to the innermost region, created by closing up the last strand of
the braid; otherwise,⟨f,e⟩ = 2. See, for instance, Figure 18 that the innermost region does
not have a crossing whose N or S-corner lies in the region.
To make⟨f,e⟩ = 2 hold for all R-edges e, we use the following lemma.
Lemma B.1. Let ei and ej be two edges of T˚D that correspond to adjacent regions. Then
there is a triple h = (h,h′,h′′) of vectors such that hj +h′
j +h′′
j = 0 and
⟨f +h,e⟩−⟨ f,e⟩ =



−1 if e =ei
1 if e =ej
0 otherwise
In addition, such h can be chosen independently of f.
Proof. Let ri and rj be the regions corresponding to the edges ei and ej, respectively. As
they are adjacent, we can find two adjacent corners, with one lying in ri and the other in rj.
If these corner are separated by an underpass, then we define h by assigning integer triples
to the corners as in Figure 19 (left); if by an overpass, as in Figure 19 (right).
Then from the first coordinate of triples, we deduce that
⟨f +h,ei⟩ =⟨f,ei⟩− 1, ⟨f +h,ej⟩ =⟨f,ej⟩ + 1.
The change of the second and third coordinates affects two edges, one U-edge and one O-edge,
but both receive one +1 and one −1, resulting in a total of 0. □
Remark B.2. Adjacent regions have a segment in common, and the proof of Lemma B.1
works for any pair of corners at one end of the segment. In particular, a choice of h may
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 23
ri rj
 ri rj
(1, 0,−1)(−1, 1, 0)
(1,−1, 0)(−1, 0, 1)
Figure 19. A choice of h.
not be not unique. However, regardless of a choice of h, the product ζh is invariant (see
Remark 4.6). Moreover,ζh for Figure 19 agrees with the inverse of what Ohtsuki and Takata
referred to as α in [OT15] that is assigned to the segment.
Roughly speaking, Lemma B.1 allows us to take one contribution from a region and give
it to an adjacent region, and thus to any region, by applying the lemma multiple times. We
take one contribution from a region adjacent to an ∞-segment and give it to the innermost
region. This can be done by (a) following ∞-segments to reach the unbounded region and
then (b) by passing through the caps, illustrated as in Figure 20. Similarly, we take one
∞
(a)
(b) ···
...
Figure 20. From a region adjacent to s∞ to the innermost region.
contribution from a region adjacent to a 0-segment and give it to the innermost region, by
following 0-segments and passing through the cups. This results in a triple h such that
⟨f +h,e⟩ = 2 for all C and R-edges e.
For O and U-edges, we can use Lemma 4.4 as we did in Section 4.1. This results in another
tripleg such that
⟨f +h +g,e⟩ =
(
⟨f +h,e⟩ if e is a C or R-edge
2 if e is an O or U-edge .
Namely,f +h +g is a flattening ofT˚D.
