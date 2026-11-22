---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-006-6-estimates
section_title: "Estimates"
section_number: 6
pages: 11-14
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
toc_source: outline
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
In this section we provide estimates for the valuations of the coeﬃcients in the
power series gn(v) of Proposition 4.3, Fn,ζ(t) of Proposition 4.4 and Hn(t) of Propo-
sition 5.8. We shall use these in Section 7 to know how many terms of those power
series we have to calculate in order to compute Lin(z) up to a speciﬁed precision
for a given z̸ = 1 in Cp.
Many expressions in Sections 6 through 8 contain the real logarithm with base
p, denoted logp, which should not be confused with the chosen branch of the p-adic
logarithm, denoted log. In order to avoid another possible confusion we denote the
real logarithm by ln.
For the coeﬃcients of gn(v) we have the following result.
Proposition 6.1. For n ≥1 let
c(n, p) =
p
p −1 −n −1
ln(p) + (n −1) logp
n(p −1)
ln(p)

+ logp
2p(p −1)n
ln(p)

.
If
gn(v) = an,1v + an,2v2 + · · · ,
then
vp(an,k) ≥max

0,
k
p −1 −logp(k) −c(n, p)

.
Proof. We ﬁrst show that vp(an,k) ≥0. For this we recall that for a power se-
ries f(z) = 
i bizi converging on the closed unit disc, we have that max |bi| =
max|z|=1 |f(z)|, where z must be considered in the algebraic closure of the ﬁeld of
coeﬃcients (see [10, Example 3.3.2]), which will be Qp in our case. It thus suﬃces
to show that gn(z) = Li(p)
n (1−z−1) takes on integral values when |z| = 1. But then
|(1 −z−1) −1| = 1 so that we can apply Proposition 4.8.
Next we estimate vp(a0,k). Recall from Proposition 4.3 that
g0(v) = v −1 −
(v −1)p
vp −(v −1)p = v −1 + (v −1)p
∞

i=0
(pf(v))i ,
where vp −(v −1)p = 1 −pf(v) for some polynomial f(v) in Z[v] of degree p −1.
Then any term contributing to vk in g0(v) for k > 1 will come from a product
containing (pf(v))i with i ≥⌈(k −p)/(p −1)⌉, where ⌈x⌉is the smallest integer
greater than or equal to x. Therefore, also for k = 1,
(6.2)
vp(a0,k) ≥

k −p
p −1

.
We now prove the estimate for n ≥1. By Proposition 4.3 we have
g′
n+1(v) = −gn(v)
v
(1 + v + v2 + · · · )
= −an,1 −(an,1 + an,2)v −(an,1 + an,2 + an,3)v2 −· · ·
and consequently kan+1,k = −(an,1 + · · · + an,k) for k ≥1. Substituting v = 1,
which is in the range of convergence for gn, we ﬁnd
∞

i=1
an,i = gn(1) = Li(p)
n (0) = 0 .
1116
AMNON BESSER AND ROB DE JEU
It follows that kan+1,k = an,k+1 + an,k+2 + · · · . Therefore
vp(an+1,k) ≥min
j≥k+1{vp(an,j) −vp(k)} .
Iterating this and using (6.2) we obtain
vp(an,k) ≥
min
k=j0<j1<j2<···<jn

jn −p
p −1

−
n−1

i=0
vp(ji)

≥
min
k=j0<j1<j2<···<jn

jn −p
p −1 −
n−1

i=0
vp(ji)

.
We shall bound the last expression from below. We do this by ﬁrst considering
possible values of jn. Suppose that k + pl ≤jn < k + pl+1 for some integer l ≥0.
We then have the lower bound
(6.3)
jn −p
p −1 ≥k + pl −p
p −1
.
We now bound n−1
i=0 vp(ji) from above when k ≤j0 < · · · < jn−1 < k + pl+1 −1.
Clearly, among the pl+1 consecutive integers k, . . . , k + pl+1 −1 there is only one
integer divisible by pl+1, and its valuation is bounded by logp(k + pl+1).
The
remaining integers in this range are not divisible by pl+1, and their valuations are
bounded by l. Thus, we have
(6.4)
n−1

i=0
vp(ji) ≤(n −1)l + logp(k + pl+1) .
Combining the estimates (6.3) and (6.4) and taking the minimum over all possible
l’s we ﬁnally arrive at the estimate
vp(an,k) ≥min
0≤l∈Z
k + pl −p
p −1
−(n −1)l −logp(k + pl+1)

≥min
0≤l∈R
k + pl −p
p −1
−(n −1)l −logp(k + pl+1)

.
(6.5)
Computing this last minimum is a standard problem. We have
d
dl
k + pl −p
p −1
−(n −1)l −logp(k + pl+1)

= ln(p) · pl
p −1
−(n −1) −
pl+1
k + pl+1 .
This derivative is clearly positive for large l and is negative for l = 0 when n ≥2.
Consequently, for n ≥2 it must vanish at the value of l where the right-hand side
of (6.5) attains its minimal value, so that we get
ln(p) · pl
p −1
= n −1 +
pl+1
k + pl+1 .
Since the last summand is always between 0 and 1 we obtain the inequalities
n > ln(p) · pl
p −1
> n −1 ,
which implies that l < logp(n(p −1)/ ln(p)), pl/(p −1) > (n −1)/ ln(p) and pl+1 <
p(p −1)n/ ln(p).
Li(p)-SERVICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS
1117
We observe that those inequalities also hold if n = 1 and l = 0 so that they
hold where the right-hand side of (6.5) attains its minimum. Using them, as well
as ln(x + y) ≤ln(x) + ln(2y) for x, y ≥1, we ﬁnd that vp(an,k) is at least equal to
k −p
p −1 + n −1
ln(p) −(n −1) logp
n(p −1)
ln(p)

−logp(k) −logp
2p(p −1)n
ln(p)

=
k
p −1 −logp(k) −c(n, p)
as required.
□
Remark 6.6. Proposition 6.1 implies that gn(v) converges for |v| < p1/(p−1), as
stated in Theorem 2.7(3) and Proposition 4.3. The bound seems to have the right
behaviour, and only the constant c(n, p) may possibly be improved.
We now move on to estimates concerning the Fn,ζ(t)’s that were introduced
in Proposition 4.4. It is clear from (3.1) that the coeﬃcient of tk in Fn,0(t) has
valuation at least −n logp(k) for all k ≥1. For the corresponding statement for the
Fn,ζ(t)’s (with ζ̸ = 1 a root of unity of order relatively prime to p) we have to work
a little more.
Proposition 6.7. Let ζ̸ = 1 be a (pf −1)-th root of unity and write
Fn,ζ(t) = an,0 + an,1t + an,2t2 + · · ·
in Qp(ζ)[[t]]. Then an,0 is in pnZp[ζ], and for k ≥1 we have vp(an,k) ≥−n logp(k).
Proof. By Corollary 4.9 an,0 = Lin(ζ) lies in pnZp[ζ]. We proceed to prove the
other statement by induction on n. For n = 0 we have that Li0(z) =
z
1−z and so
F0,ζ(t) =
ζ+t
(1−ζ)−t. Because ζ does not reduce to 1 by assumption (1 −ζ) −t is a
unit in Zp[ζ][[t]], so F0,ζ(t) is in Zp[ζ][[t]]. For n ≥1 we see from (4.6) that
(6.8)
kan+1,k = −
k−1

j=0
(−ζ)j−kan,j .
Hence k an+1,k is a sum of elements with valuations vp(an,j), 0 ≤j ≤k −1, and so
for k ≥1, vp(an+1,k) ≥minj=0,...,k−1{vp(an,j)} −vp(k) ≥−n logp(k) −logp(k).
□
Remark 6.9. The proof of Proposition 6.7 actually shows that we have the slightly
better estimate vp(ak) ≥−logp

k!
max(0,k−n)!

for all k ≥0.
Finally, we consider the series Hn(t) for n ≥2 that were introduced in Proposi-
tion 5.8. For this we need a lemma concerning the Gn(t) = logn(1+t)/n! introduced
in the same proposition.
Lemma 6.10. For n ≥1 write
Gn(t) = an,1t + an,2t2 + an,3t3 + · · · .
Then vp(an,k) ≥−n logp(k) for all k ≥1.
Proof. We proceed by induction on n, the case n = 1 being clear. For n ≥2 we
have G′
n(t) = Gn−1(t)/(1 + t) so that, for k ≥1,
kan,k = ((−1)k−2an−1,1 + (−1)k−3an−1,2 + · · · + an−1,k−1) ,
and the statement follows easily (cf. the proof of Proposition 6.7).
□
1118
AMNON BESSER AND ROB DE JEU
Proposition 6.11. For n ≥2 write
Hn(t) = bn,0 + bn,1t + bn,2t2 + · · ·
in Qp[[t]]. Then vp(bn,0) ≥n −vp(n −1) −ϵp, where ϵp = 2 for p = 2 and ϵp = 1
otherwise. Moreover, vp(bn,k) ≥−n logp(k) for all k ≥1.
Proof. We begin with the statement for k = 0. It follows easily from (5.3) and
Corollary 4.9 that
vp(Hn(0)) = vp(En(1)) ≥n −min
p∤m>1{vp(mn−1 −1)}.
Now mn−1−1 will be divisible by ps for all m relatively prime to p precisely when the
exponent of (Z/ps)∗divides n −1. Therefore any such s satisﬁes s ≤vp(n −1) + ϵp
so that vp(Hn(0)) ≥n −vp(n −1) −ϵp.
We now observe that H2(t) = −
k≥1(−t)k/k2 by Proposition 5.8 and Re-
mark 5.12(1) so that the other statement holds if n = 2. If n ≥3, then (5.10)
gives
kbn,k = ((−1)k−1bn−1,0 + (−1)k−2bn−1,1 + · · · + bn−1,k−1) + an−1,k
with an−1,k as in Lemma 6.10, hence vp(an−1,k) ≥−(n −1) logp(k). Again the
statement follows by induction on n because (n −1) −vp(n −2) −ϵp ≥0 ≥
−logp(k).
□
