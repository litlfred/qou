---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-001-4-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 4
pages: 4-6
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
2.1.Knot invariants from closed braids and traces.There are two main constructions of
quantum knot invariants from YBOs: one is through braid group representations and their trace
maps that are invariant under Markov moves, and the other is by fixing a height function on
the plane of projection and incorporate maps corresponding to maxima/minima of knot diagrams.
Although these two approaches are closely related, we examine these approaches separately to
take advantages of computations of known invariants and their deformations. In this subsection we
review the first approach of trace, and in the next subsection we review the second maxima/minima
approach.
Recall [20] that anenhanced YBO(EYBO) is a quadrupleS= (R,α,β,µ) consisting of a YBO
R, two invertible scalarsα,β∈k ×, and a linear mapµ:V−→Vsatisfying the following two
compatibility conditions
(µ⊗µ)R=R(µ⊗µ),(1)
Tr2(R±(µ⊗µ)) =α ±βµ,(2)
where Tr2 indicates the partial trace of an operator with respect to its second tensorand. To shorten
notation, in this article we also indicate an EYBO simply byR, when no risk of confusion arises.
Observe that whenµis invertible, Equation (2) is equivalent to
Tr2(R±(1⊗µ)) =α ±β1,(3)
where1denotes the identity mapping. Using EYBOs, Turaev [20] gave a definition of quantum
invariants of knots and links as follows. LetB m denote them-string braid group, whose elements
are represented by vertical string diagrams with crossings. A knot or a linkKis represented as
a closed braid form (Alexander’s theorem), where the closure is to connect the top and bottom
end points of a braid by parallel nested circular arcs to the right. Letb m∈B m denote a braid
whose closure representsK. Diagrams in closed braid form are oriented downwards on the braid
portion unless otherwise stated. Letw(b m) denote the writhe ofb m, that is the number of positive
crossings (positive braid generators) minus the negative ones. For an EYBOS= (R,α,β,µ), a
knot invariantT S(K) is defined by
TS(K) =α w(bm)β−m Tr(bmµ⊗m).(4)
The well definedness is proved by showing its invariance under Markov moves, that are conjuga-
tions and (de)stabilizations.
2.2.Knot invariants using maxima/minima.In this section we review a construction of knot
invariants using maxima/minima of knot diagrams with a fixed height function (see, for example,
[13]). This approach is used for unoriented knots and their diagrams.
A pairing∪:V⊗V→kand a copairing∩:k→V⊗Vin a moduleVover a unital ringkare
said to have (or satisfy) theswitchback propertyif they satisfy the equalities
(∪⊗1)(1⊗∩) =1= (1⊗∪)(∩⊗1).
LetRbe a YBO. A pairing∪is said to satisfy (or have) thepasscupproperty with respect toR
if it satisfies
(1⊗∪)(R⊗1) = (∪⊗1)(1⊗R −1),
(1⊗∪)(R −1⊗1) = (∪⊗1)(1⊗R).
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 5
Similarly a copairing∩is said to satisfy (or have) thepasscapproperty with respect toRif it
satisfies
(R⊗1)(1⊗∩) = (1⊗R −1)(∩⊗1),
(R−1⊗1)(1⊗∩) = (1⊗R)(∩⊗1).
In Figure 2, the switchback, passcup and passcap moves are depicted from left to right, respectively.
Figure 2
Ak-moduleVwith a YBO and a pairing and copairing that satisfy switchback, passcup, and
passcap properties provide a knot invariant up to regular isotopy equivalence relation without type
I Reidemeister move, see [13], by interpreting a given knot diagram as a linear map fromktok,
corresponding to empty to empty strings, and the linear map is a constant multiple, which defines
a desired knot invariant. See for example, [13]. If in addition the equation∪R=∪andR∩=∩
are satisfied, this procedure provides a knot invariant up to isotopy. Alternatively, one examines
the effect of type I Reidemeister move to the regular isotopy invariant, and makes a normalization
by the writhe of a given diagram when oriented.
3.Yang-Baxter cohomology
In this section we introduce a YB cohomology theory which differs in defining formulas from the
ones studied in [6, 7, 14, 17]. In particular, the main difference from [6, 7] lies in the fact that the
inverse of the YB operator is not used, and it can therefore be defined for pre-YB operators (i.e.
not necessarily invertible solutions to the YBE).
3.1.YB cohomology in low dimensions.In this subsection we review YB cohomology theory
from [18] in low dimensions, as it is used in the several sections that follow.
The cochain groups are defined byC 0
YB(V,V) = 0 andC n
YB(V,V) = Hom(V ⊗n,V ⊗n) forn>0.
We define the differentials forf∈C 1
YB(V,V) andϕ∈C 2
YB(V,V) by
δ1
YB(f) =R(f⊗1) +R(1⊗f)−(f⊗1)R−(1⊗f)R,
δ2
YB(ϕ) = (R⊗1)(1⊗R)(ϕ⊗1) + (R⊗1)(1⊗ϕ)(R⊗1) + (ϕ⊗1)(1⊗R)(R⊗1)
−(1⊗R)(R⊗1)(1⊗ϕ)−(1⊗R)(ϕ⊗1)(1⊗R)−(1⊗ϕ)(R⊗1)(1⊗R).
When the YBORneeds to be specified, we also use the notationδ n
R forδ n
YB. The fact that these
define homology theory is proved in the next section. The corresponding cocycle, coboundary,
homology groups are denoted as usual usingZ,B,H, respectively.
Figure 3
