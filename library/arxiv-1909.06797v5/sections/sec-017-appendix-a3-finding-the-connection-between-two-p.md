---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-017-appendix-a3-finding-the-connection-between-two-p
section_title: "Appendix A.3 Finding the connection between two pictures"
section_number: null
pages: 28-30
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
The character of permutation group is given by Frobenius formula
χR(C(⃗k)) =
∆(x)
Y
n
(Pn(x))kn

(h1,h2,···hN)
(A.13)
where
Pn(x) =
N
X
i=1
xn
i ,
∆(x) =
Y
i< j
(xi −x j)
(A.14)
and (x1, · · · , xN) are set of auxiliary variables. The notation [· · · ](h1,··· ,hN) implies
f(x)
(h1,··· ,hN) = coeﬃcient of xh1
1 · · · xhN
N in f(x).
(A.15)
Promoting N auxiliary variables to N complex variables (z1, · · · , zN), Frobenius formula (A.13)
can be written as a residue of a complex function as follows
χ[h(x),C(⃗k′)] =
 1
2πi
!N I [Dz(x)]
z(x)
exp[−N2S χ(h[x],⃗k′)] .
(A.16)
This is subsequently used in (A.5) to obtain
Z =
Y
n
Z
dk′
ndl′
n
Z
[dh(x)]
I
[dz(x)]
I
[dw(x)]
Z ∞
−∞
dt
Z ∞
−∞
ds exp

−N2S total
h
h, z, w,⃗k′,⃗l′, t, s
i
(A.17)
28
where,
−S total
h
h, z, w,⃗k′,⃗l′, t, s
i
=
X
n

k′
n
 
1 + ln
 βnZn
nk′
n
!!
+ l′
n
 
1 + ln
 βnWn
nl′
n
!! 
+ 1
2
Z 1
0
dx−
Z 1
0
dy (ln |z(x) −z(y)| + ln |w(x) −w(y)|)
−
Z 1
0
dxh(x) ln z(x)w(x) + it

X
n
nk′
n −K′
+ is

X
n
nl′
n −K′
.
(A.18)
Extremising S total with respect to h(x), z(x), w(x), k′
n and l′
n, we see that the saddle point equations
are given by
X
n
nk′
n
Zn
zn(x) + −
Z 1
0
dy
z(x)
z(x) −z(y) −h(x) = 0
(variation w.r.t z(x))
(A.19)
where,
Zn =
Z 1
0
dxzn(x).
(A.20)
Similar equation can be obtained when we vary action with respect to w(x). Variation with respect
to h(x) gives
z(x)w(x) = e−i(t+s) = constant (independent of x).
(A.21)
Finally, variation with respect to k′
n and l′
n provides,
βnZn
nk′
n
= e−itn,
and
βnWn
nl′
n
= e−isn.
(A.22)
Since the contours are unit circle around origin, one can take a consistent solution to the above
two equations (A.21,A.22) as
z(x) = eiθ(x),
w(x) = e−iθ(x),
t = s = 0
(A.23)
and
k′
n = l′
n = βnρn
n ,
where
Zn =
Z
dθρ(θ) cos nθ ≡ρn.
(A.24)
Deﬁning ρ(z) = dx
dz equation (A.19) can be written as
h(z) = ⊖
Z
C
dz′ρ(z′)
z
z −z′ +
X
n
nk′
n
Zn
zn.
(A.25)
We deﬁne a quantity ¯h(z)
¯h(z) =
I
C
dz′ρ(z′)
z
z −z′ +
X
n
nk′
n
Zn
zn.
(A.26)
29
¯h(z) is analytic everywhere in complex z plane except inside the support of ρ(z) on C. It has a
branch cuts along the support of ρ(z). If h+(z) and h−(z) are values of ¯h(z) on either sides of branch
cuts then we have
h±(z) = +
X
n
nk′
n
Zn
zn +
I
C
dz′ρ(z′)
z
z −z′ ± iπzρ(z).
(A.27)
Considering contour C to be unit circle we have
X
n
nk′
n
Zn
einθ + −
Z π
−π
dθρ(θ′)
eiθ
eiθ −eiθ′ −h±(θ) ± πρ(θ) = 0
(A.28)
Evaluating the partition function (A.17) on equations (A.19,A.21, A.22) we ﬁnd,
Z =
Z
[Dθ] exp
N2
∞
X
n=1
2βn
n ρn + N21
2−
Z
dθρ(θ)−
Z
dθ′ρ(θ′) ln

4 sin2
 θ −θ′
2
!

.
(A.29)
Thus we see that the partition function is exactly same as the partition function of one plaquette
model written in eigenvalue basis (equation (A.1)) with ρ(θ) being the eigenvalue density. Hence,
we identify the auxiliary variables we used to write the character of symmetric group with eigen-
values of the corresponding unitary matrix model involved.
Separating the saddlepoint equation (A.28) into real and imaginary part we see that the imaginary
part of this equation is same as the saddle point equation (5.9) for ρ(θ). Hence we are left with
only the real part, which is given by,
h±(θ) = 1
2 +
X
n
βn cos nθ ± πρ(θ).
(A.30)
The above two relations can be written as a solution of a quadratic equation of h
h2 −2S (θ)h + S (θ) −π2ρ2(θ) = 0
(A.31)
where S (θ) = 1
2 + P
n βn cos nθ.
