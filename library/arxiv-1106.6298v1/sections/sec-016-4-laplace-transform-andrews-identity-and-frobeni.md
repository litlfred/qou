---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-016-4-laplace-transform-andrews-identity-and-frobeni
section_title: "Laplace transform, Andrews identity and Frobenius maps"
section_number: 4
pages: 15-16
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
---
The aim of this section is to deﬁne the Laplace transform and to stud y its image.
4.1. Laplace transform. To deﬁne the uniﬁed invariant we have to compute
∑
n
ξ
qb n2−1
4 A(n, k)
where terms depending on n in A(n, k) look as follows
k∏
i=0
(qn + q−n − qi − q−i) = ( −1)k+1 (qn; q)k+1 (q−n; q)k+1 .
Formally, the last expression can be considered as a Laurent polyno mial in q and qn.
Hence we only have to compute ∑
n
ξ
qb n2−1
4 qna ,
which can be easily done by the square completing argument. Let us s tate the result.
Suppose r is an odd number, b is positive integer and
c := (r, b), b 1 := b/c, r 1 := r/c.
Lemma 10. [Beliakova–Le] One has
(17) γb(ξ) = c γb1(ξc).
(18)
∑
n
ξ
qb n2−1
4 qan =
{
0 if c ∤ a;
(ξc)−a2
1b∗
1 γb(ξ) if a = ca1,
where b∗
1 is an integer satisfying b1b∗
1 ≡ 1 (mod r1).
This computation inspired us to introduce the following operator, ca lled the Laplace
transform. Remember that
∫
eaxk
f (x) dx is called the Laplace transform of f of order k.
Let Lb,c ;n : Z[q±n, q±1] → Z[q±c/b ] be the Z[q±1]–linear operator, called the (discrete)
Laplace transform (of the second order), deﬁned by
(19) Lb,c ;n(qna) :=
{
0 if c ∤ a;
q−a2/b if a = ca1,
Lemma 11. [Beliakova–Le] Suppose f ∈ Z[q±n, q±1]. Then
∑
n
ξ
qb n2−1
4 f = γb(ξ) evξ(Lb,c ;n(f )).
The point is that Lb,c ;n(f ), unlike the left hand side ∑ ξ
nqb n2−1
4 f , does not depend on
ξ. To prove Theorem 5 we need to show that Lb,c ;n((qn; q)k+1 (q−n; q)k+1) is divisible by
(qk+1; q)k+1. For this we use the remarkable identity discovered by Andrews.
16 ANNA BELIAKOV A AND THANG LE
4.2. Andrews identity. To warm up we start with the identity from the Ramanujan
“Lost” Notebook:
∏
k≥1
1
(1 − q5k−4)(1 − q5k−1) =
∑
n≥0
qn2
(1 − q)(1 − q2) . . . (1 − qn)
Only in the 60s, MacMahon gave a combinatorial interpretation of th is identity as follows.
Let λ = ( λ1, λ2, . . . , λt) with ∑
i λi = n be a partition of n into non–increasing integers.
Then the identity can derived from the fact that the number of par titions of n with all λi
of the form 5 k + 1 or 5 k + 4 is equal to the number of partitions where λi − λi+1 ≥ 2 for
all i.
This identity is a very special case of the Andrews identity we used in [ 2]: For any
numbers bi, ci, i = 1, . . . , k and positive integer N we have
1 +
N∑
n=1
qkn+N n(1 + qn) (q−N )n
(qN +1)n
k∏
i=1
(bi)n
bn
i
(ci)n
cn
i
1
( q
bi
)n( q
ci
)n
=
(q)N ( q
bkck
)N
( q
bk
)N ( q
ck
)N
∑
nk≥nk−1≥···≥n2≥n1=0
qnk(q−N )nk(bk)nk(ck)nk
(q−N bkck)nk
k−1∏
i=1
qni (bi)ni
bni
i
(ci)ni
cni
i
( q
bici
)ni+1−ni
(q)ni+1−ni( q
bi
)ni+1( q
ci
)ni+1
where ( a)n = (a; q)n.
The point is that (for a special choice of parameters) the left hand side of the identity
can be identiﬁed with Lb,c ;n ((qn; q)k+1 (q−n; q)k+1), where the right hand side is a sum
with all summands divisible by ( qk+1; q)k+1.
In the case b = ±1, the computations are especially simple and we get that
L−1, 1;n((qn; q)k+1 (q−n; q)k+1) = 2( qk+1; q)k+1 .
The same holds also for L1, 1;n up to units. This allows to write the explicit formula for
IM given in the introduction.
