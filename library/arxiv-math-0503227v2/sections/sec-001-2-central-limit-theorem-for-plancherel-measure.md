---
doc_id: arxiv-math-0503227v2
doc_title: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios By Jason Fulman"
section_id: sec-001-2-central-limit-theorem-for-plancherel-measure
section_title: "Central limit theorem for Plancherel measure"
section_number: 2
pages: 3-9
source_pdf: 0503227v2.pdf
source_sha256: 4e83adfdef827103
doc_brief: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios By Jason Fulman — Bolthausen used a variation of Stein’s method to give an"
---
The random variable we wish to study is Tn(λ) =
√
(n
2)χ λ (12)
dim(λ ) where λ is
chosen from the Plancherel measure of the symmetric group Sn. To begin we
write Tn as a sum of other random variables. For this we need Kerov’s growth
process on partitions [K2]; this has a natural generalizati on to arbitrary ﬁnite
groups [F3], but we only recall it in the case of interest. Giv en a partition
λ(j) of size j, one obtains a partition λ(j +1) of size j +1 by choosing λ(j +1)
with probability dim(λ (j+1))
(j+1)dim(λ (j)) if λ(j+1) can be obtained from λ(j) by adding
a single box, and with probability 0 otherwise. Thus startin g from λ(1), the
4
unique partition of size 1, one obtains a random sequence ( λ(1), · · · , λ (n))
of partitions. Kerov [K2] proves that each λ(j) is distributed according to
the Plancherel measure of Sj.
Given Kerov’s growth process, one can write Tn = 1
√
(n
2) (X1 + · · · + Xn)
where X1 = 0, χ λ (1)(12) is deﬁned as 0, and
Xj =
( j
2
)
χ λ (j)(12)
dim(λ(j)) −
( j−1
2
)
χ λ (j−1)(12)
dim(λ(j − 1))
for j ≥ 2.
Lemma 2.1 states that the Xj are martingale diﬀerences satisfying special
properties. We remark that [F3] extends this lemma to more ge neral conju-
gacy classes and groups. The notation E(A|·) means the expected value of
A given ·.
Lemma 2.1. ([F3])
(1) E(Xj|λ(j − 1)) = 0 for 2 ≤ j ≤ n and all partitions λ(j − 1).
(2) E(Xj|Tn) = j−1√
(n
2) Tn for all 1 ≤ j ≤ n.
(3) E(X 2
j ) = j − 1.
(4) E(T 2
n ) = 1 .
Frobenius [Fr] found the following explicit formula for the character ratio
of the symmetric group on transpositions:
χ λ (12)
dim(λ) = 1( n
2
)
∑
i
(( λ i
2
)
−
( λ ′
i
2
))
where λ i is the length of row i of λ and λ ′
i is the length of column i of λ.
From his formula it follows that Xj = c(x) where x is the box added to
λ(j − 1) to obtain λ(j) and the “content” c(x) of a box is deﬁned as column
number of box - row number of box.
Lemma 2.2 gives the conditional second and fourth moments of the Xj’s.
We emphasize that these were not derived or even stated in ter ms of char-
acter ratios, but rather were proved in a completely combina torial way by
studying the behavior of the moments of c(x) where x is the box added
during Kerov’s growth process. We remark that for other conj ugacy classes,
there is not an analog of the fact that E(X 2
j |λ(j − 1)) is independent of
λ(j − 1).
Lemma 2.2. Let λ(j − 1) be a partition of size j − 1 ≥ 1.
(1) ([K3]) E(X 2
j |λ(j − 1)) = j − 1.
(2) ([La]) E(X 4
j |λ(j − 1)) =
( j
2
)
+ 3∑
x∈λ (j−1) c(x)2.
Lemma 2.3 is a useful identity. Although a combinatorial pro of can be
given using properties of Schur functions, we defer combina torial arguments
to the more general setting of Jack polynomials in Section 3 a nd give an
algebraic proof.
5
Lemma 2.3. Let er(z1, · · · , z n) = ∑
1≤i1<···<ir≤n zi1 · · ·zir be the rth ele-
mentary symmetric function of z1, · · · , z n. For λ a partition of n, let er(λ)
denote the rth elementary symmetric function of the content s of the boxes
of λ. Then E(er(λ)) = 0 for 1 ≤ r ≤ n.
Proof. If r = n the result is clear since the box in the ﬁrst row and column
of λ has content 0, so that en(λ) = 0 for all λ.
For 1 ≤ r < n , we use the theory of Murphy elements [Mu]; a friendly
reference giving background on these elements is [DG]. For 2 ≤ i ≤ n, the ith
Murphy element is deﬁned as the sum of transpositions Ri =∑
1≤j<i(j, i ).
Let z be the element of the group algebra of Sn which is the sum of all
permutations with n − r cycles. By Proposition 2.1 of [DG], z is the rth
elementary symmetric function of the elements R2, · · · , R n.
Since the elements R2, · · · , R n are simultaneously diagonalizable in every
irreducible representation of the symmetric group, it foll ows from Murphy’s
determination of their eigenvalues that in the representat ion of Sn parame-
terized by λ, z is a scalar multiple of the dim(λ) × dim(λ) identity matrix
with scalar equal to er(λ). In the regular representation of Sn the irreducible
representation parameterized by λ occurs with multiplicity dim(λ). Hence
the trace of z in the regular representation is n!E(er(λ)). But the coeﬃcient
of the identity in z is 0, so the trace of z in the regular representation is 0,
implying the result. □
Lemma 2.4 gives upper bounds for E(|Xn|3) and for E(|Tn−1||Xn|3). One
could prove a similar bound (with slightly worse constants) using the con-
centration inequality for Xn in the proof of Theorem 2.5.
Lemma 2.4. Suppose that n ≥ 3.
(1) E(|Xn|3) ≤ (n − 1)√2n − 3.
(2) E(|Tn−1||Xn|3) ≤ (n − 1)√2n − 3.
Proof. By the Cauchy-Schwarz inequality, E(|Xn|3) ≤
√
E(X 2n)E(X 4n). By
Lemma 2.2, E(X 2
n) = n − 1 and
E(X 4
n) = E(E(X 4
n|λ(n − 1))) =
( n
2
)
+ 3E

 ∑
x∈λ (n−1)
c(x)2

 .
By Lemma 2.3 with r = 2 and then part 4 of Lemma 2.1,
E

 ∑
x∈λ (n−1)
c(x)2

 = E



 ∑
x∈λ (n−1)
c(x)


2
− 2e2(λ(n − 1))


=
( n − 1
2
)
E(T 2
n−1)
=
( n − 1
2
)
.
6
This proves the ﬁrst assertion.
For the second assertion, note (using part 4 of Lemma 2.1 in th e ﬁnal
equality) that
E(|Tn−1||Xn|3) = E(E(|Tn−1||Xn|3|λ(n − 1)))
= E(|Tn−1|E(|Xn|3|λ(n − 1)))
≤
√
E(T 2
n−1)E(E(|Xn|3|λ(n − 1))2)
=
√
E(E(|Xn|3|λ(n − 1))2).
The conditional version of the Cauchy-Schwarz inequality a nd part 1 of
Lemma 2.2 give that E(|Xn|3|λ(n − 1))2 is at most
E(X 2
n|λ(n − 1))E(X 4
n|λ(n − 1)) = ( n − 1)E(X 4
n|λ(n − 1)).
Thus √
E(E(|Xn|3|λ(n − 1))2) ≤
√
(n − 1)E(X 4n),
and the proof of the ﬁrst assertion showed this to equal ( n − 1)√2n − 3, as
desired. □
Now we adapt Bolthausen’s [Bol] inductive proof of the Berry -Esseen
theorem for i.i.d. random variables to the setting of charac ter ratios. We
remark that the unpublished notes of Mann [Man] are a useful e xposition
of Bolthausen’s proof and we refer to them in the proof of Theo rem 2.5.
Theorem 2.5. Let λ be chosen from the Plancherel measure on partitions
of size n. Then for all n ≥ 2 and real x0,
⏐
⏐
⏐
⏐P (Tn(λ) ≤ x0) − 1
√
2π
∫ x0
−∞
e− t2
2 dt
⏐
⏐
⏐
⏐ ≤ Cn −1/ 2,
where C is a universal constant.
Proof. It is suﬃcient to prove the result for n ≥ 3, so we assume this.
For z real, let hz, 0 = I(−∞,z ] be the indicator function of the set ( −∞, z ].
For z real and b > 0, let hz,b be the function which is 1 for x ≤ z and then
drops linearly to the value 0 at z + b and is 0 for x ≥ z + b. Let
δ(b, n ) = sup
z
{|E(hz,b (Tn)) − Φ hz,b |}
where Φ f is the expected value of a function f under the normal distrib ution.
Note that our ultimate goal is to upper bound δ(0, n ).
As in Stein’s method [Stn], let
f (x) = fz,b (x) = ex2/ 2
∫ x
−∞
(hz,b (w) − Φ hz,b )e−w2/ 2dw.
Then f ′(x) − xf (x) = hz,b (x) − Φ hz,b , so that
E(hz,b (Tn)) − Φ hz,b = E[f ′(Tn) − Tnf (Tn)].
7
Part 2 of Lemma 2.1 with j = n implies that
E(Xnf (Tn)) = E[f (Tn)E(Xn|Tn)] = n − 1√ ( n
2
) E(Tnf (Tn)),
so that
E[f ′(Tn) − Tnf (Tn)] = E

f ′(Tn) −
√
( n
2
)
n − 1 Xnf (Tn)

 .
By part 1 of Lemma 2.1 and part 1 of Lemma 2.2, this is equal to
E
[
f ′(Tn)
]
+ E
[
X 2
n
n − 1 f ′(
√
n − 2
n Tn−1) − f ′(
√
n − 2
n Tn−1)
]
−E


√
( n
2
)
n − 1 Xnf (Tn) −
√ ( n
2
)
n − 1 Xnf (
√
n − 2
n Tn−1)


= E
[
f ′(Tn) − f ′(
√
n − 2
n Tn−1)
]
−E

 X 2
n
n − 1
∫ 1
0
f ′(
√
n − 2
n Tn−1 + t Xn√ ( n
2
) ) − f ′(
√
n − 2
n Tn−1)dt

 .
Next we upper bound E[f ′(Tn) − f ′(
√
n−2
n Tn−1)]. Recall from [Bol] or
[Man] that for any x and ∆,
|f ′(x + ∆) − f ′(x)| ≤ | ∆ |
(
3 + 2|x| + 1
b
∫ 1
0
I[z,z +b](x + s∆) ds
)
.
Thus E[f ′(Tn) − f ′(
√
n−2
n Tn−1)] ≤ A1 + A2 + A3 where
• A1 = 3E(|Xn|)√
(n
2) .
• A2 =
2
√
n−2
n√
(n
2) E(|Xn||Tn−1|).
• A3 = E
[
|Xn|
b
√
(n
2)
∫ 1
0 I[z,z +b](
√
n−2
n Tn−1 + sXn√
(n
2) )ds
]
.
By part 3 of Lemma 2.1, E(|Xn|) ≤
√
E(X 2n) = √n − 1; thus A1 ≤ 3
√
2√n . By
parts 3 and 4 of Lemma 2.1,
E(|Xn||Tn−1|) ≤
√
E(X 2n)E(T 2
n−1) =
√
n − 1.
Thus A2 ≤ 2
√
2√n .
8
Note that A3 = A′
3 + A′′
3 where
A′
3 = E

I(|Xn| ≤ 2e√
n) |Xn|
b
√ ( n
2
)
∫ 1
0
I[z,z +b](
√
n − 2
n Tn−1 + sXn√ ( n
2
) )ds


and
A′′
3 = E

I(|Xn| > 2e√
n) |Xn|
b
√ ( n
2
)
∫ 1
0
I[z,z +b](
√
n − 2
n Tn−1 + sXn√ ( n
2
) )ds

 .
Clearly
A′
3 ≤ 2e√
n
b
√ ( n
2
) E

I[z− 2e√
n√
(n
2)
,z +b+ 2e√n√
(n
2)
]
( √
n − 2
n Tn−1
) 
 .
Now use the fact (explained in [Man]) that
0 ≤ E(IB(c1Tn + c2)) ≤ |B|
c1
√
2π
+ 2δ(0, n )
for any interval B and constants c1, c 2 with c1 ⁄= 0. It follows that A′
3 ≤
D1
√n + D2
bn + D3δ(0,n −1)
b√n where D1, D 2, D 3 are universal constants. To bound
A′′
3, note that since |Xn| ≤ n, one has that A′′
3 ≤ n
b
√
(n
2) P(|Xn| > 2e√n).
The proof of Proposition 4.6 of [F1] derives the concentrati on inequality
P(|Xn| > 2e√n) ≤ 2e−2e√n. Since b will later be chosen to be a constant
multiplied by n−1/ 2, it follows that A′′
3 is much smaller than A′
3 for large n,
and one concludes that
A3 ≤ D1
√n + D2
bn + D3δ(0, n − 1)
b√n
where D1, D 2, D 3 are universal constants.
Combining the bounds on A1, A 2, A 3, we conclude that
E
[
f ′(Tn) − f ′(
√
n − 2
2 Tn−1)
]
≤ D1√n + D2
bn + D3δ(0, n − 1)
b√n
where D1, D 2, D 3 are universal constants.
Next, we upper bound
E
⏐
⏐
⏐
⏐
⏐
⏐
X 2
n
n − 1
∫ 1
0

f ′(
√
n − 2
n Tn−1 + t Xn√ ( n
2
) ) − f ′(
√
n − 2
n Tn−1)

 dt
⏐
⏐
⏐
⏐
⏐
⏐
.
Arguing as in the previous paragraph this is at most B1 + B2 + B3 where
• B1 = 1
n−1
∫ 1
0
3tE(|Xn|3)√
(n
2) dt = 3E(|Xn|3)
2(n−1)
√
(n
2) .
• B2 = 1
n−1
∫ 1
0
2t
√
n−2
n√
(n
2) E(|Tn−1||Xn|3)dt =
√
n−2
n
(n−1)
√
(n
2) E(|Tn−1||Xn|3).
9
• B3 = 1
n−1 E
[
|Xn|3
b
√
(n
2)
∫ 1
0
∫ 1
0 tI[z,z +b](
√
n−2
n Tn−1 + st Xn√
(n
2) )dsdt
]
.
To bound B1, use part 1 of Lemma 2.4 to conclude that B1 ≤ 3√n . To bound
B2, use part 2 of Lemma 2.4 to conclude that B2 ≤ 2√n . To bound B3, one
uses an argument almost identical to that for A3 to conclude that
B3 ≤ E1√n + E2
bn + E3δ(0, n − 1)
b√n
where E1, E 2, E 3 are universal constants.
Summarizing, it has been proved that
δ(b, n ) ≤ C1√n + C2
bn + C3δ(0, n − 1)
b√n
where C1, C 2, C 3 are universal constants. From [Bol] or [Man], δ(0, n ) ≤
δ(b, n ) + b√
2π for all b, which implies that
δ(0, n ) ≤ C1√n + C2
bn + C3δ(0, n − 1)
b√n + b√
2π .
We argue by induction that there is a universal constant C so that δ(0, n ) ≤
C√n for all n. Assuming the result for n − 1, one obtains that
δ(0, n ) ≤ C1√n + C2
bn +
√
3
2
C · C3
bn + b√
2π .
Choosing b = 2C3√n , it follows that if C is suﬃciently large, the induction step
will work for all n. This completes the proof. □
To conclude this section, we note that it would be of interest to prove the
following (more general) conjecture. An error term of O(n−1/ 4) has recently
been established by the method of exchangeable pairs [F4].
Conjecture: Let i ≥ 2 be ﬁxed. Then for all n ≥ i and real x0,
⏐
⏐
⏐
⏐
⏐P
( √
n!
(n − i)!i
χ λ (12 · · · i)
dim(λ) ≤ x0
)
− 1√
2π
∫ x0
−∞
e− t2
2 dt
⏐
⏐
⏐
⏐
⏐ ≤ Cin−1/ 2
where Ci is a constant depending on i.
