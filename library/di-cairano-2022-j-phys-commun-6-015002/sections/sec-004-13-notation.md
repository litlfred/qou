---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-004-13-notation
section_title: "Notation"
section_number: 1.3
pages: 5-6
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
In this section, we formalize the derivation introduced in the previous section.

We consider a Hamiltonian function describing a classical physical system composed bya heat bath (P)
interacting with a heavy particle (Z). The heat bath consists of N particles with mass m = 1 smaller than the
heavier particle mass M.

We assume that the system is embedded in the three dimensional physical space R? so that the phase space,
denoted byT, isa subset of R&Y x R°N x R° x R°. Therefore, the heat bath conjugated coordinates are:

N N
[%:= er e€ RY, Qe =>)ae e ERY, a=x,y,z (19)
i=1 i=1
where we have introduced the canonical base {e;}_, of RN. The heavy particle Hamiltonian conjugated
coordinates are

3 3
X= SV) Xe, ER’, P= D> Pee, € RB.

asl a=1

The system Hamiltonian function, #: T —> R can be split into three terms:

HP, I, X, Q) = Ha(P, X) + Hall, Q) + Hinr(Q, X),

where, as usual, we have:



P X
P
X
I Q
I
p
H
M
V
H
,
2
,
,
2
2
,
20
i
N
i
2
2
1
2
N
3
3
3
(
)
( )
(
)
(
)



å
=
+
=
=
=
B
P
where the potential function V:
3



describes any external force which just acts on the heavy particle and it
could have a generic dependence on X.
The interaction term is given by:
Q X
q
a X
K
q
a X
H
,
1
2
,
.
21
INT
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
) ≔
( )
(
( ))
(
)

å á
-
-
ñ
=
Thus, the interactions are described by the so-called interaction matrix which is a linear application
K:
N
N
3
3



acting on the heat bath degrees of freedom. Note that each Kij is a three dimensional matrix since
also the spatial degrees of freedom are included.
The meaning of the interaction described by HINT is to assume a harmonic approximation around the
equilibrium positions Q* ≔a(X) of the heat bath system, where a:
N
3
3



provides the equilibrium
conﬁguration of all the heat bath particles for a given X
3

Î
.
The system of Hamilton’s equations, then, reads:




X
P
P
a
X
K Q
a X
X
Q
I
I
K Q
a X
t
t
M
t
t
t
t
V
t
t
t
t
t
t
,
,
,
,
22
X
X
t
T
t
( )
( )
( )
(
( ))
(
( )
(
( )))
(
( ))
( )
( )
( )
(
( )
(
( )))
(
)
( )
( )
=
= 
-
- 
=
= -
-
where
a:
X t
N
3
3
3
( )





´
and the superscript T denotes the transpose operation.
The system of equations above can be reduced to a GLE for the system position vector X(t). To do so, one ﬁrst
focuses on the heat bath equations (the last two equations) and, by just having a linear dependence on the Q-
coordinates, one interprets the factor Ka(X) as an external force. Hence, one exploits the Laplace transform
method to obtain a formal solution QS(t) for the heat bath position vector. Actually, the Hamiltonian (21)
presents a translational invariance since it only depends on Q −a(X). This feature reﬂects on the formal heat
bath solution and, as we will see later, we obtain an explicit mathematical expression of the heat bath solution
directly in terms of QS(t) −a(X(t)). Then, the solution can be plugged into the equation of motion of the heavy
particle and the resulting equation explicitly takes the form of a GLE.
We will explicitly employ such a procedure in the next section after having studied more deeply the
properties of the equilibrium map a(X) which plays a fundamental role in the deﬁnition of the kernel matrix and
noise vector.
We conclude this section, mentioning that the procedure above described, called elimination of the heat
bath degrees of freedom, has been already introduced by Kac et al [30] ﬁrst and by Zwanzig [31] later. However,
Kac et al just considered linear system-heat bath interactions that, in our notation, translates in deﬁning the a
map to be ai(X) ≔X and absorbing all the parameters representing the interaction strength within the K matrix.
Zwanzig extended their system assuming a generic dependency of the a map on the heavy particle position
vector X and since it could be nonlinear, the elimination procedure led to a nonlinear GLE.
