---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-001-2-the-p-adiccomingchar-beilinson-conjecture-for
section_title: "The p-adiccomingchar Beilinson conjecture for totally real fields"
section_number: 2
pages: 4-9
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
Let k be a number ﬁeld with r1 real embeddings, 2r2 complex embeddings,
ring of algebraic integers Ok, and discriminant Dk.
As is well-known, O∗
k is a
ﬁnitely generated Abelian group of rank r = r1 + r2 −1, and its regulator R
satisﬁes w
p
|Dk| Ress=1ζk(s) = 2r1(2π)r2 |Cl(Ok)| R, with Cl(Ok) the class group
of Ok, and w the number of roots of unity in k. Because K0(Ok) ∼= Cl(Ok) ⊕Z
and K1(Ok) ∼= O∗
k, so |Cl(Ok)| = |K0(Ok)tor| and w = |K1(Ok)tor|, this can be
interpreted as a statement about the K-theory of Ok, and it is from this point
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER. FIELDS 5

of view that it can be generalized to ¢x(n) for n > 2. Namely, in [43], Quillen
proved that K,,(O,) is a finitely generated Abelian group for all m. Borel in
computed its rank when m > 2. For m even this rank is zero, but for odd m it is
ry +r or rg, and in he showed that a suitably defined regulator of Kn—1(Ox)
is related to ¢j,(n). Since Kon—1(Ox) > Kon-1(k) when n > 2 we can rephrase
his results for K2n—1(O,) in terms of 2, _1(k). Also, we replace Borel’s regulator
map regz : K2n-1(C) > R(n—1) (n > 2) with Beilinson’s regulator map reg, (see
(46) § 4]), which is half the Borel map regulator by Theorem 10.9]. Because
k @g C = @o:k-cC, and n > dim Spec(k ® C), we obtain by [46] p.9]

Hp (Spec(k @ C) x, R(n)) = H®(Spec(k @ C) x, R(n — 1))

(2.1) =(@ xn-0)",

o:k>C
which consists of those (x,)~ with xy = Z>. Finally, for any embedding o : k > C
we let 0. : Kon—1(k) 4 Kon—i(C) be the induced map.

Theorem 2.2. (Borel) Let k be a number field of degree d, with r real embeddings
and 2r2 complex embeddings, and let n > 2. Then the rank mp, of Kon—1(k) equals
ro if n is even andr, +r2 if n is odd. Moreover, the map

Kom—1(k) > EG Rn-1)
(2.3) ok 3c
ar (reg, 0 0%(Q))o

embeds K2n—1(k)/torsion as a lattice in (@,R(n — 1))+ & R™, and the volume
Vi(k) of a fundamental domain of this lattice satisfies

(2.4) Ce (n) [Del = ae) Va (he)

for some q in Q*.

Remark 2.5. In Theorem [2.2] m,, = 0 precisely when k is totally real and n > 2
is odd. In this case the given relation holds (with V,,(k) = 1) by the Siegel-Klingen
theorem [40] Chapter VII, Corollary 9.9].

This theorem is equivalent with Beilinson’s conjecture for k. In order to deal
with this in detail (see Remarks and and in order to introduce p-adic
L-functions we recall some facts about Artin L-functions [40] Chapter VII, § 10-12].
Let k be a number field, d = [k : Ql], and let x be a C-valued Artin character of
Gal(k/k). For a prime number ¢ we define

Eule(s, x, &) = [[Eu(s, xk)
te

where Eul;(s, x, k) is the reciprocal of the Euler factor for [ and the product is over
primes ( of & lying above ¢. Then for s € C with Re(s) > 1 we can write the Artin
L-function of x as

L(s,x,k) = [[Eul(s, x kot.
£
For an infinite place v of k we let
Le(sx when v is complex,

Ly (s,x,k) = {

Lr(s)"* De(s +1)" when v is real,
6 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XAVIER-FRANC¸OIS ROBLOT
where LR(s) = π−s/2Γ(s/2), LC(s) = 2(2π)−sΓ(s) and n± = d
2χ(1) ± P
v
1
2χ(Frw),
with the sum taken over the real places v of k and Frw the generator of the image
of Gal(C/R) in Gal(k/k) corresponding to any extension w : k →C of v. Then
Λ(s, χ, k) = L(s, χ, k)
Y
v|∞
Lv(s, χ, k)
extends to a meromorphic function, satisfying the functional equation (cf. [40, p.
541])
Λ(s, χ, k) = W(χ)C(χ, k)1/2C(χ, k)−sΛ(1 −s, χ, k)
with W(χ) a constant of absolute value 1 and C(χ, k) = |Dk|χ(1)Nmk/Q(f(χ, k)) for
f(χ, k) the Artin conductor of χ. Therefore
(2.6)
L(1 −s, χ, k) = W(χ)C(χ, k)s−1
2 (2(2π)−sΓ(s))dχ(1)
× (cos(πs/2))n+(sin(πs/2))n−L(s, χ, k) .
Following [28, pp. 80–81] we shall now describe a p-adic L-function Lp(s, χ, k)
when k is a totally real number ﬁeld, p a prime and χ : Gal(k/k) →Qp a suitable
Artin character. We begin with the case of 1-dimensional Artin characters.
If σ : Qp →C is any isomorphism then σ ◦χ is a complex Artin character, so
we have the Artin L-function L(s, σ ◦χ, k). We may also view χ as a character of
a suitable ray class group, so by [40, Corollary 9.9 and page 509] all L(m, σ ◦χ, k)
for m ∈Z≤0 are in Q(σ ◦χ) and the values
(2.7)
L∗(m, χ, k) = σ−1(L(m, σ ◦χ, k))
are independent of the choice of σ.
In the same way, we deﬁne
(2.8)
Eul∗
ℓ(m, χ, k) = σ−1(Eulℓ(m, σ ◦χ, k)) ,
which is clearly independent of the choice of σ. To construct the p-adic L-function
one ﬁnds a p-adic analytic or meromorphic function on an open ball around 0 that
interpolates the values L∗(m, χ, k). For 1-dimensional χ with the ﬁxed ﬁeld kχ of
its kernel totally real this was achieved independently by Deligne and Ribet [22],
Barsky [1], and Cassou-Nogu`es [14, 15]. We shall sketch a proof of the following
theorem and Remark 2.13 below in Section 6. (When kχ is not totally real the
p-adic L-function is identically zero since the values interpolated are all zero by the
functional equation of the L-function.)
Theorem 2.9. For p prime, let B in Cp be the open ball with centre 0 and radius
qp−1/(p−1) where q = p if p > 2 and q = 4 if p = 2. If k is a totally real number
ﬁeld and χ : Gal(k/k) →Qp a 1-dimensional Artin character, then there exists a
unique Cp-valued function Lp(s, χ, k) on B satisfying the following properties:
(1) Lp(s, χ, k) is analytic if χ is non-trivial and meromorphic with at most a
simple pole at s = 1 if χ is trival;
(2) if m is a negative integer such that m ≡1 modulo ϕ(q) then
Lp(m, χ, k) = Eul∗
p(m, χ, k)L∗(m, χ, k) .
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS
7
If χ : Gal(k/k) →Qp is any Artin character then by Brauer’s induction theo-
rem [40, (10.3)] there exist 1-dimensional Artin characters χ1, . . . , χt on subgroups
G1, . . . , Gt of Gal(k/k) of ﬁnite index, and integers a1, . . . , at, such that
(2.10)
χ =
t
X
i=1
aiIndGal(k/k)
Gi
(χi) .
If kχ is totally real then we can assume that the same holds for the ﬁxed ﬁelds ki
of the Gi, and we deﬁne the p-adic L-function of χ by
(2.11)
Lp(s, χ, k) =
tY
i=1
Lp(s, χi, ki)ai ,
which is a meromorphic function on B (see Section 6). For any negative integer m ≡
1 modulo ϕ(q) the value Lp(m, χ, k) is deﬁned and equals Eul∗
p(m, χ, k)L∗(m, χ, k)
by well-known properties of Artin L-functions (see [40, Prop. 10.4(iv)]), showing
the function is independent of how we express χ as a sum of induced 1-dimensional
characters.
Remark 2.12. In [28], Greenberg proves that the Main Conjecture of Iwasawa
theory implies the p-adic Artin conjecture, that is, that the p-adic L-function of an
Artin character χ is analytic on the open ball B if it does not contain the trivial
character, and has at most a simple pole at s = 1 otherwise. It therefore follows
from the proof of the Main Conjecture by Mazur and Wiles [38] for p odd that
Lp(n, χ, k) for p̸ = 2 is deﬁned for all integers n̸ = 1. In particular, the values of
the p-adic L-functions in Conjecture 2.17 below exist by Theorem 2.9, and those in
Conjecture 3.18 exist when p̸ = 2 but have to be assumed to exist when p = 2.
Remark 2.13. Let Wp ⊂Z∗
p be the subgroup of (p −1)-th roots of unity if p is
odd and let W2 = {±1}. The Teichm¨uller character on Gal(k/k) is deﬁned as the
composition
(2.14)
ωp : Gal(k/k) →Gal(Q/Q) →Gal(Q(µq)/Q)
∼
→(Z/qZ)∗∼
→Wp ,
where the last map sends an element of (Z/qZ)∗to the unique element of Wp
to which it is congruent modulo q. For an Artin character χ : Gal(k/k) →Qp
and an integer l, χωl
p is also an Artin character. If m ≤0 satisﬁes l + m ≡1
modulo ϕ(q) and either χ is 1-dimensional or kχ is totally real then Lp(m, χωl
p, k) =
Eul∗
p(m, χ, k)L∗(m, χ, k).
The p-adic Beilinson conjecture is going to predict the special values of p-adic
L-functions in terms of a p-adic regulator. The required regulator is the syntomic
regulator [3, Theorem 7.5]. Let F be a complete discretely valued ﬁeld of charac-
teristic 0 with perfect residue ﬁeld of characteristic p and let X be a scheme that is
smooth and of ﬁnite type over the valuation ring OF . Then the above mentioned
paper associates to X its rigid syntomic cohomologies Hi
syn(X, n), as well as syn-
tomic regulators (i.e., Chern characters) regp : K2n−i(X) →Hi
syn(X, n). In this
work, unlike in [3], we shall need to change the base ﬁeld F. We therefore prefer
to denote the syntomic cohomology by Hi
syn(X/OF , n). For the formulation of the
conjecture the following basic fact is required.
Lemma 2.15. We have H1
syn(Spec(OF )/OF , n) ∼= F, for all n > 0 and conse-
quently we have a syntomic regulator regp : K2n−1(OF ) →F. Furthermore, the
8 AMNON BESSER, PAUL BUCKINGHAM, ROB DE JEU, AND XAVIER-FRANC¸OIS ROBLOT
map regp commutes in the obvious way with ﬁnite extensions of ﬁelds and with
automorphisms of such ﬁelds, provided that their residue ﬁelds are algebraic over
the prime ﬁeld.
Proof. The ﬁrst claim follows from part 3 of [3, Proposition 8.6]. For the second
claim we note that by part 4 of the same proposition we have in this case an
isomorphism between syntomic and modiﬁed syntomic cohomology (the latter only
exists under the additional assumption on the residue ﬁeld). The compatibility
with ﬁnite base changes now follows from the same result for modiﬁed syntomic
cohomology in [3, Proposition 8.8]. The same holds for automorphisms, although
not explicitly stated in the above reference, since the relevant base change results,
e.g., Proposition 8.6.4, hold for this type of base change as well.
□
As a consequence of the lemma we can also, by abuse of notation, deﬁne for any
complete discretely valued subﬁeld F ⊂Qp the regulator regp : K2n−1(OF ) →F.
In [5], two of the authors of the present work showed how one can sometimes
compute the map regp by using p-adic polylogarithms.
We now restrict our attention to a totally real number ﬁeld k with [k : Q] = d.
Our goal will be to formulate a conjecture that is the p-adic analogue of Theorem 2.2
for K2n−1(k) with n ≥2. Since this K-group is torsion when n is even but has
rank d when n is odd, we only consider odd n ≥2.
In preparation for the more general construction that will follow in Section 3 let
us ﬁrst reformulate Theorem 2.2 in this special case. Let a1, . . . , ad form a Z-basis
of Ok and let σ∞
1 , . . . , σ∞
d be the embeddings of k into C. Then we deﬁne D1/2,∞
k
=
det(σ∞
i (aj)), a real root of the discriminant of k. Similarly, if α1, . . . , αd form a
Z-basis of K2n−1(k)/torsion then we let Rn,∞(k) = det(reg∞◦σ∞
i∗(αj)).
Then
D1/2,∞
k
and Rn,∞(k) are well-deﬁned up to sign, and the relation in Theorem 2.2
in this case is equivalent with
(2.16)
ζk(n)D1/2,∞
k
= q(n, k)Rn,∞(k)
with q(n, k) in Q∗.
Now let F ⊂Qp be the topological closure of the Galois closure of k embedded
in Qp in any way. If σp
1, . . . , σp
d are the embeddings of k into F then D1/2,p
k
=
det(σp
i (aj)) is a root in F of the discriminant of k. For σ : k →F an embedding
we denote the induced map K2n−1(k) →K2n−1(F) by σ∗. Then we deﬁne a p-
adic regulator in F by Rn,p(k) = det(regp ◦σp
i∗(αj)). Both D1/2,p
k
and Rn,p(k) are
well-deﬁned up to sign.
Remark 2.13 suggests that the role of ζk(n) in a p-adic analogue of Theorem 2.2
should be played by Lp(n, ω1−n
p
, k)/Eulp(n, k) where ζk(s) = Q
l Eull(s, k)−1 for
Re(s) > 1, so we can hope that
Lp(n, ω1−n
p
, k)D1/2,p
k
= qp(n, k) Eulp(n, k)Rn,p(k)
for some qp(n, k) in Q∗.
More precisely, because Rn,∞(k)/D1/2,∞
k
and Rn,p(k)/D1/2,p
k
are invariant under
reordering the σ∞
i
or σp
i , and transform in the same way if we change the bases of
Ok and K2n−1(k)/torsion, we can make the following conjecture.
Conjecture 2.17. For k a totally real number ﬁeld, p prime, and n ≥2 odd, we
have, with notation as above:
ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS
9
(1) in F the equality
Lp(n, ω1−n
p
, k)D1/2,p
k
= qp(n, k) Eulp(n, k)Rn,p(k)
holds for some qp(n, k) in Q∗;
(2) in fact, qp(n, k) = q(n, k);
(3) Lp(n, ω1−n
p
, k) and Rn,p(k) are non-zero.
As mentioned in the introduction, this, and the corresponding parts of Con-
jecture 3.18 below, can be deduced (with some eﬀort) from a much more general
conjecture of Perrin-Riou [42, 4.2.2].
Remark 2.18. The conjecture is similar to the result that the residue of ζp(s, k) at
s = 1 is related to the Leopoldt regulator of O∗
k through exactly the same formula as
for the residue of ζ(s, k) and the Dirichlet regulator [18], with part(4) corresponding
to the Leopoldt conjecture. However, we have not tried to determine if Colmez’s
normalization of the sign for the regulator is the same as here, especially given the
sign error in the proof of Lemma 4.3 in loc. cit. (see Section 6).
Remark 2.19. We can use a basis of a subgroup of ﬁnite index of K2n−1(k)/torsion
in the deﬁnition of Rn,∞(k) and Rn,p(k), or even a Q-basis of K2n−1(k)Q, without
aﬀecting the rationality of q(n, k), qp(n, k) or their equality. Similarly we can replace
the Z-basis of Ok with a Q-basis of k in the deﬁnitions of D1/2,∞
k
and D1/2,p
k
.
Remark 2.20. As is well-known, for k and n as in Conjecture 2.17, by (2.6)
ζk(s) at s = 1 −n has a zero of order d and the ﬁrst non-zero coeﬃcient in its
Taylor expansion, ζ♯
k(1−n), equals (2πi)d(1−n)((n−1)!/2)dDn−1/2
k
ζk(n). If we take
D1/2,∞
k
= D1/2
k
in (2.16) then we obtain
ζ♯
k(1 −n) = ((n −1)!/2)dq(n, k)Dn−1
k
eRn,∞(k)
for Beilinson’s renormalized regulator eRn,∞(k) = (2πi)d(1−n)Rn,∞(k). In computer
calculations ((n −1)!/2)dq(n, k)Dn−1
k
often has only relatively small prime factors,
so the larger prime factors in q(n, k) correspond to D1−n
k
. This phenomenon also
occurs in the calculations for Conjecture 3.18 below (see Remark 7.8).
Remark 2.21. (1) The thought that Lp(n, ω1−n
p
, k) is non-zero for n ≥2 and odd
when k is a totally real Abelian extension of Q is mentioned by C. Soul´e in [50,
3.4].
(2) F. Calegari [13] (see also [8]) proved that, for p = 2 and 3, ζp(3), which in
those cases equals Lp(3, ω−2
p , Q), is irrational. (More results along these lines are
described in Remark 3.20(3).)
(3) Parts (1) and (2) of Conjecture 2.17 hold when k is a totally real Abelian
number ﬁeld, and in fact the corresponding parts of a much stronger conjecture
that we shall describe in Section 3 hold for cyclotomic ﬁelds (see Proposition 4.17).
(4) We numerically veriﬁed part (3) of Conjecture 2.17, and its more reﬁned
version Conjecture 3.18(4) below, in certain cases; see Remark 4.19 and Section 7.
