---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-005-14-classiﬁcation-of-pure-modules-over-k-and-k
section_title: "Classiﬁcation of pure modules over K and K"
section_number: 1.4
pages: 7-11
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Let F ⊂G be a ﬁnite extension of diﬀerence ﬁelds. Let M be a diﬀerence
module over G. Then Res(M) (the restriction of M to F) denotes M,
considered as a diﬀerence module over F. One observes that
dimF Res(M) = [G : F] · dimG M.
Put Kn = K(z1/n) for any integer n ⩾1. We apply the above restriction
to the extension K ⊂Kn in order to construct all irreducible modules over
K. Consider integers t, n with n ⩾1 and g.c.d.(t, n) = 1 and c ∈C∗with
|q|1/n < |c| ⩽1. Let E(czt/n) := Kne denote the diﬀerence module over Kn
given by Φ(e) = czt/ne. Put E := Res(E(czt/n)).
Proposition 1.3 (The irreducible modules over K). —
(1) E depends only on t, n, cn.
(2) E is irreducible of dimension n and has slope t/n. The algebra of the
K-linear endomorphisms of E, commuting with Φ, is C.
(3) For any irreducible diﬀerence module I there are unique t, n and cn with
n ⩾1, g.c.d.(t, n) = 1 and |q| < |cn| ⩽1, such that I ∼= Res(E(czt/n)).
Proof. — (1) and (2). E has basis e, Φe, · · · , Φn−1e over K and thus e
is a cyclic vector for E. The minimal monic polynomial L ∈K[Φ] with
Le = 0 is L = Φn −qt(n−1)/2cnzt. Thus E ∼= K[Φ, Φ−1]/ K[Φ, Φ−1]L and
depends only on t, n, cn. The operator L has slope t/n and degree n. If
L has a non trivial decomposition L1L2, then the Newton polygon of L is
the sum of the Newton polygons of L1 and L2. In particular the Newton
polygon of L contains (at least) three points with integral coordinates. Since
g.c.d.(t, n) = 1, this is not the case and hence L and E are irreducible. We
note that every non zero endomorphism ( K-linear and commuting with Φ)
of E is bijective. Since C is algebraically closed, this implies that the algebra
of the endomorphisms ( K-linear and commuting with Φ) of E is C.
(3) Let I be an irreducible diﬀerence module, then I is pure and has a
slope t/n with n ⩾1 and g.c.d.(t, n) = 1. Take a cyclic vector and let
L = Φd + a1Φd−1 + · · · + ad−1Φ + ad be its minimal polynomial (with
d = dim
K I). Then ord(ai)
i
⩾t/n for all i and ord(ad)
d
= t/n. It follows that
d is a multiple of n. Now L ∈K[Φ, Φ−1] ⊂Kn[Φ, Φ−1] = Kn[Ψ, Ψ−1] with
Ψ = Φzt/n.
Then L, as operator in Ψ, has slope 0. Hence L has a right hand factor of
degree 1 in Ψ (or in Φ). This means that we have a morphism of q-diﬀerence
modules over K
I = K[Φ, Φ−1]/ K[Φ, Φ−1]L →Kn[Φ, Φ−1]/ Kn[Φ, Φ−1](Φ −a) ,
– 670 –
Galois theory of q-diﬀerence equations
for a suitable a ∈Kn. This morphism is injective since I is irreducible.
Counting the dimensions over K, one ﬁnds that d = n and that the mor-
phism is bijective. The right hand side is a one-dimensional diﬀerence mod-
ule over Kn and hence is isomorphic to E(czt/n) for some c ∈C∗with
|q|1/n < |c| ⩽1 (compare [vdP-S1], p. 149-150).
We have to show that an isomorphism between E1 := Res(E(c1zλ1))
and E2 := Res(E(c2zλ2)) implies that λ1 = λ2 and cn
1 = cn
2. The ﬁrst
statement is obvious since λi is the slope of Ei. We write λ1 = λ2 = t/n with
n ⩾1, (t, n) = 1. Let F : E1 →E2 be an isomorphism. Then F is unique
up to multiplication by a scalar in C∗. Both modules have the structure
of a diﬀerence module over Kn. Consider the map z−1/n ◦F ◦z1/n. This
is also an isomorphism between the two diﬀerence modules over K. Hence
z−1/n ◦F ◦z1/n = cF for some c ∈C∗. Clearly cn = 1. We change the Kn
structure of the module E(c2zt/n) by applying a suitable automorphism of
Kn over K. Now E(c2zt/n) is changed into E(c3zt/n) with c3 = ζc2 for some
ζ with ζn = 1. Moreover, we have now z−1/n ◦F ◦z1/n = F. Thus E(c1zt/n)
and E(c3zt/n) are isomorphic as diﬀerence modules over Kn. This implies
c1 = c3 since |q|1/n < |c1|, |c3| ⩽1.
□
Remarks 1.4. — (1) We note that Proposition 1.3 extends to the case
where the ﬁeld C is replaced by any ﬁeld C (of characteristic 0, with q ∈C∗
not a root of unity and C not necessarily equal to its algebraic closure
C). This can be formulated as follows. One extends the action of φ on
K := C((z)) to the ﬁeld  C((z1/n!)) in the obvious way. This ﬁeld contains
the algebraic closure K of K. Take a non zero element α ∈K of degree m
over K and consider the diﬀerence module K(α)e given by Φ(e) = αe.
Then K(α)e, viewed as a diﬀerence module over K, has dimension m and
is irreducible. It depends only on the Galois orbit of α. Every irreducible
diﬀerence module over K is obtained in this way.
(2) Put Kn = K(z1/n). The diﬀerence module over K obtained by viewing
Kne with Φe = czt/ne as a diﬀerence module over K, will also be denoted
by Res(E(czt/n)).
Corollary 1.5. — Proposition 1.3 remains valid if K is replaced by K.
Proof. — From the slope ﬁltration it follows that an irreducible diﬀerence
module over K is pure of some slope t/n. Let Kn denote K(z1/n). The
factorization of L as element of Kn[Ψ, Ψ−1] is valid over Kn, because L is
in this context a regular singular diﬀerence operator.
□
– 671 –
Marius van der Put, Marc Reversat
Corollary 1.6 (Indecomposable modules). —
(1) Let M be an indecomposable diﬀerence module over K. Then there are
unique integers t, n, m and cn ∈C∗with n, m ⩾1, g.c.d.(t, n) = 1, |q| <
|cn| ⩽1 such that M is isomorphic with Res(E(czt/n)) ⊗
K Um.
(2) Let M be an indecomposable pure diﬀerence module over K, then there
are unique t, n, m, cn as above such that M ∼= Res(E(czt/n)) ⊗K Um.
Proof. — (1) If the diﬀerence module M over K is indecomposable, then
M is pure. The proof of (2) that we will produce can be copied verbatim to
complete the proof of (1).
(2) Let M/K be pure with slope t/n. We will concentrate on the non trivial
case where n > 1. We consider now Kn ⊗K M. This diﬀerence module over
Kn has an action of the generator σ of the Galois group of Kn/K deﬁned by
σz1/n = ζz1/n with ζ = e2πi/n. One writes Kn ⊗K M as Kne ⊗C V , where
the action of Φ is given by Φ(e ⊗v) = zt/ne ⊗Av and where A : V →V
is a C-linear map such that all its eigenvalues α satisfy |q|1/n < |α| ⩽1.
We note that this presentation of Kn ⊗K M is unique. Moreover, the subset
C[z1/n, z−1/n]e ⊗V consists of the elements f in Kn ⊗K M such that the
C-vector space generated by {(z−t/nΦ)mf| m ∈Z} has ﬁnite dimension.
The vector space e ⊗V consists of the elements f ∈Kn ⊗K M such that
there is a monic polynomial L ∈C[(z−t/nΦ)] with L(f) = 0 and all the roots
α of L satisfy |q|1/n < |α| ⩽1. Since σ commutes with Φ on Kn ⊗K M one
has that e⊗V is invariant under σ. Hence we can write σ(e⊗v) = e⊗B(v),
where B : V →V is a linear map satisfying Bn = 1. The fact that σ and
Φ commute translates into BAB−1 = ζtA. This induces a decomposition
V = V0 ⊕V1 ⊕· · · ⊕Vn−1 into A-invariant subspaces with the property
B(Vi) = Vi+1 (where we use the cyclic notation Vn = V0).
The submodules of M are in bijection with the submodules of Kn ⊗M
that are invariant under σ. The latter are in bijection with the A-invariant
subspaces W0 of V0. This bijection associates to W0 the σ-invariant sub-
module Kne ⊗C (⊕n−1
i=0 BiW0). In particular, M is indecomposable if and
only if the action of A on V0 has only one Jordan block. Suppose that
A has this form and let c be the eigenvalue of A on V0, then one has
N ∼= Res(E(czt/n)) ⊗K Um with m = dim V0.
□
We note that there are indecomposable diﬀerence modules over K not
described in part (2) of Corollary 1.6.
Corollary 1.7. — Let M be a pure diﬀerence module over K with slope
t
n where g.c.d.(t, n) = 1 and n > 1. There exists a diﬀerence module N
– 672 –
Galois theory of q-diﬀerence equations
over Kn such that Res(N) ∼= M. The module N is not unique. A similar
statement holds for pure q-diﬀerence modules over K.
Definition 1.8. — Mglobal for a pure module M over K.
Suppose that the slope λ of the pure module M over K is an integer. Then
Kf ⊗K M, where Kf is the module deﬁned by Φf = z−λf, is pure of slope
0. It follows that M has a unique ﬁnite dimensional C-linear subspace W,
such that W is invariant under the operator z−λΦ and the restriction A ∈
GL(W) has the property that every eigenvalue c of A satisﬁes |q| < |c| ⩽1.
Moreover, the canonical K-linear map K ⊗W →M is a bijection.
For any C-linear operator L on M and any c ∈C, one writes Eigen(L, c)
for the generalized eigenspace of L for the eigenvalue c. In other words
Eigen(L, c) = 
s⩾1 ker((L −c)s, M). With this terminology one has that
W = ⊕c, |q|<|c|⩽1Eigen(z−λΦ, c) .
One deﬁnes Mglobal := C[z, z−1]⊗W = ⊕c∈C∗Eigen(z−λΦ, c). This is a free
C[z, z−1]-submodule of M, invariant under Φ and Φ−1. Thus Mglobal is a
global diﬀerence module. Further, the canonical map K ⊗C[z,z−1] Mglobal →
M is a bijection.
Now we consider a pure diﬀerence module M with slope λ = t/n, where
n ⩾1, (t, n) = 1. By Corollary 1.7, there exists a module N over Kn such
that M = Res(N). As above, N has a unique ﬁnite dimensional C-linear
subspace W invariant under z−λΦ, such that all eigenvalues c of the re-
striction A of z−λΦ to W satisfy |q|1/n < |c| ⩽1. One deﬁnes Mglobal :=
Nglobal = C[z1/n, z−1/n]⊗W. Thus Mglobal = ⊕c∈C∗Eigen(z−λΦ, c). As be-
fore, Mglobal is a global diﬀerence module and the canonical map K⊗C[z,z−1]
Mglobal →M is an isomorphism.
In order to see that the deﬁnition of Mglobal does not depend on the
choice of N one considers the operator (z−λΦ)n = qαz−tΦn, where α
is some rational number. It follows that Mglobal is also equal to ⊕c∈C∗
Eigen(z−tΦn, c). This expression is clearly independent of the choice of N.
Thus we can formulate the deﬁnition of Mglobal ⊂M for a pure module
over K of slope λ = t/n with n ⩾1, g.c.d.(t, n) = 1 by the statement:
The following properties of m ∈M are equivalent.
(1) m ∈Mglobal.
(2) The C-vector space generated by {(z−tΦn)sm |s ⩾0} has ﬁnite dimen-
sion.
(3) There exists a L ∈C[T], L̸ = 0 such that L(z−tΦn)(m) = 0.
– 673 –
Marius van der Put, Marc Reversat
The main technical diﬃculties in this paper arise from pure modules M
with non integer slope λ = t/n. There are two methods to handle these. The
ﬁrst one (Corollary 1.7) is to write M = Res(N) for some diﬀerence module
N over Kn. The second one, used in the proof of Corollary 1.6, replaces M
by Kn ⊗M provided with the action of the Galois group of Kn/K. Both
methods have their good and weak points. Now we develope the second
method in more detail. The main idea is to replace a pure diﬀerential module
N over K by M = K∞⊗K N with decent data D. Here K∞denotes the
algebraic closure of K. With this method one can more easily describe tensor
products of pure modules over K.
