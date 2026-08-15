---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-017-4-proving-the-norm-relations-theorem-313
section_title: "Proving the norm relations (Theorem 3.13)"
section_number: 4
pages: 21-23
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Theorem 3.13 is directly analogous to the norm-compatibility relations for Euler systems constructed
from Siegel units; speciﬁcally, it is the analogue in our context of [Lei et al. 2014, Theorem 3.3.2].
Exactly as in [op. cit.] it is simplest not to prove the theorem directly but rather to deduce it from a
related result concerning cohomology classes on the symmetric spaces Y∗
F(m, mn), analogous to [op. cit.,
Theorem 3.3.1]. Note that these symmetric spaces are not connected for m> 2, but haveφ(m) connected
components; this will allow us to give a tidy conceptual interpretation of the sum over j∈(Z/pr Z)∗
appearing in the deﬁnition of c8r
n,a.
4A. Rephrasing using the spaces Y ∗
F(m, mn).
Proposition 4.1. For any a∈ OF, the element
( 1
0
a
1
)
normalises U∗(m, mn)⊂ GL∗
2(A f
F).
Proof. This is easy to check. □
We can therefore regard right-translation by
( 1
0
a
1
)
as an automorphism of Y∗
F(m, mn), and we can
consider the composite map
ιm,n,a: Y∗
Q(m, m N)↪→ Y∗
F(m, mn)
( 1
0
−a
1
)
−−−→Y∗
F(m, mn),
where the ﬁrst arrow is injective (as soon as mn is divisible by some integer> 4) by the same argument
as in Proposition 2.5. Note also that the components of Y∗
F(m, mn) are indexed by(Z/mZ)∗, with the
ﬁbre over j corresponding to the component containing the image of
( j
1
)
∈ GL∗
2(A f
F); and the action of( 1
0
a
1
)
preserves each component.
Remark 4.2. The change of sign appears because we are comparing left and right actions.
1688 David Loeﬄer and Chris Williams
Deﬁnition 4.3. We deﬁne cZm,n,a to be the image of cCm N∈ H1(YQ(m, m N), Z) under pushforward
viaιm,n,a, and cZm,n,a( j) the projection of cZm,n,a to the direct summand of H1(Y∗
F(m, mn), Z) given by
the j-th component, so that
cZm,n,a=
∑
j
cZm,n,a( j).
Exactly as in the situation of Beilinson–Flach elements, these Z elements turn out to be closely related
to the8’s deﬁned above (compare [Lei et al. 2014, Proposition 2.7.4]). We consider the map
sm: Y∗
F(m, mn)→ Y∗
F,1(n)
given by the action of
( m
0
0
1
)
(corresponding to(z, t)↦→(z/m, t/m) on H3).
Proposition 4.4. We have(sm)∗(cZm,n,a( j))= c4m,n, ja , and hence
c8r
n,a=
∑
j
(spr)∗(cZpr,n,a( j))⊗[ j].
Lemma 4.5. The pushforward of cCm2 N along the map
YQ,1(m2N)→ YQ(1(m), m N),
given by z↦→ mz on H, is cCm N.
Proof. This follows from the well-known norm-compatibility relations of the Siegel units; see [Kato 2004,
Lemma 2.12]. □
Proof of Proposition 4.4. For each j∈(Z/mZ)×, we have a diagram
Y∗
F(m, m N)(1)
( 1
0
− ja
1
)
//
( j
0
0
1
)

Y∗
F(m, mn)(1)
( j
0
0
1
)

Y∗
F(m, m N)( j)
( 1
0
−a
1
)
// Y∗
F(m, mn)( j)
In other words, if we identify Y∗
F(m, m N)( j) with 0∗
F(m, m N)\H3 via
( j
0
0
1
)
, the restriction to this
component of the right action of
( 1
0
−a
1
)
on the adelic symmetric space corresponds to the left action of( 1
0
ja
1
)
on H3.
With these identiﬁcations, we see that the map
κ ja/m: Y∗
F,1(m2n)→ Y∗
F,1(n)
used in the deﬁnition of 4m,n, ja factors as
Y∗
F,1(m2n)
( 1
0
0
m
)
−−−→Y∗
F(1(m), mn) ∼=−→Y∗
F(m, mn)( j)
( 1
0
−a
1
)
−−−→Y∗
F(m, mn)( j) sm−→Y∗
F,1(n).
p-adic Asai L-functions of Bianchi modular forms 1689
Pushforward along the ﬁrst map is compatible with pushforward along the corresponding map on H,
which sends cCm2 N to cCm N by Lemma 4.5. □
Corollary 4.6. The classes c4m,n,a, cZm,n,a depend only on the image ofa in the quotient OF/(mOF+Z).
Proof. If b∈ Z, the action of
( 1
0
b
1
)
on YQ(m, m N) ﬁxes the cohomology class cCm N, as this class is
the pullback of a class on YQ,1(m N). Since the actions of
( 1
0
b
1
)
on YQ(m, m N) and Y∗
F(m, mn) are
compatible, we see that cZm,n,a= cZm,n,a+b for any a∈ OF and b∈ Z, as required. The corresponding
result for c4m,n,a now follows from Proposition 4.4. □
