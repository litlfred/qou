---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-005-4-calculation-by-the-poisson-summation-formula
section_title: "Calculation by the Poisson summation formula"
section_number: 4
pages: 19-28
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Calculation by the Poisson summation formula
In this section, we calculate the sums corresponding to the integrals of the propositions in
the previous section by the Poisson summation formula. Corresponding to Propositions
3.1, 3.2, 3.4 and 3.5 in the previous section, we show Propositions 4.1, 4.2, 4.5 and 4.6
in this section. We use Proposition 4.6 in the proof of Theorem 1.1 in Section 5. We
remark that the Poisson summation formula has also been used in the study of large level
asymptotics of quantum invariants of Seifert 3-manifolds [13, 14, 30, 31, 32].
Recall (see e.g. [33]) that the Poisson summation formula states that
∑
m ∈Zn
f(m) =
∑
m ∈Zn
ˆf(m)
(30)
for a continuous integrable function f on Rn which satisﬁes that
|f(z)| ≤C
(
1 + |z|
)−n−δ,
| ˆf(z)| ≤C
(
1 + |z|
)−n−δ
(31)
for some C, δ > 0, where ˆf is the Fourier transform of f deﬁned by
ˆf(w) =
∫
Rn f(z) e−2π√−1 wT zdz.
Proposition 4.1. Let a, c be complex numbers satisfying that
Re a < 0,

Im c

 < −π
2 Re 1
a .
We put
Λ =
{ k
N + c ∈C

 k ∈Z, b0 ≤k
N ≤b1
}
,
19
C =
{
t + c ∈C

 t ∈R, b0 ≤t ≤b1
}
for some b0, b1 ∈R and ε0 > 0 satisfying that Re (b0 + c) < 0 < Re (b1 + c) and Re a(bi +
c)2 < −ε0 (i = 0, 1); see Figure 4. Then, there exists ε > 0 such that
1
N
∑
z ∈Λ
eN·az2 =
∫
C
eN·az2dz + O
(
e−εN)
.
We note that ε depends on a, c and ε0.
b0+c
b1+c
Λ
Figure 4: The domain {z ∈C | Re az2 < 0} is shaded.
Proof. By Proposition 3.1, the required formula is rewritten,
∑
k ∈Z
b0 ≤k/N ≤b1
eN·a(k/N+c)2 =
√π ·
√
N
√−a
+ O
(
e−εN)
.
Since
∑
k ∈Z
k/N < b0
eN·a(k/N+c)2 = O
(
e−εN)
,
∑
k ∈Z
b1 < k/N
eN·a(k/N+c)2 = O
(
e−εN)
,
for some ε > 0, it is suﬃcient to show that
∑
k ∈Z
eN·a(k/N+c)2 =
√π ·
√
N
√−a
+ O
(
e−εN)
.
(32)
In order to apply the Poisson summation formula (30), we put f(z) = eN·a(z/N+c)2. Then,
its Fourier transform is
ˆf(ζ) =
∫∞
−∞
eN·a(z/N+c)2−2π√−1 ζzdz
=
∫∞
−∞
e(a/N)(z+cN−π√−1ζN/a)2dz · eNπ2ζ2/a + 2π√−1 cNζ
=
√π ·
√
N
√−a
eNπ2ζ2/a + 2π√−1 cNζ,
20
where we obtain the last equality by Proposition 3.1. These f(z) and ˆf(ζ) satisfy the
assumption (31) of the Poisson summation formula. Hence, by the Poisson summation
formula (30),
∑
k ∈Z
eN·a(k/N+c)2 =
√π ·
√
N
√−a
∑
m ∈Z
eNπ2m2/a + 2π√−1 cNm.
The summand at m = 0 gives the right-hand side of (32). When m̸ = 0, the power of the
summand is
N · πm2(π
a + 2√−1 c
m
)
,
and its real part is negative by the assumption of the proposition. Hence, the summands
at m̸ = 0 are of order e−εN for some ε > 0. Therefore, we obtain (32).
We generalize Proposition 4.1 to the case where there are perturbative terms in the
exponential of the summand.
Proposition 4.2. We put
Λ =
{ k
N + c ∈C

 k ∈Z, b0 ≤k
N ≤b1
}
,
C =
{
t + c ∈C

 t ∈R, b0 ≤t ≤b1
}
for some b0, b1 ∈R and c ∈C. Let a be a complex number whose real part is negative, let
δ0 be a real positive number, and let ψ(z) be a holomorphic function of the form,
ψ(z) = az2 + b3z3 + b4z4 + · · · ,
deﬁned in a neighborhood of 0 including the δ0-neighborhood of C. The domain (15) has
two connected components in a neighborhood of 0. We assume that b0 + c and b1 + c are
in these two components respectively, and Re ψ(bi + c) < −ε0 (i = 0, 1) for some ε0 > 0.
(See Figure 5.) Further, we assume that
b0 + c and b1 + c are in the same connected component of
{
w + δ√−1 ∈C

 w ∈C, δ ∈[0, δ0], Re
(
ψ(w + δ√−1) −2πδ
)
< 0
}
,
(33)
and
they are in the same connected component of
{
w −δ√−1 ∈C

 w ∈C, δ ∈[0, δ0], Re
(
ψ(w −δ√−1) −2πδ
)
< 0
}
.
(34)
Then,
1
N
∑
z∈Λ
eN ψ(z) =
∫
C
eN ψ(z)dz + O(e−Nε)
for some ε > 0.
We note that ε depends on ψ(z), c, δ0 and ε0; in particular, ε directly depends on ε′
2 of
(39) in the proof of the proposition.
21
b0+c
b1+c
Λ
Figure 5: The domain {z ∈C | Re ψ(z) < 0} is shaded.
Proof. The sum of the left-hand side of the required formula is rewritten,
∑
k ∈Z
b0 ≤k/N ≤b1
exp
(
N · ψ
( k
N + c
))
.
(35)
In order to apply the Poisson summation formula (30), we put
f(z) = g
( z
N + c
)
exp
(
N · ψ
( z
N + c
))
,
where g is a diﬀerentiable function on R + c satisfying that
g(w) =
{
1
if w ∈C,
0
if w /∈N(C),
0 ≤g(w) ≤1
if w ∈N(C) −C.
Here, N(C) is a neighborhood of C in R+c such that N(C)−C is included in the domain
{
z ∈C

 Re ψ(z) < −ε0/2
}
. Then, the Fourier transform of f is given by
ˆf(ζ) =
∫
R
g
( z
N + c
)
exp
(
N · ψ
( z
N + c
))
e−2π√−1 ζzdz
= N
∫
R+c
g(w) eN
(
ψ(w) −2π√−1 ζ(w−c)
)
dw,
where we put w = z/N + c. Further,
ζ2 ˆf(ζ) = −
1
4π2N
∫
R+c
g(w) eN ψ(w)(( d
dw
)2e−2π√−1 Nζ(w−c))
dw
= −
1
4π2N
∫
R+c
(( d
dw
)2g(w) eN ψ(w))
e−2π√−1 Nζ(w−c)dw
= −
1
4π2N
∫
R+c
h(w) eN ψ(w) e−2π√−1 Nζ(w−c)dw,
where we put
h(w) = g′′(w) + 2 g′(w) ψ′(w) + g(w)
(
ψ′′(w) + ψ′(w)2)
.
22
Since the above integral is bounded independently of ζ, ˆf(ζ) satisﬁes the assumption (31)
of the Poisson summation formula. Further, f(z) also satisﬁes (31). Therefore, by the
Poisson summation formula (30),
(35) =
∑
m ∈Z
ˆf(m).
When m̸ = 0, we have that
ˆf(m) = −
1
4π2N · 1
m2
∫
R+c
h(w) eN
(
ψ(w)−2π√−1 m(w−c)
)
dw
= −
1
4π2N · 1
m2
∫
C
(
ψ′′(w) + ψ′(w)2)
eN
(
ψ(w)−2π√−1 m(w−c)
)
dw
(36)
−
1
4π2N · 1
m2
∫
N(C)−C
h(w) eN
(
ψ(w)−2π√−1 m(w−c)
)
dw,
(37)
since h(w) = ψ′′(w) + ψ′(w)2 for w ∈C and h(w) = 0 for w ∈(R + c) −N(C). Further,
since Re ψ(w) < −ε0/2 for w ∈N(C) −C,
∑
m̸=0
(37) = O(e−Nε1)
for some ε1 > 0. Furthermore, when m > 0, by pushing the contour C to a contour C′ in
the domain of (34), we can show that
∫
C
(
ψ′′(w) + ψ′(w)2)
eN
(
ψ(w)−2π√−1 m(w−c)
)
dw
=
∫
C′
(
ψ′′(w) + ψ′(w)2)
eN
(
ψ(w)−2π√−1 m(w−c)
)
dw = O(e−Nε2)
(38)
for some ε2 > 0, which we can choose independently of m, since there exists ε′
2 > 0 such
that
Re
(
ψ(w) −2π
√
−1 (w −c)
)
< −ε′
2
(39)
for any w ∈C′. Hence,
∑
m>0
(36) = O(e−Nε2).
When m < 0, by pushing the contour C into the domain of (33), we similarly obtain
∑
m<0
(36) = O(e−Nε3)
for some ε3 > 0. Therefore,
∑
m̸=0
ˆf(m) = O(e−Nε4)
for some ε4 > 0. Hence,
(35) =
ˆf(0) + O(e−Nε4) = N
∫
C
eN ψ(w)dw + O(e−Nε5)
for some ε5 > 0, and this implies the required formula.
23
Remark 4.3. The assumptions (33) and (34) of Proposition 4.2 can be replaced with the
condition that there exist positive integers m0, m1 and positive real numbers δ0, δ1 such
that for any integer m satisfying that −m0 < m < 0 or 0 < m < m1,
∫
C
eN
(
ψ(w)−2π√−1 m(w−c)
)
dw = O(e−Nε)
for some ε > 0, and
b0 + c and b1 + c are in the same connected component of
{
w + δ√−1 ∈C

 w ∈C, δ ∈[0, δ1], Re
(
ψ(w + δ√−1) −2πδm1
)
< 0
}
,
and
they are in the same connected component of
{
w −δ√−1 ∈C

 w ∈C, δ ∈[0, δ0], Re
(
ψ(w −δ√−1) −2πδm0
)
< 0
}
.
Proposition 4.2 for this assumption can be proved by modifying the above proof of Propo-
sition 4.2.
Remark 4.4. Proposition 4.2 can naturally be extended to the case where the holomor-
phic function ψ(z) depends on N, if ψ(z) uniformly converges to ψ0(z) as N →∞, and
ψ0(z) satisﬁes the assumption of the proposition, and |ψ′′(z)+ψ′(z)2| is bounded by a
constant which is independent of N. In this case, (39) holds for suﬃciently large N, and
hence, (38) holds. Therefore, Proposition 4.2 also holds in this case, where we note that
we can choose ε independently of N.
We generalize Proposition 4.1 to the case of n variables.
Proposition 4.5. For c ∈Cn and an oriented n-ball D′ in Rn, we put
Λ =
{ 1
N k + c ∈Cn 

 k ∈Zn,
1
N k ∈D′}
,
D =
{
z + c ∈Cn 

 z ∈D′ ⊂Rn}
.
Let A be a non-singular symmetric complex n×n matrix such that Re (A−1) is negative
deﬁnite. We assume that ∂D is included in the domain (24). Further, we assume that
(Im c)T m < −π
2 mT · Re (A−1) · m
for any m ∈Zn−{0}. Then,
1
N n
∑
z ∈Λ
eN·zTA z =
∫
D
eN·zTA zdz + O(e−Nε),
for some ε > 0.
Proof. By Proposition 3.4, the required formula is rewritten,
∑
z ∈Λ
eN·zTA z =
πn/2N n/2
√
det(−A)
+ O
(
e−εN)
.
(40)
24
Further, in a similar way as in the proof of Proposition 4.1, putting f(z) = eN·(z/N+c)T A (z/N+c),
we can show that
ˆf(ζ) =
πn/2N n/2
√
det(−A)
eNπ2 ζT A−1ζ + 2π√−1NcT ζ
by using Proposition 3.4. Hence, we obtain
∑
k ∈Zn
eN·(k/N+c)T A (k/N+c) =
πn/2N n/2
√
det(−A)
∑
m ∈Zn
eNπ2 mT A−1m + 2π√−1NcT m
by the Poisson summation formula (30). By the assumption of the proposition, the real
part of
Nπ2 mTA−1m + 2π
√
−1NcTm
is negative for any m ∈Zn−{0}. Therefore, only the summand at m = 0 survives, and
we obtain (40) from it.
We generalize Proposition 4.5 to the case where there are perturbative terms in the
exponential of the summand. Let e1, e2, · · · , en be the standard basis vectors of Cn,
e1 = (1, 0, · · · , 0)T,
e2 = (0, 1, 0, · · · , 0)T,
· · · ,
en = (0, · · · , 0, 1)T.
Proposition 4.6. For c ∈Cn and an oriented n-ball D′ in Rn, we put
Λ =
{ 1
N k + c ∈Cn 

 k ∈Zn,
1
N k ∈D′}
,
D =
{
z + c ∈Cn 

 z ∈D′ ⊂Rn}
.
Let A be a non-singular symmetric complex n×n matrix, and let ψ(z) be a holomorphic
function of the form (25) deﬁned in a neighborhood of 0 ∈Cn including D. We assume
that ∂D is included in the domain
{
z ∈Cn | Re ψ(z) < −ε0
}
for some ε0 > 0. Further,
we assume that there exist δi, δ′
i > 0 (i = 1, · · · , n) such that
∂D is null-homotopic in
{
w + δ√−1 ei ∈Cn 

 w ∈D, δ ∈[0, δi], Re
(
ψ(w + δ√−1 ei) −2πδ
)
< 0
}
,
(41)
and
∂D is null-homotopic in
{
w −δ√−1 ei ∈Cn 

 w ∈D, δ ∈[0, δ′
i], Re
(
ψ(w −δ√−1 ei) −2πδ
)
< 0
}
,
(42)
for i = 1, · · · , n, assuming that ψ is holomorphic in these domains. Then,
1
N n
∑
z ∈Λ
eN ψ(z) =
∫
D
eN ψ(z)dz + O(e−Nε),
for some ε > 0.
We note that ε depends on ψ(z), c, δi, δ′
i and ε0.
25
Proof. The sum of the left-hand side of the required formula is rewritten,
∑
k ∈Zn
k/N ∈D′
exp
(
N · ψ
( 1
N k + c
))
.
(43)
In order to apply the Poisson summation formula (30), we put
f(z) = g
( 1
N z + c
)
exp
(
N · ψ
( 1
N z + c
))
,
where g is a diﬀerentiable function on Rn+ c satisfying that
g(w) =
{
1
if w ∈D,
0
if w /∈N(D),
0 ≤g(w) ≤1
if w ∈N(D) −D.
Here, N(D) is a neighborhood of D in Rn+ c such that N(D) −D is included in the
domain
{
z ∈Cn | Re ψ(z) < −ε0/2
}
. Then, the Fourier transform of f is given by
ˆf(ζ) =
∫
Rn g
( 1
N z + c
)
exp
(
N · ψ
( 1
N z + c
))
e−2π√−1 ζT zdz
= N n
∫
Rn+c
g(w) eN
(
ψ(w)−2π√−1 ζT (w−c)
)
dw,
where we put w = z/N + c. Further, for an integer l > n/2,
|ζ|2l ˆf(ζ) =
(
n
∑
i=1
ζ2
i
)l ˆf(ζ)
= N n( −1
4π2N
)l ∫
Rn+c
g(w) eN ψ(w)((
n
∑
i=1
∂2
∂w2
i
)le−2π√−1 NζT (w−c))
dw
= N n( −1
4π2N
)l ∫
Rn+c
((
n
∑
i=1
∂2
∂w2
i
)lg(w) eN ψ(w))
e−2π√−1 NζT (w−c)dw
= N n( −1
4π2N
)l ∫
Rn+c
h(w) eN ψ(w) e−2π√−1 NζT (w−c)dw,
where h(w) is some polynomial in derivatives of g(w) and ψ(w). Since the above integral is
bounded independently of ζ, ˆf(ζ) satisﬁes the assumption (31) of the Poisson summation
formula. Further, f(z) also satisﬁes (31). Therefore, by the Poisson summation formula
(30),
(43) =
∑
m ∈Zn
ˆf(m).
When m̸ = 0, we have that
ˆf(m) = N n( −1
4π2N
)l ·
1
|m|2l
∫
Rn+c
h(w) eN
(
ψ(w)−2π√−1 mT (w−c)
)
dw
26
= N n( −1
4π2N
)l ·
1
|m|2l
∫
D
Ψ(w) eN
(
ψ(w)−2π√−1 mT (w−c)
)
dw
(44)
+ N n( −1
4π2N
)l ·
1
|m|2l
∫
N(D)−D
h(w) eN
(
ψ(w)−2π√−1 mT (w−c)
)
dw,
(45)
where Ψ(w) is some polynomial in (at most the 2lth) derivatives of ψ(w). Further, since
Re ψ(w) < 0 for w ∈N(D) −D,
∑
m̸=0
(45) = O(e−Nε1)
for some ε1 > 0. Furthermore, when m1 > 0, pushing the contour D into the domain of
(42), we obtain
∑
m ∈Zn
m1>0
(44) = O(e−Nε2)
for some ε2 > 0, similarly as in the proof of Proposition 4.2. Similarly we obtain
∑
m ∈Zn
m1<0
(44) = O(e−Nε3)
for some ε3 > 0, from the assumption (41). Hence,
∑
m̸=0
(44) =
∑
m̸=0
m1=0
(44) + O(e−Nε4)
for some ε4 > 0. By repeating this argument for m2, · · · , mn, we obtain
∑
m̸=0
(44) = O(e−Nε5)
for some ε5 > 0. Therefore,
(43) =
ˆf(0) + O(e−Nε6) = N n
∫
D
eN ψ(w)dw + O(e−Nε6)
for some ε6 > 0, and this implies the required formula.
Remark 4.7. The assumptions (41) and (42) of Proposition 4.6 can be modiﬁed similarly
as in Remark 4.3.
Remark 4.8. Similarly as in Remark 4.4, Proposition 4.6 can naturally be extended to
the case where the holomorphic function ψ(z) depends on N, if ψ(z) uniformly converges
to ψ0(z) as N →∞, and ψ0(z) satisﬁes the assumption of the proposition, and |Ψ(z)| is
bounded by a constant which is independent of N. Similarly as in Remark 4.4, we can
also choose ε independently of N in this case.
27
