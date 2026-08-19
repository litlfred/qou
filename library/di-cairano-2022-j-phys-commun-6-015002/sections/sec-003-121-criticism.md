---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "Langevin equation in systems with also negative temperatures"
section_id: sec-003-121-criticism
section_title: "Criticism"
section_number: 1.2.1
pages: 4-5
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "Communications PAPER • OPEN ACCESS On the derivation of a Nonlinear Generalized Langevin Equation To cite this article: Loris Di Cairano 2022 J. Phys. Commun. 6 015002 — 14 sections: Introduction; Sta"
---
We now explain our main criticism to the Zwanzig’s derivation showing that the deﬁnitions (8) and (9) provided
by Zwanzig yield a FDR which is inconsistent with the standard deﬁnition [3]. The main reason of this
inconsistency can be better explained by means of the following argument. In writing the Hamiltonian for two
interacting systems, all the information about the nature of the interaction is contained in the potential function
which gives a fully microscopic and detailed description of system. Conversely, in the(generalized) Langevin
equation, one just takes into account a coarse-grained representation of these interactions encoded into two
terms: the stochastic noise vector and the friction matrix or function. The role of the FDR is somehow to balance
the energy dissipated by the friction with that supplied by the random noise. Consequently, the friction and
noise term have to contain the information about the strength of the interactions. For example, in the easiest case
of a standard Langevin equation(LE), i.e.,
U tU t F t() () () g=- + , the second term on the right-hand side can
be interpreted as a convolution between a kernel functionζ(t − τ) ∼ γδ(t − τ)( δ is the Dirac delta distribution)
and the velocity vector of the heavy particle,U(t). In this case, it is also evident that the strength of the interaction
is represented by the friction constantγ which is a coarse-grained description of the heavy particle-environment
interactions. This feature must hold also in case of a GLE, that is, we expect that, in the Zwanzig’s derivation, all
the microscopic information contained in the potential function are condensed within the friction matrixL.
By inspection, we immediately realize thatL and F, respectively, in equation(8) and (9) do not show this
feature. In fact,(up to two constantskB and T) L depends on B and K. Now, B is a constant antisymmetric matrix
whereas K is the matrix associated to the oscillation frequencies of the heat bath particles when they do not
interact with the heavy one1.
Therefore, the FDR formulated by Zwanzig in(11) does not provide any balance.
Based on this observation, we now explicitly show that, introducing the same Hamiltonian considered by
Zwanzig, that is:[31]
H P VQ
p
qQ22 2 ,1 2
j
N jj
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
() ( ) å
wg
w
=+ + + -
=
where we recall that capital letters represent the heavy particle variables.
By comparing (12) and (3), we note that theﬁrst two terms in the Hamiltonian above correspond toHs(X)
whereas the terms in the square brackets correspond toHb(X, Y). Therefore, the Hamiltonian(12) can be
deduced from that in equation(3) making explicit in the latter the position and momentum variables, i.e.:
1 We can convince about it just observing the HamiltonianHb(X, Y) in equation (3). By switching the heat bath-heavy particles interactions
off means thata(X) = 0 for anyX ≠ 0 and this leads toHb(X, Y) = Hs(X) + Y TKY/2. This is the Hamiltonian of two non-interacting
subsystems where the latter is nothing but a set of(non-interacting) harmonic oscillators.
3
J. Phys. Commun.6 (2022) 015002 L Di Cairano
H PpQq HPQ p a PQ K p a PQ
qa P Q K qa P Q
pa P Q K qa P Q
,, , , 1
2 ,,
1
2 ,,
,, . 1 3
sp T pp p
q T qq q
p T pq q
( ) ( ) [( ) ] [( ) ]
[( ) ] [( ) ]
[ ( )] [ ( )] ( )
=+ - -
+- -
+- -
Now, by imposingKpp = 1 and ap(P, Q) = 0, Kpq = Kqp = 0 and setting K diag ,, ,qq N1
2
2
22≔{ } ww w ¼ and
a PQ a Q Q,q
i
q
i i
i
2() ( ) º=
g
w , equation (13) reduces to (12). We note that i
2{ }w is the set offree oscillation frequencies
of the heat bath particles whereas i i
N
1{ }g = is the set of coupling coefﬁcients which determine the strength of the
heat bath-heavy particle interactions. Thus, a speciﬁc interaction can be switched off just imposingγi → 0 which
implies a Q 0q
i () = .
By specializing deﬁnitions (8) and (9) to this example, a cumbersome but straightforward calculation leads to
the noise term
Ft K K t K K tpcos sin , 14qq q qq qq qq
12 12 12() ( ) ( ) ( )=- +
whereas for the kernel matrix, we have
Lt K K t cos . 15qq qq qq
12() ( ) ( )=
As already stressed, the friction matrix(15) does not depend on the coupling coefﬁcients, γi and, thereby, the
FDR is ill-deﬁned as we will see in a moment. In fact, by plugging equations(14) and (15) into the deﬁnition (11)
for the FDR, one gets:
F t F kT T rK K t kT T rL t kT tcos cos . 16qq B q q qq Bq q B
i
N
i i
12
1
2( ) · ( ) [ ( ( ))] [ ( )] ( ( )) ( ) ått t w w táñ = - º - = -
=
It is evident that the friction function on the last right-hand side, that is:
tt cos , 17
i
N
i i
1
2() ≔ ( () ) ( )åxt ww t--
=
just depends on the oscillation frequencies i i
N
1{ }w = , therefore, the obtained FDR(16) does not recover the usual
deﬁnition.
Finally, we stress that, adopting the same example, Zwanzig writes a different friction function(which is also
the correct one) and it reads(see equation (23) in [31]):
tt cos . 18Z
i
N
i
1
2
i
i()( ) (( ) ) () åzt w t-= -
g
w
=
This suggests that he maybe absorbed, ad hoc, theγi-coefﬁcients within ζ.
Based on that, we conclude that the deﬁnition (18) should be adjusted in order to obtain the correctζ
function without any ad hoc-adjustment and this is the principal aim of the paper.
