---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-007-322-spectral-trace-and-its-factorisation
section_title: "Spectral trace and its factorisation"
section_number: 3.2.2
pages: 20-24
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
According to the TS/ST correspondence [18, 19], we should promote the mirror curve (3.12) to
the diﬀerence operator
OF0(mF0) = ex +mF0e−x + ey + e−y, (3.41)
where x and y are Heisenberg operators, satisfying the commutation relation
[x, y] = iℏ. (3.42)
Then the inverse operator ρF0 =O−1
F0 is of trace class [59] and its Fredholm determinant as
well as fermionic spectral traces ZN(ℏ) can be deﬁned. Furthermore the latter can be computed
explicitly [43].
The integral kernel for ρF0 was obtained in [43] for real ℏ, and it reads
ρF0(x1,x 2) = e−b2ξ/2+πb(x1+x2)/2
2b cosh(πx1−x2
b )
Φb(x1− bξ/2π + ib/4) Φb(x2 + bξ/2π + ib/4)
Φb(x1 + bξ/2π− ib/4) Φb(x2− bξ/2π− ib/4). (3.43)
The parameter ξ is related to the mass parameter mF0 by
mF0 = e2b2ξ, (3.44)
and b is related to ℏ by
ℏ =πb2. (3.45)
As we mentioned above, we need to perform an analytic continuation of the spectral theory of
ρF0 to complex ℏ. Since we have an explicit expression (3.43) for its integral kernel, this is easy
to do. We just note that Faddeev’s quantum dilogarithm can be analytic continued to all values
of b such that b2 /∈ R≤0. Therefore, (3.43) deﬁnes the integral kernel of the operator for ℏ∈ C′,
as required in (3.6).
The ﬁrst spectral trace has the following integral representation:
TrρF0 = e−b2ξ/2
2b
∫
R
eπbx Φb(x− bξ/2π + ib/4) Φb(x + bξ/2π + ib/4)
Φb(x + bξ/2π− ib/4) Φb(x− bξ/2π− ib/4)dx, (3.46)
while the fermionic trace is
Z1(mF0, ℏ) = TrρF0. (3.47)
We will only be interested in the simple case ξ = 0, where the integral reads
TrρF0 = 1
2b
∫
R
eπbx Φb(x + ib/4)2
Φb(x− ib/4)2 dx. (3.48)
– 19 –
Note that the integrand mostly consists of the product of quantum dilogarithms, and the spectral
trace is therefore very similar to state integrals in complex Chern-Simons theory. Due to this
reason, we will sometimes refer to the integral representation of spectral traces as state integrals.
The integrand of (3.48) is integrable for Re b> 0, which we always assume, and the spectral
trace (3.48) is an analytic function of ℏ∈ C′. When ℏ > 0, a conjecture of [18] states that it
can be computed in terms of the so-called modiﬁed grand potential of local F0, which is fully
speciﬁed by BPS invariants of the CY threefold. This conjecture can be extended to complex ℏ,
provided Re(ℏ)> 0 (otherwise the large radius expansion embodied in the grand potential does
not converge). We have explicitly veriﬁed this extended conjecture in many cases. Therefore,
our analytic continuation of the trace to complex ℏ matches the natural analytical continuation
of the modiﬁed grand potential, in such a way that the conjecture of [18] remains true.
We now show that the minimal resurgent structure{Φ0,n(gs), Φ1,n(gs)} can be recovered by
performing a saddle point analysis of the state integral, but we hasten to comment that this
is rather exceptional due to the particular nice form of the integrand in (3.48). In general, as
we will see in Section 3.3.3, one cannot easily recover the minimal resurgent structure from the
integral representation of the spectral traces.
In the limit ℏ→∞,gs =−1/ℏ→ 0, the integrand has the semiclassical expansion
exp
∞∑
n=0
g2n−1
s Vn(˜x, b), ˜x = 2πb−1x, (3.49)
where
V0(˜x, b) =− 1
2π2i
(
πi˜x + 2 Li2(−ie˜x)− 2 Li2(ie˜x)
)
. (3.50)
The saddle point equation
∂V0(˜x)
∂˜x =− 1
2π2i
(
πi− 2 log 1 + ie˜x
1− ie˜x
)
= 0 (3.51)
has two sets of solutions
˜x =
{
2πiZ,
πi + 2πiZ. (3.52)
By expanding the integrand in the semiclassical limit around these saddle points, and performing
Gaussian integration order by order in gs, we obtain two inﬁnite sets of asymptotic series. After
proper normalisation they are precisely Φ 0,n(gs) and Φ 1,n(gs), as deﬁned in (3.20), (3.22). 7 We
want to point out that this in fact provides a very eﬃcient way to compute the series Φ( gs), and
we are able to compute 400 terms of Φ( gs).
Next, we demonstrate that the integral (3.48) can be evaluated explicitly by closing the
contour from above and summing up residues, and show that the result factorises as a sum of
products of holomorphic and anti-holomorphic blocks given by q and ˜q-series respectively, where
q = e2πib2
, ˜q = e−2πib−2
. (3.53)
Note the deﬁnition of q here is consistent with (3.36). Throughout the section we will assume
that Im b2> 0 so that|q|,|˜q|< 1 and the q,˜q-series converge.
7If we plug ˜x = πi + 2πiZ in V0(˜x, b) we seem to ﬁnd the leading contribution exp( − 1
gs
(VF0 + i
2)) to Φ 1(gs).
However, as the singularity structure shown in Fig. 3 illustrates the correct leading contribution should be instead
exp(−
VF0
gs
).
– 20 –
It turns out it is more convenient to ﬁrst evaluate the integral (3.46) when ξ⁄= 0, as the
integrand of (3.46) has only simple poles, and then to evaluate the limit ξ→ 0. We assume that
ξ is small and since Re b> 0, the poles in the upper half plane are
± bξ
2π− ib
4 +cb + irb + isb−1, r,s = 0, 1, 2,..., (3.54)
where cb is deﬁned in (A.4). The residues at these poles can be computed using (A.6), and by
summing them up we ﬁnd
TrρF0 =−1
2e−b2ξ/2q1/8 (q;q)2
∞(−˜qe2ξ; ˜q)∞(−˜qe−2ξ; ˜q)∞
(q1/2;q)2∞(˜qe2ξ; ˜q)∞(˜qe−2ξ; ˜q)∞
coth(ξ) (I(ξ, b)−I (−ξ, b)) (3.55)
where
I(ξ, b) = eb2ξ/22φ1
(
q1/2,q 1/2
q ;q,q 1/2e2b2ξ
)
2φ1
(−1,−1
˜q ; ˜q,−˜qe−2ξ
)
(3.56)
and theq-hypergeometric function is deﬁned in (A.22). Note that, as we explained in section 3.1,
the holomorphic and the anti-holomorphic factors involve very diﬀerent functions, in contrast to
what happens in complex CS theory.
Before we turn oﬀ the mass parameter in the result, we notice that if we perform the shift
ξ↦→ξ +πi, the variable e 2b2ξ inI(ξ, b) transforms by
e2b2ξ↦→qe2b2ξ (3.57)
while the variable e−2ξ is invariant. This suggests to deﬁne the “massive” holomorphic blocks
A(x;q) =x1/42φ1
(
q1/2,q 1/2
q ;q,q 1/2x
)
, (3.58a)
B(x;q) =x−1/42φ1
(
q1/2,q 1/2
q ;q,q 1/2x−1
)
(3.58b)
=x−1/4 (q1/2;q)∞(qx−1;q)∞
(q;q)∞(q1/2x−1;q)∞
2φ1
(
q1/2,q 1/2x−1
qx−1 ;q,q 1/2
)
, (3.58c)
and “massive” anti-holomorphic blocks
~A(˜x; ˜q) = 2φ1
(−1,−1
˜q ; ˜q,−˜q˜x−1
)
, (3.59a)
~B(˜x; ˜q) = ~A(˜x−1; ˜q), (3.59b)
where
x = e2b2ξ, ˜x = e2ξ. (3.60)
The second expression of B(x;q) is obtained by applying Heine’s transformation (A.23). Both
holomorphic blocks satisfy the diﬀerence equation
(−1 +q3/2x)f(q2x;q) +q1/4(2−qx)f(qx;q) +q1/2(−1 +q1/2x)f(x;q) = 0. (3.61)
The Wronskian
W (x;q) = det
(A(x;q) B(x;q)
A(qx;q) B(qx;q)
)
(3.62)
– 21 –
can be identiﬁed as
W (x;q) =q−1/4 (q1/2;q)2
∞(qx;q)∞(x−1;q)∞
(q;q)2∞(q1/2x;q)∞(q−1/2x−1;q)∞
(3.63)
We now take the massless limit x↦→ 1. We ﬁnd that
A(qmeu;q) =gm(q) + 1
4Gm(q)u +O(u2), (3.64a)
B(qmeu;q) =hm(q)− 1
4Hm(q)u +O(u2), (3.64b)
where
gm(q) =qm/4
∞∑
n=0
(q1/2;q)2
n
(q;q)2n
qn/2+nm, m ≥ 0, (3.65a)
Gm(q) =qm/4
∞∑
n=0
(q1/2;q)2
n
(q;q)2n
qn/2+nm(1 + 4n), m ≥ 0, (3.65b)
as well as
hm(q) =qm/4
∞∑
n=0
(q1/2;q)n+m(q1/2;q)n
(q;q)n+m(q;q)n
qn/2, m ≥ 0, (3.66a)
Hm(q) =− 4q−m/4
m−1∑
n=0
(q1/2;q)n(q−1;q−1)m−n−1
(q;q)n(q−1/2;q−1)m−n
qn/2 m≥ 0
+qm/4
∞∑
n=0
(q1/2;q)n+m(q1/2;q)n
(q;q)n+m(q;q)n
qn/2

1− 4
∞∑
j=1
(
qj+n
1−qj+n− qj−1/2+n
1−qj−1/2+n
)
.
(3.66b)
We comment that when expanding B(qmeu;q) we need to use the second expression of B(x;q)
in (3.58c), since in the ﬁrst expression of B(qmeu;q) with m≥ 1, the power of q is not bounded
from below. In addition, we ﬁnd by explicit q-expansion that
hm(q) =gm(q), G 0(q) =H0(q). (3.67)
The seriesgm(q),Gm(q),hm(q) andHm(q) in (3.64) withm> 0 are the analogues of the “descen-
dants” introduced in [11, 12]. As we will see, although they do not appear in the expression for
the spectral trace, they are necessary to reconstruct the Stokes data. For the anti-holomorphic
block we ﬁnd the expansion
~A(e˜u; ˜q) = 2˜g0(˜q) + 4˜u ˜G0(˜q) +O(˜u2), (3.68)
where
˜g0(˜q) =1
2
∞∑
n=0
(−1; ˜q)2
n
(˜q; ˜q)2n
(−˜q)n, (3.69a)
˜G0(˜q) =− 1
4
∞∑
n=0
(−1; ˜q)2
n
(˜q; ˜q)2n
(−˜q)nn. (3.69b)
– 22 –
As an application of these results, we can take the massless limit of the factorisation formula
(3.55) and ﬁnd
TrρF0 =− i
2
(
G0(q)~g0(˜q) + 8b−2g0(q)~G0(˜q)
)
. (3.70)
Note that this is very similar to the factorization in holomorphic blocks of the state integral
invariant of the ﬁgure-eight knot in [75]. However, as noted above, the factorization is not sym-
metric, and the holomorphic and anti-holomorphic blocks are given by diﬀerent series. Another
important result is that in the massless limit the Wronskian identity (3.63) implies that
g0(G1 +H1)− 2g1G0 = 4q1/4
1−q1/2. (3.71)
