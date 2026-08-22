---
doc_id: di-cairano-2022-j-phys-commun-6-015002
doc_title: "On the derivation of a nonlinear generalized Langevin equation"
section_id: sec-007-211-examples-of-a-possible-equilibrium-map
section_title: "Examples of a possible equilibrium map."
section_number: 2.1.1
pages: 7-8
source_pdf: Di_Cairano_2022_J._Phys._Commun._6_015002.pdf
source_sha256: f75313b507f97172
doc_brief: "On the derivation of a nonlinear generalized Langevin equation — 14 sections: Introduction; State-of-art; Introduction to the problem"
---
Let us consider a Lennard-Jones-like interaction potential of the form
 QX Xq Xq,4 , 2 5LJ
i
N
i
i
i i
i
i i1
12 6
⎜⎟ ⎜⎟
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
⎥() ≔ ( ) å h ss
- - -= V
where the parameters ,i i s h Î have the dimension of an energy and a length, respectively; lastly, i Î are
dimensionless parameters. Note that we do not consider any mutual interaction between the heat bath particles.
The requirement (23), namely:
*QX 0,,q LJi ()=V
where * **Qq q ,, N1{}= is the equilibrium conﬁguration of the heat bath, yields
 *Xq iN2, 1 , .i i i
21 3 2 []s-= " Î
This set of relations can be geometrically interpreted imaging that any particle, let us say, thei-th one, lies on a
point of the sphere R
2
i with radius Ri = 21/6σi. The reason why any point on the sphere is equivalent to each
other is due to the fact we do not have any mutual interaction between the heat bath particles.
Therefore, every equilibrium position vector *qi can be related to the heavy particle vectorX, introducing
any unit vectorn(X)(  nX 13()  = ) such that
*q X nX iN2 ,1 , .i
i
i
i
16
≔( ) [ ] s+" Î
In general, it could depend onX, for example, such asn(X) = X/∥X∥. Thus, the equilibrium map may read:
/
aX X nX iN2 ,1 , . 2 6i
i
i
i
16
() ≔ () [ ] ( ) s+" Î
In so doing, theﬁrst and second term in harmonic expansion(24) read
aX X
Ka X XHess
,,
, 23 6 11, 2 7
JL
i
N
i
ii LJ ii
i i
i
1
23 2
2
3⎜⎟
⎛
⎝
⎞
⎠
(() )
≔[ ] ( ( ) ) ( ) 
å h
h
s
=-
=
=

V
V
6
J. Phys. Commun.6 (2022) 015002 L Di Cairano
so that aX X,JL(( ) )V can be dropped since constant and the potential function ca be approximated as follows
Q X qa X K qa X, 1
2 ,. 2 8JL
ij
N
i ii j j j
,1
3() ( ) ( ( ) ) ( ) å»á - - ñ
=
V
Note that the factor in theKii matrix of equation(27) has the physical dimension of a frequency, therefore, we
deﬁne a new set of frequencies
iN23 6 ,1 , , 2 9i
i i
i
2
23 2
2≔[ ] ( )w h
s
"Î
which allows us to rewrite the initial set of parameters(ηi, òi, σi) in terms of a new one:(ωi, ηi, òi); in particular, the
equilibrium map ai in equation (26) now reads:
aX X nX iN12 , 1, . 30i
i
i
i
() ≔ () [ ] ( ) h
w+" Î
We note that if X Î then we haven(X) = X/|X| and this implies thatn Xs g n X() () = . Therefore, during the
system dynamics, that is, along the equation of motion, the functionX = X(t) gives rise to a discontinuous
equilibrium map since n Xs g n X t() (( ) )= can change sign discontinuously in time passing from+1t o −1 and
viceversa. Hence, the application to a one-dimensional case requires that the potential function is not of the
form V = V(|X − ò
iqi|).
By going back to the three-dimensional case, we observe that the interaction matrixK does not depend on
the parameters ηi and òi describing the interactions.
We will show that, in order to coherently deﬁne a continuum limit of the kernel function appearing in a GLE
obtained through the elimination procedure, we have tonormalize the equilibrium map as we show in the
upcoming section.
