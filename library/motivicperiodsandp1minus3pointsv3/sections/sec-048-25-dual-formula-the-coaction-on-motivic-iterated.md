---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-048-25-dual-formula-the-coaction-on-motivic-iterated
section_title: "Dual formula. The coaction on motivic iterated integrals is dual to"
section_number: 2.5
pages: 13-14
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta values."
---
Ihara’s formula. Dualising (2 .17), we have
∆ : O(0Π 1) − → O(U dR) ⊗ O(0Π 1)
It is equivalent, but more convenient, to consider the inﬁni tesimal coaction
D : O(0Π 1) − → L ⊗ O(0Π 1)
(
D(x) = ∆( x) − 1 ⊗ x mod O(U dR)2
>0
)
where L = O(U dR)>0/
(
O(U dR)>0
) 2
is the Lie coalgebra of indecomposables in
O(U dR). The following formula is an inﬁnitesimal variant of a form ula due to
Goncharov [20], relating to slightly diﬀerent objects. In o rder to ﬁll a gap in the
literature, I will sketch how it follows almost immediately from Ihara’s formula.
Proposition 2.6. Let a0, . . . , an+1 ∈ {0, 1}. The coaction D is given by
D(I m(a0; a1, . . . , an; an+1)) =
∑
0≤p<q≤n
[
I u(ap; ap+1, . . . , aq; aq+1)
]
(2.18)
⊗ I m(a0; a1, . . . , ap, aq+1, . . . , an; an+1) .
where the square brackets on the left denote the map [ ] : O(U dR)>0 → L.
Proof. Denote the action of Lie A on Lie 0Π 0 by ◦0. By (2 .11), Lie A ∼
= Lie 0Π 1
is the set of primitive elements in its (completed) universa l enveloping algebra
which we denote simply by U(0Π 1). By (2 .13) and (2 .14) we have a ◦0 x0 = 0 and
a ◦0 x1 = ax1 − x1a. The antipode on U(0Π 1) is given by the signed reversal ∗.
Since a ∈ U (0Π 1) is primitive, a = −a∗ and also
a ◦0 x0 = 0 and a ◦0 x1 = ax1 + x1a∗ .
This extends to an action on U(0Π 0) via a ◦0 w1w2 = ( a ◦0 w1)w2 + w1(a ◦0 w2).
Now consider the action a ◦0 ·on the following words. All terms are omitted except
those terms where a or a∗ is inserted in-between the two bold letters:
a ◦0 w1x0x0w2 = · · ·+ 0 + · · ·
a ◦0 w1x0x1w2 = · · ·+ w1x0ax1w2 + · · ·
a ◦0 w1x1x0w2 = · · ·+ w1x1a∗x0w2 + · · ·
a ◦0 w1x1x1w2 = · · ·+ w1x1ax1w2 + w1x1a∗x1w2/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
0
+ · · ·
These four equations are dual to all but the ﬁrst and last term s in (2 .18), using
the fact that I u(x; w; x) = 0 for x = 0, 1 (ﬁrst and fourth lines), and the fact that
I u(1; w∗; 0) = I u(0; w; 1) (third line). A straightforward modiﬁcation of the abov e
argument taking into account the initial and ﬁnal terms (usi ng (2 .15)) shows that
the action ◦1 of Lie A on 0Π 1 is dual to the full expression (2 .18).
