---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-028-23-an-axiomatic-framework-31
section_title: "An axiomatic framework 31"
section_number: 2.3
pages: 39-40
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
Furthermore, the essential imageP of the perverse cohomology
functors
pHn = pτ≤n◦ pτ≥n : D−→P
is a full abelian subcategory ofD, andrat : P−→Perv(X,Λ) is an
exact functor between the respective abelian categories.
(D3) Perverse decomposition. For allK∈ D we have a (non-canonical)
isomorphism
K∼=
⨁
n∈Z
pH−n(K)[n].
(D4) Semisimplicity. In (D2) the abelian categoryP is semisimple.
(D5) Hard Lefschetz. In D there exists an invertible object1(1) whose
image in Perv(X,Λ) underrat is the Tate twist of1. For all K,L
in D and alli≥ 0 we have functorial Lefschetz isomorphisms
pH−i(K∗L)∼= pHi(K∗L)(i),
where the Tate twist(i) meansi-fold convolution with1(1).
We do not assumeD to be triangulated, indeed we will later deal with the
following non-triangulated categories.
EXAMPLE 2.3. The axioms (D1) – (D5) hold ifD⊆ Dbc (X,Λ) is the
full subcategory of all direct sums of degree shifts of semisimple perverse
sheaves which in case char(k) > 0 are deﬁned over some ﬁnite ﬁeld.
Fork =Cthis follows from [35] together with [14], [43], or alternatively
from [87] and [78]. On the other hand, forchar(k) > 0 one can invoke the
mixedness results of [69] and [10]. Note that in the above example we could
also replace the categoryD by the full subcategory of objects of geometric
origin in the sense of [10, sect. 6.2.4].
EXAMPLE 2.4. The axioms (D1) – (D5) hold for k= C and Λ = Q if
one takesD to be the full subcategory of Db(MHM(X)) consisting of all
direct sums of degree shifts of semisimple Hodge modules.
In the above setting we consider a full subcategoryN of D consisting
of objects that are negligible for our purposes. In our later application this
will be the category of objects which become isomorphic to zero in the
Andr´e-Kahn quotient categoryD. Again, since we want to proceed as far
as possible over a base ﬁeld of arbitrary characteristic, we formulate the
required properties as the following axioms.
(N1) Stability. We haveN∗D⊆N, andN is stable under taking retracts,
degree shifts, perverse truncations and adjoint duals.
32 Chapter 2 – Proof of the vanishing theorem(s)
(N2) Twisting. Every object K∈ N satisﬁes H•(X,Kχ) = 0 for most
charactersχ of the fundamental group.
(N3) Acyclicity. The categoryN contains allK∈ D withH•(X,K) =0.
(N4) Euler characteristics. The categoryN contains all simple objects
of P whose Euler characteristic vanishes.
The meaning of these axioms will become clear later on. For the time being
we content ourselves with the following
REMARK 2.5. Let Π be a set of characters ofπ1(X,0), andN⊆ D the
full subcategory of all K∈ D such that rat(K) is a direct sum of degree
shifts of local systems Lχ with χ∈ Π. Then axioms (N1) and (N2) hold.
Proof. For any M∈ Dbc (X,Λ) we haveLχ∗M = Lχ⊗Λ H•(X,Mχ−1)
by [106, p. 20], which in particular implies the stability propertyN∗D⊆ N
so that axiom (N1) holds. For (N2) use thatH•(X,Lχ) =0 if and only if the
characterχ is non-trivial. □
