---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-023-equivalence-relation-on-motivic-functions
section_title: "Equivalence relation on motivic functions"
section_number: null
pages: 73-75
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
We start with a motivation for this section. There are many ex amples of pairs
of constructible sets (or even varieties) X1,X 2 over a ﬁeld k such that their
classes [X1] and [X2] in Mot(Spec(k)) are diﬀerent (or at least not obviously
coincide), but X1 and X2 coincide in each realization described in Section
4.1 (i)-(vi) (e.g. when X1,X 2 are isogeneous abelian varieties). In particular
we will be interested in the case when Xl,l = 1, 2 are aﬃne quadrics given
by the equations ∑
1≤i≤nai,lx2
i = 1, such that they have equal determinants:∏
1≤i≤nai,1 =∏
1≤i≤nai,2∈ k×.
Here we propose a modiﬁcation of the notion of motivic functi on which
is a version of the Grothendieck’s approach to the theory of p ure motives
with numerical equivalence. Let us explain it in the case of X = Spec(k),
where k is a ﬁeld of characteristic zero (which we will assume throug hout
this section).
We start with the symmetric monoidal Q-linear category Meff (k). Its
objects are smooth projective varieties over k and
HomMef f(k)(Y1,Y 2) = Q⊗ Im(Z dimY2(Y1×Y2)→H 2 dimY2
DR (Y1×Y2)) ,
where Zn(X) denotes as usual the space of algebraic cycles in X of codi-
mension n, and we take the image of the natural map into the algebraic de
Rham cohomology. Then HomMef f(k)(Y1,Y 2) is a ﬁnite-dimensional Q-vector
space. Instead of de Rham cohomology we can use Betti cohomol ogy (for an
embedding k֒→C) or l-adic cohomology. Comparison theorems imply that
the image of the group of cycles in the cohomology does not dep end on a
cohomology theory.
Composition of morphisms is given by the usual composition o f correspon-
dences, and the tensor product is given by the Cartesian prod uct of varieties.
We extend the categoryMeff (k) by adding formally ﬁnite sums (then it be-
comes an additive category), and ﬁnally taking the Karoubia n envelope. The
K0-ring of the resulting category contains the element L = [P1
k]− [Spec(k)].
Adding formally the inverse L−1 we obtain the ring which we denote by
Motcoh(Spec(k)). It is an easy corollary of Bittner theorem (see [6]) that t he
natural map Mot(Spec(k))→ Motcoh(Spec(k)) which assigns to a smooth
projective variety its class in Motcoh(Spec(k)) is a homomorphism of rings.
The above considerations can be generalized to the case of mo tives over
constructible sets.
73
Deﬁnition 11 Let X be a constructible set over a ﬁeld k,char k = 0 . A
constructible family of smooth projective varieties over X is represented by a
pair consisting of a smooth projective morphism h : Y → X0 of schemes of
ﬁnite type over k and a constructible isomorphism j :X0
constr
≃ X. Two such
representations
h :Y→X0, j :X0
constr
≃ X, h ′ :Y′→X′
0, j′ :X′
0
constr
≃ X
are identiﬁed if we are given constructible isomorphisms f : Y
constr
≃ Y′,
g : X0
constr
≃ X′
0 such that h′◦f = g◦h, j′◦g = j, and for any point
x∈ X(k) the induced constructible isomorphism between smooth proj ective
varieties (j◦h)−1(x) and (j′◦h′)−1(x) is an isomorphism of schemes.
For a constructible family of smooth projective varieties o verX and a point
x∈ X there is a well-deﬁned smooth projective variety Yx over the residue
ﬁeld k(x) called the ﬁber over x. Moreover, one can deﬁne the notion of
constructible family of algebraic cycles of the ﬁxed dimens ion. We say that
such a family is homologically equivalent to zero if for any x∈X the corre-
sponding cycles in Yx map to zero in H•
DR(Yx). Also, having two constructible
families of smooth projective varieties over X one easily deﬁnes their product,
which is again a constructible family of smooth projective v arieties over X.
All that allows us to generalize our constructions from the c aseX =Spec(k)
to the general case. In this way we obtain the ring Motcoh(X) as well as the
natural homomorphism of rings Mot(X)→Motcoh(X).
Deﬁnition 12 We say that two elements of Mot(X) are (cohomologically)
equivalent if their images in Motcoh(X) coincide.
The set of equivalence classes (in fact the ring) will be deno ted byMot (X).
It is isomorphic to the image of Mot(X) in Motcoh(X). In particular, the
above-mentioned quadrics deﬁne the same element in Mot (Spec(k)).
Let now X be a constructible set over k, endowed with an action of an
aﬃne algebraic group G. We deﬁne an equivalence relation on MotG(X) in
the following way. First we choose an embedding֒→GL(N). We say that
f,g ∈MotG(X) are equivalent if their pull-backs to Mot((X×GL(N))/G)
have the same image in Mot (X× GL(N))/G). Using the fact that all
GL(N)-torsors over a constructible set are trivial it is easy to s how that
this equivalence relation does not depend on the embedding֒→GL(N).
74
The ring of equivalence classes is denoted by Mot
G
(X).16 Similarly one de-
ﬁnes the ring Mot
G×µ
(X), where µ = lim←−nµn. The exotic product descends
toMot
G×µ
(X). Hence we obtain the ring M
G,µ
(X) of equivalence classes as
well as homomorphism of rings MG,µ(X)→M
G,µ
(X).
