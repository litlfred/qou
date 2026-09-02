---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-005-25-sign-sequences-and-hook-partitions
section_title: "Sign sequences and hook partitions"
section_number: 2.5
pages: 3-5
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
---
partition (n −ℓ, 1ℓ). We refer to ℓ as leg length .
Lemma 2.6. Standard tableaux of shape λℓ are in bijection with sign sequences ε =
(ε1,...,ε n) ∈ {±} n such that ε1 = + and ℓ entries equal −.
Proof. Beginning with a standard λℓ-tableau, deﬁne ε = (ε1,...,ε n) by
(5) εr =
{
+, if r appears on the ﬁrst row
−, otherwise
A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL 4
Notice that the box labeled 1 has to be in the corner of the hook, so ε1 = +. Also, ℓ
numbers are on the leg of the hook, so there are ℓ entries equal to −.
For the inverse, starting with a sign sequence ε = (ε1,...,ε n) with ε1 = + and ℓ
other entries equal to −, construct a standard tableau recursively, as follows. Place
1 in the corner of the diagram. Now, for each r > 1, suppose that the numbers
1,...,r − 1 have been placed. Either add r to the end of the ﬁrst row or at the
bottom of the ﬁrst column, according to whether εr is + or −, respectively. □
Using this bijection, we can adapt the semi-normal representation to the combina-
torics of sign sequences.
Theorem 2.7. The irreducible module S(λℓ) has basis {xε}, where ε runs over sign
sequences havingε1 = + andℓ other entries equal to −. The generators H1,...,H n−1
of Hn act by
(6) Hrxε =ar(ε)xε +br(ε)xsrε
where srε denotes the sign sequence obtained from ε by permuting εr and εr+1, xε is
interpreted as zero if ε1 = −, and
ar(ε) =



v if (εr,ε r+1) = (+, +)
−v−1 if (εr,ε r+1) = ( −, −)
vr/[r] if (εr,ε r+1) = ( −, +)
−v−r/[r] if (εr,ε r+1) = (+, −),
(7)
br(ε) =



[r + 1]/[r] if (εr,ε r+1) = ( −, +)
[r − 1]/[r] if (εr,ε r+1) = (+, −)
0 otherwise.
(8)
The inverse generators H −1
1 ,...,H −1
n−1 act by
(9) H −1
r xε = ¯ar(ε)xε +br(ε)xsrε
where ¯ar(ε) is obtained from ar(ε) by replacing v by v−1.
Proof. This is just a translation of Theorem 2.4 using the bijection from Lemm a 2.6.
Given a sign sequence ε ∈ {±} n having ε1 = + and ℓ other entries equal to −, con-
struct the corresponding standard tableau, and let ( i1,...,i n) be its residue sequence.
We have i1 = 0, and for 1 ≤r<n ,
(10) ir+1 =



ir + 1 if ( εr,ε r+1) = (+, +)
ir − 1 if ( εr,ε r+1) = ( −, −)
ir +r if (εr,ε r+1) = ( −, +)
ir −r if (εr,ε r+1) = (+, −).
Given this, the formulae (7)–(8) are easily deduced from (3). Finally the formula (9)
is easily deduced from (6) since H −1
r =Hr − (v −v−1). □
A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL 5
