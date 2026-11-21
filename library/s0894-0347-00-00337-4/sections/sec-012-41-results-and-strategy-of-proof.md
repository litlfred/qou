---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-012-41-results-and-strategy-of-proof
section_title: "Results and strategy of proof"
section_number: 4.1
pages: 19-26
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
was stated in Section 1.4 of the Introduction. We refer the reader to Section 1.4 for
a discussion of the relation between Theorem 4 and the results obtained in [3, 4, 25].
Recall that the Airy kernel was deﬁned as
A(x, y) = A(x)A′(y) −A′(x)A(y)
x −y
,
where A(x) is the Airy function (1.15).
The Airy ensemble is, by deﬁnition, a
random point process on R, whose correlation functions are given by
ρAiry
k
(x1, . . . , xk) = det
h
A(xi, xj)
i
1≤i,j≤k .
This ensemble was studied in [36]. We denote by ζ1 > ζ2 > . . . a random con-
ﬁguration of the Airy ensemble. Theorem 4 says that after a proper scaling and
normalization, the rows λ1, λ2, . . . of a Plancherel random partition λ converge in
joint distribution to the Airy ensemble. Namely, the random variables eλ,
eλ =

eλ1 ≥eλ2 ≥. . .

,
eλi = n1/3
 λi
n1/2 −2

,
converge, in joint distribution, to the Airy ensemble as n →∞.
In the proof of Theorem 4, we shall follow the strategy explained in Section 1.5
of the Introduction. First, we shall prove that under the poissonized measure M θ
500
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
on the set of partitions λ, the random variables eλ converge, in joint distribution, to
the Airy ensemble as θ ≈n →∞. This result is stated below as Theorem 5. From
this, using certain monotonicity and Lemma 4.7 which is due to K. Johansson, we
shall conclude that the same is true for the measures Mn as n →∞.
The proof of Theorem 5 will be based on the analysis of the behavior of the
correlation functions of M θ, θ ≈n →∞, near the point 2√n. From the expression
for correlation functions of M θ given in Theorem 1 it is clear that this amounts to
the study of the asymptotics of J2√n(2
√
θ) when θ ≈n →∞. This asymptotics is
classically known and from it we shall derive the following
Proposition 4.1. Set r =
√
θ. We have
r
1
3 J

2r + xr
1
3 , 2r + yr
1
3 , r2
→A(x, y),
r →+∞,
uniformly in x and y on compact sets of R.
The prefactor r
1
3 corresponds to the fact that we change the local scale near 2r
to get nonvanishing limit correlations.
Using this and verifying certain tail estimates we obtain the following
Theorem 5. For any ﬁxed m = 1, 2, . . . and any a1, . . . , am ∈R we have
(4.1)
lim
θ→+∞M θ
 (
λ

λi −2
√
θ
θ
1
6
< ai , 1 ≤i ≤m
)!
= Prob{ζi < ai , 1 ≤i ≤m} ,
where ζ1 > ζ2 > . . . is the Airy ensemble.
Observe that the limit behavior of eλ is, obviously, identical with the limit be-
havior of similarly scaled 1st, 2nd, and so on maximal Frobenius coordinates.
Proofs of Proposition 4.1 and Theorem 5 are given Section 4.2. In Section 4.3,
using a depoissonization argument based on Lemma 4.7 we deduce Theorem 4.
Remark 4.2. We consider the behavior of any number of ﬁrst rows of λ, where λ is
a Plancherel random partition. By symmetry, same results describe the behavior
of any number of ﬁrst columns of λ.
4.2. Proof of Theorem 5. Suppose we have a point process on R with determi-
nantal correlation functions
ρk(x1, . . . , xk) = det[K(xi, xj)]1≤i,j≤k ,
for some kernel K(x, y). Let I be a possibly inﬁnite interval I ⊂R. By [K]I we
denote the operator in L2(I, dx) obtained by restricting the kernel on I ×I. Assume
[K]I is a trace class operator. Then the intersection of the random conﬁguration
X with I is ﬁnite almost surely and
Prob{|X ∩I| = N} = (−1)N
N!
dN
dzN det

1 −z[K]I


z=1
.
In particular, the probability that X ∩I is empty is equal to
Prob{X ∩I = ∅} = det

1 −[K]I

.
ASYMPTOTICS OF PLANCHEREL MEASURES
501
More generally, if I1, . . . , Im is a ﬁnite family of pairwise nonintersecting intervals
such that the operators [K]I1, . . . , [K]Im are trace class, then
(4.2)
Prob{|X ∩I1| = N1, . . . , |X ∩Im| = Nm}
= (−1)
P Ni
Q Ni!
∂N1+···+Nm
∂zN1
1
. . . ∂zNm
m
det

1 −z1[K]I1 −· · · −zm[K]Im


z1=···=zm=1
.
Here operators {[K]Ii} are considered to be acting in the same Hilbert space, for
example, in L2(I1 ⊔I2 ⊔· · · ⊔Im, dx).
In the case of intersecting intervals I1, . . . , Im, the probabilities
Prob{|X ∩I1| = N1, . . . , |X ∩Im| = Nm}
are ﬁnite linear combinations of expressions of the form (4.2). Therefore, in order
to show the convergence in distribution of point processes with determinantal cor-
relation functions, it suﬃces to show the convergence of expressions of the form
(4.2).
The formula (4.2) is discussed, for example, in [37]. See also Theorem 2 in [35].
It remains valid for processes on a lattice such as Z in which case the kernel K
should be an operator in ℓ2(Z).
As veriﬁed, for example, in Proposition A.11 in the Appendix, the right-hand side
of (4.2) is continuous in each [K]Ii with respect to the trace norm. We shall show
that after a suitable embedding of ℓ2(Z) into L2(R) the kernel J(x, y; θ) converges
to the Airy kernel A(x, y) as θ →∞.
Namely, we shall consider a family of embeddings ℓ2(Z) →L2(R), indexed by a
positive number r > 0, which are deﬁned by
ℓ2(Z) ∋χk 7→r1/6 χh
k−2r
r1/3 , k+1−2r
r1/3
i ∈L2(R) ,
k ∈Z ,
(4.3)
where χk ∈ℓ2(Z) is the characteristic function of the point k ∈Z and, similarly,
the function on the right is the characteristic function of a segment of length r−1/3.
Observe that this embedding is isometric. Let Jr denote the kernel on R×R that is
obtained from the kernel J( · , · , r2) on Z × Z using the embedding (4.3). We shall
establish the following
Proposition 4.3. We have
[Jr][a,∞) →[A][a,∞) ,
r →∞,
in the trace norm for all a ∈R uniformly on compact sets in a.
This proposition immediately implies Theorem 5 as follows.
Proof of Theorem 5. Consider the left-hand side of (4.1) and choose for each ai a
pair of functions k−
i (r), k+
i (r) ∈Z such that
k−
i (r) −2r
r1/3
= a−
i (r) ≤ai ≤a+
i (r) = k+
i (r) −2r
r1/3
and a−
i (r), a+
i (r) →ai as r →∞. Then, on the one hand, the probability in the
left-hand side of (4.1) lies between the corresponding probabilities for a−
i (r) and
a+
i (r). On the other hand, the probabilities for a−
i (r) and a+
i (r) can be expressed
in the form (4.2) for the kernel Jr and by Proposition 4.3 and continuity of the Airy
kernel they converge to the corresponding probabilities given by the Airy kernel as
r →∞.
502
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Now we get to the proofs of Propositions 4.1 and 4.3 which will require some
computations. Recall that the Airy function can be expressed in terms of Bessel
functions as follows:
A(x) =



1
π
p x
3 K 1
3

2
3x
3
2

,
x ≥0 ,
√
|x|
3
h
J 1
3

2
3|x|
3
2

+ J−1
3

2
3|x|
3
2
i
,
x ≤0
(4.4)
(see Section 6.4 in [43]). Also recall that
A(x) ∼
1
2x1/4√π e−2
3 x3/2 ,
x →+∞
(4.5)
(see, for example, the formula 7.23 (1) in [43]).
Lemma 4.4. For any x ∈R we have

r
1
3 J2r+xr
1
3 (2r) −A(x)

 = O(r−1
3 ) ,
r →∞,
(4.6)
moreover, the constant in O(r−1
3 ) is uniform in x on compact subsets of R.
Proof. Assume ﬁrst that x ≥0. We denote
ν = 2r + xr
1
3 ,
α = arccosh

1 + xr−2
3 /2

≥0.
It will be convenient to use the following notation:
P = ν(tanh α −α),
Q = ν
3 tanh3 α.
The formula 8.43(4) in [43] reads
Jν(2r) = tanh α
π
√
3 eP +QK 1
3 (Q) + 3γ1
ν
eP
(4.7)
where |γ1| < 1. We have the following estimates as r →+∞:
α = x
1
2 r−1
3 + O(r−1),
tanh α = α + O(α3) = x
1
2 r−1
3 + O(r−1),
P + Q = ν · O(α5) = O(r−2
3 ),
eP +Q = 1 + O(r−2
3 ),
Q = 1
3

2r + xr
1
3
 
x
3
2 r−1 + O(r−4
3 )

= 2x
3
2
3
+ O(r−1
3 ),
K 1
3 (Q) = K 1
3
 
2x
3
2
3
!
+ O(r−1
3 ),
P ≤0,
3γ1
ν
eP = O(r−1).
Substituting this into (4.7), we obtain the claim (4.6) for x ≥0.
Assume now that x ≤0. Denote
ν = 2r + xr
1
3 ,
β = arccos

1 + xr−2
3 /2

≥0,
y = |x|.
Introduce the notation
eP = ν(tan β −β),
eQ = ν
3 tan3 β .
ASYMPTOTICS OF PLANCHEREL MEASURES
503
The formula 8.43 (5) in [43] reads
(4.8)
Jν(r) = 1
3 tan β cos

eP −eQ
 h
J−1
3

eQ

+ J 1
3

eQ
i
+ 1
√
3 tan β sin

eP −eQ
 h
J−1
3

eQ

−J 1
3

eQ
i
+ 24γ2
ν
where |γ2| < 1. Again we have the estimates as r →+∞
β = y
1
2 r−1
3 + O(r−1),
tan β = β + O(β3) = y
1
2 r−1
3 + O(r−1),
eP −eQ = ν · O(β5) = O(r−2
3 ),
cos

eP −eQ

= 1 + O(r−4
3 ),
sin

eP −eQ

= O(r−2
3 ),
eQ = 1
3

2r −yr
1
3
 
y
3
2 r−1 + O(r−4
3 )

= 2y
3
2
3
+ O(r−1
3 ),
J± 1
3

eQ

= J± 1
3
 
2y
3
2
3
!
+ O(r−1
3 ).
These estimates after substituting into (4.8) produce (4.6) for x ≤0.
Lemma 4.5. There exist C1, C2, C3, ε > 0 such that for any A > 0 and s > 0 we
have

Jr+Ar
1
3 +s(r)

 ≤C1 r−1
3 exp

−C2

A
3
2 + sA
1
2 r−1
3

,
s ≤εr ,
(4.9)

Jr+Ar
1
3 +s(r)

 ≤exp (−C3(r + s)) ,
s ≥εr ,
(4.10)
for all r ≫0.
Proof. First suppose that s ≤εr. Set ν = r + Ar
1
3 + s. We shall use (4.7) with
α = arccosh(ν/r). Provided ε is chosen small enough and r is suﬃciently large, α
will be close to 0 and we will be able to use Taylor expansions. For r ≫0 we have
α = arccosh(1 + Ar−2
3 + sr−1) ≥const (Ar−2
3 + sr−1)
1
2 ,
and, similarly,
−P = ν(α −tanh α) ≥const (A + sr−1
3 )
3
2 .
Since the function x
3
2 is concave, we have
−P ≥const (A
3
2 + sA
1
2 r−1
3 ) .
The constant here is strictly positive.
Since K 1
3 (x) ≤const x−1
2 e−x (see, for example, the formula 7.23 (1) in [43]) we
obtain
tanh α eP +QK 1
3 (Q) ≤const
eP
√
ν tanh α
≤const
r
1
3
exp

−const

A
3
2 + sA
1
2 r−1
3

,
504
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
where we used that tanh α ≥const r−1
3 . Finally, we note that
eP
ν ≤1
r exp

−const

A
3
2 + sA
1
2 r−1
3

,
and this completes the proof of (4.9).
The estimate (4.10) follows directly from the formulas 8.5 (9), (4), (5) in [43].
Lemma 4.6. For any δ > 0 there exists M > 0 such that for all x, y > M and
large enough r

J

2r + xr
1
3 , 2r + yr
1
3 , r2

 < δr−1
3 .
Proof. From (2.15) we have
J

2r + xr
1
3 , 2r + yr
1
3 , r2
=
∞
X
s=1
J2r+xr
1
3 +s(2r) J2r+yr
1
3 +s(2r).
(4.11)
Let us split the sum in (4.11) into two parts,
X
1 =
X
l≤εr
,
X
2 =
X
l>εr
,
that is, one sum for l ≤εr and the other for l > εr, and apply Lemma 4.5 to these
two sums. Note that 2r here corresponds to r in Lemma 4.5; this produces factors
of 2
1
3 and does not aﬀect the estimate.
Let the ci’s stand for some positive constants not depending on M. From (4.9)
we obtain the following estimate for the ﬁrst sum:
X
1 ≤c1 r−2
3 exp

−c2 M
3
2
 [εr]
X
s=1
qs
where
q = exp

−c2M
1
2 r−1
3

,
0 < q < 1 .
Therefore,
X
1 ≤
c1 r−2
3 exp

−c2 M
3
2

1 −q
≤r−1
3 · c3 exp(−c2M
3
2 )M −1
2 .
We can choose M so that c3 exp(−c2M
3
2 )M −1
2 < δ/2.
For the second sum we use (4.10) and obtain
X
2 ≤
X
s≥εr
exp(−c4(r + s)) ≤c5 exp(−c4r).
Clearly, this is less than δr−1
3 /2 for r ≫0.
Proof of Proposition 4.1. As shown in [10, 36], the Airy kernel has the following
integral representation:
A(x, y) =
Z ∞
0
A(x + t)A(y + t)dt.
(4.12)
ASYMPTOTICS OF PLANCHEREL MEASURES
505
The formula (4.11) implies that for any integer N > 0
(4.13)
J

2r + xr
1
3 , 2r + yr
1
3 , r2
=
N
X
s=1
J2r+xr
1
3 +s(2r) J2r+yr
1
3 +s(2r)
+ J

2r + xr
1
3 + N, 2r + yr
1
3 + N, r2
.
Let us ﬁx δ > 0 and pick M > 0 according to Lemma 4.6. Since, by assumption, x
and y lie in a compact set of R, we can ﬁx m such that x, y ≥m. Set
N = [(M −m + 1) r
1
3 ] .
Then the inequalities
x + Nr−1
3 > M,
y + Nr−1
3 > M
are satisﬁed for all x, y in our compact set and Lemma 4.4 applies to the sum in
(4.13). We obtain

r
2
3
N
X
s=1
J2r+xr
1
3 +s(2r) J2r+yr
1
3 +s(2r) −
N
X
s=1
A(x + sr−1
3 )A(y + sr−1
3 )

 = O(1)
because the number of summands is N = O(r
1
3 ) and A(x) is bounded on subsets
of R which are bounded from below. Note that
r−1
3
N
X
s=1
A(x + sr−1
3 )A(x + sr−1
3 )
is a Riemann integral sum for the integral
M−m+1
Z
0
A(x + t)A(y + t) dt,
and it converges to this integral as r →+∞. Since the absolute value of the second
term in the right-hand side of (4.13) does not exceed δr−1
3 by the choice of N, we
get

r
1
3 J

2r + xr
1
3 , 2r + yr
1
3 , r2
−
M−m+1
Z
0
A(x + t)A(y + t)dt

≤δ + o(1)
as r →+∞, and this estimate is uniform on compact sets. Now let δ →0 and
M →+∞. By (4.5) the integral (4.12) converges uniformly in x and y on compact
sets and we obtain the claim of the proposition.
Proof of Proposition 4.3. It is clear that Proposition 4.1 implies the convergence
of [Jr]a to [A]a in the weak operator topology. Therefore, by Proposition A.9, it
remains to prove that tr[Jr]a →tr[A]a as r →+∞. We have
tr[Jr]a =
∞
X
k=[2r+ar
1
3 ]
J(k, k; r2) + o(1) ,
506
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
where the o(1) correction comes from the fact that a may not be a number of the
form k−2r
r1/3 , k ∈Z. By (4.11) we have
∞
X
k=[2r+ar
1
3 ]
J(k, k; r2) =
∞
X
l=1
l

J[2r+ar
1
3 ]+l(2r)
2
.
(4.14)
Similarly,
tr[A]a =
Z ∞
a
A(s, s)ds =
Z ∞
0
t(A(a + t))2dt .
(4.15)
Since we already established the uniform convergence of kernels on compact sets,
it is enough to show that both (4.14) and (4.15) go to zero as a →+∞and r →+∞.
For the Airy kernel this is clear from (4.5). For the kernel Jr it is equivalent to the
following statement: for any δ > 0 there exists M0 > 0 such that for all M > M0
and large enough r we have

∞
X
l=1
l J2
2r+Mr
1
3 +l(2r)

 < δ .
(4.16)
We shall employ Lemma 4.5 for A = M. Again, we split the sum in (4.16) into two
parts:
X
1 =
X
l≤εr
,
X
2 =
X
l>εr
.
For the ﬁrst sum Lemma 4.5 gives
X
1 ≤c1r−2
3 exp

−c2M
3
2
 X
l≤[εr]
l ql ,
where
q = exp

−c2M
1
2 r−1
3

,
0 < q < 1 ,
and the ci’s are some positive constants that do not depend on M. Since P l ql =
q(1 −q)−2 we obtain
X
1 ≤c1r−2
3 exp

−c2M
3
2

q
(1 −q)2 ≤c3
exp

−c2M
3
2

M
.
This can be made arbitrarily small by taking M suﬃciently large.
For the other part of the sum we have the estimate
X
2 ≤
X
l>εr
l exp(−c4(r + l))
which, evidently, goes to zero as r →+∞.
