---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-008-stability-data
section_title: "Stability data"
section_number: null
pages: 20-22
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
Let us ﬁx a free abelian group Γ of ﬁnite rank, and a graded Lie a lgebra
g =⊕γ∈Γ gγ over Q.7
Deﬁnition 1 Stability data on g is a pair σ = (Z,a ) such that:
1) Z : Γ → R2≃ C is a homomorphism of abelian groups called the
central charge;
7In examples g is a R-linear Lie algebra, where R is a commutative unital Q-algebra.
20
2) a = (a(γ))γ∈Γ\{0} is a collection of elements a(γ)∈ gγ,
satisfying the following
Support Property :
Pick a norm ‖•‖on the vector space Γ R = Γ ⊗Z R. Then there exists
C >0 such that for any γ∈ Suppa (i.e. a(γ)⁄= 0) one has
‖γ‖≤C|Z(γ)| .
Obviously the Support Property does not depend on the choice of the
norm. We will denote the set of all stability data on g byStab(g). Later we
will equip this set with a Hausdorﬀ topology.
The Support Property is equivalent to the following conditi on (which we
will also call the Support Property):
There exists a quadratic form Q on Γ R such that
1) Q| Ker Z < 0;
2) Suppa⊂{γ∈ Γ \{ 0}| Q(γ) /greaterorequalslant0},
where we use the same notation Z for the natural extension of Z to Γ R.
Indeed, we may assume that the norm ‖•‖is the Euclidean norm in
a chosen basis and take Q(γ) = −‖γ‖2 +C1|Z(γ)|2 for suﬃciently large
positive constant C1. Generically Q has signature (2,n− 2), where n = rk Γ.
In degenerate cases Q can have signature (1 ,n− 1) or (0,n ).
For a given quadratic form Q on Γ R we denote by StabQ(g)⊂ Stab(g)
the set of stability data satisfying the above conditions 1) and 2). Obviously
Stab(g) =∪QStabQ(g), where the union is taken over all quadratic forms Q.
Remark 4 In the case of a 3-dimensional Calabi-Yau manifold X there
is a natural candidate for the quadratic form Q of the signature (2,n− 2)
needed to formulate the Support Property. Namely, identify ingH 3(X, R) with
H 3,0(X, C)⊕H 2,1(X, C) we can equip H 3(X, R) with the complex structure.
Furthermore, the natural symplectic form coming from the Ho dge structure
gives rise to a pseudo-hermitian form on H 3(X, R) of the signature (2,n−2),
wheren = dim RH 3(X, R). One can ask whether this form is positive on ev-
ery special Lagrangian submanifold of X. If this is true, then the Support
Property gives rise to a bound on the support of the function Ω discussed in
Section 1.4.
Support Property implies the following estimate for the num ber of points
in the Supp a with the central charge inside of the disc of radius R:
# (Z(Suppa)∩{z∈ C|| z|≤ R}) = O(Rn) ,
21
where R→∞ and n = rk Γ, Therefore the set Z(Suppa) is discrete in C
and does not contain zero.
Remark 5 It seem reasonable to consider “limiting cases” of stabilit y data
when the Support Property is not satisﬁed. Then the numbers ReZ and ImZ
are allowed to take values in arbitrary totally ordered ﬁeld s, e.g. R((t)) (here
t is a formal parameter such that t >0 and t < xfor any x∈ R>0). Some
of our considerations below make sense in this situation. In the framework
of stability conditions on triangulated categories such st ructures appeared in
[1], [73].
