---
doc_id: arxiv-math-0110009v3
doc_title: "New upper bounds on sphere packings I"
section_id: sec-010-references
section_title: "References"
section_number: null
pages: 1-3
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
doc_brief: "New upper bounds on sphere packings I — We develop an analogue for sphere packing of the linear progr amming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
1. Introduction
The sphere packing problem asks for the densest packing of sp heres into
Euclidean space. More precisely, what fraction of Rn can be covered by congru-
ent balls that do not intersect except along their boundarie s? This problem ﬁts
into a broad framework of packing problems, including error -correcting codes
∗Cohn was supported by an NSF Graduate Research Fellowship an d by a summer internship at
Lucent Technologies, and currently holds an American Insti tute of Mathematics ﬁve-year fellowship.
Elkies was supported in part by the Packard Foundation.
690 HENRY COHN AND NOAM ELKIES
and spherical codes. Linear programming bounds [D] are the m ost powerful
known technique for producing upper bounds in such problems . In particular,
[KL] uses this technique to prove the best bounds known for sp here packing
density in high dimensions. However, [KL] does not study sph ere packing di-
rectly, but rather passes through the intermediate problem of spherical codes.
In this paper, we develop linear programming bounds that app ly directly to
sphere packing, and study these bounds numerically to prove the best bounds
known1 for sphere packing in dimensions 4 through 36. In dimensions 8 and 24,
our bounds are very close to the densities of the known packin gs: they are too
high by factors of 1 . 000001 and 1 . 0007071 in dimensions 8 and 24, respectively.
(The best bounds previously known were oﬀ by factors of 1.012 16 and 1.27241.)
We conjecture that our techniques can be used to prove sharp b ounds in 8 and
24 dimensions.
The sphere packing problem in Rn is trivial for n = 1, and the answer has
long been known for n = 2: the standard hexagonal packing is optimal. For
n = 3, Hales [Ha] has proved that the obvious packing, known as t he “face-
centered cubic” packing (equivalently, the A3 or D3 root lattice), is optimal,
but his proof is long and diﬃcult, and requires extensive com puter calculation;
as of December, 2002, it has not yet been published, but it is w idely regarded
as being likely to be correct. For n ≥ 4 the problem remains unsolved. Upper
and lower bounds on the density are known, but they diﬀer by an exponential
factor as n → ∞ . Each dimension seems to have its own peculiarities, and
it does not seem likely that a single, simple construction wi ll give the best
packing in every dimension.
We begin with some basic background on sphere packings; for m ore in-
formation, see [CS]. Recall that a lattice in Rn is a subgroup consisting of the
integer linear combinations of a basis of Rn. One important way to create a
sphere packing is to start with a lattice Λ ⊂ Rn, and center the spheres at
the points of Λ, with radius half the length of the shortest no nzero vectors in
Λ. Such a packing is called a lattice packing . Not every sphere packing is a
lattice packing, and in fact it is plausible that in all suﬃci ently large dimen-
sions, there are packings denser than every lattice packing . However, many
important examples in low dimensions are lattice packings.
A more general notion than a lattice packing is a periodic packing . In
periodic packings, the spheres are centered on the points in the union of ﬁnitely
many translates of a lattice Λ. In other words, the packing is still periodic
under translations by Λ, but spheres can occur anywhere in a f undamental
parallelotope of Λ, not just at its corners (as in a lattice pa cking).
1W.-Y. Hsiang has recently announced a solution of the 8-dime nsional sphere packing problem
[Hs], but the details are not yet public. His methods are appa rently quite diﬀerent from ours.
NEW UPPER BOUNDS ON SPHERE PACKINGS I 691
The density ∆ of a packing is deﬁned to be the fraction of space covered
by the balls in the packing. Density is not necessarily well- deﬁned for patho-
logical packings, but in those cases one can take a lim sup of t he densities for
increasingly large ﬁnite regions. One can prove that period ic packings come
arbitrarily close to the greatest packing density, so when p roving upper bounds
it suﬃces to consider periodic packings. Clearly, density i s well-deﬁned for pe-
riodic packings, so we will not need to worry about subtletie s. See Appendix A
for more details.
For many purposes, it is more convenient to talk about the center den-
sity δ . It is the number of sphere-centers per unit volume, if unit s pheres are
used in the packing. Thus,
∆ = π n/ 2
(n/ 2)! δ,
since a unit sphere has volume π n/ 2/ (n/ 2)!. Of course, for odd n we interpret
(n/ 2)! as Γ( n/ 2 + 1).
In most dimensions, there are not even any plausible conject ures for the
densest sphere packing. The only exceptions are low dimensi ons (up to perhaps
8 or 10), and a handful of higher dimensions (such as 12, 16, an d 24). The
most striking examples are 8 and 24 dimensions. In those dime nsions, the
densest packings are undoubtedly the E8 root lattice and the Leech lattice,
respectively. The E8 lattice is easy to deﬁne. It consists of all points of R8
whose coordinates are either all integers or all halves of od d integers, and
sum to an even integer. A more illuminating characterizatio n is as follows:
E8 is the unique lattice in R8 of covolume 1 such that all vectors v in the
lattice have even norm ⟨v, v ⟩. Such a lattice is called an even unimodular
lattice. Even unimodular lattices exist only in dimensions that are multiples
of 8, and in R8 there is only one, up to isometries of R8. The Leech lattice
is harder to write down explicitly; see [CS] for a detailed tr eatment. It is the
unique even unimodular lattice in R24 with no vectors of length
√
