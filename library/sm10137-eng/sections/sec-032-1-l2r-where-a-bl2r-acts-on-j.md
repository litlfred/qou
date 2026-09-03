---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-032-1-l2r-where-a-bl2r-acts-on-j
section_title: "(L2[R, ∞)), where A ∈B(L2[R, ∞) acts on J ∗"
section_number: 1
pages: 12-16
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
1 (L2[R, ∞))
by the rule X 7→Tr(AX). For the norm of K, considering it as a functional on
B(L2[R, ∞)) and using the definition of a trace and the expression (7.2), we have
∥K∥J1 =
sup
B∈B(L2),∥B∥=1
|Tr(BK)|
=
sup
B∈B(L2),∥B∥=1

X
i∈N
Z ∞
0
a(t)⟨fi, Bht
1⟩L2⟨(ht
2)∗, fi⟩L2 dt

,
where {fi}i∈N is an arbitrary orthonormal basis in L2[R, ∞).
Next we use the
Cauchy–Bunyakovsky–Schwarz inequality to obtain
X
i∈N
|⟨fi, Bht
1⟩L2⟨(ht
2)∗, fi⟩L2|
⩽
X
i∈N
|⟨fi, Bht
1⟩L2|2
1/2X
i∈N
|⟨(ht
2)∗, fi⟩L2|2
1/2
⩽∥ht
1∥L2 ∥ht
2∥L2,
which finishes the proof.
Rate of convergence in the central limit theorem
1619
Proposition 5. Let the kernel K(x, y) of an integral operator K be absolutely con-
tinuous with respect to y on [a, b]. Assume that K = Kχ[a,b]. Consider the operator
∂yK with kernel ∂K(x, y)/∂y and assume that ∂yK ∈J2. Then
∥K∥J1 ⩽∥K∥+ (b −a)
√
2
∥∂yK∥J2.
(7.3)
Proof. Let Pf(x) = (1/(b −a))χ[a,b](x)⟨χ[a,b], f⟩L2 be a one-dimensional projector
onto χ[a,b], and let Q = χ[a,b] −P. We decompose the operator: K = KP + KQ.
The operator KP is also a one-dimensional projector with trace norm of at most
∥KP∥J1 ⩽∥K∥∥P∥J1 = ∥K∥.
Recall that the Volterra operator V on L2([a, b]) is defined by the formula
V f(x) =
Z x
a
f(t) dt.
It is a Hilbert–Schmidt operator with kernel V (x, y) =
χ[a,x](y), and its Hilbert–Schmidt norm is
∥V ∥2
J2 =
Z b
a
dx
Z x
a
dy = (b −a)2
2
.
Integrating KQ by parts we obtain
Z b
a
K(x, y)Qf(y) dy =
Z b
a
K(x, y) d(V Qf(y)) = K(x, y)V Qf(y)

b
a −∂yKV Qf,
where
V Qf(a) = 0
and
V Qf(b) = ⟨χ[a,b], Qf⟩L2 = 0
by the definition of V and Q.
The inequality ∥∂yKV Q∥J1 ⩽∥∂yK∥J2 ∥V ∥J2
finishes the proof.
Corollary 1. There exists a constant C such that for any kernel K of an integral
operator on L2(R+) with the estimates
|K(x, y)| ⩽
A
(x + y)2
and
|∂yK(x, y)| ⩽
A
(x + y)2 ,
x, y > 0,
for some constant A, for any R > 0 we have
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽AC
 1
R +
1
√
R

.
(7.4)
Proof. By Proposition 5 we have
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽
∞
X
l=0
∥χ[R,∞)Kχ[R+l,R+l+1]∥J1
⩽
∞
X
l=0
(∥χ[R,∞)Kχ[R+l,R+l+1]∥J2 + ∥χ[R,∞)∂yKχ[R+l,R+l+1]∥J2),
1620
S. M. Gorbunov
where for each term we have by assumption
∥χ[R,∞)Kχ[R+l,R+l+1])∥2
J2 + ∥χ[R,∞)∂yKχ[R+l,R+l+1])∥2
J2
⩽2A2
Z ∞
R
dx
Z R+l+1
R+l
dy
1
(x + y)4 = 3A2
4R + 2l + 1
(2R + l)2(2R + l + 1)2
⩽
6A2
(2R + l)2(2R + l + 1).
Therefore, the trace norm satisfies
∥χ[R,∞)Kχ[R,∞)∥J1 ⩽
√
3 A
R
+ 2
√
3 A
∞
X
l=1
1
(2R + l)3/2 .
Finally, we have
∞
X
l=1
1
(2R + l)3/2 ⩽
Z
R+
1
(2R + x)3/2 dx =
1
√
2R
,
which finishes the proof.
Recall several properties of Bessel functions. Set J(x) = √x Jν(x) and D(x) =
Jν(x) −
p
2/π cos(x −ϕν), where ϕν = π/4 + (π/2)ν.
We have the following
asymptotics for the Bessel function and its derivative as x approaches infinity:
D(x) = −
r
2
π sin(x −ϕν)ν2 −1/4
x
+ O(x−2)
(7.5)
and
D′(x) = Aν
cos(x −ϕν)
x
+ O(x−2),
(7.6)
where Aν is some constant. These imply uniform estimates on R+ for ν > −1 and
some constant Cν:
|D(x)| ⩽
Cν
√x(1 + √x)
(7.7)
and

D′(x) −Aν
cos(x −ϕν)
x

 ⩽
Cν
x3/2(1 + √x).
(7.8)
Recall the following improper integral.
Proposition 6 ([3], Lemma 2.6). We have
Z ∞
0

J(xt)J(yt) −2
π cos(xt −ϕν) cos(yt −ϕν)

dt = −sin(2ϕν)
π(x + y).
(7.9)
Lastly, we establish some properties of the function spaces we have introduced.
Rate of convergence in the central limit theorem
1621
Lemma 5. There exists a constant C such that for any a ∈L1(R+) ∩L∞(R+)
satisfying ∥a∥˙B < ∞we have
(1) ∥a′′∥L1 ⩽C(∥a∥˙H1 + ∥a∥˙H2 + ∥ta(t)∥˙H2);
(2) ∥ta′′′(t)∥L1 ⩽C(∥a∥˙H3 + ∥a∥˙H1 + ∥ta(t)∥˙H2 + ∥t2a(t)∥˙H3);
(3) limt→+∞a(t) = 0, limt→+∞a′(t) = 0 and limt→+∞ta′′(t) = 0;
(4) |a′(0)| ⩽∥a∥˙H1 + ∥a∥˙H2 .
In particular, the above estimates are bounded by C∥a∥˙B.
Proof. (1) Using the Cauchy–Bunyakovsky–Schwarz inequality, for the L1-norm
we write
∥a′′∥L1 =
Z 1
0
|a′′(t)| dt +
Z ∞
1
|a′′(t)| dt ⩽∥a∥˙H2 + ∥ta′′(t)∥L2.
Since ta′′(t) = (at)′′ −2a′, the second term is estimated by 2∥a∥˙H1 + ∥ta(t)∥˙H2.
(2) The proof is quite similar to the previous one.
(3) The statement on a follows from ba ∈L1(R) and the Riemann–Lebesgue
lemma.
Since a′ ∈H1(R+) we see that ba′ is absolutely integrable and the statement on a′
follows again from the Riemann–Lebesgue lemma.
By the first and second assertions (ta′′(t))′ = a′′(t) + ta′′′(t) is absolutely inte-
grable, so ta′′(t) tends to a finite limit as t approaches infinity. Since (ta(t))′′ and
a′(t) are square integrable, so is ta′′(t), which yields that the limit is zero.
(4) The expression of a′(0) in terms of the cosine transform yields
|b′(0)| ⩽1
π
Z ∞
0
λ|bb(λ)| dλ,
and by the Cauchy–Bunyakovsky–Schwarz inequality and Parseval’s theorem we
have
Z 1
0
λ|bb(λ)| dλ ⩽∥b∥˙H1
and
Z ∞
1
λ2
λ |bb(λ)| dλ ⩽∥b∥˙H2.
Lemma 5 is proved.
We devote the rest of this section to the proof of Lemma 3.
Proof of Lemma 3. Since B1 −W1 = 0, it is sufficient to prove the statement for
b ∈L1(R+) ∩L∞(R+) satisfying ∥b∥˙B < ∞.
Recall the formula for the kernel of the difference Rb(x, y) = Bb(x, y)−Wb(x, y):
Rb(x, y) =
Z ∞
0

J(xt)J(yt) −1
π cos((x −y)t)

b(t) dt.
Let us outline the plan of the proof. One can observe from the asymptotics (7.5)
and (7.6) that the above integral contains an asymptotically small function for
large x and y. Thus, we substitute J(x) = √x Jν(x) = D(x) +
p
2/π cos(x −ϕν)
into the expression for Rb(x, y).
This substitution and several integrations by
parts represent the kernel as a sum of other kernels, to which Corollary 1 and
Proposition 4 can be applied.
1622
S. M. Gorbunov
To be precise, we perform a sequence of decompositions of our kernel, for which
we use the following notation:
Rb(x, y) = R1(x, y) −R2(x, y),
(7.10)
R2(x, y) = S(x, y) + T(x, y) + T(y, x)
(7.11)
and
T(x, y) = T0(x, y) + T1(x, y) + Z(x, y).
(7.12)
Explicit formulae are presented below (see (7.13)–(7.15)). We prove an estimate for
the trace norm for each of the above kernels separately. In particular, the estimate
of the trace norm for χ[R,∞)R1χ[R,∞) follows from Corollary 1. Estimates for the
trace norms of the operators with the kernels
χ[R,∞)2(x, y)S(x, y),
χ[R,∞)2(x, y)T0(x, y),
χ[R,∞)2(x, y)T1(x, y),
χ[R,∞)2(x, y)(Z(x, y) + Z(y, x))
follow from Proposition 4.
The sequence of decompositions. 1. The decomposition (7.10). First we sub-
stitute the following formula into the kernel Rb(x, y):
1
π cos((x −y)t) = 2
π cos(xt −ϕν) cos(yt −ϕν) −1
π cos((x + y)t −2ϕν).
By part (3) of Lemma 5 the following integral can twice be integrated by parts and
thus expressed as follows:
1
π
Z ∞
0
cos((x + y)t −2ϕν)b(t) dt
= sin(2ϕν)b(0)
π(x + y)
−b′(0) cos(2ϕν)
π(x + y)2
−
1
π(x + y)2
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt.
Next we substitute the expression (7.9) for sin(2ϕν)/(π(x + y)) into the above
identity. These calculations prove the decomposition (7.10) for the following kernels
R1 and R2:
R1(x, y) =
1
π(x + y)2

cos(2ϕν)b′(0) +
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt

,
R2(x, y) =
Z ∞
0

J(xt)J(yt) −2
π cos(xt −ϕν) cos(yt −ϕν)

b0(t) dt,
(7.13)
where b0(x) = b(x) −b(0).
