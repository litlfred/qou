---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a Nonlinear Generalized Langevin Equation"
section_id: sec-003-121-criticism
section_title: "Criticism"
section_number: 1.2.1
pages: 4-5
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
toc_source: outline
doc_brief: "On the derivation of a Nonlinear Generalized Langevin Equation — 15 sections: Front matter; Introduction; State-of-art"
---
We now explain our main criticism to the Zwanzig’s derivation showing that the deﬁnitions (8) and (9) provided
by Zwanzig yield a FDR which is inconsistent with the standard deﬁnition [3]. The main reason of this
inconsistency can be better explained by means of the following argument. In writing the Hamiltonian for two
interacting systems, all the information about the nature of the interaction is contained in the potential function
which gives a fully microscopic and detailed description of system. Conversely, in the (generalized) Langevin
equation, one just takes into account a coarse-grained representation of these interactions encoded into two
terms: the stochastic noise vector and the friction matrix or function. The role of the FDR is somehow to balance
the energy dissipated by the friction with that supplied by the random noise. Consequently, the friction and
noise term have to contain the information about the strength of the interactions. For example, in the easiest case
of a standard Langevin equation (LE), i.e., U t
U t
F t
( )
( )
( )
g
= -
+
, the second term on the right-hand side can
be interpreted as a convolution between a kernel function ζ(t −τ) ∼γδ(t −τ) (δ is the Dirac delta distribution)
and the velocity vector of the heavy particle, U(t). In this case, it is also evident that the strength of the interaction
is represented by the friction constant γ which is a coarse-grained description of the heavy particle-environment
interactions. This feature must hold also in case of a GLE, that is, we expect that, in the Zwanzig’s derivation, all
the microscopic information contained in the potential function are condensed within the friction matrix L.
By inspection, we immediately realize that L and F, respectively, in equation (8) and (9) do not show this
feature. In fact, (up to two constants kB and T) L depends on B and K. Now, B is a constant antisymmetric matrix
whereas K is the matrix associated to the oscillation frequencies of the heat bath particles when they do not
interact with the heavy one1.
Therefore, the FDR formulated by Zwanzig in (11) does not provide any balance.
Based on this observation, we now explicitly show that, introducing the same Hamiltonian considered by
Zwanzig, that is: [31]
H
P
V Q
p
q
Q
2
2
2
,
12
j
N
j
j
j
j
j
2
1
2
2
2
⎡
⎣
⎢
⎢
⎛
⎝
⎜
⎞
⎠
⎟
⎤
⎦
⎥
⎥
( )
(
)
å
w
g
w
=
+
+
+
-
=
where we recall that capital letters represent the heavy particle variables.
By comparing (12) and (3), we note that the ﬁrst two terms in the Hamiltonian above correspond to Hs(X)
whereas the terms in the square brackets correspond to Hb(X, Y). Therefore, the Hamiltonian (12) can be
deduced from that in equation (3) making explicit in the latter the position and momentum variables, i.e.:
1 We can convince about it just observing the Hamiltonian Hb(X, Y) in equation (3). By switching the heat bath-heavy particles interactions
off means that a(X) = 0 for any X ≠0 and this leads to Hb(X, Y) = Hs(X) + Y TKY/2. This is the Hamiltonian of two non-interacting
subsystems where the latter is nothing but a set of (non-interacting) harmonic oscillators.
IOP Publishing

J. Phys. Commun. 6 (2022) 015002 LDiCairano

1
HOP, p, Q 4) = H(P, Q) + 3p — ap(P, Q)I" Kpplp — ap(P, Q)I

+ sla = ag(P, QF Kaglq = ag(P, QI

+ [p — ap(P, QI Kgl — aq(P, Q)1.- (13)

Now, by imposing Kp, = 1 and a,(P, Q) = 0, Kpq = Kap = 0 and setting Ky, = diag {wj, w5y...,wy} and
aj (P, Q) = a;,(Q) = 22, equation (13) reduces to (12). We note that {w?} is the set of free oscillation frequencies
of the heat bath particles whereas {7}. is the set of coupling coefficients which determine the strength of the
heat bath-heavy particle interactions. Thus, a specific interaction can be switched off just imposing 7; > 0 which
implies a, (Q) =0.

By specializing definitions (8) and (9) to this example, a cumbersome but straightforward calculation leads to
the noise term

F,(t) = —Kyq cos(Kj/? t) + Ki/? sin(Kj/? 0) p, (14)

whereas for the kernel matrix, we have

Lag(t) = Kyg cos(Kj/? 1). (15)
As already stressed, the friction matrix (15) does not depend on the coupling coefficients, 7; and, thereby, the
FDR is ill-defined as we will see in a moment. In fact, by plugging equations (14) and (15) into the definition (11)
for the FDR, one gets:

N
(E(t) - F,(r)) = keT Tr[Kqq cos(Ky,? (t — 7))] = keT Tr[Lgg(t — 7)] = ke TDS w? cos(wi(t — 7). (16)
i=1

It is evident that the friction function on the last right-hand side, that is:
N
E(t — 7) = Dw} cos(wj(t — 7)), (17)
i=1
just depends on the oscillation frequencies {w;} ,, therefore, the obtained FDR (16) does not recover the usual
definition.
Finally, we stress that, adopting the same example, Zwanzig writes a different friction function (which is also
the correct one) and it reads (see equation (23) in [31]):
N

2
6, (t— 1) = >(%) cos(w;(t — 7)). (18)
i=1°
This suggests that he maybe absorbed, ad hoc, the 7;-coefficients within ¢.
Based on that, we conclude that the definition (18) should be adjusted in order to obtain the correct ¢
function without any ad hoc-adjustment and this is the principal aim of the paper.
