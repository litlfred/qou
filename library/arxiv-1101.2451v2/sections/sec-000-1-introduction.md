---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-4
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
The Einstein equation
Gµν = 0, (1)
and the incompressible Navier-Stokes equation
˙vi−η∂ 2vi +∂iP +vj∂jvi = 0, (2)
have long played central roles in both mathematics and physics. The Einstein equation universally governs
the long-distance behavior of essentially any gravitating system, while the incompressible Navier-Stokes
equation universally governs the hydrodynamic limit of essentially any ﬂuid. They both display a rich
non-linear structure which has been a continual source of interesting surprises yet remains, centuries
after their discovery, incompletely understood. It is the purpose of this paper to give a mathematically
precise relationship between (1) and (2) and their solutions, and thereby provide a hopefully useful bridge
between the two subjects. For example cosmic censorship could be related to global existence for Navier-
Stokes or the scale separation characterizing turbulent ﬂows related to radial separation in a spacetime
geometry, see e.g. [1,2].
Hints of such a connection, summarized in the next section, have surfaced in various forms over the
last three decades [3–28], see [26, 29–32] for reviews. In particular, excitations of a black hole horizon
dissipate very much like those of a ﬂuid [3–5, 12, 13, 28, 33–35], and there has been recent discussion of
a holographic duality relating black holes and ﬂuids [1, 8–10, 12, 14–17, 19, 21, 23, 24]. Inspired by these
suggestions, in this paper we explicitly construct a map from solutions of the nonlinear incompressible
Navier-Stokes equation to solutions of the nonlinear Einstein equation. A key ingredient is the imposition
of boundary conditions which, in a sense to be deﬁned, isolate the horizon dynamics from the rest of the
gravitational dynamics and thereby reduce equation (1) to equation (2).
Our basic construction is roughly as follows. We begin with the region ofp+2-dimensional Minkowski
space inside a hypersurface Σ c given by an equation of the form x2−t2 = 4rc. Σ c is intrinsically ﬂat
(being the translation of an hyperbola in the t-x plane along the remaining p spatial directions), but has
an extrinsic curvature linked to the constant accelerationa = 1/√4rc. It asymptotes to its future horizon
H+ which is the null surface x = t. We then study the eﬀect of ﬁnite perturbations of the extrinsic
curvature of Σc while keeping the intrinsic metric ﬂat. These generically lead, when evolved radially
inward with the Einstein equation, to singularities on H+. The special ones which are smooth on H+
are analyzed in the hydrodynamic “ ϵ-expansion”, which is a nonrelativistic, long-wavelength expansion
and, importantly, keeps terms that are nonlinear in the size of the perturbation. It is found that tensor
and scalar modes of the metric decouple in this limit and the remaining degrees of freedom are vector
modes governed by the Navier-Stokes equation inp+1 dimensions. We present (equation (14) below) the
p + 2-dimensional solution of the Einstein equation through third order in the hydrodynamic expansion
parameter ϵ. The ﬁrst term is ﬂat space. The second and third terms are algebraically constructed from
the velocity ﬁeldvi and pressureP of an incompressible ﬂuid. The nonlinear spacetime Einstein equation
then reduces to the nonlinear incompressible Navier-Stokes equation for the pair ( vi,P ).
This result is already interesting and non-trivial, but the fact that the Navier-Stokes arises when the
geometric variables are subject to the same kind of expansion used in ﬂuid dynamics might have been
anticipated. A deeper connection appears when we consider an alternate expansion in which, instead of
going to long distances, we take the acceleration of Σ c to inﬁnity. This is a near-horizon limit since it
pushes Σc towards its horizonH+. We then show that, after a constant overall rescaling of the metric, the
near-horizon expansion is mathematically identical to the hydrodynamic expansion. Hence the solutions of
the Einstein equation (constrained by the boundary conditions of a ﬂat metric on Σ c and smoothness on
H+) in this near-horizon expansion are in one-to-one correspondence with solutions of the incompressible
Navier-Stokes equation. This then is the precise mathematical sense in which horizons are incompressible
ﬂuids.
It is possible that the ultimate origin of this relation is a deep and exact holographic duality relating
(among other things) quantum black holes to ﬂuids as has been suggested by string theoretic investiga-
tions. However in this paper we have concentrated on simply establishing the mathematical relationship
between (1) and (2) in a manner which makes no assumptions about or reference to this tantalizing
possibility.
This paper is organized as follows. In section 2 we brieﬂy describe precursors of our construction
going back to the 70’s. Section 3 brieﬂy reviews the hydrodynamic expansion in the study of ﬂuids, and
the emergence of the incompressible Navier-Stokes equation in the hydrodynamic limit. In section 4 we
specify the boundary conditions, explained roughly above, used to isolate horizon dynamics. In section
5 we present the general solution of the nonlinear Einstein equation with these boundary conditions
through the ﬁrst three orders in the hydrodynamic expansion, and show that the ﬁrst nontrivial term
corresponds to the velocity ﬁeld of an incompressible ﬂuid. We also discuss the geometric analog of forcing
the ﬂuid, argue for uniqueness, and discuss the possible formation of black hole type singularities. Section
6 presents a simpler form of the metric and shows that, up to an overall rescaling and after an appropriate
coordinate transformation, it depends only on the product of the leading-order acceleration of Σc and the
hydrodynamic expansion parameter ϵ. In section 7 we show that the geometries are, through the order
constructed, of a special type known in four dimensions as Petrov type II. This may enable a connection of
the present work with the large literature on algebraically special spacetimes [36–38]. Finally in section
8 we demonstrate, using the simpliﬁed metric of section 6, the equivalence of the hydrodynamic and
near-horizon expansions.
