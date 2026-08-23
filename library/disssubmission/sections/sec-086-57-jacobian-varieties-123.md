---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-086-57-jacobian-varieties-123
section_title: "Jacobian varieties 123"
section_number: 5.7
pages: 131-133
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
Proof.For a general ppav we know from theorem 4.2 that the Tannaka
groupG(δΘ) is either a symplectic or a special orthogonal group and that
the perverse intersection cohomology sheafδΘ corresponds to the standard
representation of this group. Now the symmetric and alternating square of
the standard representation are irreducible up to a trivial one-dimensional
representation, and this trivial representation corresponds to the skyscraper
sheafδ0 of rank one supported in the origin. Furthermore, by corollary 2.9
each representation of the Tannaka group corresponds to a unique clean
perverse sheaf. Hence from lemma 5.22 we obtain that there exist clean
and simple perverse sheavesγ±∈ Perv(X,C) such that
δ+ =
{
γ+⊕δ0
γ+
and δ− =
{
γ−
γ−⊕δ0
if g is
{
odd,
even,
and by lemma 5.21 the simplicity ofγ± in particular implies that the local
systemsV± are irreducible. □
5.7. Jacobian varieties
Let us now see what happens ifX = JC is the Jacobian variety of a
smooth complex projective curveC of genusg≥2. To formulate our results
in this case we ﬁrst need to introduce some more notations. Forn∈ N we
will denote by
Cn = (C×···× C)/Sn
the n-fold symmetric product of the curve and byWn⊂ X the image ofCn
under a suitable translate of the Abel-Jacobi map, normalized such that the
theta divisorΘ = Wg−1 becomes symmetric. We writefn : Cn−→Wn for
the Abel-Jacobi map andgn : Wn×Wn−→X for the difference morphism
withgn(x,y) =y−x. Then the composite morphism
Cn×Cn
(fn,fn) //
dn
77Wn×Wn
gn // X∼= Pic0(C)
does not depend on the chosen normalization of the Abel-Jacobi map, and it
sends a pair(D,E)∈Cn×Cn of effective divisors of degreen on the curve
to the isomorphism class of the line bundleOC(D−E).
In what follows we will be especially interested in non-hyperelliptic
curves of genusg = 4. For these we know from lemma 4.5 that the theta
divisor has only isolated singularities, so we can consider the variations of
Hodge structuresV± from lemma 5.10 and the perverse sheavesδ± from
lemma 5.21. Here we have the following situation.
124 Chapter 5 – A family of surfaces
PROPOSITION 5.24. Let X = JC be the Jacobian variety of a smooth
non-hyperelliptic complex projective curve C of genus g= 4.
(a) The above semisimple perverse sheavesδ+ and δ− each contain
the negligible constituentδX precisely once.
(b) After shrinking the open dense subset U⊂ X in lemma 5.10 there
exists an isomorphism
V+∼= d2∗(CC2×C2)|U.
Proof. (a)We must check for the lowest hypercohomology degree that
dim(H−g(X,δ+)) = dim(H−g(X,δ−)) = 1. For this we can use the same
computation as in lemma 5.22, the only difference is that for a Jacobian
variety the hypercohomologyH•(X,δΘ) is larger than the one for a general
ppav. Indeed it has been shown in [106, cor. 13(iii)] that if the curveC is
not hyperelliptic, then
Hi(X,δΘ) =
{
Hi+3(X,C) for i∈{−3,−2},
Hi+3(X,C)⊕Hi+1(X,C) for i∈{−1,0}.
Compared with the computation in lemma 5.22, fori =−1 the extra direct
summandH0(X,C)⊂ H−1(X,δΘ) gives a two-dimensional extra term
H0(X,C)⊗H−3(X,δΘ)⊕ H−3(X,δΘ)⊗H0(X,C)⊂ H−4(X,δΘ∗δΘ).
This extra term splits into two one-dimensional contributions, one in the
symmetric and one in the alternating tensor square. Hence
H−4(X,S2(δΘ)) = H−4(X,L+)⊕C,
H−4(X,Λ2(δΘ)) = H−4(X,L−)⊕C,
and our claim follows becauseS2(δΘ) = L+⊕δ+ and Λ2(δΘ) = L−⊕δ−.
(b) This is most conveniently checked in the setting of Brill-Noether
sheaves and will be done after the proof of lemma 5.25 below. □
Before we proceed further, let us recall from [106] some facts about
Brill-Noether sheaves. Here we are mainly interested in their Tannakian
description — more about their geometric construction can be found in the
brief survey in section 6.1 below. LetX = JC be the Jacobian variety of a
smooth non-hyperelliptic complex projective curveC of genusg≥ 2, and
letC ↪→X be a translate of the Abel-Jacobi map such that the corresponding
theta divisorΘ =Wg−1 is symmetric. Then by loc. cit. the convolutions of
the perverse intersection cohomology sheafδC∈ Perv(X,C) are described
via corollary 2.14 by the Tannaka group
G(δC) = Sl2g−2(C).
