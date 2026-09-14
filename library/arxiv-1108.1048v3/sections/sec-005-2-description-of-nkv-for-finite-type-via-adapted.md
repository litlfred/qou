---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-005-2-description-of-nkv-for-finite-type-via-adapted
section_title: "Description of Nk(v) for Finite Type Via Adapted Strings"
section_number: 2
pages: 14-17
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules ove r Khovanov-Lauda- Rouquier algebras R and their"
---
In this section, we give an explicit description of the modul es Nk(v) for ﬁnite type. To
that end, we choose a particular reduced expression of the lo ngest element w0 of the Weyl
group W . Using the notion of adapted strings for crystals given in [2 4] with respect to these
specially chosen expressions, we describe Nk(v) explicitly in terms of Kashiwara operators ˜fi
(Proposition 2.3).
Throughout the section, we assume that the Cartan datum ( A, P, Π , P∨, Π ∨) is of ﬁnite
type. For a sequence m = ( m1, . . . , mk) of elements in I, we write rm = rm1rm2 · · ·rmk
for the corresponding element in the Weyl group. Using this c onvention, we ﬁx a particular
reduced expression for the longest element w0 of W
(2.1) w0 = rs1rs2 · · · rsn = rs1rs2 · · ·rsℓ
where the sequences sk are displayed in Table 1 below. Let lk be the length of the sequence
sk in (2.1) for k = 1 , . . . , n. Then rs1 = rs1 · · ·rsl1
, rs2 = rsl1+1 · · ·rsl1+l2
and so forth. Note
that ℓ is the length of the reduced expression.
Deﬁnition 2.1. Let v ∈ B(∞) (resp. v ∈ B(λ)). An ℓ-tuple a(v) = ( a1, . . . , aℓ) ∈ (Z≥0)ℓ is
called the adapted string of v with respect to the expression rs1 · · ·rsℓ if
a1 = εs1(v), a 2 = εs2
(
˜ea1
s1 v
)
, . . . , a ℓ = εsℓ
(
˜eaℓ−1
sℓ−1 · · · ˜ea1
s1 v
)
.
We denote by S = {a(v) | v ∈ B(∞)} (resp. S λ = {a(v) | v ∈ B(λ)}) the set of all adapted
strings of elements in B(∞) (resp. B(λ)).
Observe that if ιλ(v) = v′ ⊗ tλ ⊗ c for some v ∈ B(λ) and v′ ∈ B(∞), then a(v) = a(v′). It
follows from [17, 23] that S and S λ are in one-to-one correspondence with the crystals B(∞)
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 15
Table 1.
Dynkin diagrams w0 = rs1 · · ·rsn
(An) ◦ ◦ ◦ ◦
1 2 n − 1 n sk = (n + 1 − k, . . . , n− 1, n) for k = 1, . . . , n
(Bn)
/d43/d51◦ ◦ ◦ ◦
1 2 n − 1 n
sk = (n + 1 − k, . . . , n− 1, n, n − 1, . . . , n+ 1 − k)
for k = 1, . . . , n
(Cn) /d107/d115◦ ◦ ◦ ◦
1 2 n − 1 n sk is the same as for type Bn for k = 1, . . . , n
(Dn)
♦♦♦ ❖❖❖◦ ◦ ◦ ◦
◦1 2 n − 2
n
n − 1
s1 = (n), s2 = (n − 1),
sk = (n + 1 − k, . . . , n− 2, n, n − 1, n − 2, . . . , n+ 1 − k)
for k = 3, . . . , n
(E6) ◦ ◦ ◦ ◦ ◦
◦
1 2 3 5 6
4 sk is the same as for type D5 for k = 1, . . . ,5,
s6 = (6, 5, 3, 4, 2, 1, 3, 2, 5, 3, 4, 6, 5, 3, 2, 1),
(E7) ◦ ◦ ◦ ◦ ◦ ◦
◦
1 2 3 5 6 7
4 sk is the same as for type E6 for k = 1, . . . ,6,
s7 = (7, 6, 5, 3, 4, 2, 1, 3, 2, 5, 3, 4, 6, 5, 3, 2, 1, 7, 6, 5, 3, 4, 2,
3, 5, 6, 7)
(E8) ◦ ◦ ◦ ◦ ◦ ◦ ◦
◦
1 2 3 5 6 7 8
4
sk is the same as for type E7 for k = 1, . . . ,7,
s8 = (8, 7, 6, 5, 3, 4, 2, 1, 3, 2, 5, 3, 4, 6, 5, 3, 2, 1, 7, 6, 5, 3, 4,
2, 3, 5, 6, 7, 8, 7, 6, 5, 3, 4, 2, 1, 3, 2, 5, 3, 4, 6, 5, 3, 2, 1,
7, 6, 5, 3, 4, 2, 3, 5, 6, 7, 8)
(F4) /d43/d51◦ ◦ ◦ ◦
1 2 3 4
sk is the same as for type B3 for k = 1, . . . ,3,
s4 = (4, 3, 2, 1, 3, 2, 3, 4, 3, 2, 1, 3, 2, 3, 4)
(G2)
✹✹
✡✡◦ ◦
1 2 s1 = (1), s2 = (2, 1, 2, 1, 2)
and B(λ), respectively, by the maps
(2.2)
S 1-1− →B(∞) given by a = (a1, . . . , aℓ) ↦→˜f a1
s1 · · · ˜f aℓ
sℓ 1,
S λ 1-1− →B(λ) given by a = (a1, . . . , aℓ) ↦→˜f a1
s1 · · · ˜f aℓ
sℓ bλ.
16 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
For a = (a1, . . . , aℓ) ∈ (Z≥0)ℓ, set
ak,j = al1+···+lk−1+j and ak = (ak,1, ak,2, . . . ,ak,lk ),(2.3)
where lk is, as above, the length of sk. Then a = a1 ∗ · · · ∗ an.
In particular, for v ∈ B(∞), we have a(v) = a(v)1 ∗ · · · ∗ a(v)n and
v = ˜f a(v)1
s1
˜f a(v)2
s2 · · · ˜f a(v)n
sn 1.
Proposition 2.2 ([24]). Let (A, P, Π , P∨, Π ∨) be a Cartan datum of ﬁnite type. Then S has
the following description:
(An) : {a ∈ (Z≥0)ℓ | ai,1 ≥ ai,2 ≥ · · · ≥ ai,i (1 ≤ i ≤ n)}
(Bn) : {a ∈ (Z≥0)ℓ | 2ai,1 ≥ · · · ≥ 2ai,i−1 ≥ ai,i ≥ 2ai,i+1 ≥ · · · ≥ 2ai,2i−1 (1 ≤ i ≤ n)}
(Cn) : {a ∈ (Z≥0)ℓ | ai,1 ≥ · · · ≥ ai,i−1 ≥ ai,i ≥ ai,i+1 ≥ · · · ≥ ai,2i−1 (1 ≤ i ≤ n)}
(Dn) : {a ∈ (Z≥0)ℓ | ai,1 ≥ · · · ≥ ai,i−1, ai,i ≥ ai,i+1 ≥ · · · ≥ ai,2i−2 (3 ≤ i ≤ n)}
(E6) : {a ∈ (Z≥0)ℓ | a6,1 ≥ a6,2 ≥ a6,3 ≥ a6,4, a6,5 ≥ a6,7 ≥ a6,8, a6,9 ≥ a6,10 ≥ a6,11, a6,13
≥ a6,14 ≥ a6,15 ≥ a6,16; a6,5 ≥ a6,6 ≥ a6,8; a6,9 ≥ a6,12 ≥ a6,13;
ai,j’s satisfy the inequalities for D5 for i = 1, . . . ,5}
(E7) : {a ∈ (Z≥0)ℓ | a7,1 ≥ a7,2 ≥ a7,3 ≥ a7,4 ≥ a7,5, a7,6 ≥ a7,8 ≥ a7,9, a7,10
≥ a7,11 ≥ a7,12, a7,14 ≥ a7,15 ≥ a7,16, a7,20 ≥ a7,21 ≥ a7,22, a7,23
≥ a7,24 ≥ a7,25 ≥ a7,26 ≥ a7,27; a7,6 ≥ a7,7 ≥ a7,8;
a7,10 ≥ a7,13 ≥ a7,14, a7,18 ≥ a7,19 ≥ a7,20; a7,16 ≥ a7,17 ≥ a7,23;
ai,j’s satisfy the inequalities for E6 for i = 1, . . . ,6}
(E8) : {a ∈ (Z≥0)ℓ | (a8,2, . . . ,a8,28) and (a8,30, . . . ,a8,56) satisfy the inequalities of a7 for E7;
a8,1 ≥ a8,2; a8,29 ≥ a8,30; a8,56 ≥ a8,57;
a8,19 ≥ max{a8,30, a8,29 − a8,28}; min{a8,23, a8,25 + a8,33 − a8,34} ≥ a8,35;
a8,20 ≥ max{a8,31, a8,28 + a8,30 − a8,27}; min{a8,25, a8,26 + a8,32 − a8,33} ≥ a8,37;
a8,21 ≥ max{a8,32, a8,27 + a8,31 − a8,26}; min{a8,26, a8,27 + a8,31 − a8,32} ≥ a8,39;
a8,22 ≥ max{a8,33, a8,26 + a8,32 − a8,25}; min{a8,27, a8,28 + a8,30 − a8,31} ≥ a8,42;
a8,24 ≥ max{a8,34, a8,25 + a8,33 − a8,23}; min{a8,28, a8,29 − a8,30} ≥ a8,47;
ai,j’s satisfy the inequalities for E7 for i = 1, . . . ,7}
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 17
(F4) : {a ∈ (Z≥0)ℓ | a4,1 ≥ a4,2 ≥ a4,3 ≥ a4,4, a4,5 ≥ a4,6 ≥ a4,7;
a4,9 ≥ a4,10 ≥ a4,11, a4,12 ≥ a4,13 ≥ a4,14 ≥ a4,15;
a4,5 ≥ a4,9; a4,7 ≥ a4,12; a4,5 + a4,7 ≥ a4,8 ≥ a4,9 + a4,12;
2a4,6 ≥ a4,7 + a4,9 ≥ 2a4,10;
ai,j’s satisfy the inequalities for B3 for i = 1, 2, 3}
(G2) : {a ∈ (Z≥0)ℓ | 6a2,1 ≥ 2a2,2 ≥ 3a2,3 ≥ 2a2,4 ≥ 6a2,5}.
We now give a description of Nk(v) using Proposition 2.2.
Proposition 2.3. Let (A, P, Π , P∨, Π ∨) be a Cartan datum of ﬁnite type. For v ∈ B(∞) and
k = 1, . . . , n, the module Nk(v) deﬁned by (1.4) is given by
Nk(v) = ˜f a(v)k
sk 1,
where a(v) is the adapted string of v with respect to the expression w0 = rs1 · · ·rsn in Table
1.
Proof. Let I(k) = {n + 1 − k, . . . , n − 1, n} for k = 1 , . . . , n and set I(0) = ∅. Let Bk denote
the crystal obtained from B(∞) by forgetting the i-arrows with i /∈ I(k). Take v ∈ B(∞)
and let a = a(v) = a1 ∗ · · · ∗ an be the adapted string of v with respect to the expression
w0 = rs1 · · · rsn in Table 1. For k = 1 , . . . , n, let 0k = (0 , . . . ,0/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
lk
) where lk is the length of sk
as before. Then, by Proposition 2.2,
bk := 01 ∗ . . . ∗ 0k ∗ ak+1 ∗ . . . ∗ an−1 ∗ an
is contained in S. Let uk = ˜f ak+1
sk+1 · · · ˜f an
sn 1 for k = 0, . . . , n− 1 and let un = 1. Since bk is the
adapted string of uk, by the deﬁnition of adapted strings we have
v = ˜f a1
s1 · · · ˜f ak
sk uk, ε i(uk) = 0 for i ∈ I(k),
which implies that uk is the highest weight vector of the connected component Ck of Bk
containing v. Therefore, Nk(v) = ˜f ak
sk 1 for k = 1, . . . , n. □
