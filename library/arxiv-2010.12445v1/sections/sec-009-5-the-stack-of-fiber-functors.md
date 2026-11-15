---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-009-5-the-stack-of-fiber-functors
section_title: "The stack of fiber functors"
section_number: 5
pages: 18-20
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
The last statement of Theorem 3.2 admits an almost converse. Let X be a ﬁbered category
over R and C ⊆Vect X be a full monoidal subcategory. We deﬁne
G∗: C →Hom(FibX ,C, VectR)
where VectR is the stack of locally free sheaves over R, mapping a sheaf E ∈C to
GE(Γ ∈FibX ,C(A)) = ΓE ∈Vect(A) for all R-algebras A
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
19
In particular the composition X →FibX ,C
GE
−−→VectR is just E ∈C. Notice that, a priori, FibX ,C
is not necessarily ﬁbered in groupoids and therefore the notion of a locally free sheaf on it is not
deﬁned (although one can easily guess the deﬁnition). In the next result we will see that, under
suitable conditions on C, the stack FibX ,C is ﬁbered in groupoid. In this case G∗will just be a
map G∗: C →Vect(FibX ,C), which is easily seen to be a covariant strong monoidal functor.
Given a function f : C →N we deﬁne Fibf
X ,C as the sub-ﬁbered category of FibX ,C of functors
Γ such that rk ΓE = f(E) for all E ∈C.
We summarize all the main results of this section in the following:
Theorem 5.1. Let X be a quasi-compact ﬁbered category over R and C ⊆Vect X be a full
monoidal subcategory with duals. If R is not a Q-algebra assume moreover that Symn E ∈C for
all E ∈C and n ∈N. Set also
I = {f : C →N | ∃ξ : Spec L →X with f(E) = rk(ξ∗E) for all E ∈C}
Then FibX ,C is an fpqc stack in groupoids and:
1) Fibf
X ,C̸ = ∅if and only if f ∈I.
2) Using notation from Section 1.2, we have D(E) = D(GE) and Q(E) = Q(GE) for E ∈C,
so that D(C) = D(C →Vect(X)) = D(G∗: C →Vect(FibX ,C)) is an aﬃne scheme. If we
think GL(Q(E)) as a group scheme over D(C) and set G = Q
E GL(E) →D(C) then the
map (see 1.13)
FibX ,C →B G
is pseudo-aﬃne.
In particular U = Fr(G∗: C →Vect(FibX ,C)) is pseudo-aﬃne and
FibX ,C ≃[U/G].
3) FibX ,C is a quasi-compact fpqc stack with aﬃne diagonal and the subcategory {GE}E∈C ⊆
Vect(FibX ,C) generates QCoh(FibX ,C). In particular FibX ,C has the resolution property.
4) If f ∈I then the map Spec R →D(C) induced by the constant function (f(E))E : Spec R →
Q
E ranks(E) (see 1.9) is well deﬁned and we have Cartesian diagrams
Fibf
X ,C
B GLf
Spec R
FibX ,C
B G
D(C)
ω
where GLf = Q
E GLf(E) and ω is induced by the (GE)E∈C. The vertical maps are ﬂat
closed immersion, ω: Fibf
X ,C →B GLf is pseudo-aﬃne, U = Fr(G∗: C →Vect(Fibf
X ,C))
is pseudo-aﬃne, Fibf
X ,C ≃[U/ GLf] and {GE}E∈C ⊆Vect(Fibf
X ,C) generates QCoh(Fibf
X ,C).
In particular Fibf
X ,C is a quasi-compact fpqc stack in groupoids with aﬃne diagonal and
the resolution property.
5) Assume the category C has the following two properties: there exists a ﬁnite set J of
objects of C such that any objects of C can be obtained by sheaves of J using the operations
⊗, ⊕, −∨, Symm, Λm several times; there is a ﬁnite set of ﬁnite test sequences for C
such that if Γ: C →Vect(A) is an R-linear strong monoidal functor with then Γ is exact.
Then FibX ,C is an algebraic stack and a quotient [U ′/ GLm] for some quasi-aﬃne scheme
U ′.
Remark 5.2. It is not clear if Fibf
X ,C is algebraic even if X is a projective scheme and we choose
a C that does not generate QCoh(X). The statement of 5.1, 5) is not really satisfactory for two
reasons. The ﬁrst condition requires C to be not too big, for example C = Vect(X) in general
will not have this property. The second problem is that it is not clear when the second condition
is satisﬁed.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
