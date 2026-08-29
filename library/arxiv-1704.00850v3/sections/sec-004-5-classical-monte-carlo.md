---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-004-5-classical-monte-carlo
section_title: "Classical Monte Carlo"
section_number: 5
pages: 9-17
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Throughout the remainder of the paper, we assume that P is a DA operator with Mtd given by (3), and
that (4) holds.
5 Classical Monte Carlo
Consider the Mtd given by
a(u,·) =
∫
SV
∫
SV
πU|V (·|v′)r(v,dv′)πV|U(v|u)ν(dv), u∈SU, (8)
where r(v,·), v∈ SV is an Mtf on SV with invariant pdf πV (·). We will show in this section that this
form has utility beyond constructing sandwich algorithms. Indeed, the k-step Mtd of a DA algorithm (or
a sandwich algorithm) can be re-expressed in the form (8). This motivates the development of a general
method for estimating the integral
∫
SU
a(u,u )µ(du), which is the main topic of this section.
We begin by showing howp(k)(u,·), u∈ SU can be written in the form (8). The case k = 1 is trivial.
Indeed, if r(v,·) is taken to be the kernel of the identity operator, then a(u,·) = p(u,·). Deﬁne an Mtd
9
q(v,·), v∈SV by
q(v,·) =
∫
SU
πV|U(·|u)πU|V (u|v)µ(du),
and letq(k)(v,·), k≥ 1 denote the correspondingk-step Mtd. If we let
r(v,dv′) =q(k−1)(v,v′)ν(dv′), v∈SV
fork≥ 2, thena(u,·) = p(k)(u,·). Next, consider the sandwich Mtd ˜p(k)(u,·), u∈SU. Again, the k = 1
case is easy. Taking
r(v,·) =s(v,·)
yieldsa(u,·) = ˜p(u,·). Now let
˜q(v,·) =
∫
SU
∫
SV
s(v′,·)πV|U(v′|u)πU|V (u|v)ν(dv′)µ(du),
and denote the correspondingk-step transition function by ˜q(k)(v,·). Then taking
r(v,·) =
∫
SV
˜q(k−1)(v′,·)s(v,dv′)
whenk≥ 2 yieldsa(u,·) = ˜p(k)(u,·).
The following proposition shows that, whenP is trace-class,
∫
SU
a(u,u )µ(du) is ﬁnite.
Proposition 3.
∫
SU
a(u,u )µ(du)<∞.
Proof. That
∫
SU
a(u,u )µ(du)<∞ is equivalent to
∫
SU
∫
SV
(∫
SV
πU,V (u,v′)
πU(u)πV (v′)r(v,dv′)
)( πU,V (u,v )
πU(u)πV (v)
)
πU(u)πV (v)ν(dv)µ(du)<∞. (9)
Note that ∫
SU
( πU,V (u,v )
πU(u)πV (v)
)2
πU(u)πV (v)µ(du)ν(dv) =
∫
SU
p(u,u )µ(du)<∞, (10)
and by Jensen’s inequality,
∫
SU
∫
SV
(∫
SV
πU,V (u,v′)
πU(u)πV (v′)r(v,dv′)
)2
πU(u)πV (v)ν(dv)µ(du)
≤
∫
SU
∫
SV
∫
SV
( πU,V (u,v′)
πU(u)πV (v′)
)2
r(v,dv′)πU(u)πV (v)ν(dv)µ(du)
=
∫
SU
∫
SV
( πU,V (u,v′)
πU(u)πV (v′)
)2
πU(u)πV (v′)ν(dv′)µ(du)
=
∫
SU
p(u,u )µ(du)
<∞.
(11)
The inequality (9) follows from (10), (11), and the Cauchy-Schwarz inequality.
10
Combining Proposition 3 and Theorem 2 leads to the following result: If P is trace-class and ˜p(u,·)
is representable, then ˜P is also trace-class. This is a generalization of Khare and Hobert’s (2011) Theo-
rem 1, which states that, under a condition on s(v,dv′) that implies representability, the trace-class-ness of
P implies that of ˜P .
We now develop a classical Monte Carlo estimator of
∫
SU
a(u,u )µ(du). Let ω :SV → [0,∞) be a pdf
that is almost everywhere positive. We will exploit the following representation of the integral of interest:
∫
SU
a(u,u )µ(du) =
∫
SV
∫
SU
(πV|U(v|u)
ω(v)
)(∫
SV
πU|V (u|v′)r(v,dv′)
)
ω(v)µ(du)ν(dv). (12)
Clearly,
η(u,v ) :=
(∫
SV
πU|V (u|v′)r(v,dv′)
)
ω(v)
deﬁnes a pdf onSU×SV , and if (U∗,V ∗) has joint pdfη(·,·), then
∫
SU
a(u,u )µ(du) = E
(πV|U(V∗|U∗)
ω(V∗)
)
.
Therefore, if{(U∗
i,V ∗
i )}N
i=1 are iid random elements fromη(·,·), then
1
N
N∑
i=1
πV|U(V∗
i|U∗
i )
ω(V∗
i ) (13)
is a strongly consistent and unbiased estimator of
∫
SU
a(u,u )µ(du). This is the Monte Carlo formula that is
central to our discussion.
Of course, we are mainly interested in the cases a(u,·) = p(k)(u,·) or a(u,·) = ˜p(k)(u,·). We now
develop algorithms for drawing from η(·,·) in these two situations. First, assume a(u,·) = p(k)(u,·). If
k = 1, thenr(u,·) is the kernel of the identity operator, and
η(u,v ) =πU|V (u|v)ω(v).
Ifk≥ 2, thenr(v,dv′) =q(k−1)(v,v′)dv′, and
η(u,v ) =
(∫
SV
πU|V (u|v′)q(k−1)(v,v′)ν(dv′)
)
ω(v) =
(∫
SU
p(k−1)(u′,u )πU|V (u′|v)µ(du′)
)
ω(v).
Thus, whenk≥ 2, we can draw fromη(u,v ) as follows: DrawV∗∼ω(·), then drawU′∼πU|V (·|v∗), then
drawU∗∼p(k−1)(u′,·), and return (u∗,v∗). Of course, we can draw from p(k−1)(u′,·) by simply running
k− 1 iterations of the original DA algorithm from starting valueu′. We formalize all of this in Algorithm 1.
Algorithm 1: Drawing (U∗,V ∗)∼η(·,·) whena(·,·) =p(k)(·,·).
11
1. Draw V∗ fromω(·).
2. Given V∗ =v∗, drawU′ fromπU|V (·|v∗).
3. If k = 1, setU∗ =U′. Ifk≥ 2, givenU′ =u′, drawU∗ fromp(k−1)(u′,·) by runningk−1 iterations
of the DA algorithm.
Similar arguments lead to the following algorithm for the sandwich algorithm
Algorithm 1S: Drawing (U∗,V ∗)∼η(·,·) whena(·,·) = ˜p(k)(·,·)
1. Draw V∗ fromω(·).
2. Given V∗ =v∗, drawV′ froms(v∗,·).
3. Given V′ =v′ drawU′ fromπU|V (·|v′).
4. If k = 1, setU∗ =U′. Ifk≥ 2, givenU′ =u′, drawU∗ from ˜p(k−1)(u′,·) by runningk−1 iterations
of the sandwich algorithm.
It is important to note that we do not need to know the representing conditionals πU| ˜V (·|v) andπ ˜V|U(·|u)
from (7) in order to run Algorithm 1S.
As with all classical Monte Carlo techniques, a key element in successful implementation is a ﬁnite
variance. Deﬁne
D2 = var
(πV|U(V∗|U∗)
ω(V∗)
)
.
Of course,D2<∞ if and only if
∫
SV
∫
SU
(πV|U(v|u)
ω(v)
)2
η(u,v )µ(du)ν(dv)<∞. (14)
The following theorem provides a sufﬁcient condition for ﬁnite variance.
Theorem 4. The variance,D2, is ﬁnite if
∫
SV
∫
SU
π3
V|U(v|u)πU|V (u|v)
ω2(v) µ(du)ν(dv)<∞. (15)
Proof. First, note that (14) is equivalent to
∫
SV
∫
SU
(π2
V|U(v|u)
πV (v)ω(v)
)(∫
SV
πU|V (u|v′)r(v,dv′)
πU(u)
)
πU(u)πV (v)µ(du)ν(dv)<∞.
12
Now, it follows from (15) that
∫
SV
∫
SU
(π2
V|U(v|u)
πV (v)ω(v)
)2
πU(u)πV (v)µ(du)ν(dv)<∞. (16)
Moreover, by Jensen’s inequality,
∫
SV
∫
SU
(∫
SV
πU|V (u|v′)r(v,dv′)
πU(u)
)2
πU(u)πV (v)µ(du)ν(dv)
≤
∫
SV
∫
SU
∫
SV
(πU|V (u|v′)
πU(u)
)2
r(v,dv′)πU(u)πV (v)µ(du)ν(dv)
=
∫
SV
∫
SU
(πU|V (u|v′)
πU(u)
)2
πU(u)πV (v′)µ(du)ν(dv′)
=
∫
SU
p(u,u )µ(du)
<∞.
(17)
The conclusion now follows from (16), (17), and Cauchy-Schwarz.
Theorem 4 implies that an ω(·) with heavy tails is more likely to result in ﬁnite variance (which is not
surprising). It might seem natural to take ω(·) = πV (·). However, in practice, we are never able to draw
fromπV (·). (If we could do that, we would not need MCMC.) Moreover, setting ω(·) to beπV (·) does not
always result in a ﬁnite variance. On the other hand, it can be beneﬁcial to use ω(·)s resembling πV (·), as
we argue in Section 6.
When an appropriate ω(·) is difﬁcult to ﬁnd, one can construct an alternative Monte Carlo estimator as
follows. Let ψ :SU→ [0,∞) be a pdf that is positive almost everywhere. The following dual of (12) may
also be used to represent
∫
SU
a(u,u )µ(du):
∫
SU
a(u,u )µ(du) =
∫
SU
∫
SV
∫
SV
πU|V (u|v)
ψ(u) r(v′,dv )πV|U(v′|u)ψ(u)ν(dv′)µ(du).
Now suppose that{(U∗
i,V ∗
i )}N
i=1 are iid from
ζ(u,v )µ(du)ν(dv) =
(∫
SV
r(v′,dv )πV|U(v′|u)ν(dv′)
)
ψ(u)µ(du).
The analogue of (13) is the following classical Monte Carlo estimator of
∫
SU
a(u,u )µ(du):
1
N
N∑
i=1
πU|V (U∗
i|V∗
i )
ψ(U∗
i ) . (18)
We now state the obvious analogues of Algorithms 1 and 1S.
Algorithm 2: Drawing (U∗,V ∗)∼ζ(·,·) whena(·,·) =p(k)(·,·).
13
1. Draw U∗ fromψ(·).
2. If k = 1, setU′ =U∗. Ifk≥ 2, givenU∗ =u∗, drawU′ fromp(k−1)(u∗,·).
3. Given U′ =u′, drawV∗ fromπV|U(·|u′).
Algorithm 2S: Drawing (U∗,V ∗)∼ζ(·,·) whena(·,·) = ˜p(k)(·,·).
1. Draw U∗ fromψ(·).
2. If k = 1, setU′ =U∗. Ifk≥ 2, givenU∗ =u∗, drawU′ from ˜p(k−1)(u∗,·).
3. Given U′ =u′, drawV′ fromπV|U(·|u′).
4. Given V′ =v′, drawV∗ froms(v′,·).
LetD′2 be the variance ofπU|V (U∗|V∗)/ψ(U∗) underζ. To ensure that it’s ﬁnite, we only need
∫
SU
∫
SV
∫
SV
(πU|V (u|v)
ψ(u)
)2
r(v′,dv )πV|U(v′|u)ψ(u)ν(dv′)µ(du)<∞. (19)
The following result is the analogue of Theorem 4.
Corollary 5. The variance,D′2, is ﬁnite if
∫
SU
∫
SV
π3
U|V (u|v)πV|U(v|u)
ψ2(u) ν(dv)µ(du)<∞. (20)
Proof. Note that the left hand side of (19) is equal to
∫
SU
∫
SV
(∫
SV
π2
U|V (u|v)
ψ(u)πU(u)r(v′,dv )
)(πV|U(v′|u)
πV (v′)
)
πU(u)πV (v′)ν(dv′)µ(du).
Apply the Cauchy-Schwarz inequality, then utilize Jensen’s inequality to get rid of r(v′,dv ), and ﬁnally
make use of (20) and the fact thatP is trace-class.
Typically, it’s easy to select a good sampling densityω(·) for Algorithm 1 whenSV is low dimensional,
or to select a good ψ(·) for Algorithm 2 whenSU is low dimensional. For DA algorithms used in Bayesian
models, it’s often the case that dim (SU) = p, and dim (SV ) = n, where p and n are, respectively, the
number of unknown parameters in the model and the number of observations. When this is the case, the
estimator (13) is likely to be efﬁcient whenn is small, while (18) is likely to be efﬁcient whenp is small.
14
Suppose that we have obtained estimates of sk andsk−1 based on (13) or (18), call them s∗
k ands∗
k−1.
Thenu∗
k = (s∗
k− 1)1/k andl∗
k = (s∗
k− 1)/(s∗
k−1− 1) serve as point estimates of uk andlk, respectively.
When our estimators have ﬁnite variances, we can acquire, via the delta method, conﬁdence intervals foruk
andlk. Assume that a conﬁdence interval for lk is (ak,bk) and a conﬁdence interval for uk is (ck,dk), then
(ak,dk) is an interval estimate forλ1. Interval estimates of ˜λ1 can be derived in a similar fashion.
It’s worth pointing out thatuk is a nontrivial upper bound onλ1∈ [0, 1) only ifsk < 2. The parameterk
can be determined sequentially. Take Algorithm 1 for example. Suppose that we have drawn N iid copies
of (U∗,V ∗) fromη(·,·) witha(·,·) =p(k)(·,·), but ﬁnd thats∗
k is not small enough for our purposes. Since
sk is decreasing in k, we wish to increase k by a positive integer j. To draw (U∗∗,V ∗∗) fromη(·,·) with
a(·,·) = p(k+j)(·,·), we only need to set V∗∗ = V∗, and draw U∗∗ fromp(j)(U∗,·). This procedure can
be repeated until the estimated power sum s∗
k+j is decreased to a satisfactory value. More guidance on the
choice ofk can be found in the next section.
6 Efﬁciency of the algorithm
To obtain an interval estimate of λ1 based on (13) or (18), one needs to run N iterations of Algorithm 1
or 2. If the time needed to simulate one step of the DA chain is τ, then the time needed to run N iterations
of Algorithm 1 or 2 is approximately kNτ . Note that signiﬁcant speedup can be achieved through parallel
computing, since theN iterations are carried out independently. Givenk andN, the accuracy of the estimate
depends on two factors: 1. The distance between lk anduk, and 2. The errors in the estimates, l∗
k andu∗
k.
We now brieﬂy analyze these two factors, and give some additional guidelines regarding the choice of ω(·)
andψ(·).
As before, suppose that
1 =λ0>λ 1 =λ2 =··· =λm>λ m+1≥···≥ λκ> 0
for somem< ∞. Clearly, ask→∞ ,
sk− 1 =λk
1
(
m +O
(
λk
m+1/λk
1
))
.
Hence, ask→∞ ,
lk := sk− 1
sk−1− 1 =λ1
(
1 +O
(
λk−1
m+1/λk−1
1
))
,
15
and
uk := (sk− 1)1/k
=λ1m1/k
(
1 +O
(
k−1λk
m+1/λk
1
))
=λ1
(
1 + (logm)O
(
k−1))(
1 +O
(
k−1λk
m+1/λk
1
))
.
=



λ1
(
1 +O
(
k−1λk
2/λk
1
))
m = 1
λ1
(
1 +O
(
k−1))
m> 1.
Depending on whetherm = 1 or not,uk−lk decreases at either a geometric or polynomial rate ask grows.
The errors ofl∗
k andu∗
k arise from those ofs∗
k ands∗
k−1. We now consider the estimator (18) for estimating
sk. Its variance is given by
D′2
N = 1
N
{∫
SU
∫
SV
∫
SV
(πU|V (u|v)
ψ(u)
)2
r(v′,dv )πV|U(v′|u)ψ(u)ν(dv′)µ(du)−s2
k
}
= 1
N
{∫
SU
∫
SV
∫
SU
π2
U|V (u|v)
ψ(u) πV|U(v|u′)p(k)(u,u′)µ(du′)ν(dv)µ(du)−s2
k
}
.
Note that
pk
(
(u,v ), (u′,v′)
)
:=πV|U(v′|u′)p(k)(u,u′)
gives thek-step Mtd of a Gibbs chain whose stationary pdf isπU,V (·,·). Thus, under suitable conditions, for
almost anyu∈SU,
lim
k→∞
sk(u) := lim
k→∞
∫
SV
∫
SU
π2
U|V (u|v)
ψ(u) πV|U(v|u′)p(k)(u,u′)µ(du′)ν(dv)
=
∫
SV
∫
SU
π2
U|V (u|v)
ψ(u) πU,V (u′,v )µ(du′)ν(dv)
= p(u,u )πU(u)
ψ(u) .
Ask→∞ , we expect
D′2 =
∫
SU
sk(u)µ(du)−s2
k→
∫
SU
p(u,u )πU(u)
ψ(u) µ(du)− 1.
Suppose thatψ(u)≈πU(u), then heuristically,
∫
SU
p(u,u )πU(u)
ψ(u) µ(du)− 1≈
∫
SU
p(u,u )µ(du)− 1 =s1− 1.
Thus, if the sum ofP ’s eigenvalues,s1, is relatively small, we recommend pickingψ(·)s that resembleπU(·),
with possibly heavier tails (to ensure that the moment condition (20) holds). By a similar argument, when
using the estimator (13), pickingω(·)s that resembleπV (·) is likely to controlD2 arounds1− 1 for largeks.
16
While (under suitable conditions) the variance of s∗
k converges to a constant as k→∞ , this is not the
case for u∗
k andl∗
k (becauseuk andlk are non-linear in sk andsk−1). In fact, using the delta method, one
can show that these variances are unbounded. Thus, there’s a trade-off between decreasing uk−lk (by
increasingk) and controlling the errors of u∗
k andl∗
k. We do not recommend increasing k indeﬁnitely. As
long ask is large enough so that sk− 1 is signiﬁcantly smaller than 1,uk serves as a non-trivial (and often
decent) upper bound forλ1.
