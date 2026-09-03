---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-031-3-q-const
section_title: "(Q) ≤const"
section_number: 3
pages: 23-26
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 35 sections: Introduction; Plancherel measures. Given a ﬁnite; Poissonization and correlation fun"
---
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
