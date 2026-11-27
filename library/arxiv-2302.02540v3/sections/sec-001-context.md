---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-001-context
section_title: "Context"
section_number: null
pages: 3-4
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
mannian manifold (with 1/4 replaced by the bottom of the spectrum of the Laplacian on
the universal cover ofMin the case ofN small) and their maximization has been studied by
several authors for various classes of manifolds. These shape optimization problems seek
to find optimal inequalities analogous to the isoperimetric inequality for other geometric
quantities.
For example, if we fix a topological manifold Σ, then maximizing the systole over all
Riemannian manifoldsMof a given volume that are homeomorphic to Σ is called the
isosystolic problemand it has been solved for the projective plane [Pu52], the 2-dimensional
torus (Loewner), and the Klein bottle [Bav86]. The maximum ofm 1 is known for the same
surfaces [Bes80, CdV87, Nad88] as well as for the 2-sphere [Che75], while the maximum of
λ1 is known for the closed orientable surface of genus 2 [JLN +05, NS19] in addition to all
the previous surfaces [Her70, LY82, Nad96, ESGJ06].
4 MAXIME FORTIER BOURQUE AND BRAM PETRI
Another much-studied case is that of flatd-dimensional tori of unit volume. In that
case,λ 1(M) = (2πsys(M ∗))2 andm 1(M) = kiss(M ∗)/2 whereM ∗ is the torus dual to
M, so the first four maximization problems above reduce to only two while the fifth is
trivial since the bottom of the spectrum of the Laplacian onR d is 0. Furthermore, if
Λ is a lattice such thatM ∼= Rd/Λ, then the balls of radius sys(M)/2 centered at the
points in Λ form a sphere packing of density 2−d sys(M)d vol(Bd
1), whereB d
1 is the unit ball
inR d, and there are exactly kiss(M) balls tangent to any ball in this packing. In other
words, maximizing the systole and kissing number of flat tori of unit area is equivalent to
maximizing the packing density and kissing number among sphere packings whose centers
form a lattice. Both problems have been solved in dimensions 1 to 8 and 24 (see [CS93,
Table 1.1] and [CK09]). In some cases, the solutions to these problems were obtained by a
method known aslinear programmingfirst introduced by Delsarte in the context of error-
correcting codes [Del72]. This was then adapted to prove bounds on the kissing numbers
of arbitrary sphere packings (not necessarily coming from lattices) in [DGS77] and then
on their packing density in [CE03]. In addition to giving optimal bounds in dimensions 8
[Via17] and 24 [CKM+17], this approach also yields the best known asymptotic bounds on
kissing numbers and packing density as the dimension tends to infinity [CZ14].
The five invariants we consider here were previously investigated for hyperbolic surfaces
in [Sch93, BS94, Bav96], [Sch94, SS97, Par13], [Che75, HM23, KMcP24], [CCdV88, LM24],
and [Hub76, OR09], among many others. Prior to our work, the only optimal bounds
known were for the systole [Jen84] and kissing number [Sch94] in genus 2, and forN small
in every genus [OR09]. The known examples that maximizeN small have a short pants
decomposition [Bus77], which is why we are interested in improved bounds as the systole
grows. We added one new optimal inequality to the list in [FBP24], where we determined
the maximum ofm 1 in genus 3 using the same techniques as in the current paper. Here
we extend and improve this method in a systematic way. Although our new bounds in low
genus do not appear to yield any new optimizers, they are a first step in that direction.
The next step would be to compute the invariants for more examples.
