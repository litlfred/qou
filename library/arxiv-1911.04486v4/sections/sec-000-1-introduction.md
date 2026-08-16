---
doc_id: arxiv-1911.04486v4
doc_title: ""
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
doc_brief: "Knots and the Maxwell Equations Ion V. Vancea Grupo de F´ ısica Teórica e Matemática F´ ısica Departamento de F´ ısica Universidade Federal Rural do Rio de Janeiro — In this chapter, we review the"
---
The discovery of the knot solutions of Maxwell’s equations in the vacuum
represents one of the most exciting results obtained recently in the modern
classical electrodynamics. Since their ﬁrst appearance in the seminal papers
[1, 2, 3, 4], many interesting properties, applications, and generalizations of
the knot electromagnetic ﬁelds have been discovered.
The knot solutions of Maxwell’s equations can be described in terms of
electric and magnetic ﬁeld lines, and their topology can be given in terms of
a pair of complex scalar ﬁelds that are interpreted as Hopf maps S3→ S2
on the compactiﬁed space-like directions of the Minkowski space-time [4]-[6].
Among the properties studied up to now, one can cite: the relationship be-
tween the linked and the knotted electromagnetic ﬁelds discussed in [7, 8],
the dynamics of the electric charges in topologically non-trivial electromag-
netic backgrounds investigated in [10]-[13], and the topological quantization
presented in [14]-[17]. In the last decade, the Ra˜ nada solutions were gen-
eralized in two ways. The ﬁrst generalization is from knot ﬁelds to torus
ﬁelds and was given in the works of Arrayas and Hoyos [18]-[20]. The second
generalization is from the electromagnetic ﬁelds in vacuum to electromag-
netic ﬁelds in matter. Several authors have showed that topological ﬁelds
can be found in various areas of physics such as: ﬂuid physics [22, 23], atmo-
spheric physics [24], liquid crystals [25], plasma physics [26], optics [27, 28],
and superconductivity [29]. (For a recent review of the knot solutions and
their applications see [30] and the references therein). More recently, new
and important generalizations of the topological electromagnetic ﬁelds have
been made to the non-linear electrodynamics, the ﬂuid physics [21]-[23] as
well as to the gravitational physics [31] - [34]. A new method to obtain the
electromagnetic knot solutions in Minkowski space, by completely solving
the Maxwell equations ﬁrst in de Sitter space and then conformally mapping
to Minkowski space was presented in [35, 36].
Due to their wide range of applications in both physics and mathematics,
the topological electromagnetic ﬁelds represent an important ﬁeld of science
and an active line of research.
In the present chapter, we are going to revisit the construction of the
knot solutions of Maxwell’s equations in Ran˜ ada’s approach. Also, we are
going to brieﬂy survey the diﬀerent mathematical formulations of Maxwell’s
equations and to present the construction of the Hopf maps in electrody-
namics. Of utmost importance for the understanding of the knot solutions is
the factorization method of the 2-forms introduced by Bateman. We will re-
view the application of Bateman’s method to the topological electromagnetic
ﬁelds. Finally, we are going to present the argument from [22, 23] where it was
1
showed that knot solutions can also be found in the non-linear Born-Infeld
electrodynamics and other non-linear generalizations of Maxwell’s electrody-
namics. We will focus our presentation on the electromagnetic ﬁelds in ﬂat
space-time. The generalization of the ﬁeld line solutions to the gravitating
electromagnetic ﬁelds is discussed in a diﬀerent chapter of this volume [37].
The results reviewed here can be found in the original papers cited in the
text. Other reviews are available too, most notably [30] to which we refer
for an updated list of references. In the Appendix, we collect some basic
mathematical properties of the Hopf mapping. We adopt throughout this
chapter the natural units in which c = 1.
2 Maxwell’s equations
In this section, we will brieﬂy review the formulation of Maxwell’s electrody-
namics in terms of diﬀerential forms in the three-dimensions Euclidian space
and in the four-dimensional space-time (the covariant formulation). This is
a well-known material which can be found in standard textbooks on classical
electrodynamics such as [38, 39].
2.1 Maxwell’s equations in the three-dimensional for-
mulation
The two formulations of Maxwell’s equations that are our concern in this
paper are: the formulation in terms of diﬀerential forms and the covari-
ant formulation. Both formulations are equivalent to the one in terms of
three-dimensional vectors that is known from the undergraduate textbooks
on electrodynamics, see e. g. [38].
Consider the following standard form of Maxwell’s equations in the
Heaviside units
∇· D =ρ, (1)
∇· B = 0, (2)
∇× E =−∂B
∂t , (3)
∇× H = J + ∂D
∂t . (4)
Here, E and H are the electric and magnetic intensities and D and B are the
electric and magnetic ﬂux densities, respectively. The sources of the electric
and magnetic ﬁelds are the density of charge ρ and the density of vector
2
current J. All vectors are three-dimensional and they are deﬁned on the
entire R3 at each instant of time if no other conditions are imposed on the
system.
The set of equations (1) - (4) can be written in terms of diﬀerential
forms from either Ω k(R3) or Ωk(R1,3) which denote the diﬀerential forms of
rank k deﬁned on the corresponding spaces. This abstract mathematical
formulation is advantageous for at least two reasons - ﬁrst, it provides a
more economical formulation of the basic relations of the electromagnetism.
Second, it provides the mathematical framework that is necessary for the
generalization of the classical electromagnetism to curved space-times (see
e. g. [39]). The diﬀerential forms associated with the three-dimensional
electromagnetic ﬁeld are given in the Table 1.
Table 1: Field content of Maxwell’s equations
Vector Form Form Field
notation notation rank
E E 1 - form electric intensity
H H 1 - form magnetic intensity
D D 2 - form electric ﬂux density
B B 2 - form magnetic ﬂux density
ρ Q 3 - form charge density
J J 2 - form current density
It is easy to show that the diﬀerential forms from the Table 1 can be
projected onto the orthonormal Cartesian basis of R3. The corresponding
components are given by the following relations
E =Exdx +Eydy +Ezdz,
H =Hxdx +Hydy +Hzdz,
D =Dxdy∧dz +Dydz∧dx +Dzdx∧dy,
B =Bxdy∧dz +Bydz∧dx +Bzdx∧dy,
Q =ρdx∧dy∧dz,
J =Jxdy∧dz +Jydz∧dx +Jzdx∧dy. (5)
The basis (dx,dy,dz ) from the space Ω 1(R3) of 1-forms is associated by the
canonical procedure to the basis (x,y,z ) from R3. The second canonical basis
(dx∧dy,dy∧dz,dz∧dx) in the space Ω 2(R3) of 2-forms is constructed from
the 1-forms (dx,dy,dz ) by taking their wedge product which is deﬁned as
3
follows
∧ : Ωk× Ωs→ Ωk+s, (ω,σ )→ω∧σ. (6)
In the equation above, we have not speciﬁed which is the base space because
the wedge product is deﬁned in the same way on either R3 or R1,3.
In order to write Maxwell’s equations in terms of diﬀerential forms, one
has to recall that the exterior derivative d is deﬁned as being the R-linear
map from Ωk→ Ωk+1 with the following properties
df =∂ifdx i, (7)
d2ω = 0, (8)
d (ω∧σ) =d (ω)∧σ + (−)kω∧d (σ) . (9)
Here,f is an arbitrary smooth function andω andσ are arbitrary diﬀerential
forms. Note that the exterior derivative is nilpotent, i. e. d2 = 0.
The Hodge dual operation ⋆ is deﬁned as the map from Ω n−k→ Ωk,
where n is the dimension of the base manifold, that satisﬁes the following
relation
ω∧ (⋆σ) =⟨ω,σ⟩n. (10)
Here, n is an unitary vector and⟨·,·⟩ is the scalar product. In particular, the
action of the Hodge star operator on the components of an arbitrary k-form
is given by the following equations [39]
ω = 1
k!ωi1,...,ikdxi1∧···∧ dxik =
∑
i1<···<ik
ωi1,...,ikdxi1∧···∧ dxik, (11)
(⋆ω ) = 1
(n−k)!(⋆ω )ik+1,...,indxik+1∧···∧ dxin. (12)
The above equations can be easily particularized to the three-dimensional
case. For example, the Hodge duals to the elements of the canonical basis in
the space of 1-forms are given by the following relations
⋆dx =dydz, ⋆dy =dzdx, ⋆dz =dxdy. (13)
Similarly, the Hodge duals of the elements of the canonical basis in the space
of 1-forms are obtained from the equation (12) and they are given by the
following relations
⋆ dydz =dx, ⋆dzdx =dy, ⋆dxdy =dz. (14)
The equations (13) and (14) illustrate the more general property of invo-
lution ⋆ (⋆ω ) = ω in the three-dimensional Euclidean space. By using the
4
equations (12), (13) and (14), one can show that the exterior derivative d
can be decomposed in the canonical basis as follows
d = (∂xdx +∂ydy +∂zdz)∧ . (15)
By using the exterior derivative from the equation (15), one can write the
Maxwell equations in terms of the three-dimensional diﬀerential forms. The
result is given by the following set of equations
dD =Q, (16)
dB = 0, (17)
dE =−∂tB, (18)
dH =J +∂tD. (19)
It is easy to recognize in the equations (16) - (19) the familiar laws of the
electromagnetism. They allow one to write the electromagnetic ﬁeld in terms
of potentials Φ andA. That is made possible by the Poincar’s theorem, that
states that on a contractible manifold all closed forms ( dω = 0) are exact,
i. e. for any exact form ω there exists a form σ such that ω = dσ [39].
By applying this mathematical result, one can show that the electric and
magnetic 1-forms can be written as follows
E =−dΦ−∂tA, (20)
B =dA. (21)
It is an simple exercise to show that the equations (16) - (19) are invariant
under the following gauge transformations
Φ→ Φ′ = Φ−∂tΛ, (22)
A→A ′ =A +dΛ, (23)
where Λ is an arbitrary smooth function that plays the role of the gauge
parameter.
The equations (16) - (19) describe the dynamics of the electromagnetic
ﬁeld alone. Their solutions are given in terms of charge and current densities,
respectively, which are non-dynamical objects. As usual, the change of the
source state is given by Newton’s second law written for the Lorentz force,
which has the following form
FL =ρE− ι(⋆J )B. (24)
The interior product ι is deﬁned as the contraction between a diﬀerential
form from the space Ωk and a vector ﬁeldX. The interior product lowers the
5
form degree by one, and its image belongs to the space Ωk−1. For example, if
ω∈ Ω2 is a 2-form, its interior product with the vector ﬁeld X is the 1-form
ιXω for which the following equality holds
ιXω(Y ) =ω(X,Y ), (25)
where Y is an arbitrary smooth vector ﬁeld. The equation (25) is the last
equation needed to represent the dynamics of the electromagnetic ﬁeld and
its sources in terms of diﬀerential forms. Since in the rest of this chapter we
will investigate the topological solutions of the electromagnetic ﬁeld in the
vacuum, that is away from its sources, we will ignore the Lorentz force as
well as the charge and current densities.
