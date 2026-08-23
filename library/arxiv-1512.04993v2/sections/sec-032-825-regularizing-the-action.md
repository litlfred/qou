---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-032-825-regularizing-the-action
section_title: "Regularizing the action"
section_number: 8.2.5
pages: 51-52
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
In this paper we have calculated the rate of growth of action of the WDW patch at
late times. If we wish to calculate the rate of growth at ﬁnite times we must introduce
a method of regularizing divergences, for example those that occur at the boundary of
AdS. A divergence of this type shows up in the part of the WDW patch that lies behind
the past horizon. The corner term at the bottom, which consists of the intersection of
two lights heets, is divergent.17
Let us take for example the BTZ black hole. One way of regulating the action using
timelike radial geodesics leads to the formula
dA
dt = r2
h
4G𝓁2
AdS
(
tanh2(πt/β) + log (cosh(πt/β))
cosh2(πt/β) − logϵ
cosh2(πt/β)
)
+O(ϵ), (8.4)
wheret≡tL+tR andϵ is an ultraviolet regulator. There are three terms in parentheses.
The ﬁrst term tends to the constant late-time growth rate from Sec. 3.1. This correctly
gives the linear growth that has been the subject of this paper and is robust against
changes in the cutoﬀ prescription. The second term is a UV-ﬁnite transient, which dies
away exponentially fast. The third term is more problematic. While it exponentially
decreases with time, it is logarithmically UV divergent.
A UV-divergent complexiﬁcation rate violates the bound of Eq. 2.14, and mixes IR
and UV dependence in an anomalous way. We do not understand the physics of this
term. It seems likely there is an improved regulator that removes the divergence. This
16In some cases, we can quantitatively think of complexity as the integral of the “size” of an
operator over time [7], where the growth of the operator is a manifestation of the system scrambling.
An example of this is given by the operator shown in Fig. 14.
17We thank Henry Maxﬁeld for helpful discussions that prompted us to revisit this issue.
50
UV divergence is tied up with the issue of the complexity of formation (the complexity
already present at tL =tR = 0) and we intend to address this question in [41].
Because there is no corner, this issue does not arise for either one-sided black holes
or geometries with a wide Penrose diagram, e.g. wormholes lengthened by multiple
shock waves. So while a subtlety with the regulator does occur for the action growth
of unperturbed eternal black holes, these black holes are dual to rather special states
of the conformal ﬁeld theory. For many other states, such as those dual to black holes
formed by collapse or wormholes perturbed by multiple strong shock waves, CA-duality
gives a robust regulator-independent characterization of the growth of complexity.
