---
doc_id: arxiv-math-0610591v3
doc_title: "SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC"
section_id: sec-002-3-surjectivity-of
section_title: "Surjectivity of"
section_number: 3
pages: 7-16
source_pdf: arxiv-math-0610591v3.pdf
source_sha256: 187a84c35624b171
toc_source: outline
---
3. Surjectivity of Φ
It remains to establish the surjectivity of the induced map Φ in (1.3).
This surjectivity was ﬁrst established in positive characteristic in [3,
Theorem 4.1].5 We will outline an alternative proof here, following our
avowed strategy of showing that the dimensions of Φ(KSr), EndΓ(V ⊗r)
are independent of the characteristic of the inﬁnite ﬁeld K.
In order to establish the independence statement for Φ(KSr) we
apply results of Murphy and H¨arterich in order to compute the anni-
hilator of the action of Sr on V ⊗r. Note that Murphy and H¨arterich
worked with the Iwahori–Hecke algebra (with parameter q) in type A,
so one needs to take q = 1 in their formulas in order to get correspond-
ing results for the group algebra KSr. The results of Murphy and
H¨arterich hold over an arbitrary commutative integral domain, so K
does not need to be an inﬁnite ﬁeld in this part. So we assume from now
on, until the paragraph after Corollary 12, that K is a commutative
integral domain.
Let λ be a composition of r. We regard λ as an inﬁnite sequence
(λ1, λ2, . . . ) of nonnegative integers such that P λi = r. The individual
λi are the parts of λ, and the largest index ℓsuch that λℓ= 0 and
λj = 0 for all j > ℓis the length, or number of parts, of λ.
Any
composition λ may be sorted into a partition λ+, in which the parts
are non-strictly decreasing. When writing compositions or partitions,
trailing zero parts are usually omitted. If λ is a partition, we generally
write λ′ for the transposed (or conjugate) partition, corresponding to
writing the rows of the Young diagram as columns.
Given a composition λ = (λ1, . . ., λℓ) of r, a Young diagram of shape
λ is an arrangement of boxes into rows with λi boxes in the ith row. A
λ-tableau T is a numbering of the boxes in the Young diagram of shape
λ by the numbers 1, . . . , r so that each number appears just once. In
other words, it is a bijection between the boxes in the Young diagram
and the set {1, . . ., r}. Such a T is row standard if the numbers in each
row are increasing when read from left to right, and standard if row
standard and the numbers in each column are increasing when read
from top to bottom.
The group Sr acts naturally on tableaux, on the right, by permuting
the entries. Given a tableau T, we deﬁne the row stabilizer of T to
be the subgroup R(T) of Sr consisting of those permutations that
permute entries in each row of T amongst themselves, similarly the
5The statement of Theorem 4.1 in [3] is actually much more general.
8
STEPHEN DOTY
column stabilizer is the subgroup C(T) consisting of those permutations
that permute entries in each column of T amongst themselves.
Let λ be a composition of r. Let T λ be the λ-tableau in which the
numbers 1, . . ., r have been inserted in the boxes in order from left to
right along rows, read from top to bottom. Set Sλ = R(T λ). This is
the same as the Young subgroup
S{1,...,λ1} × S{λ1+1,...,λ1+λ2} × · · ·
of Sr deﬁned by the composition λ. Given a row standard λ-tableau T,
we deﬁne d(T) to be the unique element of Sr such that T = T λd(T).
Given any pair S, T of row standard λ-tableaux, following Murphy [19]
we set
(3.1)
xST = d(S)−1xλd(T);
yST = d(S)−1yλd(T).
where xλ = P
w∈Sλ w and yλ = P
w∈Sλ(sgn w) w.
Theorem 6 (Murphy). Let K be a commutative integral domain. Each
of the sets {xST} and {yST}, as (S, T) ranges over the set of all ordered
pairs of standard λ-tableaux for all partitions λ of r, is a K-basis of
the group algebra A = KSr.
Note that xST and yST are interchanged by the K-linear ring invo-
lution of KSr which sends w to (sgn w)w, for w ∈Sr. This gives a
trivial way of converting results about one basis into results about the
other.
We will need several equivalent descriptions of the permutation mod-
ules Mλ, which we now formulate. Let λ be a composition of r. Recall
that Mλ = 1 ⊗(KSλ) (KSr), where 1 is the one dimensional module K
with trivial action. In [13, Deﬁnition 4.1], an alternative combinatorial
description of Mλ is given in terms of “tabloids” (certain equivalence
classes of tableaux), and in [5, (1.3)] the authors write out an explicit
isomorphism between these two descriptions. The following gives two
additional descriptions of Mλ, the second of which was used already in
the previous section.
Lemma 7. For any composition λ of r, the permutation module Mλ
is isomorphic (as a right KSr-module) with either of
(a) the right ideal xλ(KSr) of KSr;
(b) the weight space (V ⊗r)λ in V ⊗r, where V is free over K of rank
at least as large as the number of parts of λ.
Proof. Let Dλ = {d(T)} as T varies over the set of row standard
tableaux of shape λ.
This is a set of right coset representatives of
SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC
9
Sλ in Sr. The map d →xλd gives the isomorphism (a), in light of
Lemma 3.2(i) of [5]. The isomorphism (b) works as follows. Given
d ∈Dλ, write d = d(T) for some (unique) row standard tableau T of
shape λ. Use T to construct a simple tensor vi1 ⊗· · · ⊗vir of weight
λ, by letting ij be the (unique) row number in T in which j is found.
This map is well deﬁned, and is a bijection since there is an obvious
inverse map.
□
We recall that compositions are partially ordered by dominance, de-
ﬁned as follows.
Given two compositions λ, µ of r, write λ ⊵µ (λ
dominates µ) if P
i⩽j λi ⩾P
i⩽j µi for all j.
One writes λ ⊲µ (λ
strictly dominates µ) if λ ⊵µ and the inequality P
i⩽j λi ⩾P
i⩽j µi is
strict for at least one j.
The dominance order on compositions extends to the set of row stan-
dard tableaux, as follows. Let T be a row standard λ-tableau, where
λ is a composition of r. For any s < r denote by T↓s the row stan-
dard tableau that results from throwing away all boxes of T containing
a number bigger than s. Let [T↓s] be the corresponding composition
of s (the composition deﬁning the shape of T↓s). Given row standard
tableaux S, T with the same number r of boxes, deﬁne
(3.2)
S ⊵T if for each s ⩽r, [S↓s] ⊵[T↓s];
S ⊲T if for each s ⩽r, [S↓s] ⊲[T↓s].
Note that if S, T are standard tableaux, respectively of shape λ, µ where
λ and µ are partitions of r, then S ⊵T if and only if T ′ ⊵S′. Here T ′
denotes the transposed tableau of T, obtained from T by writing its
rows as columns.
Let ∗be the K-linear anti-involution on A = KSr given by
(P
w∈Sr bww)∗→P
w∈Sr bww−1
for any bw ∈K. An easy calculation with the deﬁnitions shows that
(3.3)
x∗
ST = xTS;
y∗
ST = yTS
for any pair S, T of row standard λ-tableaux.
We write c ∈{x, y} in order to describe the cell structure of A =
KSr relative to both bases simultaneously.
Theorem 8 (Murphy, [19, Theorem 4.18]). Let c ∈{x, y}. Let λ be a
partition of r. The K-module A[⊵λ] = P KcST, the sum taken over
all pairs (S, T) of standard µ-tableaux such that µ ⊵λ, is a two-sided
ideal of A, as is A[⊲λ] = P KcST, the sum taken over all pairs (S, T)
10
STEPHEN DOTY
of standard µ-tableaux such that µ ⊲λ. For any a ∈A and any pair
(S, T) of λ-tableaux, we have
(3.4)
cST a = P
U ra(T, U) cSU
mod A[⊲λ]
where ra(T, U) ∈K is independent of S, and in the sum U varies over
the set of standard λ-tableaux.
In the language of cellular algebras, introduced by Graham and
Lehrer [9], for c ∈{x, y} the basis {cST} is a cellular basis of A. Note
that by applying the anti-involution ∗to (3.4) we obtain by (3.3) the
equivalent condition
(3.5)
a∗cTS = P
U ra(T, U) cUS
mod A[⊲λ]
for any a ∈A and any pair (S, T) of λ-tableaux.
Now ﬁx n and r, and let P be the set of partitions λ of r such that
λ1 > n. Note that P is empty if n ⩾r. Set A[P] = P KyST, where the
sum is taken over the set of pairs (S, T) of standard tableaux of shape
λ, for all λ ∈P. It follows from (3.4), (3.5) that A[P] is a two-sided
ideal of A because P satisﬁes the property: λ ∈P, µ ⊵λ =⇒µ ∈P
for any partition µ of r. Note that A[P] is the zero ideal if n ⩾r.
Lemma 9. The kernel of Φ contains A[P].
Proof. If n ⩾r then P is empty and there is nothing to prove, so we
may assume that n < r.
We ﬁrst observe that yλ acts as zero on any simple tensor vi1 ⊗· · · ⊗
vir ∈V ⊗r, for any λ ∈P. This is because any such tensor has at most
n distinct tensor factors, and thus is annihilated by the alternating sum
α = P
w∈S{1,...,λ1}(sgn w)w. (Recall that λ1 > n.) The alternating sum
α is a factor of yλ, i.e., we have yλ = αβ for some β ∈KSr, so yλ acts
as zero as well. Since V ⊗r is spanned by such simple tensors, it follows
that yλ acts as zero on V ⊗r.
It follows immediately that every yST = d(S)−1yλd(T), for λ ∈P,
acts as zero on V ⊗r, for any λ-tableaux S, T, since d(S)−1 simply per-
mutes the entries in the tensor, and then yλ annihilates it. Since A[P]
is spanned by such yST, it follows that A[P] is contained in the kernel
of Φ.
□
We will use a lemma of Murphy to establish the opposite inclusion.
Let (S, T) be a pair of λ-tableaux, where λ is a composition of r. The
pair is row standard if both S, T are row standard; similarly the pair is
standard if both S, T are standard. The dominance order on tableaux
SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC
11
deﬁned in (3.2) extends naturally to pairs of tableaux, by deﬁning:
(3.6)
(S, T) ⊵(U, V ) if S ⊵U and T ⊵V.
For a, b ∈A let (a, b) denote the coeﬃcient of 1 in the expression
ab∗= P
w∈Sr cw w, where cw ∈K. Then ( , ) is a non-degenerate
symmetric bilinear form on A = KSr. It is straightforward to check
that this bilinear form satisﬁes the properties
(3.7)
(a, bd) = (ad∗, b);
(a, db) = (d∗a, b)
for any a, b, d ∈A.
Lemma 10 (Murphy, [20, Lemma 4.16]). Let (S, T) be a row standard
pair of µ-tableaux and (U, V ) a standard pair of λ-tableaux, where µ is
a given composition of r and λ a partition of r. Then:
(a) (xST, yU′V ′) = 0 unless (U, V ) ⊵(S, T);
(b) (xUV , yU′V ′) = ±1
where T ′ denotes the transpose of a tableau T.
This is used in proving the following result, which in particular shows
that the rank (over K) of the annihilator of the symmetric group action
on V ⊗r is independent of the characteristic of K.
Proposition 11 (H¨arterich, [12, Lemma 3]). The kernel of Φ, i.e., the
annihilator annKSr V ⊗r, is the cell ideal A[P].
Proof. By Lemma 9, the kernel of Φ contains A[P], so we only need to
prove the reverse containment. Let
a = P
(S,T) aSTyST ∈ker Φ
where aST ∈K, and the sum over all pairs (S, T) of standard tableaux
of shape λ, where λ is a partition of r. It suﬃces to prove: (∗) aST = 0
for all pairs (S, T) of standard tableaux of shape µ ∈P c, where P c is
the complement of P in the set of all partitions of r.
We note that P c is the set of conjugates λ′ of partitions λ in Λ(n, r).
Write Λ+(n, r) for the set of partitions in Λ(n, r); this is the set of
partitions of r into not more than n parts.
We proceed by contradiction.
Suppose (∗) is not true.
Since by
Lemma 9 we have P
shape(S,T)∈P aSTyST ∈ker(Φ), it follows that
b = P
shape(S,T)∈P c aSTyST
is also in the kernel of Φ; i.e., the element b annihilates V ⊗r. Under
the assumption we have b̸ = 0. Let (S0, T0) be a minimal pair (with
respect to ⊵) with shape(S0, T0) ∈P c such that aS0T0̸ = 0. So aST = 0
12
STEPHEN DOTY
for all pairs (S, T) with (S0, T0) ⊲(S, T). Let λ0 be the shape of T ′
0
(same as shape of S′
0). Then λ0 ∈Λ+(n, r), and we have
(xλ0S′
0 b, d(T ′
0)) = (xλ0S′
0
X
aSTyST, d(T ′
0))
=
X
aST(d(T ′
0)−1xλ0S′
0, y∗
ST)
=
X
aST(xT ′
0S′
0, yTS)
where all sums are taken over the set of (S, T) of shape some member
of P c. Here, we write xµT shorthand for xT µT, where (as before) T µ is
the µ-tableau in which the numbers 1, . . ., r have been inserted in the
boxes in order from left to right along rows, read from top to bottom.
By Lemma 10(a) all the terms in the last sum are zero unless (S0, T0)⊵
(S, T), in other words (xT ′
0S′
0, yTS) = 0 for all pairs (S, T) which are
strictly more dominant than (S0, T0). By assumption, aST = 0 for all
pairs (S, T) strictly less dominant than (S0, T0). Thus, the above sum
collapses to a single term aS0T0(xT ′
0S′
0, yT0S0), and by our assumption
and Lemma 10(b) this is nonzero.
This proves that xλ0S′
0 b̸ = 0. Thus b does not annihilate the permu-
tation module Mλ0 ≃xλ0A. Since λ0 ∈Λ+(n, r) as noted above, and
thus Mλ0 is isomorphic to a direct summand of V ⊗r, we have arrived
at a contradiction. This proves the result.
□
Corollary 12. For any commutative integral domain K, the K-module
Φ(KSr) is free over K, of rank r! −P
λ∈P N(λ)2, where N(λ) is the
number of standard tableaux of shape λ. In particular, the K-rank of
Φ(KSr) is independent of K.
Proof. By the preceding proposition, Φ(KSr) ≃A/A[P]. This is free
over K because it is a submodule of the free K-module EndK(V ⊗r).
By deﬁnition, A[P] is free over K of rank P
λ∈P N(λ)2, so the result
follows.
□
Now we return to the assumption that K is an inﬁnite ﬁeld, and con-
sider why dimK EndΓ(V ⊗r) is independent of K. This involves facts
about the representation theory of algebraic groups that are less ele-
mentary than facts used so far. We identify the group Γ = GLn(K),
the group of K-rational points in the algebraic group GLn(K), where
K is an algebraic closure of K, with the group scheme GLn over K.
For Γ = GLn(K) we let T be the maximal torus consisting of all
diagonal elements of Γ. Regard an element λ ∈Zn as a character on
T (via diag(a1, . . . , an) →aλ1
1 · · ·aλn
n for ai ∈K×). Consider the Borel
SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC
13
subgroup B consisting of the lower triangular matrices in Γ, and let
∇(λ) be the induced module (see [14, Part I, §3.3]):
indΓ
B(Kλ) = {f ∈K[Γ] : f(gb) = b−1f(g), all b ∈B, g ∈G}
for any λ ∈Zn, where Kλ is the one dimensional T-module with char-
acter λ, regarded as a B-module by making the unipotent radical of B
act trivially.
The dual space M∗= HomK(M, K) of a given rational KΓ-module
M is again a rational KΓ-module, in two diﬀerent ways:
(i)
(g · f)(m) = f(g−1m);
(ii)
(g · f)(m) = f(gtm)
(gT is the matrix transpose of g)
for g ∈Γ, f ∈M∗, m ∈M. Denote the ﬁrst dual by M∗and the
second by MT. Let ∆(λ) = ∇(λ)T. It is known that ∆(λ) ≃∇(−w0λ)∗
where w0 is the longest element in the Weyl group W. The modules
∇(λ), ∆(λ) are known as “dual Weyl modules” and “Weyl modules”,
respectively.6 The most important property these modules satisfy, for
our purposes, is the following
(3.8)
Extj
Γ(∆(λ), ∇(µ)) ≃
(
K
if j = 0 and λ = µ
0
otherwise.
This is a special case of [14, Part II, Proposition 4.13].
Say that a Γ-module M has a ∇-ﬁltration (respectively, ∆-ﬁltration)
if it has an ascending chain of submodules
0 = M0 ⊆M1 ⊆· · · ⊆Mt−1 ⊆Mt = M
such that each successive quotient Mi/Mi−1 is isomorphic with ∇(λi)
(respectively, ∆(λi)) for some λi ∈Zn. Another fact we need goes back
to [24, Theorem B, page 164]:
(3.9)
∆(λ) ⊗∆(µ) has a ∆-ﬁltration
for any λ, µ ∈Zn. (Note that this fundamental result has been ex-
tended in [6], which in turn was extended in [18].) From (3.9) it follows
immediately by taking duals that
(3.10)
∇(λ) ⊗∇(µ) has a ∇-ﬁltration
for any λ, µ ∈Zn.
The following result, which says that V ⊗r is a
“tilting” module for Γ, is now easy to prove.
Lemma 13. V ⊗r has both ∇- and ∆-ﬁltrations.
6Weyl and dual Weyl modules for GLn(K) are studied in [10, Chapters 4, 5],
where they are respectively denoted by Dλ,K and Vλ,K.
14
STEPHEN DOTY
Proof. One has V = ∇(ε1) = ∆(ε1) where ε1 = (1, 0, . . ., 0). The result
then follows from (3.9) and (3.10) by induction on r.
□
For the next argument we will need the notion of formal characters.
Any rational KΓ-module M has a weight space decomposition M =
L
λ∈Zn Mλ where
Mλ = {m ∈M : tm = tλm, for all t ∈T}.
Here tλ = aλ1
1 · · · aλn
n
where t = diag(a1, . . .an) as previously deﬁned,
just before (2.5).
Set X = Zn and let Z[X] be the free Z-module
on X with basis consisting of all symbols e(λ) for λ ∈X, with a
multiplication given by e(λ)e(µ) = e(λ + µ), for λ, µ ∈X. If M is
ﬁnite dimensional, the formal character ch M ∈Z[X] of M is deﬁned
by
ch M = P
λ∈X(dimK Mλ) e(λ).
The formal character of ∆(λ), which is the same as ch ∇(λ) since the
maximal torus T is ﬁxed pointwise by the matrix transpose, is given
by Weyl’s character formula [14, Part II, Proposition 5.10].7
Proposition 14. For any inﬁnite ﬁeld K, dimK EndΓ(V ⊗r) is inde-
pendent of K.
Proof. Let 0 = N0 ⊆N1 ⊆· · · ⊆Ns−1 ⊆Ns = V ⊗r be a ∇-ﬁltration
and 0 = M0 ⊆M1 ⊆· · · ⊆Mt−1 ⊆Mt = V ⊗r a ∆-ﬁltration. Write
(V ⊗r : ∇(λ)) for the number of successive subquotients Ni/Ni−1 which
are isomorphic to ∇(λ), and similarly write (V ⊗r : ∆(λ)) for the num-
ber of successive subquotients Mi/Mi−1 which are isomorphic to ∆(λ).
Since characters are additive on short exact sequences, we have
ch V ⊗r =
X
λ∈X
(V ⊗r : ∇(λ)) ch ∇(λ) =
X
λ∈X
(V ⊗r : ∆(λ)) ch ∆(λ).
Since V ⊗r is self-dual (under the transpose dual) we may choose the
ﬁltration (N∗) to be dual to the ﬁltration (M∗). It follows that s = t
and (V ⊗r : ∇(λ)) = (V ⊗r : ∆(λ)) for all λ.
Now one applies (3.8) and a double induction through the ﬁltrations.
The argument is standard homological algebra, safely left at this point
as an exercise for the reader. At the end one ﬁnds that
dimK EndΓ(V ⊗r) = P
λ∈Zn(V ⊗r : ∇(λ))2
7The computation of the ch ∆(λ) for GLn(C) goes back to Schur’s 1901 disserta-
tion. Thus, these characters are sometimes called Schur functions. See [17] or [23,
Chapter 7] for exhaustive accounts of their many properties.
SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC
15
where the number of nonzero terms in the sum is ﬁnite. The result
follows.
□
Now we are ready to prove the second half of Schur–Weyl duality
in positive characteristic. We remind the reader that we assume the
validity of Theorem 1 in case K = C.
Proposition 15. For any inﬁnite ﬁeld K, the image Φ(KSr) of the
representation Φ is equal to the centralizer algebra EndΓ(V ⊗r), so the
map Φ in (1.3) is surjective.
Proof. The argument is essentially the same as the proof of Proposition
5. By Corollary 12 and Proposition 14 we have equalities
dimK Φ(KSr) = dimC Φ(CSr),
dimK EndGLn(K)((Kn)⊗r) = dimC EndGL(n(C)((Cn)⊗r)
for any inﬁnite ﬁeld K. Since Φ(CSr) = EndGLn(C)((Cn)⊗r) it follows
that dimK Φ(KSr) = dimK EndGLn(K)((Kn)⊗r) for any inﬁnite ﬁeld
K, and thus by comparison of dimensions the second inclusion in (1.2)
must be an equality. Equivalently, the map Φ in (1.3) is surjective.
□
By putting together Propositions 5 and 15 we have now established
Theorem 1 in positive characteristic, assuming its validity for K = C.
Remark 16. (a) Let K be an arbitrary inﬁnite ﬁeld. Lemma 3 gives
the equality dimK(KΓ) =
 n2+r−1
r

, and the proof of Lemma 4 in
light of [13, Theorem 13.19] gives the equality dimK EndSr(V ⊗r) =
P
λ,µ∈Λ(n,r) N(λ+, µ+), where N(λ+, µ+) counts the number of “semi-
standard” tableaux of shape λ+ and weight µ+.
Corollary 12 says
that dimK Φ(KSr) = r! −P
λ∈P N(λ)2, where N(λ) is the number of
standard tableaux of shape λ, and the proof of Proposition 14 shows
that dimK EndΓ(V ⊗r) = P
λ∈Λ+(n,r)(V ⊗r : ∇(λ))2. Thus, in order to
obtain a proof of Theorem 1 in full generality (without assuming its
validity for K = C) from the methods of this paper, one only needs to
demonstrate the combinatorial identities
n2 + r −1
r

=
X
λ,µ∈Λ(n,r)
N(λ+, µ+);
(3.11)
r! −
X
λ∈P
N(λ)2 =
X
λ∈Λ+(n,r)
(V ⊗r : ∇(λ))2.
(3.12)
The author has not attempted to construct a combinatorial proof of
these identities. If one assumes the validity of Theorem 1 in the case
16
STEPHEN DOTY
K = C, then these identities follow from the results in this paper. Al-
ternatively, if one can ﬁnd an independent proof of the identities, then
one would have a new proof of Theorem 1 in full generality, including
the case K = C.
(b) There is a variant of Theorem 1 worth noting. One may twist
the action of Sr on V ⊗r by letting w ∈Sr act as (sgn w)w (so Sr
acts by “signed” place permutations). This action also commutes with
the action of Γ = GL(V ), and Theorem 1 holds for this action as
well. This may be proved the same way. In the course of carrying out
the argument, one needs to replace permutation modules by “signed”
permutation modules, and interchange the role of Murphy’s two bases
{xST}, {yST}.
(c) There is also a q-analogue of Theorem 1, in which one replaces
GLn(K) by the quantized enveloping algebra corresponding to the Lie
algebra gln, and replaces KSr by the Iwahori–Hecke algebra H(Sr).
The generic case (q not a root of unity) of this theorem was ﬁrst ob-
served in Jimbo [15], and the root of unity case was treated in Du,
Parshall, and Scott [8]. Alternatively, one may derive the result in the
root of unity case from Jimbo’s generic version, using arguments along
the lines of those sketched here.
