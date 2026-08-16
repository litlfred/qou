---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "Langevin equation in systems with also negative temperatures"
section_id: sec-004-13-notation
section_title: "Notation"
section_number: 1.3
pages: 5-6
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "Communications PAPER • OPEN ACCESS On the derivation of a Nonlinear Generalized Langevin Equation To cite this article: Loris Di Cairano 2022 J. Phys. Commun. 6 015002 — 14 sections: Introduction; Sta"
---
In this section, we formalize the derivation introduced in the previous section.
We consider a Hamiltonian function describing a classical physical system composed by a heat bath(P)
interacting with a heavy particle (B). The heat bath consists ofN particles with massm = 1 smaller than the
heavier particle massM.
We assume that the system is embedded in the three dimensional physical space 3 so that thephase space,
denoted by Γ, is a subset of NN333 3  ´´ ´ . Therefore, the heat bath conjugated coordinates are:
eeIp Qq x y z ,, , , , 1 9
i
N
i i N
i
N
i i N
11
≔≔ ( ) åå aÎÎ =a a a a
==
where we have introduced the canonical base ei i
N
1{ }= of N .TheheavyparticleHamiltonianconjugated
coordinatesare
Xe P e XP ,.
1
3
3
1
3
3≔≔ åå ÎÎ
a
a a
a
a a
==
The system Hamiltonian function, : ⟶ GH can be split into three terms:
PIXQ PX IQ QXHH H,, , , , , , INT() ≔ ( ) ( ) ( ) ++H BP
4
J. Phys. Commun.6 (2022) 015002 L Di Cairano
where, as usual, we have:

 
PX
P
X
IQ
I p
H M V
H
, 2 ,
, 22 ,2 0
i
N i
2
2
1
2N
3
33
() ( )
() ( )


å
=+
==
=
B
P
where the potential functionV : 3  describes any external force which just acts on the heavy particle and it
could have a generic dependence onX.
The interaction term is given by:
Q X qa X K qa XH , 1
2 ,. 2 1INT
ij
N
i ii j j j
,1
3() ≔ ( ) ( ( ) ) ( ) å á- - ñ
=
Thus, the interactions are described by the so-calledinteraction matrix which is a linear application
K : NN33  acting on the heat bath degrees of freedom. Note that eachKij is a three dimensional matrix since
also the spatial degrees of freedom are included.
The meaning of the interaction described byHINT is to assume a harmonic approximation around the
equilibrium positions Q* ≔ a(X) of the heat bath system, wherea: N33 provides the equilibrium
conﬁguration of all the heat bath particles for a givenX 3Î .
The system of Hamilton’s equations, then, reads:




X P
Pa X K Q a X X
QI
IK Q a X
t t
M
tt t t V t
tt
tt t
,
,
,
,2 2
XXt T t
() ()
( ) ( ( )) ( ( ) ( ( ))) ( ( ))
() ()
() ( () ( () ) ) ( )
() ()
=
= - -
=
=- -
where a:X t N33 3()  ´ and the superscriptT denotes the transpose operation.
The system of equations above can be reduced to a GLE for the system position vectorX(t). To do so, oneﬁrst
focuses on the heat bath equations(the last two equations) and, by just having a linear dependence on theQ-
coordinates, one interprets the factorKa(X) as an external force. Hence, one exploits the Laplace transform
method to obtain a formal solutionQS(t) for the heat bath position vector. Actually, the Hamiltonian(21)
presents a translational invariance since it only depends onQ − a(X). This feature reﬂects on the formal heat
bath solution and, as we will see later, we obtain an explicit mathematical expression of the heat bath solution
directly in terms ofQ
S(t) − a(X(t)). Then, the solution can be plugged into the equation of motion of the heavy
particle and the resulting equation explicitly takes the form of a GLE.
We will explicitly employ such a procedure in the next section after having studied more deeply the
properties of the equilibrium mapa(X) which plays a fundamental role in the deﬁnition of the kernel matrix and
noise vector.
We conclude this section, mentioning that the procedure above described, called elimination of the heat
bath degrees of freedom, has been already introduced by Kacet al [30] ﬁrst and by Zwanzig[31] later. However,
Kac et al just considered linear system-heat bath interactions that, in our notation, translates in deﬁning the a
map to beai(X) ≔ X and absorbing all the parameters representing the interaction strength within theK matrix.
Zwanzig extended their system assuming a generic dependency of thea map on the heavy particle position
vector X and since it could be nonlinear, the elimination procedure led to a nonlinear GLE.
