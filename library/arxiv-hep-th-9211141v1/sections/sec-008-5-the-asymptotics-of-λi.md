---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-008-5-the-asymptotics-of-λi
section_title: "The asymptotics of λi"
section_number: 5
pages: 25-26
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
If we look at the asymptotics of fi(x) (the eigenfunction associated with the eigenvalue
µi of L, normalized so that fi(0) = 1) given by (4.9), (4.11), (4.13), and (4.16) we see that
the main contribution to
R ∞
0 fi(x)2 dx comes from any region
t−1/4|t −x| < η(t)
as long as η(t) →∞. For some such region we have, by (4.15) and (4.17),
fi(x) ∼2−5
2 i−2
√π t−3
4i−3
4Di
√
2t−1/4(t −x)

.
25
Using this, and the fact
R ∞
−∞Di(x) dx =
√
2πi!, we deduce
Z ∞
0
fi(x)2 dx ∼i!
√π2−5i−4t−3
2 i−5
4 exp
8
3t3/2

.
(4.18)
This was the goal of all that went before.
Since L has simple eigenvalues and commutes with our integral operator K (translated
to (0, ∞)) the set {fi} is the set of eigenfunctions of K corresponding to its eigenvalues {λi}.
However fi corresponds to µi and there is no assurance that the corresponding eigenvalue
of K is its ith largest, which we have denoted by λi. We shall eventually show that this is
actually the case. The ﬁrst lemma of this section shows that the eigenvalues of K are simple,
and this is crucial for the argument we shall later use. (The proof of the corresponding result
for the sine kernel is in [27].)
Lemma 1 If f1 and f2 are eigenfunctions of L corresponding to distinct eigenvalues, then
they are eigenfunctions of K corresponding to distinct eigenvalues.
Proof. The eigenvalues of K are the squares of the eigenvalues of the operator on (0, ∞)
with kernel A(x + y −2t). So we have to show that if for some ν we have either
Z ∞
0
A(x + y −2t)fi(y) dy = νfi(x)
(i = 1, 2)
(4.19)
or
Z ∞
0
A(x + y −2t)f1(y) = νf1(x) ,
Z ∞
0
A(x + y −2t)f2(y) dy = −νf2(x)
(4.20)
then f1 = f2. (Recall that all eigenfunctions are normalized to satisfy f(0) = 1.)
Assuming ﬁrst that (4.19) holds, apply d2/dx2 to both sides of the identity with i = 1
and integrate the resulting integral by parts twice. What results is
νf ′′
