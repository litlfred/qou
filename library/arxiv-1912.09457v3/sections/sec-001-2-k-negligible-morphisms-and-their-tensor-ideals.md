---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-001-2-k-negligible-morphisms-and-their-tensor-ideals
section_title: "k-negligible morphisms and their tensor ideals"
section_number: 2
pages: 5-10
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
2.1. Preliminaries. In the following let R be a local ring with maximal
ideal m. We assume CR (or sometimes simply C) to be a monoidal rigid
spherical category whose Hom spaces are free R-modules and such that
End(1) = R (see e.g. [ EGNO15, Section 4.7] for details). For simplicity we
additionally assume that CR is braided. Otherwise we would have to dis-
tinguish between left thick ideals and right thick ideals an d between partial
and modiﬁed traces for the left and right versions. However, the followings
notions make sense without the added braided if one is willing to either work
with left or right versions of these.
Recall that under these assumptions there exist, for each ob jectX in CR,
canonical morphisms
iX : 1 →X ⊗X ∗, ˜dX :X ⊗X ∗ → 1
6 THORSTEN HEIDERSDORF AND HANS WENZL
via which we can deﬁne the traceTr X on End(X) by
Tr X(a) = ˜dX (a ⊗idX ∗ )iX, for all a ∈ End(X);
here iX and dX ∗ : X ∗∗ ⊗X ∗ → 1 are the morphisms in the deﬁnition of
rigidity for the objects X and X ∗, and ˜dX = dX ∗ ◦ (sX ⊗ 1). The isomor-
phismssX :X →X ∗∗ from the spherical structure are normalized such that
dim(X) = dim(X ∗) for all objects X in C, where dim( X) = Tr (idX ). For
elementsa ∈ End(X ⊗Y ), we can also deﬁne the partial trace or conditional
expectationEX : End(X ⊗Y ) → End(X) by
EX(a) = (idX ⊗ ˜dY )(a ⊗idY ∗)(idX ⊗iY ).
The name partial trace is justiﬁed by the equation
Tr X(EX (a)) = Tr X⊗Y (a), a ∈ End(X ⊗Y ).
2.2. T ensor ideals. Let C be a monoidal category. A tensor ideal I in C
consists of an R-submodule I(X,Y ) ⊂ Hom(X,Y ) for all X,Y ∈ C such
that
• for all X,Y,Z,W ∈ C and g ∈Hom(X,Y ) and h ∈Hom(Z,W )
f ∈ I (Y,Z ) implies f ◦g ∈ I (X,Z ) and h ◦f ∈ I (Y,W );
• f ∈ I (X,Y ) implies idZ ⊗f ∈ I (Z ⊗X,Z ⊗Y ) and likewise from
the right.
A collection of objects I in a monoidal category C is called a thick ideal
of C if the following conditions are satisﬁed:
(i) X ⊗Y ∈I wheneverX ∈ C and Y ∈I.
(ii) If X ∈ C , Y ∈ I and there exist α : X → Y , β : Y → X such that
β ◦α = idX, then X ∈I.
To any tensor ideal I we can associate the thick ideal I given by
I = {X ∈ C | idX ∈ I (X,X )}.
One of the major reasons to study the tensor ideals and thick i deals in C
is due to the fact that the morphisms that are sent to zero unde r a monoidal
functor C → C ′ to another monoidal category C′ form a tensor ideal; and the
objects of C that are sent to zero form a thick ideal.
2.3. Generalized negligible morphisms. Let R be a local ring and CR
as in section
2.1.
Deﬁnition 2.1. a) LetI ⊂R be an ideal. We call a morphism f :X →Y I-
negligible if Tr X(g ◦f ) ∈I andTr Y (f ◦g) ∈I for all morphisms g :Y →X.
An object X is called I-negligible if Tr X (a) ∈I for all a ∈ End(X).
b) If f is I-negligible with respect to I = mk, we simply say that f is
k-negligible. An object is k-negligible if it is I-negligible for I = mk.
Lemma 2.2. The I-negligible morphisms form a tensor ideal NI in the
category CR. The I-negligible objects form a thick ideal NI in CR.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 7
Proof. It is easy to see that NI is an ideal using Tr (f ◦g) = Tr (g ◦f ) for
composable morphisms f : X → Y , g : Y → X [Ka95, Theorem XIV.4.2].
Now let f ∈ N I(X,Y ) and g ∈Hom(W,Z ) arbitrary for X,Y,W,Z in CR.
Leth ∈Hom(Y ⊗Z,X ⊗W ). Then
Tr ((f ⊗g) ◦h) = Tr (h ◦ (f ⊗g)) = Tr (h′ ◦f )
for some h′ :Y →X (as in [ BW99, Theorem 2.9]). Since f is I-negligible,
this implies Tr ((f ⊗g) ◦h) ∈I.
Let now X be an I-negligible object, and Y any object in C. If a ∈
End(X ⊗Y ), we have
Tr X⊗Y (a) = Tr X(EX (a)) ∈I,
as EX(a) ∈ End(X) and X is I-negligible. Hence X ⊗Y is an object in NI
as well. □
Remark 2.3. The deﬁnition is similar to the the one of the Jantzen ﬁltrati on
on morphisms deﬁned by the form Tr (f ◦g).
2.4. The mod m evaluation. We are primarily interested in categories
whose Hom spaces are vector spaces over a ﬁeld. Recall that if M is a
freeR-module of rank r, we obtain a well-deﬁned vector space M/mM over
k =R/m of dimensionr. We call the mod m evaluation (or reduction modulo
m) of CR the category C over k whose objects are in 1-1 correspondence with
the ones of CR, and where
Hom C(X,Y ) = Hom CR(X,Y )/mHom CR(X,Y ) ∼
=Hom CR(X,Y ) ⊗RR/m.
In the following, the notations Hom, End etc will refer to the evaluation
category C. The corresponding spaces for CR will be denoted by Hom R,
EndR etc. We call CR a lift of C.
2.5. Examples. We give some examples of the lifting of a monoidal cate-
gory C over k to a monoidal category over a local ring.
2.5.1. Fusion categories. Let k be any ﬁeld, R a local ring with R/m ∼
= k.
If C is a split fusion category over k, a lifting of C in the sense of [
EGNO15,
9.16] is a split fusion category ˜C overR such that C is the mod m evaluation
of ˜C.
Theorem 2.4. [EGNO15, Theorem 9.16.1] If the global dimension of C is
non-zero, C admits a lifting to R and this lifting is unique up to equivalence.
Of particular interest is the situation where k is a perfect ﬁeld of prime
characteristicp. Then the ring of Witt vectors W (k) is a discrete valuation
ring with maximal ideal generated by p and W (k)/pW (k) ∼
= k. If C is a
non-degenerate (symmetric/braided) fusion category cate gory over k, then
it admits a (symmetric/braided) lifting to W (k) by [
ENO05, Theorem 9.3,
Corollary 9.4]. Since we are interested here in the construc tion of tensor
ideals, the semisimple case is not relevant to us.
8 THORSTEN HEIDERSDORF AND HANS WENZL
2.5.2. Algebraic groups. While we can deﬁne the mod m evaluation for any
monoidal category over the local ring R, it is often not the correct category
one is interested in. Consider the case of an algebraic group G over the local
ring R. Then extension of scalars of Rep(G,R ) deﬁnes a monoidal functor
Rep(G,R ) →Rep(G ⊗R/m,R/ m)
V ↦→V ⊗RR/m
Hom G(X,Y ) ↦→Hom G(X,Y ) ⊗R/m.
The image of Rep(G,R ) under this functor is the mod m evaluation, but it
is not the category Rep(G ⊗R/m,R/ m) (unless we are in the semisimple
case). Indeed the canonical functor
Hom G(M,N ) ⊗R/m →Hom GR/ m(M ⊗R/m,N ⊗R/m),
where GR/m is the algebraic group over k obtained by extension of scalars,
is in general not bijective [
J03, 10.14].
2.5.3. Deligne categories. For every ﬁeld k Deligne [ Del07] deﬁned symmet-
ric monoidal categories Rep(St), Rep(GLt) and Rep(Ot), t ∈ k, which in-
terpolate the representation categories of the symmetric g roup, the general
linear group and the orthogonal group. Each of this categori es is constructed
in the following way: One deﬁnes a skeletal subcategory corr esponding to
the tensor powers of the permutation representation V of Sn, the standard
representation V of O(n) or the tensor product V ⊗V ∨ of the standard
representation V of GL(n) and its dual. The object corresponding to such
a tensor power V ⊗r is denoted r in the Sn and O(n)-case and ( r,s ) in the
GL(n)-case. The endomorphism algebras of these objects are by de ﬁnition
(1) EndRep(St)(r) = kPr(t), the partition algebra for the parameter t.
(2) EndRep(Ot)(r) = kBr r(t), the Brauer algebra for the parameter t.
(3) EndRep(GLt)(r,s ) = kWB r,s(t), the walled Brauer algebra for the
parameter t.
To get the full category, we take the additive karoubian enve lope of the
skeletal subcategory. The categories Rep(St),Rep(GLt) and Rep(Ot) admit
a lift to the completion of the local ring of evaluable ration al functions
R =k[T ](T −t) [HW]. Indeed the construction described above makes sense
over R as well. This can be generalized to inlcude the q-deformations of
Rep(Ot) and Rep(GLt).
2.5.4. Tilting modules. Let Tilt denote the monoidal category of modu-
lar/quantized tilting modules. Then Tilt admits a lift to the category of
tilting modules over the ring of Witt vectors W (k) (where k is a perfect
ﬁeld of characteristic p > 0) respectively a lift to the category of tilting
modules over the completion of Q[v]v−q. For details we refer the reader to
sections 5, 6 and 7.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 9
2.6. New tensor ideals.
Lemma 2.5. The tensor ideals NI of CR deﬁne tensor ideals in the mod
m evaluation C. The thick ideals NI deﬁne thick ideals in the mod m evalu-
ation. The tensor ideal N1 corresponds to the ideal of negligible morphisms
in C and the thick ideal N1 corresponds to the indecomposable objects of
categorial dimension 0.
In particular we obtain a chain of tensor ideals
... ⊆ N 3 ⊆ N 2 ⊆ N
and likewise a chain of thick ideals
... ⊆N3 ⊆N2 ⊆N.
The numberk can often be seen as a measure for the vanishing of dim( X).
If X ∈ Nk with k minimal, we say that X has nullity k. For the explicit
meaning of this nullity we refer to the examples that appear l ater in the
article.
Question 2.6. The following question was raised by Kevin Coulembier
and Victor Ostrik: Can one ﬁnd a local ring R such that the NJ , where J
runs over the ideals of R, is a complete list of thick ideals in C? While we do
not know the answer, the existence of a lifting to a local ring seems delicate
in the non-semisimple case.
2.7. Compatibilities and k-semisimplicity. The following lemma fol-
lows immediately from the deﬁnition.
Lemma 2.7. Let C be the mod- m evaluation of CR over the local ring R.
The diagram
CR /d47/d47
/d15/d15
C
/d15/d15
CR/Nk /d47/d47C/Nk
commutes. In particular C/Nk is the mod m evaluation of CR/Nk.
Since Nk ⊂ N k+1 we obtain a chain of full and surjective tensor functors
... /d47/d47
/d15/d15
CR/N3 /d47/d47
/d15/d15
CR/N2 /d47/d47
/d15/d15
C/N
/d15/d15
... /d47/d47C/N3 /d47/d47C/N2 /d47/d47C/N.
If C is a tensor category so that C/N is semisimple, this loosely suggests
to interpret C/Nk as k-semisimple. This can be made more precise by con-
sidering the trace. Recall [ Del07, Proposition 5.7] that a tensor category is
semisimple if and only if the trace pairing Hom(X,Y ) ×Hom(Y,X ) → k
is non-degenerate, i.e. Tr (fg ) = 0 for all g : Y → X implies f = 0. For
a morphism f in C/Nk the deviation for the failure of the non-degeneracy
10 THORSTEN HEIDERSDORF AND HANS WENZL
condition can be seen as an element in I ≤k−1 by considering the lift of f in
CR/Nk.
2.8. A generalization. If a monoidal functor is full and surjective (on
objects), the images of the tensor ideals and thick ideals Nk are again tensor
ideals and thick ideals. Therefore we can more generally deﬁ nek-negligible
morphisms and objects provided we have a full and surjective monoidal
functor CR → C .
2.9. Monoidal supercategories. The notion of an I-negligible ideal and
the mod m evaluation can be deﬁned in the same way for monoidal su-
percategories as in [
BE17] [ Co18, A.1.2]. Examples of monoidal supercate-
gories are the odd Temperley-Lieb supercategory ST L (δ),δ ∈ k of [ BE17,
Example 1.17], the aﬃne VW supercategory s⋁ ⋁ [BD17] and the oriented
Brauer-Cliﬀord and degenerate aﬃne oriented Brauer-Cliﬀord supercate-
gories [ BCK17]. An ideal J in a supercategory is an ideal as in an ordinary
category with the extra assumption that J(X,Y ) is a graded subgroup of
Hom(X,Y ) for all X,Y ∈ C . The notion of a tensor ideal is otherwise
unchanged. Thick ideals can be deﬁned as for monoidal catego ries.
