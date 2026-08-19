---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-042-20-generalization-it-is-clear-that-one-can-deduc
section_title: "Generalization. It is clear that one can deduce (2 .3)N from the more general"
section_number: 20
pages: 35-41
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
identity
∑
n1,...,nk+1
qn2
1+···+n2
k
nk+1∏
m=1
(1 +xqm)(1 +x−1qm−1)
(q)N−n1 (q)n1−n2··· (q)nk−nk+1(q)2nk+1
= 1
(q)2N
∑
m
xmq
1
2 ((2k+3)m2+m)
[
2N
N +m
]
q
. (2.4)
36 Anatol N. Kirillov
Indeed, let us take x =−1 in (2.4). Then the non zero terms in the LHS(2.4) happen to
appear only if nk+1 = 0.
30. Induction. The proof of the identity (2.4) is based on the fo llowing two Lemmas.
Lemma 1 (Classical identities).
i) (q-binomial theorem)
(qx;q)n =
n∑
k=1
(−1)kqk(k+1)xk
[
n
k
]
q
, (2.5)
ii) (Euler identity)
1
(qx;q)n
=
n∑
k=0
[
n
k
]
q
xkqk
(xq;q)k
, (2.6)
iii) (Cauchy identity)
n∑
k=−n
xkq
1
2 k(k+1)
[
2n
n +k
]
q
=
n∏
k=1
(1 +xqk)(1 +x−1qk−1). (2.7)
Lemma 2. Given N∈ N, a∈ C, then
N∑
m=−N
xmqam2
(q)N−m(q)N+m
=
N∑
l=0
ql2
(q)N−l
l∑
n=0
xnq(a−1)n2
(q)l−n(q)l+n
. (2.8)
The statements of Lemma 1 are well-known (see e.g. [An1] or [G R]). Let us prove the
Lemma 2. For this purpose let us take n := N−m, x := q2m in (2.6) and multiply the
both sides of Euler’s identity (2.6) on ( q)−1
2m. We get
(q)−1
n+m =
∑
k
[
n−m
k
]
q
qk2+2km
(q)k+2m
. (2.9)
Now let us substitute the expression for ( q)−1
n+m from (2.9) to the LHS of (2.8):
LHS(2.8) =
∑
m
xmqam2
(q)N−m
∑
k
qk2+2mk(q)N−m
(q)k+2m(q)k(q)N−m−k
=
∑
m,k
q(m+k)2
(q)N−m−k
· xmq(a−1)m2
(q)k(q)k+2m
.
Finally, let us take l :=m +k in the last expression.
Now let us return back to a proving of (2.4). For this purpose w e apply Lemma 2 to
the RHS of (2.4):
RHS(2.4) =
∑
m
(xq
1
2 )mq
1
2 (2k+3)m2
(q)N−m(q)N+m
=
∑
n1
qn2
1
(q)N−n1
∑
m
(xq
1
2 )mq
1
2 (2k+1)m2
(q)n1−m(q)n1+m
=... k times... =
∑
n1,...,nk+1
qn2
1+···+n2
k+1
(q)N−n1 (q)n1−n2... (q)nk−nk+1
∑
m
(xq
1
2 )mq
1
2 m2
(q)nk+1−m(q)nk+1+m
.
Now let us apply the Cauchy identity (2.6) to simplify the sum overm. The result is the
LHS(2.4), as we set out to prove.
Dilogarithm identities 37
2.1.2. Partitions.
Let us consider the following classes of partitions:
Ak,n,a =
{
(m1,...,m p)∈ Zp
+
⏐
⏐
⏐ m1≥... ≥mp≥ 1, m i−mi+k≥ 2, i +k≤p,∑ mi =n, and at most a− 1 of bi equal 1
}
,
Bk,n,a =
{
(r1,...,r s)∈ Zs
+
⏐
⏐
⏐ ri = 0, if i≡ 0,±a(mod (2k + 3)),
∑
iri =n
}
,
Cn,k,a =
{
(f1,...,f l)∈ Zl
+|
∑
jfj =n, f1≤a− 1, fj +fj+1≤k, ∀j
}
,
Dk,n,a =
{
(λ1,...,λ r)∈ Zr
+|λ⊢n; if λj≥j then −a + 2≤λj−λ′
j≤ 2k−a + 1
}
.
Lemma 3.
∑
n
#|Ak,n,a|qn = LHS of Gordon − Andrews′ identity,
∑
n
#|Bk,n,a|qn = RHS of Gordon − Andrews′ identity.
Proof. The second statement of Lemma 3 is clear. Let us prove t he ﬁrst one for k = 1 and
a = 2. In fact, we are going to prove a slightly more general resu lt (k = 1,a = 2). Namely,
let us consider the set
Cd
1,N =
{
(m1,...,m p)∈ Zp
+
⏐
⏐
⏐
⏐
⏐
m1≥m2≥···≥ mp≥d,
mi−mi+1≥d, if i + 1≤p, ∑ mi =N
}
.
Then
∑
n≥0
qdn2
(q)n
=
∑
(m)∈Cd
1,N
q
∑
mi.
Indeed, one can check
∑
n≥0
qdn2
(1−q)... (1−qn) =
∑
{ki≥0}
qdn2+k1+2k2+···+nkn. (2.10)
Now let us consider the collection of integer numbers {ki≥ 0}n
i=1 appearing in the RHS
of (2.10) and deﬁne the partition m = (m1,m 2,...,m n) by the following rules
m1 =d(2n− 1) +k1 +... +kn, m 2 =d(2n− 3) +k2 +... +kn, ...,
mi =d(2n− 2i + 1) +ki +...,k n, ..., m n =d +kn, N =m1 +··· ,m n.
It is easy to check that the partition m constructed by this way belongs to the set Cd
1,N
and vice versa.
38 Anatol N. Kirillov
Theorem D. (A. Garsia and S. Milne [GM], W. Burge [Bur]). There exist the natural
bijections
Ak,n,a←→Bk,n,a←→Ck,n,a←→Dk,n,a.
From Theorem D there follows a combinatorial proof of the Gor don-Andrews identity.
Remark. Bijection Ak,n,a↔ Ck,n,a is obvious; bijection Ck,n,a ↔ Dk,n,a was con-
structed by W. Burge (see e.g. [Bur]). Further information c an be found in Exercise 7.
Example.
A2,6,3 ={ (3, 2, 1), (4, 1, 1), (6), (5, 1), (4, 2), (3, 3)},
B2,6,3 ={ (16), (2, 14), (22, 12), (23), (5, 1), (6)},
C2,6,3 ={ (4, 12), (32), (3, 2, 1), (4, 2), (5, 1), (6)},
D2,6,3 ={ (3, 1, 1, 1), (4, 1, 1), (3, 2, 1), (2, 2, 2), (3, 3), (4, 2)}.
The next step (S. Ramanujan, G. Hardy, G. Meinardus, G. Andre ws, B. Richmond,
G. Szekeres, TBA (Thermodynamic Bethe’s Ansatz, Al. Zamolo dchikov, ...) ...) is to
examine the asymptotic behavior of the numbers # |Ck,n,a| and #|Bk,n,a| asn→∞ . It is
well known from the theory of partitions (see e.g. [An1]) tha t if we introduce the partition
function p(n) using the expansion of the generating function
∞∑
n=0
p(n)qn =
∞∏
n=1
(1−qn)−1,
then logp(n) = π
√
2n
3 +o(√n) (more exactly, p(n)∼ 1
4n
√
3 exp
(
π
√
2n
3
)
).
Consequently,
log(#|Bk,n,a|) = π
√
2k
2k + 3·
√
2n
3 +o(√n).
In order to ﬁnd the asymptotic behavior of log(# |Ck,n,a|) as n→ +∞ one can use the
saddle point method.
Lemma 4. Assume that
∑
n=(n1,...,nk)∈Zk
+
qnBnt
(q)n1... (q)nk
=
∞∑
N=0
aNqN, (2.11)
whereB is a symmetric and positively deﬁnite rational matrix. Then
log2aN = 4N
k∑
i=1
L(zi) +o(N ),
Dilogarithm identities 39
wherezi, 1≤i≤k, satisfy the following system of algebraic equations
zi =
k∏
j=1
(1−zj)2Bij.
Proof. Using Cauchy’s theorem, aN−1 can be expressed as the integral
aN−1 =
∑
n=(n1,...,nk)
∮ qnBnt−N
(q)n1··· (q)nk
. (2.12)
In the sequel we are follow to the paper [RS] (see also [NRT], [ Tr2], [DKMM]). In order to
analyze the behavior of the integral (1.12), we are going to u se the saddle point approxi-
mation, i.e. a crude estimate of the integral can be obtained from the integrand evaluated
at its saddle point. First of all, we rewrite each summand of ( 2.12) in the exponential form
exp((nBnt−N ) logq−
k∑
j=1
nk∑
i=1
log(1−qi)). (2.13)
Using the Euler-Maclaurin formula, we ﬁrst approximate
log(q)nk =
nk∑
i=1
log(1−qi)≃
∫ nk
0
log(1−qt)dt. (2.14)
Hence, we replace (2.13) on
exp((nBnt−N ) logq−
k∑
j=1
∫ nk
0
log(1−qt)dt). (2.15)
Furthermore, we replace the summation in (2.12) by the integ ration over dn, treating the
ni’s as continuous variables, so that the RHS of (2.12) is appro ximately given by
∮ dq
2πi
∫
dn exp(F (q,n )), (2.16)
whereF (q,n ) = (nBnt−N ) logq−
k∑
j=1
∫ nj
0
log(1−qt)dt. Now the saddle point conditions
with respect to n, namely, ∂niF (q,n ) = 0, 1 ≤i≤k, give the set of constraints
2(nB)i logq− log(1−qni ) = 0. (2.17)
If we put xi :=qni, then we obtain a system of algebraic equations on xi:
1−xi =
k∏
j=1
x2Bij
j . (2.18)
40 Anatol N. Kirillov
Further, the value of the function F (q,n ) at the critical point x = (x1,...,x k) can be
found using the formulae:
∫ ni
0
dt log(1−qt)
z=qt
= 1
logq
∫ xi
1
log(1−z)dz
z = 1
logq{Li2(1−xi) + logxi· log(1−xi)}
(hint : Li2(x) +Li2(1−x) = L(1)− logx log(1−x), L.Euler);
nBnt logq = 1
2 logq
∑
i
logxi· log(1−xi).
The result is
F (q,n crit) =−N logq− 1
logq
k∑
j=1
L(1−xj).
Now the equation ∂qF (q,n crit) = 0 ﬁxes q at the saddle point
(logq)2 = 1
N
k∑
j=1
L(1−xj),
so that ﬁnally, the asymptotic behavior of aN is given by
aN∼ exp{2(N
k∑
j=1
L(1−xj))
1
2}.
Now if we put zj := 1−xj, then zj satisfy the following system of algebraic equations
zi =
n∏
j=1
(1−zj)2Bij.
Corollary 4 ( L. Lewin, B. Richmond, G. Szekeres, A.N. Kirillov, N. Reshe tikhin ).
k∑
n=1
L








sin π
k + 2
sin (n + 1)π
k + 2




2


 = 3k
k + 2· π2
6 .
The interesting applications of the Corollary 4 to the study of thermodynamic proper-
ties of the XXX model one can ﬁnd in [KR1] and [BR].
Dilogarithm identities 41
Exercises to Section 2.1.
