---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-004-11-monoidal-functors-and-their-sheafification
section_title: "Monoidal functors and their sheafification"
section_number: 1.1
pages: 4-6
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
Deﬁnition 1.1. Let C and D be R-linear symmetric monoidal categories. A (contravariant)
pseudo-monoidal functor Ω: C →D is an R-linear (and contravariant) functor together with a
natural transformation
ιΩ
V,W : ΩV ⊗ΩW →ΩV ⊗W for V, W ∈C
A (contravariant) pseudo-monoidal functor Ω: C →D is
1)
symmetric or commutative if for all V, W ∈C the following diagram is commutative
ΩV ⊗ΩW
ΩV ⊗W
ΩW ⊗ΩV
ΩW⊗V
ιΩ
V,W
ιΩ
W,V
where the vertical arrows are the obvious isomorphisms;
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
5
2)
associative if for all V, W, Z ∈C the following diagram is commutative
ΩV ⊗ΩW ⊗ΩZ
ΩV ⊗W ⊗ΩZ
ΩV ⊗ΩW⊗Z
ΩV ⊗W⊗Z
ιΩ
V,W ⊗id
ιΩ
V,W ⊗Z
id⊗ιΩ
W,Z
ιΩ
V ⊗W,Z
If I and J are the unit objects of C and D respectively, a unity for Ωis a morphism 1: J →ΩI
such that, for all V ∈C , the compositions
ΩV ⊗J →ΩV ⊗ΩI →ΩV ⊗I →ΩV and J ⊗ΩV →ΩI ⊗ΩV →ΩI⊗V →ΩV
coincide with the natural isomorphisms ΩV ⊗J →ΩV and J ⊗ΩV →ΩV respectively.
A (contravariant) monoidal functor Ω: C →D is a symmetric and associative pseudo-
monoidal (contravariant) functor with a unity 1.
A (contravariant) strong monoidal functor
Ω: C →D is a (contravariant) monoidal functors such that all the maps ιΩ
V,W and 1: J →ΩI
are isomorphisms.
A morphism of pseudo-monoidal functors (Ω, ιΩ) →(Γ, ιΓ), called a monoidal morphism or
transformation, is a natural transformation Ω→Γ which commutes with the monoidal structures
ι∗. A morphism of monoidal functors is a monoidal transformation preserving the unities.
Deﬁnition 1.2. Let X be a ﬁbered category over R and C a full subcategory of QCoh(X). We
say that C generates QCoh(X) if all quasi-coherent sheaves on X are a quotient of a direct sum
of sheaves in C. We say that X has the resolution property if Vect(X) generates QCoh(X).
We will consider only fpqc stacks with quasi-aﬃne diagonal, for instance algebraic stacks with
quasi-aﬃne diagonal (see [LMB05, Corollary 10.7]) and quasi-separated schemes. This is because
resolution property is somehow meaningless for other stacks, see for instance Remark (1) in the
introduction of [Tot02].
Deﬁnition 1.3. [Ton20, Def 2.1] Let X be a ﬁbered category over R, A an R-algebra and D a
subcategory D ⊆QCoh(X).
We deﬁne LR(D, A) as the category of contravariant R-linear functors Γ: D →Mod A and
natural transformations as arrows. If D is a monoidal subcategory of QCoh X, that is a subcat-
egory such that OX ∈D and for all E, E′ ∈D we have E ⊗E′ ∈D, we also deﬁne the category
MLR(D, A) whose objects are Γ ∈LR(D, A) with a monoidal structure.
We denote by D⊕the full subcategory of QCoh(X) containing all the ﬁnite direct sums of
elements in D. Notice that a (contravariant) R-linear functor from D to an R-linear and additive
category extends uniquely to D⊕(see [Ton20, Prop 2.16]). We will denote this extension by the
same symbol. In other words we will evaluate a linear functor with source D also on objects and
maps of D⊕.
Deﬁnition 1.4. A ﬁnite test sequence for D is an exact sequence in QCoh(X) of the form
E′ →E →0 or E′′ →E′ →E →0 with E′′, E′, E ∈D⊕
If D ⊆Vect(X), X is quasi-compact and Y is another ﬁber category over R we say that a
(contravariant) R-linear functor Γ: D →QCoh(Y) is right (resp. left) exact if it is exact on all
test sequences in D. We deﬁne LexR(D, A) (resp. MLexR(D, A)) as the subcategory of LR(D, A)
(resp. MLR(D, A)) of left exact functors.
We deﬁne XA = X ×R A and
Ω∗: QCoh XA →LR(D, A), ΩG
H = HomX (π∗H, G)
where π: XA →X is the projection.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
6
Remark 1.5. The deﬁnition of test sequence and therefore of the categories LexR(D, A) and
MLexR(D, A) it is not completely equivalent to the one in [Ton20, Def 4.3]. As discussed in
the proof of the next Theorem the two notions agree when D generates QCoh(X): functors left
exact in the sense of [Ton20] are automatically left exact in our sense. In [Ton20] we were looking
for a minimal collection of test sequences which make results like the one below true under the
assumption that D generates QCoh(X). In this paper instead we will deal with more general
subcategories D and therefore this notion of test sequence seems more precise.
Theorem 1.6. Let X be a quasi-compact ﬁbered category over R and D ⊆Vect(X) be a full
subcategory that generates QCoh(X).
Then Ω∗: QCoh XA →LR(D, A) is fully faithful with
essential image LexR(D, A) and it has an exact left adjoint F∗,D : LR(D, A) →QCoh XA. In
particular Ω∗and (F∗,D)| LexR(D,A) are quasi-inverses of each other.
Assume that D is a monoidal subcategory of Vect(X). Then the functor Ω∗and F∗,D extends
to adjoint functors Ω∗: QAlg XA →MLR(D, A) and A∗,C : MLR(D, A) →QAlg XA. Moreover
Ω∗: QAlg(XA) →MLexR(D, A) is an equivalence and (A∗,C)| MLexR(D,A) is a quasi-inverse.
Proof. By [Ton20, Theorem A], [Ton20, Theorem B] and [Ton20, Theorem 6.8] the same result
works for the notion of test sequence given in [Ton20, Def 2.1]. On the other hand by [Ton20,
Prop 4.5] functors in the image of Ω∗: QCoh XA →LR(D, A) are automatically left exact in our
stronger sense.
□
Remark 1.7. If X is a quasi-compact ﬁbered category over R and C ⊆Vect(X) is a full (monoidal)
subcategory there always exists a full (monoidal) subcategory ˜C ⊆C such that eC is small, that
is the class ob( ˜C) is a set, and eC →C is an equivalence. In particular in this case the restriction
along eC →C induces an equivalence for all the categories of linear (monoidal) functors we have
considered. Thus, when X is a quasi-compact ﬁbered category over R, we will tacitly assume
that the category C is small.
To see how to ﬁnd eC we use the following argument. The category C is essentially small
because X is quasi-compact (see [Ton20, Prop 1.8]), so we can start taking R0 ⊆ob(C) so that
any sheaf in C is isomorphic to a sheaf in R0. If we don’t need duals or monoidal structure we
can stop here and consider as eC the full subcategory with objects in R0.
If C is a submonoidal category, this choice is not enough, since we don’t want to change the
⊗. Assume also OX ∈R0. At this point we denote by R the set of objects of C that can be
written using ﬁnitely many times ⊗and −∨, starting from objects in R0. Setting as ˜C the full
subcategory of C with objects in R makes the trick.
