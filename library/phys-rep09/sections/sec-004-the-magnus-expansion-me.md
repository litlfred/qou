---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-004-the-magnus-expansion-me
section_title: "The Magnus expansion (ME)"
section_number: null
pages: 9-11
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Magnus’ proposal with respect to the linear evolution equation
Y ′(t) = A(t)Y(t)
(30)
with initial condition Y(0) = I, was to express the solution as the exponential of a certain function,
Y(t) = exp Ω(t).
(31)
This is in contrast to the representation
Y(t) = T

exp
Z t
0
A(s)ds

in terms of the time-ordering operator T introduced by Dyson [13].
It turns out that Ω(t) in (31) can be obtained explicitly in a number of ways. The crucial point is to derive a differential
equation for the operator Ωthat replaces (30). Here we reproduce the result first established by Magnus as Theorem III
in [4]:
Theorem 1 (Magnus 1954). Let A(t) be a known function of t (in general, in an associative ring), and let Y(t) be an unknown
function satisfying (30) with Y(0) = I. Then, if certain unspecified conditions of convergence are satisfied, Y(t) can be written in
the form
Y(t) = exp Ω(t),
where
dΩ
dt =
∞
X
n=0
Bn
n!
adn
ΩA,
(32)
and Bn are the Bernoulli numbers. Integration of (32), by iteration, leads to an infinite series for Ω, the first terms of which are
Ω(t) =
Z t
0
A(t1)dt1 −
1
2
Z t
0
Z t1
0
A(t2)dt2, A(t1)

dt1 + · · · .
2.1. A proof of Magnus’ Theorem
The proof of this theorem is largely based on the derivative of the matrix exponential map, which we discuss next. Given
a scalar function ω(t) ∈R, the derivative of the exponential is given by d exp(ω(t))/dt = ω′(t) exp(ω(t)). One could think
of a similar formula for a matrix Ω(t). However, this is not the case, since in general [Ω, Ω′]̸ = 0. Instead, one has the
following result.
Lemma 2. The derivative of a matrix exponential can be written alternatively as
(a)
d
dt
exp(Ω(t)) = d expΩ(t)(Ω′(t)) exp(Ω(t)),
(33)
(b)
d
dt
exp(Ω(t)) = exp(Ω(t))d exp−Ω(t)(Ω′(t)),
(34)
(c)
d
dt
exp(Ω(t)) =
Z 1
0
exΩ(t) Ω′(t)e(1−x)Ω(t)dx,
(35)
160
S. Blanes et al. / Physics Reports 470 (2009) 151–238
where d expΩ(C) is defined by its (everywhere convergent) power series
d expΩ(C) =
∞
X
k=0
1
(k + 1)!
adk
Ω(C) ≡
exp(adΩ) −I
adΩ
(C).
(36)
Proof. Let Ω(t) be a matrix-valued differentiable function and set
Y(σ, t) ≡∂
∂t (exp(σΩ(t))) exp(−σΩ(t))
for σ, t ∈R. Differentiating with respect to σ ,
∂Y
∂σ = ∂
∂t (exp(σΩ)Ω) exp(−σΩ) + ∂
∂t (exp(σΩ)) (−Ω) exp(−σΩ)
=

exp(σΩ)Ω′ + ∂
∂t (exp(σΩ)) Ω

exp(−σΩ) −∂
∂t (exp(σΩ)) Ωexp(−σΩ) = exp(σΩ)Ω′ exp(−σΩ)
= exp(adσΩ)(Ω′) =
∞
X
k=0
σ k
k!
adk
Ω(Ω′),
where the first equality in the last line follows readily from (12) and (13). On the other hand
d
dt (exp Ω) exp(−Ω) = Y(1, t) =
Z 1
0
∂
∂σ
Y(σ, t)dσ
(37)
since Y(0, t) = 0, and
Z 1
0
∂
∂σ
Y(σ, t)dσ =
Z 1
0
∞
X
k=0
σ k
k!
adk
Ω(Ω′)dσ =
∞
X
k=0
1
(k + 1)!
adk
Ω(Ω′),
from which formula (33) follows. The convergence of the power series (36) is a consequence of the boundedness of the ad
operator: ∥adΩ∥≤2∥Ω∥.
Multiplying both sides of (33) by exp(−Ω), we have
e−ΩdeΩ
dt
= e−Ωd expΩ(Ω′)eΩ= ead−Ωd expΩ(Ω′) =
ead−Ω−I
ad−Ω
Ω′ = d exp−Ω(Ω′)
from which (34) follows readily. Finally, Eq. (35) is obtained by taking
Z 1
0
∂
∂σ
Y(σ, t)dσ =
Z 1
0
exp(σΩ)Ω′ exp(−σΩ)dσ
in (37).
■
According to Rossmann [46] and Sternberg [47], formula (33) was first proved by F. Schur in 1890 [48] and was taken up
later from a different point of view by Poincaré (1899), whereas the integral formulation (35) has been derived a number of
times in the physics literature [19].
As a consequence of the Inverse Function Theorem, the exponential map has a local inverse in the vicinity of a point Ω
at which d expΩ= (exp(adΩ) −I)/adΩis invertible. The following lemma establishes when this takes place.
Lemma 3 (Baker 1905). If the eigenvalues of the linear operator adΩare different from 2mπi with m ∈{±1, ±2, . . .}, then
d expΩis invertible. Furthermore,
d exp−1
Ω(C) =
adΩ
eadΩ−I
C =
∞
X
k=0
Bk
k!
adk
Ω(C)
(38)
and the convergence of the d exp−1
Ωexpansion is certainly assured if ∥Ω∥< π.
Proof. The eigenvalues of d expΩare of the form
µ =
X
k≥0
νk
(k + 1)! =
eν −1
ν
,
where ν is an eigenvalue of adΩ. By assumption, the values of µ are non-zero, so that d expΩis invertible. By definition
of the Bernoulli numbers, the composition of (38) with (36) gives the identity. Convergence for ∥Ω∥< π follows from
∥adΩ∥≤2∥Ω∥and from the fact that the radius of convergence of the series expansion for x/(ex −1) is 2π.
■
S. Blanes et al. / Physics Reports 470 (2009) 151–238
161
It remains to determine the eigenvalues of the operator adΩ. In fact, it is not difficult to show that if Ωhas n eigenvalues
{λj, j = 1, 2, . . . , n}, then adΩhas n2 eigenvalues {λj −λk, j, k = 1, 2, . . . , n}.
As a consequence of the previous discussion, Theorem 1 can be rephrased more precisely in the following terms.
Theorem 4. The solution of the differential equation Y ′ = A(t)Y with initial condition Y(0) = Y0 can be written as Y(t) =
exp(Ω(t))Y0 with Ω(t) defined by
Ω′ = d exp−1
Ω(A(t)),
Ω(0) = O,
(39)
where
d exp−1
Ω(A) =
∞
X
k=0
Bk
k!
adk
Ω(A).
Proof. Comparing the derivative of Y(t) = exp(Ω(t))Y0,
dY
dt =
d
dt (exp(Ω(t))) Y0 = d expΩ(Ω′) exp(Ω(t))Y0
with Y ′ = A(t)Y, we obtain A(t) = d expΩ(Ω′). Applying the inverse operator d exp−1
Ωto this relation yields the differential
equation (39) for Ω(t).
■
Taking into account the numerical values of the first few Bernoulli numbers, the differential equation (39) therefore
becomes
Ω′ = A(t) −
1
2[Ω, A(t)] +
1
12[Ω, [Ω, A(t)]] + · · · ,
which is nonlinear in Ω. By defining
Ω[0] = O,
Ω[1] =
Z t
0
A(t1)dt1,
and applying Picard fixed point iteration, one gets
Ω[n] =
Z t
0

A −
1
2[Ω[n−1], A] +
1
12[Ω[n−1], [Ω[n−1], A]] + · · ·

dt1
and limn→∞Ω[n](t) = Ω(t) in a suitably small neighborhood of the origin.
