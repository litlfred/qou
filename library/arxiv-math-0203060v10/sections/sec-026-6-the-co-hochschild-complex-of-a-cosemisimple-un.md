---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-026-6-the-co-hochschild-complex-of-a-cosemisimple-un
section_title: "The co-Hochschild complex of a cosemisimple unimodular weak Hopf algebra and its subcomplex of invariants"
section_number: 6
pages: 24-25
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
Hopf algebra and its subcomplex of invariants
6.1. The deﬁnition. LetA be a weak Hopf algebra and let B ⊂A be a weak Hopf
subalgebra. We will deﬁne a complex C•(A,B ) that generalizes the subcomplex of
the co-Hochschild complex of a Hopf algebra consisting of invariants of the adjoint
action, cf. [S, Sch].
We set C0(A,B ) = At ∩Z(A), the algebra of endomorphisms of the trivial
A-module; and for all n ≥ 1, we set
(29) Cn(A,B ) := {f ∈A⊗n |f = Ad(1)f and Ad(h)f = Ad(εt(h))f, ∀h ∈B},
where Ad(h) denotes the adjoint action of h, i.e., Ad(h)f = ∆ n(h(1))f ∆ n(S(h(2)))
for all h ∈ B and f ∈ A⊗n. Here ∆ n : A → A⊗n is the iteration of the comulti-
plication (we set ∆ 1 = id). Note that A⊗n is a non-unital B-module with respect
to Ad. The conditions of (29) mean that A lies in A ⊗At · · · ⊗AtA (where A is an
At-bimodule via z1 ·h ·z2 =z1S(z2)h for h ∈A, z1,z 2, ∈At) viewed as a subspace
of A⊗n and that f commutes with ∆ n(h) for all h ∈A.
Let us deﬁne a linear map δn :Cn(A,B ) →A⊗(n+1) byδ0(f ) = f −S(f ) and
δn(f ) = Ad(1) {1 ⊗f +
n∑
i=1
(−1)i(idi−1 ⊗ ∆ ⊗ idn−i)(f ) + (−1)n+1f ⊗ 1}(30)
for n ≥ 1.
Lemma 6.1. For all n ≥ 0 we have Im (δn) ⊂Cn+1(A,B ) and δn+1 ◦δn = 0, i.e.,
the collection {Cn(A,B ), δn}n≥0 is a complex.
ON FUSION CATEGORIES 25
Proof. That δn(f ), f ∈ Cn(A,B ) is Ad(1) stable is a part of deﬁnition (30). For
all h ∈B we compute
Ad(h)δn(f ) =
= Ad( h)(1 ⊗f ) − Ad(h)(∆ ⊗ idn−1)f + · · ·
· · · + (−1)nAd(h)(idn−1 ⊗ ∆) f + (−1)n+1Ad(h)(f ⊗ 1)
= h(1)S(h(3)) ⊗ Ad(h(2))f − (∆ ⊗ idn−1)(Ad(h)f ) + · · ·
· · · + (−1)n(idn−1 ⊗ ∆)Ad( h)f + (−1)n+1∆ n(h(1))f ∆ n(S(h(3))) ⊗εt(h(2))
= 1 (1)εt(h) ⊗ Ad(1(2))f − (∆ ⊗ idn−1)(Ad(εt(h))f ) + · · ·
· · · + (−1)n(idn−1 ⊗ ∆)Ad( εt(h))f + (−1)n+1∆ n(1(1))Ad(εt(h))f ⊗ 1(2)
= Ad( εt(h))δn(f ),
where we used the identity (id ⊗εt)∆( x) = (1 ⊗x)∆(1) for all x ∈A. Therefore,
δn(f ) ∈Cn+1(A,B ). Thus, δn(Cn(A,B )) ⊂Cn+1(A,B ).
That δn+1 ◦δn = 0 can be checked in a direct standard way, by cancelling the
similar terms with opposite signs among ( n + 3)(n + 2) tensors in δn+1 ◦δn(f ). □
The n-th cohomology group of the pair A, Bis
(31) Hn(A, B) := Hn(C•(A,B )) = Ker(δn)/Im(δn−1), for n ≥ 0.
