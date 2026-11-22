---
doc_id: sm10137-eng
doc_title: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel"
section_id: sec-006-7-proof-of-lemma-3
section_title: "§7 Proof of Lemma 3"
section_number: null
pages: 12-20
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
toc_source: outline
doc_brief: "Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel — We consider a family of linear operators diagonalized by the Hankel transform."
---
In this section we establish Lemma 3. Our calculations follow Basor and Ehrhardt
(see [3], Lemmas 2.6–2.8). The section is structured as follows. In Propositions 4
and 5 and Corollary 1 we establish estimates for the trace norms of integral opera-
tors with kernels of certain form. Then we recall the necessary properties of Bessel
functions and their derivatives. We end the preparations to the proof by Lemma 5,
establishing some properties of the function spaces in question. The rest of the
section is devoted to the proof of Lemma 3 itself.
Proposition 4. Let K be an integral operator on L2[R, ∞) with kernel
K(x, y) =
Z
R+
a(t)h1(x, t)h2(y, t) dt,
where h1, h2 and a are some measurable functions. Then the estimate
∥K∥J1 ⩽
Z ∞
0
|a(t)|
Z ∞
R
|h1(x, t)|2 dx
1/2Z ∞
R
|h2(y, t)|2 dy
1/2
dt
(7.1)
holds, provided that the right-hand side is finite.
Proof. Let f, g ∈L2[R, ∞). Set ht
i(x) = hi(x, t), i = 1, 2. Then
⟨f, Kg⟩L2 =
Z ∞
R
Z ∞
R
Z ∞
0
a(t)h1(x, t)h2(y, t) dt

g(y) dyf ∗(x) dx
=
Z ∞
0
a(t)
Z ∞
R
h1(x, t)f ∗(x) dx
Z ∞
R
h2(y, t)g(y) dy

dt
=
Z ∞
0
a(t)⟨f, ht
1⟩L2⟨(ht
2)∗, g⟩L2 dt,
(7.2)
where Fubini’s theorem can be applied since the function under the integral is abso-
lutely integrable by the assumption that the right-hand side of (7.1) is finite. Recall
that B(L2[R, ∞)) ≃J ∗
1 (L2[R, ∞)), where A ∈B(L2[R, ∞) acts on J ∗
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
2. The decomposition (7.11). It can be verified directly that (7.11) holds if we
take S and T to be
S(x, y) =
Z ∞
0
D(xt)D(yt)b0(t) dt,
T(x, y) =
Z ∞
0
D(xt)
r
2
π cos(yt −ϕν)b0(t) dt.
(7.14)
3. The decomposition (7.12). We integrate the expression for T(x, y) by parts:
Z ∞
0
D(xt)
r
2
π
1
y b0(t) d(sin(yt −ϕν)) = D(xt)
r
2
π
1
y b0(t) sin(yt −ϕν)

∞
0
−
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt
−
Z ∞
0
xD′(xt)
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
where the first term is zero by Lemma 5 and (7.7). Next we take the following
kernels for the decomposition (7.12):
T0(x, y) = −
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt,
T1(x, y) = −
Z ∞
0
x

D′(xt) −Aν
cos(xt −ϕν)
xt
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
Z(x, y) = −
Z ∞
0
xAν
cos(xt −ϕν)
xt
b0(t)
r
2
π
1
y sin(yt −ϕν) dt.
(7.15)
Trace norm estimates. Before diving into calculations we present several inequal-
ities we need.
Firstly, the Cauchy–Bunyakovsky–Schwarz inequality implies the following:
|b0(t)| =

Z t
0
b′(x) dx

 ⩽
√
t ∥b∥˙H1.
(7.16)
The same argument for the derivative gives
|b′(t)| ⩽
√
t (|b′(0)| + ∥b∥˙H2).
(7.17)
Further, using (7.17) we have
|b0(t)| =

Z t
0
b′(x) dx

 ⩽(|b′(0)| + ∥b∥˙H2)t3/2.
(7.18)
Lastly, observe the identity
d
dt
b0(t)
t

= 1
t2
Z t
0
b′(x) dx −b0(t) +
Z t
0
xb′′(x) dx

= 1
t2
Z t
0
xb′′(x) dx.
The Cauchy–Bunyakovsky–Schwarz inequality implies that

Z t
0
xb′′(x) du

 ⩽t3/2∥b∥˙H2.
Substituting this in yields

d
dt
b0(t)
t


 ⩽∥b∥˙H2
√
t .
(7.19)
1. An estimate for R1. We have
|R1(x, y)| ⩽
1
(x + y)2 (|b′(0)| + ∥b′′∥L1).
By Lemma 5 b′′ is absolutely integrable, so we have the following expression for
the derivative:
∂yR1(x, y) = −
2
π(x + y)3

cos(2ϕν)b′(0) +
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt

−
1
π(x + y)2
Z ∞
0
sin((x + y)t −2ϕν)tb′′(t) dt.
Next we integrate the second term by parts:
1
(x + y)
Z ∞
0
d(cos((x + y)t −2ϕν))tb′′(t) dt = cos((x + y)t −2ϕν)tb′′(t)

∞
0
−
1
(x + y)
Z ∞
0
cos((x + y)t −2ϕν)(tb′′′(t) + b′′(t)) dt,
where the limit at infinity is zero by Lemma 5.
These calculations imply the
following estimate for x, y ⩾1:
|∂yR1(x, y)| ⩽
2
(x + y)2 (|b′(0)| + ∥b′′∥L1 + ∥tb′′′(t)∥L1).
Finally, applying Corollary 1 and Lemma 5 we obtain the required estimate for
some constant C and R ⩾1:
∥χ[R,∞)R1χ[R,∞)∥J1 ⩽C∥b∥˙B
√
R
.
2. An estimate for S. Using (7.7) we obtain
Z ∞
R
|D(xt)|2 dx ⩽C2
ν
Z ∞
R
1
xt(1 +
√
xt)2 dx = 2C2
ν
t

ln

1 +
1
√
tR

−
1
1 +
√
tR

.
Set G(x) = ln(1 + 1/√x) −1/(1 + √x). Using Proposition 4 we have
∥χ[R,∞)Sχ[R,∞)∥J1 ⩽2C2
ν
Z ∞
0
|b0(t)|
t
G(tR) dt.
Next we substitute (7.16) in to obtain
∥χ[R,∞)Sχ[R,∞)∥J1 ⩽2C2
ν∥b∥˙H1
Z ∞
0
G(tR)
√
t
dt = 4C2
ν
√
R
∥b∥˙H1 ⩽4C2
ν
√
R
∥b∥˙B.
3. An estimate for T0. Again, Proposition 4 in combination with (7.7) gives
∥χ[R,∞)T0χ[R,∞)∥J1 ⩽Cν
√
R
Z ∞
0
|b′(t)|
√
t
p
G(tR) dt.
For the integral over [0, 1] using inequality (7.17), for some constant C we can write
Z 1
0
|b′(t)|
√
t G1/2(tR) dt ⩽(|b′(0)| + ∥b∥˙H2)
Z 1
0
p
G(tR) dt ⩽C(|b′(0)| + ∥b∥˙H2).
And for the integral over [1, ∞) we use the Cauchy–Bunyakovsky–Schwarz inequa-
lity:
Z ∞
1
|b′(t)|
√
t
p
G(tR) dt ⩽∥b∥˙H1
sZ ∞
1
G(xR)
x
dx ⩽
√
2 ∥b∥˙H1.
These calculations yield the following estimate by Lemma 5:
∥χ[R,∞)T0χ[R,∞)∥J1 ⩽2CCν
√
R
(|b′(0)| + ∥b∥˙H1 + ∥b∥˙H2) ⩽4CCν
√
R
∥b∥˙B.
4. An estimate for T1. Using estimate (7.8) we obtain
Z ∞
R
x2

D′(xt) −Aν
cos(xt −ϕν)
xt
2
dx ⩽C2
ν
t3
Z ∞
R
1
x(1 +
√
xt)2 dx = 2C2
ν
t3 G(tR).
In combination with Proposition 4, this implies that
∥χ[R,∞)T1χ[R,∞)∥J1 ⩽
√
2Cν
√
R
Z ∞
0
|b0(t)|
t3/2
p
G(tR) dt.
For the integral over [0, 1] we use inequality (7.18) to obtain
Z 1
0
|b0(t)|
t3/2
p
G(tR) dt ⩽(|b′(0)| + ∥b∥˙H2)
Z 1
0
p
G(tR) dt ⩽C(|b′(0)| + ∥b∥˙H2)
for some constant C. For the integral over [1, ∞), using (7.16), for some constant eC
we have
Z ∞
1
|b0(t)|
t3/2
p
G(tR) dt ⩽∥b∥˙H1
Z ∞
1
p
G(tR)
t
dt ⩽eC∥b∥˙H1.
Therefore, we conclude that
∥χ[R,∞)T1χ[R,∞)∥J1 ⩽
√
2(C + eC)Cν
√
R
(∥b∥˙H1 + ∥b∥˙H2 + |b′(0)|)
⩽2
√
2(C + eC)Cν
√
R
∥b∥˙B.
5. An estimate for Z(x, y) + Z(y, x). We denote the operator induced by this
kernel by eZ. Integration of the kernel by parts yields
eZ(x, y) = Z(x, y) + Z(y, x) = Aν
r
2
π
Z ∞
0
b0(t)
xyt
d
dt(sin(xt −ϕν) sin(yt −ϕν)) dt
= −Aν
r
2
π
b′(0)
xy sin2(ϕν)
−Aν
r
2
π
1
xy
Z ∞
0
d
dt
b0(t)
t

sin(xt −ϕν) sin(yt −ϕν) dt.
The first term induces the one-dimensional projector h1(x)⟨h2(y), −⟩L2 with trace
norm bounded by ∥h1∥L2∥h2∥L2. By Lemma 5, for the trace norm of the corres-
ponding operator on L2[R, ∞) we have |Aνb′(0)|/R ⩽|Aν|∥b∥˙B/R.
We apply Proposition 4 to the second term. This results in the estimate
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽|Aν|∥b∥˙B
R
+ |Aν|
R
Z ∞
0

d
dt
b0(t)
t


 dt.
The integral over [0, 1] is estimated as follows in view of (7.19):
Z 1
0

d
dt
b0(t)
t


 dt ⩽∥b∥˙H2.
The integral over [1, ∞) is estimated using (7.16) and the Cauchy–Bunyakovsky–
Schwarz inequality:
Z ∞
1

d
dt
b0(t)
t


 dt ⩽
Z ∞
1
|b′(t)|
t
+ ∥b∥˙H1
t3/2

dt ⩽3∥b∥˙H1.
Therefore, we conclude that
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽5|Aν|∥b∥˙B
R
.
This finishes the proof of Lemma 3.
