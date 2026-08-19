---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 4-7
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
According to the holographic principle all physics is encoded at the boundaries of
spacetime. A good deal is known in the context of AdS/CFT about this encoding as
long as we restrict our attention to the region outside horizons. Very much less is known
about the holographic encoding of physics behind black hole horizons. The purpose
of this paper is to explore a proposal for how properties of the black hole interior are
represented on the holographic boundary. We propose that the quantum complexity of
the boundary state is equal to the classical action of a spacetime region that extends
deep inside the horizon. This region—which we call the Wheeler-DeWitt patch—is
deﬁned as the bulk domain of dependence of a bulk Cauchy slice anchored at the
boundary state. For the case of one- and two-sided black holes in Anti-de Sitter space,
the geometry is shown in Fig. 1. Quantum complexity C is the minimum number
of elementary operations (quantum gates) needed to produce the boundary state of
interest from a reference state. Calling the action of the Wheeler-DeWitt patch A, our
proposal is [1]
C = A
πℏ. (1.1)
Quantum complexity entered black hole physics to help quantify the diﬃculty of
decoding Hawking radiation [2], but it appears to also shed light on physics behind
the horizon. It was observed that black hole interiors grow in time long after local
equilibrium is reached [3]. The complexity of the plasma dual to the black hole is also
expected to increase long after local thermal equilibrium is reached, so it was proposed
that the two growths are dual descriptions of the same phenomenon [4, 5]. In this
paper we will characterize the size of the black hole interior by its action. This action
conjecture subsumes a previous conjecture [6] that characterized the size of the black
hole interior by its spatial volume.
The original complexity/volume or “CV” duality [6] stated that the complexity of
the boundary state is proportional to the spatial volume V of a maximal slice behind
the horizon,
C∼ V
G𝓁, (1.2)
where 𝓁 is a length scale that has to be chosen appropriately for the conﬁguration
(typically either the AdS radius or the radius of the black hole).
CV-duality had a number of nice features. The maximal volume slice is a rela-
tively robust geometric object that naturally grows at a rate roughly proportional to
the temperature T times the entropy S of the black hole. CV-duality works because
TS provides a rough estimate for the rate of complexiﬁcation of a strongly coupled
conformal plasma. Shock wave geometries dual to the insertion of a simple operator
3
tRtL
tRtL
r=0
r=0
r=1
r=1
tL
 tR
 r=0
r=1
 r=0
t
t
t
infallingshockwave
maximal slice for CV (old)
WdW patchfor CA (new)
Figure 1: The Penrose diagrams for two-sided eternal black holes (left) and one-sided
black holes that form from collapsing shock waves (right). The two-sided black hole is
dual to an entangled state of two CFTs that live on the left and right boundaries; the
one-sided black hole is dual to a single CFT. The (old) complexity/volume conjecture
related the complexity of the entangled CFT state to the volume of the maximal spatial
slice anchored at the CFT state. Our (new) complexity/action conjecture relates the
complexity of the CFT state to the action of the Wheeler-DeWitt patch.
4
in the distant past provide additional tests of CV-duality. For these shock wave ge-
ometries it was found that the maximal volume slice had cancellations that precisely
match cancellations expected in the complexity [6–8]. Finally, various tensor network
constructions qualitatively agreed with the holographic results [6, 7]. (For additional
work on the CV-duality, see also [9–11].)
However, CV-duality has a number of unsatisfactory elements. First we must choose
by hand a length scale 𝓁, depending on the situation. Further, it is also not clear why
the maximal volume slice should play a preferred role. The conjecture that complexity
equals action (“CA-duality”) inherits all the nice features of CV-duality and none of
the unsatisfactory elements.
One virtue of CA-duality is that it associates with the boundary state the entire
Wheeler-DeWitt patch, and doesn’t single out a special spacelike slice. Another virtue
is that it is not necessary to introduce an arbitrary length scale; as a consequence,
the prefactor of the complexity could potentially have physical meaning. CA-duality
reproduces the results of CV-duality for small and large AdS black holes without the
need to choose diﬀerent lengths in the two cases. Once the constant in Eq. 1.1 has been
ﬁxed by considering any particular black hole, the conjecture then makes unambiguous
predictions with no further free parameters for black holes of any size, for black holes in
any number of dimensions, for black holes that are charged or rotating, and for states
that are not black holes. The CA-duality passes all the same shock wave tests as were
passed by CV-duality.
We work in the context of AdS/CFT and assume a familiarity with those notions;
we also assume familiarity with notions of quantum information including quantum
circuits, see e.g. [12,13]. CA-duality is a quantum-classical duality, insofar as it relates
a highly quantum theory on the boundary (where the complexity is deﬁned) to a highly
classical theory in the bulk (where the action is deﬁned). In order to use CA-duality we
will need to identify a set of weakly interacting semiclassical bulk degrees of freedom,
to consider states that are semiclassical with respect to those degrees of freedom, and
to assume the existence of a unique real-valued semiclassical eﬀective action for those
degrees of freedom. In this paper we will generally be considering semiclassical bulk
states of the Einstein-Maxwell system. When studying states with growing complexity
we will always restrict to times less than O(eS). Beyond this time the complexity
is expected to saturate and ﬂuctuate (and eventually decrease at times of order the
quantum recurrence time O(eeS
)).
The paper is structured as follows:
In§1.1 we more precisely deﬁne our conjecture.
In§2 we review bounds on information processing and conjecture that black holes
5
are the fastest computers in nature.
In§3 we examine a number of diﬀerent types of black holes and compute the growth
of the action of the Wheeler-DeWitt (WDW) patch with time.
In§4 we use our conjecture to compare the rate of growth of action of black holes
with a conjectured quantum mechanical bound on complexity growth inspired by a
conjectured bound of Lloyd’s [14]. We ﬁnd precise agreement for uncharged and ro-
tating black holes. For charged black holes, the situation appears more complicated,
but these complications result from dynamical issues associated with the production
of hair, and we have no controlled examples that violate our bound.
In§5 we test our conjectures with an analysis of black holes surrounded by static
shells of inert matter. We ﬁnd our conjectures pass.
In§6 we test our conjectures with an analysis of black holes perturbed by shock
waves. We show that CA-duality passes this test, for much the same reason that
CV-duality did. We ﬁnd that the geometry of the Einstein-Rosen bridge of shock
wave states matches the geometry of the minimal tensor network that describes such
products of precursors. In general, the CA-calculations turn out to be signiﬁcantly
simpler than the CV calculations. We also discuss complexity growth with ﬁnite-energy
perturbations.
In§7 we will provide a tensor network computation of complexiﬁcation. Using
tensor network renormalization group techniques, we will show that the growth of
complexity is independent of the UV cutoﬀ.
In§8 we review the main implications of CA-duality presented in this work, com-
ment on a number of extensions and puzzles raised by our work, and discuss some open
questions.
