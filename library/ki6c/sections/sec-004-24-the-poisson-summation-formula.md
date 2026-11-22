---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-004-24-the-poisson-summation-formula
section_title: "The Poisson summation formula"
section_number: 2.4
pages: 8-11
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
The Poisson summation formula
In this section, we review the Poisson summation formula and a proposition obtained
from it.
Recall (see e.g. [23]) that the Poisson summation formula states that
∑
m ∈Zn
f(m) =
∑
m ∈Zn
ˆf(m)
(13)
for a continuous integrable function f on Rn which satisﬁes that
|f(z)| ≤C
(
1 + |z|
)−n−δ,
| ˆf(z)| ≤C
(
1 + |z|
)−n−δ
(14)
for some C, δ > 0, where ˆf is the Fourier transform of f deﬁned by
ˆf(w) =
∫
Rn f(z) e−2π√−1 wT zdz.
The following proposition is obtained from the Poisson summation formula.
Proposition 2.3 (see [20]). For (c1, c2, c3) ∈C3 and an oriented 3-ball D′ in R3, we put
Λ =
{( i
N + c1, j
N + c2, k
N + c3
)
∈C3 

 i, j, k ∈Z,
( i
N , j
N , k
N
)
∈D′}
,
D =
{
(t + c1, s + c2, u + c3) ∈C3 

 (t, s, u) ∈D′ ⊂R3}
.
Let ψ(t, s, u) be a holomorphic function deﬁned in a neighborhood of 0 ∈C3 including D.
We assume that ∂D is included in the domain
{
(t, s, u) ∈C3 

 Re ψ(t, s, u) < −ε0
}
for some ε0 > 0. Further, we assume that ∂D is null-homotopic in each of the following
domains,
{
(t + δ
√
−1, s, u) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t + δ
√
−1, s, u) < 2πδ
}
,
(15)
{
(t −δ
√
−1, s, u) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t −δ
√
−1, s, u) < 2πδ
}
,
(16)
{
(t, s + δ
√
−1, u) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t, s + δ
√
−1, u) < 2πδ
}
,
(17)
{
(t, s −δ
√
−1, u) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t, s −δ
√
−1, u) < 2πδ
}
,
(18)
{
(t, s, u + δ
√
−1) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t, s, u + δ
√
−1) < 2πδ
}
,
(19)
{
(t, s, u −δ
√
−1) ∈C3 

 (t, s, u) ∈D′, δ ≥0, Re ψ(t, s, u −δ
√
−1) < 2πδ
}
.
(20)
8
Then,
1
N 3
∑
(t,s,u) ∈Λ
eN ψ(t,s,u) =
∫
D
eN ψ(t,s,u)dt ds du + O(e−Nε),
for some ε > 0.
Proof. We brieﬂy review the proof; for details, see [20].
The sum of the left-hand side of the required formula is rewritten,
∑
i,j,k
exp
(
N · ψ
( i
N + c1, j
N + c2, k
N + c3
))
.
(21)
In order to apply the Poisson summation formula, we put
f(t, s, u) = g
( t
N + c1, s
N + c2, u
N + c3
)
exp
(
N · ψ
( t
N + c1, s
N + c2, u
N + c3
))
,
where g is a diﬀerentiable function on Rn+ c satisfying that
g(x, y, z) =
{
1
if (x, y, z) ∈D,
0
if (x, y, z) /∈N(D),
0 ≤g(x, y, z) ≤1
if (x, y, z) ∈N(D) −D.
Here, N(D) is a neighborhood of D in R3+ (c1, c2, c3) such that N(D) −D is included
in the domain
{
(t, s, u) ∈C3 | Re ψ(t, s, u) < −ε0/2
}
. Then, the Fourier transform of f
is given by
ˆf(m1, m2, m3) =
∫
R3 g
( t
N + c1, s
N + c2, u
N + c3
)
× exp
(
N · ψ
( t
N + c1, s
N + c2, u
N + c3
))
e−2π√−1 (m1t+m2s+m3u)dt ds du
= N 3
∫
R3+(c1,c2,c3)
g(x, y, z) eN
(
ψ(x,y,z)−2π√−1 (m1(x−c1)+m2(y−c2)+m3(z−c3)
)
dx dy dz,
where we put x = t/N +c1, y = s/N +c2 and z = u/N +c3. Further,
(ζ2
1 + ζ2
2 + ζ2
3)2 ˆf(ζ1, ζ2, ζ3)
= N 3( −1
4π2N
)2 ∫
R3+(c1,c2,c3)
g(x, y, z) eN ψ(x,y,z)
×
(( ∂2
∂x2 + ∂2
∂y2 + ∂2
∂z2
)2e−2π√−1 N
(
ζ1(x−c1)+ζ2(y−c2)+ζ3(z−c3)
))
dx dy dz
= N 3( −1
4π2N
)2 ∫
R3+(c1,c2,c3)
(( ∂2
∂x2 + ∂2
∂y2 + ∂2
∂z2
)2g(x, y, z) eN ψ(x,y,z))
× e−2π√−1 N
(
ζ1(x−c1)+ζ2(y−c2)+ζ3(z−c3)
)
dx dy dz
= N 3( −1
4π2N
)2 ∫
R3+(c1,c2,c3)
h(x, y, z) eN ψ(x,y,z) e−2π√−1 N
(
ζ1(x−c1)+ζ2(y−c2)+ζ3(z−c3)
)
dx dy dz,
9
where h(x, y, z) is some polynomial in derivatives of g(x, y, z) and ψ(x, y, z).
Here,
we obtain the second equality by repeatedly using the fact that
∫a
b F ′(w)G(w)dw +
∫a
b F(w)G′(w)dw =
∫a
b
(
F(w)G(w)
)′dw = 0 if F(w)G(w) = 0 for w ∈R −(a, b). Since
the above integral is bounded independently of (x, y, z), ˆf(x, y, z) satisﬁes the assumption
(14) of the Poisson summation formula. Further, f(t, s, u) also satisﬁes (14). Therefore,
by the Poisson summation formula (13),
(21) =
∑
m1,m2,m3 ∈Z
ˆf(m1, m2, m3).
When (m1, m2, m3)̸ = (0, 0, 0), we have that
ˆf(m1, m2, m3) = N 2( −1
4π2N
)2 ·
1
(m2
1 + m2
2 + m2
3)2
×
∫
R3+(c1,c2,c3)
h(x, y, z) eN
(
ψ(x,y,z)−2π√−1 (m1(x−c1)+m2(y−c2)+m3(z−c3))
)
dx dy dz
= N 2( −1
4π2N
)2 ·
1
(m2
1 + m2
2 + m2
3)2
×
∫
D
Ψ(x, y, z) eN
(
ψ(x,y,z)−2π√−1 (m1(x−c1)+m2(y−c2)+m3(z−c3))
)
dx dy dz
(22)
+ N 2( −1
4π2N
)2 ·
1
(m2
1 + m2
2 + m2
3)2
×
∫
N(D)−D
h(x, y, z) eN
(
ψ(x,y,z)−2π√−1 (m1(x−c1)+m2(y−c2)+m3(z−c3))
)
dx dy dz,
(23)
where Ψ(x, y, z) is some polynomial in (at most the 4th) derivatives of ψ(x, y, z). Further,
since Re ψ(x, y, z) < ε0/2 for (x, y, z) ∈N(D) −D,
∑
(m1,m2,m3)̸=(0,0,0)
(23) = O(e−Nε1)
for some ε1 > 0. Furthermore, when m1 > 0, pushing the contour D into the domain
(16), we obtain
∑
m1,m2,m3 ∈Z
m1>0
(22) = O(e−Nε2)
for some ε2 > 0. Similarly we obtain
∑
m1,m2,m3 ∈Z
m1<0
(22) = O(e−Nε3)
for some ε3 > 0, by pushing D into the domain (15). Hence,
∑
(m1,m2,m3)̸=(0,0,0)
(22) =
∑
(m1,m2,m3)̸=(0,0,0)
m1=0
(22) + O(e−Nε4)
10
for some ε4 > 0. By repeating this argument for m2 and m3, we obtain
∑
(m1,m2,m3)̸=(0,0,0)
(22) = O(e−Nε5)
for some ε5 > 0. Therefore,
(21) =
ˆf(0, 0, 0) + O(e−Nε6) = N 3
∫
D
eN ψ(x,y,z)dx dy dz + O(e−Nε6)
for some ε6 > 0, and this implies the required formula.
Remark 2.4. By modifying the proof of Proposition 2.3, we can show that, instead of
the domains (15)–(20), we can use the domains (17)–(20) and
{
(t + δ√−1, s −δ√−1, u) ∈C3 

(t, s, u) ∈∆′, δ ≥0, Re ψ(t + δ√−1, s −δ√−1, u) < 2πδ
}
,
(24)
{
(t −δ√−1, s + δ√−1, u) ∈C3 

(t, s, u) ∈∆′, δ ≥0, Re ψ(t −δ√−1, s + δ√−1, u) < 2πδ
}
.
(25)
In this case, we can prove the proposition by considering the cases where m1̸ = m2, m2̸ = 0
or m3̸ = 0, instead of the cases where m1̸ = 0, m2̸ = 0 or m3̸ = 0.
Remark 2.5. Similarly as in [20, Remark 4.8], Proposition 2.3 can naturally be extended
to the case where the holomorphic function ψ(t, s, u) depends on N, if ψ(t, s, u) uniformly
converges to ψ0(t, s, u) as N →∞, and ψ0(t, s, u) satisﬁes the assumption of the proposi-
tion, and |Ψ(t, s, u)| is bounded by a constant which is independent of N. We note that
we can choose ε of the proposition independently of N in this case.
