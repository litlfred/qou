---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-007-2-background-on-cone-deformation
section_title: "Background on Cone Deformation"
section_number: 2
pages: 7-9
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
In this section, we will recall deﬁnitions associated with c one deformations
and review relevant results from work of Hodgson and Kerckho ﬀ ([13], [14]).
Deﬁnition 2.1. Let M be a 3–manifold containing a closed 1–manifold
Σ. A hyperbolic cone structure on M is an incomplete hyperbolic structure
on X = M − Σ, whose completion is singular along Σ. A cross section of a
component of Σ is a hyperbolic cone with angle α, where α is constant along
that component. (For a more complete description of the metr ic on M , see
[13].) The set Σ is called the singular locus of M . M with this structure is
called a hyperbolic cone manifold . A hyperbolic cone deformation on M is a
smooth one–parameter family of hyperbolic cone structures Xt.
2.1. Inﬁnitesimal deformations. Now, we may study deformations by
considering possible “derivatives at time t” of Xt, or inﬁnitesimal defor-
mations of hyperbolic structure, for any time t. Each of these inﬁnitesi-
mal deformations corresponds to an element in a certain coho mology group
H 1(X; E), where recall X = M − Σ. We will be manipulating elements of
H 1(X; E), so we recall some information on their structure.
2.1.1. Cohomology. Given ω in H 1(X; E), ω is a one–form on X with values
in the vector bundle E of inﬁnitesimal isometries of X. The bundle E has
ﬁber sl(2, C), which is the Lie algebra of inﬁnitesimal isometries of H3.
Recall that this Lie algebra has a complex structure. Geomet rically, if s
represents an inﬁnitesimal translation in the direction of s, then is represents
an inﬁnitesimal rotation with axis in the direction of s. Thus on X we can
identify E with the complexiﬁed tangent bundle T X ⊗ C, and write any
ω ∈ H 1(X; E) in complex form: ω = v + iw.
8 JESSICA S. PURCELL
By the Hodge theorem proved in [13], in each cohomology class of H 1(X; E)
there is a harmonic representative of the form
ω = η + i ∗ Dη,
where η is a unique T X-valued 1–form on X = M − Σ that satisﬁes:
D∗η = 0,
(2) D∗Dη + η = 0.
Here D is the exterior covariant derivative on such forms and D∗ is its
adjoint.
Thus we may assume that our cone deformation is chosen such th at at
each time t, the inﬁnitesimal deformation of hyperbolic structure of Xt cor-
responds to a harmonic element ω in H 1(X; E).
2.1.2. Tubular and Horoball neighborhoods. For purposes of this paper, we
are particularly interested in the eﬀect of the deformation i n a neighborhood
of the singular locus or in a horoball neighborhood of a cusp. So in this
subsection, we will review a decomposition of ω (and η) into a nice form in
these types of neighborhoods.
Select a component of the singular locus Σ of M . Let V be a tubular
neighborhood of that component, with tube radius R. V is a solid torus with
a singular core curve. During the cone deformation, the geom etric structure
on V is changing in meridional, longitudinal, and radial direct ions. We can
write ω in V to reﬂect this:
(3) ω = ω0 + ωc.
Here only ω0 = η0 + i ∗ Dη0 changes the holonomy of the meridian and
longitude on the torus ∂V , and ωc is a correction term.
We can further decompose ω0 as follows:
(4) ω0 = u ωm + (x + iy) ωℓ.
Here, u, x, and y are real numbers. The 1–forms ωm and ωℓ are standard
forms, calculated in [13], which depend only on the tube radi us R of V . The
form ωm = ηm + i ∗ Dηm gives the change in the meridional direction. In
particular, it represents the inﬁnitesimal deformation wh ich decreases the
cone angle but doesn’t change the real part of the complex len gth of the
meridian. The form ωℓ = ηℓ + i ∗ Dηℓ stretches the singular locus, but leaves
the holonomy of the meridian unchanged.
Since we will use the explicit formula for the standard form ωℓ in a cal-
culation in a later section, we will restate that form here. L et e1, e2, and e3
be an orthonormal frame for V in cylindrical coordinates, with e1 pointing
in the radial direction and e2 tangent to the meridian. Let R be the radius
of the tube V . Recall ωℓ is a ( T X ⊗ C)–valued 1–form, which can be viewed
CUSP SHAPES UNDER CONE DEFORMATION 9
as an element of Hom(T X, T X ⊗ C). Thus it can be described as a matrix
in the cylindrical coordinates e1, e2, e3.
(5) ωℓ(R) =


(cosh R)−2 0 0
0 −1 −i tanh R
0 −i tanh R 1 + (cosh R)−2


Now, so far, our decomposition of ω has been in a tubular neighborhood
V of a component of the singular locus. We can do a similar decom position
of ω in a horoball neighborhood U of a cusp. In fact, we may consider U
as a tubular neighborhood of a 1–dimensional submanifold of M on which
the cone angle remains 0 throughout the deformation, and the tube radius
is inﬁnite. Again we may decompose ω as ω0 + ωc, where only ωc aﬀects the
holonomy of the torus ∂U . But now, since the cone angle at the core of U
is not changing, the meridional part of ω0 is identically 0. Thus in this case,
ω0 = (x + iy) ωℓ,
where again x and y are real numbers, and ωℓ is a standard form. Since the
tube radius of U is inﬁnite, to write down the formula for ωℓ explicitly we
let R go to inﬁnity in equation (5).
(6) ωℓ(∞) =


0 0 0
0 −1 −i
0 −i 1


