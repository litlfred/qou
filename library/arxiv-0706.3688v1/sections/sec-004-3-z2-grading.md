---
doc_id: arxiv-0706.3688v1
doc_title: "WHY THE STANDARD MODEL"
section_id: sec-004-3-z2-grading
section_title: "Z/2-grading"
section_number: 3
pages: 7-8
source_pdf: 0706.3688.pdf
source_sha256: f2a18b0defebff66
toc_source: outline
doc_brief: "WHY THE STANDARD MODEL — The Standard Model is based on the gauge invariance principle with gauge group U(1) × SU(2) × SU(3) and suitable representations for fermions and bosons, which are begging"
---
In the set-up of spectral triples one assumes that in the even case the Hilbert space
is Z/2-graded i.e. endowed with a grading operator γ, γ2 = 1, γ = γ∗. This grading
should be compatible with a Z/2-grading of the algebra A which amounts to asking
that γAγ−1 = A. One then has [γ, a] = 0 for any a ∈Aev the even part of A.
Lemma 3.1. In the case Z(AC) = C of Proposition 2.5, let γ be a Z/2-grading of H
such that γAγ−1 = A and Jγ = ǫ′′γJ for ǫ′′ = ±1. Then ǫ′′ = 1.
Proof. We can assume that (AC, H, J) are as in Proposition 2.5. Let δ ∈Aut(AC) be
the automorphism given by δ(a) = γaγ−1, ∀a ∈AC . One has δ2 = 1. Similarly one
gets an automorphism δ0 of A0
C such that δ0(b0) = γb0γ−1 since γA0
Cγ−1 = A0
C using
the relation Jγ = ǫ′′γJ. Then δ ⊗δ0 deﬁnes an automorphism of AC ⊗A0
C such that
γβ(x)γ−1 = β(δ ⊗δ0(x)) ,
∀x ∈B = AC ⊗A0
C .
Thus γ implements the tensor product of two automorphisms of Mk(C). These auto-
morphisms are inner and it follows that there are unitary matrices u, v ∈Mk(C) such
that γ(a) = uav∗, ∀a ∈AC . One then has
JγJ−1(a) = (ua∗v∗)∗= vau∗,
∀a ∈Mk(C) .
Thus the equality JγJ−1 = −γ means that
vau∗= −uav∗,
∀a ∈Mk(C) ,
i.e. that u∗v = z fulﬁlls zaz = −a for all a. Thus z2 = −1 and za = az for all a so
that z = ηi for some η ∈{±1}. We thus get v = ηiu. Then γ(a) = −ηiuau∗and
γ2(a) = −u2au−2. But since γ2 = 1 one gets that a = −u2au−2 for all a ∈Mk(C)
which is a contradiction for a = 1.
□
8
CHAMSEDDINE AND CONNES
Thus Lemma 3.1 shows that we cannot obtain the required commutation relation Jγ =
−γJ in the case Z(AC) = C.
At this point we are at a cross-road. We know that we are in the case Z(AC) = C ⊕C
but we must choose the integer k and the real form A of AC = Mk(C) ⊕Mk(C).
We make the hypothesis that both the grading and the real form come by assuming that
the vector space W of Remark 2.9 is a right vector space over H and is non-trivially
Z/2-graded. The right action of quaternions amounts to giving an antilinear isometry
I of W with I2 = −1 (cf. [15] Chapter 3). Since W is a non-trivially Z/2-graded
vector space over H its dimension must be at least 2 (and hence 4 when viewed as a
complex vector space). We choose the simplest case i.e. W is a two-dimensional space
over H, and there is no ambiguity since all non-trivial Z/2-gradings are equivalent. A
conceptual description of the algebra A and its representation in H is then obtained
from Remark 2.9. We let V be a 4-dimensional complex vector space. Our algebra is
(3.1)
A = EndH(W) ⊕EndC(V ) ∼M2(H) ⊕M4(C) .
It follows from the grading of W that the algebra (3.1) is also Z/2-graded, with non-
trivial grading only on the M2(H)-component. We still denote by γ the gradings of
E = HomC(V, W) and E∗= HomC(W, V ) given by composition with the grading of W.
We then have, with the notations of (2.13),
Proposition 3.2. There exists up to equivalence a unique Z/2-grading of H compatible
with the graded representation of A and such that:
(3.2)
J γ = −γ J
It is given by
(3.3)
H = E ⊖E∗,
γ(ξ, η) = (γξ, −γη)
Proof. By construction the grading (3.3) is a solution. Given two gradings γj fulﬁlling
the required conditions one gets that their ratio γ1γ2 commutes with A (since both
deﬁne the grading of A by conjugation) and with J. Thus by irreducibility one gets
that γ1γ2 ∈±1. Changing γ to −γ amounts to changing the grading of W to its
opposite, but up to isomorphism this gives the same result.
□
Remark 3.3. The space E = HomC(V, W) is related to the classiﬁcation of instantons
(cf. Equation (1.1) Chapter III of [1]).
