---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-005-6-maps-with-small-arakelovzhang-pairing
section_title: "Maps with small Arakelov–Zhang pairing"
section_number: 6
pages: 11-15
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
toc_source: inferred
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Front matter; Introduction; Some algebraic lemmas"
---
We now describe how to extend the ideas used in the proof of Theorem 12 to treat polynomials which
are not necessarily K-conjugate to powering maps, but which are K ab-conjugate to some polynomial
φ(x) ∈K[x] that is arithmetically close to a powering map.
We ﬁrst recall the deﬁnitions of several arithmetic-dynamical objects associated to a polynomial
φ(x) ∈K[x] of degree d ≥2 deﬁned over a number ﬁeld K; see [Silverman 2007, Sections 3.4–3.5] for
further details. The Call–Silverman canonical height function ˆhφ : K →R may be deﬁned by the limit
ˆhφ(x) =
lim
n→+∞
h(φn(x))
dn
and can be characterized by the identity ˆhφ(φ(x)) = d ˆhφ(x) together with the fact that h −ˆhφ is bounded
on K. Locally, given a ﬁnite extension L/K, for each place v ∈ML deﬁne the canonical local height
1992
Jesse Andrews and Clayton Petsche
function by
λφ,v : Cv →R,
λφ,v(x) =
lim
n→+∞
1
dn log+|φn(x)|v.
(10)
Then an alternative expression for the canonical height is given by
ˆhφ(α) =
X
v∈ML
rvλφ,v(α),
(11)
for all α ∈L, a formula which may be viewed as analogous to (5).
For each place v ∈MK, standard arguments show that λφ,v(x) ≥0 for all x ∈Cv, with equality if and
only if x is in the ﬁlled Julia set
Fφ,v = {x ∈Cv | |φn(x)|v is bounded as n →+∞}
associated to φ. The canonical measure µφ,v associated to φ is a φ-invariant unit Borel measure supported
on Fφ,v which describes the limiting distribution of preperiodic points and iterated inverse images with
respect to φ. There are several equivalent constructions of this measure in the literature; see [Freire et al.
1983; Ljubich 1983] in the Archimedean case and [Baker and Rumely 2006; Chambert-Loir 2006; Favre
and Rivera-Letelier 2006] in the non-Archimedean case. (Technically, when v is a non-Archimedean
place, the objects λφ,v, Fφ,v, and µφ,v need to be interpreted on the Berkovich afﬁne line A1
v. We will
not need to go into these details in the present paper.)
Given two polynomials φ(x), ψ(x) ∈K[x] of degree at least two, the Arakelov–Zhang pairing can be
deﬁned by either of the two expressions
⟨φ, ψ⟩=
X
v∈MK
rv
Z
λφ,v dµψ,v =
X
v∈MK
rv
Z
λψ,v dµφ,v.
(12)
Thus ⟨φ, ψ⟩is a nonnegative real number, and in some sense it measures the global arithmetic-dynamical
distance between the two maps. This pairing was originally deﬁned as a limit of arithmetic intersection
products by Zhang [1995], and described analytically using Berkovich spaces by Petsche, Szpiro and
Tucker [Petsche et al. 2012]. For our purposes the most important fact about the Arakelov–Zhang pairing
is that it is closely related to points which have small canonical height with respect to one of the two
maps. In particular, it was shown in [Petsche et al. 2012] that if {αn} is a sequence of distinct points in K
with ˆhφ(αn) →0, then ˆhψ(αn) →⟨φ, ψ⟩.
In the special case ψ(x) = xd for d ≥2, the canonical height ˆhψ is the same as the usual Weil height
h, λψ,v(·) = log+|·|v, Fψ,v is the closed unit disc, and µψ,v is equal to the normalized Haar measure
supported on the unit circle of Cv = C when v is Archimedean, and equal to the Dirac measure supported
at the Gauss point of A1
v when v is non-Archimedean. In particular, the value of the pairing ⟨φ, xd⟩does
not depend on d.
Abelian extensions in dynamical Galois theory
1993
Theorem 14. Let φ(x) ∈K[x] be a polynomial of degree d ≥2 deﬁned over K such that ⟨φ, xd⟩> 0,
and let α be a nonexceptional point for φ. If K∞(φ, α) ⊆L ⊆K, then
B0(L) ≤⟨φ, xd⟩.
(13)
Proof. For each n ≥1, let αn ∈K∞⊆L satisfy φn(αn) = α; since α is not an exceptional point we
may assume that the αn are distinct. It follows from properties of the canonical height that ˆhφ(αn) =
ˆhφ(α)/dn →0 as n →+∞. By Theorem 1 of [Petsche et al. 2012], it follows that h(αn) →⟨φ, xd⟩> 0,
and (13) follows from the deﬁnition of B0(L).
□
As a sample application of Theorem 14, we can show that for any number ﬁeld K, a certain inﬁnite
family of polynomials satisﬁes the Conjecture.
Corollary 15. For each number ﬁeld K, there exists a constant CK such that Gal(K∞((x p−x)/p, α)/K)
is nonabelian over K for all α ∈K and all primes p ≥CK. In particular, Gal(K∞((x p −x)/p, α)/Q) is
nonabelian for all α ∈Q and all p ≥29.
Proof. It has been shown by Petsche and Stacy [2019] that ⟨(x p −x)/p, xd⟩= log p/(p −1). Thus if
K∞((x p −x)/p, α) ⊆K ab, Theorem 14 implies that B0(K ab) ≤log p/(p −1). But since B0(K ab) > 0
[Amoroso and Zannier 2000], we have a contradiction for large enough p. In particular, it was shown by
Amoroso and Dvornicich [2000] that B0(Qab) ≥(log 5)/12, which exceeds log p/(p−1) once p ≥29. □
We remark that, according to the Conjecture, we expect that Gal(K∞((x p −x)/p, α)/K) is nonabelian
for all number ﬁelds K, all α ∈K, and all primes p.
7. The map x2 −1
It is well known that there are exactly three Q-conjugacy classes of postcritically ﬁnite quadratic poly-
nomials over Q, represented by x2, x2 −1, and x2 −2. By Q-conjugacy it sufﬁces to check the family
φc(x) = x2 + c for c ∈Q, and the assumption that the critical point 0 is preperiodic (i.e., φm
c (0) = φn
c (0)
for m < n) forces c to be an algebraic integer (hence a rational integer) and also an element of the complex
Mandelbrot set M = {c ∈C | φn
c (0)̸ →∞}. It is elementary to check that M ∩Z = {−2, −1, 0}.
Since x2 and x2 −2 are a powering map and a Chebyshev map, respectively, they are treated by
Theorems 12 and 13, and the stable postcritically inﬁnite quadratic case is treated in Theorem 8. Thus in
order to complete the proof of Theorem 1, it sufﬁces to consider the polynomial φ(x) = x2 −1 over Q in
the stable case.
In order to show that K∞(x2 −1, α)/Q is never an abelian extension, one might hope to combine
the bound B0(Qab) ≥(log 5)/12 = 0.134 . . . of Amoroso and Dvornicich with Theorem 14, but it turns
out that the Arakelov–Zhang pairing ⟨x2 −1, x2⟩= 0.167 . . . is too large for this argument to apply
directly. However, we can recover this strategy (in the stable case) by showing that if K∞(x2 −1, α)
is an abelian extension of Q then it is contained in the subﬁeld Q(µ2∞) of Qab, which has Bogomolov
constant B0(Q(µ2∞)) ≥(log 2)/4 = 0.173 . . ., large enough to obtain a contradiction.
1994
Jesse Andrews and Clayton Petsche
Lemma 16. Let φ(x) = x2 −1, let α ∈K, and assume that the pair (φ, α) is stable over K and that
K∞= K∞(x2 −1, α) is an abelian extension of K. If p is a prime of K with residue characteristic not
equal to 2, then p is unramiﬁed in K∞.
Proof. The stability and abelian hypotheses imply via Lemma 2 that [Kn : K] = 2n for all n ≥1. Let
ψ(x) = φ(x + α) −α = x2 + 2αx + α2 −α −1. The critical point of ψ(x) is c = −α, which is part of a
2-cycle; that is, ψn(c) = −α for all even n, and ψn(c) = −1 −α for all odd n. Clearly
disc(φ(x) −α) = 4(1 + α)
and using Lemma 5 for n ≥2 we have
disc(φn(x) −α) = disc(φn(x + α) −α) = disc(ψn(x)) =
R2
n(−α)
if n ≥2 is even,
R2
n(−1 −α)
if n ≥3 is odd,
for some nonzero Rn ∈K.
Case 1: −1 −α is not a square in K. Then disc(φn(x) −α) is not a square for all odd n ≥3, and thus
viewing Gal(Kn/K) as a subgroup of S2n via its action on the roots of φn(x) −α, Gal(Kn/K) is not a
subgroup of A2n for all odd n ≥3. By Lemma 4, it follows that Gal(Kn/K) is cyclic for all odd n ≥3.
Then Gal(Kn/K) must be cyclic for all n, since Gal(Km/K) is a quotient of Gal(Kn/K) when 1 ≤m < n.
We conclude from Lemma 7 that no primes of K of odd residue characteristic ramify in K∞.
Case 2: −1−α = t2 for t ∈K. By the stability hypothesis we know that disc(φ(x)−α) = 4(1+α) = −4t2
is not a square in K, and thus we conclude that −1 is not a square in K and K1 = K(φ−1(α)) =
K(√4(1 + α)) = K(
√
−1). In particular, no primes of K with odd residue characteristic ramify in K1,
so it now sufﬁces to show that no primes of K1 with odd residue characteristic ramify in K∞.
Let φ−1(α) = {α′, α′′}. Thus for each n ≥1, we have a disjoint union
φ−n(α) = φ−(n−1)(α′) ⨿φ−(n−1)(α′′).
and it follows from the transitive action of Gal(Kn/K) on φ−n(α) that Gal(Kn/K1) acts transitively on
φ−(n−1)(α′). We conclude that (φ, α′) is a stable pair over K1. Arguing as above, it follows that 1 + α′ is
not a square in K1, and as −1 is a square in K1, we deduce that −1 −α′ is not a square in K1. We are
now in the setting of Case 1 for the pair (φ, α′) over K1, and we conclude that no primes of K1 with odd
residue characteristic ramify in K∞.
□
Theorem 17. Let φ(x) = x2 −1, let α ∈Q, and assume that the pair (φ, α) is stable. Then Gal(K∞/Q)
is nonabelian.
Proof. Assume on the contrary that K∞/Q is an abelian extension. By Lemma 16, no odd primes ramify
in K∞, and it follows from class ﬁeld theory that K∞⊆Q(µ2∞). As we will calculate in Section 8, we
have
⟨x2 −1, x2⟩= 0.167 . . . ,
(14)
Abelian extensions in dynamical Galois theory
1995
and we conclude from Theorem 14 that B0(Q(µ2∞)) ≤⟨x2 −1, x2⟩= 0.167 . . .. This is a contradiction
of the bound B0(Q(µ2∞)) ≥(log 2)/4 = 0.173 . . . proved in Theorem 10.
□
