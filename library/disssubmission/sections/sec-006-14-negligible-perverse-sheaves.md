---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-006-14-negligible-perverse-sheaves
section_title: "Negligible perverse sheaves"
section_number: 1.4
pages: 23-25
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
15
One easily checks that Supp(Mn) ⊆Xn, so Mn[−n] is a direct summand
of Rf∗C ¯Yn[d] by base change. To control the Hodge structure on twists of
the cohomology of this direct image, let π : ˜Y →Y be a composition of
blow-ups in smooth centers that gives rise to an embedded resolution of
singularities ˜Yn = π−1(Y n) →Y n, see [56] or [11, th. 10.7]. Then CY[d]
occurs as a direct summand of the complex Rπ∗C ˜Y[d] by the decomposition
theorem, so the restriction CY n[d] is a direct summand of Rπ∗C ˜Yn[d]. It then
follows that Mn[−n] is a direct summand of Rf∗Rπ∗C ˜Yn[d], and we get an
embedding
H0(X,(Mn)χ, ¯χ) ,→Hd+n(˜Yn,π∗f ∗(Lχ ⊕Lχ−1)).
But the Hodge types (p,q) on the right hand side satisfy p,q ≤dim(˜Yn) = dn
as one may check from the Hodge theory of compact K¨ahler manifolds with
coefﬁcients in unitary local systems.
□
The above result contains the generic vanishing theorem of Green and
Lazarsfeld [47, second part of th. 1] as the special case q = 0. Indeed, for
any p < dim(f(Y)) the number n = d −p is larger than the dimension of the
generic ﬁbre of the Albanese morphism, hence dn < d so that H p(Y,L ) = 0
for most L by theorem 1.5. If Y is algebraic, the theorem also holds more
generally for H p(Y,Ωq
Y(E ⊗C L )) with a unitary local system E on Y.
In general the bounds in the above theorem are strict: If d = 4 and if Y
is the blow-up of X along a smooth algebraic curve C ⊂X of genus ≥2,
then one has w(Y) = d1 = 3 but H2(Y,Ω1
Y(L ))̸ = 0 for all non-trivial line
bundles L as explained in [47, top of p. 402].
1.4. Negligible perverse sheaves
A crucial ingredient for the proof of our vanishing theorem to be given
in section 2.7 will be a classiﬁcation of all perverse sheaves on X of Euler
characteristic zero. To obtain this classiﬁcation we use an index formula for
D-modules, extending the arguments of [37, cor. 1.4] which have shown
that on a complex abelian variety X every perverse sheaf P ∈Perv(X,C)
has Euler characteristic χ(P) ≥0. As we mentioned earlier, this is the only
part of our proof of theorem 1.1 which so far only works over C.
PROPOSITION 1.6. Let P ∈Perv(X,C) be a simple perverse sheaf.
(a) One has χ(P) = 0 iff there exists an abelian subvariety A ,→X of
positive dimension with quotient morphism q : X ↠B = X/A such
that
P ∼= Lϕ ⊗q∗(Q)[dim(A)]
for some Q ∈Perv(B,C) and some character ϕ ∈Π(X).
(b) One has χ(P) = 1 iff P is a skyscraper sheaf on X of rank one.
16
Chapter 1 – Vanishing theorems on abelian varieties
Proof. Via the Riemann-Hilbert correspondence [57] we can consider P
as a D-module. For Z ⊆X closed and irreducible, let ΛZ ⊆T ∗X be the
closure in T ∗X of the conormal bundle in X to the smooth locus of Z. As in
loc. cit. we write the characteristic cycle of P as a ﬁnite formal sum
CC(P) = ∑
Z⊆X
nZ ·ΛZ
with
nZ ∈N0,
where Z runs through all closed irreducible subsets of X. From CC(P) the
support of P can be recovered via SuppP = S
nZ̸=0 Z. Furthermore, by the
microlocal index formula [44, th. 9.1] we have
χ(P) = ∑
Z⊆X
nZ ·dZ
with
dZ = [ΛX]·[ΛZ] ∈Z.
The intersection numbers dZ are well-deﬁned even though ΛZ is not proper
for Z̸ = X, see loc. cit. for details. Now if X is a simple abelian variety, then
lemma 1.8 below implies (a), and if we additionally assume dim(X) > 1,
also (b) follows in view of lemma 1.9 below. The non-simple case can be
reduced to the simple case, see [107].
□
The reduction to the case of simple abelian varieties in loc. cit. works for
ground ﬁelds k of characteristic p > 0 as well, but we do not know how to
deal with simple abelian varieties in that case. For k = C, Christian Schnell
has given in [94, cor. 3.11] a different proof of proposition 1.6(a) via the
Fourier-Mukai transform for D-modules.
COROLLARY 1.7. A simple perverse sheaf P ∈Perv(X,C) has Euler
characteristic zero iff H•(X,Pχ) = 0 for most characters χ.
Proof. “⇐” holds by corollary 2.2. For “⇒” take a positive-dimensional
abelian subvariety A ,→X with quotient q : X ↠B = X/A and a character ϕ
such that P ∼= Lϕ ⊗q∗(Q)[dim(A)] for some perverse sheaf Q on B as in
proposition 1.6(a). We can assume that the Euler characteristic of Q is not
zero. Then we claim that
H•(X,Pχ) = H•(B,Rq∗(Pχ)) = H•(B,Rq∗(Lϕχ)⊗Q[dim(A)])
vanishes iff the restriction of the local system Lϕχ to A = ker(q) ⊆X is
not trivial. Indeed, if this restriction is non-trivial, then by base change one
checks that Rq∗(Lϕχ) = 0 and hence a fortiori H•(X,Pχ) = 0. On the other
hand, if this restriction is trivial, then Lϕχ = q∗(Lψ) for some character ψ
and then H•(X,Pχ) = H•(A,C)⊗H•(B,Qψ)[dim(A)] is non-zero since the
Euler characteristic of Qψ is not zero.
□
For completeness we include the following two elementary lemmas
about characteristic cycles that have been used, in the case of simple abelian
varieties, in the proof of proposition 1.6.
