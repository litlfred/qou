---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-014-18-chapter-1-vanishing-theorems-on-abelian-varie
section_title: "Chapter 1 – Vanishing theorems on abelian varieties"
section_number: 18
pages: 26-27
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
geometric origin each of the occuring translations can be taken to be torsion
points of Π(X), see lemma 1.11 below. More generally, for semisimple
sheaf complexesK =⨁
n∈Z pH−n(K)[n] we deﬁne
S (K) =
⋃
n∈Z
S (pH−n(K)).
The deﬁnitions imply thatS (Kχ) = χ−1· S (K) for allχ∈ Π(X), and for
all semisimpleK1,K2 we have
S (K1∗K2)⊆ S (K1)∪S (K2) = S (K1⊕K2),
whereK1∗K2 denotes the convolution ofK1 andK2 as deﬁned in section 2.1
below. Note that the equality displayed on the right hand side reduces the
computation of the spectrum of semisimple sheaf complexes to the case
of simple perverse sheaves. Of course the spectrumS (P) may be empty,
for example ifP is a skyscraper sheaf or, more interestingly, ifP = i∗E[1]
wherei : C ↪→ X is the embedding of a smooth curve inX and whereE is
an irreducible local system onC of rank at least two.
Since π1(X,0)∼= Z2g, the character groupΠ(X)∼= C2g is a complex
algebraic torus of rank 2g. FurthermoreΠ is a contravariant functor: For
any homomorphismh : X−→B of complex abelian varieties, the pull-back
of characters gives rise to a homomorphismΠ(h): Π(B)−→Π(X) between
the corresponding algebraic tori.
REMARK 1.10. The functorΠ has the following properties.
(a) Let h: X→B be an isogeny with kernel F. Then we have an exact
sequence
0 // Hom(F,C∗) // Π(B)
Π(h) // Π(X) // 0.
For P∈Perv(X,C) we have h∗(P)∈Perv(B,C), andΠ(h) induces
a surjection
S (h∗(P))↠ S (P).
(b) Let i : A ↪→ X be an embedding of abelian varieties with quotient
morphism q: X→B = X/A. Then we have an exact sequence
0 // Π(B)
Π(q) // Π(X)
Π(i) // Π(A) // 0.
In this situation we denote by K(A)⊆ Π(X) the image ofΠ(q).
Proof.The exactness of the considered sequences can be seen from the
description of a complex abelian variety as the quotient of a complex vector
space modulo a lattice. For the surjectivityS (g∗(P))↠ S (P) in part(a)
one can use thatHi(X,Pϕ) =Hi(B,g∗(P)χ) for the pull-backϕ = Π(g)(χ)
and thatΠ(g) is surjective. □
