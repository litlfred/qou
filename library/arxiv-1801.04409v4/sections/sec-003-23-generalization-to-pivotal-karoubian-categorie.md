---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-003-23-generalization-to-pivotal-karoubian-categorie
section_title: "Generalization to pivotal Karoubian categories"
section_number: 2.3
pages: 5-8
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
results generalize to pivotal tensor categories ([EGNO], Subsectio n 4.7)
such that dim LX = 0 if and only if dim RX = 0 for any indecompos-
able object X ∈ C (an example of such a category which is not spherical
is the category of representations of the Taft Hopf algebra). Na mely,
in such a category, for any endomorphism h :X →X of an indecom-
posable object X, one has Tr L(h) = 0 if and only if Tr R(h) = 0. Thus,
if f : X → Y is a morphism between arbitrary objects of C, then the
condition that for any g :Y →X, one has Tr L(f ◦g) = 0 is equivalent
to the condition that for any g : Y → X, one has Tr R(f ◦g) = 0.
One then deﬁnes f to be negligible if any of these two equivalent con-
ditions is satisﬁed. Then Lemma 2.2, Lemma 2.3 and Proposition 2.4
generalize verbatim, with analogous proofs.
Moreover, the above results also extend to the case when C is a
Karoubian rigid monoidal category in which the trace of a nilpotent en -
domorphism is zero, a necessary condition for C to be embeddable into
an abelian tensor category. 1 For instance, the well-known construction
1Note that this condition is not necessarily satisﬁed: e.g. if char( k) = p, t ∈ k,
and Rep k(St) is the Karoubian Deligne category of representations of St ([EGNO],
5
of the fusion categories attached to a simple Lie algebra g (in character-
istic zero or p bigger than the Coxeter number), [EGNO], Subsection
8.18.2, starts with the category of tilting modules for the correspo nd-
ing (quantum) group (which is Karoubian), and takes a quotient by
the tensor ideal of negligible morphisms. Note that in this special cas e
negligible morphisms happen to be those that factor through negligib le
objects (i.e., direct sums of simple objects of dimension 0); this is not
the case in general (e.g., for Rep k(Z/p)).
To summarize, we have the following result. Let C be a pivotal
category, let dim L(X) := TrL(IdX), dimR(X) := TrR(IdX) for X ∈ C ,
and call a morphism f : X → Y negligible if for any g : Y → X one
has TrL(f ◦g) = 0.
Theorem 2.6. Let C be a k−linear Karoubian rigid monoidal category
such that all morphisms spaces are ﬁnite dimensional. 2 Assume that C
is equipped with a pivotal structure such that
(1) the left trace Tr L of any nilpotent endomorphism is zero;
(2) dimLX = 0 if and only if dimRX = 0 for an indecomposable
X ∈ C .
Then negligible morphisms are characterized as in Lemma 2.2 and
form a tensor ideal N (C). Moreover, C/N (C) is a semisimple tensor
category, whose simple objects are the indecomposable obje cts of C of
nonzero dimension.
Proof. First of all, (1) implies that the right trace of any nilpotent en-
domorphism in C is zero, since Tr L(f ) = TrR(f ∗), see [EGNO], Propo-
sition 4.7.3.
Hence, for an endomorphism h : X →X, TrL(h) = 0 if and only if
TrR(h) = 0. Indeed, by decomposing X into generalized eigenobjects
of h, we may assume that h = λId +h0, where h0 is nilpotent. Then
TrL(h) = λ dimLX and TrR(h) = λ dimRX (as TrL(h0) = TrR(h0) =
0), so our claim follows from (2).
The rest of the proof is parallel to the spherical abelian case. □
Example 2.7. 1. If C is semisimple, then
C ∼= C. Moreover, in this
case for any tensor category D one has C ⊠ D ∼= C ⊠ D.
Subsection 9.12) then this property holds only if t ∈ Fp ⊂ k; namely, if σ is the
cyclic permutation on X ⊗ p, where X is the tautological object, then (1 − σ )p = 0
but Tr(1 − σ ) = tp − t.
2Note that any Karoubian linear category with ﬁnite dimensional morp hism
spaces satisﬁes the Krull-Schmidt theorem, which says that any ob ject has a unique
decomposition into a direct sum of indecomposables (up to a non-uniq ue iso-
morphism); for this reason, such categories are sometimes called K rull-Schmidt
categories.
6
2. If char( k) = p > 0 and C = Rep k(Z/p) then C is the Verlinde
category Verp introduced by Gelfand-Kazhdan and Georgiev-Mathieu,
see [O] and references therein.
3. Let char( k) = 0 and C = Rep GL(n|1), n ≥ 1. Then C =
Rep(GL(n − 1) ×GL(1) ×GL(1)) ⊠ Supervec, where Supervec is the
category of supervector spaces, see [H], Theorem 4.13.
4. Let G = ( Z/2Z)2 and char( k) = 2. Then it is well known that
indecomposable representations of G over k of non-zero mod 2 (i.e.
odd) dimension are precisely Ω n(1),n ∈ Z, where Ω is the Heller shift
operator, see e.g. [B1, Theorem 4.3.3]. Also one deduces from [B1,
Corollary 3.1.6] that
Ωn(1) ⊗ Ωm(1) ≃ Ωn+m(1) ⊕ a projective module .
Thus
Repk(G) = Vec Z = RepGL(1).
Remark 2.8. 1. It is clear that if C is symmetric or braided, then so
is C and the functor S.
2. If C is ﬁnite then C may be inﬁnite (see Example 2.7(4)), and
can, in fact, be unmanageably large, since the problem of classifying
indecomposable objects in ﬁnite abelian categories is often wild (in
fact, this is already so for Rep k(Z/p)2, where char( k) = p> 2).
Remark 2.9. 1. Let C = Rep H, where H is a ﬁnite dimensional
Hopf algebra over a ﬁeld k of characteristic zero. Then condition (2)
of Theorem 2.6 (that dim LX = 0 if and only if dim RX = 0) holds for
any pivotal structure. Indeed, we may assume that k = C. A pivotal
structure on Rep H is given by a grouplike element g ∈ H such that
gxg −1 =S2(x) for x ∈H, and dim LX = TrX(g), dimRX = TrX (g−1).
Butg has ﬁnite order, so the eigenvalues of g are roots of unity, hence
dimRX =
dimLX, as desired. We expect that the same holds for any
ﬁnite tensor category over a ﬁeld of characteristic zero.
However, the above condition can be violated for categories of ﬁnit e
dimensional modules or comodules over an inﬁnite dimensional Hopf
algebra. For example, let C be the category of ﬁnite dimensional repre-
sentations ofUq(b),q ∈ C×, where b ⊂ sl3 is a Borel subalgebra. Recall
that a pivotal structure on C is deﬁned by the element K =q2ρ. Let X
be the Uq(b) subrepresentation of the adjoint representation of Uq(sl3)
(with highest weight α1 +α2) spanned by the vectors whose weights
are positive roots. Then dim LX = 2q2 +q4 and dimRX = 2q−2 +q−4.
So if q2 = −2 then dim LX = 0 but dim RX = −3/4 ⁄= 0.
The same happens in characteristic p, even for a ﬁnite dimensional
Hopf algebra. Namely, we can take the same example. Note that
7
q2 = −2 is then a root of unity (or some order dividing p − 1), so one
may replace Uq(b) with the corresponding small quantum group uq(b).
2. Condition (1) of Theorem 2.6 holds true if C is an abelian tensor
category, since the quantum trace is additive on exact sequences , see
e.g. [EGNO, Proposition 4.7.5]. Moreover, assume that there exists a
pivotal tensor functor C → D , where the category D satisﬁes condition
(1) of Theorem 2.6 (e.g., D is abelian). Then obviously the category
C also satisﬁes condition (1) of Theorem 2.6. This observation was
used by U. Jannsen to prove that the category of numerical motiv es is
semisimple, see [Ja]. Moreover, the assumption on ﬁnite dimensionality
of morphism spaces in C in Theorem 2.6 can be dropped if there exists
a pivotal monoidal functor F : C → D ′, where all morphism spaces
in D′ are ﬁnite dimensional, since the tensor ideal of morphisms sent
by F to zero consists of negligible morphisms, which implies ﬁnite
dimensionality of morphism spaces in C/N (C).
Here is an example of such a situation. Take any collection of mor-
phisms in a symmetric tensor category D, compute some of relations
between them, and deﬁne C to be the Karoubian envelope of the uni-
versal symmetric monoidal category generated by morphisms sat isfying
these relations. Then we have an obvious symmetric monoidal funct or
C → D , hence the semisimpliﬁcation of C is a semisimple symmetric
tensor category.
