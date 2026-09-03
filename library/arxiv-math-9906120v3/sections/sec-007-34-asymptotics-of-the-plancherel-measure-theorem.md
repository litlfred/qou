---
doc_id: arxiv-math-9906120v3
doc_title: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson"
section_id: sec-007-34-asymptotics-of-the-plancherel-measure-theorem
section_title: "Asymptotics of the Plancherel measure. Theorem 1.3 can be used"
section_number: 3.4
pages: 23-27
source_pdf: 9906120v3.pdf
source_sha256: 436982ef45e940bd
doc_brief: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson — We consider discrete orthogonal polynomial ensembles which are discrete analogues of the orthogonal polynomial"
---
to analyze the asymptotic properties of the Plancherel measure in diﬀerent
regions. One can distinguish three cases corresponding to three diﬀerent scaling
limits of the Bessel kernel. First we have the edge scaling limit,
(3.35)
lim
α→∞α1/6Bα(2√α + ξα1/6, 2√α + ηα1/6) = A(ξ, η),
where A is the Airy kernel deﬁned in (1.4). This is the case that is considered
in Theorem 1.4. Secondly we have the bulk scaling limit,
(3.36)
lim
α→∞Bα(r√α, r√α + u) = sin(uR)
uπ
,
u ∈Z, −2 < r < 2, where R = arccos(r/2); the right-hand side is the discrete
sine kernel. We will not discuss the local behavior in the bulk of the Young
diagram; see [BOO]. Thirdly we have an intermediate region,
(3.37)
lim
α→∞πα1/4−δ/2Bα(2√α −αδ + πξα1/4−δ/2, 2√α −αδ + πηα1/4−δ/2)
= sin π(ξ −η)
π(ξ −η)
,
if 1/6 < δ < 1/2, the ordinary sine kernel.
Thus in this region the local
behavior is the same as that in the bulk in a random Hermitian matrix. The
limits (3.35) to (3.37) can be proved using the saddle-point method on the
integral formula for the Bessel function. From the point of view of the Coulomb
gas picture of the Young diagram, the cases one and three are similar to the
random matrix case since at the edge a discrete Coulomb gas approximates a
continuous Coulomb gas. Case two is diﬀerent however, since in the bulk the
discrete nature is manifest; the charges sit close to each other.
Before turning to the proof of Theorem 1.4 we have to say something
about de-Poissonization, the joint distribution of the ﬁrst k rows (k largest
eigenvalues) and the asymptotics of the Bessel kernel.
We have the following generalization of a lemma in [Jo2].
Lemma 3.8. Let µN = N + 4√N log N and νN = N −4√N log N. Then
there is a constant C such that, for 0 ≤xi ≤N,
(3.38)
PµN
Plan[λ1 ≤x1, . . . , λk ≤xk] −C
N 2 ≤PPlan,N[λ1 ≤x1, . . . , λk ≤xk]
≤PνN
Plan[λ1 ≤x1, . . . , λk ≤xk] + C
N 2 .
Proof. This is proved as Lemmas 2.4 and 2.5 in [Jo2]. Denote a permu-
tation in SN by π(N) and let SN+1(j) denote the set of all π(N+1) such that
π(N+1)(N + 1) = j.
Each π(N+1) in SN+1(j) is mapped to a permutation
Fj(π(N+1)) in SN by replacing each π(N+1)(i) > j by π(N+1)(i) −1. The map
282
KURT JOHANSSON
Fj is a bijection from SN+1(j) to SN. Apply the Robinson-Schensted corre-
spondence to Fj(π(N+1)) to obtain the P-tableau. Replace the entries i by
i + 1 for i = j, . . . , N and then insert j. This insertion can only increase the
length of any row and we obtain the P-tableau for π(N+1). Thus,
λi(Fj(π(N+1))) ≤λi(π(N+1)),
for all rows. If we deﬁne g(π(N)) to be 1 if λi(πN) ≤xi for i = 1, . . . , k and 0
otherwise, we see that
g(Fj(π(N+1))) ≥g(π(N+1)),
and we can proceed exactly as in [Jo2] using the fact that the Plancherel
measure on P(N) is the push-forward of the uniform distribution on SN.
For x ∈RM, n ∈Nk and a sequence I = (I1, . . . , Ik) of intervals in R we
let χ(I, n, x) denote the characteristic function for the set of all x ∈RM such
that exactly nj of the xi’s belong to Ij, j = 1, . . . , k. A computation shows
that for a single interval
χ(Ij, nj, x) = 1
nj!
∂nj
∂znj
j
M
Y
i=1
(1 + zjχIj(xi))

zj=−1
and hence
(3.39) χ(I, n, x) =
1
n1! . . . nk!
∂n1+···+nk
∂zn1
j . . . ∂znk
j
M
Y
i=1
k
Y
j=1
(1 + zjχIj(xi))

z1=···=zk=−1
.
Note that if the intervals are pairwise disjoint, then Qk
j=1(1 + zjχIj(xi)) =
1 + Pk
j=1 zjχIj(xi); compare with [TW2].
Let P be a probability measure
on RM and let a1 ≥· · · ≥ak. Set Ij+1 = (aj+1, aj], j = 1, . . . , k −1 and
I1 = (a1, ∞). Let
Lk = {n ∈Nk ;
r
X
j=1
nj ≤r −1, r = 1, . . . , k}.
Deﬁne x(j) to be the jth largest of the xi’s. Then,
(3.40)
P[x(1) ≤a1, . . . , x(k) ≤ak] =
X
n∈Lk
E[χ(I, n, x)].
Hence, the problem of investigating the distribution function in (3.40) reduces
to investigating expectations of the right-hand side of (3.39).
In the proof of Theorem 1.4 we will need some asymptotic results for
Bessel functions.
ENSEMBLES AND THE PLANCHEREL MEASURE
283
Lemma 3.9. Let M0 > 0 be given. Then there exists a constant C =
C(M0) such that if we write x = 2√α + ξα1/6, then
(3.41)
|Jx(2√α)| ≤Cα−1/6 exp

−1
4 min
1
4α1/6, |ξ|1/2

|ξ|

for ξ ∈[−M0, ∞). Furthermore
(3.42)
lim
α→∞α1/6Jx(2√α) = Ai (ξ),
uniformly for ξ ∈[−M0, M0].
This can be deduced from classical asymptotic results, [Wa] and it is also
rather straightforward to proceed as in Section 5 of [Jo3] using the integral
formula (3.28).
We are now ready for the
Proof of Theorem 1.4. We will prove (1.20). The proof of (1.19) is analo-
gous using the Hermite kernel instead. From Lemma 3.8, the fact that a dis-
tribution function is increasing in its arguments, that the distribution function
F(t1, . . . , tk) is continuous and √µN −
√
N ≈2√log N, √νN −
√
N ≈2√log N,
we see that it suﬃces to prove that
(3.43)
lim
α→∞Pα
Plan[λ1 −1 ≤2√α + t1α1/6, . . . λk −k ≤2√α + tkα1/6] = F(t1, . . . , tk),
for any ﬁxed (t1, . . . , tk) ∈Rk, t1 ≥· · · ≥tk. Set
Ij+1 = (2√α + tj+1α1/6, 2√α + tjα1/6],
j = 1, . . . , k −1
and I1 = (2√α + t1α1/6, ∞). By (3.39) and (3.40) it is enough to consider the
expectations
(3.44)
Eα
Plan


∞
Y
i=1
k
Y
j=1
(1 + zjχIj(λj −j))

.
If we write φα(s) = Qk
j=1(1 + zjχIj(s)) −1 it follows from Theorem 1.3, with
L = 0, that the expectation (3.44) can be written as
(3.45)
Fα(z, t) =
∞
X
k=0
1
k!
X
h∈Nk
k
Y
j=1
φα(hj) det[Bα(hi, hj)]k
i,j=1.
Note that Fα(z, t) is an entire function of z. Set Jj+1 = (tj+1, tj], j = 1, . . . ,
k −1, J1 = (t1, ∞) and write ψ(s) = Qk
j=1(1 + zjχJj(s)) −1. Deﬁne
(3.46)
F(z, t) =
∞
X
k=0
1
k!
Z
Rk
k
Y
j=1
ψ(ξj) det[A(ξi, ξj)]k
i,j=1.
284
KURT JOHANSSON
We want to show that
(3.47)
lim
α→∞Fα(z, t) = F(z, t),
uniformly for z in a compact subset of Ck. Then also derivatives of Fα(z, t)
converge to the corresponding derivatives of F(z, t).
The limit (3.43) then
follows with
(3.48)
F(t1, . . . , tk) =
X
n∈Lk
1
n1! . . . nk!
∂n1+···+nk
∂zn1
1 . . . ∂znk
k
F(z, t)

z1=...zk=−1
.
So it remains to prove (3.47). Note that φα(s) = 0 if s < 2√α+tkα1/6 and
that φα(s) = ψ(α−1/6(s−2√α)). Given r ∈R we set A(r) = {r, r+1, r+2, . . . }.
Then,
(3.49)
Fα(z, t) =
∞
X
l=0
1
l!
X
h∈A(tkα1/6)l
lY
j=1
ψ
 hj
α1/6

det[ ˜Bα(ξ, η)]
1
(α1/6)l ,
where ˜Bα(ξ, η) = α1/6Bα(2√α + ξα1/6, 2√α + ηα1/6).
We can now prove
that (3.47) holds pointwise in z by the same argument as was used in the
proof of the analogous statement in Section 3 of [Jo3]. That proof depends on
the following properties of the kernel; compare with Lemma 3.1 in [Jo3] and
Lemma 4.1 below.
(i) For any M0 > 0 there is a constant C = C(M0) such that for all ξ ≥−M0
∞
X
m=1
Bα(2√α + ξα1/6 + m, 2√α + ξα1/6 + m) ≤C.
(ii) For any ε > 0, there is an L > 0 such that
∞
X
m=1
Bα(2√α + Lα1/6 + m, 2√α + Lα1/6 + m) ≤ε,
for all suﬃciently large α.
(iii) For any M0 > 0 and any ε > 0

 ˜Bα  n
α1/6 , m
α1/6

−A
 n
α1/6 , m
α1/6


 ≤ε
for all integers m, n ∈[−M0α1/6, M0α1/6] provided α is suﬃciently large.
The estimate (i) is used to estimate the tail in the k-summation in (3.49),
(ii) is used to limit the h-summation and (iii) is used to prove that the Riemann
sums converge to integrals.
If z belongs to a compact set K there is a constant C, independent of z,
such that ||ψ||∞≤C. Together with (i) this shows that the family {Fα(z, t)}
is uniformly bounded for α > 0, z ∈K and hence (3.47) holds uniformly by a
normal family argument.
ENSEMBLES AND THE PLANCHEREL MEASURE
285
The properties (i) to (iii) above are straightforward to prove using the
representation (3.31) and Lemma 3.9. To prove (i) and (ii) we use
∞
X
m=1
Bα(x + m, x + m) =
∞
X
n=1
nJ2
x+n+1(2√α),
which can be estimated using (3.41) (we get a Riemann sum).
Similarly,
˜Bα(
n
α1/6 ,
m
α1/6 ) can be written as a Riemann sum, using (3.31), which is con-
trolled using (3.41) and (3.42). This Riemann sum can be compared with the
corresponding Riemann sum for the following representation of the Airy kernel,
[TW1],
A(ξ, η) =
Z ∞
0
Ai (ξ + t)Ai (η + t)dt
and in this way we obtain (iii).
