---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-005-4-springer-theory
section_title: "Springer Theory"
section_number: 4
pages: 6-7
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
We shall now apply the above construction with Go replaced by G ≈Go × Go. B will again denote the
ﬂag manifold of g, Bo that of Go, so that B = Bo × Bo. N = No × No is the nilpotent cone in g∗, No that
in g∗
o. We again set z1 = bo × bo and zw = w−1z1. For V we now take
N ∩k⊥= {(ν, −ν)|ν ∈No} ≈No.
Then B∗(V ) becomes
Z = {(b, b′; ν, −ν)|ν ∈b⊥∩b′⊥}
the conormal variety of the K-orbits on B. Our construction therefore gives a representation of W ≈
Wo × Wo on H∗(Z, Z).
We may identify No with the subset N ∩k⊥of N. For a subset V of No we write Z(V ) for B∗(V ).
When V is a closed subvariety of N, then H2n(Z(V )) is naturally a W-submodule of H2n(Z), by (2.9).
When V is only constuctible then H2n(Z(V )) is naturally a W-subquotient:
H2n(Z(V )) ≈H2n(Z( ¯V ))/H2n(Z(∂V ))
where ¯V is the closure of V and ∂V is the topological boundary of V.
The decomposition of No into Go-orbits O (equivalently: the decomposition of N∩k⊥into K-orbits)
leads to a ﬁltration of H2n(Z) according to the closure relations among the orbits :
O′ ⊂¯O implies H2n(Z( ¯O)) ⊂H2n(Z( ¯O′)).
The subquotients of this ﬁltration are
H2n(Z(O)) = H2n(Z( ¯O))/

O′<O
H2n(Z( ¯O′)).
Where O′ < O means ¯O′ ⊄
=
¯O. The associated graded group is
grH2n(Z) ≈⊕H2n(Z(O)),
(1)
sum over all Go-orbits on No. (1) is a W-decomposition; but one shoud keep in mind that the H2n(Z(O))
are naturally W-subquotients of H2n(Z ), not W-submodules. This in spite of the fact that H2n(Z(O))
REPRESENTATIONS OF WEYL GROUPS
7
may naturally be realized as a subgroup of H2n(Z): it has as a basis the fundamental cycles of the
components of Z(O) and is therefore isomorphic to the subgroup of H2n(Z) spanned by the fundamental
cycles of the closures in Z of these components. But the latter subgroup of H2n(Z) is generally not
W-stable. It should also be noted that according to Steinberg [1976] each Z(O) has uniform dimension
= dimZ = n, so its components are certain Zw’s. More precisely, the components of Z(O) are dense
parts of those ¯Zw for which O intersects the ﬁbre Zw ∩k⊥of Z →B over Zw densely. We denote them
Zw(O) := Z(O) ∩¯Zw.
From the ﬁbration Z(O) →O one gets that
H2n(Z(O)) ≈H2e(ν)(Bν)Ao(ν)
(2)
where ν ∈O, e(ν) = dimCBν = 2eo(ν),
eo(ν) = dimCBoν, and Ao(ν) is the component group of the sta-
bilizer of ν in Go, a quotient of the fundamental group of O. H2e(ν)(Bν)Ao(ν) denotes the Ao(ν)-invariants
in H2e(ν)(Bν).
The isomorphism (1) is explicitly seen as follows.
As just mentioned, H2n(Z(O)) has a basis
consisting of the fundamental cycles of those Zw of Z which make up Z(O). On such a Zw the ﬁbration
Z(O) →O restricts to a ﬁbration Zw(O) →O whose ﬁbre over ν is exactly an Ao(ν)-orbit of components
of Bν = Bo
ν × Bo
ν (according to Steinberg [1976]); and these Ao(ν)-orbits of components of Bν form a
basis of H4e(ν)(Bν)Ao(ν).
The action of the component group A(ν) = Ao(ν)×Ao(ν) of the G−stabilizer of ν on H2e(ν)(Bν) =
H2eo(ν)(Boν) ⊗H2eo(ν)(Boν) commutes with the action of W = Wo × Wo, as we know, and the invariants
of the diagonal Ao(ν) in Ao(ν) × Ao(ν) decompose as

φ
χν, ¯φ ⊗χν,φ
where φ runs over the irreducible characters of Ao(ν) which occur in H2eo(ν)(Boν) and χν,φ is the character
of Wo on the subspace of H2eo(ν)(Boν) which transforms according to φ. (A priori one might have to extend
scalars to C for this decomposition, but it follows from the known structure of the Ao(ν) that it suﬃces
to work over Q.) If one knew that
the representation of W = Wo × Wo on H2n(Z, C) is the
biregular representation on C[W/Wo] = C[Wo],
(3)
which is the main result of the Kazhdan-Lusztig [1980] paper, this argument (which they attribute to
Springer) would prove
4.1 Springer’s Theorem. The χν,φ, are exactly the irreducible characters of Wo.
In the present context the missing link (3) will be supplied by the Integral Formula, as we shall now show.
