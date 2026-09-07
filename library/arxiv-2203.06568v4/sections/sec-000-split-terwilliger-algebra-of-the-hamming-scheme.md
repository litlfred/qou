---
doc_id: arxiv-2203.06568v4
doc_title: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-000-split-terwilliger-algebra-of-the-hamming-scheme
section_title: "Split Terwilliger algebra of the Hamming scheme"
section_number: null
pages: 5-8
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
doc_brief: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
an extension of the block-diagonal formula for the Terwilli ger algebra of the Hamming scheme with the deﬁnition of tenso r
product. As in Schrijver’s decomposition of the Terwillige r algebra, this split decomposition is irreducible. By cert ain basic
results from representation theory, An1,n2 will be mapped to a direct sum of simple An1,n2-modules. Thus we have the
following corollary.
Corollary 5. [Sch05, equation (56)] There is an isomorphism from An1,n2 to
⌊
n1
2 ⌋⨁
k=0
⌊
n2
2 ⌋⨁
k′=0
CNk,k′ ×Nk.k′ ,
with Nk,k′ = (n1 − 2k + 1)(n2 − 2k′ + 1) that maps A =∑
i,j,i′,j′,t,t′ xt,t′
i,j,i′,j′ M t,t′
i,j,i′,j′ to
⌊ n1
2 ⌋⨁
k=0
⌊ n2
2 ⌋⨁
k′=0
Bk,k′ ,
where
Bk,k′ =

∑
t,t′
αk,n1,n2
i,j,i′,j′ βn1,t
i,j,kβn2,t′
i′,j′,k′ xt,t′
i,j,i′,j′


((n1−k,n2−k′),(n1−k,n2−k′))
((i,i′),(j,j′))=((k,k′),(k,k′))
with
βnl,t
i,j,k =
nl∑
u=0
(−1)u−t
(u
t
)(nl − 2k
u − k
)(nl − k − u
i − u
)(nl − k − u
j − u
)
,
for l = 1, 2 and
αk,n1,n2
i,j,i′,j′ =
(n1 − 2k
i − k
)− 1
2
(n1 − 2k
j − k
)− 1
2
(n2 − 2k′
i′ − k′
)− 1
2
(n2 − 2k′
j′ − k′
)− 1
2
.
Remark 6. The formula in Corollary 5 was provided by Schrijver in [Sch0 5] to provide SDP constraints for a constant-weight
code of weight w by choosing n1 = w and n2 = n − w.
Now we can derive additional semideﬁnite constraints on a no ntrivial code C ⊂ P from the 2-split Terwilliger algebra of
the Hamming scheme. Deﬁne
xt,t′
i,j,i′,j′ = 1
|C|
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)λt,t′
i,j,i′,j′ , (7)
where
λt,t′
i,j,i′,j′ = {(X, Y, Z) ∈ C3 : |(X∆ Y ) ∩ T1| = i, |(X∆ Z) ∩ T1| = j,
|((X∆ Y ) ∩ (X∆ Z)) ∩ T1| = t,
|(X∆ Y ) ∩ T2| = i′, |(X∆ Z) ∩ T2| = j′,
|((X∆ Y ) ∩ (X∆ Z)) ∩ T2| = t′}|,
(8)
for i, j, t ∈ { 0, . . . , n1}, i′, j′, t′ ∈ { 0, . . . , n2} with i − t ≥ 0, j − t ≥ 0, i + j − 2t ≤ n1, i′ − t′ ≥ 0, j′ − t′ ≥ 0 and
i′ + j′ − 2t′ ≤ n2. Also, the size of the code is
|C| =
n∑
a=0
∑
i+i′=a
(n1
i
)(n2
i′
)
x0,0
i,0,i′,0.
Let λc
a,b, xc
a,b and M c
a,b be deﬁned as in Schrijver’s SDP in the previous section. From the deﬁnitions, we have the following
identities:
λc
a,b =
∑
i+i′=a,j+j′=b,t+t′=c
λt,t′
i,j,i′,j′ , (9)
xc
a,b =
∑
i+i′=a,j+j′=b,t+t′=c
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)
( n
a−c,b−c,c
) xt,t′
i,j,i′,j′ , (10)
M c
a,b =
∑
i+i′=a,j+j′=b,t+t′=c
M t,t′
i,j,i′,j′ . (11)
6
Consider the following two sets of automorphisms:
Π s = {(π1, π2) ∈ G1 × G2 | ∅ ∈ (π1, π2)(C)},
Π ′
s = {(π1, π2) ∈ G1 × G2 | ∅ /∈ (π1, π2)(C)}.
Here the subscript s stands for split. Similarly, we deﬁne
Rs = 1
|Π s|
∑
(π1,π2)∈Π s
χ(π1,π2)(C)(χ(π1,π2)(C))T ,
R′
s = 1
|Π ′s|
∑
(π1,π2)∈Π ′s
χ(π1,π2)(C)(χ(π1,π2)(C))T .
One can immediately see that Rs and R′
s are positive semideﬁnite and they only depend on the action G1 ×G2 on C. Moreover,
Rs and R′
s are elements of An1,n2 as a consequence of the following proposition.
Proposition 7.
Rs =
∑
i,j,i′,j′,t,t′
xt,t′
i,j,i′,j′ M t,t′
i,j,i′,j′ ,
R′
s = |C|
2n − |C|
∑
i,j,i′,j′,t,t′
(
x0,0
i+j−2t,0,i′+j′−2t′,0 − xt,t′
i,j,i′,j′
)
· M t,t′
i,j,i′,j′ .
Proof. Let X ∈ P . We deﬁne Π X
s = {(π1, π2) ∈ Π 1 × Π 2 | (π1, π2)(X) = ∅}. For an element (π1, π2) ∈ Π X
s , we can see π1
as a permutation of T1 and π2 as a permutation of T2. Hence, we have |Π X
s | = n1!n2!. Deﬁne
RX
s = 1
|Π Xs |
∑
(π1,π2)∈Π Xs
χ(π1,π2)(C)(χ(π1,π2)(C))T ,
λt,t′,X
i,j,i′,j′ = |{(Y, Z ) ∈ C2 : |(X∆ Y ) ∩ T1| = i, |(X∆ Z) ∩ T1| = j,
|((X∆ Y ) ∩ (X∆ Z)) ∩ T1| = t,
|(X∆ Y ) ∩ T2| = i′, |(X∆ Z) ∩ T2| = j′,
|((X∆ Y ) ∩ (X∆ Z)) ∩ T2| = t′}|.
For (π1, π2) ∈ Π X
s and ﬁxed i, j, t, i′, j′, t′, observe that the number of 1’s in
(χ(π1,π2)(C)(χ(π1,π2)(C))T )Y,Z
such that (M t,t′
i,j,i′,j′ )Y,Z = 1 is λt,t′,X
i,j,i′,j′ . There are
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)
such (Y, Z ). Thus,
RX
s =
∑
i,j,i′,j′,t,t′
1( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)λt,t′,X
i,j,i′,j′ M t,t′
i,j,i′,j′ .
Next, we see that
Rs =
∑
X∈C
RX
s
|C| , R ′
s =
∑
X /∈C
RX
s
|P \ C| ,
and ∑
X∈C
λt,t′,X
i,j,i′,j′ = λt,t′
i,j,i′,j′ .
Therefore,
Rs =
∑
X∈C
RX
s
|C|
= 1
|C|
∑
i,j,i′,j′,t,t′
1( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)
(∑
X∈C
λt,t′,X
i,j,i′,j′
)
M t,t′
i,j,i′,j′
=
∑
i,j,i′,j′,t,t′
λt,t′
i,j,i′,j′
|C|
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)M t,t′
i,j,i′,j′
=
∑
i,j,i′,j′,t,t′
xt,t′
i,j,i′,j′ M t,t′
i,j,i′,j′ .
7
For (Y, Z ) ∈ C2 with |Y ∆ Z ∩ T1| = i + j − 2t, |Y ∆ Z ∩ T2| = i′ + j′ − 2t′. The number of X ∈ P such that |(X∆ Y ) ∩ T1| =
i, |(X∆ Z) ∩ T1| = j, |((X∆ Y ) ∩ (X∆ Z)) ∩ T1| = t, |(X∆ Y ) ∩ T2| = i′, |(X∆ Z) ∩ T2| = j′, |((X∆ Y ) ∩ (X∆ Z)) ∩ T2| = t′
is
(i+j−2t
i−t
)(n1−t−j+2t
t
)(i′+j′−2t′
i′−t′
)(n2−i′−j′+2t′
t′
)
.
Thus we have
∑
X∈P
λt,t′,X
i,j,i′,j′ =
(i + j − 2t
i − t
)(n1 − t − j + 2t
t
)(i′ + j′ − 2t′
i′ − t′
)(n2 − i′ − j′ + 2t′
t′
)
λ0,0
i+j−2t,0,i′+j′−2t′,0.
Hence,
R′
s =
∑
X∈P\C
RX
s
2n − |C|
= 1
2n − |C|
∑
i,j,i′,j′,t,t′
1( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)

 ∑
X∈P\C
λt,t′,X
i,j,i′,j′

 M t,t′
i,j,i′,j′
= |C|
2n − |C|
∑
i,j,i′,j′,t,t′
1
|C|
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)
·
((i + j − 2t
i − t
)(n1 − t − j + 2t
t
)( i′ + j′ − 2t′
i′ − t′
)
·
(n2 − i′ − j′ + 2t′
t′
)
λ0,0
i+j−2t,0,i′ +j′−2t′,0 − λt,t′
i,j,i′,j′
)
M t,t′
i,j,i′,j′
= |C|
2n − |C|
∑
i,j,i′,j′,t,t′
((i+j−2t
i−t
)(n1−t−j+2t
t
)(i′+j′−2t′
i′−t′
)(n2−i′−j′+2t′
t′
)
|C|
( n1
i−t,j−t,t
)( n2
i′−t′,j′−t′,t′
)
· λ0,0
i+j−2t,0,i′+j′−2t′,0 − xt,t′
i,j,i′,j′
)
M t,t′
i,j,i′,j′ .
Using the identities
( n1
i − t, j − t, t
)−1(i + j − 2t
i − t
)(n1 − i − j + 2t
t
)
=
( n1
i + j − 2t
)−1
and
( n2
i′ − t′, j′ − t′, t′
)−1(i′ + j′ − 2t′
i′ − t′
)(n2 − i′ − j′ + 2t′
t′
)
=
( n2
i′ + j′ − 2t′
)−1
,
we have
R′
s = |C|
2n − |C|
∑
i,j,i′,j′,t,t′
(
1
|C|
( n1
i+j−2t
)( n2
i′+j′−2t′
) λ0,0
i+j−2t,0,i′+j′−2t′,0 − xt,t′
i,j,i′,j′
)
M t,t′
i,j,i′,j′
= |C|
2n − |C|
∑
i,j,i′,j′,t,t′
(
x0,0
i+j−2t,0,i′+j′−2t′,0 − xt,t′
i,j,i′,j′
)
M t,t′
i,j,i′,j′ .
Using Theorem 5 and the positive semideﬁniteness of Rs and R′
s, we have the following semideﬁnite constraints. For each
k = 0, . . . ,⌊ n1
2 ⌋ and k′ = 0, . . . ,⌊ n2
2 ⌋, the following matrices are positive semideﬁnite:

∑
t,t′
αk,n1,n2
i,j,i′,j′ βn1,t
i,j,kβn2,t′
i′,j′,k′ xt,t′
i,j,i′,j′


((n1−k,n2−k′),(n1−k,n2−k′))
((i,i′),(j,j′))=((k,k′),(k,k′))
, (12)

∑
t,t′
αk,n1,n2
i,j,i′,j′ βn1,t
i,j,kβn2,t′
i′,j′,k′ (x0,0
i+j−2t,0,i′ +j′−2t′,0 − xt,t′
i,j,i′,j′ )


((n1−k,n2−k′),(n1−k,n2−k′))
((i,i′),(j,j′))=((k,k′),(k,k′))
. (13)
8
Proposition 8. Let C be a code with length n and minimum distance at least d. Then xt,t′
i,j,i′,j′ corresponding to C satisfy the
