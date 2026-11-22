---
doc_id: arxiv-hep-th-9506138v1
doc_title: "Black Hole Complementarity vs. Locality"
section_id: sec-001-2-the-nice-slice-argument
section_title: "The Nice-Slice Argument"
section_number: 2
pages: 5-8
source_pdf: 9506138v1.pdf
source_sha256: bb85afba0530402c
toc_source: inferred
doc_brief: "Black Hole Complementarity vs. Locality — 18 sections: Front matter; Introduction; The Nice-Slice Argument"
---
Consider the process by which a collection of particles of total mass M gravitation-
ally collapses to form a black hole. In the absence of any net angular momentum, the
black hole becomes approximately spherically symmetric in a short time after the collapse
process. As long as we are only considering processes with lifetimes short compared to
G2M 3, we can approximate the geometry of the system by the Schwarzschild solution.
The nice-slice argument begins by introducing a family of Cauchy surfaces which foliate
the geometry. The surfaces should avoid regions of strong spacetime curvature and yet
cut through the infalling matter and the outgoing Hawking radiation so that both sets of
particles have low energy in the local frame of the slice. Also, in order to ensure that short
distance physics does not creep in to the description through the choice of coordinates, we
require that the slices be everywhere smooth, with small extrinsic curvature compared to
any microscopic scale. For convenience, we will choose surfaces that agree with surfaces
of constant Schwarzschild time far from the black hole. Such a family of surfaces will
henceforth be designated “nice slices”. While it is seldom spelled out, the existence of
such a set of surfaces is implicitly assumed in much of the existing literature on black hole
evaporation. The ﬁrst explicit construction of nice slices that we are aware of was carried
out by Wald [13].
To construct an example of a family of nice slices, we begin with the Schwarzschild
black hole in Kruskal-Szekeres coordinates, as shown in ﬁg. 1. These coordinates are related
Fig. 2: A family of nice slices.
to the usual Schwarzschild coordinates r and t by the transformation
−UV = 16G2M 2 
r
2GM −1

er/2GM ,
−V/U = et/2GM .
(2.1)
The singularity is at UV = 16G2M 2, and the event horizon is the surface U = 0.
We ﬁrst construct a spacelike surface composed of two pieces joined smoothly at the
surface U = V . The ﬁrst piece is the hyperbola which satisﬁes the condition UV = R2 for
V < U. The constant R is assumed to be large by comparison with any microscopic scale,
but should not be so large that the surface is anywhere near the singularity. Later, we
will choose R to be ﬁxed and send M →∞. The second piece of the nice slice is deﬁned
by the line satisfying U + V = 2R for V > U. The resulting surface is asymptotic to the
surface deﬁned by t = 0.
The nice slice we have constructed can be pushed forward and backward in time by
using the symmetry under the boost-like operations
U →U ′ = Ue−t/4GM ,
V →V ′ = V et/4GM .
(2.2)
Since the nice slices are asymptotic to surfaces of constant Schwarzschild time, they can
be parametrized by t. The full set of nice slices can then be written
UV = R2 ,
V < et/2GMU ,
et/4GMU + e−t/4GMV = 2R ,
V > et/2GMU ,
(2.3)
and is shown in ﬁg. 2. The join between the line segment and the hyperbola on each slice
should be smoothed to avoid having a large extrinsic curvature there.
A Hamiltonian may be deﬁned by introducing a vector ﬁeld v which is orthogonal to
the nice slices. The nice-slice Hamiltonian, HNS, is the generator of motions along this
vector ﬁeld, and maps the state of the system on one slice to a state on a neighboring slice
by means of the Schr¨odinger equation
i∂t|ψ⟩= HNS|ψ⟩.
(2.4)
Since the vector ﬁeld v is not a Killing vector ﬁeld, the Hamiltonian HNS is time dependent,
so there is no conserved nice slice energy. If the mass M of the black hole and the value
of R are very large, however, the rate of change of the nice-slice energy is very small, and
becomes adiabatic as M and R tend to inﬁnity.
The three-momentum of an infalling particle as it crosses a given slice can be deﬁned
by projecting the four-momentum vector onto the slice. It is easily seen that the spatial
momentum of an ordinary particle remains small throughout its entire journey toward
the hyperbola UV = R2.
This is in sharp contrast to the situation in Schwarzschild
coordinates, where the three-momentum of a particle diverges as it approaches the horizon.
The outgoing Hawking quanta also have low momenta as they cross each nice slice.
So far we have been discussing a classical background geometry, but in order to address
the issue of information loss we should include the eﬀect of black hole evaporation. This
introduces an important new feature into the problem. Our nice slices in the static classical
geometry never get closer to the singularity than the hyperbola UV = R2, but when the
semi-classical back-reaction is included the black hole has a ﬁnite lifetime and eventually
the part of a slice that extends into the black hole interior will encounter large curvature.
The best one can do in this case is to construct a family of slices that avoid the region
of strong gravitational coupling for as long as possible. This is not a serious drawback.
If we start with a suﬃciently large black hole then even after 99.99% of the energy has
evaporated the black hole will still be large and a set of nice slices can still be found. By
starting with a suﬃciently large black hole, we can thus follow the evolution long enough
to have most of the total Hawking radiation already emitted, and well separated from the
black hole region, by the time our nice slices run into strong curvature.
It is therefore natural to make the assumption that the entire history of the black hole
(except for the short time when the Hawking temperature exceeds the cutoﬀscale) can
be described by a low-energy eﬀective quantum ﬁeld theory deﬁned on a slowly varying
background geometry.
The cutoﬀlength is chosen suﬃciently large that gravitational
ﬂuctuations can be ignored altogether. We emphasize that no trans-Planckian frequencies
have entered into the discussion. In fact the adiabatic theorem implies that only degrees of
freedom of very low-energy (E ∼1/M) get excited from their ground state in the Hawking
emission process.
The construction seems to leave no room for stringy short distance
behavior, or any other modiﬁcation of ﬁeld theory, to inﬂuence the details of the Hawking
radiation.
The nice-slice argument can be combined with another argument, the “no quantum
Xerox principle” [1], to show that the information carried by infalling matter can not be
stored on the stretched horizon. Consider a late time slice Σ, and partition it into two
portions, Σin and Σout, with Σin containing the region behind the horizon, while Σout
contains the horizon and the region outside the black hole. Since the low-energy nice-
slice theory is a local quantum ﬁeld theory on a time-dependent but classical background
geometry, low-energy ﬁeld operators will commute when their arguments are spacelike
related (as measured by the background metric). This means that we can form a complete
set of commuting observables using local ﬁelds deﬁned on Σin and Σout, and thus the
Hilbert space of states on the slice Σ factorizes into a tensor product
H(Σ) = H(Σin) ⊗H(Σout) .
(2.5)
The evolution operator deﬁnes a linear map from states in the Hilbert space of initial
conﬁgurations of infalling matter to states in H(Σ).
It is now easy to give the argument for information loss. The “no quantum Xerox
principle” states that the process of linear evolution cannot faithfully replicate quantum
information in two separate sets of commuting degrees of freedom. If the infalling informa-
tion is completely and faithfully recorded in the states of H(Σin) (as is widely believed),
then little or no information can be found in the states of H(Σout). This conclusion would
apply to both the Hawking radiation itself and to the stretched horizon.
