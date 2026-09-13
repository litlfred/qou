---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-009-42-derived-categories-of-graded-abelian-categori
section_title: "Derived categories of graded abelian categories"
section_number: 4.2
pages: 11-12
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
categories. We recall that if A is an abelian category, then the bounded derived category Db(A)
has a standard t-structure ( Db(A)≤0,D b(A)≥0) whose heart is A.
Given a B ⊂ A a Serre subcategory, we let Db
B(A) ⊂ Db(A) denote the thick subcategory
consisting of complexes with cohomology supported in B. The category Db
B(A) inherits a natural
t-structure from the standard t-structure on Db(A): Db
B(A)≤0 =Db
B(A)∩Db(A)≤0 andDb
B(A)≥0 =
Db
B(A) ∩Db(A)≥0. The heart of the t-structure on Db
B(A) is B. Moreover, if C ⊂ B is another Serre
subcategory then the t-structure on Db
B(A) is compatible with Db
C(A). In particular, the quotient
Db
B(A)/Db
C(A) inherits a natural t-structure whose heart is B/C.
For the remainder of this section let A, A′ be graded abelian categories. In the setting of derived
categories of graded abelian categories, a perverse equiva lence can be packaged as follows. We can
encode a perversity triple ( A•, A′
•,p ) using ﬁltrations on the abelian categories: A• and A′
• are
ﬁltrations by shift-invariant Serre subcategories:
0 = A−1 ⊂ A 0 ⊂ A 1 ⊂... ⊂ A r = A, 0 = A′
−1 ⊂ A ′
0 ⊂ A ′
1 ⊂... ⊂ A ′
r = A′.
Then a graded equivalence F :Db(A) →Db(A′) is a perverse with respect to ( A•, A′
•,p ) if conditions
(1) and (2) of Deﬁnition 4.1 hold for Ti =Db
Ai(A) and T ′
i =Db
A′
i
(A′)
As above, a graded perverse equivalence F :Db(A) →Db(A′) induces a bijection ϕF : Irr(A) →
Irr(A′).
The following standard lemma will be useful in the proof of ou r main result.
12 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
Lemma 4.8. Let A, A′ be abelian categories, and B, B′ Serre subcategories. Let a ≤b be integers,
and Fi : A → A ′ be exact functors for a ≤ i ≤ b. Suppose these functors ﬁt into a complex
F = (Fa → Fa+1 → · · · → Fb), deﬁning a functor
F :Db(A) →Db(A′).
If Fi(B) ⊂ B ′ for all a ≤i ≤b, then F(Db
B(A)) ⊆Db
B′(A′).
