---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations"
section_id: sec-004-the-solutions-of-125-on-01
section_title: "The solutions of (1.25) on [0,1+]"
section_number: null
pages: 23-28
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
toc_source: outline
doc_brief: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations — For analytic nonlinear systems of ordinary"
---
Let Y0 be the solution given by Proposition 6, take ǫ small enough and
denote by Oǫ a neighborhood in C of width ǫ of the interval [0, 1 + ǫ].
23
Remark 21 . Y0 ∈L1(Oǫ). As φ →±0, Y0(peiφ) →Y±
0 (p) in the sense
of L1([0, 1 + ǫ]) and also in the sense of pointwise convergence for p̸ = 1,
where
Y±
0 :=

Y0(p)
p < 1
(1 −p ± 0i)β−1a1(p) + a2(p)
p > 1
(β̸ = 1)
Y±
0 :=

Y0(p)
p < 1
ln(1 −p ± 0i)a1(p) + a2(p)
p > 1
(β = 1) (2.40)
Moreover, Y±
0 are L1
loc solutions of the convolution equation (1.25) on the
interval [0, 1 + ǫ].
The proof is immediate from Lemma 20 and Proposition 13.
Proposition 22 For any λ ∈C the combination Yλ = λY+
0 + (1 −λ)Y−
0
is a solution of (1.25) on [0, 1 + ǫ].
Proof.
For p ∈[0, 1) ∪(1, 1 + ǫ] let yλ(p) := Yλ −H(p). Since y∗2
λ = 0
the equation (1.25) is actually linear in yλ (compare with (2.27)).
*
Note: We consider the application Y := y0 7→Yλ and require that it is
compatible with complex conjugation of functions Y(y0∗) = (Y(y0))∗where
F ∗(z) := F(z). We get ℜλ = 1/2. It is natural to choose λ = 1/2 to make
the linear combination a true average. This choice corresponds, on [0, 1 + ǫ],
to the balanced averaging (1.16).
*
Remark 23 For any δ > 0 there is a constant C(δ) such that for large b
∥(Yba
0 )∗l∥u < C(δ)δ|l| ∀l with |l| > 1
(2.41)
(∥∥u is taken on the interval [0, 1 + ǫ]).
Without loss of generality, assume that l1 > 1. Using the notation (2.29),

Z p
0
(Y0)ba
1 (s)(Yba
0 )∗¯l1(p −s)ds

u
≤
24

Z
p
2
0
(Yba
0 )1(s)(Yba
0 )∗¯l1(p −s)ds

u2
+

Z
p
2
0
(Y0)1(p −s)(Yba
0 )∗¯l1(s)ds

u2
(2.42)
(∥∥u2 refers to the interval p ∈[0, 1/2 + ǫ/2].) The ﬁrst u2 norm can be
estimated directly using Corollary 11 whereas we majorize the second one by
∥(Yba
0 )1∥b∥(Yba
0 )∗¯l1(x)∥u2
and apply Corollary 11 to it for |l| > 2 (if |l| = 2 simply observe that (Yba
0 )∗l
is analytic on [0, 1/2 + ǫ/2]).
Lemma 24 The set of all solutions of (1.25) in L1
loc([0, 1 + ǫ]) is parameter-
ized by a complex constant C and is given by
Y0(p) =

Yba
0 (p)
for p ∈[0, 1)
Yba
0 (p) + C(p −1)β−1A(p) for p ∈(1, 1 + ǫ]
(2.43)
for β̸ = 1 or, for β = 1,
Y0(p) =

Yba
0 (p)
for p ∈[0, 1)
Yba
0 (p) + C(p −1)A(p) for p ∈(1, 1 + ǫ]
(2.43)′
where A extend analytically in a neighborhood of p = 1.
Diﬀerent values of C correspond to diﬀerent solutions.
This result remains true if Yba
0 is replaced by any other combination Yλ :=
λY+
0 + (1 −λ)Y−
0 , λ ∈C.
Proof.
We look for solutions of (1.25) in the form
Yba(p) + h(p −1)
(2.44)
By Lemma 20 , h(p −1) = 0 for p < 1. Note that
N (Yba
0 ◦τ−1 + h)(z) = N (Yba
0 )(1 + z) +
n
X
j=1
Z z
0
hj(s)Dj(z −s)ds
(2.45)
25
where the Dj are given in (2.29), and by Remark 2.41 all the inﬁnite sums
involved are uniformly convergent. For z < ǫ (1.25) translates to (compare
with (2.27)):
−(1 + z)h(z) = −ˆΛh(z) −ˆB
Z z
0
h(s)ds +
n
X
j=1
Z z
0
hj(s)Dj(z −s)ds (2.46)
Let
Q(z) :=
Z z
0
h(s)ds
(2.47)
As we are looking for solutions h ∈L1, we have Q ∈AC[0, ǫ] and Q(0) = 0.
Following the same steps as in the proof of Lemma 20 we get the system of
equations:
(z−βQ1(z))′ = z−β−1
n
X
j=1
Z z
0
D′
1j(z −s)Qj(s)ds
(e
ˆC(z)Q⊥)′ = e
ˆC(z)ˆΓc(z)−1
n
X
j=1
Z z
0
D′
⊥(z −s)Qj(s)ds
ˆC(z) := −
Z z
0
ˆΓc(s)−1 ˆBc(s)ds
Q(0) = 0
(2.48)
which by integration gives
(ˆ1 + J)Q(z) = CR(z)
(2.49)
where C ∈C and
(J(Q))1(z) = zβ
Z z
0
t−β−1
n
X
j=1
Z t
0
Qj(s)D′
1j(t −s)dsdt
J(Q)⊥(z) := e−ˆC(z)
Z z
0
e
ˆC(t)ˆΓc(t)−1
 n
X
j=1
Z z
0
D′
⊥(z −s)Qj(s)ds
!
dt
R⊥= 0
26
R1(z) = zβ
(2.50)
First we note the presence of an arbitrary constant C in (2.49) (Unlike
in Lemma 20 when the initial condition, given at z = ǫ was determining the
integration constant, now the initial condition Q(0) = 0 is satisﬁed for all
C).
For small ǫ the norm of the operator J deﬁned on AC[0, ǫ] is O(ǫ), as in
the proof of Lemma 20. Given C the solution of the system (2.48) is unique
and can be written as
Q = CQ0;
Q0 := (ˆ1 + J)−1R̸ = 0
(2.51)
It remains to ﬁnd the analytic structure of Q0. We now introduce the
space
T =

Q : [0, ǫ) 7→Cn : Q = zβA(z)
	
(2.52)
where A(z) extends to an analytic function in Dǫ. With the norm (2.37) (with
B ≡0), T is a Banach space. As in the proof of Lemma 20 the operator J
extends naturally to T where it has a norm O(ǫ) for small ǫ.
It follows
immediately that
Q0 ∈T
(2.53)
The formulas (2.43), (2.43’) follow from (2.44) and (2.47).
Remark 25 If Sβ̸ = 0 (cf. Lemma 20) then the general solution of (1.25)
is given by
Y0(p) = (1 −λ)Y+
0 (p) + λY−
0 (p)
(2.54)
with λ ∈C.
Indeed, if a1̸ ≡0 (cf. Lemma 20) we get at least two distinct solutions of
(2.49) (i.e., two distinct values of C) by taking diﬀerent values of λ in (2.54).
The remark follows from (2.53) (2.52) and Lemma 24..
27
2.5
