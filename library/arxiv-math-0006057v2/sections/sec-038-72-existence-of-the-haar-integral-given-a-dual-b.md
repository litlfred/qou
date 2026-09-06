---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-038-72-existence-of-the-haar-integral-given-a-dual-b
section_title: "Existence of the Haar integral. Given a dual bases {fi} and {ξi} of H"
section_number: 7.2
pages: 28-29
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
and ˆH, respectively, let us consider the following canonical element
χ =
∑
i
(ξi ↼S −2(fi)).
One can show that χ is a left integral in ˆH such that χ(xy) = χ(yS 2(x)) for all
x,y ∈H and l⇀χ = ˆS2(ˆ1↼l ) for any left integral l in H (see [BNSz], 3.25).
Lemma 7.2.1 ([BNSz], 3.26) . (i) The Haar integral h ∈ H exists iﬀ the above
mentioned χ is non-degenerate, in which case (h,χ ) is a dual pair of left
integrals.
(ii) A left integral l is a Haar integral iﬀ εs(l) = 1 .
Proof. (ii) If εs(l) = 1, then by l ⇀ χ = ˆS2(ˆ1 ↼ l) one has l ⇀ χ = ˆ1.
Therefore, ( h,χ ) is a dual pair of non-degenerate left integrals. The property
χ(xy) = χ(yS 2(x)) is equivalent to that the quasi-basis of χ satisﬁes
l(2) ⊗S−1(l(1)) = S(l(1)) ⊗l(2),
from where ∆( l) = ∆( S(l)) andl =S(l). Furthermore, εt(l) = εt(S(l)) = S ·εs(l) =
1. Thus, l is a Haar integral. The inverse statement is obvious.
(i) The ”only if” part follows from the proof of (ii). If χ is non-degenerate and h
is its dual left integral, then, as above, S(h) = h; so h is a two-sided integral and
since l⇀χ = ˆS2(ˆ1↼l ), it is normalized.
Theorem 7.2.2 ([BNSz], 3.27) . LetH be a ﬁnite quantum groupoid over an alge-
braically closed ﬁeld k. Then the following conditions are equivalent:
(i) There exists a Haar integral,
(ii) H is semisimple and there exists an invertible element g ∈ H such that
gxg −1 = S2(x) for all x ∈ H and Tr (πα(g−1)) ⁄= 0 for all irreducible repre-
sentations πα of H (hereTr is the usual trace on a matrix algebra).
Proof. The assumption on k is used only to ensure that H = ⊕αMnα (k), once
knowing that it is semisimple, so that there is a k-basis of matrix units {eα
ij} inH.
(ii) = ⇒ (i): Recall that any trace τ on H is completely determined by its
trace vector τα = τ (1α). Now let τ : H → k be the trace with trace vector
τα = trπα(g−1). Then τ is non-degenerate and has a quasi-basis
∑
i
xi ⊗yi =
∑
α
1
τα
nα∑
i,j=1
eα
ij ⊗eα
ji.
Notice that ∑
ixig−1yi = 1. It is straightforward to verify that χ′ = g ⇀ τ
coincides with χ, so χ is non-degenerate and therefore its dual left integral l has
εs(l) = 1 by l⇀χ = ˆS2(ˆ1↼l ). Thus, l is a Haar integral.
(i) =⇒ (ii): If h is a Haar integral, then H is semisimple by Theorem 3.3.1.
Let τ be a non-degenerate trace on H, then there exists a unique i ∈H such that
i⇀τ = ˆ1 = τ ↼i. One can verify that i is a two-sided non-degenerate integral in
H and that S(i) = i (see [BNSz], I.3.21). To prove that S2 is inner, it is enough
to construct a non-degenerate functional χ on H such that χ(xy) = χ(yS 2(x)) for
allx,y ∈H. But the proof of Lemma 7.2.1 shows that this is the case for the dua l
left integral to i.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 29
Remark 7.2.3. (a) There is a unique normalization of g from Theorem 7.2.2(ii)
such that the following conditions hold ([BNSz], 4.4) :
(i) tr(πα(g−1)) = tr(πα(g)) for all irreducible representations πα of H (here
tr is a usual trace on a matrix algebra);
(ii) S(g) = g−1.
One can show that such a g is group-like, i.e.,
∆( g) = (g ⊗g)∆(1) = ∆(1)( g ⊗g).
The element g implementing S2 and satisfying normalization conditions (i)
and (ii) is called the canonical group-like element of H.
(b) Since χ = g ⇀ τis the dual left integral to h, its quasi-basis ∑
ixig−1 ⊗yi
equals to h(2) ⊗S−1(h(1)), which implies the formula
(S ⊗id)∆( h) =
∑
i
xi ⊗g−1yi =
∑
α
1/τα
∑
ij
eα
ijg−1/2 ⊗g−1/2eα
ji.
A dual notion to that of the Haar integral is the Haar measure. Nam ely, a
functional φ ∈ ˆH is said to be a Haar measure on H if it is a normalized left and
right invariant measure and φ◦S =φ. Any of the equivalent conditions of Theorem
7.2.1 is also equivalent to existence (and uniqueness) of the Haar mea sure.
