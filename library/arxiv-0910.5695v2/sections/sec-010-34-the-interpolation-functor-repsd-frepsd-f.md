---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-010-34-the-interpolation-functor-repsd-frepsd-f
section_title: "The interpolation functor Rep(Sd; F)Rep(Sd; F)"
section_number: 3.4
pages: 19-21
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
tion we assume d is a nonnegative integer. In this section we will describe following
[Del07, §6] how Rep(Sd; F) “interpolates” the category Rep(Sd; F). More precisely,
20
JONATHAN COMES AND VICTOR OSTRIK
we will show Rep(Sd; F) is equivalent to the quotient of Rep(St; F) by the so-called
“negligible morphisms.” To start, let us deﬁne the interpolation functor.
Deﬁnition 3.18. F : Rep(Sd; F) →Rep(Sd; F) is the functor deﬁned on indecom-
posable objects by F([n], e) = f(e)(V ⊗n
d
), and on morphisms α : ([n], e) →([n′], e′)
by F(α) = f(α). Here f and Vd are as in section 2.1.
Notice that F is clearly a tensor functor. From the discussion in section 2.1 we
have the following.
Proposition 3.19. F is surjective on objects and morphisms.
Proof. This follows from Proposition 2.1 and Theorem 2.6(1).
□
However, by Theorem 2.6(2) we know that F does not induce an equivalence of
categories. To illustrate the amount by which F fails to induce an equivalence of
categories we need the following deﬁnition.
Deﬁnition 3.20. A morphism f : X →Y in a tensor category is called negligible
if tr (fg) = 0 for all g : Y →X. Set N(X, Y ) := {f : X →Y | f is negligible}.
Example 3.21. (1) The only morphisms in Rep0(S0; F) which are not negligible
are nonzero scalar multiples of id0 (see Example 2.22(1)).
(2) Let π : [1] →[1] be as in the proof of Theorem 3.4. Then xπ : [1] →[1],
deﬁned by equation (2.1), is given by xπ = π −id1. Since tr (π) = t = tr (id1), we
have tr (xπ) = 0. Moreover, xππ = (t−1)π so that tr (xππ) = t(t−1). We conclude
that xπ is negligible if and only if t = 0, 1.
(3) Consider the morphism π ∈HomRep0(St;F )([1], [2]) given by
From equation (2.1) we get xπ = π −µ1 −µ2 −µ3 + 2µ4 where
If we set
then one can compute tr (xπν0) = t(t −1)(t −2), and tr (xπνi) = 0 for i = 1, 2, 3, 4.
Thus xπ is negligible if and only if t = 0, 1, 2.
2
Remark 3.22. Each of the examples 3.21 follow from the following fact:
In
Rep0(St; F)
N([n], [m]) =
 SpanF {xπ | π ∈Pn,m has more than t parts},
if t ∈Z≥0
0,
otherwise.
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
21
For t ∈Z≥0 this fact follows from Theorem 2.6(2), Remark 2.17, along with the
following Proposition 3.23(2). For t̸ ∈Z≥0 we will eventually show that the larger
category Rep(St; F) is semisimple (see Corollary 5.23). It is well-known that there
are no nonzero negligible morphisms in a semisimple category.
Proposition 3.23. The following statements hold in any tensor category.
(1) N is a tensor ideal.
(2) The image under a full tensor functor of a morphism f is negligible if and
only if f is negligible.
Proof. Suppose f : A →B, g : B →A, and h : B ⊗C →A ⊗C are morphisms
in a tensor category. Observe that tr (f ◦g) = tr (g ◦f). Moreover, one can show
tr ((f ⊗idC) ◦h) = tr (f ◦(idA ⊗evC) ◦(h ⊗idC) ◦(idB ⊗coevC)). Statement
(1) follows. Statement (2) follows from the fact that a tensor functor preserves the
trace of a morphism.
□
Since there are no nonzero negligible morphisms in Rep(Sd; F), by Proposition
3.23(2) we conclude the functor F : Rep(Sd; F) →Rep(Sd; F) sends all negligible
morphisms to zero. Thus F induces a functor F : Rep(Sd; F)/N →Rep(Sd; F).
Theorem 3.24. F induces an equivalence of categories Rep(Sd; F)/N ∼= Rep(Sd; F).
Proof. This follows from Proposition 3.19 and Proposition 3.23(2).
□
We ﬁnish this section with the following proposition concerning the functor F.
For proof of the proposition we refer the reader to [Del07, Proposition 6.4]¶.
Proposition 3.25. Suppose d is a nonnegative integer and λ = (λ1, λ2, . . .) is a
Young diagram. If d −|λ| ≥λ1, then F(L(λ)) = Lλ(d). If d −|λ| < λ1, then
F(L(λ)) = 0.
