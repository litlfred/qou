---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
1.1. The Palais–Smale condition
A Palais–Smale sequence (or (PS)-sequence) for a continuously differentiable energy function
E on a smooth Banach manifold M, is a sequence (𝑥𝑘)𝑘⊂M such that sup𝑘∈N E(𝑥𝑘) < ∞
and lim𝑘→∞∥DE𝑥𝑘∥(𝑇𝑥𝑘M)∗= 0, where (𝑇𝑥M)∗denotes the dual space of the tangent space
𝑇𝑥M of the manifold M at the point 𝑥∈M.
The energy E is said to satisfy the Palais–Smale condition or (PS)-condition, if every (PS)-
sequence (𝑥𝑘)𝑘⊂M for E contains a convergent subsequence, 𝑥𝑘𝑙→𝑥∞∈M as 𝑙→∞.
The (PS)-condition has been central for the investigation of critical points and of energy
landscapes, with sophisticated tools such as Mountain Pass theorems, Ljusternik-Schnirelman
theory, or Morse-Bott results; see, e.g., the monographs [56], [55], [43], [73], [64, Chapters II
& III], and [35].
In geometric knot theory one considers non-local energies that penalize self-intersections of
geometric objects like curves or surfaces, so called self-avoidance energies or knot energies.
With these functionals one can treat variational problems in spaces of embeddings under
1
arXiv:2505.02719v2  [math.CA]  2 Mar 2026
topological constraints, such as a prescribed knot type. In this way, energy minimizing curves
or Euclidean submanifolds have been found in given ambient isotopy classes. In addition,
bounds on the number of isotopy types under given energy values were established, and
classical knot invariants such as the crossing number or the stick number can be controlled
in terms of knot energies; see the surveys [49, 69, 67, 66, 14, 65] and the many references
therein.
Moreover, critical points were found by symmetric criticality, not only for self-
avoidance energies alone [20, 32, 75], but also for linear combinations of such with the classic
Euler-Bernoulli bending energy
𝐸b(𝛾) ≔1
2
∫
𝛾
𝜅2 d𝑠
(1.1)
for closed curves 𝛾: R/Z →R3, in search of elastic knots [31, 33]. There are long-time
existence results for different kinds of gradient flows for various knot energies, the 𝐿2-gradient
flow [12, 11, 13], and Hilbert or Banach gradient flows [37, 42], as well as 𝐿2-gradient flows
for linear combinations with the bending energy (1.1) in [40, 18]. We should also point out the
substantial advances in the numerical treatment of such problems as in [7, 5, 6, 77, 76, 59].
However, a more sophisticated critical point theory for knot energies has not been developed
yet, partially because of the lack of the (PS)-condition for these non-local energies. With this
paper we want to close this gap for a family of knot energies and for linear combinations of
basically all known differentiable knot energies with the bending energy (1.1).
