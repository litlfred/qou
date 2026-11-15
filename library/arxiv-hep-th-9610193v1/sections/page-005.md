---
doc_id: arxiv-hep-th-9610193v1
doc_title: "KNOTS AND PARTICLES"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 9610193v1.pdf
source_sha256: e879864ec3a68faf
toc_source: undetermined
doc_brief: "KNOTS AND PARTICLES — 14 sections: Page 1; Page 2; Page 3"
---
invariant −QH. The ﬁrst symmetry emerges when we change orientation ϕ →−ϕ on the
cross sectional plane. The second symmetry interchanges the north pole with the south
pole on the cross sectional plane, i.e. maps the core to θ(⃗xc) = 0 and the region outside
of the vortex to θ(⃗x) ≈π. In terms of the U(⃗x) and V (⃗x) variables this means that
on each cross sectional plane the Hamiltonian (5) must be invariant under the inversion
Z(⃗x) = U(⃗x) + iV (⃗x) →Z−1(⃗x). This implies in particular, that the energy density
H(⃗x) must be concentrated in a relatively narrow tubular neighborhood around the core
of the vortex.
In ﬁgure 3 we have depicted the energy density on a cross sectional plane for the
unknot vortex. The concentration of energy density in a tubular manner around the
core is clearly visible.
In order to specify the initial condition in (4) we need a knot conﬁguration which is
topologically equivalent to the desired vortex solution. We specify this conﬁguration by
ﬁrst introducing a parametrization⃗x(λ) for the center of the knot in R3, and then for
each λ use the Serret-Frenet equations to deﬁne local coordinates U(⃗x; λ) and V (⃗x; λ)
on the cross sectional planes.
The choice of initial parametrization⃗x(λ) for the core introduces a scale which may
be quite diﬀerent from the one speciﬁed by the coupling constant g in (5). In order to
enhance convergence, we adopt a simple renormalization procedure by promoting g to
a time dependent function g(t). We deﬁne this time dependence by demanding that at
each value of t the virial theorem (3) must be obeyed. Since a vortex solution obeys (3),
this means that g(t) ﬂows towards a ﬁxed point value g(t) →g⋆.
We have performed our numerical simulations using version 5.3 of G. Sewell’s PDE2D
ﬁnite element algorithm [15]. During the early phase of our simulations we have used
the initial knot conﬁguration to determine the boundary conditions on the ﬁnite element
mesh. However, since the exact boundary conditions for the desired vortex are a priori
unknown, after several time steps we have decreased the size of the ﬁnite element mesh
and used the pertinent simulated conﬁguration to determine the boundary conditions
in the new mesh. By starting from a suﬃciently large initial mesh, we then eventually
obtain a submesh with boundary conditions that are close to those of the actual solution.
For our simulation we have used two Silicon Graphics Power Challenge computers
with R8000 processors equipped with 1GB resp. 2GB of internal memory.
For the unknot vortex (QH = ±1), the equations of motion can be simpliﬁed using
axial symmetry. We select the symmetry axis to coincide with the z-axis in R3, and
introduce cylindrical coordinates r, φ, z. With the Ansatz ϕ(⃗x) = ϕ(r, z)+φ and θ(⃗x) =
θ(r, z) the φ-coordinate separates, and we obtain a two dimensional equation for U(r, z)
and V (r, z). That such a separation of variables is possible follows directly from the
SO(2)×SO(2) symmetry of the unknot conﬁguration. The ensuing equations are deﬁned
on the half-plane r ≥0, z ∈(−∞, ∞), which at each φ determines our cross sectional
4
