---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-057-7-f-ormality-conjecture-for-general-manifolds
section_title: "F ormality conjecture for general manifolds"
section_number: 7
pages: 30-31
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
In this section we establish the formality conjecture for ge neral manifolds, not only for open domains in
Rd. It turns out that that essentially all work is already done. The only new analytic result is vanishing of
certain integrals over conﬁguration spaces, analogous to t he lemma from 6.6.
One can treat Rd
f ormal, the formal completion of vector space Rd at zero, in many respects as usual
manifold. In particular, we can deﬁne diﬀerential graded Li e algebras Dpoly(Rd
f ormal) and Tpoly(Rd
f ormal).
The Lie algebra Wd :=Vect (Rd
f ormal) is the standard Lie algebra of formal vector ﬁelds. We consi derWd as
a diﬀerential graded Lie algebra (with the trivial grading a nd the diﬀerential equal to 0). There are natural
homomorphisms of diﬀerential graded Lie algebras:
mT :Wd−→Tpoly(Rd
f ormal), m D :Wd−→Dpoly(Rd
f ormal),
because vector ﬁelds can be considered as polyvector ﬁelds a nd as diﬀerential operators.
We will use the following properties of the quasi-isomorphi smU from 6.4:
P1)U can be deﬁned for Rd
f ormal as well,
P2) for any ξ∈Wd we have the equality
U1(mT (ξ)) = mD(U1(ξ)),
P3)U is GL(d, R)-equivariant,
P4) for any k≥ 2, ξ1,...,ξ k∈Wd we have the equality
Uk(mT (ξ1)⊗... ⊗mT (ξk)) = 0
,
30
P5) for any k≥ 2, ξ∈gl(d, R)⊂Wd, and for any η2,...,η k∈Tpoly(Rd
f ormal) we have
Uk(mT (ξ)⊗η2⊗... ⊗ηk) = 0 .
We will construct quasi-isomorphisms from Tpoly(X) to Dpoly(X) for arbitrary d-dimensional manifold
X using only properties P1-P4 of the map U. Properties P1,P2 and P3 are evident, and the properties P4, P5
will be established later (subsections 7.3.1.1 and 7.3.3.1 ).
It will be convenient to use in this section the geometric lan guage of formal graded manifolds, instead of
the algebraic language of L∞-algebras. Let us ﬁx the dimension d∈ N. We introduce three formal graded
Q-manifolds without base points:
T,D,W .
These formal graded Q-manifolds are obtained in the usual way from diﬀerential gr aded Lie algebras
Tpoly(Rd
f ormal), Dpoly(Rd
f ormal) and Wd forgetting base points.
In next two subsections (7.1 and 7.2) we present two general g eometric constructions, which will used
in 7.3 for the proof of formality of Dpoly(X).
