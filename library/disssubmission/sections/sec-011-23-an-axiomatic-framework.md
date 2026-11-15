---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-011-23-an-axiomatic-framework
section_title: "An axiomatic framework"
section_number: 2.3
pages: 38-40
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
Since the Tannakian constructions to be given below are of independent
interest also in more general situations than in the proof of theorem 1.1, for
the rest of this chapter we work in the following axiomatic setting. Consider
a Λ-linear rigid symmetric monoidal category (D,∗) whose unit object 1
satisﬁes EndD(1) ∼= Λ, and let
rat : (D,∗) −→(Db
c (X,Λ),∗)
be a faithful Λ-linear tensor functor ACU. The notation rat is motivated by
the case where k = C, Λ = Q and where D = Db(MHM(X)) is the bounded
derived category of the category MHM(X) of mixed Hodge modules [89],
but our formulation also applies to other situations.
For K ∈D we denote by H•(X,K) resp. by χ(K) the hypercohomology
resp. the Euler characteristic of the sheaf complex rat(K). Similarly we use
the notation H•(X,Kχ) = H•(X,rat(K)χ) for twists by characters χ. Notice
however that we do not assume the twisting functor lifts to the category D,
so the formal token Kχ does not refer to an object in D. Depending on the
context, we require the ﬁrst four or all of the following axioms.
(D1) Degree shifts. We have an auto-equivalence K 7→K[1] on D which
induces the usual shift functor on Db
c (X,Λ).
(D2) Perverse truncations. For n ∈Z we have endofunctors pτ≤n, pτ≥n
on D and natural morphisms
pτ≤n(K) −→K
and
K −→pτ≥n(K)
for
K ∈D
which induce on Db
c (X,Λ) the usual perverse truncations.
2.3. An axiomatic framework
31
Furthermore, the essential image P of the perverse cohomology
functors
pHn = pτ≤n ◦pτ≥n :
D −→P
is a full abelian subcategory of D, and rat : P −→Perv(X,Λ) is an
exact functor between the respective abelian categories.
(D3) Perverse decomposition. For all K ∈D we have a (non-canonical)
isomorphism
K ∼=
M
n∈Z
pH−n(K)[n].
(D4) Semisimplicity. In (D2) the abelian category P is semisimple.
(D5) Hard Lefschetz. In D there exists an invertible object 1(1) whose
image in Perv(X,Λ) under rat is the Tate twist of 1. For all K,L
in D and all i ≥0 we have functorial Lefschetz isomorphisms
pH−i(K ∗L) ∼= pHi(K ∗L)(i),
where the Tate twist (i) means i-fold convolution with 1(1).
We do not assume D to be triangulated, indeed we will later deal with the
following non-triangulated categories.
EXAMPLE 2.3. The axioms (D1) – (D5) hold if D ⊆Db
c (X,Λ) is the
full subcategory of all direct sums of degree shifts of semisimple perverse
sheaves which in case char(k) > 0 are deﬁned over some ﬁnite ﬁeld.
For k = C this follows from [35] together with [14], [43], or alternatively
from [87] and [78]. On the other hand, for char(k) > 0 one can invoke the
mixedness results of [69] and [10]. Note that in the above example we could
also replace the category D by the full subcategory of objects of geometric
origin in the sense of [10, sect. 6.2.4].
EXAMPLE 2.4. The axioms (D1) – (D5) hold for k = C and Λ = Q if
one takes D to be the full subcategory of Db(MHM(X)) consisting of all
direct sums of degree shifts of semisimple Hodge modules.
In the above setting we consider a full subcategory N of D consisting
of objects that are negligible for our purposes. In our later application this
will be the category of objects which become isomorphic to zero in the
Andr´e-Kahn quotient category D. Again, since we want to proceed as far
as possible over a base ﬁeld of arbitrary characteristic, we formulate the
required properties as the following axioms.
(N1) Stability. We have N∗D ⊆N, and N is stable under taking retracts,
degree shifts, perverse truncations and adjoint duals.
32
Chapter 2 – Proof of the vanishing theorem(s)
(N2) Twisting. Every object K ∈N satisﬁes H•(X,Kχ) = 0 for most
characters χ of the fundamental group.
(N3) Acyclicity. The category N contains all K ∈D with H•(X,K) = 0.
(N4) Euler characteristics. The category N contains all simple objects
of P whose Euler characteristic vanishes.
The meaning of these axioms will become clear later on. For the time being
we content ourselves with the following
REMARK 2.5. Let Π be a set of characters of π1(X,0), and N ⊆D the
full subcategory of all K ∈D such that rat(K) is a direct sum of degree
shifts of local systems Lχ with χ ∈Π. Then axioms (N1) and (N2) hold.
Proof. For any M ∈Db
c (X,Λ) we have Lχ ∗M = Lχ ⊗Λ H•(X,Mχ−1)
by [106, p. 20], which in particular implies the stability property N∗D ⊆N
so that axiom (N1) holds. For (N2) use that H•(X,Lχ) = 0 if and only if the
character χ is non-trivial.
□
