---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-015-43-arithmetic-properties-of-kerov-polynomials
section_title: "Arithmetic properties of Kerov polynomials"
section_number: 4.3
pages: 21-25
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
4.3.1. Auxiliary results. We present two theorems we need to prove Lemma
3.3.
Theorem 4.2(Doł˛ ega, Féray,´Sniady [DF´S10]). Letk ≥ 1 and lets2,s 3,...
be a sequence of non-negative integers with only ﬁnitely many non-zero el-
ements. The coefﬁcient of Rs2
2 Rs3
3 · · · in the Kerov polynomialKk is equal
to the number of triples (σ1,σ 2,q ) with the following properties:
(a) σ1,σ 2 is a factorization of the cycle; in other words σ1,σ 2 ∈ S(k)
are such thatσ1 ◦σ2 = (1, 2,...,k );
(b) the number of cycles of σ2 is equal to the number of factors in the
productRs2
2 Rs3
3 · · ·; in other words |C(σ2)| =s2 +s3 + · · ·;
(c) the total number of cycles of σ1 andσ2 is equal to the degree of the
productRs2
2 Rs3
3 · · ·; in other words|C(σ1)|+|C(σ2)| = 2s2 +3s3 +
4s4 + · · ·;
(d) q : C(σ2) → { 2, 3,... } is a coloring of the cycles of σ2 with a
property that each color i ∈ { 2, 3,... } is used exactly si times
(informally, we can think that q is a map which to cycles of C(σ2)
associates the factors in the productRs2
2 Rs3
3 · · ·);
(e) for every set A ⊂ C(σ2) which is nontrivial (i.e., A ⁄= ∅ andA ⁄=
C(σ2)) there are more than ∑
i∈A
(
q(i) − 1
)
cycles of σ1 which
intersect⋃ A.
We say that a partitionΠ of the set [k] = {1,...,k } is a pushing partition
if any pair of neighboring elements of [k] with respect to the cyclic order
(i.e.i andi + 1 are a pair of neighboring elements for any 1 ≤i ≤k − 1 as
well as 1 andk) does not belong to the same block of Π .
The cyclic group Z/kZ acts on the set of all partitions (respectively, the
set of pushing partitions) of the set [k] as follows: for a partition Π of [k]
andi ∈ Z/kZ we deﬁnei + Π as the partition of [k] with a property thata,b
belong to the same block of Π if and only ifa′,b ′ belong to the same block
ofi + Π for all a,b,a ′,b ′ ∈ [k] such that a +i ≡ a′ (mod k),b +i ≡ b′
(mod k).
22 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
For any pushing partition Π it is possible (see [ ´Sni06]) to deﬁne the nor-
malized character Σ Π . It has a property that Σ Π = Σ π , where the right-hand
side should be understood as in (1) for some π ∈ S(l),l ≥ 1. So deﬁned
partition-indexed character has the following properties:
Theorem 4.3 (Proposition 4.4, Claim 3.1, Proposition 3.2 in [´Sni06]).
• The map Π ↦→Σ Π is constant on the orbits of the action of the cyclic
group Z/kZ on the set of pushing partitions of [k].
• For any integerk ≥ 2
(19) Rk =
∑
Π
IΠ Σ Π,
where the sum runs over pushing partitions of[k] andIΠ ∈ Z, called
free index, is constant on the orbits of the action of the cyclic group
Z/kZ on the set of pushing partitions of [k].
• For the minimal partition Π =
{
{1},..., {k}
}
the corresponding
character is given by
Σ {{1},..., {k}} = Σ k−1.
4.3.2. Proof of Lemma 3.3.
Proof of Lemma 3.3. In the following we shall prove that the coefﬁcients
are integer numbers. Their nonnegativity would follow from Theorem 4.2.
In order to prove that the coefﬁcients of Σ p−Rp+1+2R2
p are integer we con-
sider the action of the cyclic group Z/pZ on the set of triples (σ1,σ 2,q )
which contribute to Theorem 4.2 deﬁned by conjugation
ψ(i)(σ1,σ 2,q ) =
(
ciσ1c−i,c iσ2c−i,q ′),
wherec = (1, 2,...,k ) is the cycle and q′(a) = q(c−iaci) fora ∈ C(σ2).
All orbits of this action consist ofp elements except for the ﬁxpoints of this
action which are of the formσ1 =ca,σ2 =c1−a. These ﬁxpoints contribute
to the monomial Rp+1 (with multiplicity 1) and to the monomial R2 (with
multiplicityp − 2). This ﬁnishes the proof of the integrality of coefﬁcients
of (a).
We apply Theorem 4.3 in the case when k = p is a prime number. The
right-hand side of (19) is constant on each orbit of the actio n of the cyclic
group Z/pZ. Each orbit of this action consists of p elements, except for
the ﬁxpoints. The only pushing partition of [p] which is invariant under the
action of the cyclic group Z/pZ is the minimal partition
{
{1},..., {p}
}
.
In this way we proved that
Rp = Σ p−1 +p
(
linear combination of the characters Σ π
forπ ∈ S(l),l ≥ 1 with integer coefﬁcients
)
.
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 23
Thanks to Kerov polynomials, each Σ π can be written as a polynomial in
free cumulants with integer coefﬁcients. This shows part (b).
In the following we shall use the notations and results prese nted in the
paper of Biane [Bia03]. In order to prove part (c) we consider the formal
power series
H(z) = z −
∑
j≥1
Bj+1z−j
whereBj are Boolean cumulants. Biane showed that
(20) (−p − 1)Σ p+1 = [z−1]H(z)H(z − 1) · · ·H(z −p)
and
(−p − 1)Rp+2 = [z−1]H(z)p+1.
We know from [Bia03] thatBj is a polynomial in free cumulantsR2,R 3,...
with integer coefﬁcients as well as Σ p+1 is a polynomial in Boolean cumu-
lants B2,B 3,... with integer coefﬁcients; hence it sufﬁces to show that
(−p − 1)(Σ p+1 −Rp+2 +R3) is a polynomial in Boolean cumulants with all
coefﬁcients divisible byp. It is equivalent to show thatΣ p+1 −Rp+2 +R3 =
0 under additional assumption that all coefﬁcients of the pow er series are
taken from a ﬁeld of characteristicp, hence all formulas are considered in a
ﬁeld of characteristicp from now.
From (20) it follows that
[B3]Σ p+1 = 1
p + 1
∑
0≤z≤p
1
2
d2
dz2
[
z(z − 1) · · ·(z −p)
]
.
From Fermat’s little theorem (see for example [GKP94]) it fo llows that in
the ﬁeld of characteristicp
z(z − 1) · · ·(z −p) = z(zp −z) = zp+1 −z2
hence
(21) [B3]Σ p+1 = 1
p + 1
∑
0≤z≤p
(−1) = −1.
We deﬁneB0 = −1 andB1 = 0; then using binomial formula we have
H(z −i) =
∑
j≥−1
∑
k≥0
(−1)k+1
( −j
k
)
ikBj+1z−(j+k),
24 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
hence
(22) − 1
p + 1H(z)H(z − 1) · · ·H(z −p) =
− 1
p + 1
∑
k∈A
∑
j∈B
(−1)|k|1+p+1
( ∏
0≤i≤p
( −ji
ki
)
ikiBji+1
)
z−|j|0−|k|1,
whereA,B ⊂ Zp+1 such that
A = {(k0,k 1,...,k p) : ki ≥ 0 for 0 ≤i ≤p},
B = {(j0,j 1,...,j p) : ji ≥ −1 for 0 ≤i ≤p}
and for k = (k0,k 1,...,k p), i ∈ { 0, 1} the sum ki +ki+1 + · · · +kp is
denoted by |k|i. For any a ∈ Z/pZ such that a ⁄= 0 the map x ↦→ax is a
bijection of the multiset (0, 1,...,p ) ⊂ Z/pZ (notice that 0 = p appears
twice in this multiset) therefore the left-hand side of (22) is equal to
(23) − 1
p + 1H(z)H(z −a) · · ·H(z −pa) =
− 1
p + 1
∑
k∈A
∑
j∈B
(−1)|k|1+p+1a|k|1
( ∏
0≤i≤p
( −ji
ki
)
ikiBji+1
)
z−|j|0−|k|1.
The coefﬁcient ofz−1 in (23) can be viewed as a polynomial ina; we shall
denote it byP (a). In the following we will study its coefﬁcients of highest
degrees. We are interested only in the summands for which |j|0 + |k|1 = 1;
since |j|0 ≥ −p − 1 therefore |k|1 ≤p + 2 and the degree ofP (a) is at most
p + 2.
However, |k|1 =p + 2 would correspond to the casej = (−1, 1,..., −1)
which is equivalent to settingB2 =B3 = · · · = 0; therefore [ap+2]P (a) =
0.
For |k|1 = p + 1 there is no summand for which j0,...,j p ⁄= 0 hence
[ap+1]P (a) = 0 .
For |k|1 =p every summand which contributes is of the following form:
one of the numbersj0,...,j p is equal to 1 and all the others are equal to−1.
This shows that [ap]P (a) viewed as a polynomial in B2,B 3,... contains
only one monomial, namely a multiple of B2; also [B2]P (a) viewed as
a polynomial in a contains only one monomial namely a multiple of ap.
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 25
Therefore [ap]P (a) is a multiple ofB2 and the value of the coefﬁcient ofB2
fulﬁlls:
[B2][ap]P (a) = [B2]P (1) = [B2]Σ p+1.
Sincep is odd, the expansion ofΣ p+1 into Boolean cumulants contains only
summands which are of odd degree [Bia03]; it follows that [ap]P (a) = 0 .
In an analogous way we prove that [ap−1]P (a) is a multiple ofB3 and
[B3][ap−1]P (a) = [B3]Σ p+1 = −1
from (21).
In this way we proved that P (a) is a polynomial of degree p − 1 which
takes the same value for alla ∈ {1,...,p − 1}. Polynomial
~P (a) = −B3ap−1 +P (0)
has the same properties. It follows that P − ~P has degree at most p − 2
which takes the same value for all a ∈ { 1,...,p − 1} hence it must be
equal to the constant. It follows that ~P =P .
Therefore
Σ p+1 =P (1) = −B3 +Rp+2.
Observation thatB3 =R3 ﬁnishes the proof for the third expression. □
It is interesting that for the ﬁrst two expressions we managed to ﬁnd com-
binatorial proofs while for the last expression there seems to be no natural
candidate for a combinatorial approach.
