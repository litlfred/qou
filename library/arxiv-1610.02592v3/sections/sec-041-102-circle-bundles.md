---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-041-102-circle-bundles
section_title: "Circle bundles"
section_number: 10.2
pages: 318-320
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We now introduce another simple class of 3-manifolds, the orientable circle
bundlesoversomecompactsurface S. Wewilldiscoverthatthereisessentially
only one circle bundle ifS has boundary, and inﬁnitely many ifS is closed,
distinguished by an integer called theEuler number.
10.2.1. Thetrivialcirclebundle. LetS beacompactconnectedsurface.
As every connected manifold, the surfaceS has a unique orientable line bundle
S×I or S×∼ I
depending on whetherS is orientable or not. We denote by
M =S×S1 or S×∼ S1
respectively the double ofS×I and S×∼ I along its boundary. If we do not
know whetherS is orientable or not, we use the symbolsS×
(∼)
I and S×
(∼)
S1
to denote these objects. The manifoldS×
(∼)
S1 is an orientable circle bundle
overS, called thetrivial one.
10.2.2. Circle bundles with boundary.We start by exploring the case
where the base surfaceS has non-empty boundary: in this case every bundle
M over S is a 3-manifold with boundary; the boundary consists of tori, one
ﬁbering above each circle in∂S, because the torus is the unique orientable
surface that ﬁbres overS1.
It turns out that there is essentially only one bundle overS, the trivial one:
Lemma 10.2.1. If ∂S ⁄= ∅, the orientable circle bundles on S are all
isomorphic.
Proof. LetN→S be an orientable circle bundle. DecomposeS as a disc
D with some pairs of disjoint segments(Ii,Ji ) in∂D to be glued. SinceD is
contractible the restriction ofN toD is a productD×S1 andN is obtained
from it by gluing the annuliIi×S1 andJi×S1 via orientation-reversing ﬁbre-
preserving maps. Two such maps are always isotopic (exercise) and henceN
is uniquely determined. □
We now want to study thesections of the trivial bundleM→S, because
these will be useful in the study of bundles over closed surfaces. We now
discover that, although the bundle is trivial, it contains many non isotopic
sections, and we want to classify them.
Recall that asection of the bundleπ :M→S is a mapi :S→M such
thatπ◦i = id. Since the sectioni is determined by its imagei(S), we simply
10.2. CIRCLE BUNDLES 311
A
S
Figure 10.8. A twist along a ﬁbered annulusA modiﬁes a sectionS as shown.
consider the surfacei(S) as a section ofπ. By constructionM is the double
of an interval bundle overS and as such it contains thezero-section S there.
However, this section is not unique in general, not even up to isotopy.
To modify a section, pick a properly embedded arc inS. The arc deter-
mines a ﬁbered annulusA⊂M above it, which we may use totwist the section
as shown in Figure 10.8. This operation modiﬁes the curves∂S ⊂ ∂M via
two Dehn twists (one positive and one negative) on the tori∂M along the two
curves in∂A.
By twisting along annuli we may construct all the sections ofM:
Lemma 10.2.2. Two sections ofS×
(∼)
S1 are connected by a composition
of twists along ﬁbered annuli and ﬁbre-preserving isotopies.
Proof. Leti1,i 2 be two sections. DecomposeS as a 0-handleD with some
rectangular 1-handles attached to∂D. The bundle is trivial on each handle.
SinceD is contractible, every mapi :D→S1 is homotopic to a constant and
we may hence isotopei1 andi2 so that they coincide onD.
See a 1-handle as[−1, 1]2 with{±1}× [−1, 1] glued toD. The sections
i1,i 2 : [−1, 1]2→S1 coincide on{±1}× [−1, 1], and up to reparametrising we
may suppose that they are constantly1 there. The sectioni1 : [−1, 1]2→S1
deﬁnes an elementd∈π1(S1, 1) = Z, determined by the loopt↦→i1(t,u ),
whose homotopy class does not depend on the ﬁxedu∈ [−1, 1]. The section
is in fact determined up to isotopy byd, and by twisting along the annulus
0× [−1, 1] we can vary this integer arbitrarily. Therefore after some twists
and isotopies the sectionsi0 and i1 are both constantly 1 on 1-handles, and
thus coincide everywhere. □
Corollary 10.2.3. If S has only one boundary component, the boundary
of a section ofM = S×
(∼)
S1 is a slope in∂M that does not depend on the
section.
Proof. Distinct sections are connected by ﬁnitely many Dehn twists along
annuli. One such twist acts on the torus∂M as a composition of two opposite
Dehn twists, which cancel each other. Hence it does not aﬀect the boundary
slope of a section. □
