---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-008-22-generalization-of-the-equilibrium-map
section_title: "Generalization of the equilibrium map"
section_number: 2.2
pages: 8-8
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
In order to make our derivation as general as possible, we assume to have n heavy particle position-dependent
functions,
X
fI
I
n
1
{ ( )} = , such that each ai map can be written as a sum of these functions weighted with different
parameters
i I,

h
Î
which, in turn, represent the interaction strength.
Thus, we have:
a X
X
f
,
31
i
I
n
i I I
1
,
( ) ≔
( )
(
)
å h
=
Essentially, the main trick is to separate, in the equilibrium map, the dependence by X from the dependence by
the parameters ηi,I, so that the fI-functions do not depend on such parameters. Although each function fI could
have a generic X dependence, without loss of generality, we assume that only the gradient of the ﬁrst function f1
equals the identity matrix in
3
. These assumptions can be formalized as follows
X
X
f
f
I
N
1
,
1
,
2,
.
32
X
X
I
1
3
3
( )
( )
[
]
(
)



=

¹
"
Î
The speciﬁc case provided in equation (26) can be obtained from the deﬁnition (31) posing n = 2 and f1(X) ≔X
and f2(X) ≔X/∥X∥.
Therefore, in this setting, the Hamiltonian function of the system is:


P X
P
X
I
q
X
K
q
X
H
M
V
f
f
,
2
2
1
2
,
.
33
I J
n
i j
N
i
i I I
ij
j
i J J
2
2
,
1 ,
1
,
,
N
3
3
3
(
)
( )
( )
(
( ))
(
)



å å
h
h
=
+
+
+
á
-
-
ñ
=
=
