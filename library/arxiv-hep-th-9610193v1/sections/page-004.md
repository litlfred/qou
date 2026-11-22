---
doc_id: arxiv-hep-th-9610193v1
doc_title: "KNOTS AND PARTICLES"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9610193v1.pdf
source_sha256: e879864ec3a68faf
toc_source: undetermined
doc_brief: "KNOTS AND PARTICLES — 14 sections: Page 1; Page 2; Page 3"
---
Several articles have been devoted for analyzing the general properties of the unknot
vortex in the model (2) [12]. However, to our knowledge there have been no real attempts
to ﬁnd an actual solution. This is due to the fact, that even in the simplest case of an
unknot the separation of variables eliminates only one of the three space coordinates,
leaving numerical methods as the sole alternative for ﬁnding a solution. With the recent,
enormous progress in supercomputing techniques serious attempts are ﬁnally becoming
realistic.
The Euler-Lagrange equations for (2) determine a highly nonlinear elliptic system,
and a direct numerical approach appears to be complicated. Instead, we consider the
parabolic equation
dφa
dt
= −δH(φ)
δφa
(4)
where φa denotes a generic dynamical variable in (2). The t-bounded solutions of (4)
connect the critical points of H by ﬂowing away from an unstable critical point at
t →−∞towards a stable critical point at t →+∞. From this we expect that by
deﬁning a suitable initial conﬁguration at t = 0, for large t ≫0 we ﬂow towards a stable
vortex solution of the original stationary equation.
We parametrize our unit vector by⃗n = (cos ϕ sin θ, sin ϕ sin θ, cos θ) through stere-
ographic coordinates ϕ = −arctan(V
U ) and θ = 2 arctan
√
U2 + V 2. In terms of these
variables the Hamiltonian (2) becomes
H =
Z
d3x
4g2
(1 + U2 + V 2)2(∂µU2 +∂µV 2)+
16e2
(1 + U2 + V 2)4(∂µU∂νV −∂νU∂µV )2 (5)
By a global SO(3) rotation we can select our asymptotic vacuum vector⃗n0 so that
outside of the vortex it points to the positive-z direction. This means that outside of
the vortex we are near the north pole where θ(⃗x) ≈0, while the core corresponds to
the south pole θ(⃗xc) = π. The internal structure of a vortex can then be investigated
by cutting it once with a plane at right angle to its core. This cross sectional plane is
topologically identical to a sphere S2: At the core we have θ(⃗xc) = π corresponding to
the south pole and outside of the vortex on the plane we have θ(⃗x) ≈0 corresponding
to the north pole. Furthermore, ϕ(⃗x) increases (or decreases, depending on orientation)
by 2π when we go around the core once on the cross sectional plane.1 For Uand V this
means, that we identify them as local coordinates on the Riemann sphere in a patch
that contains the north pole U(⃗x) = V (⃗x) = 0.
In ﬁgures 1 and 2 we have drawn θ(⃗x) and ϕ(⃗x) respectively for our unknot vortex.
The general structure is clearly visible in these pictures.
In the present model there are two symmetries that relate a given vortex solution
with Hopf invariant QH to an antivortex solution with equal energy but opposite Hopf
1More generally, ϕ is deﬁned modulo 2πn where n is an integer. Here we only consider the simplest
case with n = ±1.
3
