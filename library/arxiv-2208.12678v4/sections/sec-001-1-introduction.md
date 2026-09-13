---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THEM ÖBIUS-PLATEAU ENERGY"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
---
The problem of finding a surface of minimal area bounded by a fixed closed curve, also known as Plateau’s
problem, has captivated mathematicians for over two centuries. A relevant extension to this problem is when
the boundary possesses its own energy and is allowed to deform. Since most experimental realizations of
Plateau’s problem involve films formed by dipping closed loops of wire in soapy water, it is natural to consider
boundary curves with elastic energy, defined as the integral of squared curvature. This problem, known now
as the Euler-Plateau problem has received considerable attention in recent years [BY01, GM12, GPT21,
CF14]. In [BY01], the authors prove the existence of loop configurations that minimize a combination
of the elastic energy of curves with preferred curvature and the area of a minimal surface spanning the
curve. However, they require strong assumptions to avoid self-contact of the boundary curve during energy
minimization. The paper [GLF17] models the boundary curve as a Kirchhoff rod and find minimizers whose
boundary curves can touch without interpenetration of matter.
In view of this, we propose an interesting variation on the above theme— minimal surfaces bounded by
self-repulsive curves. Competition between the self-repulsive force trying to enlarge the bounding curve and
surface tension of the spanning surface trying to shrink it leads to interesting physics in this problem. Knots
charged with regularized Coulomb-like self-interaction energies were considered originally by O’Hara [O’H91,
O’H92, O’H03] and studied extensively in [FHW94]. In particular, it is shown in [FHW94] that this energy
is M¨ obius invariant, and is hence referred to as the M¨ obiusenergy. Furthermore, [FHW94] establishes the
existence of loops minimizing the M¨ obius energy in fixed irreducible knot classes. In this work, we consider an
energy that combines the M¨ obius self-repulsive energy of a closed loop and the area of a minimal disk spanning
that loop and prove the existence of minimizing configurations for this energy. We apply well-known results
on M¨ obius minimizers stated in [FHW94], but lower semicontnuity of the Plateau energy, while assumed
in the Euler-Plateau literature (e.g. [BY01]), does not have a written proof to the authors’ knowledge.
One might be misled into believing that the sequence of Plateau solutions associated to a given uniformly
convergent sequence of boundary curves also converges, but even when the solutions catastrophically jump
when passing to the limit, the area is still lower semicontinuous, masking the catastrophe.
And so, even though minimizers of the M¨ obius-Plateau energy exist, the competition between the two
constituent energies can complicate the critical points themselves. We then turn our attention to the cor-
responding Euler-Lagrange equations and explore an example of this phenomenon, even though our prior
existence result does not apply. In particular, we consider helicoidal strips— regions bounded between two
helices on a common helicoid as candidate solutions. These configurations can be classified as helicoidal
screws or ribbons depending on the signs of the radii of the bounding helices. By working directly with the
oscillatory variational integrals to derive nontrivial necessary conditions, we will see that while screw-like
1
arXiv:2208.12678v4  [math.DG]  9 Mar 2025
2 MAX LIPTON AND GOKUL G. NAIR
critical points are abundant, ribbon-like solutions are strongly constrained: they must have high-frequency
(low pitch), thin width and remain close to the axis. Many of the calculations in this section were performed
with the assistance of a computer algebra system for the sake of practicality.
The outline of this paper is as follows: In Section 2 we recall the definition and properties of the M¨ obius
energy and formulate the M¨ obius-Plateau energy minimization problem. In Section 3, we show compactness
properties and lower semicontinuity of the energy and establish the existence of disk-like energy minimizing
configurations for simple closed curves in a given irreducible knot type. In Section 4 we turn our attention
to helicoidal solutions of the Euler-Lagrange equations.
