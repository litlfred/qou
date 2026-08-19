---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-001-11-complexity-equals-action
section_title: "Complexity equals action"
section_number: 1.1
pages: 7-9
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Here we deﬁne CA-duality within the context of holographic duality. The setup of
CA-duality and the relationship between CV-duality and CA-duality is illustrated in
Fig. 1. Choosing times tL,tR on the left and right AdS boundaries of the eternal
AdS-Schwarzschild black hole determines a state|ψ(tL,tR)⟩,
|ψ(tL,tR)⟩ =e−i(HLtL+HRtR)|TFD⟩, (1.3)
where|TFD⟩ = Z−1/2∑
αe−βEα
2 |Eα⟩L|Eα⟩R is the thermoﬁeld double (TFD) state
which puriﬁes the thermal state of one side. 1
1Note that with our conventions, time on both sides of Fig. 1 increases upwards.
6
CV-duality proposes that the complexity of|ψ(tL,tR)⟩ is computed from the volume
V of a (D− 1)-dimensional maximal volume slice anchored at tL and tR,
C(|ψ(tL,tR)⟩)∼ V (tL,tR)
G𝓁 , (1.4)
where G is Newton’s constant and 𝓁 is another length scale (the AdS radius for large
black holes and the Schwarzschild radius for small black holes). This yields a complexity
which grows linearly with time and is proportional to temperature T and entropyS, a
result that roughly matches CFT expectations.
The prescription Eq. 1.4 has a degree of arbitrariness. First of all the choice of
foliation by maximal slices is not unique. Moreover these slices do not foliate the
entire geometry behind the horizon. Another unattractive feature is the introduction
of the length scale𝓁 which varies from case to case. The proposal of this paper remedies
these unsatisfactory elements while retaining all the beneﬁts of CV-duality.
To motivate the CA proposal we note that the geometry of the D-dimensional
world volumeW behind the horizon is roughly that of a D-dimensional tube of length
tL + tR. The ( D-1)-dimensional cross section of the tube has spatial area GS and
time duration ∼ 𝓁AdS. The world volume of the tube is deﬁned to be |W|. Since
V (tL,tR)∼GS(tL +tR) the volume formula may be expressed as
V (tL,tR)
G𝓁AdS
∼|W(tL,tR)|
G𝓁2
AdS
. (1.5)
Since the cosmological constant Λ is proportional to −1/𝓁2
AdS, the second expression
is roughly the classical action of the world volume W. This clue leads to CA-duality
which we now deﬁne.
Consider again the eternal black hole geometry (the extension to other geometries
is straightforward) and pick times tL and tR. Deﬁne the Wheeler-DeWitt (WDW)
patchW(tL,tR) to be the union of all spacelike surfaces anchored at tL and tR. The
WDW patch is equivalent to the spacetime region sandwiched between forward and
backward light rays sent from the boundary at tL and tR. W is also the spacetime
region determined by the data on the maximal slice (or any other spacelike slice within
W) and is naturally associated with the boundary state, e.g. [15]. Note that W is not
a causal patch so no single observer is able to monitor all of W; this is consistent with
the complexity not being a conventional quantum mechanical observable.
LetAW be the action obtained by integrating the bulk Lagrangian over W and
including suitable boundary terms on ∂W (see§3). The complexity C (deﬁned more
fully just below) is roughly the minimum number of gates from a universal set necessary
7
to produce the state of interest from a simple state. CA-duality states that
C(|ψ(tL,tR)⟩) =AW
πℏ . (1.6)
The factor of π is arbitrarily chosen so that an increase of complexity by one unit
advances the phase of eiAW/ℏ from one to minus one. At present we do not assign a
physical meaning to this factor of π, it is only a convention to normalize the complex-
ity. We speculate in Appendix A that there is a more universal continuum version of
complexity where the prefactor can be unambiguously deﬁned.
