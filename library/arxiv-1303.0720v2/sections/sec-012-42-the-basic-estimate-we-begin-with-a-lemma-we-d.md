---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-012-42-the-basic-estimate-we-begin-with-a-lemma-we-d
section_title: "The basic estimate. We begin with a lemma. We decompose the given bianalytic function"
section_number: 4.2
pages: 7-9
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
as u(z) = u1(z) + c¯z + |z|2u2(z), where c is a constant and uj is holomorphic for j = 1, 2. Let
ds(z) := |dz| denote arc length measure.
Lemma 4.1. If u(z) = u1(z) + c¯z + |z|2u2(z) is bianalytic and ψ is subharmonic in D, then
Z 1
0

u1(0) + r2u2(0) + cr
π
Z
T
¯ζψ(rζ)ds(ζ)

2
rdr ≤e−2ψ(0)
2π
Z
D
|u|2e2ψdA.
Proof. We write ψr(ζ) := ψ(rζ) for the dilation of ψ, and let gr be the holomorphic and zero-free
function given by
log gr(z) := 1
2π
Z
T
1 + z ¯ζ
1 −z ¯ζψr(ζ)ds(ζ).
8
ANTTI HAIMI AND HAAKAN HEDENMALM
This of course deﬁnes gr uniquely, and also picks a suitable branch of log gr. Taking real parts,
we see that
log |gr| = Re log gr = P[ψr](z) := 1
2π
Z
T
1 −|z|2
|1 −z ¯ζ|2 ψr(ζ)ds(ζ),
z ∈D,
where P[ψr] denotes the Poisson extension of ψr. Then, in the standard sense of boundary
values, |gr|2 = e2ψr on T. By the mean value property, we have that
(4.2.1)
1
2π
Z
T
u(rζ)gr(ζ)ds(ζ) = 1
2π
Z
T
{u1(rζ) + cr ¯ζ + r2u2(rζ)} gr(ζ)ds(ζ)
= u1(0)gr(0) + crg′
r(0) + r2u2(0)gr(0) = gr(0)

u1(0) + r2u2(0) + cr g′
r(0)
gr(0)

.
Here,
g′
r(z)
gr(z) = d
dz log gr(z) = 1
π
Z
T
¯ζ
(1 −z ¯ζ)2 ψr(ζ) ds(ζ),
so that in particular
(4.2.2)
g′
r(0)
gr(0) = 1
π
Z
T
¯ζψr(ζ)ds(ζ).
By (4.2.1) combined with the Cauchy-Schwarz inequality,
|gr(0)|2

u1(0) + r2u2(0) + cr g′
r(0)
gr(0)

2
≤1
2π
Z
T
|u(rζ)gr(ζ)|2ds(ζ) = 1
2π
Z
T
|u(rζ)|2e2ψr(ζ)ds(ζ).
Next, we multiply both sides by 2r and integrate with respect to r:
(4.2.3)
Z 1
0
|gr(0)|2

u1(0) + r2u2(0) + cr g′
r(0)
gr(0)

2
2rdr ≤1
π
Z
D
|u(z)|2e2ψ(z)dA(z).
The sub-mean value property applied to ψ gives that e2ψ(0) ≤|gr(0)|2, so we obtain from (4.2.3)
that
(4.2.4)
e2ψ(0)
Z 1
0

u1(0) + r2u2(0) + cr g′
r(0)
gr(0)

2
rdr ≤1
2π
Z
D
|u(z)|2e2ψ(z)dA(z),
as claimed.
□
4.3. Applications of the basic estimate. We can now estimate rather trivially the ¯∂-derivative
at the origin.
Proposition 4.2. If u(z) is bianalytic and ψ is subharmonic in D, then
| ¯∂u(0)|2 ≤3
πe−2ψ(0)
Z
D
|u|2e2ψdA.
Proof. We apply Lemma 4.1 to the function v(z) := zu(z) = zu1(z) + |z|2(c + zu2(z)):
|c|2
6 =
Z 1
0
|r2c|2rdr ≤e−2ψ(0)
2π
Z
D
|v|2e2ψdA ≤e−2ψ(0)
2π
Z
D
|u|2e2ψdA.
It remains to observe that c = ¯∂u(0).
□
We can also estimate the value at the origin, under an additional assumption.
