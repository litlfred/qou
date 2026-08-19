---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "Langevin equation in systems with also negative temperatures"
section_id: sec-002-12-introduction-to-the-problem
section_title: "Introduction to the problem"
section_number: 1.2
pages: 3-4
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "Communications PAPER • OPEN ACCESS On the derivation of a Nonlinear Generalized Langevin Equation To cite this article: Loris Di Cairano 2022 J. Phys. Commun. 6 015002 — 14 sections: Introduction; Sta"
---
In this section, we revisit and formalize the theoretical derivation of a GLE introduced by Zwanzig[31] putting in
evidence what are the main inconsistencies and giving an insight about how to overcome them.
The physical system that Zwanzig considered is composed by a subsystem that we callheavy particle
described by the variableX ≔ (Q, P) where Q is the generalized coordinate andP the conjugated momentum and
a heat bath which is a set ofN particles whose state is described by the collective variablesY ≔ (q, p) with the same
meaning as before.
The whole Hamiltonian of this system is given by Zwanzig is[31]
HX Y H X Y aX KY aX, 1
2 ,3s T( )( ) [( ) ] [( ) ] ( )=+ - -
where the second term represents the interaction Hamiltonian since it involves the variables of both heavy
particle and heat bath through thea(X) vector. In fact, in order to switch off the interactions, we have to impose
somehow a(X) = 0 for eachX ≠ 0. Finally, the matrixK is a symmetric constant matrix.
The equation of motion for the heat bath and heavy particle variables are, respectively:
dY
dt tB K Y t a X t
dX
dt t VXt A WXt KYt aXt
,
4
() [ () ( () ) ]
( ) ( ( )) ( ( )) [ ( ) ( ( ))] ( )
=-
=- -
where A and B are two constant antisymmetric matrix, i.e.:
AB 01
10 , 01
10 ,
hp
hp
hb
hb
.
.
.
.
⎜⎟
⎛
⎝
⎞
⎠
⎛
⎝
⎞
⎠
= - = -
such that the ranks ofA and B are, in general, different and whereW(x) = ∇Xa T(X), V(X) = A∇XHs(X).
The heat-bath equation in(4) can be formally solved and we have:
Yt a Xt B K t Y a X B K d
d aXt dexp 0 0 exp . 5
t
0
( ) ( ( )) ( )[ ( ) ( ( ))] ( ) ( ( )) ( ) ò t t tt-= - + -
2
J. Phys. Commun.6 (2022) 015002 L Di Cairano
The time-derivative of thea(X) vector can be rewritten in terms of theW matrix, i.e.
d
d aXt W Xt Xt .6T(( ) ) (( ) )( ) ( )t tt t-= - - -
By replacing equation(5) into the ﬁrst equation in(4) and by making use of equation(6), one gets
dX
dt t VXt A WXt K B K W Xt Xt d
AW X t K B K t Y a X
exp
exp 0 0 . 7
t
T
0
( ) (( ) ) (( ) ) ( ) (( ) ) ( )
( ( )) ( )[ ( ) ( ( ))] ( )
ò tt t t=+ - -
--
At this point, Zwanzig deﬁned the noise vector
Ft K B Kt Y aXexp 0 0 , 8( ) ( )[ ( ) ( ( ))] ( )=- -
and the kernel matrix
Lt K B Kt exp , 9() ( ) ()=
and, introducing the canonical partition function
pq Q H pqQ,e x p , , , 1 0 b(∣ ) ≔ ( ( ) ) ( )rb -
he formulates theﬂuctuation-dissipation relation (FDR)
Ft F kT t ,1 1B()· ( ) ( ) ( )tz táñ = - r
where kB and T, respectively, are the Boltzmann constant and the temperature whereas Tr L≔[ ]z and Tr
denotes the trace of a matrix.
