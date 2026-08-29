---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-005-22-frobenius-algebras-and-2-categories
section_title: "Frobenius algebras and 2-categories"
section_number: 2.2
pages: 6-7
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Definition 2.1 Let A be a (strict) monoidal category. A Frobenius algebra in A is a
quintuple Q = ( Q, v, v′, w, w′), where Q is an object in A and v : 1 → Q, v′ : Q → 1, w :
Q → Q2, w′ : Q2 → Q are morphisms satisfying the following conditions:
w ⊗ idQ ◦ w = idQ ⊗ w ◦ w, (2.1)
w′ ◦ w′ ⊗ idQ = w′ ◦ idQ ⊗ w′, (2.2)
v′ ⊗ idQ ◦ w = idQ = idQ ⊗ v′ ◦ w, (2.3)
w′ ◦ v ⊗ idQ = idQ = w′ ◦ idQ ⊗ v, (2.4)
w′ ⊗ idQ ◦ idQ ⊗ w = w ◦ w′ = idQ ⊗ w′ ◦ w ⊗ idQ. (2.5)
A Frobenius algebra Q in a F-linear category is canonical if
w′ ◦ w = λ1idQ, (2.6)
v′ ◦ v = λ2id1 (2.7)
with λ1, λ2 ∈ F∗. Q is normalized if λ1 = λ2.
Let X be an object in a spherical category A. Then the quintuple
(XX, ε (X), ε(X), idX ⊗ ε(X) ⊗ idX, idX ⊗ ε(X) ⊗ idX )
is easily seen to be a normalized canonical Frobenius algebr a in A. The following theorem,
which combines the Theorems 3.12 and 5.13 from [38], shows th at in fact every canonical
Frobenius algebra in a tensor category arises in this way, pr ovided one is ready to embed
the category as a corner into a bicategory.
Theorem 2.2 Let A be a strict F-linear tensor category and Q = (Q, v, v′, w, w′) a canon-
ical Frobenius algebra in A. Then:
(i) There is a bicategory E such that
6
