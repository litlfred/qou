---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-003-4-short-geodesics-in-arithmetic-orbifolds
section_title: "Short geodesics in arithmetic orbifolds"
section_number: 4
pages: 9-15
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
The main results of this section are Theorem 4.6 and its Corollary, which set strong limits
on the possible lengths of short geodesics in arithmetic cusped hyperbolic orbifolds,
thus giving a necessary condition for arithmeticity.
We also describe a conjectural
statement of the same type for closed arithmetic orbifolds, dependent on the “Lehmer
Conjecture” of number theory. We ﬁrst recall some basic relevant facts about arithmeticity
of Kleinian groups, includingthe algebraic characterization of arithmeticity given in [MR]
and [R1, Chap. 2].
4.1.
Arithmetic Kleinian groups are obtained as follows (cf., [Bo] and [Vig, Chap. 4],
also [Vig] for relevant details on quaternion algebras).
Let k be a number ﬁeld with one complex place and A a quaternion algebra over
k ramiﬁed at all real archimedean places of k (this means A ⊗kR is the algebra of
hamiltonian quaternions for each real embedding k ,→R). Let O be an order of A
(a ﬁnitely generated subring of the set of A-integers, which contains the ring Rk of
k-integers and generates A as a k-vectorspace) and O1 the group of elements of norm 1
in O. The complex place k ,→C induces an embedding ρ: A ,→M2(C) which restricts
to ρ: O1 ,→SL2C. Then Pρ(O1) is a Kleinian group of ﬁnite covolume. An arithmetic
Kleinian group is one commensurable with a group of the type Pρ(O1). We say it is
derived from a quaternion algebra if it is actually a subgroup of some Pρ(O1). We call
M = H3/Γ arithmetic or derived from a quaternion algebra if Γ is arithmetic or derived
from a quaternion algebra.
The ﬁeld k and quaternion algebra A associated as above with an arithmetic Kleinian
group Γ are the same as the invariant trace ﬁeld k(Γ) and invariant quaternion algebra
A(Γ) of the previous section (see Theorem 4.3 below and subsequent remarks). The
arithmetic Kleinian group Γ has cusps if and only if A is M2(k), which holds if and
only if A is unramiﬁed at all places (see e.g., [Vig, Chap. 3]). We thus obtain (see also
[H]):
Proposition 4.1. A non-cocompact Kleinian group Γ of ﬁnite covolume is arithmetic if
and only if Γ is conjugate in PSL2C to a group commensurable with some “Bianchi
group” PSL2Od, where Od is the ring of integers in Q(
√
−d).
4.2.
We shall make use of the characterization theorems for arithmetic Kleinian groups
given in [MR] and [R1] in the special case of cusped orbifolds. We ﬁrst recall these
results in the general case.
Theorem 4.2. Let Γ be a Kleinian group of ﬁnite covolume. Then Γ is arithmetic if and
only if Γ(2) is derived from a quaternion algebra.
Theorem 4.3. With Γ as in Theorem 4.2, Γ is derived from a quaternion algebra if and
only if the following conditions hold:
(i)
k = Q(tr Γ) has just one complex place;
(ii) the set tr Γ consists of algebraic integers;
(iii) for every real place σ: k ,→R the set |σ(tr Γ)| is bounded.
Remarks. 1. The arguments of [R1] and [Tak] show that |σ(tr Γ)| bounded can be
replaced by |σ(tr Γ)| ≤2.
2.
It follows that when Γ is derived from a quaternion algebra, the associated quaternion
algebra is deﬁned over Q(tr Γ).
When Γ contains parabolic elements we may deduce from these theorems (see [H]
and [R1] for details):
Proposition 4.4. Let Γ be a non-cocompact Kleinian group of ﬁnite covolume. Then:
(a)
Γ is arithmetic if and only if k(Γ) = Q(
√
−d) for some square-free d ∈N and
tr Γ consists of algebraic integers.
(b)
Γ is derived from a quaternion algebra if and only if tr Γ ⊂Od for some d.
Corollary 4.5. If Γ is arithmetic and satisﬁes the condition of Corollary 2.3 (or, more
generally, Γ = Γ(2)P ), then Γ is derived from a quaternion algebra. In particular, this
holds if M = H3/Γ is a link complement in a Z/2-homology sphere.
4.3.
The main result of this section is the following theorem and its corollary.
Theorem 4.6. Let M 3 = H3/Γ be a cusped arithmetic hyperbolic orbifold. If M
contains a geodesic of length less than arccosh 3
2 = 0.9624236501. . . then Γ is com-
mensurable with PSL2Od with d ∈{1, 2, 3, 7, 11, 15, 19} and the geodesic has length
one-half a value listed in Table 1.
Moreover, if Γ is derived from a quaternion algebra, then the above can be improved
by a factor of 2: a geodesic of length less than 2 arccosh 3
2 = 1.9248473002. . . has
length listed in Table 1 and Γ is commensurable with a PSL2Od as above.
Table 1
length
d
0.8625546276620610
3
0.9624236501192069
1
1.0612750619050357
1
1.0870701449957391
3
1.2659486384018949
7
1.3169578969248167
2
1.4183161349689732
2
1.4657153519472905
1
1.4860221248769271
7
1.5343944365026389
11
1.5667992369724111
3
1.6628858910586211
3
1.7251092553241221
3
1.7365960799226493
11
1.7400216453048509
15
1.7627471740390861
1 or 2
1.8522660627003648
1
1.9079255392337773
19
Corollary 4.7. If the cusped hyperbolic 3-orbifold M = H3/Γ contains a geodesic of
length less than 0.431277313 (0.862554627 if Γ = Γ (2)P ) then M is non-arithmetic.
Remarks. 1.
Let O be any maximal order of M2(Q(
√
−d)).
Using the standard
description of types of maximal orders in M2(Q(
√
−d)) (see [Vig, p. 100, ex. 4.7]), it
follows that H3/PO1 always contains a geodesic of length 2 arccosh 3
2 , so Theorem 4.6
cannot be improved.
2.
The proof of Theorem 4.6 gives the same results for closed arithmetic 3-orbifolds
M = H3/Γ with invariant trace ﬁeld k(Γ) = Q(
√
−d).
Proof of Theorem 4.6. Since for any arithmetic Γ, Γ(2) is derived from a quaternion
algebra, we need only consider the case that Γ is derived from a quaternion algebra.
We ﬁrst introduce some notation. Let M 3 = H3/Γ have ﬁnite volume and let γ ∈Γ
be a loxodromic or hyperbolic element with tr γ = λ + λ−1 with |λ| > 1.
Notation. The length of the geodesic in M determined by γ is 2 log |λ| and will be
denoted by ℓ0(γ).
It is the real part of the “complex length" ℓ(γ) = 2 log λ whose
imaginary part is the holonomy of the geodesic determined by γ.
Note that, with γ as above, tr γ = ±2 cosh ℓ(γ)
2 , so
| tr γ| =

e
1
2 ℓ(γ) + e−1
2 ℓ(γ)

 ≤

e
1
2 ℓ(γ)

 +

e−1
2 ℓ(γ)

= e
1
2 ℓ0(γ) + e−1
2 ℓ0(γ)
= 2 cosh ℓ0(γ)
2
.
Hence, if | tr γ| ≥2,
ℓ0(γ) ≥2 arccosh | tr γ|
2
,
so that for γ with | tr γ| ≥3 we have ℓ0(γ) ≥2 arccosh 3
2 .
Now suppose Γ contains an element γ with ℓ0(γ) < 2 arccosh 3
2 . Then | tr γ| < 3.
But by Proposition 4.4 (a), tr γ ∈Od. Thus if tr γ where real, it would be in Z, and
γ would be parabolic or elliptic, contrary to assumption. The existence of a non-real
τ ∈Od with |τ| < 3 imposes strong conditions on d and τ, as we now describe.
If d̸ ≡−1 (mod 4) then τ = a + b
√
−d with a, b ∈Z and b̸ = 0.
Then
|τ|2 = a2 + db2, whence d < 9. If d ≡−1 (mod 4) then τ = (a + b
√
−d)/2 with
a ≡b (mod 2) and b̸ = 0.
In this case |τ|2 = (a2 + db2)/4, and it follows that
d < 35. We thus get a ﬁnite list of possible d and for each such d there is a short
ﬁnite list of τ ∈Od with |τ| < 3. It is thus a simple matter to list the d and τ with
Re(2 arccosh τ
2) < 2 arccosh 3
2 , giving Table 1.
4.4.
For closed hyperbolic 3-orbifolds we conjecture a similar result to Corollary 4.7:
Conjecture 4.8. There is a universal lower bound for the lengths of geodesics in closed
arithmetic hyperbolic orbifolds. (The current guess is approximately 0.09174218, or
twice this, 0.18348436, if the orbifold is derived from a quaternion algebra, see Sect. 4.5
below.)
This conjecture would be a consequence of a classical conjecture of number theory
due to D.H. Lehmer [Le] (see also [Boy] for a discussion). Suppose P(x) is a monic
integral polynomial of degree n with roots θ1, . . . , θn. The Mahler measure of P is
M(P) =
n
Y
i=1
max(1, |θi|).
Lehmer’s Conjecture. There exists m > 1 such that M(P) ≥m for all non-cyclotomic
P . The currently conjectured value of m is approximately 1.176780821 (see Sect. 4.5
below).
That Lehmer’s conjecture implies Conjecture 4.8 follows from the following lemma,
part of which is implicit in [R1] and [Tak].
Lemma 4.9. Let Γ be a Kleinian (or Fuchsian) group derived from a quaternion algebra.
Let γ ∈Γ be a loxodromic or hyperbolic element, and write tr γ = u+u−1 with |u| > 1.
Then u is an algebraic integer and u−1 is a conjugate of u. Moreover,
(a) if γ is loxodromic, then u is not real, and exactly four conjugates of u lie off the
unit circle;
(b) if γ is hyperbolic, then u is real, and exactly two conjugates of u lie off the unit
circle;
(c)
ℓ0(γ) = log M(P) or 2 log M(P) according as γ is loxodromic or hyperbolic,
where P = P(x) is the monic integral polynomial of u.
Proof. We prove the Kleinian case; the Fuchsian case is similar. Note that u + u−1 =
tr γ ∈k(Γ) = k. On the other hand, u is not in k: u ∈k implies that the quaternion
algebra is a matrix algebra, so k = Q(
√
−d) and u is a unit in this ﬁeld, which contradicts
the assumption |u| > 1. Thus u has degree 2 over k and u−1 is the other root of the
minimal polynomial u2 −u tr γ + 1 = 0.
For any real embedding σ: k ,→R, extend σ to ψ: k(u) →C.
We claim that
|ψ(u)| = 1. Indeed, if |ψ(u)|̸ = 1 then for sufﬁciently large positive integers t we
have |σ(tr γt)| = |ψ(ut + u−t)| > 2, which contradicts Theorem 4.3 and its following
Remark 1. Parts (a) and (b) of the Lemma now follow. Moreover, M(P) = |u|2 or |u|
according as u is complex or real, so part (c) also follows.
4.5.
Lemma 4.9 has a converse, as pointed out to us by Ted Chinburg:
Lemma 4.10. Suppose u is an algebraic integer such that |u| > 1, u−1 is a conjugate
of u, and u satisﬁes one of conditions (a) or (b) of Lemma 4.9. Then, in case (a) (resp.
case (b)) there is a Kleinian (resp. Fuchsian) group Γ derived from a quaternion algebra
and a loxodromic (resp. hyperbolic) element γ ∈Γ with tr γ = u + u−1. Moreover,
in case (b) we can require Γ to be a subgroup of a Kleinian group Γ0 derived from a
quaternion algebra.
Before we prove this converse, we describe its implications for short geodesics.
The conjectured smallest Mahler measure of approximately 1.176780821 is attained by
an example P1(x) = x10 + x9 −x7 −x6 −x5 −x4 −x3 + x + 1 due to Lehmer
[Le] given in 1933 (see [Boy] for a discussion). It has just one real root outside the
unit circle.
The smallest known Mahler measure for a polynomial with a complex
root outside the unit circle is approximately 1.2013961862, attained by an example
P2(x) = x18 + x17 + x16 −x13 −x11 −x9 −x7 −x5 + x2 + x + 1 of D. W. Boyd
[Boy]. Lemma 4.10 implies the existence of a hyperbolic 3-orbifold M1 containing
a hyperbolic 2-suborbifold N1 with a hyperbolic geodesic of length 2 log M(P1) ≈
0.324715228, and also a hyperbolic 3-orbifold M 2 with a loxodromic geodesic of
length log M(P2) ≈0.18348436; all these orbifolds being derived from quaternion
algebras. By Lemma 4.9, these are the conjectural shortest lengths for hyperbolic resp.
loxodromic geodesics in hyperbolic 2- or 3-orbifolds derived from quaternion algebras.
The conjectural shortest lengths in arithmetic orbifolds would be half these (approx.
0.162357614 resp. 0.09174218), and can also be realized in examples by the following
theorem of Chinburg (private communication), which we prove below.
Theorem 4.11. Suppose Γ is a Kleinian or Fuchsian group which is derived from a
quaternion algebra and γ ∈Γ is a loxodromic or hyperbolic element. Then there is a
group Γ0 commensurable with Γ containing an element γ0 with γ2
0 = γ in PSL2C.
Proof of Lemma 4.10. As in the proof of Lemma 4.9 we deal with the Kleinian group
case; the Fuchsian case is analogous. Thus assume that u is not real and has exactly
four conjugates off the unit circle. Since u−1 is assumed to be a conjugate of u, the
conjugates of u which are not on the unit circle are exactly u, u−1 and their complex
conjugates. Hence the only non-real conjugates of θ = u + u−1 are itself and u + u−1.
In particular the ﬁeld l0 = Q(θ) has exactly one complex place whilst the ﬁeld l = Q(u)
is totally imaginary as u has no real conjugates. Also note that l has degree 2 over l0.
We now construct a quaternion algebra over l0 in which l embeds.
Let S be the set of real places of l0 and ν a ﬁnite place of l0 which is inert in l.
Now deﬁne the set S1 to be S when |S| is even and S ∪{ν} otherwise. Since |S1|
is even, the classiﬁcation theorem for quaternion algebras over number ﬁelds (see for
example [Vig, Chapter 3]) guarantees the existence of a quaternion algebra A over l0
with S1 as ramiﬁcation set. Moreover, by construction, l embeds in A—since the real
places of l0 are ramiﬁed in l and ν is inert in l (see [Vig, Theorems 1.2.8 and 3.3.8]).
Thinking of l as a subﬁeld of A, u is an algebraic integer in l. Thus, to complete
the proof we need to ﬁnd an order of A containing u.
By assumption u−1 is the
distinct conjugate of u over l0. Hence u has l/l0-norm 1. Now A is a 2-dimensional
l-vector space, so let τ1, τ2 be a basis. Then Λ = Rlτ1 ⊕Rlτ2 is an ideal of A (see
[Vig, Chap. 1]), where Rl is the ring of integers of l, so OΛ = {x ∈A : xΛ ⊂Λ}
(the left order of Λ in the terminology of [Vig, Chap. 1]) is an order of A which clearly
contains Rl and hence u. The ﬁnal sentence of Lemma 4.10 follows from [MR] or
[R1].
Proof of Theorem 4.11 (Chinburg). We may assume Γ = Pρ(O1), where O is an order
in the quaternion algebra A = A(Γ) (cf. Sects. 4.1 and 3.1). Let γ = Pρ(u) for some
u ∈O1. Since γ is loxodromic or hyperbolic, tr γ = u + u−1, and we can assume
|u| > 1. As in the proof of Lemma 4.9, u has degree 2 over the center k of A. Since
u ∈O1, the k(u)/k-norm of u is 1. By Hilbert’s Theorem 90, there is a u0 ∈k(u) with
u0/σ(u0) = u, where σ is the non-trivial element of Gal(k(u)/k). By multiplying u0
by a suitable element of Rk (the ring of integers of k ), we may assume u0 ∈Rk(u). Now
σ(u2
0/u) = (σ(u0))2/σ(u) = (u0/u)2/u−1 = u2
0/u, so u2
0/u ∈k∗. It will now sufﬁce
to ﬁnd an arithmetic group Γ0 commensurable with Γ and containing γ0 = Pρ(u0),
since γ2
0 = γ in A∗/k∗.
As in the proof of Lemma 4.10, we can ﬁnd a maximal order O in A containing u0.
Let Rf be the (ﬁnite) set of ﬁnite places of k over which A ramiﬁes. Let S be a ﬁnite
set of places of k such that u0 is an S-unit. For ν /∈Rf ∪S and ν ﬁnite, u0 is in
the unit group of Oν = O ⊗Rk Rν, where Rν is the ring of integers of the completion
kν. Hence u0 ﬁxes the vertex Pν of the Bruhat-Tits building at ν which is ﬁxed by
O∗
ν. Suppose now that ν ∈S −Rf . Because u has reduced norm 1, u ﬁxes the vertex
Pν in the building at ν which is ﬁxed by O∗
ν, though u0 need not ﬁx Pν. However,
since u2
0 = u in A∗/k∗, the action of u0 on the building at ν exchanges the vertices Pν
and u0Pν. Since the building is a tree, u0 ﬁxes the mid-point Tν of the shortest path
between these vertices. (Note that Tν is either a vertex or a midpoint of an edge.) From
Borel’s description ([Bo, Prop. 4.4]) of the maximal elements in the commensurability
class of Γ, there is a group Γ0 in this commensurability class consisting of precisely
those elements of A∗/k∗which locally ﬁx the same points as described above for u0 on
Bruhat-Tits buildings, i.e., they ﬁx Pν (resp. Tν ) if ν is a ﬁnite place not in Rf ∪S
(resp. in S −Rf ).
