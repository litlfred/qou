---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-016-24-homological-properties-of-the-adjoint-action
section_title: "Homological properties of the adjoint action"
section_number: 2.4
pages: 8-8
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
L rests in its role linking homological algebra over A with that over Ae, thus per-
mitting the calculation of Hochschild cohomology. The key lemma is the f ollowing
result of Ginzburg and Kumar [GK, Proposition p.197]:
Lemma. [GK] Let A be a Hopf algebra and let M be an A-bimodule.
(a) HomAe (A, M) = Hom A(k, L(M )) = Z(M ).
(b) If S is bijective, Exti
Ae(A, M) = Ext i
A(k, L(M )) for all i.
Proof. (a) This was proved in [GK, Proposition p.197]. We oﬀer a proof following
the line of the proof of [Mo, Lemma 5.7.2(1)]. By deﬁnition,
HomAe (A, M) = {m ∈ M | am = ma, ∀ a ∈ A} = Z(M )
and
HomA(k, L(M )) = {m ∈ M |
∑
a1mS(a2) = ǫ(a)m, ∀ a ∈ A}.
If ∑ a1mS(a2) = ǫ(a)m for all a ∈ A, then
am =
∑
a1mǫ(a2) =
∑
a1mS(a2)a3 =
∑
ǫ(a1)ma2 = ma.
Conversely, if am = ma for all a ∈ A, then
∑
a1mS(a2) =
∑
a1S(a2)m = ǫ(a)m.
Thus (a) follows.
(b) Let I be an injective Ae-resolution of M . Since L is exact and preserves injec-
tive modules by Lemma 2.2(d), L(I) is an injective resolution of L(M ). Therefore
(b) follows from (a) by replacing M by its injective resolution. □
Remark. In [GK] part (b) was stated for any Hopf algebra. But it seems to us
that the bijectivity of S is needed. This should also be compared to Proposition
3.3 in which case the bijectivity is not needed.
