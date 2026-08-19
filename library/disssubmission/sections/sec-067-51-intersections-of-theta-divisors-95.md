---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-067-51-intersections-of-theta-divisors-95
section_title: "Intersections of theta divisors 95"
section_number: 5.1
pages: 103-105
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
THEOREM 5.2. If C is a general curve of genus g= 2n, then G(dn) is
either the alternating groupAN or the full symmetric groupSN.
The proof of this in section 5.8 again uses a degeneration, this time
from a general curve into a hyperelliptic one. We also remark that if the
Galois groupG(dn) in the above theorem is the full symmetric groupSN,
then also the monodromy groupG in the previous theorem has to be the
full Weyl groupW(E6) because it then contains a reﬂection. However, at
present we do not know how to decide whether this is indeed the case.
5.1. Intersections of theta divisors
Consider a complex ppavX of dimensiong≥ 2 with a symmetric theta
divisorΘ⊂ X as above. In this section we will always assume thatΘ is
smooth or has at most isolated singularities, a situation in which we have
the following Bertini-type result.
LEMMA 5.3. If the theta divisorΘ is smooth or has at most isolated
singularities, then over some Zariski-open dense subset U⊂ X there exists
a smooth proper family
fU : YU−→U
whose ﬁbre over any point x∈U(C) is isomorphic to Yx = Θ∩Θx.
Proof.Recall the general fact [55, cor. III.10.7] that iff : V−→W is a
morphism of complex algebraic varieties and ifV is smooth, then over some
Zariski-open denseU⊆W the restrictionfU = f|f−1(U) : f−1(U)−→U is
a smooth morphism. Since we can replaceW by any Zariski-open dense
subset, this remains true if the smoothness assumption onV is replaced
by the weaker assumption that the singular locusSing(V) is mapped viaf
into a proper closed subset ofW. In the case at hand, we apply this to the
composite morphism
f : V = Θ×Θ   // X×X a // X = W
wherea : X×X−→X denotes the group law. If the theta divisor has at
most isolated singularities, thenSing(V) = (Sing(Θ)×Θ)∪(Θ×Sing(Θ))
has dimensiong−1 or is empty. In both cases the general fact from above
shows that over some Zariski-open dense subsetU⊂ X the restrictionfU
is smooth of relative dimensiong−2. This being said, our claim follows
from the observation that the projection onto the ﬁrst factorΘ×Θ−→Θ
induces an isomorphismf−1(x)∼= Θ∩Θx for x∈ X(C). □
We want to study the ﬁbresYx of the above family. In this context an
important role is played by the involutionσx : X−→X,y↦→ x−y. Notice
that the intersectionYx = Θ∩ Θx is mapped onto itself by this involution
96 Chapter 5 – A family of surfaces
because we assumed the theta divisor to be symmetric. The above Bertini
argument yields the following
COROLLARY 5.4. If the theta divisor is smooth or has only isolated
singularities, then there exists a Zariski-open dense subset U⊂ X such that
for all x∈U(C) the quotient morphism
Yx−→Y+
x = Yx/σx
is an ´etale double covering between smooth varieties of dimension g−2.
Proof.From lemma 5.3 we get a Zariski-open dense subsetU⊂ X such
thatYx is smooth of dimensiong−2 for allx∈U(C). Shrinking this open
dense subset we can furthermore assume that it does not contain points of
the formx = 2y withy∈ Θ(C). Then the involutionσx : Yx−→Yx is ´etale
for all pointsx∈U(C), and our claim follows. □
For the rest of this section we always ﬁx a pointx with the properties in
the above corollary, and we put
Y = Yx, Y+ = Y+
x and σ = σx
for brevity. Like for any´etale double cover of smooth complex varieties,
the rational cohomology of the quotientY+ coincides with the eigenspace
for the eigenvalue+1 in
H•(Y,Q) = H•(Y,Q)+⊕H•(Y,Q)−
where the upper index± indicates that the involutionσ acts by±1 on the
respective two eigenspaces. Now recall the following version of the weak
Lefschetz theorem [71, rem. 3.1.29]: IfW is a smooth complex projective
variety of dimensiond, then for all ample effective divisorsD1, . . . ,Dr the
restriction mapHn(W,Z)−→Hn(D1∩···∩ Dr,Z) is an isomorphism in
degreesn < d−r and a monomorphism in degreen = d−r. Note that
the intersecting divisors are not required to be smooth or transverse to each
other. In our case, sinceY is the intersection of two ample divisors onX it
follows that the restriction morphism
Hn(X,Q)−→Hn(Y,Q)
is an isomorphism forn < g−2 and a monomorphism forn = g−2. So
the interesting part of the cohomology ofY sits in the middle cohomology
degreen = g−2 and can be deﬁned as the orthocomplement
V = Hg−2(X,Q)⊥⊆ Hg−2(Y,Q)
with respect to the intersection form. The involutionσ acts byε = (−1)g
on Hg−2(X,Q), hence
Hg−2(X,Q)⊆ Hg−2(Y,Q)ε =
{
Hg−2(Y,Q)+ for g even,
Hg−2(Y,Q)− for g odd.
