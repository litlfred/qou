---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-137-5-initiation-of-the-burgess-argument
section_title: "Initiation of the Burgess argument"
section_number: 5
pages: 265-269
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
We now derive the ﬁrst steps of the Burgess method, generalizing the approach of [Gallagher and Mont-
gomery 2010; Heath-Brown 2013] from the one-variable case and [Pierce 2016] in the multi-variable case.
The central complications that are distinctive to our new stratiﬁed setting are mainly addressed in Section 6.
We make the observation that given a character sum S(F; N, H) with data F, N, H, we may reorder
the variables x1,..., xn so that the lengths H1,..., Hn satisfy
H1≤ H2≤···≤ Hn. (5-1)
1932 Lillian B. Pierce and Junyan Xu
In particular, if the reduction of F modulo q is(1, q)-admissible, then it stays(1, q)-admissible after
any reordering of the variables (Lemma 3.5). We will assume (5 -1) from now on, and will prove the
statement of Theorem 1.1 with H1= Hmin and Hn= Hmax.
Fix a prime p ∤ q such that p≤ Hmin, and split each coordinate xi∈(Ni, Ni+ Hi] into residue classes
modulo p by writing x= qa+ pm with a, m∈ Zn, where 0≤ ai< p and mi∈(N′
i, N′
i+ H′
i], for which
we deﬁne
N′
i=(Ni− aiq)/p, H′
i= Hi/p
for each i= 1,..., n. Then
S(F; N, H)=
∑
a(mod p)
∑
m∈(N′,N′+H′]
χ( F(qa+ pm)).
By the fact thatχ has period q, the homogeneity of F and the multiplicativity ofχ,
S(F; N, H)=χ( pD)
∑
a(mod p)
∑
m∈(N′,N′+H′]
χ( F(m)),
so that
|S(F; N, H)|≤
∑
a(mod p)
|S(F; N′, H′)|.
We now average over a set P of primes, P={ P< p≤ 2P: p ∤ q}, so that|P|≫ P(log P)−1. We will
later choose P so that
P≤ Hi, 1≤ i≤ n. (5-2)
Then
|S(F; N, H)|≤ 1
|P|
∑
p∈P
∑
a(mod p)
|S(F; N′, H′)|. (5-3)
Here we recall that N′ and H′ depend on a and p. We now average over the starting points N′ and the
lengths H′ in order to make them independent of a, p.
Lemma 5.1. Fix M∈ Rn and L∈ Rn
≥1. For any K≤ L,
|S(F; M, K)|≤ 22n‖L‖−1 ∑
m∈(M−L,M]
max
k≤2L
|S(F; m, k)|.
Proof. The ﬁrst observation is that for any ﬁxed M, K, and any ﬁxed m with mi≤ Mi for all i= 1,..., n,
S(F; M, K)=
∑
δ=(δ1,...,δn)
δi∈{0,1}
(−1)σ(δ)S(F; m, M− m+(1−δ)· K), (5-4)
whereσ(δ)=∑
iδi. We will prove this momentarily, but ﬁrst we see how it implies Lemma 5.1. For any
Ki≤ Li, and any mi with Mi− Li< mi≤ Mi, we have
0≤ Mi− mi+(1−δi)Ki≤ 2Li,
Burgess bounds for short character sums evaluated at forms 1933
for either choice ofδi∈{ 0, 1}. Hence for any m with M− L≤ m≤ M, (5-4) shows that
|S(F; M, K)|≤ 2n max
k≤2L
|S(F; m, k)|. (5-5)
There are at least Li/2 integers with Mi− Li< mi≤ Mi, so that there are at least 2−n‖L‖ values m in
the range M− L< m≤ M, and the lemma now follows by averaging (5-5) over these values.
Finally, we prove (5-4). This is simple to see in the case of dimension n= 1: for any m1≤ M1, we
observe that as intervals,
(M1, M1+ K1]= (m1, M1+ K1]\(m1, M1].
Thus in terms of the sums over these intervals,
S(F; M1, K1)= S(F; m1, M1− m1+ K1)− S(F, m1, M1− m).
For general dimensions n≥ 1, (5-4) follows from the principle of inclusion-exclusion. Explicitly, the sum
S(F; M, K) has a range of summation over the box W:=∏n
i=1(Mi, Mi+ Ki]. Temporarily, for ease of
notation, let S(W) denote this sum, with range of summation over the box W ; similarly, given any box W′
deﬁned below, we will let S(W′) denote the corresponding sum, with range of summation over the box W′.
Suppose m≤ M is ﬁxed. Let W∗ be the larger box W∗:=∏n
i=1(mi, Mi+ Ki]. For each j= 1,..., n,
let W( j) be the box deﬁned as a product of intervals for 1≤ i≤ n, with “short” interval(m j, M j] in the
j-th coordinate and “long” interval(mi, Mi+ Ki] in every other coordinate, for i⁄= j. For each j let
W( j) be the complement of W( j) inside W∗. Precisely, W( j) is a product of intervals for 1≤ i≤ n, with
interval(M j, M j+ K j] in the j-th coordinate and interval (mi, Mi+ Ki] for i⁄= j. Observe that our
box W of interest is W=⋂n
i=1 W( j). Then by the principle of inclusion-exclusion,
S(W)= S(W∗)−
n∑
i=1
S(W( j))+
∑
1≤ j1< j2≤n
S(W( j1)∩ W( j2))+···+ (−1)n S(W(1)∩ W(2)∩···∩ W(n)).
We can recognize that this is the identity (5 -4) as follows. First, on the left-hand side, S(W) is by
deﬁnition our desired sum S(F; M, K). Next, we observe that the entries on the right-hand side are in
bijection with the entries on the right-hand side of (5-4). Precisely, ﬁx a tuple(δ1,...,δ n) withδi∈{ 0, 1}.
Suppose that this tuple has k entries of 1, occurring at the indices j1,..., jk. If k= 0 then in the notation
of the identity (5-4), the sum S(F; m, M−m+(1−δ)· K) is precisely the sum S(W∗). If 1≤ k≤ n, then
S(F; m, M− m+(1−δ)· K) is precisely S(W( j1)∩···∩ W( jk)) appearing in the inclusion-exclusion
identity above. In each case, the signs (−1)σ(δ)=(−1)k agree as well. □
We apply Lemma 5.1 to (5-3) with Li= Hi/P≥ 1. We obtain
|S(F; N, H)|≤| P|−1∑
p∈P
∑
a(mod p)
22n‖H‖−1 Pn ∑
m∈(N′−H/P,N′]
max
k≤2H/P
|S(F; m, k)|. (5-6)
1934 Lillian B. Pierce and Junyan Xu
After rearranging,
|S(F; N, H)|≤| P|−122n‖H‖−1 Pn ∑
m
A(m) max
k≤2H/P
|S(F; m, k)|, (5-7)
where we have deﬁned
A(m)= #
{
a, p: p∈ P, a=(a1,..., an), 0≤ ai< p: Ni− aiq
p − Hi
P < mi≤ Ni− aiq
p , i= 1,..., n
}
.
We record the following facts about A(m), whose proof we defer to Section 7B.
Lemma 5.2. The quantity A(m) vanishes unless m satisﬁes|mi|≤ 2q for each i. Moreover , if
Hi P< q, 1≤ i≤ n, (5-8)
then ∑
m
A(m)≪ P‖H‖,
∑
m
A(m)2≪ P‖H‖.
Applying Hölder’s inequality twice to (5-7), we obtain
|S(F; N, H)|
≪| P|−1‖H‖−1 Pn
(∑
m
A(m)
)1−1/r(∑
m
A(m)2
)1/(2r)( ∑
m
|mi|≤2q
max
k≤2H/P
|S(F; m, k)|2r
)1/(2r)
.
Thus applying the results of Lemma 5.2 shows that
|S(F; N, H)|≪ (log P)Pn−1/2r‖H‖−1/2r
( ∑
m
|mi|≤2q
max
k≤2H/P
|S(F; m, k)|2r
)1/(2r)
. (5-9)
It is sufﬁcient to look at the internal sum over m modulo q; in fact obtaining this complete character sum
is the main accomplishment of the manipulations up to this point.
We ignore for the moment the maximum over k≤ 2H/P and focus ﬁrst on estimating the nonmaximal
moment. We rewrite S(F; m, k) as
S(F; m, k)=
∑
x∈(m,m+k]
χ( F(x))=
∑
x∈(0,k]
χ( F(m+ x)),
so that upon expansion,
∑
m(mod q)
|S(F; m, k)|2r=
∑
m(mod q)
⏐⏐⏐
∑
x∈(0,k]
χ( F(m+ x))
⏐⏐⏐
2r
≤
∑
x(1),...,x(2r)
x(i)∈(0,k]
⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐, (5-10)
where F{x} is deﬁned in terms of the original form F and the collection{x(1),..., x(2r)} by (2-6).
Burgess bounds for short character sums evaluated at forms 1935
6. Stratiﬁcation and a Menshov–Rademacher argument
6A. Application of the stratiﬁcation for character sums. We now come to a critical novel step, which
is to estimate how often we obtain a certain quality of upper bound for the complete character sum
∑
m(mod q)
χ( F{x}(m)).
For this, we call upon the stratiﬁcation of complete character sums stated in Theorem 4.4. Let us suppose
that k1≤... ≤ kn≤ q. For each 1≤ j≤ n, deﬁne
Y j:=
{
{x}∈ (0, k]2r:
⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐> Cq(n+ j−1)/2
}
,
in which C= C(n, r, D) is the constant provided by Theorem 4.4. Then by Theorem 4.4, we have
(0, k]2r=: Y0⊃ Y1⊃ Y2⊃···⊃ Yn⊃ Yn+1:= ∅, and #Y j≤ C′′‖k‖2r Bn,r( j; k)−1. Upon employing the
decomposition(0, k]2r=∐n
j=0 Y j\ Y j+1 in (5-10) we have
∑
m(mod q)
|S(F; m, k)|2r≤
n∑
j=0
∑
{x}∈Y j\Y j+1
⏐⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐⏐ (6-1)
≤
n∑
j=0
(#Y j)Cq(n+( j+1)−1)/2
≤ C· C′′‖k‖2r
n∑
j=0
q(n+ j)/2Bn,r( j; k)−1.
To summarize, we have proved:
Lemma 6.1. Fix n, r, D,1≥ 1, a prime q, and a multiplicative Dirichlet character χ of order 1
modulo q. Then for every form F∈ Z[X1,..., Xn] of degree D such that its reduction modulo q is
(1, q)-admissible, the following holds. For every k=(k1,..., kn) with 1≤ k1≤ k2≤···≤ kn≤ q, then
∑
m (mod q)
|S(F; m, k)|2r≪n,r,D,1‖k‖2r
n∑
j=0
q(n+ j)/2Bn,r( j; k)−1, (6-2)
with Bn,r( j; k) as deﬁned in (4-5), and with the implicit constant dependent on n, r, D,1 but independent
of q,χ, F, k.
However recall that the actual quantity we must bound in (5 -9) is a moment of |S(F; m, k)| that
includes a maximum over k≤ 2H/P. To do so, we will employ a Menshov–Rademacher argument.
