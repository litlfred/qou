---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-007-21-dilogarithm-and-partitions
section_title: "Dilogarithm and partitions."
section_number: 2.1
pages: 34-53
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
2.1.1. Rogers-Ramanujan and Gordon-Andrews identities
Theorem C. Let a be an integer, 1 ≤a ≤k + 1. Then
i) (Gordon-Andrews)
X
n1,...,nk
qN2
1 +...+N2
k+Na+...+Nk
(q)n1 . . . (q)nk
=
Y
n̸≡0, ±a mod (2k+3)
(1 −qn)−1 =
(2.1.a)
= (q)−1
∞
X
m∈Z
(−1)mq
1
2 [m(m+1)(2k+3)−am],
(2.1.b)
ii) (G¨ollnitz-Gordon-Andrews)
X
n1,...,nk
(−q; q2)N1qN2
1 +N2
2 +···+N2
k+Na+...+Nk
(q2; q2)n1 . . . (q2; q2)nk
=
Y
n̸ ≡2(mod 4)
n̸ ≡0, ±(2a −1) (mod 4k + 4)
(1 −qn)−1,
(2.2)
Dilogarithm identities
35
where Ni = ni + . . . + nk, (q)n := (q; q)n and (x; q)n = (1 −x)(1 −qx) · · ·(1 −qn−1x).
The Rogers-Ramanujan identities correspond to k = 1, a = 1, or 2 in (2.1a).
Note that the second equality (2.1.b) follows from the Jacobi triple-product formula
m∈Z
xmq
1
2 m(m+1) =
Y
m≥1
(1 −qm)(1 + xqm)(1 + x−1qm−1),
which follows from the Cauchy identity (2.6) after passing to the limit N →∞.
There exist essentially four methods of proving the partition identities of Gordon-
Andrews’ type, namely, analytical one, using the transformation properties of q-series
(L. Rogers, G. Watson, I. Schur, W. Bailey, L. Slater, G. Andrews, D. Bressoud, J. Stem-
bridge, ...), algebraic one, based on the recurrence relations technique (L. Rogers, S. Ra-
manujan, G. Andrews, R. Baxter, P. Forrester, ...), combinatorial one, based on an ex-
plicit construction of a bijection between some sets of partitions (F. Franklin, G. Andrews,
W. Durfee, A. Garsia, S. Milne, D. Bressoud, W. Burge, ...) and group-theoretical one,
based on an investigation of the (integrable) highest-weight modules over the Kac-Moody
or Virasoro algebras and the Weyl-Kac character formula (I. Macdonald, A. Feingold,
J. Lepowsky, R. Wilson, M. Primc, V. Kac, S. Milne, B. Feigin, D. Fuchs, E. Frenkel, ...).
We give here an analytical proof of (2.1) due to D. Bressoud [Bre2].
Proof of the Gordon-Andrews identity (for a = k + 1).
It is convenient to divide the proof into three steps.
10. Reduction to ﬁnite dimensional (polynomial) case. Note that it is suﬃcient to
prove the following polynomial identity (ﬁnite dimensional analog of (2.1))
(q)N
X
n1,...,nk
qn2
1+···+n2
k

2N
N −n1, n1 −n2, . . ., nk−1 −nk, nk

q
=
X
m
(−1)mq
1
2 ((2k+3)m2+m)

2N
N + m

q
,
(2.3)N
where

M
m1, . . ., mk

q
:=
(q)M
(q)m1 . . . , (q)mk(q)M−m1−...−mk
is the q-analog of multinomial
coeﬃcient.
Indeed, it is easy to check that
lim
N→∞(2.3)N = (2.1.b).
20.
Generalization.
It is clear that one can deduce (2.3)N from the more general
identity
X
n1,...,nk+1
qn2
1+···+n2
k
nk+1
Y
m=1
(1 + xqm)(1 + x−1qm−1)
(q)N−n1(q)n1−n2 · · · (q)nk−nk+1(q)2nk+1
=
1
(q)2N
X
m
xmq
1
2 ((2k+3)m2+m)

2N
N + m

q
.
(2.4)
36
Anatol N. Kirillov
Indeed, let us take x = −1 in (2.4). Then the non zero terms in the LHS(2.4) happen to
appear only if nk+1 = 0.
30. Induction. The proof of the identity (2.4) is based on the following two Lemmas.
Lemma 1 (Classical identities).
i) (q-binomial theorem)
(qx; q)n =
n
X
k=1
(−1)kqk(k+1)xk

n
k

q
,
(2.5)
ii) (Euler identity)
1
(qx; q)n
=
n
X
k=0

n
k

q
xkqk
(xq; q)k
,
(2.6)
iii) (Cauchy identity)
n
X
k=−n
xkq
1
2 k(k+1)

2n
n + k

q
=
n
Y
k=1
(1 + xqk)(1 + x−1qk−1).
(2.7)
Lemma 2. Given N ∈N, a ∈C, then
N
X
m=−N
xmqam2
(q)N−m(q)N+m
=
N
X
l=0
ql2
(q)N−l
l
X
n=0
xnq(a−1)n2
(q)l−n(q)l+n
.
(2.8)
The statements of Lemma 1 are well-known (see e.g. [An1] or [GR]). Let us prove the
Lemma 2. For this purpose let us take n := N −m, x := q2m in (2.6) and multiply the
both sides of Euler’s identity (2.6) on (q)−1
2m. We get
(q)−1
n+m =
X
k

n −m
k

q
qk2+2km
(q)k+2m
.
(2.9)
Now let us substitute the expression for (q)−1
n+m from (2.9) to the LHS of (2.8):
LHS(2.8) =
X
m
xmqam2
(q)N−m
X
k
qk2+2mk(q)N−m
(q)k+2m(q)k(q)N−m−k
=
X
m,k
q(m+k)2
(q)N−m−k
· xmq(a−1)m2
(q)k(q)k+2m
.
Finally, let us take l := m + k in the last expression.
Now let us return back to a proving of (2.4). For this purpose we apply Lemma 2 to
the RHS of (2.4):
RHS(2.4) =
X
m
(xq
1
2 )mq
1
2 (2k+3)m2
(q)N−m(q)N+m
=
X
n1
qn2
1
(q)N−n1
X
m
(xq
1
2 )mq
1
2 (2k+1)m2
(q)n1−m(q)n1+m
= . . .
k times . . . =
X
n1,...,nk+1
qn2
1+···+n2
k+1
(q)N−n1(q)n1−n2 . . . (q)nk−nk+1
X
m
(xq
1
2 )mq
1
2 m2
(q)nk+1−m(q)nk+1+m
.
Now let us apply the Cauchy identity (2.6) to simplify the sum over m. The result is the
LHS(2.4), as we set out to prove.
Dilogarithm identities
37
2.1.2. Partitions.
Let us consider the following classes of partitions:
Ak,n,a =

(m1, . . ., mp) ∈Zp
+

 m1 ≥. . . ≥mp ≥1,
mi −mi+k ≥2,
i + k ≤p,
P mi = n,
and at most a −1 of bi equal 1

,
Bk,n,a =
n
(r1, . . ., rs) ∈Zs
+

 ri = 0, if i ≡0, ±a(mod (2k + 3)),
X
iri = n
o
,
Cn,k,a =
n
(f1, . . ., fl) ∈Zl
+ |
X
jfj = n, f1 ≤a −1, fj + fj+1 ≤k, ∀j
o
,
Dk,n,a =

(λ1, . . ., λr) ∈Zr
+ | λ ⊢n; if λj ≥j then −a + 2 ≤λj −λ′
j ≤2k −a + 1
	
.
Lemma 3.
X
n
#|Ak,n,a|qn = LHS of Gordon −Andrews′ identity,
X
n
#|Bk,n,a|qn = RHS of Gordon −Andrews′ identity.
Proof. The second statement of Lemma 3 is clear. Let us prove the ﬁrst one for k = 1 and
a = 2. In fact, we are going to prove a slightly more general result (k = 1, a = 2). Namely,
let us consider the set
Cd
1,N =
(
(m1, . . ., mp) ∈Zp
+

m1 ≥m2 ≥· · · ≥mp ≥d,
mi −mi+1 ≥d,
if i + 1 ≤p,
P mi = N
)
.
Then
X
n≥0
qdn2
(q)n
=
X
(m)∈Cd
1,N
q
P
mi.
Indeed, one can check
X
n≥0
qdn2
(1 −q) . . .(1 −qn) =
X
{ki≥0}
qdn2+k1+2k2+···+nkn.
(2.10)
Now let us consider the collection of integer numbers {ki ≥0}n
i=1 appearing in the RHS
of (2.10) and deﬁne the partition m = (m1, m2, . . . , mn) by the following rules
m1 = d(2n −1) + k1 + . . . + kn,
m2 = d(2n −3) + k2 + . . . + kn,
. . . ,
mi = d(2n −2i + 1) + ki + . . . , kn,
. . . ,
mn = d + kn,
N = m1 + · · · , mn.
It is easy to check that the partition m constructed by this way belongs to the set Cd
1,N
and vice versa.
38
Anatol N. Kirillov
Theorem D. (A. Garsia and S. Milne [GM], W. Burge [Bur]). There exist the natural
bijections
Ak,n,a ←→Bk,n,a ←→Ck,n,a ←→Dk,n,a.
From Theorem D there follows a combinatorial proof of the Gordon-Andrews identity.
Remark. Bijection Ak,n,a ↔Ck,n,a is obvious; bijection Ck,n,a ↔Dk,n,a was con-
structed by W. Burge (see e.g. [Bur]). Further information can be found in Exercise 7.
Example.
A2,6,3 = { (3, 2, 1), (4, 1, 1), (6), (5, 1), (4, 2), (3, 3) },
B2,6,3 = { (16), (2, 14), (22, 12), (23), (5, 1), (6) },
C2,6,3 = { (4, 12), (32), (3, 2, 1), (4, 2), (5, 1), (6) },
D2,6,3 = { (3, 1, 1, 1), (4, 1, 1), (3, 2, 1), (2, 2, 2), (3, 3), (4, 2) }.
The next step (S. Ramanujan, G. Hardy, G. Meinardus, G. Andrews, B. Richmond,
G. Szekeres, TBA (Thermodynamic Bethe’s Ansatz, Al. Zamolodchikov, ...) ...) is to
examine the asymptotic behavior of the numbers #|Ck,n,a| and #|Bk,n,a| as n →∞. It is
well known from the theory of partitions (see e.g. [An1]) that if we introduce the partition
function p(n) using the expansion of the generating function
∞
n=0
p(n)qn =
∞
Y
n=1
(1 −qn)−1,
then log p(n) = π
r
2n
3 + o(√n) (more exactly, p(n) ∼
1
4n
√
3 exp
 
π
r
2n
3
!
).
Consequently,
log(#|Bk,n,a|) = π
r
2k
2k + 3 ·
r
2n
3 + o(√n).
In order to ﬁnd the asymptotic behavior of log(#|Ck,n,a|) as n →+∞one can use the
saddle point method.
Lemma 4. Assume that
X
n=(n1,...,nk)∈Zk
+
qnBnt
(q)n1 . . . (q)nk
=
∞
X
N=0
aNqN,
(2.11)
where B is a symmetric and positively deﬁnite rational matrix. Then
log2 aN = 4N
k
X
i=1
L(zi) + o(N),
Dilogarithm identities
39
where zi,
1 ≤i ≤k, satisfy the following system of algebraic equations
zi =
k
j=1
(1 −zj)2Bij.
Proof. Using Cauchy’s theorem, aN−1 can be expressed as the integral
aN−1 =
X
n=(n1,...,nk)
I
qnBnt−N
(q)n1 · · ·(q)nk
.
(2.12)
In the sequel we are follow to the paper [RS] (see also [NRT], [Tr2], [DKMM]). In order to
analyze the behavior of the integral (1.12), we are going to use the saddle point approxi-
mation, i.e. a crude estimate of the integral can be obtained from the integrand evaluated
at its saddle point. First of all, we rewrite each summand of (2.12) in the exponential form
exp((nBnt −N) log q −
k
X
j=1
nk
X
i=1
log(1 −qi)).
(2.13)
Using the Euler-Maclaurin formula, we ﬁrst approximate
log(q)nk =
nk
X
i=1
log(1 −qi) ≃
Z nk
0
log(1 −qt)dt.
(2.14)
Hence, we replace (2.13) on
exp((nBnt −N) log q −
k
X
j=1
Z nk
0
log(1 −qt)dt).
(2.15)
Furthermore, we replace the summation in (2.12) by the integration over dn, treating the
ni’s as continuous variables, so that the RHS of (2.12) is approximately given by
I
dq
2πi
Z
dn exp(F(q, n)),
(2.16)
where F(q, n) = (nBnt −N) log q −
k
X
j=1
Z nj
0
log(1−qt)dt. Now the saddle point conditions
with respect to n, namely, ∂niF(q, n) = 0, 1 ≤i ≤k, give the set of constraints
2(nB)i log q −log(1 −qni) = 0.
(2.17)
If we put xi := qni, then we obtain a system of algebraic equations on xi:
1 −xi =
k
Y
j=1
x2Bij
j
.
(2.18)
40
Anatol N. Kirillov
Further, the value of the function F(q, n) at the critical point x = (x1, . . ., xk) can be
found using the formulae:
Z ni
0
dt log(1 −qt)
z=qt
=
1
log q
Z xi
1
log(1 −z)dz
z =
1
log q {Li2(1 −xi) + log xi · log(1 −xi)}
(hint :
Li2(x) + Li2(1 −x) = L(1) −log x log(1 −x),
L.Euler);
nBnt log q =
1
2 log q
X
i
log xi · log(1 −xi).
The result is
F(q, ncrit) = −N log q −
1
log q
k
X
j=1
L(1 −xj).
Now the equation ∂qF(q, ncrit) = 0 ﬁxes q at the saddle point
(log q)2 = 1
N
k
X
j=1
L(1 −xj),
so that ﬁnally, the asymptotic behavior of aN is given by
aN ∼exp{2(N
k
X
j=1
L(1 −xj))
1
2 }.
Now if we put zj := 1 −xj, then zj satisfy the following system of algebraic equations
zi =
n
Y
j=1
(1 −zj)2Bij.
Corollary 4 ( L. Lewin, B. Richmond, G. Szekeres, A.N. Kirillov, N. Reshetikhin ).
k
X
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
sin
π
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
=
3k
k + 2 · π2
6 .
The interesting applications of the Corollary 4 to the study of thermodynamic proper-
ties of the XXX model one can ﬁnd in [KR1] and [BR].
Dilogarithm identities
41
Exercises to Section 2.1.
1. Using the Jacobi triple product identity, prove
i) (Euler’s pentagonal number theorem)
∞
Y
n=1
(1 −qn) =
X
m∈Z
(−1)mq
1
2 m(3m−1).
ii) (Gauss’ identities)
X
n∈Z
(−1)nqn2 =
∞
Y
m=1
1 −qm
1 + qm ,
∞
X
n=0
q
n(n+1)
2
=
∞
Y
m=1
1 −q2m
1 −q2m−1 .
iii) (Gauss’ identity)
∞
Y
n=1
(1 −qn)3 =
X
m≥0
(−1)m(2m + 1)q
m(m+1)
2
.
More generally, [FeSt], (we use the notation of Section 2.2)
X
n=(na)∈Z2(k−1)
+
q
1
2 n(A2⊗T −1
k−1)nt
Y
a
(q)na
=
1
(q)3∞
X
n∈Z
((2k + 2)n + 1)q(k+1)n2+n.
(1)
The Gauss identity iii) corresponds to k = 1. If k = 2, then (1) takes the form
X
m∈Z
qm2 =
1
(q)2∞
 X
m∈Z
(6m + 1)q3m2+m
!
.
Proofs and further details see in [FeSt].
iv) (Problem). Find a polynomial analog for the identity (1) (compare with Exercise 5).
2. Prove a q-analog of the binomial series
∞
X
n=0
(a; q)nzn
(q; q)n
= (az; q)∞
(z; q)∞
,
|z| < 1, |q| < 1.
(E. Heine, 1847)
Hint: both sides satisfy the functional equation (1 −z)f(z) = (1 −az)f(qz).
42
Anatol N. Kirillov
3. Using the result of Exercise 2, prove the Ramanujan
1ψ1 summation formula
X
n∈Z
(a; q)nzn
(b; q)n
= (b/a; q)∞(az; q)∞(q/az; q)∞(q; q)∞
(q/a; q)∞(b/az; q)∞(b; q)∞(z; q)∞
.
(S. Ramanujan, 1915)
4. Deduce from Ramanujan’s
1ψ1-summation formula the following identities
i)
X
n∈Z
(−1)nq
n(n−1)
2
zn
(b; q)n
= (z; q)∞(q/z; q)∞(q; q)∞
(b/z; q)∞(b; q)∞
.
ii) (Gauss-Jacobi’s identity)
X
k∈Z
(−1)kz
k(k+1)
2
1
z
k(k−1)
2
2
=
Y
n≥1
(1 −zn
1 zn
2 )(1 −zn
1 zn−1
2
)(1 −zn−1
1
zn
2 ).
iii) (Watson’s identity)
X
k∈Z
z
3k2+k
2
1

z3k2−2k
1
−z3k2−4k+1
2

=
=
Y
n≥1
(1 −zn
1 z2n
2 )(1 −zn
1 z2n−1
2
)(1 −zn−1
1
z2n−1
2
)(1 −z2n−1
1
z4n−4
2
)(1 −z2n−1
1
z4n
2 ).
(G. Watson, 1928)
iv) (Kac-Van der Leur-Wakimoto’s identity, [KW3])
1
(q)2∞
 
∞
X
m,n=0
−
−∞
X
m,n=−1
!
xnymqmn =
(xy)∞(qx−1y−1)∞
(x)∞(y)∞(qx−1)∞(qy−1)∞
.
Hint: consider the Laurent series F1(x, y) = (q)2
∞·RHS and F2(x, y) = (q)2
∞·LHS. Show
that these series satisfy the same functional equations (i = 1, 2)
Fi(qx, y) = y−1Fi(x, y),
Fi(x, qy) = x−1Fi(x, y).
v) (Problem) Find the polynomial analog for Watson’s and Kac-Van der Leur-Wakimoto’s
identities.
5. Let [x] denote the largest integer ≤x. Prove
i) (Polynomial analog of Euler’s pentagonal number theorem)
X
k∈Z
(−1)kq
k(3k−1)
2


N
N + 1 −3k
2



q
= 1,
N ∈Z+.
(I. Schur, 1917)
ii) (Polynomial analog of Rogers-Ramanujan’s identities, a = 0 or 1).
X
j≥0
qj2+aj

N −a −j
j

q
=
X
k∈Z
(−1)kq
1
2 k(5k+1)−2ak


N
1
2(N −5k) + a


q
.
(I. Schur, 1917; G. Andrews, 1970)
Hint: check that each side satisﬁes the recurrence relation fN = fN−1 + qN−1fN−2.
Dilogarithm identities
43
6. Deduce from Exercise 5 the Rogers-Ramanujan identities (a = 0 or 1)
X
j≥0
qj2+aj
(q)j
=
Y
j≥0
1
(1 −q5j+1+a)(1 −q5j+4−a).
(2)
• Prove,
RHS(2)= lim
N→∞
X
σi ∈{0, 1}, σiσi+1 = 0
σ1 = a, σN+1 = 0
q
PN−1
j=1 jσj+1
=
1
(q)∞
X
k∈Z

qk(10k+1+2a) −q(2k+1)(5k+2−a)
.
(3)
7.
(Fusion rules and Rogers-Ramanujan’s type identities).
A. Let r ≥3 be an odd integer and l := r −3
2
. Let us introduce
i) matrix M := M(x) ∈Matl+1×l+1(Z[x]), where (1 ≤i, k ≤l + 1)
Mik :=

0,
if i + k < l + 2;
xl−k+1,
if i + k ≥l + 2;
ii) the highest weight vector |j >= el−j+1 + . . . + el+1, where 0 ≤j ≤l and ei is the basis
vector in (Rl)∗, namely, et
i = (δik), 1 ≤k ≤l + 1;
iii) vector aj,N := aj,N(x; q) = (a(1)
j,N, . . . , a(l+1)
j,N ) by the following rule
M(qN−1x)M(qN−2x) · · ·M(qx)M(x)|j >= at
j,N.
• Prove,
a(p)
j,N(x, q) =
X
m=(m1,...,ml)∈Zl
+
xN1+...+NlqN2
1 +N2
2 +...+N2
l −N1−...−Nj
lY
k=1

Pk(m; j, p) + mk
mk

q
,
where Ni := mi + mi+1 + . . . + ml, 1 ≤p ≤l + 1,
and
Pk(m; j, p) := kN + min(k, l −j) −max(k + 1 −p, 0) −2
l
X
i=1
min(i, k)mi.
It is well-known (see e.g. [FrSz1]) that
lim
N→∞a(p)
j,N(q, q) = χ(2,r)
1,1+j(q).
Using the Feigin–Fuchs–Rocha-Caridi character formula for χ(2,r)
1,1+j(q) (see e.g. [FF] or for-
mula (5)), and the exact expression for a(p)
j,N(x, q), we obtain the group-theoretic proof/ex-
planation of the Gordon-Andrews identity. Even more, one can consider the polynomial
(x; q)N · a(l+1)
j,N (x, q) as a ”natural ﬁnitization” of the Watson-Andrews identity (9). How-
ever, the exact computation of polynomials (x; q)N · a(l+1)
j,N (x, q) seems to be very diﬃcult
(even for x = 1). In this direction one can obtain the following partial result.
44
Anatol N. Kirillov
Theorem 8 (A.N. Kirillov). We have
(x; q)Na(l+1)
j,N (x, q) ≡
X
m≥0
(−1)mx(l+1)mq
1
2 (2l+3)m(m+1)−(l+2+j)m

(l + 1)(N −2m) + l + 2 + j
m

q
·
 1 −(q2mx)1+j (x; q)m
(q; q)m
(mod degqN).
Taking the limit N →∞one can obtain the Watson–Andrews identity (9).
B. (Fusion algebra). Let us deﬁne the level r fusion algebra Fr as a ﬁnite dimensional
algebra over rational numbers Q with generators {vj | j = 0, 1
2, 1, 3
2, . . ., r −2
2
} and the
following multiplication rule (the level r Clebsch-Gordan series):
vj1 b⊗vj2 =
min(j1+j2, r−2−j1−j2)
X
j=|j1−j2|, j−j1−j2∈Z
vj.
(4)
It is well known (see e.g. [Kac]), that the fusion algebra Fr is a commutative and associative
one. Note also, that the fusion rules (4) correspond to a decomposing the tensor product
Vj1 b⊗Vj2 of the restricted representations [Ros] Vj1 and Vj2 of the Hopf algebra Uq(sl(2))
when q is the root of unity q = exp
2πi
r

into the irreducible parts (see e.g. [Lu3]).
Further, let us denote by MultVk(Vj1 b⊗· · · b⊗VjN ) the coeﬃcients which appear in the
decomposition of the product vj1 b⊗· · · b⊗vjN in the fusion algebra Fr:
vj1 b⊗· · · b⊗vjN =
X
k
MultVk(vj1 b⊗· · · b⊗vjN ) · vk.
i) Prove the following relation (see Exercise 7, part A, 0 ≤j ≤l)
a(l+1)
j,N (1, 1) = MultVr(j)(V b
⊗(N+1)
s
),
s :=
l + 1
2

,
where for given j, r(j) is the unique integer such that
0 ≤r(j) ≤r −3
2
and j r −3
2
≡±r(j) (mod (r −2)).
ii) Prove the following multiplicity formula (cf. [Kir6]):
MultVk(Vj1 b⊗· · · b⊗VjN ) =
X
{ν}
Y
n≥1

Pn,r(νij) + mn(ν)
mn(ν)

,
where the summation is taken over all partitions ν = (ν1 ≥ν2 ≥· · · ≥0) such that
Dilogarithm identities
45
a) |ν| := ν1 + ν2 + . . . =
N
X
s=1
js −k,
b) (inequalities for vacancy numbers)
Pn,r(ν; j) :=
N
X
s=1
min(n, 2js) −max(n + 2k + 2 −r, 0) −2Qn(ν) ≥0.
Here Qn(ν) :=
X
j≥1
min(n, νj) and mn(ν) is the number of parts of partition ν which are
equal to n.
C. (Restricted Kostka-Foulkes polynomials).
For the given natural number l, partition λ = (λ1 ≥λ2 ≥0) and composition µ, we
deﬁne the level l (or restricted) Kostka-Foulkes polynomial K(l)
λ,µ(q) by the following way
K(l)
λ,µ(q) :=
X
ν, l(ν′)≤l
q2n(ν) Y
n≥1

Pn(ν; µ) + mn(ν)
mn(ν)

q
,
where summation is taken over all partitions ν such that
i) |ν| = ν1 + ν2 + · · · = λ2, ν1 ≤l,
ii) Pn(ν; µ) :=
X
j
min(n, µj) −2Qn(ν) ≥0, ∀n.
It follows from the Exercise 7, A, that
a(l+1)
0,N (x; q) =
X
0≤m≤Nl
2
(qx)mK(l)
(Nl−m,m),(lN )(q).
• Prove, that if m ≤l, then
K(l)
(Nl−m,m),(lN)(q) = K(Nl−m,m),(lN )(q) =

m + l −1
l −1

q
.
• Using the deﬁnition of restricted Kostka polynomials K(l)
λ,µ(q), prove that the q-
binomial coeﬃcients

m
n

q
are the unimodal and symmetric polynomials (cf. [Kir5]).
Conjecture 2. Polynomials K(l)
(Nl−m,m),(lN )(q) are unimodal.
Let us consider a simple example with l = 2, N = m = 4. One can compute the Kostka
polynomial K(4,4),(24)(q) by using the Theorem 10. Namely, there exist three conﬁgurations
0,
c = 1 + 1 + 1 + 1 −4 = 0,
0
0
,
c = 3 + 1 + 1 + 1 −4 = 2,
0,
c = 3 + 3 + 1 + 1 −4 = 4.
46
Anatol N. Kirillov
Consequently, K(4,4),(24)(q) = 1 + q2 + q4 and this is a non-unimodal polynomial,
whereas the level 2 Kostka polynomial K(2)
(4,4),(24)(q) = q4 is the unimodal one.
D. (Polynomial analog of Gordon-Andrews’ identities).
Let us remind the basic facts about the minimal series irreducible representations of
the Virasoro algebra. Given two (coprime) positive integers p′ > p ≥2, then central charge
and highest weights of the corresponding irreducible representations V(p,p′)
r,s
of the Virasoro
algebra are (see e.g. [FF])
c(p,p′) = 1 −6(p′ −p)2
pp′
and
∆(p,p′)
r,s
= (rp′ −sp)2 −(p′ −p)2
4pp′
,
1 ≤r ≤p −1, 1 ≤s ≤p′ −1.
The characters of these representations are ([R-C], [FF])
χ(p,p′)
r,s
(q) := q−∆(p,p′)
r,s
TrV(p,p′)
r,s
qL0 =
1
(q)∞
X
k∈Z

qk(kpp′+rp′−sp) −q(kp+r)(kp′+s)
.
(5)
Note the symmetry of the ”conformal grid”
{(r, s) | 1 ≤r ≤p −1, 1 ≤s ≤p′ −1},
(6)
(r, s) ↔(p −r, p′ −s) : ∆(p,p′)
r,s
= ∆(p,p′)
p−r,p′−s ⇒χ(p,p′)
r,s
(q) = χ(p,p′)
p−r,p′−s(q).
Note also that the RHS(3) is precisely χ(2,5)
1,2−a(q) as given by the RHS(5).
We are interested in ﬁnding a natural polynomial analog for the character χ(p,p′)
r,s
(q).
For this purpose let us introduce the polynomials (cf. [Me2])
B(N)
p,p′;r,s(q) :=
X
k∈Z







qk(kpp′+rp′−sp)


N
N + s −r −d(p, p′)
2

−p′k


q
−q(pk+r)(p′k+s)


N
N −s −r −d(p, p′)
2

−p′k


q







,
(7)
where d(p, p′) :=
p′ −p
2

.
It is clear that in the ”physical region” (6)
lim
N→∞B(N)
p,p′;r,s(q) = χ(p,p′)
r,s
(q).
• Prove the following properties of the ”bosonic” polynomials (7)
Dilogarithm identities
47
i) (Symmetry) If p ≡p′ (mod 2), 1 ≤r ≤p −1 and 1 ≤s ≤p′ −1, then
B(N)
p,p′;r,s(q) = B(N)
p,p′;p−r,p′−s(q).
ii) (Positivity) All coeﬃcients of the polynomials B(N)
p,p′:r,s(q) in the ”physical region” (6)
are the non-negative integers.
iii) (Recurrence relations and initial conditions)
B(N)
p,p′;r,s(q) = B(N−1)
p,p′;r.s(q) +





q
N+s−r−d(p,p′)
2
B(N−1)
p,p′;r−1,s(q),
if N ≡s −r −d(p, p′)(mod 2);
q
N−s+r+d(p,p′)+1
2
B(N−1)
p,p′;r+1,s(q),
if N̸ ≡s −r −d(p, p′)(mod 2);
B(0)
p,p′;r,s(q) = δs,r+d(p,p′) + δs,r+1+d(p,p′).
iv) (Fusion multiplicities) Assume that p′ ≡1(2), l = (p−3)/2 and {V0, V1, . . ., Vl} are the
odd dimensional restricted representations of the quantum group Uq(sl(2)) at the root of
unity q = exp
2πi
p′

(see [Lu3] or Exercise 7, A and B). If −d ≤r ≤p + ed, 1 ≤s ≤p′ −1
then B(N)
p,p′;r,s(1) is a linear combination with non-negative integer coeﬃcients of the ”fusion
multiplicities”
MultVj(V b
⊗N
l
), 0 ≤j ≤l.
• Prove, for example, that (1 ≤s ≤l + 1)
B(N)
2,2l+3;1,s(1) =
s
X
j=1
MultVr(j;l)

V b
⊗N
l

,
where r(j; l) :=
l + 1
2

+ (−1)l+j
j
2

;
B(N)
p,p′;r,1(1) =







MultV[ r+d
2 ]

V b
⊗N
l

,
N ≡0(2),
MultVh
p−r+e
d
2
i

V b
⊗N
l

,
N ≡1(2),
where ed := ed(p, q) =
p′ −p −1
2

, −d ≤r ≤p + ed.
• Prove that
B(N)
p,p′;r,s(1) = B(N)
p,p′;r+1,s(1),
if s + r ≡1 + (−1)N
2
(mod 2).
• Let us deﬁne a matrix B(N)
p,p′ of the size p′ × (p′ −1) by the following manner

B(N)
p,p′

i,j = B(N)
p,p′;i−1−d,j(1),
1 ≤i ≤p′,
1 ≤j ≤p′ −1.
48
Anatol N. Kirillov
Prove that (p′ ≡1(2))
B(N)
2,p′ = B(N)
3,p′ = · · · = B(N)
p′−1,p′.
• Let us put B(N)
p′
:= B(N)
p,p′, where p′ ≡1 (mod 2) and 1 ≤p ≤p′ −1.
Prove (1 ≤i ≤p′, 1 ≤j ≤p′ −1)
j) If i + j ≡N + 1 (mod 2), then
(B(N)
p′ )ij =













min(i−1,p′−i+1,j,p′−j)
X
k=1
MultVk−1+ 1
2 |p′−i−j+1|(V b
⊗N
l
),
if N ≡1 (mod 2);
min(i−1,p′−i+1,j,p′−j)
X
k=1
MultVk−1+ 1
2 |i−j−1|(V b
⊗N
l
),
if N ≡0 (mod 2).
jj) If i + j ≡N (mod 2), then
(B(N)
p′ )ij =













min(i,p′−i,j,p′−j)
X
k=1
MultVk−1+ 1
2 |p′−i−j|(V b
⊗N
l
),
if N ≡1 (mod 2);
min(i,p′−i,j,p′−j)
X
k=1
MultVk−1+ 1
2 |i−j|(V b
⊗N
l
),
if N ≡0 (mod 2).
Let us remark that
B(N)
p,p′;r,s(1) = (B(N)
p′ )r+d+1,s.
It is an interesting problem to ﬁnd a pure combinatorial interpretation in terms of some
kind of partitions for the numbers B(N)
p,p′;r,s(1) in the region {−d ≤r ≤p+ ed, 1 ≤s ≤p′−1},
as well as their natural q-analogs.
A proof of part ii). Following the paper [ABBBFV], we give a combinatorial inter-
pretation of the ”bosonic” polynomials B(N)
p,p′;r,s(q).
Deﬁnition 4. Let λ be a partition/Young diagram. For any box x ∈λ lying in the
i-th row and j-th column of the Young diagram λ, let us deﬁne the hook diﬀerence at the
x (notation hd(x)) as follows
hd(x) = λi −λ′
j.
Deﬁnition 5. We say that a box x := (i, j) ∈λ lies on diagonal c, if i −j = c.
Deﬁnition 6.
For given positive integers
A, B, p, p′, r
and s let us deﬁne
Rp′,s(A, B; p, r; n) to be the set of partitions of n into at most B parts each ≤A such
that the hook diﬀerences on diagonal 1 −r are ≥1 + r −s and on diagonal p −r −1 are
≤p′ −s −p + r −1.
Dilogarithm identities
49
The related generating function is, of course, a polynomial
Dp′,s(A, B; p, r; q) =
X
n≥0
#|Rp′,s(A, B; p, r; n)|qn.
Theorem ([ABBBFV]). Assume that 1 ≤r < p and 1 ≤2s ≤p′. Then
B(N)
p,p′;r,s(q) = Dp′,s(N −B, B; p, r; q),
where
B =
N + s −r −d(p, p′)
2

.
Remark. It seems plausible that for given integers p′ > p ≥2, N ≥1 and r, the
polynomials B(N)
p,p′;r,s(q) have the nonnegative coeﬃcients for all s, 1 ≤s ≤p′ −1, if and
only if r satisﬁes the inequalities 0 ≤r ≤p. For example,
B(9)
4,9;0,1(q) = q4(1 + q4)(1 + q3 + q6)1 −q7
1 −q .
However, one can prove that lim
N→∞B(N)
p,p′;r,s(q) = 0, if r = 0 or p and 1 ≤s ≤p′ −1.
• It is an interesting task to ﬁnd a natural representation of the ”restricted Hecke
algebra” eHN(q), q = exp
2πi
p′

, p′ ≡1(mod 2) (see e.g.
[GW]), in the linear space
generated by the ﬁnite set
a
n
Rp′,s(N −B, B; p, r; n).
• Another interesting problem is to ﬁnd the ”fermionic” representation (see e.g. [Me2])
for B(N)
p,p′;r,s(q). Such representation is known in the following three cases:
i) (p, p′) := (p, p + 1), d(p, p′) = 0, E. Melzer [Me2] (conjecture), A. Bercovich [Ber]
(proof the Melzer conjecture for all pairs (r, s) with s = 1).
ii) (p, p′) := (2, 2l + 3), d(p, p′) = l, Y.-H. Quano, A.N. Kirillov.
iii) (p, p′) := (2l + 2), d(p, p′) = l, Y.H. Quano.
Theorem 9* (A.N. Kirillov). We have the following equivalent expressions for the
RHS(7) (we use the notation from Exercise 7, A,B,C,D. Note also, that in our case r = 1
and we assume that 0 ≤s ≤l + 1): B(N)
2,2l+3;1,s(q) =
=
X
(m1,...,ml)∈Zl
+
qN2
1 +···+N2
l +Ns+···+Nl
lY
k=1

Pk(m; s, N) + mk
mk

q
(8)
=
X
m
q2m X
ν⊢m
q2n(ν)−Qs−1(ν)
lY
k=1

N −max(k + 1 −s, 0) −2Qk(ν) + mk(ν)
mk(ν)

q
,
* After ﬁnishing this work, I was informed by A. Kato about the recent preprint of Y.-
H. Quano [Q1] which contains the proof of Theorem 9. Also in [Q1] a polynomial analog
of Bressoud’s identity (10) is given.
50
Anatol N. Kirillov
where ( the so-called vacancy numbers)
Pk(m; s, N) := N −max(k + 1 −s, 0) −2
l
X
j=1
min(k, j)mj ≥0.
Our proof is based on the Theorem [ABBBFV], the combinatorial description of the
RHS(8) in terms of the special type partitions (see e.g. [AB], [Bre4], [Bre5]) and that in
terms of the rigged conﬁgurations (see e.g. [Kir3]).
Problems. i) To ﬁnd the corner-transfer-matrix type representation for the ”bosonic”
sum (7) (see e.g. [ABF], [FB], [Me2]).
ii) To ﬁnd a natural polynomial analog for the G¨ollnitz-Gordon-Andrews identity (2.2).
It is well-known, that the RHS(2.2) is the character of a representation of the Neveu-
Schwarz algebra.
8. Prove the following generalizations of the Gordon-Andrews identity (2.1):
i)
X
n1,...,nk
zN1+···+NkqN2
1 +···+N2
k+Nj+···+Nk
(q)n1 . . . (q)nk
(9)
=
1
(qz)∞



X
m≥0
(−1)mz(k+1)mq(2k+3) m(m+1)
2
−jm(1 −(q2m+1z)j)(qz)m
(q)m


,
(L. Rogers and S. Ramanujan, 1920; G. Watson, 1928; G. Andrews, 1974)
ii)
X
n1,...,nk
(zq−1)N1+···+NkqN2
1 +···+N2
k(a; q−1)N1(b; q−1)N1
(q)n1 . . .(q)nk
=
X
m≥0
(−1)mz(k+1)mq(2k+3) m(m+1)
2
(a; q−1)m(b; q−1)m(azqm)∞(bzqm)∞(1 −zq2m−1)
(q)m(zqm−1)∞(abz)∞
.
(G. Andrews, J. Stembridge)
9. Prove the following identity
X
n1,...,nl
qN2
1 +...+N2
l +Ns+...+Nl
(q)n1 · · · (q)nl−1(q2; q2)nl
=
Y
n̸≡0,±s (mod 2l+2)
(1 −qn)−1.
(10)
(D. Bressoud, 1980)
• Prove the polynomial analog of Bressoud’s identity (10),
1 ≤s ≤l + 1 (see [Q1]),
B(N)
2,2l+2;1,s(q) =
X
m=(m1,...,ml)∈Zl
+
qN2
1 +·+N2
l +Ns+·+Nl
l−1
Y
k=1

Pk(m; s, N) + mk
mk

q


N + s −l −1
2

−Nl−1
ml


q2
,
Dilogarithm identities
51
where Pk(m; s, N) := N + 1 −min(l −s + 1, k) −δs,1 −δs,l+1 −2
l
j=1
min(j, k)mj ≥0.
10. Prove the following identity
X
n1,...,nl
q2(N2
1 +···+N2
l +Ns+···+Nl)
(q2; q2)n1 · · · (q2; q2)nl(−q)2nl
=
1
(−q)∞
Y
n̸≡0,±2s (mod 4k+3)
(1 −qn)−1
(L. Rogers, 1894; A. Selberg, 1936; P. Paule, 1985)
11. Prove the following polynomial identities (a = 0, 1)
X
k∈Z
(−1)kq4k2−(2a+1)k

2N + a
N + k

q2
= (q2N+2; q2)N+a
N
X
k=0
q2k2+2ak
(−q; q2)k+a

N
k

q2
.
(11)
(P. Paule, 1985)
It is easy to see that in the limit N →∞these identities become
X
k≥0
q2k2+2ak
(−q; q2)k+a(q2; q2)k
=
1
(q2; q2)∞
Y
n≡0,±(3−2a) (mod 8)
(1 −qn).
(L. Slater, 1950; H. G¨ollnitz, 1967; B. Gordon, 1961)
12. (Bailey’s transform and Rogers-Ramanujan’s type identities).
1) (Bailey’s transform). Let a be indeterminate and i, j ≥0 be integers. Let us consider
the matrices M and M ∗, where
Mij := (q)−1
i−j(aq)−1
i+j;
(12a)
M ∗
ij := (−1)i−jq
(i−j)(i−j−1)
2
(1 −aq2i)(aq)i+j−1(q)−1
i−j.
(12b)
Prove that M and M ∗are inverse, inﬁnite, lower-triangle matrices. That is
X
j≤k≤i
MikM ∗
kj = δij.
Hint: use the terminating very well-poised 4ϕ3 summation theorem (see e.g. [GR]).
2) Let α = {αn} and β = {βn}, n ≥0 be sequences of functions in q. Let M and M ∗be
as in (12). We say (cf. [An3]) that α and β form a Bailey pair relative to a if
βn =
n
X
k=0
Mnkαk,
for all n ≥0.
52
Anatol N. Kirillov
It is clear that (Bailey’s pair inversion rule)
αn =
n
k=0
M ∗
nkβk.
Theorem (G. Andrews [An2]) (Bailey’s lemma). Let the sequences α = {αn} and
β = {βn} form a Bailey pair. If α′ = {α′
n} and β′ = {β′
n} are deﬁned by
α′
n :=
(ρ1)n(ρ2)n
(aq/ρ1)n(aq/ρ2)n
(aq/ρ1ρ2)nαn,
β′
n :=
n
X
k=0
(ρ1)k(ρ2)k(aq/ρ1ρ2)n−k
(q)n−k(aq/ρ1)k(aq/ρ2)k
(aq/ρ1ρ2)kβk,
then α′ and β′ also form a Bailey pair.
A proof can be found in [An3].
• Prove the following corollary of Bailey’s lemma:
X
k≥0
akqk2βk =
1
(aq)∞
∞
X
k=0
akqk2αk,
(13)
for any Bailey pair α = {αn} and β = {βn}.
Hint: take the limit n, ρ1, ρ2 →∞in the Bailey pair deﬁning relation
β′
n =
n
X
k=0
α′
k
(q)n−k(aq)n+k
.
More generally, prove that if α = {αn} and β = {βn} is a Bailey pair, then
X
m1,...,mk
aN1+···+NkqN2
1 +···+N2
k
(q)m1 · · · (q)mk
βmk =
1
(aq)∞
X
n≥0
qkn2aknαn.
(G. Andrews, 1984)
Hint: use the k-fold iteration of Bailey’s lemma.
3) Prove that the following sequences form the Bailey pair
i) βn =
 1,
n = 0,
0,
n > 0,
(15)
αn = (−1)nq
n(n−1)
2
(1 −aq2n)(a)n
(1 −a)(q)n
.
Hint: use the Agarwal identity (see e.g. [An2]):
N
X
k=0
(1 −aq2k)(q−n)k(a)kqnk
(1 −a)(q)k(aqn+1)k
= (aq)NqnN(q1−n)N
(q)N(aqn+1)N
.
Dilogarithm identities
53
It is easy to see that the Watson-Andrews identity (9) (with j = 1 or k + 1) follows
from (14) and (15).
ii) Prove that if α = {αn} and β = {βn} be a Bailey pair relative to a, then
α′
n :=





α0,
n = 0,
(1 −a)anqn2−n

αn
1 −aq2n −aq2n−2αn−1
1 −aq2n−2

,
n > 0,
β′
n :=
n
k=0
akqk2−k
(q)n−k
βk
is also a Bailey pair relative to aq−1.
Proofs and further details see in [AAB], [Bre6], [P2], [GS], [FQ], [Q2], [Sl], [ML]. It is
well-known (see e.g. [W1]) that the classical Rogers-Ramanujan identities (see e.g. Exercise
6 to Section 2.1) can be deduced from Watson’s [W1] q-analog of Whipple’s transformation
formula (see e.g. [GR]). It seems very interesting to understand what kind of partition
identitis correspond to the Milne (see e.g. [Ml3], [ML]) multidimensional generalization of
Bailey’s lemma and the Watson-Whipple transformation formula.
