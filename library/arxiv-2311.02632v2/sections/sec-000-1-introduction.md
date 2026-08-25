---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In 1893, Hurwitz proved that a compact Riemann surface X of genus g≥ 2 has at
most 84(g− 1) conformal automorphisms [Hur93]. This upper bound is now known as
the Hurwitz bound, and a Riemann surface attaining this bound is called a Hurwitz
surface.
Notably, for Riemann surfaces of low genera, those meeting the Hurwitz bound are
rare. One prominent example is the Klein quartic [Kle79], described by the equation
x3
0x1 +x3
1x2 +x3
2x0 = 0,
in complex projective space. The Klein quartic predates Hurwitz’s seminal work and
stands as the first of its kind to have ever been discovered. This surface possesses
168 conformal automorphisms, with its automorphism group being isomorphic to the
simple group PSL2(7). For a comprehensive exploration of the history and significance
of Klein’s quartic, as well as the subsequent advancements inspired by it, one can refer
to [Lev99].
In 1899, Fricke made a significant contribution to the subject by unveiling another
Hurwitz surface, particularly one of genus 7 [Fri99]. This surface possesses the auto-
morphism group PSL2(8), a simple group of order 504. Subsequently, in 1965, without
being aware of Fricke’s earlier work, Macbeath determined its algebraic model [Mac65].
This surface is now known as the Fricke-Macbeath surface, and alongside the Klein
Date: December 19, 2023.
1
arXiv:2311.02632v2  [math.RT]  17 Dec 2023
2 CHUL-HEE LEE
quartic, it holds the distinction of being one of the only two instances of Hurwitz sur-
faces with genera less than 14. Interestingly, in the case of genus 14, there exist three
distinct Hurwitz surfaces with the same automorphism group of order 1092.
The abundant symmetries inherent in Hurwitz surfaces facilitates intriguing interac-
tions with various structures associated with a surface, making their study compelling.
This interplay makes Hurwitz surfaces a fertile ground for researchers across diverse
fields. Notably, in the realm of arithmetic, some of these surfaces hold significant
recognition as Shimura curves, a fact highlighted by Shimura [Shi67]. Their connec-
tion with Galois theory is also a subject of discussion in Serre’s enlightening letter to
Abhyankar [Ser94]. For their role in the theory of dessins d’enfants, see the book by
Jones and Wolfart [JW16].
In this paper, we explore the interaction between symmetries and the spectral prop-
erties of such a surface. According to the uniformization theorem, X is conformally
equivalent to Γ\H, where H is the upper half-plane in the complex plane and Γ is
discrete, torsion-free subgroup of PSL 2(R). Then Aut( X)∼= N(Γ)/Γ, where N is the
normalizer of Γ in PSL 2(R). In particular, X is a Hurwitz surface when N(Γ) is the
(2, 3, 7)-triangle group. Now X admits a hyperbolic metric, namely, the Riemannian
metric of constant Gaussian curvature -1. The elements of Aut( X) act as orientation-
preserving isometries of X = Γ\H. The Laplacian ∆ for X has non-negative discrete
eigenvalues
0 =λ0 <λ 1≤λ2≤... →∞.
An interesting feature of a Riemann surface with many automorphisms is that each
eigenspace of the Laplacian can exhibit high multiplicities, as each of these eigenspaces
of the Laplacian serves as a representation of Aut( X).
There are only a few known cases of Riemann surfaces with non-trivial automorphism
groups for which we have established values for the multiplicitiesm1 ofλ1. To the best
of our knowledge, the Bolza surface and the Klein quartic are the only known cases. The
Bolza surface, despite not meeting the Hurwitz bound, is a genus 2 Riemann surface
renowned for having the highest number of conformal symmetries, totaling 48, within
its genus. In a study by Jenni [Jen84], it was asserted thatm1 = 3 for the Bolza surface;
however, Cook [Coo18] identified a gap in its proof. Cook subsequently narrowed down
the possible range to 3 ≤ m1≤ 4. A subsequent investigation conducted in [FBP21]
successfully confirmed that the correct value for m1 is indeed 3. Concerning the Klein
quartic, Cook’s analysis indicated that the multiplicity of the first eigenvalue lies within
the range of 6 to 8. A rigorous proof establishing m1 = 8 is also provided in [FBP21].
Surfaces with many automorphisms like the Bolza surface and the Klein quartic often
emerge as solutions to extremal problems concerning both m1 and λ1. In [FBP21], it
was shown that the Klein quartic attains the maximalm1 among all hyperbolic surfaces
of genus 3. In a work by Strohmaier and Uski [SU13], they conjectured that the Bolza
surface maximizes λ1 among all hyperbolic surfaces of genus 2 based on numerical
SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURF ACE 3
experiments. A recent study [KMP21] provides additional evidence supporting the
conjecture that both the Bolza surface and the Klein quartic maximize λ1 among
hyperbolic surfaces of genus 2 and 3, respectively.
Our main result is as follows:
Theorem. The multiplicity of the first eigenvalue λ1 of the Fricke-Macbeath surface
is 7, and λ1∈ [1.23, 1.26].
Our primary tool for the proof is the Selberg trace formula. We make use of Vogeler’s
results [Vog03] concerning the length spectrum of the Fricke-Macbeath surface, specif-
ically, we require information about the conjugacy classes of the two shortest lengths
in the spectrum. When applying the Selberg trace formula, we utilize various types of
test functions. These include the functions featured in [BS07, Section 4] and [BLS20,
Section 5], which played a crucial role in confirming the Selberg eigenvalue conjecture
for numerous congruence subgroups with small conductor. We also employ the test
functions introduced in the context of the sphere packing problem [CE03, Section 7],
which were recently employed in the investigation of spectral properties of hyperbolic
surfaces in [FBP21].
After establishing the multiplicity of an eigenvalue, the subsequent natural question
is to identify the associated eigenspace as a representation. To address this, we present
a numerical method for computing the character of a representation obtained from
a set of eigenfunctions. This method enables us to formulate a conjecture regarding
which 7-dimensional representation of PSL 2(8) corresponds to the representation as-
sociated with λ1 of the Fricke-Macbeath surface; see Conjecture 5.1. The application
of these algorithms to compute the characters for other Riemann surfaces with many
automorphisms will be discussed in a separate work.
To conduct a numerical calculation based on the finite element method, we determine
a fundamental domain for the Fuchsian group that uniformizes the Fricke-Macbeath
surface using Poincar´ e’s polyhedron theorem [Mas71], along with its side-pairing trans-
formations. It is a hyperbolic polygon with 42 sides, which is actually the Dirichlet
domain centered at 0. We offer a visualization of this fundamental domain, updating
the classic Fricke-Klein illustration [Mag74]; see Figures 1 and 2 for a comparison.
Unlike the case of the Klein quartic in Figure 4, we find that this polygon is not com-
pletely tessellated by the fundamental (2, 3, 7)-triangles. We note that the fundamental
domain discussed in [Fri99] differs from ours.
