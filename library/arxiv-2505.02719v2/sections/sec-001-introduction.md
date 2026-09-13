---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais–Smale condition in geometric knot theory"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
---
1.1. The Palais–Smale condition
APalais–Smalesequence(or(PS)-sequence)foracontinuouslydifferentiableenergyfunction
Eon a smooth Banach manifoldM, is a sequence(𝑥𝑘)𝑘⊂Msuch thatsup 𝑘∈NE(𝑥𝑘)<∞
andlim 𝑘→∞∥DE 𝑥𝑘∥(𝑇𝑥𝑘M)∗ =0, where(𝑇 𝑥M)∗ denotes the dual space of the tangent space
𝑇𝑥Mof the manifoldMat the point𝑥∈M.
The energyEis said to satisfy thePalais–Smale conditionor (PS)-condition, if every (PS)-
sequence(𝑥 𝑘)𝑘⊂MforEcontains a convergent subsequence,𝑥 𝑘𝑙→𝑥∞∈Mas𝑙→∞.
The (PS)-condition has been central for the investigation of critical points and of energy
landscapes, with sophisticated tools such as Mountain Pass theorems, Ljusternik-Schnirelman
theory, or Morse-Bott results; see, e.g., the monographs [56], [55], [43], [73], [64, Chapters II
& III], and [35].
Ingeometricknottheoryoneconsidersnon-localenergiesthatpenalizeself-intersectionsof
geometric objects like curves or surfaces, so calledself-avoidance energiesorknot energies.
With these functionals one can treat variational problems in spaces of embeddings under
1
arXiv:2505.02719v2  [math.CA]  2 Mar 2026
topological constraints, such as a prescribed knot type. In this way, energy minimizing curves
or Euclidean submanifolds have been found in given ambient isotopy classes. In addition,
bounds on the number of isotopy types under given energy values were established, and
classical knot invariants such as the crossing number or the stick number can be controlled
in terms of knot energies; see the surveys [49, 69, 67, 66, 14, 65] and the many references
therein. Moreover, critical points were found by symmetric criticality, not only for self-
avoidanceenergiesalone[20,32,75],butalsoforlinearcombinationsofsuchwiththeclassic
Euler-Bernoulli bending energy
𝐸b(𝛾)≔ 1
2
∫
𝛾
𝜅2 d𝑠(1.1)
for closed curves𝛾:R/Z→R 3, in search ofelastic knots[31, 33]. There are long-time
existenceresultsfordifferentkindsofgradientflowsforvariousknotenergies,the𝐿 2-gradient
flow [12, 11, 13], and Hilbert or Banach gradient flows [37, 42], as well as𝐿2-gradient flows
forlinearcombinationswiththebendingenergy(1.1)in[40,18]. Weshouldalsopointoutthe
substantial advances in the numerical treatment of such problems as in [7, 5, 6, 77, 76, 59].
However,amoresophisticatedcriticalpointtheoryforknotenergieshasnotbeendeveloped
yet, partially because of the lack of the (PS)-condition for these non-local energies. With this
paper we want to close this gap for a family of knot energies and for linear combinations of
basically all known differentiable knot energies with the bending energy (1.1).
