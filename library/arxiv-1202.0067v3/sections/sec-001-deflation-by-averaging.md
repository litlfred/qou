---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-001-deflation-by-averaging
section_title: "Deflation by averaging"
section_number: 2
pages: 7-9
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
Let m, n ∈ N. We shall think of Sm o Sn as the group of permutations of
{1, . . . , m} × {1, . . . , n}
that leaves invariant the set of blocks of the form ∆j = {(1, j), . . . , (m, j)},
1 ≤ j ≤ n. Given h1 , . . . , hn ∈ Sm and g ∈ Sn , we write (h1 , . . . , hn ; g) for
the permutation which sends (i, j) to (hgj i, gj). This left action is equivalent
to the action defined in [8, 4.1.18]. Let B = Sm × · · · × Sm denote the base
group in the wreath product. As shorthand, if k = (h1 , . . . , hn ) ∈ B then
we shall write (k ; g) for (h1 , . . . , hn ; g).
Lemma 2.1. Let m, n ∈ N, let ϑ be an irreducible character of Sm , and
×n Inf Sm oSn χν for some
let ξ be an irreducible character of Sm o Sn . If ξ = ϑg
Sn
partition ν of n then
1 X
×n (k ; g) = χν (g),
ξ(k ; g)ϑg
|B|
k∈B

and if ξ ∈ Irr(Sm o Sn ) is not of this form then the left-hand side is zero.
×n of
Proof. Suppose that the left-hand side is non-zero. The character ϑg
Sm o Sn restricts to the irreducible character ϑ × · · · × ϑ of B. Hence,
by
applied with G = Sm o Sn and N = B, we have
E
D [7, Lemma 8.14(b)],
g
×n
6= 0. It follows by Frobenius Reciprocity that ξ is a
ResB ξ, ResB ϑ
constituent of
X
×n Inf Sm oSn χν ,
IndSBm oSn (ϑ × · · · × ϑ) =
χν (1)ϑg
Sn
ν

where the sum is over all partitions ν of n. Since ξ is irreducible we must
×n Inf Sm oSn χν for some ν. Therefore the left-hand side in the
have ξ = ϑg
Sn
lemma is
2
χν (g) X g
ϑ×n (k ; g)
|B|
k∈B

which is equal to χν (g) by [7, Lemma 8.14(c)].



×n Inf Sm oSn χν )(g) = χν (g) for all
By Definition 1.1, we have DefresϑSn (ϑg
Sn
g ∈ Sn . The next proposition therefore follows immediately from Lemma 2.1.


8

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

Proposition 2.2. Let m, n ∈ N, let ϑ be an irreducible character of Sm ,
and let ψ be a character of Sm o Sn . If g ∈ Sn then
1 X
×n (k ; g).
(Def ϑSn ψ)(g) =
ψ(k ; g)ϑg

|B|
k∈B

Corollary 2.3. Let m, n ∈ N, let ϑ be an irreducible character of Sm , and
let ψ be a character of Sm o Sn . If g ∈ Sn is an n-cycle then
1 X
(Def ϑSn ψ)(g) =
ψ(h, 1, . . . , 1; g)ϑ(h).
m!
h∈Sm

Proof. Suppose that g is the n-cycle (x1 x2 . . . xn ). By [8, 4.2.8], the permutations (h1 , . . . , hn ; g) and (h01 , . . . , h0n ; g) ∈ Sm o Sn are conjugate in Sm o Sn
if and only if the elements hxn hxn−1 . . . hx1 and h0xn h0xn−1 . . . h0x1 are conjugate in Sm . In particular, each conjugacy class of Sm o Sn which meets
{(k ; g) : k ∈ B} has a representative of the form (h, 1, . . . , 1; g). Moreover, the number of elements (h1 , h2 , . . . , hn ; g) conjugate to (h, 1, . . . , 1; g)
is m!n−1 |hSm |, since h2 , . . . , hn may be chosen arbitrarily, and then h1 must
be chosen so that hxn hxn−1 · · · hx1 ∈ hSm . It follows that
X
X
×n (k ; g) = m!n−1
×n (h, 1, . . . , 1; g)
ψ(k ; g)ϑg
ψ(h, 1, . . . , 1; g)ϑg
k∈B

h∈Sm

= m!n−1

X

ψ(h, 1, . . . , 1; g)ϑ(h)

h∈Sm

where the second equality uses [8, Lemma 4.3.9]. Now apply Proposition 2.2
to the left-hand side.

The following definition and lemma allow for a more convenient statement
of Corollary 2.3.
Definition 2.4. Let m, n ∈ N, let g ∈ Sn be an n-cycle, and let ψ be a
character of Sm o Sn . We define ω(ψ) to be the class function on Sm such
that
ω(ψ)(h) = ψ(h, 1, . . . , 1; g)
for all h ∈ Sm .
Lemma 2.5. Let m, n ∈ N. If g ∈ Sn is an n-cycle and h ∈ Sm has cycle
type α then (h, 1, . . . , 1; g) ∈ Sm o Sn has cycle type nα.
Proof. It suffices to show that if O is an orbit of h on {1, 2, . . . , m} then
O × {1, . . . , n} is an orbit of (h, 1, . . . , 1; g) in its action on {1, . . . , m} ×
{1, . . . , n}. We leave this to the reader as an easy exercise.

The next proposition follows easily from Lemma 2.5 and Corollary 2.3.


CHARACTER DEFLATIONS

9

Proposition 2.6. Let m, n ∈ N, and let χ be a character of Smn .
(i) If α is a partition of m then
ω(ResSm oSn χ)(gα ) = χ(gnα ).
(ii) If ϑ is an irreducible character of Sm and g ∈ Sn is an n-cycle then
(DefresϑSn χ)(g) = hω(ResSm oSn χ), ϑi
X χ(gnα )
=
ϑ(gα )
zα
α
where the sum is over all partitions α of m.



The character value χ(gnα ) in part (i) is the subject of Theorem 3.3; we
shall see that combining this theorem with part (ii) gives Equation (8) in §4
below. Note also that part (ii) of the proposition implies Equation (3) in §2.
