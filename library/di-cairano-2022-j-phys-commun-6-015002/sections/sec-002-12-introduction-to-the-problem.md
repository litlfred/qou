---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-002-12-introduction-to-the-problem
section_title: "Introduction to the problem"
section_number: 1.2
pages: 3-4
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
In this section, we revisit and formalize the theoretical derivation of a GLE introduced by Zwanzig [31] putting in
evidence what are the main inconsistencies and giving an insight about how to overcome them.
The physical system that Zwanzig considered is composed by a subsystem that we call heavy particle
described by the variable X ≔(Q, P) where Q is the generalized coordinate and P the conjugated momentum and
a heat bath which is a set of N particles whose state is described by the collective variables Y ≔(q, p) with the same
meaning as before.
The whole Hamiltonian of this system is given by Zwanzig is [31]
H X Y
H X
Y
a X
K Y
a X
,
1
,
3
s
T
(
)
( )
[
( )]
[
( )]
( )
=
+
-
-
where the second term represents the interaction Hamiltonian since it involves the variables of both heavy
particle and heat bath through the a(X) vector. In fact, in order to switch off the interactions, we have to impose
somehow a(X) = 0 for each X ≠0. Finally, the matrix K is a symmetric constant matrix.
The equation of motion for the heat bath and heavy particle variables are, respectively:
dY
dt t
BK Y t
a X t
dX
dt t
V X t
A W X t
K Y t
a X t
,
4
( )
[ ( )
( ( ))]
( )
( ( ))
( ( ))
[ ( )
( ( ))]
( )
=
-
=
-
-
where A and B are two constant antisymmetric matrix, i.e.:
A
B
0
1
1
0
,
0
1
1
0
,
h p
h p
h b
h b
.
.
.
.
⎜
⎟
⎛
⎝
⎞
⎠
⎛
⎝
⎞
⎠
=
-
=
-
such that the ranks of A and B are, in general, different and where W(x) = ∇Xa T(X), V(X) = A∇XHs(X).
The heat-bath equation in (4) can be formally solved and we have:
Y t
a X t
BK t
Y
a X
BK
d
d a X t
d
exp
0
0
exp
.
5
t
0
( )
( ( ))
(
)[ ( )
( ( ))]
(
)
( (
))
( )
ò
t
t
t
t
-
=
-
+
-
2
The time-derivative of the a(X) vector can be rewritten in terms of the W matrix, i.e.

d
d a X t
W
X t
X t
.
6
T
( (
))
( (
))
(
)
( )
t
t
t
t
-
= -
-
-
By replacing equation (5) into the ﬁrst equation in (4) and by making use of equation (6), one gets

dX
dt t
V X t
A W X t
K
BK
W
X t
X t
d
A W X t
K
BK t
Y
a X
exp
exp
0
0
.
7
t
T
0
( )
( ( ))
( ( ))
(
)
( (
))
(
)
( ( ))
(
)[ ( )
( ( ))]
( )
ò
t
t
t
t
=
+
-
-
-
-
At this point, Zwanzig deﬁned the noise vector
F t
K
BK t
Y
a X
exp
0
0
,
8
( )
(
)[ ( )
( ( ))]
( )
= -
-
and the kernel matrix
L t
K
BK t
exp
,
9
( )
(
)
( )
=
and, introducing the canonical partition function
p q Q
H
p q Q
,
exp
,
,
,
10
b
(
∣) ≔
(
(
))
(
)
r
b
-
he formulates the ﬂuctuation-dissipation relation (FDR)
F t
F
k T
t
,
11
B
( ) ·
( )
(
)
(
)
t
z
t
á
ñ =
-
r
where kB and T, respectively, are the Boltzmann constant and the temperature whereas
Tr L
≔
[ ]
z
and Tr
denotes the trace of a matrix.
