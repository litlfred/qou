---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "Langevin equation in systems with also negative temperatures"
section_id: sec-009-23-alternative-derivation
section_title: "Alternative derivation"
section_number: 2.3
pages: 8-11
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "Communications PAPER • OPEN ACCESS On the derivation of a Nonlinear Generalized Langevin Equation To cite this article: Loris Di Cairano 2022 J. Phys. Commun. 6 015002 — 14 sections: Introduction; Sta"
---
The system of Hamilton’s equations of motion(22) based on the Hamiltonian(33) written as a system of second
order differential equations reads:
Xa X K Q a X Xtt t t V t ,3 4XXt T ẗ ( ) ( ( )) ( ( ) ( ( ))) ( ( )) ( )() ()= - -
QK Q a Xtt t .3 5̈ () ( () ( () ) ) ( )=- -
We note that equation(35) is linear in the heat bath-variablesQ, this allows us to apply the Laplace transform
method [24– 26]. Hence, the Laplace transform of equation(35) is
Q K QQK a Xss s s 110 0 . 3 621() ( ) [ () () ( () ) ] ( )=+ + +~ ~-
7
J. Phys. Commun.6 (2022) 015002 L Di Cairano
Then, applying the inverse Laplace transform we get:
QK Q K K QK K a Xtt t t dcos 0 sin 0 sin , 37
t
12 12 12
0
12 12( ) () ( ) () ( ) ( ( ) ) ( ( ) ) ( ) ò tt t=+ + - -
where the matrix-valued function is deﬁned through the series representation:
KK K Kt n tt n tcos 1
2 ,s i n 1
21 .
n
n
nn
n
n
nn12
0
21 2
0
21() ()
() ! () ()
() !åå= - = -
+=
¥
=
¥
+
In order to recover a GLE, in the convolution on the right-hand side the time derivative of the heavy particle
variable has to appear. Therefore, we notice that the kernel matrixK K tsin12 12 (( ) )t- can be written as the
derivative of K tcos 12(( ) ) t- and an integration by parts leads to:


QK Q K K Q a X K a X
Ka X X
tt t t t
td
cos 0 sin 0 cos
cos , 38 X
t
12 12 12 12
0
12
( ) ( ) ( ) ( ) ( ) ( ( )) ( ( )) ( ( ))
( ( )) ( ( )) ( ) ( ) ()ò
t
tt t t
=+ + -
--  t
-
where  a Xa X X X(( ) ) (( ) )( ) ()tt t= t .
Now, we note that the heat bath variable enter equation(34) under a speciﬁc combination, i.e.,K[Q(t) −
a(X(t))], but this relation can be obtained in equation(38) that is:
 KQ aX Q Q aX aX Xtt G tH t S t d 00 0 ,
39
KK K X
t
0
[ ( ) ( ( ))] ( ) ( ) ( )( ( ) ( ( ))) [ ( ) ( ( ))] ( )
()
()ò tt t t-= + ---  t
KK K KKHt t Gt t St t cos , sin , cos , 40KK K 12 12 12()≔ ( ) ()≔ ( ) ()≔ ( () ) ( )
Finally, we introduce a further canonical basis eI I
n
1{ } = of n whichallowsustode ﬁne, respectively, the parameter
matrix and the equilibrium map vector:
ee g X X e f,, 4 1
i
N
J
n
iJ iJ
I
n
I I
11
,
1
≔( ) ≔ ( ) ( )åå åhL Ä
== =
such that
aX gX .4 2XX () () ( )L= 
Hence, we plug equation(39) into equation (34) and we obtain:

Xg X I Q a X
gX g X X X
Mt t G t H t
tS t d V t
00 0
.4 3
XK K
XK X X
t TT
t
t TT t
0
̈ ( ) ( ( )) ( ( ) ( ) ( )[ ( ) ( ( ))])
(( ) ) ( ( )) (( ) )( ) (( ) ) ( )
()
() ( ) ()ò tt t t
L
LL
= + -
- -  -  t
In order to recover the common structure of a GLE, we note that the mathematical structure of the equation
obtained above allows to deﬁne the kernel matrix and the noise term as follows:
L
FI Q a X
tS t
tG t H t
,
00 0 , 4 4
K
KK
T
T
() ≔ ()
( ) ≔ ( ( ) ( ) ( )[ ( ) ( ( ))]) ( )
tt LL
L
--
+-
We wish to stress a signiﬁcant difference between the current deﬁnitions of noise vector and kernel matrix in
equation (44) and the previous ones in equation(8) and (9). In the latter, the noise and kernel terms do not
contain any information about the strength of the interactions represented by the coefﬁcients γi,I and all the
parameters γi,I are contained in the equilibrium map. In the former case, the parametersηi,I have been
completely absorbed into the noise term and kernel matrix.
Therefore, we can recast equation(43) into a nonlinear GLE:
Xg X F g X L g X X XMt t t t t d V t .4 5XX X Xt T
t
t T t
0
̈ ( ) (( ) )( ) (( ) )( ) (( ) )( ) (( ) ) ( )() () ( ) () ò tt t t= -  -  - t
An important step forward in the investigation of stochastic behaviors arising from interacting Hamiltonian
systems would be made if we could solve equation(45) which is a nonlinear stochastic differential equation.
Two different approaches could be employed. From one side, one can attempt a semi-analytical approach
exploiting the same method introduced in[34]. The authors showed that, even though we have a nonlinear
differential equation, but we explicit know the time-dependence of the functions entering the equation2, we can
still apply the Laplace transform method to equation(45). However, this approach cannot always provide an
exact solution but a series representation of the solution is possible. So far, this approach has been applied just
for investigating nonlinear differential equations which are not stochastic but it could be extended to address
stochastic differential equation. A more detailed study will be done in a future paper.
2 In our case, this translates in choosing a speciﬁc potential function so that the equilibrium map is well-deﬁned.
8
J. Phys. Commun.6 (2022) 015002 L Di Cairano
Another possible approach is the numerical one. In particular, under suitable condition on the kernel
matrix, L(t − τ), a GLE can be converted into a stochastic Volterra equation where several numerical integration
schemes have been developed such as the Euler and Milstein scheme[35].
We now show that adopting deﬁnitions (44), one naturally recover the FDR.
Hence, let us consider the heat bath Hamiltonian from equation(33), namely:

IQ
I
Qa X K Qa XH , 2
1
2 ,. 4 6
2
N
N
3
3() ( ) ( ( ) ) ( )
=+ á - - ñP
The canonical probability density is given by:
XQ I Z ee00 , 0 1 ,4 7I I Qa X K Qa X,0 0 , 0 0NN2 3 2 3( () ∣ () () ) ≔ · ( ) ( ) ( ( )) ( ( ) ( ( )))r -á ñ -á - - ñbb
where Z is the canonical partition function
QIZe d d 00 , 4 8IQX0, 0, 0≔( ) ( ) ( )[ (() () () ) ]
ò
b- HB
and where β−1 = kBT.
Let us note that, sinceX is held ﬁxed, we can introduce the following substitution:
xQa X00 0 , 4 9() ≔ () ( () ) ( )-
which does not affect the integration measure, i.e.dx(0) = dQ(0), thereby, the canonical partition and density
functions read:
Xx I
xI
Z e
Ze d d
00 , 0 1 ,
00 , 5 0
II x K x
II x K x
,0 , 0
,0 , 0
NN
NN
2 33
2 33
( () ∣ () () ) ≔
≔( ) ( ) ( )
(( ) ( ) )
(( ) ( ) )


ò
r -á ñ - á ñ
-á ñ - á ñ
b
b
and the integration measure assumes manifestly a Gaussian form.
By exploiting equation(49), the noise vector in equation(44) becomes:
FI xtG t H t 00 , 5 1KKT()≔ ( () () () () ) ( )L +
and the computation of the second order correlation functions can be done easily[30]:
Ix I I x x K xI00, 11 ,, . 5 2
1N3
()
bbá ñ= á ñ= áÄñ= á Ä ñ= á Äñ=rr r r r
-
Furthermore, we notice that the noise,F, is a mean-zero vector, namely:〈F(t)〉ρ = 0. In order to explicitly write
the ﬂuctuation-dissipation relation (noise autocorrelation function),w e ﬁrst expand the tensor product, i.e.:
FF I x I x
II xx
xI Ix
tG t H t G H
Gt G Ht H
Ht G Gt H
00 0 0
00 00
00 00 . 5 3
KK KK
K K K K
K K K K
T TT
T TT
TT
( ) ( ) ( ( ) ( ) ( ) ( )) ( ( ) ( ) ( ) ( ))
(( ) ( ) ( )( ) ( ) ( ) ( )( )
() () () () () () () () ( )
tt t
tt
tt
LL
L
L
Ä= + Ä +
=Ä + Ä
+Ä +Ä
Thus, by exploiting equation(52), the average of the tensor product above becomes:
FF K Ktt cos , 54T11 2() ( ) ( ( ) ) ( )tb t LLáÄ ñ = - r -
where we used equation(40) and knowing that K tcos 12() and K tsin 12() commute with any polynomial ofK.
We obtained in equation(54), the ﬂuctuation-dissipation relation; in fact, by comparing the operator on the
right-hand side above with equation(44), we explicitly have:
FF Ltt .5 51() ( ) ( ) ( )tb táÄ ñ = - r -
As proof of consistence and show-case example, let usﬁnally apply such a derivation to the Hamiltonian
system in equation(12) proposed by Zwanzig. Thus, the equilibrium map is given by
a XX iN,1 , ,i
Hi
i
2() ≔ [ ] h
w
"Î
whereas the interaction matrixK is
Ke e ,5 6
i
N
i ii
1
2≔( )å w Ä
=
In this setting, it consists in imposingf1(X) ≔ X with ii i i,1
2h hh wº= and ηi,I = 0 for anyI ä [2, n]. This
implies that the matrixΛ in equation (41) reduces to
9
J. Phys. Commun.6 (2022) 015002 L Di Cairano
ee ,
i
N
i
i
i
1
2 1≔ å
h
w
L Ä
=
whereas
eeSt t sin . 57K
i
N
i ii i
1
2( ) (( ) ) () åtw w t-= - Ä
=
Therefore, the kernel matrix reduces
Le ett cos , 58
i
N
i
i
ii i
1
2
2() ≔ ( () ) ( )åt h
w
wt-- Ä
=
whose trace coincides with theζZ function (15) in the Zwanzig’s result [31]. However, now, the continuum limit
can be computed. We conclude this section discussing the importance of including all the parameters
representing the interactions(in this caseη
i) directly in the deﬁnitions of the kernel matrix and noise terms In
particular, this can be appreciated as soon as one computes the continuum limit of the friction matrix, which
consists in assuming that the set of heat bath frequencies di i
N
1≔{ }w =S becomes a continuum set ÌS
together with a distribution functiong(ω) of frequencies which depends on the speciﬁc interactions we
considered.
In this limit, one replaces the sum over the frequencies with an integral[31]:
gd ,
i
N
i
1
⟶( ) ( )òå hh w w w
= S
where i i
N
1{ }h = is any set of coefﬁcients and η(ω) is the associated frequency-dependent function in the continuum
limit.
Now, if the kernel function is deﬁned as in equation(17), i.e., without including the parametersγi, the
continuum limit, which reads:
tt g d cos ,2() ⟶ ( () ) ( )òx tw w t w w--
S
cannot provide a bounded continuous kernel function.
Conversely, including the coefﬁcients γi in the kernel as in(18), one assumes that the set i i
N
1{ }g = becomes a
continuous function γ(ω) of the frequency variable, so that the continuum limit can be applied
t t gdcos ,5 92
2() ⟶ (( ) ) ()() ( )òzt wt
w gw ww- -
S
choosing γ such that it remains bounded asω → ∞.
The degree of freedom represented by theγ function can beﬁxed for requiring the boundedness of the kernel
function. In practice, the remaining effort consists in providing the correct modeling, depending on the
interaction nature, of the functionJ(ω) ≔ γ
2(ω)g(ω) even called density function. with the existing techniques
already introduced in the literature[19].
