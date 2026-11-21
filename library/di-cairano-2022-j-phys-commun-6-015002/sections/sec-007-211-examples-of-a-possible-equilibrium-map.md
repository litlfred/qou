---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-007-211-examples-of-a-possible-equilibrium-map
section_title: "Examples of a possible equilibrium map."
section_number: 2.1.1
pages: 7-8
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
Let us consider a Lennard-Jones-like interaction potential of the form




Q X
X
q
X
q
,
4
,
25
LJ
i
N
i
i
i
i
i
i
i
1
12
⎜
⎟
⎜
⎟
⎡
⎣
⎢⎛
⎝
⎞
⎠
⎛
⎝
⎞
⎠
⎤
⎦
⎥
(
) ≔
(
)
å h
s
s
-
-
-
=


V
where the parameters
,i
i

s h Î
have the dimension of an energy and a length, respectively; lastly,
i

Î

are
dimensionless parameters. Note that we do not consider any mutual interaction between the heat bath particles.
The requirement (23), namely:
*
Q
X
0
,
,
q
LJ
i
(
)

=
V
where

*
*
*
Q
q
q
,
, N
1
{
}
=
is the equilibrium conﬁguration of the heat bath, yields


*
X
q
i
N
2
,
1,
.
i
i
i
2
1 3
2
[
]
s
-
=
"
Î

This set of relations can be geometrically interpreted imaging that any particle, let us say, the i-th one, lies on a
point of the sphere
R
2
i

with radius Ri = 21/6σi. The reason why any point on the sphere is equivalent to each
other is due to the fact we do not have any mutual interaction between the heat bath particles.
Therefore, every equilibrium position vector
*
qi can be related to the heavy particle vector X, introducing
any unit vector n(X) (

n X
1
3
( ) = ) such that
*
q
X
n X
i
N
2
,
1,
.
i
i
i
i
1 6
≔
( )
[
]
s
+
"
Î


In general, it could depend on X, for example, such as n(X) = X/∥X∥. Thus, the equilibrium map may read:
/
a X
X
n X
i
N
2
,
1,
.
26
i
i
i
i
1 6
( ) ≔
( )
[
]
(
)
s
+
"
Î


In so doing, the ﬁrst and second term in harmonic expansion (24) read
a X
X
K
a X
X
Hess
,
,
,
2
36
1
,
27
JL
i
N
i
ii
LJ ii
i
i
i
1
2 3
2
2
3
⎜
⎟
⎛
⎝
⎞
⎠
( ( )
)
≔
[
] ( ( )
)
(
)

å h
h
s
= -
=
=

V
V
6
so that
a X
X
,
JL( ( )
)
V
can be dropped since constant and the potential function ca be approximated as follows
Q X
q
a X
K
q
a X
,
1
2
,
.
28
JL
i j
N
i
i
ij
j
j
,
1
3
(
)
( )
(
( ))
(
)

å
»
á
-
-
ñ
=
V
Note that the factor in the Kii matrix of equation (27) has the physical dimension of a frequency, therefore, we
deﬁne a new set of frequencies
i
N
2
36
,
1,
,
29
i
i
i
i
2
2 3
2
2
≔
[
]
(
)
w
h
s
"
Î

which allows us to rewrite the initial set of parameters (ηi, òi, σi) in terms of a new one: (ωi, ηi, òi); in particular, the
equilibrium map ai in equation (26) now reads:
a X
X
n X
i
N
12
,
1,
.
30
i
i
i
i
( ) ≔
( )
[
]
(
)
h
w
+
"
Î

We note that if X

Î
then we have n(X) = X/|X| and this implies that n X
sgn X
( )
( )
=
. Therefore, during the
system dynamics, that is, along the equation of motion, the function X = X(t) gives rise to a discontinuous
equilibrium map since n X
sgn X t
( )
( ( ))
=
can change sign discontinuously in time passing from +1 to −1 and
viceversa. Hence, the application to a one-dimensional case requires that the potential function is not of the
form V = V(|X −òiqi|).
By going back to the three-dimensional case, we observe that the interaction matrix K does not depend on
the parameters ηi and òi describing the interactions.
We will show that, in order to coherently deﬁne a continuum limit of the kernel function appearing in a GLE
obtained through the elimination procedure, we have to normalize the equilibrium map as we show in the
upcoming section.
