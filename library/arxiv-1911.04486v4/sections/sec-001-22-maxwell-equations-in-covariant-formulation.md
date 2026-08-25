---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-001-22-maxwell-equations-in-covariant-formulation
section_title: "Maxwell equations in covariant formulation"
section_number: 2.2
pages: 7-19
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜ nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
---
The geometric properties of the electromagnetic ﬁeld are highlighted in the
formulation of Maxwell’s equations in terms of diﬀerential forms onR3. How-
ever, the fundamental symmetry of Maxwell’s equations, which is the invari-
ance under the Lorentz transformations, is explicitly displayed only in the
Minkowski space-time R1,3. Therefore, it is important to write the Maxwell
equations in terms of diﬀerential forms onR1,3. To this end, the canonical ba-
sis{dxi} on R3 must be extended to the corresponding basis on R1,3, denoted
by{dxµ} ={dx0 =dt,dxi}, by including the time-like 1-form dx0. Here, we
are using the indices µ,ν = 0, 1, 2, 3 to denote the geometrical objects and
their components in the Minkowski space-time. The electromagnetic 2-form
ﬁeld F is deﬁned by the following relation
F =B +E∧dx0. (26)
In this notation, the components of F in the basis{dxµ∧dxν} are the same
as the components of the electromagnetic rank-2 antisymmetric tensor Fµν,
namely
F = 1
2Fµνdxµ∧dxν. (27)
The source of the electromagnetic ﬁeld can also be written in terms of diﬀer-
ential forms in four dimensions and it is expressed by the 1-form J =Jµdxµ
whose components are equal to the projections of the four-currentJµ = (ρ, J)
onto the space-time directions. By using these mathematical objects, one can
write down the Maxwell equations in their most compact form as follows
dF = 0, (28)
⋆d⋆F =J. (29)
6
It is easy to show that the homogeneous equation (28) corresponds to the
magnetic Gauss law and to the Faraday law combined into one equation,
while the inhomogeneous equation (29) is the same as the electric Gauss law
and the Maxwell-Amp´ ere law packed in to a single mathematical relation.
The equations (28) and (29) ﬁx to some extent the geometrical properties
of the electromagnetic 2-form. Indeed, from the geometrical point of view,
the ﬁeld F is a closed 2-form due to the equation (28). From this property
and from the nilpotency of the exterior derivative, i. e. d2 = 0, we can derive
the action of the diﬀerential form on the electromagnetic ﬁeld which is given
by the following equation
dF =dB +dE∧dx0. (30)
Recall that the exterior derivative on R1,3 can be decomposed in to two
terms: the exterior derivative d on the spatial subspace R3∈ R1,3 and the
1-form dx0 along the time-like direction R. This decomposition is given by
the following equation
d =dx0∧∂0 + d. (31)
By plugging the equations (31) and (30) into the equation (28), one obtains
the following set of equations
dE +∂0B = 0, (32)
dB = 0. (33)
The equations (32) and (33) are the homogeneous Maxwell equations written
in terms of 1-forms on the Euclidean space R3.
The three-dimensional inhomogeneous equations can be derived from the
four-dimensional system, too. The outline of the derivation is the following.
Firstly, note that the electromagnetic Hodge dual form ⋆F can be obtained
from F by making the following replacements
Ej→−Bj, B j→Ej. (34)
Secondly, decompose the form ⋆F as follows
⋆F = ⋆E− ⋆B∧dx0, (35)
where ⋆ denotes the three-dimensional Hodge star operator. Thirdly, calcu-
late the sequence of operations from the equation (29). Then one obtains the
following set of inhomogeneous equations
⋆ d ⋆E =ρ, (36)
7
⋆ d ⋆B−∂0E =J . (37)
This concludes the derivation of the three-dimensional Maxwell equations in
terms of diﬀerential forms from the four dimensional formulation.
Let us make some observations about the electromagnetic ﬁelds away
from their sources. In this case, the ﬁelds propagate in the vacuum. Their
dynamics is still given by the equations (28) and (29), but with the sup-
plementary condition J = 0. Due to this last relation, the symmetries of
Maxwell’s equations are enhanced to the group SO(1, 3)×U(1)×D , where
D denotes the electromagnetic duality symmetry deﬁned by the following
transformations
F↔⋆F . (38)
The relation (38) implies that the 2-formF can be written as a sum between a
self-dual formF+ and an anti self-dual formF−. The corresponding equations
are
F =F+ +F−, ⋆F ± =±iF±. (39)
The last of the two equations from above is the result of the self-duality
relation for 2-forms in the Minkwoski space-time: ⋆⋆ ω =−ω.
We end this section by observing that the formulation of the classical
electrodynamics in terms of diﬀerential forms is completely equivalent with
the formulation in terms of three-dimensional vector ﬁelds. However, each
framework has its own advantages. The vector approach is useful for the
visualization of the spatial distribution of ﬁelds and sources. The diﬀerential
forms are interesting because they provide more economical equations, a
deeper view of the symmetries and more information about the geometrical
and topological properties of the electromagnetic ﬁelds.
3 Knots in Maxwell’s electrodynamics
In this section, we are going to review the ﬁeld line solutions of Maxwell’s
equations and their relationship with the Hopf knots. These solutions were
discovered by Ra˜ nada and were communicated in [2, 3]. An important study
of the Hopf ﬁbration in the context of the classical electromagnetism can be
found in the early pioneering work by Trautman [1]. In our presentation, we
follow the very good indepth review of these solutions and their applications
given in the reference [30].
8
3.1 Ran˜ ada solutions
The Ran˜ ada solutions form a particular class of ﬁeld line solutions whose
main feature is that the ﬁeld lines completly characterize the electromagnetic
ﬁeld. In general, one can associate a ﬁeld line to any smooth vector ﬁeld
through its integral ﬂow. The path formed by the ﬁeld line is tangent in each
of its points to the vector obtained by taking the value of the vector ﬁeld at
that point. The picture of all ﬁeld lines at a given instant of time can be
used to visualize the state of the vector ﬁeld at that instant.
As we can see from the equations (28) and (29), the properties of the
sources determine the physical and geometrical properties of the electromag-
netic ﬁeld. In particular, the ﬁeld lines of the electromagnetic ﬁeld can have
a very complex structure for non-trivial sources and can take a simple form
in the vacuum.
In order to construct an electromagnetic ﬁeld in terms of its ﬁeld lines,
we need a formal description of the latter. That can be given in terms of two
smooth scalar complex ﬁelds on R3, namely
φ : R3→ C, θ : R3→ C. (40)
By introducing the above functions, one can interpret the electric and the
magnetic ﬁeld lines as level lines of θ and φ. In the covariant formulation,
the corresponding electromagnetic ﬁelds take the following form [30]
Fµν =g(¯φ,φ )
(
∂µ ¯φ∂νφ−∂ν ¯φ∂µφ
)
, (41)
⋆Fµν =f(¯θ,θ )
(
∂µ¯θ∂νθ−∂ν ¯θ∂µθ
)
, (42)
whereg andf are smooth functions onθ andφ, and the dual electromagnetic
ﬁeld has the following form
⋆Fµν = 1
2ϵµνρσFρσ. (43)
The components of the electromagnetic tensor Fµν contain the electric and
magnetic vector ﬁelds E and B. These can be obtained from the following
relations
F = 1
2Fµνdxµ∧dxν =−εjklBjdxk∧dxl +Ejdxj∧dx0, (44)
⋆F = 1
2 ⋆Fµνdxµ∧dxν =εjklEjdxk∧dxl +Bjdxj∧dx0. (45)
Note that the ﬁeld line solutions (41) and (42) are given in the covariant
formulation. Although they are explicitly Lorentz covariant and electromag-
netically dual to each other, it is almost impossible to visualize the geometry
9
of the electromagnetic ﬁeld from the equations (41) and (42). This problem
can be solved by invoking the equations (44) and (45) and by giving concrete
values to the arbitrary functions g and f. The ﬁrst solution with the knot
topology obtained in this way is the Ran˜ ada solution from [2, 3]. It has the
following electric and magnetic decomposition
Ej =
√a
2πi
(
1 +|θ|2)−2
εjkl∂k ¯θ∂lθ, (46)
Bj =
√a
2πi
(
1 +|φ|2)−2
εjkl∂k ¯φ∂lφ. (47)
The electromagnetic duality imposes some constraints on the ﬁelds θ and φ.
These constraints can be easily found by substituting the functions g(¯φ,φ )
and f(¯θ,θ ) from the equations (46) and (47) into the equation (38), which
leads to the following equations [30]
(
1 +|φ|2)−2
εjmn∂mφ∂n ¯φ =
(
1 +|θ|2)−2(
∂0¯θ∂jθ−∂0θ∂j ¯θ
)
, (48)
(
1 +|θ|2)−2
εjmn∂m¯θ∂nθ =
(
1 +|φ|2)−2(
∂0 ¯φ∂jφ−∂0φ∂j ¯φ
)
. (49)
The equations (48) and (49) form a set of independent non-linear partial
diﬀerential equations. The electric and magnetic ﬁeld lines are the level
curves of the solutions of the equations (48) and (49).
As one can see from the equations (46) and (47), the Ran˜ ada ﬁelds
correspond to particular functionsg andf. Recall that the null ﬁeld solutions
of Maxwell’s equations in vacuum are deﬁned by the following equations
EjBkδjk = 0, (50)
δjk
(
EjEk−BjBk)
= 0. (51)
Then it is easy to verify that Ran˜ ada ﬁelds E and B satisfy the ﬁrst null
ﬁeld equation (50), but do not satisfy the second one. From that, we can
conclude that the electric and magnetic ﬁelds are orthogonal to each other
and so are their ﬁeld lines.
The parametrization of the electromagnetic 2-forms F and ⋆F in terms
of φ and θ is not unique according to the equations (46) and (47). Other
possibility is to use the so called Clebsch parametrization. The main mathe-
matical tool to construct it is the Darboux theorem [39] that is satisﬁed by
both F and ⋆F . By using the Darboux theorem, we can write F and ⋆F in
terms of four canonical 1-forms dσa, dξa, dρa and dζa [30] as follows
F =δabdσa∧dξb, (52)
⋆F =δabdρa∧dζb, (53)
10
dσa∧dξa =dρa∧dζa =−iτ2, (54)
where the indicesa,b = 1, 2 enumerate the 1-forms andτ2 is the Pauli matrix.
The Clebsch representation of the electromagnetic ﬁeld takes a simpler form
for ﬁelds that satisfy the equation (50), namely
F =dσ∧dξ, (55)
⋆F =dρ∧dζ. (56)
Another important parametrization of the electromagnetic ﬁeld is given in
terms of Euler potentials which are smooth scalar real ﬁelds on the Minkowski
space-time [30]
αa : R3→ C, β a : R3→ C, (57)
where a = 1, 2. The electric and magnetic ﬁelds have the following form
Ej =εjkl∂kβ2∂lβ1, (58)
Bj =εjkl∂kα2∂lα1. (59)
By comparying the two sets of equations (46)-(47) and (58)-(59) with each
other, one can easily ﬁnd the following relation among the parameters of the
Ran˜ ada and Euler parametrizations, respectively,
β1 =
(
1 +|θ|2)−1
, β 2 = 1
2π arg(θ), (60)
α1 =
(
1 +|φ|2)−1
, α 2 = 1
2π arg(φ). (61)
These representations are useful to express diﬀerent properties of the ﬁeld line
solutions. Other representations can be found for more general topological
electromagnetic ﬁelds. But before discussing this case, let us take a closer
look at the Ran˜ ada ﬁelds.
3.2 Electromagnetic knot ﬁelds
As we have seen above, the electromagnetic ﬁeld characterized by the equa-
tions (41) and (42) is parametrized by g and f. In particular, by choosing
these functions as in the equations (46) and (47), the ﬁeld line solutions dis-
play non-trivial topological properties. In order to see that, we note that
φ and θ should be chosen such that the electromagnetic ﬁeld and the ob-
servables constructed from it, e. g. energy, linear momentum, and angular
momentum, be ﬁnite. Therefore, if the ﬁeld is deﬁned in the full R3, the reg-
ularity conditions to be imposed on the complex functions are the following
|φ(x)|→ 0 and|θ(x)|→ 0 if|x|→∞ . (62)
11
The boundary conditions (62) imply that the deﬁning domain of φ and θ is
the compactiﬁcation R3∪{∞} = S3 at any given value of t. Since φ and
θ take values in the compactiﬁcation C∪{∞} =S2, they can be viewed as
two families of one-parameter mapsφ(x) ={φt(x)}t∈R andθ(x) ={θt(x)}t∈R
from S3 to S2. Here, it is convenient to use the vector notation to discuss
separately the electric and the magnetic ﬁeld lines, respectively.
The ﬁelds E and B can be written in terms of electromagnetic potentials
C and A in a symmetric way
Ej =εjkl∂kCl, B j =εjkl∂kAl. (63)
Note that C is dependent on A, as they are related by the following equation
εjmn∂mCn =−∂0Aj. (64)
However, it is convenient to keepC explicit, as it makes the electric-magnetic
duality more symmetric. The Chern-Simons integrals associated to the elec-
tric and magnetic ﬁelds and their potentials can be used to deﬁne the helic-
ities of the electromagnetic ﬁeld as follows
Hee =
∫
d3xδijEiCj =
∫
d3xεjklCj∂kCl, (65)
Hmm =
∫
d3xδijBiAj =
∫
d3xεjklAj∂kAl, (66)
Hem =
∫
d3xδijBiCj =
∫
d3xεjklCj∂kAl, (67)
Hmm =
∫
d3xδijEiAj =
∫
d3xεjklAj∂kCl. (68)
The pure electric and magnetic helicites given above are the Hopf indexes
of the corresponding electric and magnetic ﬁeld lines (see the Appendix). If
one substitutes the equations (63) into Maxwell’s equations (1) - (4) in the
vacuum, one obtains the following set of equations
εjmn∂m
(∂An
∂x0 +εnrs∂rCs
)
= 0, (69)
εjmn∂m
(∂Cn
∂x0−εnrs∂rAs
)
= 0. (70)
From the vector calculus, we conclude that there are two scalar functions κ1
and κ2 such that
∂Aj
∂x0 +εjmn∂mCn =∂jκ1, (71)
12
∂Cj
∂x0−εjmn∂mAn =∂jκ2. (72)
By using the equations (69) - (72), the following equations are obtained
δmn
∂(AmBn)
∂x0 + 2δmnEmBn−∂k (εkrsAkEs−κ1Bk) = 0. (73)
δmn
∂(CmEn)
∂x0 + 2δmnEmBn +∂k (εkrsCkBs +κ2Ek) = 0. (74)
From these, it follows that
∂(Hmm−Hee)
∂x0 + 4
∫
d3xδmnEmBn = 0, (75)
∂(Hmm +Hee)
∂x0 = 0. (76)
The equations (75) and (76) show that the pure electric and magnetic helic-
ities are conserved if the ﬁelds satisfy the ﬁrst null ﬁeld condition (50).
Let us quote here the explicit Hopﬁon solution obtained in [6]. The ﬁelds
φ and θ have the following form
φ = (ax1−x0x3) +i(ax2 +x0(a− 1)
(ax3 +x0x1) +i[a(a− 1)−x0x1], (77)
θ = [ax2 +x0(a− 1)] +i(ax3 +x0x1)
(ax1−x0x3) +i[a(a− 1)−x0x2], (78)
where xµ’s are dimensionless coordinates and
a = r2−x2
0 + 1
2 , r =
√
δmnx2
mx2
n. (79)
The electric and magnetic ﬁelds derived from the scalars given by the equa-
tions (77) and (78) have the following form
E = 1
π
qH1−pH2
(a2 +x2
0)3 , (80)
B = 1
π
qH1 +pH2
(a2 +x2
0)3 , (81)
where
H1 = (x2 +x0−x1x3) e1− [x1 + (x2 +x0)x3] e2
+ 1
2
[
−1−x2
3 +x2
1 + (x2 +x0)2]
e3 (82)
13
H2 = +1
2
[
1 +x2
1−x2
3− (x2 +x0)2]
e1 + [−x3 + (x2 +x0)x1] e2
+ (x2 +x0 +x1x3) e3, (83)
and
p =x0
(
x2
0− 3a2)
, q =a
(
a2− 3x2
0
)
. (84)
Here, we have denoted by {el} the unit vectors of the Cartesian basis in
the spatial directions. The Hopf indices of the above Hopﬁon solution are
H(φ) =H(θ) = 1 [30].
Another example of Hopﬁon is given by the Hopf map deﬁned by the
following scalar ﬁelds
φ = 2(x1 +ix2)
2x2
3 +i(δmnxmxn− 1), (85)
θ = ¯φ. (86)
The electromagnetic ﬁeld corresponding to these scalars has the following
components
Em = 1√
(2π)3
∫
d3k [Pm(kj) cos (ηµνkµxν)−Qm(kj) sin (ηµνkµxν)] , (87)
Bm = 1√
(2π)3
∫
d3k [Pm(kj) cos (ηµνkµxν) +Qm(kj) sin (ηµνkµxν)] , (88)
where
P = e−k0
√
2π
(
−k1k3
k0
,k0k2 +k2
2 +k2
3
k0
,−k0k1 +k1k2
k0
)
, (89)
Q = e−k0
√
2π
(
−k0k2 +k2
1 +k2
2
k0
,k1k3
k0
,k0k3 +k2k3
k0
)
. (90)
The ﬁelds given by the equations (87) and (88) describe a particular wave
packet that travels along the x3 axis and has the following energy, linear
momentum, and angular momentum densities
E = 2, p = (0, 0, 1) , L = (0, 0, 1) . (91)
The exact values ofE, p and L are calculated in a dimensionless parametriza-
tion of the space-time coordinates. From the equations (91), it follows that
the mass of the wave packet is ﬁnite and it has the value m2 = 3.
14
4 Electric and magnetic knots in Bateman
parametrization
In the previous section, we have discussed several parametrizations of the
ﬁeld line solutions. In this section, we present the factorized parametrization
of the self-dual electromagnetic ﬁelds in terms of 1-forms given by Bateman
in [41]. This representation is useful for the generalization of the ﬁeld line
solutions to the gravitating electromagnetic ﬁelds [32] as well as to the non-
linear electromagnetism [22, 23]. For extensive reviews of the properties of
the Hopﬁons in the Bateman representation see [20, 30, 42].
Let us recall the covariant form of Maxwell’s equation in the vacuum
given by the equations (28) and (29), namely
dF = 0, (92)
d⋆F = 0. (93)
The equation (92) states that the electromagnetic 2-form ﬁeld is closed. Then
F can be written in terms of two scalar complex functions
α : R3→ C, β : R3→ C, (94)
as follows
F =dα∧dβ. (95)
It is relevant to write the above equation in terms of the electric and magnetic
ﬁelds. To this end, we use the components of the electromagnetic 2-form F
which are the same as the components of the electromagnetic tensor Fµν. It
follows from the equation (95) that Fµν satisﬁes the following relation
iεµνρσFρσ− 2Fµν = 2εµνρσ∂ρα∂σβ. (96)
By deﬁnition, the electric and magnetic ﬁelds are given by the following
equations
−Em =F 0m, B m = 1
2εmnpFnp. (97)
Some algebraic manipulations of the equation (96) lead to the following re-
lation between the complex scalars
Bm−iEm =i (∂0α∂mβ−∂0β∂mα) . (98)
We know from the equation (39) that the electromagnetic ﬁeld in the vac-
uum is either self-dual or anti self-dual according to the eigenvalues of the ⋆
15
operation. That implies that the functions α andβ must obey the following
constraint
∇α×∇β =±i (∂0α∇β−∂0β∇α) . (99)
In order to understand the geometry of the electric and magnetic ﬁelds on
R3, it is useful to introduce the Riemann-Silberstein vector
F = B±iE, (100)
where E and B can be complex. Also, it is required that F be a solution of
Bateman’s equation
δmnFmFn = 0. (101)
Note that in general the norm of the ﬁeld F is non-zero
δmn ¯FmFn⁄= 0, (102)
where the bar stands for the complex conjugate. One can easily write the
equations (101) and (102) on components. The result is the following
δmn (BmBn−EmEn)± 2iδmnEmBn = 0, (103)
δmn
( ¯BmBn + ¯EmEn
)
= 0. (104)
If the vector ﬁeldsE and B are real, the left-hand side of the equation (103) is
an invariant of the electromagnetic ﬁeld and the left-hand side of the equation
(104) is the energy density of the electromagnetic ﬁeld. The equations (103)
and (104) deﬁne the so called null ﬁelds [19].
It is easy to verify that the Bateman solutions conserve the energy, mo-
mentum and the angular momentum of the electromagnetic ﬁeld. These
conservation laws follow from the Lorentz symmetry. Also, the U(1) sym-
metry of Maxwell’s equations implies that there is a conserved four-current
whose components are given by the following relations
ρ = 1
2δmn (EmEn +BmBn) , (105)
Jk =εkmnEmBn. (106)
Beside the conserved quantities discussed above, there are new topologically
conserved charges, the helicities from the equations (65)-(66). The Bate-
man equations admit solution with knot as well as toric topologies. In the
Bateman parametrization, diﬀerent solutions can be related to each other,
or derived from each other, due to the following important theorem [28]:
16
Let α and β be two smooth complex scalar ﬁelds on M that satisfy the
Bateman relation (99). Then for any two arbitrary smooth complex functions
f and g deﬁned on C2, the following 2-form exists
F :=df(α,β )∧dg(α,β ), (107)
andF has the following properties:
dF = 0, (108)
⋆F =±iF. (109)
There are several known solutions in the literature constructed with the
Bateman method. Let us cite here the Hopﬁon obtained in [19] whose com-
plex functions are given by the following relations
α =−x2
0 +δmnxmxn− 1 + 2ix3
−x2
0 +δmnxmxn + 1 + 2ix0
, (110)
β = x1−ix2
−x2
0 +δmnxmxn + 1 + 2ix0
. (111)
The functions α and β given above satisfy the following relation
|α|2 +|β|2 = 1. (112)
The electromagnetic vector F that is obtained fromα andβ has the following
form
F = 4
(−x2
0 +δmnxmxn + 1 + 2ix0)3
×


(x0−x1−x3 +i (x2− 1)) (x0 +x1−x3−i (x2 + 1))
−i (x0−x2−x3−i (x1 + 1)) (x0 +x2−x3 +i (x1− 1))
2 (x1−ix2) (x0−x3−i)

 , (113)
where F is in a column vector notation. The general properties of the ﬁeld
(113) are discussed in [19, 20].
New Hopﬁons can be obtained from a given solution by performing in-
ﬁnitesimal conformal transformations, or a subgroup of them, on the func-
tions α and β. In order to see that, recall that the scalar functions change
under the inﬁnitesimal coordinate trasformations as follows [20]
xµ→x
′µ =xµ +ξµ (114)
α(x)→α′(x′) =α(x) +ξν∂να(x), (115)
β(x)→β′(x′) =β(x) +ξν∂νβ(x), (116)
17
where ξ = ξµ∂µ is an arbitrary inﬁnitesimal smooth vector ﬁeld on R1,3.
The equation (99) is invariant under the transformations (114) - (116) if the
following condition is satisﬁed [20]
ϵrmn [δjr (∂0ξ0−∂sξs) +iϵjrs (−∂0ξs +∂sξ0) +∂jξr +∂rξj] ∂mα∂nβ = 0.
(117)
The generators of the special conformal transformations are the vector ﬁelds
ξµ =aµηµνxµν− 2aνxνxµ. (118)
It is easy to show that any vector ﬁeld of the form (118) is a solution of
the equation (117). By using this property of the special conformal transfor-
mations, the authors of [20] obtained new Bateman solutions characterized
by integer powers p and q of the scalar functions α and β. The plane wave
solution is one example of electromagnetic ﬁeld from which new solutions can
be generated by conformal deformations. The plane waves are characterized
by the following scalar functions
α =eı(x3−x0), β =x1 +ix2. (119)
The new functions that can be obtained from the equation (119) by conformal
deformations have the following form
α′ = exp
[
−1 + i (x0 +x3−i)
1−x2
0 +δmnxmxn + 2ix0
]
, (120)
β′ = x1 +ix2
1−x2
0 +δmnxmxn + 2ix0
. (121)
The electric and magnetic ﬁelds built from α′ and β′ have toric topology. A
generalization of this method to more complex knotted electromagnetic ﬁelds
was given in [43]. The conformal deformations method was applied to the
study of the physical properties of the optical vorticies in [44, 28].
