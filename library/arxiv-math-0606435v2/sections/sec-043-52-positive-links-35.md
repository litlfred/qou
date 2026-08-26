---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-043-52-positive-links-35
section_title: "Positive links 35"
section_number: 5.2
pages: 35-37
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The only common extension of the two MW F = 3 extensions is
[122331221123321], which has MW F = 4.
So it remains to verify that (the closures of)[22 ∗3 ∗122 ∗11 ∗23211∗] and [22 ∗3122 ∗11 ∗23 ∗211∗] have braid index
4.
For this we use the two-cabled MWF inequality. Let for a braidβ ∈ Bn, the “two-cabled” braid(β)2 ∈ B2n be obtained
from β by replacing in (9) each σi by σ2iσ2i−1σ2i+1σ2i. Then (β)2 is a braid representation of the (blackboard framed)
two-cable link L2 of the closure L = ˆβ of β. We consider now for β the above braid β0.
We know, from the computations described in [MS, FW], that MW F((139465)2) = 7. This is in fact true also for
the connected cable (the one with braid representation (β0)2 · σ1). Now we claim that reducing or resolving a clasp
(changing a σ2
i into a σi or deleting it) does not reduce the two-cabled MWF bound. The 2-cable of a clasp can
be resolved by resolving 4 clasps. The 2-cable of a crossing i n a 2-cabled clasp can be resolved by resolving one
clasp and changing twice σ2
i → σi. Finally, the 2-cable of an isolated σi can be reduced into two internal twists of
the doubled original strand. Such twists can be collected fo r every doubled component, resolved for each doubled
component to one, and joined if doubled components are joine d by reducing a doubled crossing in a doubled clasp.
So the two-cabled MWF reduces to the one of the connected cable of 139465 and we are done.
The proof of theorem 5.1 is now completed.
5.2. Positive links
In this section, we will reﬁne the arguments proving theorem1.1 to restrict the possible 3-braid representations of pos-
itive links. Our positivity considerations will make use of the criterion of Yokota [Yo], and the Kauffman polynomial
F. We recall the properties (6) – (8) that determine F and its writhe-unnormalized version Λ.
Note that for P one can similarly deﬁne a regular isotopy invariant
˜P(D)(a,z) = (ia)−w(D)P(D)(ia,iz) ,(37)
with i = √−1. Then ˜P satisﬁes similar relations to (6) – (8). The difference to Λ is that ˜P is deﬁned on oriented link
diagrams, and that the term making orientation incompatible on the right of (6) is missing.
Theorem 5.4 (Yokota [Yo]) IfL is a positive link, then
mindeg a F(L) = mindeg v P(L) = 1 − χ(L) ,
and
[F(L)]a1−χ(L) = [P(L)(ia,iz)]a1−χ(L) .
We also require an extension of braids to the context of F. This was described in [BW] and [Mr], but we use only
the generators of the algebra deﬁned there. Strings will be a ssumed numbered from left to right and words will be
composed from bottom to top. We write σi for a braid generator, where strand i from the lower left corner, passing
over strand i + 1, goes to the upper right corner.
We add elements δi of the following form:
i i + 1
.
By hat we denote the usual closure operation.
A word in the described generators gives rise to an unoriented tangle diagram that turns into an unoriented link diagram
under closure. If the word has no δi then this diagram can be oriented to give a(n oriented) closed braid diagram. We
will assume this orientation is chosen. Otherwise, a cohere nt orientation is not generally possible. In particular, th e
sign of exponents of σi in this context may not coincide with the sign of the correspo nding crossings after some (or
even any) orientation choice of the diagram. For kinks (the diagram fragments occurring in (7) on the left hand-sides),
however, a sign is deﬁnable since any possible component ori entation chosen gives rise to the same (skein) sign. So
we will be able (and we will need) to distinguish between posi tive (in the left equation of (7)) and negative kinks (in
the right one).
36 5 Positivity of 3-braid links
Lemma 5.6 Let
D = ˆ
(
σ
k1,1
1 σ
k1,2
2 . . .σ
k1,n1
1 σ−1
2 σ
k2,1
1 . . .σ
k2,n2
1 σ−1
2 . . . σ
kl,1
l . . .σ
kl,nl
1 δ2
)
(38)
where ni ≥ 1 odd and ki,j ≥ 2 when 1 < j < ni and ki,j ≥ 1 when j = 1 or ni. Then mindeg a Λ(D) = −l.
Proof. For l = 1 see lemma 5.9 below. Then use induction on l. Change a crossing of a σ−1
2 in D = D−. Then:
D+ can be reduced by the same argument as in the proof of lemma 5.2of [St4] until we have a form (38) with smaller
l, and a non-zero number of negative kinks added. Then since ne gative kinks shift the a-degree of Λ up, we have
mindeg a Λ(D+) > −l.
D0 has mindega Λ(D0) = 1 − l > −l by induction.
D∞ = Dl1#Dl2 with l1 + l2 = l, so mindeg a Λ(D∞ ) = −l1 − l2 = −l, and mindeg a Λ(D) is inherited from Λ(D∞ ). ✷
Lemma 5.7 Let
D = ˆ
(
σ
k1,1
1 σ
k1,2
2 . . .σ
k1,n1
1 σ−1
2 σ
k2,1
1 . . .σ
k2,n2
1 σ−1
2 . . . σ
kl,1
l . . .σ
kl,nl
1 σ−1
2
)
(39)
where ni ≥ 1 odd and ki,j ≥ 2 when 1 < j < ni and ki,j ≥ 1 when j = 1 or ni. Then mindeg a Λ(D) ≥ −2 when l ≤ 2
and mindeg a Λ(D) = −l when l ≥ 3.
Proof. Assume ﬁrst we proved the result for l ≤ 2, and that l > 2. We argue by induction on l.
Apply the Λ-relation at a σ−1
2 crossing in D = D−. Then D0 has mindeg a Λ = 1 − l by induction. D+ simpliﬁes
as in the proof of lemma 5.2 of [St4]. This simpliﬁcation only removes negative letters. It can be iterated until
one of two situations occurs. It can (a) happen that all negat ive letters disappear. Then we have a positive braid
and mindeg a Λ = −2 > −l by Yokota’s result. Or it can (b) occur that no σ1σ2σ1 or σ2σ1σ2 occur as subwords.
Then ki,j ≥ 2 for 1 < j < ni, and the number l of negative crossings has decreased strictly. So we have by i nduction
mindeg a Λ(D+) > −l. Finally we must deal with the D∞ term. This follows from lemma 5.6.
It remains to justify the claim mindeg a Λ(D) ≥ −2 when l ≤ 2. This is done exactly with the same argument, only
that now we observe that all of Λ(D0,+,∞ ) have a-degree ≥ −2. ✷
Lemma 5.8 The closed braids in (39) are not positive for l ≥ 2.
Proof. The representation (39) clearly gives rise to a positive ban d representation by replacing σ2σ
ki,ni
1 σ−1
2 by σ
ki,ni
3 .
So [β] = 3 − χ(ˆβ). If l > 2, then we have
mindeg a F(D) = w(D) + mindeg a Λ(D) = 3 − χ(ˆβ) +mindega Λ(D) < 1 − χ(ˆβ)
but mindegv P(D) = 1 − χ(ˆβ) as before, so mindeg a F ⁄= mindeg v P and we are done by theorem 5.4.
If l = 1, then if n1 = 1, we have a (2,k1,1)-torus link, and for n1 = 3 we have the (1,k1,1,k1,2,k1,3)-pretzel link.
Otherwise we apply the relations for ˜P and Λ at the negative crossing. Then mindeg a Λ(D+,0) = mindeg a ˜P(D+,0) =
−2, and [Λ(D+,0)]a−2 = [ ˜P(D+,0)]a−2 by theorem 5.4 since D+,0 are positive braids. That the extra term Λ(D∞ ) has
no contribution to a−2 follows from lemma 5.9 below. So D satisﬁes Yokota’s conditions in theorem 5.4. (We do not
always know if D depicts a positive link; see remark 5.2.)
If l = 2 then resolve a negative crossing in D = D− via the relation ˜P− = z ˜P0 − ˜P+ and via the Λ-relation Λ − =
zΛ 0 + zΛ ∞ − Λ +. Now [ ˜P+,0]a−2 = [Λ +,0]a−2. This follows from the above argument for l = 1. The additional term Λ ∞
has a-degree −2 by lemma 5.6, so [Λ −]a−2 ⁄= [ ˜P−]a−2. Again by theorem 5.4, D = D− can therefore not belong to a
positive link. ✷
Remark 5.1 Ishikawa asks in [I] whether strongly quasi-positive knots satisfy the equality TB = 2gs − 1, where T B
is the maximal Thurston-Bennequin invariant. The proof of t he lemma shows that there are inﬁnitely many strongly
quasi-positive 3-braid knots with T B < 2gs − 1: take any of the knots with l > 2. (There are also many other such
knots, like the counterexamples to Morton’s conjecture in [St3].)
