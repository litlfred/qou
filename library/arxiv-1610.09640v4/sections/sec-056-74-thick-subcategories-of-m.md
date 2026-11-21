---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-056-74-thick-subcategories-of-m
section_title: "Thick Subcategories of M"
section_number: 7.4
pages: 138-139
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
categories.
Deﬁnition 7.4.1. Let M be an abelian category. A thick abelian subcategory of M
is a full abelian subcategory N that is closed under extensions. Namely if
0 →M ′ →M →M ′′ →0
is a short exact sequence in M with M ′, M ′′ ∈N, then M ∈N too.
Proposition 7.4.2. Let M be an abelian category, and let M′ ⊆M be a thick abelian
subcategory. Suppose M1 →M2 →N →M3 →M4 is an exact sequence in M, and
the objects Mi belong M′. Then N ∈M′ too.
Exercise 7.4.3. Prove this proposition.
Deﬁnition 7.4.4. Let M be an abelian category and N ⊆M a thick abelian subcat-
egory. We denote by DN(M) the full subcategory of D(M) consisting of complexes
M such that Hi(M) ∈N for every i.
Given a boundedness condition ⋆,
we write D⋆
N(M) := DN(M) ∩D⋆(M) and
DN(M)⋆:= DN(M) ∩D(M)⋆.
Proposition 7.4.5. If N is a thick abelian subcategory of M then DN(M) is a full
triangulated subcategory of D(M).
Proof. Clearly DN(M) is closed under translations.
Now suppose M ′ →M →
M ′′
△
−−→is a distinguished triangle in D(M) such that M ′, M ∈DN(M); we have to
show that M ′′ is also in DN(M). Consider the exact sequence Hi(M ′) →Hi(M) →
Hi(M ′′) →Hi+1(M ′) →Hi+1(M).
The four outer objects belong to N.
Since
N is a thick abelian subcategory of M it follows (using Proposition 7.4.2) that
Hi(M ′′) ∈N.
□
Example 7.4.6. Let A be a noetherian commutative ring. The category Modf A
of ﬁnitely generated modules is a thick abelian subcategory of Mod A.
Example 7.4.7. Consider Mod Z = Ab.
As above we have the thick abelian
subcategory Abf = Modf Z of ﬁnitely generated abelian groups. There is also the
thick abelian subcategory Abtors of torsion abelian groups (every element has a
ﬁnite order).
The intersection of Abtors and Abf is the category Abﬁn of ﬁnite
abelian groups. This is also thick.
Example 7.4.8. Let X be a noetherian scheme (e.g. an algebraic variety over an
algebraically closed ﬁeld). Consider the abelian category Mod OX of OX-modules.
In it there is the thick abelian subcategory QCoh OX of quasi-coherent sheaves, and
in that there is the thick abelian subcategory Coh OX of coherent sheaves.
Passing to complexes, let us write C(X) := C(Mod OX), the DG category of
unbounded complexes. Its strict subcategory is Cstr(X), and for each bounded-
ness condition ⋆we have the full subcategory C⋆
str(X) ⊆Cstr(X). For the derived
category we write D(X) := D(Mod OX). Inside it there are the full triangulated
subcategories
Dc(X) := DCoh OX(Mod OX) ⊆Dqc(X) := DQCoh OX(Mod OX).
One
can
show
(see
[62,
Corollary
II.7.19])
that
the
canonical
functor
D+(QCoh OX) →D+
qc(X) is an equivalence.
The proof is based on the deep
fact (see [62, Theorem II.7.18]) that QCoh OX has enough injectives relative to
Mod OX, in the sense of Deﬁnition 11.5.7. Then Theorem 11.5.8 says that every
complex M ∈D+
qc(X) admits a quasi-isomorphism M →I in Cstr(X), where I is
a bounded below complex of injective quasi-coherent OX-modules.
138
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Then, using smart truncations and the fact that every quasi-coherent sheaf on
X is the direct limit of its coherent subsheaves, one can show that the canonical
functor Db(Coh OX) →Db
c(X) is an equivalence. See [70, Proposition 3.5]; when
X = Spec(A) is aﬃne see also Proposition 7.4.9 below. The category Db
c(X) is
the focus of a signiﬁcant part of the research in modern algebraic geometry (e.g.
birational geometry, see [70]).
A totally diﬀerent approach yields this result: if X is separated and quasi-
compact, then the canonical functor D(QCoh OX) →Dqc(X) is an equivalence.
See [23, Corollary 5.5].
For a left noetherian ring A we write Df(Mod A) := DModf A(Mod A).
Proposition 7.4.9. Let A be a left noetherian ring and ⋆∈{−, b}. Then the
canonical functor D⋆(Modf A) →Df(Mod A)⋆is an equivalence of triangulated cat-
egories.
Proof. Consider the functor F : D−(Modf A) →D(Mod A). Suppose s : M →L
is a quasi-isomorphism in K(Mod A), such that L ∈K−(Modf A).
Then M ∈
Df(Mod A)−. A bit later (in Theorem 11.4.40) we will prove that M admits a free
resolution P →M, where P is a bounded above complex of ﬁnitely generated free
modules. Thus we get a quasi-isomorphism t : P →M with P ∈K−(Modf A). By
Proposition 7.1.13 with condition (r) we conclude that F is fully faithful. This also
shows that the essential image of F is Df(Mod A)−.
Next consider the functor G : Db(Modf A) →D−(Modf A). Suppose s : L →
M is a quasi-isomorphism in K−(Modf A) with L ∈Kb(Modf A).
Say H(L) is
concentrated in the integer interval [d0, d1].
Then t : M →smt≥d0(M) is a
quasi-isomorphism, and smt≥d0(M) ∈Kb(Modf A).
By Proposition 7.1.13 with
condition (l) we conclude that G is fully faithful.
Therefore the composition
F ◦G : Db(Modf A) →D(Mod A) is fully faithful. Suitable truncations (smt≥d0
and smt≤d1) show that the essential image of F ◦G is Df(Mod A)b.
□
