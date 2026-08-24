---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-015-15-the-spectrum-of-a-perverse-sheaf-19
section_title: "The spectrum of a perverse sheaf 19"
section_number: 1.5
pages: 27-28
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
In what follows, letE(X) be the class of all semisimple perverse sheaves
on X with Euler characteristic zero. We say that a perverse sheaf is clean
if it does not contain constituents fromE(X). For x∈ X(C) we denote
bytx : X→X the translation morphismy↦→x+y, and forK∈ Dbc (X,C) we
consider the stabilizer
Stab(K) = {x∈ X(C)| t∗
x (K)∼= K}.
By constructibility ofK this is an algebraic subset ofX, and its connected
componentStab(K)0⊆ Stab(K) is an abelian subvariety ofX. We can now
formulate the main result of the present section.
LEMMA 1.11. (a) Let P∈E(X) be a semisimple perverse sheaf of Euler
characteristic zero. Then a characterχ lies inS (P) iff H•(X,Pχ)⁄= 0. In
particular, if P is simple, there exists a characterϕ such that
S (P) = ϕ−1·K(A) for A = Stab(P)0
where K(A)⊂ Π(X) is the algebraic subtorus from remark 1.10(b).
(b) For any semisimple perverse sheaf P on X there are non-zero abelian
subvarieties A1, . . . ,An⊆ X and χ1, . . . ,χn∈ Π(X) such that
S (P) =
n⋃
i=1
χi·K(Ai).
(c) If in part (b) the semisimple perverse sheaf P is of geometric origin in
the sense of[10, 6.2.4], then theχi can be chosen to be torsion characters.
Proof. (a) The ﬁrst statement is obvious from proposition 1.6(a), and
the second one follows easily from the proof of corollary 1.7.
(b)The proof of this part is most conveniently formulated in terms of the
convolution product∗ to be deﬁned in section 2.1 below. For the time being
it sufﬁces to know that the convolution of semisimple sheaf complexes is
again a semisimple sheaf complex by Gabber’s decomposition theorem, that
for K,M∈ Dbc (X,C) we have the K¨unneth formula
H•(X,K∗M) = H•(X,K)⊗CH•(X,M)
and that convolution is compatible with character twists in the sense that for
all χ∈ Π(X) we have(K∗M)χ∼= Kχ∗Mχ, see proposition 2.1. Hence for
theg-fold convolution power of a semisimple perverse sheafP∈Perv(X,C)
it follows from theorem 1.1 thatP∗g = Q⊕⨁
ν∈ZNν[ν] whereQ is a clean
semisimple perverse sheaf and theNν are semisimple perverse sheaves
in E(X). So for anyχ∈ Π(X) we obtain
(⋆) H•(X,Pχ)⊗g = H•(X,Qχ)⊕
⨁
ν∈Z
H•(X,(Nν)χ)[ν].
