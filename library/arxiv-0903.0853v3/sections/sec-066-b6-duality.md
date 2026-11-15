---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-066-b6-duality
section_title: "Duality"
section_number: B.6
pages: 147-149
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
---
cording to [11, §4.2], the canonical morphism:
ν : LK(V, V ′) ⊗K W →LK(V, V ′ ⊗K W)
is a monomorphism if W is projective and an isomorphism if V or W is pro-
jective of ﬁnite rank. One checks that the following diagram is commutative:
LK(V, V ′) ⊗K W

ν
/ LK(V, V ′ ⊗K W)

LK(V, V ′) ⊗K W
ν
/ LK(V, V ′ ⊗K W)
The left vertical map is given by: f ⊗w 7→(Φ′ ◦f ◦Φ−1) ⊗Ψ(w), while the
right vertical map is given by: g 7→(Φ′ ⊗Ψ) ◦g ◦Φ−1.
Proposition A.2.11. — For any three diﬀerence modules, ν induces a
canonical and functorial isomorphism of diﬀerence modules:
Hom(M, M′) ⊗N ≃Hom(M, M′ ⊗N).
Proof. — Immediate from the discussion above.
Deﬁnition A.2.12. — The dual of the diﬀerence module M is:
M∨:= Hom(M, 1).
If M = (V, Φ), then M∨= (V ∗, Φ∨), where Φ∨(u) := σ ◦u ◦Φ−1. For
instance, for A ∈GLn(K), one has (Kn, ΦA)∨= (Kn, A∨), where A∨:= tA−1
is the contragredient of A.
Corollary A.2.13. — We have a canonical and functorial isomorphism of
diﬀerence modules:
M∨⊗N ≃Hom(M, N).
Proof. — Set M′ := 1 in the proposition.
Remark A.2.14. — Part of these conclusions stay true for more general
DK,σ-modules. In the proposition, as well as in the corollary, the map is a
monomorphism if M is an arbitrary DK,σ-module and N is a K-projective
DK,σ-module; and an isomorphism if M or N is a diﬀerence module, the other
being an arbitrary DK,σ-module.
142
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
A.3. Finitely ﬁltered diﬀerence modules
A.3.1. Isograded classiﬁcation of diﬀerence modules. — Let (K, σ)
be a diﬀerence ring, with K is a commutative C-algebra and σ a C-algebra
automorphism.
Recall from the previous section that a diﬀerence module
over K is a left DK,σ-module which is projective of ﬁnite rank as a K-module
and that the category DiffMod(K, σ) of diﬀerence modules is abelian and
C-linear. Diﬀerence modules over K can be realized as pairs (E, Φ), where E
is a projective K-module of ﬁnite rank and Φ is a semi-linear automorphism
of E. In this description, a morphism of diﬀerence modules from (E, Φ) to
(F, Ψ) is a map u ∈LK(E, F) such that Ψ ◦u = u ◦Φ.
As an instance of the general problem considered in section A.1, we ﬁx
diﬀerence modules Pi (1 ≤i ≤k) and consider ﬁnitely ﬁltered diﬀerence
modules M with associated graded module P = P1 ⊕· · · ⊕Pk. We assume
that each such object M = (0 = M0 ⊂M1 ⊂· · · ⊂Mk = M) comes equipped
with an isomorphism u = (ui : Mi/Mi−1 ≃Pi)1≤i≤k from grM to P.
In accordance with the general problem described in section A.1, we
consider (M, u) and (M′, u′) to be equivalent if there exists a morphism
f : M →M′ that respects the ﬁltration: f(Mi) ⊂M′
i for 1 ≤i ≤k, and such
that, writing gi : Mi/Mi−1 →M′
i/M′
i−1 the morphisms thus induced by f|Mi,
one has ui = u′
i◦gi for 1 ≤i ≤k. Since f respects the ﬁltration, one can deﬁne
grf : grM →grM′ and the above condition is equivalent to u = grf ◦u′. It is a
standard fact (and easy to prove) that f is then automatically an isomorphism.
Our goal is to classify such pairs (M, u) up to this equivalence relation. The
equivalence classes clearly form a set, which we write F(P1, . . . , Pk). In this
section, we give some matricial descriptions, under additional assumptions.
A.3.2. Matricial description of diﬀerence modules. —
Here, we
assume that the K-module E is free of ﬁnite rank n. This assumption will
be maintained in A.3.3 and A.4.2, where we pursue the matricial description.
We then see that the diﬀerence module M = (E, Φ) is then isomorphic to
some (Kn, ΦA) (example A.2.2).
Indeed, choosing a basis B allows one to
identify E with Kn. It is then clear that Φ(B) is also a basis of E, whence
the existence of A ∈GLn(K) such that Φ(B) = BA−1. If x ∈E has the
coordinate column vector X ∈Kn in basis B, i.e. if x = BX, computing
Φ(x) = Φ(BX) = Φ(B)σ(X) = BA−1σ(X) shows that Φ(x) ∈E has the
