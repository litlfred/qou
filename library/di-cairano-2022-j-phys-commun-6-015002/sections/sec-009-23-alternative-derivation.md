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
7
J. Phys. Commun. 6 (2022) 015002
L Di Cairano
Then, applying the inverse Laplace transform we get:

Q
K
Q
K
K
Q
K
K
a X
t
t
t
t
d
cos
0
sin
0
sin
,
37
t
1 2
1 2
1 2
0
1 2
1 2
( )
(
)
( )
(
)
( )
(
(
)) (
( ))
(
)
ò
t
t
t
=
+
+
-
-
where the matrix-valued function is deﬁned through the series representation:
K
K
K
K
t
n
t
t
n
t
cos
1
2
,
sin
1
2
1
.
n
n
n
n
n
n
n
n
1 2
0
2
1 2
0
2
1
(
)
(
)
(
)!
(
)
(
)
(
)!
å
å
=
-
=
-
+
=
¥
=
¥
+
In order to recover a GLE, in the convolution on the right-hand side the time derivative of the heavy particle
variable has to appear. Therefore, we notice that the kernel matrix K
K
t
sin
1 2
1 2
(
(
))
t
-
can be written as the
derivative of
K
t
cos
1 2
(
(
))
t
-
and an integration by parts leads to:


Q
K
Q
K
K
Q
a X
K
a X
K
a X
X
t
t
t
t
t
t
d
cos
0
sin
0
cos
cos
,
38
X
t
1 2
1 2
1 2
1 2
0
1 2
( )
(
)
( )
(
)
( )
(
( ))
(
( )) (
( ))
(
(
))
(
( ))
( )
(
)
( )
ò
t
t
t
t
t
=
+
+
-
-
-

t
-
where 

a X
a X
X
X
(
( ))
(
( ))
( )
( )
t
t
t
= 
t
.
Now, we note that the heat bath variable enter equation (34) under a speciﬁc combination, i.e., K[Q(t) −
a(X(t))], but this relation can be obtained in equation (38) that is:


K Q
a X
Q
Q
a X
a X
X
t
t
G
t
H
t
S
t
d
0
0
0
,
39
K
K
K
X
t
0
[
( )
(
( ))]
( )
( )
( )(
( )
(
( )))
[
(
)
(
( ))]
( )
(
)
( )
ò
t
t
t
t
-
=
+
-
-
-

t
K
K
K
K
K
H
t
t
G
t
t
S
t
t
cos
,
sin
,
cos
,
40
K
K
K
1 2
1 2
1 2
( ) ≔
(
)
( ) ≔
(
)
( ) ≔
(
( ))
(
)
Finally, we introduce a further canonical basis eI I
n
1
{ } = of
n
which allows us to deﬁne, respectively, the parameter
matrix and the equilibrium map vector:
e
e
g X
X e
f
,
,
41
i
N
J
n
i J i
J
I
n
I
I
1
1
,
1
≔
( ) ≔
( )
(
)
åå
å
h
L
Ä
=
=
=
such that
a X
g X .
42
X
X
( )
( )
(
)
L

=

Hence, we plug equation (39) into equation (34) and we obtain:

X
g
X
I
Q
a X
g
X
g X
X
X
M
t
t
G
t
H
t
t
S
t
d
V
t
0
0
0
.
43
X
K
K
X
K
X
X
t
T
T
t
t
T
T
t
0̈
( )
(
( ))
(
( ) ( )
( )[
( )
(
( ))])
(
( ))(
(
)
)
(
( ))
( )
(
( ))
(
)
( )
( )
( )
( )
ò
t
t
t
t
L
L
L
= 
+
-
-

-

- 
t
In order to recover the common structure of a GLE, we note that the mathematical structure of the equation
obtained above allows to deﬁne the kernel matrix and the noise term as follows:
L
F
I
Q
a X
t
S
t
t
G
t
H
t
,
0
0
0
,
44
K
K
K
T
T
(
) ≔
(
)
( ) ≔
(
( ) ( )
( )[
( )
(
( ))])
(
)
t
t
L
L
L
-
-
+
-
We wish to stress a signiﬁcant difference between the current deﬁnitions of noise vector and kernel matrix in
equation (44) and the previous ones in equation (8) and (9). In the latter, the noise and kernel terms do not
contain any information about the strength of the interactions represented by the coefﬁcients γi,I and all the
parameters γi,I are contained in the equilibrium map. In the former case, the parameters ηi,I have been
completely absorbed into the noise term and kernel matrix.
Therefore, we can recast equation (43) into a nonlinear GLE:

X
g
X
F
g
X
L
g X
X
X
M
t
t
t
t
t
d
V
t .
45
X
X
X
X
t
T
t
t
T
t
0̈
( )
(
( )) ( )
(
( )) (
)
(
( ))
( )
(
( ))
(
)
( )
( )
( )
( )
ò
t
t
t
t
= 
-

-

- 
t
An important step forward in the investigation of stochastic behaviors arising from interacting Hamiltonian
systems would be made if we could solve equation (45) which is a nonlinear stochastic differential equation.
Two different approaches could be employed. From one side, one can attempt a semi-analytical approach
exploiting the same method introduced in [34]. The authors showed that, even though we have a nonlinear
differential equation, but we explicit know the time-dependence of the functions entering the equation2, we can
still apply the Laplace transform method to equation (45). However, this approach cannot always provide an
exact solution but a series representation of the solution is possible. So far, this approach has been applied just
for investigating nonlinear differential equations which are not stochastic but it could be extended to address
stochastic differential equation. A more detailed study will be done in a future paper.
2 In our case, this translates in choosing a speciﬁc potential function so that the equilibrium map is well-deﬁned.
8
J. Phys. Commun. 6 (2022) 015002
L Di Cairano
Another possible approach is the numerical one. In particular, under suitable condition on the kernel
matrix, L(t −τ), a GLE can be converted into a stochastic Volterra equation where several numerical integration
schemes have been developed such as the Euler and Milstein scheme [35].
We now show that adopting deﬁnitions (44), one naturally recover the FDR.
Hence, let us consider the heat bath Hamiltonian from equation (33), namely:

I Q
I
Q
a X
K Q
a X
H
,
2
1
2
,
.
46
2
N
N
3
3
(
)
( )
(
( ))
(
)


=
+
á
-
-
ñ
P
The canonical probability density is given by:
X
Q
I
Z e
e
0
0 ,
0
1
,
47
I I
Q
a X
K Q
a X
,
0
0 ,
0
0
N
N
2
3
2
3
(
( )∣
( )
( )) ≔
·
(
)
( )
(
( ))
(
( )
(
( )))


r
- á
ñ
- á
-
-
ñ
b
b
where Z is the canonical partition function
Q
I
Z
e
d
d
0
0 ,
48
I
Q
X
0 ,
0 ,
0
≔
( )
( )
(
)
[
( ( )
( )
( ))]
ò
b
-
HB
and where β−1 = kBT.
Let us note that, since X is held ﬁxed, we can introduce the following substitution:
x
Q
a X
0
0
0 ,
49
( ) ≔
( )
(
( ))
(
)
-
which does not affect the integration measure, i.e. dx(0) = dQ(0), thereby, the canonical partition and density
functions read:
X
x
I
x
I
Z e
Z
e
d
d
0
0 ,
0
1
,
0
0 ,
50
I I
x
Kx
I I
x
Kx
,
0 ,
0
,
0 ,
0
N
N
N
N
2
3
3
2
3
3
(
( )∣( )
( )) ≔
≔
( )
( )
(
)
(
( )
( )
)
(
( )
( )
)




ò
r
-
á
ñ
-á
ñ
-
á
ñ
-á
ñ
b
b
and the integration measure assumes manifestly a Gaussian form.
By exploiting equation (49), the noise vector in equation (44) becomes:
F
I
x
t
G
t
H
t
0
0 ,
51
K
K
T
( ) ≔
(
( ) ( )
( ) ( ))
(
)
L
+
and the computation of the second order correlation functions can be done easily [30]:
I
x
I
I
x
x
K
x
I
0
0
,
1
,
,
.
52
1
N
3
(
)

b
b
á ñ = á ñ =
á Ä ñ =
á
Ä
ñ =
á
Ä ñ =
r
r
r
r
r
-
Furthermore, we notice that the noise, F, is a mean-zero vector, namely: 〈F(t)〉ρ = 0. In order to explicitly write
the ﬂuctuation-dissipation relation (noise autocorrelation function), we ﬁrst expand the tensor product, i.e.:
F
F
I
x
I
x
I
I
x
x
x
I
I
x
t
G
t
H
t
G
H
G
t
G
H
t
H
H
t
G
G
t
H
0
0
0
0
0
0
0
0
0
0
0
0
.
53
K
K
K
K
K
K
K
K
K
K
K
K
T
T
T
T
T
T
T
T
( )
( )
(
( ) ( )
( ) ( ))
( ( )
( )
( )
( ))
(
( ) ( )
( )
( )
( ) ( )
( )
( )
( ) ( )
( )
( )
( ) ( )
( )
( )
(
)
t
t
t
t
t
t
t
L
L
L
L
Ä
=
+
Ä
+
=
Ä
+
Ä
+
Ä
+
Ä
Thus, by exploiting equation (52), the average of the tensor product above becomes:
F
F
K
K
t
t
cos
,
54
T
1
1 2
( )
( )
(
(
))
(
)
t
b
t
L
L
á
Ä
ñ =
-
r
-
where we used equation (40) and knowing that
K
t
cos
1 2
(
) and
K
t
sin
1 2
(
) commute with any polynomial of K.
We obtained in equation (54), the ﬂuctuation-dissipation relation; in fact, by comparing the operator on the
right-hand side above with equation (44), we explicitly have:
F
F
L
t
t
.
55
1
( )
( )
(
)
(
)
t
b
t
á
Ä
ñ =
-
r
-
As proof of consistence and show-case example, let us ﬁnally apply such a derivation to the Hamiltonian
system in equation (12) proposed by Zwanzig. Thus, the equilibrium map is given by
a
X
X
i
N
,
1,
,
i
H
i
i
2
( ) ≔
[
]
h
w
"
Î
whereas the interaction matrix K is
K
e
e ,
56
i
N
i
i
i
1
2
≔
(
)
å w
Ä
=
In this setting, it consists in imposing f1(X) ≔X with
i
i
i
i
,1
2
h
h
h w
º
=
and ηi,I = 0 for any I ä [2, n]. This
implies that the matrix Λ in equation (41) reduces to
9
J. Phys. Commun. 6 (2022) 015002
L Di Cairano
e
e ,
i
N
i
i
i
1
2
1
≔å
h
w
L
Ä
=
whereas
e
e
S
t
t
sin
.
57
K
i
N
i
i
i
i
1
2
(
)
(
(
))
(
)
å
t
w
w
t
-
=
-
Ä
=
Therefore, the kernel matrix reduces
L
e
e
t
t
cos
,
58
i
N
i
i
i
i
i
1
2
2
(
) ≔
(
(
))
(
)
å
t
h
w
w
t
-
-
Ä
=
whose trace coincides with the ζZ function (15) in the Zwanzig’s result [31]. However, now, the continuum limit
can be computed. We conclude this section discussing the importance of including all the parameters
representing the interactions (in this case ηi) directly in the deﬁnitions of the kernel matrix and noise terms In
particular, this can be appreciated as soon as one computes the continuum limit of the friction matrix, which
consists in assuming that the set of heat bath frequencies
d
i i
N
1
≔{ }
w
=
S
becomes a continuum set

Ì
S
together with a distribution function g(ω) of frequencies which depends on the speciﬁc interactions we
considered.
In this limit, one replaces the sum over the frequencies with an integral [31]:
g
d ,
i
N
i
1
⟶
( )
( )
ò
å h
h w
w
w
=
S
where
i i
N
1
{ }
h
= is any set of coefﬁcients and η(ω) is the associated frequency-dependent function in the continuum
limit.
Now, if the kernel function is deﬁned as in equation (17), i.e., without including the parameters γi, the
continuum limit, which reads:
t
t
g
d
cos
,
2
(
) ⟶
( (
)) ( )
ò
x
t
w
w
t
w
w
-
-
S
cannot provide a bounded continuous kernel function.
Conversely, including the coefﬁcients γi in the kernel as in (18), one assumes that the set
i i
N
1
{ }
g
= becomes a
continuous function γ(ω) of the frequency variable, so that the continuum limit can be applied
t
t
g
d
cos
,
59
2
2
(
) ⟶
( (
))
( ) ( )
(
)
ò
z
t
w
t
w
g
w
w
w
-
-
S
choosing γ such that it remains bounded as ω →∞.
The degree of freedom represented by the γ function can be ﬁxed for requiring the boundedness of the kernel
function. In practice, the remaining effort consists in providing the correct modeling, depending on the
interaction nature, of the function J(ω) ≔γ2(ω)g(ω) even called density function. with the existing techniques
already introduced in the literature [19].
