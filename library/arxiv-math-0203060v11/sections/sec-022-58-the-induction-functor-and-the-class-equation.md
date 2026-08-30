---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-022-58-the-induction-functor-and-the-class-equation
section_title: "The induction functor and the class equation for fusion categories"
section_number: 5.8
pages: 21-22
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
ﬁnite group theory, an important role is played by the “class equatio n” ∑
s
1
|Gs| = 1,
where the summation is over conjugacy classes of a ﬁnite group G, and Gs are the
corresponding centralizers. There is a similar formula for semisimple H opf algebras
(due to G.I.Kac and Y.Zhu, see [Ka], [Zhu]), which is also very useful. Her e we will
prove a class equation for any fusion category, which generalizes t he results of Kac
and Zhu.
Let C be a fusion category. Let I : C → Z(C) be the induction functor, deﬁned
by the condition Hom Z(C)(I(V ),X ) = Hom C(V,X ),V ∈ C , X ∈Z(C).
Let [ X : Y ] denote the multiplicity of a simple object Y in an object X.
For X ∈ Z(C), let X|C denote the corresponding object of C. Then I(V ) =
⊕X∈Irr (Z(C))[X|C :V ]X.
Proposition 5.4. One has I(V )|C = ⊕Y ∈Irr (C)Y ⊗V ⊗Y ∗.
Example 5.5. If G is a ﬁnite group and C = Rep(G), then I(1) is the following
representation of the quantum double D(G) = C[G] ⋉ O(G): it is the regular
representation of the function algebra O(G), on which G acts by conjugation. In
this case proposition 5.4 for trivial V is the standard fact that for conjugation
action, O(G) = ⊕Y ∈Irrep (G)Y ⊗Y ∗.
Proof. Let C = Rep(A), where A is a weak Hopf algebra. Then Z(C) = Rep(D(A)),
whereD(A) is the quantum double of A (see [NTV]). As a space, D(A) = A∗ ⊗Amin
A. So we have I(V )|C =D(A) ⊗AV =A∗ ⊗Amin V , with the action of A deﬁned
by h(φ ⊗v) = h(3) ⇀ φ ↼ S(h(1)) ⊗h(2)v for all h ∈ A, φ∈ A∗, v ∈ V . This
yields exactly ⊕Y ∈Irr (C)Y ⊗V ⊗Y ∗, where the tensor product is taken in the
representation category of A. The proposition is proved. □
Proposition 5.6. The number ∑
X∈Irr (Z(C))[X|C : 1]2 is equal to the number of
simple objects of C.
Proof. This sum equals dim End( I(1)), which is the same as [ I(1)|C : 1]. But by
Proposition 5.4 we know that I(1)|C = ⊕Y ∈Irr (C)Y ⊗Y ∗, so the result follows. □
Proposition 5.7. (The class equation) Let C be a spherical fusion category. Then
one has ∑
X∈Irr (Z(C)):[X|C:1]⁄=0
[X|C : 1] 1
mX
= 1,
wheremX = dim C
dimX is an algebraic integer.
22 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Proof. The proposition is immediately obtained by computing the dimension of I(1)
in two ways. On the one hand, this dimension is equal to dim C by Proposition 5.4.
On the other hand, it equals ∑ [X|C : 1] dimX. The fact that mX is an algebraic
integer follows from Proposition 3.3. The proposition is proved. □
Example 5.8. Let C = Rep(G). In this case Z(C) = Rep D(G), so simple ob-
jects are parametrized by pairs (conjugacy class, irreducible rep resentation of the
centralizer). The simple objects X ∈ Z(C) for which X|C contains 1 are exactly
those for which the representation of the centralizer is trivial. Thu s, the equation
of Proposition 5.7 is exactly the class equation for G.
