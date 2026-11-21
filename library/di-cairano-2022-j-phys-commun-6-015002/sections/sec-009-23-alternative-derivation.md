---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-009-23-alternative-derivation
section_title: "Alternative derivation"
section_number: 2.3
pages: 8-11
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
2.3. Alternative derivation
The system of Hamilton’s equations of motion (22) based on the Hamiltonian (33) written as a system of second
order differential equations reads:
X
a
X
K Q
a X
X
t
t
t
t
V
t ,
34
X
X
t
T
ẗ
( )
(
( ))
(
( )
(
( )))
(
( ))
(
)
( )
( )
= 
-
- 
Q
K Q
a X
t
t
t
.
35̈
( )
(
( )
(
( )))
(
)
= -
-
We note that equation (35) is linear in the heat bath-variables Q, this allows us to apply the Laplace transform
method [24–26]. Hence, the Laplace transform of equation (35) is

Q
K
Q
Q
Ka X
s
s
s
s
1
0
0
.
36
2
1
( )
(
)
[
( )
( )
(
( ))]
(
)
=
+
+
+
~
~
-
IOP Publishing

J. Phys. Commun. 6 (2022) 015002 LDiCairano

Then, applying the inverse Laplace transform we get:

. t
Q(t) = cos(K'/24) Q(0) + K-!/? sin(K'/t) Q(0) + f K!/? sin(K'/2(t — 7))a(X (1) dr, (37)
0
where the matrix-valued function is defined through the series representation:
SS (=1)" : SS (=1)"
cos(K'/*t) = > ——_K"1?", sin(K'/7t) = S> ——_ kr"!
& Qn)!  Qn+ Dd!

In order to recover a GLE, in the convolution on the right-hand side the time derivative of the heavy particle
variable has to appear. Therefore, we notice that the kernel matrix K!/? sin(K'/?(t — 7)) can be written as the
derivative of cos(K'/?(t — )) andan integration by parts leads to:

Q(t) = cos(K'/7t)Q(0) + K~!/? sin(K'/7t) Q(0) + a(X(r7)) — cos(K'/2(t))a(X(t))
-f cos(K'/?(t — 7)) Vxinya(X (7) X (7) dr, (38)
0

where 4(X(7)) = Vx(ya(X(7))X (7).
Now, we note that the heat bath variable enter equation (34) under a specific combination, i.e., K[Q(t) —
a(X(t))], but this relation can be obtained in equation (38) that is:

K[Q(t) — a(X(t))] = Gx (1) Q(0) + Hx (t)(Q(0) — a(X(0))) — f [Sk(t — 7) Vx a(X(7))]X (1) dr,
(39)
H(t) = K cos(K'’t), Gx(t) := sin(K'/2t), Sk (t) := K cos(K'/?(t)), (40)

Finally, we introduce a further canonical basis {e;}/_ of R” which allows us to define, respectively, the parameter
matrix and the equilibrium map vector:

Non n
A= myer Sep — g(X) = DOF, Ker (41)
I=1

i=1J=1
such that
Vxa(X) = AVyg(X). (42)
Hence, we plug equation (39) into equation (34) and we obtain:

MX(t) = Veg” XA’ (Gx (HI) + Hx (QO) — a(X(0))])
-f Vn? (X(D)(A'SK (t= TIA) Vang (X(T) X (1) dr — Ve V(X). (43)

In order to recover the common structure ofa GLE, we note that the mathematical structure of the equation
obtained above allows to define the kernel matrix and the noise term as follows:

L(t — 7) := A'Sx(t — T)A,
F(t) := A'(Gx(t)1(0) + Hx(t)[Q(0) — a(X(0))]), (44)

We wish to stress a significant difference between the current definitions of noise vector and kernel matrix in
equation (44) and the previous ones in equation (8) and (9). In the latter, the noise and kernel terms do not
contain any information about the strength of the interactions represented by the coefficients ¥;,, and all the
parameters 7;,,are contained in the equilibrium map. In the former case, the parameters 77;,, have been
completely absorbed into the noise term and kernel matrix.

Therefore, we can recast equation (43) into a nonlinear GLE:

MX(t) = Veg! (X())FO) — f Vag! (X(t) L(t — 7) Ve~g (XK (7) X (1) dr — Vx V (XO). (45)

An important step forward in the investigation of stochastic behaviors arising from interacting Hamiltonian
systems would be made if we could solve equation (45) which is a nonlinear stochastic differential equation.

Two different approaches could be employed. From one side, one can attempt a semi-analytical approach
exploiting the same method introduced in [34]. The authors showed that, even though we have a nonlinear
differential equation, but we explicit know the time-dependence of the functions entering the equation’, we can
still apply the Laplace transform method to equation (45). However, this approach cannot always provide an
exact solution but a series representation of the solution is possible. So far, this approach has been applied just
for investigating nonlinear differential equations which are not stochastic but it could be extended to address
stochastic differential equation. A more detailed study will be done in a future paper.

In our case, this translates in choosing a specific potential function so that the equilibrium map is well-defined.

IOP Publishing

J. Phys. Commun. 6 (2022) 015002 LDiCairano

Another possible approach is the numerical one. In particular, under suitable condition on the kernel
matrix, L(t — T),a GLE can be converted into a stochastic Volterra equation where several numerical integration
schemes have been developed such as the Euler and Milstein scheme [35].

We now show that adopting definitions (44), one naturally recover the FDR.

Hence, let us consider the heat bath Hamiltonian from equation (33), namely:

IITs 1

Ag, Q = + 7 {2 — a(X), K(Q — a(X)))g. (46)

The canonical probability density is given by:

p(X (0)|Q(0), 1(0)) = se ites : 2 (Q—aXO),K(QW)—aXO))) ga (47)

where Z is the canonical partition function
Ze f e- 121 0).Q0)XO)1gQ (0) dI(0), (48)

and where 3-! = kgT.
Let us note that, since X is held fixed, we can introduce the following substitution:

x(0) = Q(0) — a(X(0)), (49)
which does not affect the integration measure, i.e. dx(0) = dQ(0), thereby, the canonical partition and density
functions read:

p(X(0)|x(0), 1(0)) += i ECL D)g3n — (x(0),Kxe(0)) 23 ),
Z
Zs f eb)» — (#0)5K())22®) dee (0) AT (0), (50)
and the integration measure assumes manifestly a Gaussian form.
By exploiting equation (49), the noise vector in equation (44) becomes:
F(t) = A'(Gx(t)I() + Hx (t)x(0)), (1)
and the computation of the second order correlation functions can be done easily [30]:

lpn —1
(Dp = (x)p = 0; (I@I)p = a (x ®@ x)p = (x @ I), =0. (52)

B B >

Furthermore, we notice that the noise, F, isa mean-zero vector, namely: (F(t)) p=0.In order to explicitly write
the fluctuation-dissipation relation (noise autocorrelation function), we first expand the tensor product, i.e.:
F(t) @ F(t) = M'(Gx (IO) + Hx()x(0) ® CO)GK(T) + XOHE TA
= A(Gx(t)1 (0) @ (0) G(T) + Hg (t)x(0) @ x(0) Hk (7)
+ Hx (t)x(0) ® I(0) Gh(r) + Gx(t)I(0) @ x (0)He(r)A. (53)
Thus, by exploiting equation (52), the average of the tensor product above becomes:
(F(t) ® F(7))y = B-'ATK cos(K'/(t — 7) A, (54)

where we used equation (40) and knowing that cos(K'/?t) and sin(K!/?t) commute with any polynomial of K.
We obtained in equation (54), the fluctuation-dissipation relation; in fact, by comparing the operator on the
right-hand side above with equation (44), we explicitly have:

(F(t) @ F(t))) = GLU — 7). (55)

As proof of consistence and show-case example, let us finally apply such a derivation to the Hamiltonian
system in equation (12) proposed by Zwanzig. Thus, the equilibrium map is given by
a}l(x) = “Ex, Vie f,NI
w;

whereas the interaction matrix K is

N

K=)\ wie; ® ei, (56)

i=1
In this setting, it consists in imposing f,(X) = X with n; = nj.) = 0; /w? and j= 0 for any I € [2, n]. This
implies that the matrix A in equation (41) reduces to

IOP Publishing

J. Phys. Commun. 6 (2022) 015002 LDiCairano

whereas
N
Sx(t — 7) = )ou7 sin(wi(t — 7))ej ® e. (57)
i=1
Therefore, the kernel matrix reduces
N 7
L(t— 7) = > 5 cos(wi(t — 7))e; ®@ ej, (58)
i=1 Vi

whose trace coincides with the ¢z function (15) in the Zwanzig’s result [3 1]. However, now, the continuum limit
can be computed. We conclude this section discussing the importance of including all the parameters
representing the interactions (in this case 1;) directly in the definitions of the kernel matrix and noise terms In
particular, this can be appreciated as soon as one computes the continuum limit of the friction matrix, which
consists in assuming that the set of heat bath frequencies = {w;}, becomes acontinuum set Y C R
together with a distribution function g(w) of frequencies which depends on the specific interactions we
considered.

In this limit, one replaces the sum over the frequencies with an integral [31]:

N

Sn i; nw) g(w)dw,

i=1

where {17;}_, is any set of coefficients and 1(w) is the associated frequency-dependent function in the continuum
limit.

Now, if the kernel function is defined as in equation (17), i.e., without including the parameters 7; the
continuum limit, which reads:

&(t-—T) — I w* cos(w(t — T))g(w)dw,

cannot provide a bounded continuous kernel function.
Conversely, including the coefficients +; in the kernel as in (18), one assumes that the set {7;}., becomes a
continuous function 7(w) of the frequency variable, so that the continuum limit can be applied

(t-n— i COCR 2g (we) de, (59)
choosing such that it remains bounded as w — 00.

The degree of freedom represented by the 7 function can be fixed for requiring the boundedness of the kernel
function. In practice, the remaining effort consists in providing the correct modeling, depending on the
interaction nature, of the function J(w) = YF w)gw) even called density function. with the existing techniques
already introduced in the literature [19].
