---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-016-2-the-rˆ-ole-of-the-assumption-on-the-dimension
section_title: "The rˆ ole of the assumption on the dimension is obvious: If dim C = 0 then the"
section_number: 2
pages: 14-16
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
map EX,X with the factor (dim C)−1 removed is identically zero on End Z1(C)(X), thus we
cannot use it to obtain a conditional expectation.
14
3. The proof uses a special instance of the ‘handle sliding’ w hich is formalized in [1].
✷
Lemma 3.12 For every X ∈ C we have trX ◦ EX,X = trX, where trX is the trace on
EndC(X) provided by the spherical structure.
Proof. Let t ∈ HomC(X, X). Using the fact that the spherical structure of Z1(C) is
induced from C we compute
dim C tr ◦ EX,X (t) =
∑
i
di
ε(X)
✬ ✩
☛ ✟
❆❆
✁
✁
✁
❆❆
Xi
✎
✍
☞
✌
t
Xi
❆❆
✁
✁
✁
❆❆
X X ✡ ✠ε(Xi)
✡ ✠ε(X)
=
∑
i
di
✬ ✩
☛ ✟
❆❆
✁
✁
✁
❆❆
Xi
✎
✍
☞
✌
t
Xi
❆
❆
❆ ✁✁
✁✁
✡ ✠ X
✫ ✪ε(X)
=
∑
i
di
∑
j,α
✛ ✘
☛ ✟
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌
t
Xi
❆
❆
❆ ✁✁
✁✁
X
✡ ✠tα
Xj Xj
✚ ✙
ε(Xj )
=
∑
i
di
∑
j,α
✛ ✘
☛ ✟
Xi
✎
✍
☞
✌
t
Xi
✡ ✠
✚ ✙
=
∑
i
di
✬ ✩
☛ ✟
Xi X
✎
✍
☞
✌
t
Xi
✡ ✠
✫ ✪ε(Xi)
= dim C tr(t).
In the ﬁrst step we have used Proposition 3.9, the second is ba sed on standard prop-
erties of categories with duals. In the next step we use that, given a basis {tα} in
HomC(Xj, XiX) with dual basis {ˆtα}, {eX (Xi)◦tα} is a basis in Hom C(Xj, XXi) with dual
basis {ˆtα ◦eX (Xi)−1}. Replacing one basis by the other leaves the expression inva riant. ■
A trace on a ﬁnite dimensional F-algebra A is a F-linear map A → F such that
tr(ab) = tr(ba). It is non-degenerate if for every a ⁄= 0 there is b such that tr(ab) ⁄= 0.
Lemma 3.13 Let A be a ﬁnite dimensional F-algebra and tr : A → F a non-degenerate
trace. If tr is vanishes on nilpotent elements then A is semisimple. Conversely, every trace
(not necessarily non-degenerate) on a semisimple algebra v anishes on nilpotent elements.
15
Proof. Well known, but see, e.g., [38]. ■
Lemma 3.14 Let A be a ﬁnite dimensional semisimple algebra over F with a non-dege-
nerate trace tr : A → F. Let B be a subalgebra containing the unit of A and assume there
is a conditional expectation E : A → B (i.e. a linear map such that E(bab′) = bE(a)b′ for
a ∈ A, b, b′ ∈ B) such that tr ◦ E = tr. Then B is semisimple.
Proof. Let 0 ⁄= x ∈ B. By non-degeneracy of tr there is y ∈ A such that tr(xy) ⁄= 0.
Now, using the properties of E we compute 0 ⁄= tr(xy) = tr ◦ E(xy) = tr(xE(y)). Since
E(y) ∈ B we conclude that the restriction trB ≡ tr ↾ B is non-degenerate, too. By
Lemma 3.13 tr vanishes on nilpotent elements, thus the same trivially hol ds for trB. Now
the other half of Lemma 3.13 applies and B is semisimple. ■
Remark 3.15 Algebra extensions A ⊃ B admitting a conditional expectation E : A → B
(satisfying certain conditions) are well known as Frobeniu s extensions, cf., e.g., [21] and
are called Markov extensions if there is an E-invariant trace on A. ✷
Now we can put everything together:
Theorem 3.16 Let F be algebraically closed and C a F-linear, spherical and semisimple
tensor category. We assume that there are only ﬁnitely many s imple objects and that
dim C ⁄= 0. Then the quantum double Z1(C) is spherical and semisimple.
Proof. Recall that by our deﬁnition of semisimplicity, C has direct sums, subobjects and
a simple unit. By our earlier results also Z1(C) has these properties and is spherical. It
therefore only remains to show that the endomorphism algebr a of every object of Z1(C)
is a multi matrix algebra.
Let ( X, eX ) ∈ Z 1(C). Then End C(X) is a ﬁnite dimensional multi matrix alge-
bra by semisimplicity of C. The trace on End C(X) provided by the duality structure
is non-degenerate, cf. e.g. [16, Lemma 3.1], and Lemmas 3.10 , 3.12 provide us with a
trace preserving conditional expectation EX : End C(X) → EndZ1(C)((X, eX )). Thus
EndZ1(C)((X, eX )) is semisimple by Lemma 3.14 and therefore a multi matrix al gebra
since F is assumed algebraically closed. ■
Remark 3.17 1. Even if ( X, eX ) is simple as an object of Z1(C) there is no reason why
X should be simple in C. Usually it is not. Since we do not know a priori which non-
simple objects of C appear in the simple objects of Z1(C) we cannot dispense with the
assumption that C has all ﬁnite direct sums as done, e.g., in [53].
