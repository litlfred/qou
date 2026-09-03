---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-6
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensi onal space."
---
Hopf solitons arise in theories in three-dimensional space where the ﬁeld takes values in
a two-sphere. The Skyrme-Faddeev model [1] is the most famous e xample of a theory with
Hopf solitons and consists of the O(3) sigma model modiﬁed by the addition of a Skyrme
term that is quartic in the derivatives of the ﬁeld. Substantial nume rical work [2, 3, 4, 5, 6]
has led to a reasonable understanding of the minimal energy solitons in this theory. There are
axially symmetric solitons for all Hopf charges but they are stable on ly for charges one, two
and four. For all other charges the minimal energy solitons are less symmetric and include
knotted and linked conﬁgurations. It is unknown whether the appe arance of knots and links
as minimal energy solutions is a universal feature of Hopf solitons, s ince the Skyrme-Faddeev
model is currently the only theory in which non-axial Hopf solitons ha ve been investigated.
The Nicole model [7] is a conformal ﬁeld theory with Hopf soliton solut ions. The confor-
mal symmetry allows the consistent use of an axially symmetric ansat z in toroidal coordinates
that reduces the partial diﬀerential equation of the static theor y to a single ordinary diﬀeren-
tial equation for a proﬁle function [8]. The toroidal ansatz involves a pair of integers ( n, m )
associated with angular windings around the two generating circles o f the torus, and the
corresponding Hopf charge is Q = mn. A ﬁeld conﬁguration of this type will be denoted by
An,m and may be thought of as a two-dimensional baby Skyrmion [9] with w inding number
m embedded in the normal slice to a circle in three-dimensional space, w ith a phase that
rotates through an angle 2 πn as it travels around the circle once. The proﬁle function and
energy within the toroidal ansatz have been obtained [7] in closed fo rm when Q = 1 and
have been computed numerically [10] for a range of pairs ( n, m ). In this paper we restrict to
the case Q > 0, since the situation for Q < 0 is simply obtained by reversing an orientation.
An upper bound has been derived [10] for the minimal energy soliton E ≤ cQ
3
4 , where
c is a known constant. This upper bound takes the same form as in the Skyrme-Faddeev
model [11]. Furthermore, in the Nicole model it has been shown that t he energy Eaxial of the
axial ansatz obeys a linear lower bound Eaxial ≥ ~cQ, with a known constant ~c. Together these
results imply that for suﬃciently large Hopf charge the minimal energ y Hopf soliton is not
obtained from the axially symmetric toroidal ansatz. This suggests that Hopf solitons in the
Nicole model may be similar to those in the Skyrme-Faddeev model, whe re unstable axially
symmetric solitons signal the appearance of more exotic knotted a nd linked solutions. The
purpose of the present paper is to investigate this issue using nume rical simulations of the full
nonlinear ﬁeld theory, without any restrictions to axial symmetry. This requires a numerical
method that can overcome known technical diﬃculties associated w ith simulations of a scale
invariant ﬁeld theory. We introduce a method of volume-preserving ﬂow to deal with this
issue and present the results of this approach for all Hopf charge s from one to eight. A
comparison with the Skyrme-Faddeev model suggests many univer sal features, including the
appearance of knotted and linked conﬁgurations, although there are some minor diﬀerences
in the details of particular links that appear at given Hopf charges.
2
2 The Nicole model and volume-preserving ﬂow
The Nicole model [7] is a rather exotic modiﬁcation of the O(3) sigma model, although
it involves the same ﬁeld φ : R3 ↦→S2, which is realized as a real three-component vector
φ = ( φ 1, φ 2, φ 3), of unit length, φ · φ = 1 . As we are concerned only with static solutions
then the Nicole model may be deﬁned by its static energy
E = 1
32π 2√
2
∫
(∂iφ · ∂iφ )
3
2 d3x, (2.1)
where the normalization is chosen for later convenience.
The fractional power in (2.1) is a novel modiﬁcation of the sigma mode l energy den-
sity and is clearly engineered to produce a conformal theory in thre e spatial dimensions.
Although there is no known physical motivation for this theory, the re is a mathematical
stimulus to investigate the model as the conformal symmetry leads to interesting mathemat-
ical properties: including an explicit exact solution for the Q = 1 Hopf soliton. By studying
this theory it is possible to make comparisons with Hopf solitons of the Skyrme-Faddeev
model and hence determine which features appear to be generic. T his should help in un-
derstanding the properties of Hopf solitons in theories construct ed from more conventional
terms.
Finite energy boundary conditions require that the ﬁeld tends to a c onstant value at
spatial inﬁnity, which is chosen to be φ = (0, 0, 1) ≡ e3. This boundary condition compactiﬁes
space to S3, so that the ﬁeld becomes a map φ : S3 ↦→S2. There is a homotopy classiﬁcation
of such maps, given by the Hopf charge Q ∈ Z = π3(S2). This integer has a geometrical
interpretation as the linking number of two curves obtained as the p reimages of any two
distinct points on the target two-sphere.
The position of the soliton is the closed curve obtained as the preimag e of the point
φ = (0 , 0, −1), which is antipodal to the vacuum value e3 on the target two-sphere. Hopf
solitons are therefore novel string-like topological solitons.
The static ﬁeld equation that follows from the variation of the energ y (2.1) is the nonlinear
partial diﬀerential equation
∂i∂iφ + (∂iφ · ∂iφ )φ + (∂i∂jφ · ∂jφ )∂iφ
∂kφ · ∂kφ = 0. (2.2)
Using combinations of stereographic projection and the standard Hopf map, the solution
with Hopf charge Q = 1 is explicitly given by [7]
φ 1 + iφ 2
1 + φ 3
= 2λ(x1 + ix2)
r2 − λ 2 + 2iλx3
. (2.3)
Here r2 = xixi and λ is an arbitrary positive real constant associated with the scale of t he
soliton. It is easily seen from (2.3) that the position of the soliton is th e circle in the plane
x3 = 0 with centre the origin and radius λ. The fact that λ is arbitrary is a result of the
conformal symmetry of the Nicole model.
3
The energy of this soliton is E = 1 , as a result of the convenient normalization of the
energy in (2.1). The soliton is axially symmetric and is of the type A1, 1.
In this paper we are interested in Hopf solitons of the Nicole model wit h Q > 1, for which
explicit closed form solutions are not available. Numerical methods ar e therefore required to
ﬁnd solutions of equation (2.2) that correspond to local minima of th e energy (2.1), including
the global energy minimum in each sector with Hopf charge Q that we consider.
The discretization (and restriction to a ﬁnite simulation region) involv ed in the numerical
simulation of a conformal ﬁeld theory breaks the conformal invaria nce of the continuum
theory and leads to technical diﬃculties. This has been studied in det ail for solitons in a
simpler conformal ﬁeld theory, namely the O(3) sigma model in two-dimensional space. The
numerical discretization is equivalent to studying a lattice version of the theory and in the
planar case the resulting energy minimization leads to an exceptional conﬁguration on the
lattice [12]. In the continuum theory this is associated with a reductio n of the soliton scale
until it is of the same order as the lattice spacing, at which point the t opology of the soliton
is lost as it unwinds by essentially falling through the lattice [13]. In the case of the planar
sigma model a novel lattice formulation has been devised [14] that p reserves topology on
the lattice. However, the topology of Hopf solitons in the Nicole mode l is signiﬁcantly more
complicated than that of solitons in the planar sigma model, and no ana logous topology
preserving lattice formulation is known.
As expected, a standard discretization and energy minimization of t he Nicole model leads
to the same technical diﬃculties as described above. Namely, any init ial condition with Q ⁄= 0
shrinks until the size of the conﬁguration is of the same order as th e lattice spacing, upon
which the topology is lost, leading to a trivial vacuum solution with Q = 0. An additional,
though related, issue is that in numerical simulations Euclidean space is typically replaced
by a ﬁnite region Ω , with the ﬁeld ﬁxed to its vacuum value on the boundary of Ω . This will
be a good approximation if Ω is large compared to the soliton size. Howe ver, in a conformal
theory there is no ﬁxed soliton size and the restriction to a ﬁnite volu me also results in the
shrinking of a soliton. To overcome these diﬃculties we introduce a vo lume-preserving ﬂow,
using ideas based on a similar approach developed in the context of do main walls [15].
To describe the construction of our volume-preserving ﬂow we initia lly concentrate on
the continuum theory deﬁned in a ﬁnite region Ω , with vacuum boundary conditions, φ = e3
on ∂Ω . In the later numerical simulations Ω will be taken to be a cube.
A standard method to minimize the energy (2.1) is to evolve any given in itial condition
using gradient ﬂow. A ﬂow which is proportional to gradient ﬂow is give n by
∂tφ = F, (2.4)
where the force F is the left-hand-side of the static ﬁeld equation (2.2), and is propor tional
to the variation of the energy (taking into account the constraint that φ lies on the unit two-
sphere). Theoretically, the end-point of this ﬂow yields static solut ions that solve equation
(2.2). As described above, a numerical discretization introduces a spatial lattice that breaks
the conformal symmetry of the theory, so that a numerical solut ion of a standard discrete
version of (2.4) results in a Hopf soliton that continually shrinks durin g the ﬂow. A minimal
4
energy Hopf soliton in the continuum theory has zero modes (in part icular a scale invariance)
associated with the conformal symmetry and the spatial lattice pr oduces negative modes
associated with the broken zero modes. The idea is to modify the sta ndard gradient ﬂow
(2.4) by projecting out the component in the direction of the zero m ode. The subsequent
discretization will then not produce negative modes since their origin has been removed from
the ﬂow.
Deﬁne the following volume associated with a ﬁeld conﬁguration
V =
∫
Ω
(1 − φ 3) d3x. (2.5)
This volume will serve as a measure of the size of a soliton, since the int egrand is maximal
along the position of the soliton and is zero if the ﬁeld takes its vacuum value. In particular,
the shrinking of a soliton that results from the numerical discretiza tion corresponds to a
decrease of the volume V during the gradient ﬂow (2.4). The aim is to construct a modiﬁed
version of gradient ﬂow that preserves the volume V, and hence ﬁxes the soliton scale.
Associated with the volume (2.5) is the gradient ﬂow
∂tφ = e3 − φ 3φ ≡ f, (2.6)
which results in a decrease in the volume V during this ﬂow, since the force f is proportional
to the variation of V. Deﬁne the inner product
< f, g > =
∫
Ω
f · g d3x, (2.7)
then the volume-preserving ﬂow is given by
∂tφ = F − < F, f >
< f, f > f. (2.8)
This ﬂow has been constructed by taking the standard gradient ﬂo w and then projecting
out the component due to the volume reducing ﬂow (2.6). The result ing ﬂow is therefore
orthogonal to the volume reducing ﬂow and hence preserves the v olume. It is easy to prove
that the volume-preserving ﬂow (2.8) indeed preserves the volume V and reduces the energy
E: the proof is a simple modiﬁcation of that presented in [15] but the r esult should be
obvious from the geometrical aspect of its construction.
Equation (2.8) is a nonlinear partial diﬀerential equation but it is also n onlocal, because
of the appearance of the inner product. However, it can be solved numerically using standard
ﬁnite diﬀerence methods. In section 4 we shall present results for a scheme using fourth-order
accurate ﬁnite diﬀerence approximations to spatial derivatives on a cubic lattice consisting
of 151 3 points with unit lattice spacing (taking advantage of the scale invaria nce of the
continuum problem in R3). The ﬂow is evolved using a simple ﬁrst-order accurate explicit
method with timestep ∆ t = 0. 1. All inner products are evaluated by approximating integrals
by sums over lattice sites.
5
