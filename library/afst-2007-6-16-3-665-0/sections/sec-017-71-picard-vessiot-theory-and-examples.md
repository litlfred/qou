---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-017-71-picard-vessiot-theory-and-examples
section_title: "Picard-Vessiot theory and examples"
section_number: 7.1
pages: 49-53
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Consider a ﬁeld F provided with an automorphism φ of inﬁnite order.
The ﬁeld of constants C := {f ∈F| φ(f) = f} is supposed to be alge-
braically closed. A diﬀerence module M is a ﬁnite dimensional vector space
over F, provided with a bijective additive map Φ : M →M satisfying
Φ(fm) = φ(f)Φ(m). After choosing a basis of M over F, the equation
Φ(m) = m translates into a matrix diﬀerence equation y = Aφ(y) with
A ∈GLn(F).
A Picard-Vessiot ring PV for M (or y = Aφ(y)) is a commutative F-
algebra with unit element satisfying
1. An extension of φ as automorphism of PV is given.
2. PV has no φ-invariant ideals except {0} and PV .
3. There is a U ∈GLn(PV ) with U = Aφ(U).
4. PV is generated over F by the entries of U and U −1.
With the methods of [vdP-S 1,2] one shows the existence and unicity of
PV (up to φ-isomorphisms). One observes that PV is reduced and has in
– 712 –
Galois theory of q-diﬀerence equations
general zero divisors. The ﬁeld of constants of the total ring of fractions of
PV is again C.
The naive deﬁnition of the diﬀerence Galois group G of M is: G is the
‘abstract’ group of the F-automorphisms of PV commuting with φ. This
deﬁnition is insuﬃcient in positive characteristic. A more precise deﬁnition
is the following. One deﬁnes a covariant functor G from the category of the
ﬁnitely generated commutative C-algebras R to the category of groups by
G(R) is the group of the automorphisms of R⊗CPV which are R⊗CF-linear
and commute with the action of φ. It can be shown that G is represented
by an aﬃne group scheme of ﬁnite type over C. The diﬀerence Galois group
G is by deﬁnition this group scheme.
If the ﬁeld F has characteristic zero then G is a reduced linear alge-
braic group. In our case, where F has characteristic p > 0, the diﬀerence
Galois group need not be reduced. In the following examples we calculate
the Picard-Vessiot rings and their diﬀerence Galois groups for some typical
equations. For all examples we take F = K = C((z)) with C as before.
Since the examples are pure modules, one may replace K by K = C({z})
everywhere. For convenience, we calculate for modules M the ‘contravari-
ant solutions’, i.e., ker(Φ −1, Hom(M, PV )) , in stead of the ‘covariant
solutions’, i.e., ker(Φ −1, PV ⊗M) .
Example 1. — The extension K ⊂K(z1/p) is the Picard-Vessiot exten-
sion for the diﬀerence equation φ(y) = q1/py. Its diﬀerence Galois group is
the group µp,C. More generally, K(z1/n) is the Picard-Vessiot extension of
an equation φ(y) = qt/ny with (t, n) = 1 and its diﬀerence Galois group
is µn,C. We recall that µn,C = Spec(C[t]/(tn −1)), with co-multiplication
given by t →t ⊗t.
Example 2. — Equation φ(y) = cy with c ∈C∗. Suppose that for all
n ⩾1 the only solution of φ(y) = cny in K is y = 0, then the Picard-Vessiot
extension is K[Y, Y −1] with φ(Y ) = cY and the diﬀerence Galois group is
Gm,C.
Suppose that there exists a non zero y ∈K such that φ(y) = cay for some
a ⩾1. Then c has the form ζqt/n with ζ a primitive dth root of unity
and n ⩾1, (t, n) = 1. We consider the two equations φ(y) = qt/ny and
φ(y) = ζy separately. The ﬁrst equation is considered in example 1. The
second equation has Picard-Vessiot ring K[y] with equation yd = 1 and
φ(y) = ζy. This ring has obviously zero divisors (if d > 1). Its diﬀerence
Galois group is µd,C ∼= Z/Zd over C since d is not divisible by p. The Picard-
Vessiot extension for φ(y) = cy is a subring of K[z1/n][y]. The diﬀerence
Galois group is therefore a quotient of the group µn,C × Z/Zd.
– 713 –
Marius van der Put, Marc Reversat
Example 3. — Um = K ⊗V with dim V = m, Φ(1 ⊗v) = 1 ⊗U(v)
and U ∈GL(V ) the indecomposable unipotent operator. There exists an
element e ∈V such that e, (U −1)e, . . . , (U −1)m−1e is a basis of V . Hence
Um ∼= K[Φ, Φ−1]/ K[Φ, Φ−1]((Φ −1)m). Thus we have to ﬁnd the Picard-
Vessiot ring for the equation (φ −1)m(y) = 0.
(a) Suppose that 1 < m ⩽p. The diﬀerence ring A1 := K[ℓ], deﬁned
by ℓp −ℓ= 0 and φ(ℓ) = ℓ+ 1, has only trivial φ-invariant ideals. The
elements

ℓ
i

for i = 0, . . . , m −1 are C-linear independent solutions of
(φ −1)m(y) = 0. Since A1 is generated over K by ℓone ﬁnds that A1 is
the Picard-Vessiot extension for the equation (φ −1)m(y) = 0. Let R be a
C-algebra and σ a R⊗C automorphism of R ⊗C K[ℓ], which commute with
φ. Then σ is determined by σ(ℓ) and σ(ℓ) = ℓ+ a where a is any element
in R with ap = a. The diﬀerence Galois group is therefore the group Z/Zp
over C. In view of further equations we write ℓ= ℓ1.
(b) Suppose that p < m ⩽p2. The Picard-Vessiot ring for (φ −1)m(y)
= 0 is A2 := K[ℓ1, ℓ2], deﬁned by ℓp
1 −ℓ1 = 0, ℓp
2 −ℓ2 = 0, φ(ℓ1) =
ℓ1 + 1, φ(ℓ2) = ℓ2 +

 ℓ1
p−1

. The set of maximal ideals of A2 is {(ℓ1 −a,
ℓ2−b)|a, b ∈Fp} ∼= F2
p. One calculates that φ acts transitively on this set and
one concludes that A2 has only trivial φ-invariant ideals. One observes that
(φ−1)p(ℓ2) = (φ−1)p−1(
 ℓ1
p −1

) = 1 and (φ−1)p2−1
 ℓ2
p −1
 ℓ1
p −1

= 1 .
The conclusion is that C[ℓ1, ℓ2] is the kernel of (φ−1)p2, acting on A2. This
shows that A2 is generated by the solutions of (φ −1)my = 0 and thus that
A2 is indeed the Picard-Vessiot ring.
We have to represent the functor G, given by G(R) is the group of the dif-
ference automorphism of R⊗C A2 over R⊗C K. For the calculation of G(R)
we suppose for convenience that Spec(R) is connected. Then a ∈R, ap = a
implies a ∈Fp. Further Fp[ℓ1, ℓ2] = {ξ ∈R ⊗C A2| ξp = ξ and (φ −1)p2ξ =
0}. Thus any σ ∈G(R) induces an automorphism of Fp[ℓ1, ℓ2] commuting
with φ. On the other hand, any automorphism of Fp[ℓ1, ℓ2] commuting with
φ, extends uniquely to an element of G(R).
The algebra Fp[ℓ1, ℓ2] is seen as Fp[φ]-module. The element ξ =

 ℓ2
p−1

·

 ℓ1
p−1

is a generator and the module can be written as Fp[t]/(tp2), where
t = φ −1. We recall that tp2−1ξ = 1. Thus an automorphism σ satisﬁes
σξ = aξ with a ∈Fp[t]/(tp2) and a ≡1 mod (t). On the other hand any a,
as above, produces a unique automorphism. The above group is the cyclic
group of order p2, generated by a = 1 + t mod (tp2). Thus the diﬀerence
Galois group is equal to the group Z/Zp2 over C.
– 714 –
Galois theory of q-diﬀerence equations
(c) In a similar way one obtains that the diﬀerence ring Ak := K[ℓ1, · · · , ℓk],
given by the equations ℓp
i −ℓi = 0 for i = 1, . . . , k and
(φ −1)(ℓi) =
 ℓi−1
p −1
 ℓi−2
p −1

· · ·
 ℓ1
p −1

for i = 2, . . . , k and (φ−1)ℓ1 = 1, is the Picard-Vessiot ring for (φ−1)my = 0
for m such that pk−1 < m ⩽pk. Its diﬀerence Galois group is the group
Z/pkZ over C. As in the case k = 2, the diﬀerence Galois group is identiﬁed
with the group of the automorphisms of Z := Fp[ℓ1, . . . , ℓk] which commute
with φ. Now Z, as a Fp[φ] = Fp[t]-module (with t = φ −1), has ξ =

 ℓk
p−1

ℓk−1
p−1

· · ·

 ℓ1
p−1

as cyclic element, and is isomorphic to Fp[t]/(tpk). The
automorphisms are given by the elements a ∈Fp[t]/(tpk) with a ≡1 mod (t).
This group is cyclic of order pk and has generator a = 1 + t mod (tpk).
Example 4. — M = K(z1/n)e, Φe = zt/ne with n ⩾1, (t, n) = (p, n) = 1.
The corresponding scalar equation is φn(y) = qt(n−1)/2zty. By deﬁnition,
PV contains an invertible element α satisfying the equation. Any other
solution y has the form ˜yα with φn(˜y) = ˜y. Hence PV contains K[y1] with
yn
1 = 1 and φ(y1) = ζny1 where ζn is a primitive nth root of unity. The
invertible element u := φ(α)α−1 satisﬁes the equation φn(u) = qtu. All
solutions of the latter equation have the form zt/ny with φny = y. Thus y
is an invertible element of C[y1]. It follows that zt/n and z1/n are in PV .
After changing α we may suppose that u = zt/n. This leads to the assertion
that the Picard-Vessiot ring is K(z1/n)[y1, α, α−1] with the rules: yn
1 =
1, φ(y1) = ζny1 (with ζn a primitive nth root of unity); α transcendental
over K and φ(α) = zt/nα. The elements {yi
1α| i = 0, . . . , n −1} form a
C-basis of solutions. The inclusion K[z1/n][y1] ⊂K[z1/n][y1, α, α−1] induces
an exact sequence for the diﬀerence Galois group, namely
1 →Gm →G →µn × µn →1 .
The term µn × µn is the diﬀerence Galois group of the Picard-Vessiot ex-
tension K(z1/n)[y1] of the equation φn(y) = qy.
Example 5. One considers the diﬀerence module M = K(z1/p)e with Φe =
zt/pe (and 1 ⩽t < p), seen as diﬀerence module of dimension p over
K. A corresponding scalar equation is φp(y) = qt(n−1)/2zty. The method
of example 4 yields that the Picard-Vessiot extension for M is PV
=
K(z1/p)[ℓ1, α, α−1], satisfying the following rules: ℓp
1 −ℓ1 = 0 and φ(ℓ1) =
ℓ1 + 1, α is transcendental over
K and φ(α) = zt/pα. The inclusion
– 715 –
Marius van der Put, Marc Reversat
K(z1/p)[ℓ1] ⊂K(z1/p)[ℓ1, α, α−1], induces an exact for the diﬀerence Galois
group G
1 →Gm →G →Z/pZ × µp →1 .
The group Z/pZ × µp is the diﬀerence Galois group of the Picard-Vessiot
extension K(z1/p)[ℓ1] of the equation φp(y) = qy.
Example 6. — M = K(z1/pk)e with Φe = zt/pke and (t, p) = 1. A corre-
sponding scalar equation is φpk(y) = qt(pk−1)/2zty. The Picard-Vessiot ring
is K(z1/pk)[ℓ1, . . . , ℓk, α, α−1] with φ(α) = zt/pkα. The diﬀerence Galois
group admits an exact sequence
1 →Gm →G →Z/pkZ × µpk →1 .
