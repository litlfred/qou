---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-014-72-finite-fields
section_title: "Finite fields"
section_number: 7.2
pages: 15-17
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
The third, which requires a complete rewrite of the argument, disproves the
sum-product conjecture in certain fields of formal Laurent series in characteristicp.
The bounds on|A+A|and|AA|obtained this way get worse as the characteristic
pgrows, but for small characteristics, the bounds are much stronger than those
obtained from the real version of the argument.
7.1.Thep-adics.We now explain thep-adic variant. If the fieldKin Lemma 4.1
has a prime lying overpthat is split, for example, ifpsplits completely inK, then
Kembeds intoQ p and thus the setA⊆O K constructed in Lemma 4.1 embeds
intoZ p. Thus, to prove the analogue of Theorem 1.1 inZ p, it suffices to prove the
following variant of Theorem 3.2.
Lemma 7.1.There exists an absolute constantC >0such that, for everyda
power of2, there exists a totally real number fieldKwith degreedin which the
primepsplits completely such that∆ K≤C d.
Proof.LetT={p,∞}andS={3,5,7,11,13,17,19,23}\{p}. LetG T
S (2) be the
Galois group of the maximal pro-2 extension ofQunramified outsideSand split
completely at all primes inT. IfG T
S (2) is infinite, then for everyda power of 2
there is a number fieldsKwith degreedwhich is totally real (since∞splits), in
whichpsplits completely, and is ramified only at primes inS, with Galois group
of order a power of 2. This is because an infinite pro-2-group has open subgroups
of index every power of 2 (because a finite 2-group has subgroups of index every
power of 2 up to its order).
An extension of fields is called tamely ramified at a primepif the order of the
inertia subgroup atpof the Galois group is coprime top. Since these fieldsKhave
Galois group of order a power of 2, the inertia subgroup has order a power of 2,
so because they are ramified only at odd primes, they are tamely ramified at each
ramified prime. It follows by [32, III, Theorem 2.6] that ∆ K≤( Q
q∈Sq)d≤C d
whereC= 3·5·7·11·13·17·19·23. So it only remains to check thatG T
S (2) is
infinite.
Letd(G T
S (2)) be the minimum number of generators andr(G T
S (2)) the minimum
number of relations in a presentation ofG T
S (2). We can check
d(GT
S (2))≥|S|−2
as follows. The quadratic fieldQ({ √q|q∈S}) is split at infinity, ramified only
at primes inSand possibly at 2, and has Galois group (Z/2) |S|. Forman odd
integer, the extensionQ 2(√m) depends only onmmod 8. It follows that
Q2({√q|q∈S}) =Q 2(1,
√
−1,
√
5,
√
−5) =Q 2(
√
−1,
√
5)
where we have chosen one representative from each congruence class mod 8. Since
Q2(
√
5) is unramified,Q 2(√−1,
√
5) has inertia group of order 2. Thus the inertia
group at 2 is a subgroup of order 2 of the Galois group. Taking the quotient by
this we get a field with Galois group (Z/2) |S|−1 that is ramified only at primes in
S. The Frobenius element atpis an element of this Galois group, and thus has
order 1 or 2. Taking the quotient by this element, we get a field with Galois group
16 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
(Z/2)|S|−2 or (Z/2)|S|−1 which in addition splits completely atp. Thus (Z/2) |S|−2
is a quotient ofG T
S (2) and hence
(7.1)d(G T
S (2))≥|S|−2≥5.
We have
(7.2)r(G T
S (2))≤d(G T
S (2)) + 1
by [33, Theorem 10.7.12], since, in the notation of [33],χ(G T
S (2)) = 1 +r(GT
S (2))−
d(GT
S (2)) and we haveθ= 0,Sdoes not intersectS p ={p},r= 1, andT\
S∞ ={p}has cardinality 1, so thatχ(G T
S (2))≤0 + 0 + 1 + 1 = 2 and hence
r(GT
S (2))−d(G T
S (2))≤1.
It follows from (7.1) and (7.2) that
r(GT
S (2))< d(GT
S (2))2
4
and hence by the Golod-Shafarevich theorem [17] in its refined form due to Gasch¨ utz
and Vinberg [41, 23],G T
S (2) is infinite, as desired.□
7.2.Finite fields.
Theorem 7.2.There exist constantsc>0andf <1such that for eachδ∈(0,1),
for each primepsufficiently large depending onδ, there existsA⊂F p withp fδ <
|A|<p δ andmax(|A+A|,|AA|)≤|A| 2−c.
Sum-product results in finite fields typically require both an upper bound and a
lower bound on the size ofA, so we have stated this result with an upper bound
and a lower bound.
It may be possible to prove a result with tighter control on|A|in terms ofp, by
choosingpafter constructing a fieldKand a subset ofO K, at the cost that this
result would hold for infinitely many primes instead of all primes.
The value ofcobtained from our argument is very small. It is slightly worse than
the explicit value ofcwe obtain for the main theorem, owing to the dependence
of this argument on Lemma 7.1. It may be possible to prove a similar result in
finite fields of large size and small characteristic, with a better exponent, using the
results of the next subsection and reducing modulo a prime of the function field
Fq(C). To make this interesting, one would have to check that the sets produced
this way are far from any subfield of the finite field, for example as in the finite
field sum-product estimate of Li and Roche-Newton [28].
Proof.We apply Lemma 7.1 for adto be chosen later to produce a number fieldK
of degreedin whichpsplits completely. We apply Lemma 4.1 to produceA⊂O K.
Since the primepsplits completely inK, we may choose a primepofO K lying
overp, with residue fieldF p, to obtain a surjectionO K→F p. We will consider the
image ofAinsideF p.
In the proof of Lemma 4.1, it is observed that everyα∈Ahas|σ(α)|≤2Xe Y
for allσ, and thus forα 1̸=α 2 inAwe have|σ(α 1−α 2)|≤4Xe Y and hence the
norm ofα 1−α 2, which is the product of its image under all embeddingsσ, is at
most (4XeY )d. Ifα 1 andα 2 have the same image inF p, thenα 1−α 2 must be
divisible bypand hence have a norm a multiple ofp.
It follows that for the mapO K→F p to be injective onA, it suffices to have
(4XeY )d <p.
THE SUM-PRODUCT CONJECTURE IS F ALSE FOR REAL NUMBERS 17
From Lemma 4.1,|A|≤(XY/c ′)d for an absolute constantc ′. Thus to have
|A|<p δ, it suffices to have (XY/c′)d <p δ. Letdbe the least power of 2 such that
(4XeY )d <pand (XY/c ′)d <p δ. Arguing as in the proof of Theorems 1.2 and 1.1,
we have max(|A+A|,|AA|)≤|A| 2−c. Sincepis sufficiently large,dis sufficiently
large to be used in this argument.
It remains to prove|A|>p
δ
f . To do this, we use Lemma 4.1 which gives
(7.3)|A|≥ (c′XY) d
Y∆ 3/2
K
≥ (c′XY) d
YC 3d/2
which, with parameters chosen as in the proof of Theorems 1.2 and 1.1, is expo-
nentially large ind. Sincedis the least power of 2 such that (4Xe Y )d < pand
(XY/c′)
d
δ <p, we have either (4Xe Y )2d≥por (XY/c ′)
2d
δ ≥p. Combining either
one of these with (7.3) gives a lower bound of a power ofp δ, as desired.□
