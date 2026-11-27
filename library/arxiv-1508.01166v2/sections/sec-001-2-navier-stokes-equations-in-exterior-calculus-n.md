---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-001-2-navier-stokes-equations-in-exterior-calculus-n
section_title: "Navier-Stokes equations in exterior calculus notation"
section_number: 2
pages: 4-6
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The ﬁrst step in deriving a DEC discretization of NS equations is to express
the equations using the exterior calculus notation. This is done ﬁrst by starting
from the well-known vector calculus formulation of NS equations (in Euclidean
space) and substituting with identities relating the di ﬀerential operators; viz. div,
grad and curl, with exterior calculus operators; viz. exterior derivative, Hodge
star and wedge product. An alternative derivation of the resultant formulation is
then presented, starting from the coordinate invariant formulation of NS equations
expressed in terms of the Lie and exterior derivatives. Readers not familiar with
exterior calculus may refer to [17, 18] for a concise introduction to the topic.
Considering the incompressible ﬂow of a homogeneous ﬂuid with unit density
and no body forces, the governing equations for the ﬂuid motion are the Navier-
Stokes equations expressed as
∂u
∂t−µ∆u + (u.∇)u +∇p = 0, (1a)
∇.u = 0, (1b)
where u is the velocity vector, p is the pressure and µ is the dynamic viscosity.
Substituting with the tensor identities: ∆u =∇(∇.u)−∇× (∇× u) and (u.∇)u =
1
2∇(u.u)− u× (∇× u), and considering the incompressibility condition∇.u = 0,
Eq. (1a) can be expressed in its rotational form as
∂u
∂t +µ∇×∇× u− u× (∇× u) +∇pd = 0, (2)
where pd is the dynamic pressure deﬁned as pd = p + 1
2(u.u).
The notation transformation is carried out by applying the ﬂat operator ( ♭) to
Eqs. (2) and (1b), and substituting with the following identities
(∇×∇× u)♭ = (−1)N+1∗ d∗ du♭,
(u× (∇× u))♭ = (−1)N+1∗ (u♭∧∗ du♭),
(∇.u)♭ =∗d∗ u♭,
(∇pd)♭ = dpd,
(3)
where∗ is the Hodge star, d is the exterior derivative, and∧ is the wedge product
operators. The action of the ﬂat operator ( ♭) on a vector u transforms it into a
1-form u♭. The sign (−1)N+1 in the ﬁrst two relationships implies a negative sign
4
only in the two-dimensional (2D) case, where N is the space dimension (i.e. N =
2 and 3 for the 2D and 3D cases, respectively). The above relationships can be
easily veriﬁed using the deﬁnition of di ﬀerential forms and the action of exterior
derivative, Hodge star and wedge product operators on them. Substituting with
Eqs. (3) in Eqs. (2) and (1b), the Navier-Stokes equations are then expressed as
∂u♭
∂t + (−1)N+1µ∗ d∗ du♭ + (−1)N+2∗ (u♭∧∗ du♭) + dpd = 0, (4a)
∗ d∗ u♭ = 0, (4b)
where the velocity ﬁeld is represented by the 1-formu♭ and pd is now the dynamic
pressure 0-form.
The above formulation in Eqs. (4) is derived starting from the standard vector
calculus formulation of NS equations. We now present an alternative derivation
purely in terms of diﬀerential forms, starting from NS equations formulated using
the exterior derivative (d) and the Lie derivative (£) operators. The Navier-Stokes
equation in coordinate invariant form is (see [19] pg. 589 for Euler equation in
this form)
∂u♭
∂t +µ(δd + dδ)u♭ + £uu♭− 1
2d(u♭(u)) + dp = 0, (5)
whereδ is the codiﬀerential operator deﬁned as δ = (−1)N(k−1)+1∗ d∗, which acts
on a k-form and results in a ( k− 1)-form, and N again is the space dimension.
Therefore, the incompressibility condition (Eq. (4b)) translates to δu♭ = 0. The
operator (δd + dδ) is the Laplace operator in the exterior calculus notation, which
diﬀers by a negative sign from that deﬁned in the vector calculus notation (e.g.
the Laplace operator in Eq. (1a)). The Lie derivative term (£ uu♭) evaluates the
change of the velocity 1-form u♭ along the velocity vector ﬁeld u, and the term
u♭(u) represents the dot product of the vector ﬁeld u with itself. Using Cartan
homotopy formula (see [19], pg. 430), the Lie derivative term is expressed as
£uu♭ = diuu♭ + iudu♭ = d(u♭(u)) + iudu♭, (6)
where ixα is the interior product of a k-formα with a vector ﬁeld x. Accordingly,
considering the incompressibility conditionδu♭ = 0, Eq. (5) can be expressed as
∂u♭
∂t +µδdu♭ + iudu♭ + 1
2d(u♭(u)) + dp = 0. (7)
5
Deﬁning the dynamic pressure 0-form as pd = p + 1
2(u♭(u)), and substituting
with δ = (−1)N+1∗ d∗ since the codi ﬀerential operator δ in Eq. (7) acts on the
2-form du♭ (hence k = 2), Eq. (7) then takes the form
∂u♭
∂t + (−1)N+1µ∗ d∗ du♭ + iudu♭ + dpd = 0. (8)
The interior product term iudu♭ can be written in terms of the Hodge star and
wedge product using the formula (see [15] Eq. 8.2.1)
ixα = (−1)k(N−k)∗ (∗α∧ x♭), (9)
for a k-form α and a vector ﬁeld x. Therefore, with x = u and α = du♭ (hence
k = 2), Eq. (8) becomes
∂u♭
∂t + (−1)N+1µ∗ d∗ du♭ + (−1)N−2∗ (u♭∧∗ du♭) + dpd = 0, (10)
where the order of the wedge product was ﬂipped using the relation α∧ β =
(−1)klβ∧α, withα =∗du♭ is an (N− 2)-form andβ = u♭ is a 1-form. Noting that
(−1)N+2 = (−1)N−2 = (−1)N for any N, Eq. (10) is exactly the same as Eq. (4a),
which was derived earlier starting from the standard vector calculus formulation
of Navier-Stokes equation.
Applying the exterior derivative operator to Eq. (10) (equivalent to taking the
curl of the momentum equation Eq. (2)), and considering the exterior derivative
property dd = 0, the resulting governing equation is
∂du♭
∂t + (−1)N+1µd∗ d∗ du♭ + (−1)Nd∗ (u♭∧∗ du♭) = 0. (11)
The DEC discretization of Navier-Stokes equations is carried out through the dis-
cretization of Eq. (11). The advantage of discretizing the vorticity form of the NS
equations is highlighted in the next section.
