---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
1.1. Negligible morphisms. We are interested in the structure of tensor
ideals [ Co18] [ Ba05] [ BKN17] [ CH17] in a rigid spherical monoidal category
C over a ﬁeld k. Roughly speaking we have two notions of tensor ideals:
• tensor ideals , submodules I(X,Y ) ⊂ Hom C(X,Y ) (for any X,Y ∈
C) that are closed under composition and tensor products with mor-
phisms;
• thick (tensor) ideals , subsets of ob(C) which are closed under tensor
products with arbitrary objects of C and also closed under retracts.
Arguably the most important tensor ideal is the tensor ideal of negligible
morphisms
N (X,Y ) = {f :X →Y | Tr (f ◦g) = 0 ∀g :Y →X}.
By [AK02] it is the largest proper tensor ideal of C, and the only tensor ideal
such that the categorial quotient C/N can be semisimple. Its associated
thick ideal
N = {X ∈ C | X ∼
= 0 ∈ C/N }
consists of direct sums of indecomposable objects X whose categorial di-
mension dim(X) = 0 vanishes (the negligible objects).
2010 Mathematics Subject Classiﬁcation. 17B10, 17B37, 18D10, 19D23.
Key words and phrases. Tensor ideals, Monoidal categories, Quantum groups, Local
rings, Deligne categories, Tilting modules, Categorial di mensions, Modiﬁed traces, Weyl
groups, Kazhdan-Lusztig cells.
1
2 THORSTEN HEIDERSDORF AND HANS WENZL
1.2. Generalized negligible morphisms. It is the aim of this article to
present a generalization of the notion of negligible morphi sm which will
lead to a measure - the nullity - for the negligibility of an object X ∈ C .
While N and dim(X) can always be deﬁned under our assumptions on C,
the deﬁnition of the generalized negligible tensor ideals NI and the nullity
requires more restrictive conditions.
In order to deﬁne these tensor ideals, we consider a deformat ion or lift of
C to a monoidal category CR over a local ring R as follows. Let CR denote
a monoidal rigid spherical category whose Hom spaces are fre e R-modules
satisfying End(1) = R. For any ideal I of R we put
NI(X,Y ) = {f :X →Y |Tr X(g ◦f ) ∈I and Tr Y (f ◦g) ∈I ∀g :Y →X},
the tensor ideal I-negligible morphisms in CR. An object X ∈ C R is called
I-negligible if Tr X(a) ∈ I for all a ∈ End(X). For a ﬁxed ideal I we can
also say that f : X → Y is k-negligible with respect to I if Tr (f ◦g) is in
I k. We will only use this in the special situation where I = m, the maximal
ideal of R. We then obtain the k-negligible morphisms Nk := Nmk which
form a decreasing chain
N1 ⊃ N 2 ⊃ N 3 ⊃...
of tensor ideals in CR and likewise for the Nk.
In order to deﬁne these for the category C over k we suppose now that we
have a surjective and full tensor functor CR → C with k =R/m. A special
case of this is if C is the mod m evaluation of CR: here the objects of C are
the same as those of CR with
Hom C(X,Y ) = Hom CR(X,Y )/mHom CR(X,Y ) ∼
=Hom CR(X,Y ) ⊗RR/m.
When passing from CR to C, the images of the NI and NI deﬁne tensor
ideals and thick ideals in C respectively (possibly zero if we are not in the
special situation of the mod m evaluation) which we denote again by NI and
NI (or Nk and Nk). Note that N1 and N1 are mapped to N and N in C.
We call an indecomposable object of C k-negligible if X ∈Nk. Its nullity is
the smallest k such that X ∈Nk.
1.3. Examples. Given a monoidal category C the question is whether it
admits a lift to a monoidal category CR. Our main examples are the follow-
ing:
Theorem 1.1. The following categories can be obtained as mod m eval-
uations:
(1) The category of (quantum) tilting modules Tilt (Uq(g), Q(q)), where g
is a semisimple complex Lie algebra and q a nontrivial primitive ℓ-th
root of unity with ℓ odd,ℓ>h and not divible by 3 if g contains g2,
is the mod m evaluation of Tilt (Uv(g),R ) whereR is the completion
of Q[v](v−q), the polynomial ring localized at (v −q), i.e. all rational
functions over Q which are evaluable at v =q.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 3
(2) The category of (modular) tilting modules Tilt (G,k ), where G is a
semisimple simply connected algebraic group over a perfect ﬁeld k
of characteristic p > 0, is the mod m evaluation of Tilt (G,W (k))
whereW (k) is the ring of Witt vectors of k.
(3) The Deligne categories Rep(St), Rep(GLt) and Rep(Ot), t ∈ C,
are mod m evaluations from their analogs over the completion of
C[t](t−n).
The proof of theorem 1.1 1) and 2) is explained in sections 6 - 7. The
ﬁeld Q(q) can of course be replaced by C. Part 3) can be generalized to
incorporate the q-versionsRep(Uq(glt)) and Rep(Uq(ot)) [ HW]. In this case
however we deal with two parameter versions, e.g. the local r ing is the
completion of C[r,ξ ]r−ξn−1,ξ−q (using BMW notation) for the q-version ofOt.
Using 3) it is possible to deﬁne k-negligible ideals also for certain categories
of representations of supergroups. In this case the nullity is related to the
atypicality.
1.4. Modiﬁed dimensions and link invariants. In recent years there
has been a lot of interest in the construction of modiﬁed trac es and dimen-
sion functions [
GKPM11] [GKPM13] [GPMV13] [GPM18]. One of the main
motivations for the introduction of these modiﬁed trace and dimension func-
tions is the construction of knot invariants since the invar iant (in the sense
of Reshetikhin-Turaev) of an indecomposable object X with dim(X) = 0
vanishes. It is very diﬃcult to show that a given ideal has a no ntrivial
modiﬁed trace function. In many cases the only known thick id eal to admit
such a nontrivial modiﬁed trace is the ideal of projective ob jects in C, the
smallest nontrivial thick ideal. Moreover, in most cases th ese modiﬁed trace
functions are not explicitely given.
The situation changes if there is a surjective and full tenso r functor CR →
C. In this case we can often renormalize the usual trace in CR and consider
its image in C to get a modiﬁed trace function.
Theorem 1.2. Let R be a local domain (which is not a ﬁeld) whose
maximal ideal (p) is generated by the element p. Let CR be a rigid spherical
monoidal category whose Hom spaces are free R-modules. Let I be a thick
ideal all of whose objects are k-negligible (with respect to (p)), such as e.g.
the ideal Nk of all k-negligible objects. For X ∈I and a ∈End(X)
(1) Tr (k)
X (a) := 1
pk Tr X(a), dim(k)(X) := 1
pk dim(X),
deﬁne modiﬁed trace and dimension functions on I. The image of the mod-
iﬁed trace function under CR → C deﬁnes a modiﬁed trace function on the
image of I in C.
The proof of this theorem is essentially trivial. The whole d iﬃculty lies
in the construction of an appropriate lift of C to an analogous category over
4 THORSTEN HEIDERSDORF AND HANS WENZL
a local ring R. Since any proper thick ideal is contained in the ideal of
negligible objects, we obtain
Corollary 1.3. Under the assumptions of the theorem, every thick ideal
in C admits a modiﬁed trace function.
Since in each case in theorem
1.1 the maximal ideal is generated by a
single element, we obtain
Corollary 1.4. Each thick ideal of Tilt (Uq(g), Q(q)), Tilt (G,k ) and the
Deligne categories Rep(St), Rep(GLt) and Rep(Ot), t ∈ C, admits a non-
trivial modiﬁed trace function.
The most interesting example for this is the case of Tilt (Uq(g), C). The
classical way of Reshetikhin-Turaev to deﬁne link invarian ts colored by ob-
jects of Tilt (Uq(g), C) yields a trivial invariant L unless the objects are all in
the fundamental alcove. Due to our lifting theorem, we can di rectly deﬁne
a link invariant in the sense of Reshetikhin-Turaev over the local ring R,
the completion of C[v](v−q). This invariant can be normalized by 1
pk like the
dimension function and yields an R/(p) valued invariant for Tilt (Uq(g), C).
Theorem 1.5. (see theorem 4.1) Assume that the components of the link
have been colored with the objects X1,...,X m ∈ C R. Let k be the nullity of
X ⊗c1
1 ⊗X ⊗c2
2 ⊗ ... ⊗X ⊗cm
m . Then the value of the R/(p)-valued invariant
is equal to 1
k!
dk
dvk L(X1, ...,X m)(L)|v=q, which is valid for its evaluation on any
m-component link L.
1.5. Thick ideals for tilting modules. What does the nullity capture in
the tilting module case?
• In the modular case, the maximal ideal m of the complete discrete
valuation ring W (k) is generated by p. If a tilting module over
W (k) is in Nk, then in particular rank(T (λ)) ∈ (p)k. There are
however tilting modules over W (k) satisfyingpk|rankW (k)T (λ) while
T (λ) /∈ Nk. However, if T (λ) is irreducible, then T (λ) ∈ Nk if and
only if pk|rankW (k)T (λ).
• In the quantum case the maximal ideal is generated by ( v −q). The
dimension is an element in the subring Q[v](v−q); and the dimension
over Q(q) is obtained by evaluating this rational function at v =q.
As for the modular case, T (λ) ∈ Nk implies that the multiplicity
of (v −q)k in the numerator is at least k; and conversely if T (λ) is
irreducible.
In the modular and quantum case the thick ideals are sums of th ick ideals
attached to a right p-cell or a right cell in the aﬃne Weyl group W +
p (orW +
ℓ )
(see section 8.1) by results of [ AHR17] [ O97]. The combinatorics of these
cells is however very diﬃcult and not fully understood, espe cially in the
modular case [ Je17]. We construct thick ideals I(F ) associated to minimal
facets F and compute their nullities in Proposition 8.8. This suggests a
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 5
description of tensor ideals as a collection of positive con es associated to
certain facets.
For the quantum type An−1 every thick ideal is a sum of thick ideals
attached to Young diagrams λ of size n (which parametrize the two-sided
cells of the aﬃne Weyl group). We attach a standard facet F0(λ) to every
such Young diagram and prove:
Theorem 1.6. (see theorem 9.11 for details) The thick ideal I(λ) =
I(F0(λ)) generated by the tilting modules T (ν) for which ν +ρ ∈F0(λ) coin-
cides with the thick ideal constructed by Ostrik for the cell in the dominant
Weyl chamber corresponding to the two-sided cell labeled by the Young dia-
gram λT . In particular, the nullity of any generating module T (ν) of that
ideal is equal to the value of Lusztig’s a-function of that cell.
For the relation between Nk and the values of the a-function in all types
see remark 9.12. For type A we can also give the already alluded geometric
description of tensor ideals via positive cones associated to certain facets,
see Theorem 9.9 for details. This follows fairly easily from earlier work of
[Shi], where we have beneﬁtted from its description in [ Co08]. In particular,
we obtain an explicit description of the Nk. Moreover, this approach also
suggests a description of the ideal structure for the modula r case which is
done in section 9.7.
1.6. Structure of the article. In section 2 we introduce basic properties
of the generalized negligible ideals. Modiﬁed trace functi ons are studied in
section 3 and modiﬁed link invariants in section 4. Sections 6 - 7 deal with
the case of tilting modules. In section 9 we give a description of the thick
ideals in quantum type A. We end the article with some open questions in
section 10. A second article [ HW] will treat the case of Deligne categories.
A third article will deal with open questions about the thick ideals and the
Nk for modular and quantum tilting modules.
