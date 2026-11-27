---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-6
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
The AdS/CFT correspondence provides an important laborato ry to explore both gravita-
tional physics as well as strongly coupled dynamics in a clas s of quantum ﬁeld theories.
Using this correspondence it is possible to test general lor e about quantum ﬁeld theory in
a non perturbative setting and so learn general lessons abou t strongly coupled dynamics.
Conversely, it is also possible to use the AdS/CFT duality to convert strongly held convic-
tions about the behaviour of quantum ﬁeld theories into gene ral lessons about gravitational
and stringy dynamics.
In this paper we use the AdS/CFT correspondence to study the e ﬀective description
of strongly coupled conformal ﬁeld theories at long wavelen gths. On physical grounds it
is reasonable that any interacting quantum ﬁeld theory equi librates locally at high enough
energy densities, and so admits an eﬀective description in t erms of ﬂuid dynamics. The
variables of such a description are the local densities of al l conserved charges together with
the local ﬂuid velocities. The equations of ﬂuid dynamics ar e simply the equations of local
conservation of the corresponding charge currents, supple mented by constitutive relations
that express these currents as functions of ﬂuid mechanical variables. As ﬂuid dynamics
is a long wavelength eﬀective theory, these constitutive re lations are usually speciﬁed in a
derivative expansion. At any given order, thermodynamics p lus symmetries determine the
form of this expansion up to a ﬁnite number of undetermined co eﬃcients. These coeﬃcients
may then be obtained either from measurements or from micros copic computations.
The best understood examples of the AdS/CFT correspondence relate the strongly
coupled dynamics of certain conformal ﬁeld theories to the d ynamics of gravitational sys-
tems in AdS spaces. In this paper we will demonstrate that Ein stein’s equations with
a negative cosmological constant, supplemented with appro priate regularity restrictions
and boundary conditions, reduce to the nonlinear equations of ﬂuid dynamics in an ap-
propriate regime of parameters. We provide a systematic fra mework to construct this
universal nonlinear ﬂuid dynamics, order by order in a bound ary derivative expansion.
Our work builds on earlier derivations of linearized ﬂuid dy namics from linearized gravity
by Policastro, Son and Starinets [1] and on earlier examples of the duality between non-
linear ﬂuid dynamics and gravity by Janik, some of the curren t authors and collaborators
[2, 3, 4, 5] ( cf, [6, 7, 8, 9, 10, 11] for related work and extensions and [12, 1 3] for some recent
work). There is a large literature in deriving linearized hy drodynamics from AdS/CFT,
see [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 , 30, 31] for developments in
this area and [32] for a review and comprehensive set of refer ences.
Our results, together with those of earlier papers referred to above, may be interpreted
from several points of view. First, one may view them as a conﬁ rmation that ﬂuid dy-
namics is the correct long wavelength eﬀective description of strongly coupled ﬁeld theory
dynamics. Second, one could assume the correctness of the ﬂu id description and view our
results as providing information on the allowed singularit ies of ‘legal’ solutions of gravity.
Finally, our work may be used to extract the values of all coeﬃ cients of the various terms
in the expansion of the stress tensor in the ﬂuid dynamical de rivative expansion, for the
ﬂuid dual to gravity on AdS 5. The universal behaviour of the shear viscosity - a coeﬃcien t
of a term in the expansion of the stress tensor to ﬁrst order in ﬁeld theory derivatives - in
ﬂuids dual to gravity [24] has already attracted attention a nd has impacted experimental
analysis of RHIC data [33, 34, 35]. In this paper we work out th e universal values of all
coeﬃcients of (nonlinear) two derivative terms stress tens or of the distinguished conformal
ﬂuid dual to gravity on AdS 5.
Consider any two derivative theory of ﬁve dimensional gravi ty interacting with other
ﬁelds, that has AdS 5 as a solution. Examples of such theories include IIB supergr avity
on AdS 5 ×M where M is any compact ﬁve dimensional Einstein manifold with posit ive
cosmological constant; for example M = S5, T 1, 1 and Y p,q for all p, q. The solution space
of such systems has a universal sub-sector; the solutions of pure gravity with a negative
cosmological constant. 1 We will focus on this universal sub-sector in a particular lo ng
wavelength limit. Speciﬁcally, we study all solutions that tubewise2 approximate black
branes in AdS 5, whose temperature and boost velocities vary as a function o f boundary
coordinates xµ on a length scale that is large compared to the inverse temper ature of the
brane. We investigate all such solutions order by order in a p erturbative expansion; the
perturbation parameter is the length scale of boundary vari ation divided by the thermal
length scale. Within the domain of validity of our perturbat ive procedure (and subject
to a technical assumption), we establish the existence of a o ne to one map between these
gravitational solutions and the solutions of the equations of a distinguished system of
boundary conformal ﬂuid dynamics. Implementing our pertur bative procedure to second
order, we explicitly construct the ﬂuid dynamical stress te nsor of this distinguished ﬂuid
to second order in the derivative expansion.
Roughly speaking, our construction may be regarded as the ‘C hiral Lagrangian’ for
brane horizons. Recall that the isometry group of AdS 5 is SO(4, 2). The Poincare algebra
plus dilatations form a distinguished subalgebra of this gr oup; one that acts mildly on
the boundary. The rotations SO(3) and translations R3, 1 that belong to this subalgebra
annihilate the static black brane solution in AdS 5. However the remaining symmetry gen-
1Recall that the Einstein frame Lagrangian contains no inter action terms that are linear in the non
gravitational ﬂuctuations.
2We will work in AdS spacetimes where the radial coordinate r ∈ (0, ∞) and will refer to the remaining
coordinates xµ = (v, x i) ∈ R1, 3 as ﬁeld theory or boundary coordinates. The tubes referred t o in the text
cover a small patch in ﬁeld theory directions, but include al l values of r well separated from the black
brane singularity at r = 0; typically r ≥ rh where rh is the scale set by the putative horizon.
erators – dilatations and boosts – act nontrivially on this b rane, generating a 4 parameter
set of brane solutions. These four parameters are simply the temperature and the velocity
of the brane. Our construction eﬀectively promotes these pa rameters to ‘Goldstone ﬁelds’
(or perhaps more accurately collective coordinate ﬁelds) a nd determines the eﬀective dy-
namics of these collective coordinate ﬁelds, order by order in the derivative expansion, but
making no assumption about amplitudes. Of course the collec tive coordinates method has
a distinguished tradition in theoretic physics; see for ins tance the derivation of the Nambu-
Goto action in [36]. Our paper, which applies these methods t o black brane horizons, is
strongly reminiscent of the membrane paradigm of black hole physics, and may perhaps be
regarded as the precise version of this paradigm in its natur al setting, i.e., AdS spacetime.
Seen from inverse point of view, our construction may be rega rded as a map from
solutions of the relativistic ﬂuid dynamics equations on R3, 1 to the space of long wavelength,
locally black brane, solutions of gravity in AdS 5. That is, we present a systematic procedure
to explicitly construct a metric dual to any solution of the e quations of the distinguished
ﬂuid dynamics alluded to above. This metric solves the Einst ein’s equations to a given
order in the derivative expansion (one higher than the order to which the equations of ﬂuid
dynamics were formulated and solved), asymptotes to AdS 5 with a boundary stress tensor
equal to the ﬂuid dynamical stress tensor, and is regular awa y from the usual singularity
of black branes (chosen by convention to be at r = 0).
As an important physical input into our procedure, we follow [3, 7, 10] to demand
that all the solutions we study are regular away from the r = 0 curvature singularity of
black branes, and in particular at the the location of the hor izon of the black brane tubes
out of which our solution is constructed. We present our cons truction in the analogue
of Eddington-Finklestein coordinates which extend all the way to the future curvature
singularity. Although we have not yet performed a careful gl obal analysis of our solutions, it
seems rather clear that they each possess a regular event hor izon that shields the boundary
from this curvature singularity.
This paper is organized as follows. We begin in § 2 with the basic outline of the
computation expanding on the ideas presented above. In § 3 we outline in detail the logic
and strategy of our perturbative procedure. We then proceed in § 4 to implement our
perturbative procedure to ﬁrst order in the derivative expa nsion. In § 5 we extend our
computation to second order in the same expansion. In § 6 we demonstrate the Weyl
invariance of the ﬂuid dynamical stress tensor we obtain, an d further use this stress tensor
to compute corrections to the dispersion relation for sound and shear waves in this ﬂuid.
In § 7 we end with a discussion of our results and of future directi ons.
Note added: After we had completed writing this paper we learnt of relate d work soon
to appear [37]. The authors of this paper utilize Weyl invari ance to constrain the form of
the second order ﬂuid dynamical stress tensor up to 5 undeter mined coeﬃcients. They then
use information from linearized gravitational quasinorma l mode calculations together with
an earlier computation of Janik and collaborators to determ ine 3 of these ﬁve coeﬃcients.
As far as we have been able to tell, their results are consiste nt with the full second order
stress tensor (and prediction for quasinormal mode frequen cies) presented herein. This is a
nontrivial check of our results. We thank the authors of [37] for sharing their results with
us prior to publication.
Note added in v2: The preprint [37] appeared simultaneously in an arXiv listi ng with v1
of this paper. In § 6.3 of this updated version of our preprint we have presented a detailed
comparison of our results with those of [37]; where they over lap we ﬁnd perfect agreement.
