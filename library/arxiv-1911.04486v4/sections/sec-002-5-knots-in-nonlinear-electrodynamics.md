---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-002-5-knots-in-nonlinear-electrodynamics
section_title: "Knots in nonlinear electrodynamics"
section_number: 5
pages: 19-26
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜ nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
---
A very important application of Bateman method to non-linear electrody-
namical models that generalize Maxwell’s electrodynamics in the strong ﬁeld
regime, was given recently in [22, 23]. In these works, the authors showed
that there are knot solutions of the equations of motion in any non-linear ex-
tension of Maxwell’s electrodynamics that satisﬁes strong ﬁeld requirement.
Let us see how the Bateman method can be applied to the Born-Infeld
electrodynamics. The non-linear Born-Infeld action has the following form
SBI =−γ2
∫
d4x
(√
1 +F−P 2− 1
)
, (122)
18
where γ is a constant of dimension 2 and L and P are the usual Lorentz
invariants deﬁned as follows
L =γ−2δmn (BmBn−EmEn) , (123)
P =γ−2δmnEmBn. (124)
The scalarsL andP are zero for all null-ﬁelds that satisfy the equations (50)
and (51).
In order to prove that the theory described by the actionSBI has Hopﬁon
solutions, the following argument has been developed in [22, 23]. Starting
from the action (122), deﬁne new vector ﬁelds H and D whose components
can be written in a notation analogous to Maxwell’s electrodynamics
Hm =−∂LBI
∂Bm , D m = ∂LBI
∂Em . (125)
Here,LBI is the Lagrangian density from the action (122). From it, one
obtains the explicit form of Hm and Dm as follows
Hm =− 1√
1 +F−P 2 (Bm−PEm) , (126)
Dm =− 1√
1 +F−P 2 (Em−PBm) . (127)
By applying the variational principle to the action (122), the following equa-
tions of motion are obtained
∂mDm = 0, (128)
∂mBm = 0, (129)
εmnr∂nEr =−∂0Bm, (130)
εmnr∂nHr =∂0Dm. (131)
The above equations show that the null ﬁelds from the relations (50) and
(51) belong to a theory in which the equations of motion are of Maxwellian
type. Therefore, by using the results presented in Section 2, one concludes
that there are null ﬁeld Hopﬁon solutions in the non-linear Born-Infeld elec-
trodynamics.
The same argument can be generalized to all non-linear actions that in
the weak ﬁeld limit can be reduced to Maxwell’s electrodynamics. Another
interesting generalization is based on the observation that the equations of
the classicall electrodynamics are similar to the equations of the ﬂuid me-
chanics. Then by using the same reasoning as before, Hopﬁon solutions of
the ﬂuid ﬂow lines were showed to exist in [22, 23].
19
Appendix - Hopf map
In this Appendix, we brieﬂy review the deﬁnition and some basic properties
of the Hopf map that have been used in the text. A classical reference on
this topic is the textbook [40] in which Hopf’s theory is presented from a
geometrical point of view.
Consider a n-dimensional unit sphere Sn deﬁned as follows
Sn ={ x∈Rn+1 : δijxixj = 1, i,j = 0, 1,...,n }. (132)
The Hopf ﬁbration is the mapping h : S3 → S2 ≃ CP1 deﬁned by the
following Hopf map
h(x0,x 1,x 2,x 3) =
(
x2
0 +x2
1−x2
2−x2
3, 2(x0x3 +x1x2), 2(x1x2−x0x3)
)
.
(133)
Alternatively, the Hopf map can be written in terms of the following complex
coordinates on the spheres S2 and S3
S2 ={(x,z )∈ R× C : x2 +|z|2 = 1}, (134)
S3 ={(z1,z 2)∈ C2 :|z1|2 +|z2|2 = 1}. (135)
Then the Hopf map takes the following form
h(z1,z 2) =
(
2z1¯z2,|z1|2−|z2|2)
. (136)
Since the projective space is a quotient set CP1≃ S3/U(1), the action of
U(1) on S3 deﬁnes the ﬁbres over S3. These are mapped into the ﬁbres over
S2 as follows. Consider the equivalence class of points of S3 deﬁned by the
following relation
(z′
1,z′
2)∼ (z1,z 2) : if ∃λ∈ C such that (z′
1,z′
2) = (λz1,λz 2). (137)
Then the Hopf map of (z′
1,z′
2) satisﬁes the following relation
h(z′
1,z′
2) =|λ|2h(z1,z 2). (138)
The points (z′
1,z′
2) and (z1,z 2) of S3 belong to a ﬁbre over S2 if they are
mapped onto the same point of S2. This represents a constraint on the
parameter λ which is satisﬁed by any λ of the form λ = exp(iϑ), where
ϑ∈ [0, 2π). Thus, λ necessarily belongs to the deﬁning representation of
U(1).
From the geometrical point of view, the ﬁbre of S3 is the great circle
that contains (z1,z 2). An useful parametrization of ﬁbres is given by the
following relations
z1 = exp
(
iξ + ϕ
2
)
sin
(ϑ
2
)
, z 2 = exp
(
iξ− ϕ
2
)
cos
(ϑ
2
)
. (139)
20
It is easy to see that the Hopf map h takes the points from the ﬁbres of S3
to the following points on S2⊂ R3
x1 = 2|z1||z2| cos(ϕ), (140)
x2 = 2|z1||z2| sin(ϕ), (141)
x3 =|z1|2−|z2|2. (142)
The stereographic projections can be easily determined from its deﬁnition
and we ﬁnd that there are several parametrizations of these projections. For
example:
π2(x1,x 2,x 3) =
( x1
1−x3
, x2
1−x3
)
, (143)
π3(x0,x 1,x 2,x 3) =
( x1
1−x0
, x2
1−x0
, x3
1−x0
)
. (144)
The Hopf map inverse γ =h−1 takes points (x,z ) from S2 into loops on S3.
In general, if the points are diﬀerent (x,z )⁄= (x′,z′), so are the corresponding
loops γ⁄=γ′. However, there is an object associated to a pair of loops called
the Hopf invariant of h that is the linking number of the pair of loops, also
called the Hopf index of (γ,γ′), and which has the following general form
H(h) =l(γ,γ′). (145)
H(h) is an homotopy invariant that characterizes the Hopf map. It is useful
to write the Hopf invariant in terms of the Chern-Simons integral [45] of
some vector ﬁelds. This can be done as follows. Consider an unit vector ﬁeld
U(x) with the following properties
δijUi(x)Uj(x) = 1, |U(x)|→ u if|x|→∞ , (146)
where u is a constant unit vector. Then deﬁne the vector ﬁeld F(x) with the
following components
Fj(x) =εjmnεprsUp(x)∂mUr(x)∂nUs(x). (147)
The ﬁeld F(x) can be written in terms of a potential vector ﬁeld A(x) as
follows
Fj(x) =εjmn∂mAn(x). (148)
Then the Hopf index of the ﬁeld U(x) is given by the following equalities
H(U) =
∫
d3xδijFi(x)Aj(x) =
∫
d3xεjmnAj(x)∂mAn(x). (149)
We recognize in the last equality above the explicit form of the Chern-Simons
integral for the potential A(x).
21
References
[1] Trautman, A. (1977). “Solutions of the Maxwell and Yang-Mills
Equations Associated with Hopf Fibrings,” Int. J. Theor. Phys. 16,
561.
[2] Ra˜ nada, A. F. (1989). “A Topological Theory of the Electromag-
netic Field,” Lett. Math. Phys. 18, 97.
[3] Ra˜ nada, A. F. (1990). “Knotted solutions of the Maxwell equations
in vacuum,” J. Phys. A 23 L815.
[4] Ra˜ nada, A. F. (1992). “Topological electromagnetism,”J. Phys. A
25, 1621.
[5] Ra˜ nada, A. F. and Trueba, J. L. (1995). “Electromagnetic Knots,”
Phys. Lett. A 202, 337-342.
[6] Ra˜ nada, A. F. and Trueba, J. L. (1997). “Two properties of elec-
tromagnetic knots,” Phys. Lett. A 222, 25-33.
[7] Irvine, W. T. M. and Bouwmeester, D. (2008). “Linked and knotted
beams of light,” Nature Physics 4, 716 - 720.
[8] Irvine, W. T. M. (2010). “Linked and knotted beams of light, con-
servation of helicity and the ﬂow of null electromagnetic ﬁelds,” J.
Phys. A: Math. Theor. 43 385203.
[9] Array´ as, M. and Trueba, J. L. (2010). “Motion of charged particles
in a knotted electromagnetic ﬁeld,” J. Phys. A 43, 235401.
[10] Kleckner, D. and Irvine, W. T. M. (2013). “Creation and dynamics
of knotted vortices,” Nature Physics 9, 253-258.
[11] Array´ as, M. and Trueba, J. L. (2012). “Exchange of helicity in a
knotted electromagnetic ﬁeld,” Annalen Phys. 524, 71.
[12] Array´ as, M. and Trueba, J. L. (2017). “Collision of two hopﬁons,”
J. Phys. A 50, 085203.
[13] Ra˜ nada, A. F., Tiemblo, A. and Trueba, J. L. (2017). “Time evolv-
ing potentials for electromagnetic knots,” Int. J. Geom. Meth. Mod.
Phys. 14, 1750073.
[14] Ra˜ nada, A. F. and Trueba, J. L. (1998). “A Topological mechanism
of discretization for the electric charge,” Phys. Lett. B 422, 196.
22
[15] Ra˜ nada, A. F. (2003). “Interplay of topology and quantization:
topological energy quantization in a cavity,” Phys. Lett. A 310,
434-444.
[16] Ra˜ nada, A. F. and Trueba, J. L. (2006). “Topological quantization
of the magnetic ﬂux,” Found. Phys. 36, 427.
[17] Array´ as, M., Trueba, J. L. and Ra˜ nada, A. F. (2012). “Topological
Electromagnetism: Knots and Quantization Rules,” in Trends in
Electromagnetism - From Fundamentals to Applications , Barsan,
V. and Lungu, R. P. (Eds.), IntechOpen Ltd.
[18] Array´ as, M. and Trueba, J. L. (2011). “Electromagnetic Torus
Knots,” J. Phys. A: Math. Theor. 48, 025203.
[19] Kedia, H., Bialynicki-Birula, I., Peralta-Salas, D. and Irvine, W.
T. M. (2013). “Tying knots in light ﬁelds,” Phys. Rev. Lett. 111,
150404.
[20] Hoyos, C., Sircar, N. and Sonnenschein, J. (2015). “New knotted
solutions of Maxwell’s equations,” J. Phys. A 48, no. 25, 255204.
[21] Goulart, ´E. (2016). “Nonlinear electrodynamics is skilled with
knots,” Europhys. Lett. 115, 10004.
[22] Alves, D. W.F., Hoyos, C., Nastase, H. and Sonnenschein, J. (2017).
“Knotted solutions for linear and nonlinear theories: electromag-
netism and ﬂuid dynamics,” Phys. Lett. B 773, 412.
[23] Alves, D. W. F., Hoyos, C., Nastase, H. and Sonnenschein, J.
(2017). “Knotted solutions, from electromagnetism to ﬂuid dynam-
ics,” Int. J. Mod. Phys. A 32, 1750200.
[24] Ra˜ nada, A. F. and Trueba, J. L. (1996). “Ball lightning an electro-
magnetic knot,” Nature 383, 32.
[25] Irvine, W. T. M. and Kleckner, D. (2014). “Liquid crystals: Tangled
loops and knots,” Nature Materials 13, 229231.
[26] Smiet, C. B., Candelaresi, S., Thompson, A., Swearngin, J., Dal-
huisen, J. W. and Bouwmeester, D. (2015). “Self-Organizing Knot-
ted Magnetic Structures in Plasma,” Phys. Rev. Lett. 115, 095001.
23
[27] Ji-Rong, R., Tao, Z. and Shu-Fan, M. (2008). J. R. Ren, T. Zhu
and S. F. Mo, “Knotted topological phase singularities of electro-
magnetic ﬁeld,” Commun. Theor. Phys. 50, 1071.
[28] de Klerk, A. J. J. M., van der Veen, R. I., Dalhuisen, J. W. and
Bouwmeester, D. (2017). “Knotted optical vortices in exact solu-
tions to Maxwell’s equations,” Phys. Rev. A 95, 053820.
[29] Trueba, J. L. (2008). “Electromagnetic knots and the magnetic ﬂux
in superconductors,” Ann. Fond. Louis de Broglie 33, 183-192.
[30] Array´ as, M., Bouwmeester, D. and Trueba, J. L. (2017). “Knots in
electromagnetism,” Phys. Rept. 667.
[31] Kopi´ nski, J. and Nat´ ario, J. (2017). “On a remarkable electromag-
netic ﬁeld in the Einstein Universe,” Gen. Rel. Grav. 49, 81.
[32] Vancea, I. V. (2017). “On the existence of the ﬁeld line solutions of
the Einstein - Maxwell equations,” Int. J. Geom. Meth. Mod. Phys.
15, 1850054.
[33] Costa e Silva, W., Goulart, E. and Ottoni, J. E. (2018). “On
spacetime foliations and electromagnetic knots,” arXiv:1809.09259
[math-ph].
[34] Alves, D. W. F. and Nastase, H. (2018). “Hopﬁon solutions in grav-
ity and a null ﬂuid/gravity conjecture,” arXiv:1812.08630 [hep-th].
[35] O. Lechtenfeld and G. Zhilin, “A new construction of ratio-
nal electromagnetic knots,” Phys. Lett. A 382, 1528 (2018).
doi:10.1016/j.physleta.2018.04.027
[36] O. Lechtenfeld and K. Kumar, “On rational electromagnetic ﬁelds,”
arXiv:2002.01005 [hep-th].
[37] I. V. Vancea, “Field Line Solutions of the Einstein-Maxwell Equa-
tions,” in An Essential Guide to Maxwell’s Equations , Ed. Casey
Erickson, Nova Science Publishers.
[38] Jackson, J. D. (1962). “Classical Electrodynamics,” John Wiley and
Sons.
[39] Frankel, T. (1997). “The geometry of physics: An introduction,”
Cambridge University Press.
24
[40] Milnor, J. (1997). “Topology from the Diﬀerentiable Viewpoint,”
Princeton University Press.
[41] Bateman, H. (2016). “The Mathematical Analysis of Electrical and
Optical Wave-Motion,” Cambridge University Press.
[42] Thompson, A., Wickes, A., Swearngin, J. and Bouwmeester, D.
(2015). “Classiﬁcation of Electromagnetic and Gravitational Hop-
ﬁons by Algebraic Type,” J. Phys. A 48, 205202.
[43] Kedia, H., Foster, D., Dennis, M. R. and Irvine, W. T. M. (2016).
“Weaving knotted vector ﬁelds with tunable helicity,” Phys. Rev.
Lett. 117, 274501.
[44] Dennis, M. R., King, R. P., Jack, B., O’Holleran, K. and Padgett
, M. J. (2010). “Isolated optical vortex knots,” Nature Physics 6,
118-121.
[45] Whitehead, J. H. C. 1947. “An expression of Hop’s invariant as an
integral,” Proc. Nat. Acad. Sci. U.S.A. 33, 117123.
25
