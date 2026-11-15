---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations"
section_id: sec-003-behavior-of-y0p-near-p1
section_title: "Behavior of Y0(p) near p=1."
section_number: null
pages: 18-23
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
toc_source: outline
doc_brief: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations — For analytic nonlinear systems of ordinary"
---
Let Y0 be the unique solution in Lray(D) of (1.25) and let ǫ > 0 be small.
Deﬁne
18
H(p) :=
 Y0(p) for p ∈D ,|p| < 1 −ǫ
0
otherwise
and h(1 −p) := Y0(p) −H(p)
(2.20)
In terms of h, for real z = 1 −p, z < ǫ, the equation (1.25) reads:
−(1 −z)h(z) = F1(z) −ˆΛh(z) + ˆB
Z z
ǫ
h(s)ds + N (H + h)
(2.21)
where
F1(1 −s) := F0(s) −ˆB
Z 1−ǫ
0
H(s)ds
Proposition 18 i) For small ǫ, H∗l(1 + z) extends to an analytic function
in the disk Dǫ := {z : |z| < ǫ}. Furthermore, for any δ there is an ǫ and
a constant K1 := K1(δ, ǫ) such that for z ∈Dǫ the analytic continuation
satisﬁes the estimate
|H∗l(1 + z)|∧< K1δl
(2.22)
Proof.
The case |l| = 1 is trivial: H itself extends as the zero analytic function.
We assume by induction on |l| that Proposition 18 is true for all l, |l| ≤l
and show that it then holds for (e.g.) H1 ∗H∗l, for all l, |l| ≤l.
H is analytic in an ǫ–neighborhood of [0, 1 −2ǫ], and therefore so is H∗l.
Taking ﬁrst z ∈R+, z < ǫ, we have
Z 1−z
0
H1(s)H∗l(1 −z −s)ds =
Z 1−ǫ
0
H1(s)H∗l(1 −z −s)ds =
Z 1/2
0
H1(s)H∗l(1 −z −s)ds +
Z 1−ǫ
1/2
H1(s)H∗l(1 −z −s)ds
(2.23)
The integral on [1/2, 1 −ǫ] is analytic for small z, since the argument of H∗l
varies in an ǫ-neighborhood of [0, 1/2]; the integral on [0, 1/2) equals
Z 1−z
1/2−z
H1(1−z−t)H∗l(t)dt =
 Z 1/2
1/2−z
+
Z 1−ǫ
1/2
+
Z 1−z
1−ǫ
!
H1(1−z−t)H∗l(t)dt
(2.24)
19
In (2.24) the integral on [1/2 −z, 1/2] is clearly analytic in Dǫ, the following
one is the integral of an analytic function of the parameter z with respect to
the absolutely continuous measure H∗ldt whereas in the last integral, both
H∗l (by induction) and H1 extend analytically in Dǫ.
To prove now the the induction step for the estimate (2.22), ﬁx δ small
and let:
η < δ; M1 :=
max
|p|<1/2+ǫ |H(p)|∧; M2(ǫ) :=
max
0≤x≤1−ǫ |H(p)|∧;
ǫ <
δ
4M1
(2.25)
Let K2 := K2(η; ǫ) be large enough so that (2.19) holds with η in place of δ
for real x ∈[0, 1−ǫ] and also in an ǫ neighborhood in C of the interval [0, 1/2+
2ǫ]. We use (2.19) to estimate the second integral in the decomposition (2.23)
and the ﬁrst two integrals on the r.h.s. of (2.24). For the last integral in (2.24)
we use the induction hypothesis. If K1 > 2K2 (2M1 + M2), it follows that
|H∗l ∗H1|∧is bounded by (the terms are in the order explained above):
M2(ǫ)K2ηl + M1K2ηl + M1K2ηl + (2ǫ)M1K1δl < K1δl+1
(2.26)
Proposition 19 The equation (2.21) can be written as
−(1−z)h(z) = F(z)−ˆΛh(z)+ ˆB
Z z
ǫ
h(s)ds−
n
X
j=1
Z z
ǫ
hj(s)Dj(s−z)ds (2.27)
where
F(z) := N (H)(1 −z) + F1(z)
(2.28)
Dj =
X
|l|≥1
ljGl ∗H∗¯lj +
X
|l|≥2
ljg0,lH∗¯lj; ¯lj := (l1, l2, ..(lj −1), ..ln)
(2.29)
(cf. also (1.24)) extend to analytic functions in Dǫ (cf. Proposition 18).
Moreover, if H is a vector in L1
b(R+) then, for large b, Dj ∈L1
b(R+) and the
functions F(z) and Dj extend to analytic functions in Dǫ.
20
Proof.
Noting that (Y0 −H)∗2(1 −z) = 0 for ǫ < 1/2 and z ∈Dǫ the result is
easily obtained by re-expanding N (H + h) since Proposition 18 guarantees
the uniform convergence of the series thus obtained. The proof that Dj ∈L1
b
for large b is very similar to the proof of (2.18). The analyticity properties
follow easily from Proposition 18, since the series involved in N (H) and Dj
converge uniformly for |z| < ǫ.
Consider again the equation (2.27). Let ˆΓ = ˆΛ −(1 −z)ˆ1, where ˆ1 is the
identity matrix. By construction ˆΓ and ˆB are block-diagonal, their ﬁrst block
is one-dimensional: ˆΓ11 = z and ˆB11 = β. We write this as ˆΓ = z ⊕ˆΓc(z)
and similarly, ˆB = β ⊕ˆBc, where ˆΓc and ˆBc are (n −1) × (n −1) matrices.
ˆΓc(z) and ˆΓ−1
c (z) are analytic in Dǫ.
Lemma 20 The function Y0 given in Proposition 6 can be written in the
form
Y0(p) = (1 −p)β−1a1(p) + a2(p) (β̸ = 1)
Y0(p) =
ln(1 −p)a1(p) + a2(p) (β = 1)
(2.30)
for p in the region (Dǫ + 1) ∩D (Dǫ + 1 := {1 + z : z ∈Dǫ}) where a1, a2
are analytic functions in Dǫ + 1 and (a1)j = 0 for j > 1.
Proof.
Let Q(z) :=
R z
ǫ h(s)ds. By Proposition 6, Q is analytic in Dǫ ∩(1 −D).
From (2.27) we obtain
(z ⊕ˆΓc(z))Q′(z) −(β ⊕ˆBc)Q(z) = F(z) −
n
X
j=1
Z z
ǫ
Dj(s −z)Q′
j(s)ds (2.31)
or, after integration by parts in the r.h.s. of (2.31), (Dj(0) = 0, cf. (2.29)),
(z ⊕ˆΓc(z))Q′(z) −(β ⊕ˆBc)Q(z) = F(z) +
n
X
j=1
Z z
ǫ
D′
j(s −z)Qj(s)ds (2.32)
With the notation (Q1, Q⊥) := (Q1, Q2, .., Qn) we write the system in the
form
21
(z−βQ1(z))′ = z−β−1
 
F1(z) +
n
X
j=1
Z z
ǫ
D′
1j(s −z)Qj(s)ds
!
(e
ˆC(z)Q⊥)′ = e
ˆC(z)ˆΓc(z)−1
 
F⊥+
n
X
j=1
Z z
ǫ
D′
⊥(s −z)Qj(s)ds
!
ˆC(z) := −
Z z
0
ˆΓc(s)−1 ˆBc(s)ds
Q(ǫ) = 0
(2.33)
After integration we get:
Q1(z) = R1(z) + J1(Q)
Q⊥(z) = R⊥(z) + J⊥(Q)
(2.34)
with
J1(Q) = zβ
Z z
ǫ
t−β−1
n
X
j=1
Z t
ǫ
Qj(s)D′
1j(t −s)dsdt
J⊥(Q)(z) := e−ˆC(z)
Z z
ǫ
e
ˆC(t)ˆΓc(t)−1
 n
X
j=1
Z z
ǫ
D′
⊥(s −z)Qj(s)ds
!
dt
R⊥(z) := e−ˆC(z)
Z z
ǫ
e
ˆC(t)ˆΓc(t)−1F⊥(t)dt
R1(z) = zβ
Z z
ǫ
t−β−1F1(t)dt
(β̸ = 1)
R1(z) = F1(0) + F ′
1(0)z ln z + z
Z z
ǫ
F1(s) −F1(0) −sF ′
1(0)
s
ds (β = 1)
(2.35)
Consider the following space of functions:
Tβ
=
n
Q analytic in Dǫ ∩(D −1) : Q = zβA(z) + B(z)
o
for β̸ = 1 and
T1
=
n
Q analytic in Dǫ ∩(D −1) : Q = z ln zA(z) + B(z)
o
(2.36)
where A, B are analytic in Dǫ. (The decomposition of Q in (2.36) is unam-
biguous since zβ and z ln z are not meromorphic in Dǫ.)
22
The norm
∥Q∥= sup {|A(z)|∧, |B(z)|∧: z ∈Dǫ}
(2.37)
makes Tβ a Banach space.
For A(z) analytic in Dǫ the following elementary identities are useful in what
follows:
Z z
ǫ
A(s)srds = Const + zr+1
Z 1
0
A(zt)trdt = Const + zr+1Analytic(z)
Z z
0
sr ln s A(s)ds = zr+1 ln z
Z 1
0
A(zt)trdt + zr+1
Z 1
0
A(zt)tr ln tdt
(2.38)
where the second equality is obtained by diﬀerentiating with respect to r the
ﬁrst equality.
Using (2.38) it is straightforward to check that the r.h.s. of (2.34) extends
to a linear inhomogeneous operator on Tβ with image in Tβ and that the norm
of J is O(ǫ) for small ǫ. For instance, one of the terms in J for β = 1,
z
Z z
0
t−2
Z t
0
s ln s A(s)D′(t −s)ds =
z2 ln z
Z 1
0
Z 1
0
σA(zτσ)D′(zτ −zτσ)dσdτ+
z2
Z 1
0
dτ
Z 1
0
dσσ(ln τ + ln σ)A(zτσ)D′(zτ −zτσ)
(2.39)
manifestly in Tβ if A is analytic in Dǫ. Comparing with (2.36), the extra
power of z accounts for a norm O(ǫ) for this term.
Therefore, in (2.33) (1−J) is invertible and the solution Q ∈Tβ ⊂L (D).
In view of the the uniqueness of Y0 (cf. Proposition 6), the rest of the proof
of Lemma 20 is immediate.
2.4
