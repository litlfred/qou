---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-040-101-lens-spaces
section_title: "Lens spaces"
section_number: 10.1
pages: 311-318
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We introduce some of the simplest 3-manifolds, the lens spaces. These
manifolds (and many more) are easily described using an important three-
dimensional construction, calledDehn ﬁlling.
10.1.1. Dehn ﬁlling.If a 3-manifoldM has a spherical boundary com-
ponent, we can cap it oﬀ with a ball. IfM has a toric boundary component,
there is no canonical way to cap it oﬀ: the simplest object that we can attach
to it is a solid torusD×S1, but the resulting manifold depends on the gluing
map. This operation is called aDehn ﬁllingand we now study it in detail.
LetM be a 3-manifold andT⊂∂M be a boundary torus component.
Deﬁnition 10.1.1. ADehn ﬁllingof M along T is the operation of gluing
a solid torusD×S1 toM via a diﬀeomorphismϕ:∂D×S1→T.
The closed curve∂D×{x} is glued to some simple closed curveγ⊂T,
see Figure 10.1. The result of this operation is a new manifoldMﬁll, which
has one boundary component less thanM.
Lemma 10.1.2. The manifoldMﬁll depends only on the isotopy class of
the unoriented curveγ.
Proof. DecomposeS1 into two closed segmentsS1 =I∪J with coinciding
endpoints. Theattachingof D×S1 maybeseenastheattachingofa2-handle
D×I along ∂D×I, followed by the attaching of a 3-handleD×J along its
full boundary.
303
304 10. SEIFERT MANIFOLDS
Figure 10.1. The Dehn ﬁllingMﬁll of a 3-manifoldM is determined by
the unoriented simple closed curveγ⊂T to which a meridian∂D of the
solid torus is attached.
If we changeγ by an isotopy, the attaching map of the 2-handle changes
by an isotopy and hence gives the same manifold. The attaching map of the
3-handle is irrelevant by Proposition 9.2.1. □
We say that the Dehn ﬁllingkills the curve γ, since this is what really
happens on fundamental groups, as we now see.
The normaliser of an elementg∈G in a groupG is the smallest normal
subgroupN(g)◁G containingg. Thenormaliserdependsonlyontheconjugacy
class ofg±1, hence the subgroupN(γ)◁π 1(M) makes sense without ﬁxing a
basepoint or an orientation forγ.
Proposition 10.1.3. We have
π1(Mﬁll) =π1(M)/N(γ).
Proof. The Dehn ﬁlling decomposes into the attachment of a 2-handle
overγ and of a 3-handle. By Van Kampen, the ﬁrst operation killsN(γ), and
the second leaves the fundamental group unaﬀected. □
Let aslope on a torusT be the isotopy classγ of an unoriented homo-
topically non-trivial simple closed curve. The set of slopes onT was indicated
by S in Chapter 7. If we ﬁx a basis(m,l ) forH1(T, Z) =π1(T ), every slope
may be written asγ =±(pm +ql ) for some coprime pair(p,q ). Therefore
we get a 1-1 correspondence
S←→ Q∪{∞}
by sending γ to p
q. If T is a boundary component ofM, every number p
q
determines a Dehn ﬁlling ofM that kills the corresponding slopeγ.
10.1. LENS SPACES 305
Diﬀerent values ofp
q typically produce non-diﬀeomorphic manifoldsMﬁll:
this is not always true - a notable exception is described in the next section -
but it holds in “generic” cases.
10.1.2. Lens spaces. The simplest manifold that can be Dehn-ﬁlled is
the solid torusM =D×S1 itself. The orientedmeridian m =S1×{y} and
longitude l ={x}× S1 form a basis forH1(∂M, Z).
Deﬁnition 10.1.4. Thelens spaceL(p,q ) is the result of a Dehn ﬁlling of
M =D×S1 that kills the slopeqm +pl.
A lens space is a three-manifold that decomposes into two solid tori. We
have already encountered lens spaces in the more geometric setting of Section
3.4.10, and we will soon prove that the two deﬁnitions are coherent. Since
L(p,q ) =L(−p,−q) we usually supposep> 0.
Exercise 10.1.5. We haveπ1
(
L(p,q )
)
= Z/pZ.
Proposition 10.1.6. We haveL(0, 1) =S2×S1 andL(1, 0) =S3.
Proof. The lens spaceL(0, 1) is obtained by killingm, that is by mirroring
D×S1 along its boundary. The lens spaceL(1, 0) isS3 because the comple-
ment of a standard solid torus inS3 is another solid torus, with the roles ofm
andl exchanged (exercise). □
Exercise 10.1.7. Every Dehn ﬁlling of one component of the productT×
[0, 1] is diﬀeomorphic toD×S1. Therefore by Dehn-ﬁlling both components
ofT× [0, 1] we get a lens space.
The solid torusD×S1 has a non-trivial self-diﬀeomorphism
(x,e iθ )↦−→(xeiθ,eiθ )
called atwist along the discD×{y}. The solid torus can also bemirrored
via the map
(x,e iθ )↦−→(x,e−iθ ).
Exercise 10.1.8. We haveL(p,q )∼=L(p,q′) ifq′≡±q±1 (modp).
Hint. Twist, mirror, and exchange the two solid tori givingL(p,q ). □
Remark 10.1.9. The meridianm of the solid torusM = D×S1 may be
deﬁned intrinsically as the unique slope in∂M that is homotopically trivial in
M. The longitudel is not intrinsically determined: a twist sendsl to m +l.
The solid torus contains inﬁnitely many non-isotopic longitudes, and there is
no intrinsic way to choose one of them.
306 10. SEIFERT MANIFOLDS
10.1.3. Equivalence of the two deﬁnitions.When p >0, we have de-
ﬁned the lens spaceL(p,q ) in two diﬀerent ways: as the(q,p )-Dehn ﬁlling
of the solid torus, and as an elliptic manifold in Section 3.4.10. In the latter
description we set
ω =e
2πi
p , f (z,w ) = (ωz,ω qw )
and deﬁneL(p,q ) as S3/Γ where Γ =⟨f⟩ is generated byf. We now show
that the two deﬁnitions produce the same manifolds.
Proposition 10.1.10. The manifoldS3/⟨f⟩ is the (q,p )-Dehn ﬁlling of the
solid torus.
Proof. The isometryf preserves the central torus
T =
{
(z,w )
⏐⏐|z| =|w| =
√
2
2
}
that dividesS3 into two solid tori
N1 =
{
(z,w )
⏐⏐|z|⩽
√
2
2 ,|w| =
√
1−|z|2}
,
N2 =
{
(z,w )
⏐⏐|w|⩽
√
2
2 ,|z| =
√
1−|w|2}
.
IdentifyT withS1×S1 = R2/Z2 in the obvious way, so thatH1(T ) = Z× Z.
The meridians ofN1 andN2 are (1, 0) and (0, 1). The isometryf act onT as
a translation of vectorv =
( 1
p, q
p
)
. The quotientT/⟨f⟩ is again a torus, with
fundamental domain the parallelogram generated byv andw = (0, 1).
The quotientsN1/⟨f⟩, andN2/⟨f⟩ are again solid tori. ThereforeS3/⟨f⟩
is also a union of two solid tori. Their meridians are the projections of the
horizontal and vertical lines inR2 to T/⟨f⟩ = R2/⟨v,w⟩. In the basis (v,w )
these meridians arepv−qw andw respectively. ThereforeS3/⟨f⟩ is a(−q,p )-
Dehn ﬁlling on the solid torus, which is diﬀeomorphic to the(q,p )-Dehn ﬁlling
by mirroring the solid torus. □
Corollary 10.1.11.We haveL(1, 0) =S3 andL(2, 1) = RP3.
Proof. We havef = id andf =−id, correspondingly. □
10.1.4. Classiﬁcation of lens spaces.Which lens spaces are diﬀeomor-
phic? It is not so easy to answer this question, because many lens spaces like
L(5, 1)andL(5, 2)havethesamehomotopyandhomologygroups, whilethere
is no evident diﬀeomorphism between them. A complete answer was given by
Reidemeister in 1935, who could distinguish lens spaces using a new invari-
ant, now known as theReidemeister torsion. More topological proofs were
discovered in th 1980s by Bonahon and Hodgson. We follow here Hatcher
[26].
Theorem 10.1.12.The lens spacesL(p,q ) andL(p′,q′) are diﬀeomorphic
⇐⇒p =p′ andq′≡±q±1 (modp).
10.1. LENS SPACES 307
Figure 10.2. We require thep sheets of the spine∆ to lie above every
local maximum forf|Σ.
Proof. We may supposep> 1. Exercise 10.1.8 furnishes one implication,
so we start with a lens spaceL(p,q ) and we prove that there is (up to isotopy)
only one torusT dividingL(p,q ) into two solid tori: this fact then implies that
one can recoverp andq intrinsically fromL(p,q ), up to the stated ambiguity
forq (which depends on the chosen longitudes and orientations, and changes
by switching the solid tori). So we suppose that there is another torusT′.
Let Σ be the core circle of one solid torus adjacent toT′. If we can
isotope Σ inside the torusT, we are done: in that caseT′ is isotopic to the
boundary of a small tubular neighbourhood ofΣ, hence bothT andT′ are cut
into two annuliT = A1∪A2 and T′ = A′
1∪A′
2 such that Σ⊂ A1, all four
annuli share the same boundaries, andA2 is contained in the large outside solid
torus bounded byT′; the annulusA2 is incompressible in this solid torus by
Proposition 9.3.4 (otherwise Σ would be homotopically trivial, contradicting
p >1) and hence∂-parallel by Proposition 9.3.16, so it is isotopic to either
A′
1 orA′
2, suppose toA′
2; sinceA1 is clearly isotopic toA′
1 we conclude that
T andT′ are isotopic.
Our aim is now to prove thatΣ can be isotoped insideT. To this purpose
we construct two diﬀerent objects fromT′ and T, aspine ∆ and afoliation
F. The spine ∆⊂ M is built by adding toΣ the meridianD of the other
solid torus incident toT′, enlarged so that∂D is glued alongΣ like a degree-p
covering. Note thatM\ ∆ is an open ball.
We construct the foliationF ofM by subdividing each solid torus bounded
byT into concentric tori, with a central singular circle in each. We represent
F as the level sets of a mapf :L(p,q )→ [0, 1] where the singular circles are
the extreme levelsf−1(0) andf−1(1).
We now put∆ in some good position with respect toF. We ﬁrst perturb
Σsothatitisdisjointfromthesingularcirclesof F andf|Σ isaMorsefunction
with singular points in distinct levels. At every local maximum (minimum) of
f|Σ we isotope ∆ so that thep sheets of ∆ lie above (below)Σ as in Figure
10.2. Finally, we require∆ to be transverse to the two singular circles ofF
and f|∆\Σ to be a Morse function, with critical points at distinct levels (also
distinct from those of the critical points off|Σ).
The foliation F induces a singular foliation on∆ that pulls back toD via
the mapD→ ∆. There are three types of singular points in the foliation,
shown in Figure 10.3: centres, saddles, and half-saddles.
308 10. SEIFERT MANIFOLDS
Figure 10.3. The singular points inD can be centres (top left), saddles
(top right) and half-saddles (bottom).
Figure 10.4. A singular leaf exiting from a singular point may be of one
of these kinds. The dots in (e) indicate that there might be another half-
saddle at the other endpoint: this is because there are half-saddles at the
same level (preciselyp for every local maximum or minimum forf|Σ).
A leaf inD incident to a singular point issingular. Since we minimised the
critical points that may stay at the same level, the singular leaves exiting from
a singular point may be only of the six possible kinds shown in Figure 10.4.
The saddles and half-saddles of type (a) and (e) are calledessential, and the
others inessential. In (a) the singular leaves divideD into fourquarter discs,
and in (e) they cut oﬀ two or morehalf discs.
Among all possible good conﬁgurations of∆, we pick one that minimises
ﬁrst the number of critical points inf|Σ, and second the number of essential
saddles.
LetD′⊂D be a quarter or half-disc not containing any smaller quarter or
half-disc. Deﬁneα =D′∩∂D. Suppose ﬁrst thatD′ is a half-disc and both
endpoints ofα are singular. The singular discD′ can contain some singular
point of type (b), and it certainly contains one singular point of type (f), see
Figure 10.5-(left). (It contains no other singular point except these.) The
image ofD′ in ∆ is shown in Figure 10.5-(right). In this case we can slide
α along D′ to the green arc shown in the ﬁgure which lies entirely in a level
torus off. If we could do this for all the arcs of∂D cut by singular points, we
10.1. LENS SPACES 309
Figure 10.5. The discD′ is a half-disc andα is incident to two singular points.
Figure 10.6. The discD′ is a half-disc andα is incident to one singular point.
Figure 10.7. The discD′ is a quarter disc.
would happily isotopeΣ inside a torus level and hence intoT, and we would
be done.
There are however two other cases to consider, and both will be excluded
by our minimality assumption on∆. One is thatD′ may be a half-disc with
only one singular endpoint forα, as in Figure 10.6. In that case we can isotope
α to the green curve throughD′, dragging the spine∆ behind. In the new
conﬁgurationf|Σ has strictly less critical points, a contradiction.
In the last caseD′ is a quarter disc as in Figure 10.7 and we can isotope
α to the green curve draggingΣ as above, but more carefully: we enlarge the
other p− 1 sheets of ∆ by parallel copies ofD′. In the new conﬁguration
the number of critical points inf|Σ is unchanged, but there are strictly fewer
essential saddles: at least one is destroyed and no new one is created. (Note
that many inessential saddles may be created.) This is also excluded. □
310 10. SEIFERT MANIFOLDS
We have discovered, in particular, that there are closed three-manifolds
likeL(5, 1) andL(5, 2) that are not diﬀeomorphic, although their fundamental
groups are both isomorphic toZ/5Z; the two manifolds are both covered by
S3, so they also have isomorphic higher homotopy groups.
