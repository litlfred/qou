---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
Introduction
2.
Lattices, Fourier transforms, and Poisson summation
3.
Principal theorems
4.
Homogeneous spaces
5.
Conditions for a sharp bound
6.
Stationary points
7.
Numerical results
8.
Uniqueness
Appendix A. Technicalities about density
Appendix B. Other convex bodies
Appendix C. Numerical data
Acknowledgements
References
1. Introduction
The sphere packing problem asks for the densest packing of spheres into
Euclidean space. More precisely, what fraction of Rn can be covered by congru-
ent balls that do not intersect except along their boundaries? This problem ﬁts
into a broad framework of packing problems, including error-correcting codes
∗Cohn was supported by an NSF Graduate Research Fellowship and by a summer internship at
Lucent Technologies, and currently holds an American Institute of Mathematics ﬁve-year fellowship.
Elkies was supported in part by the Packard Foundation.
690
HENRY COHN AND NOAM ELKIES
and spherical codes. Linear programming bounds [D] are the most powerful
known technique for producing upper bounds in such problems. In particular,
[KL] uses this technique to prove the best bounds known for sphere packing
density in high dimensions. However, [KL] does not study sphere packing di-
rectly, but rather passes through the intermediate problem of spherical codes.
In this paper, we develop linear programming bounds that apply directly to
sphere packing, and study these bounds numerically to prove the best bounds
known1 for sphere packing in dimensions 4 through 36. In dimensions 8 and 24,
our bounds are very close to the densities of the known packings: they are too
high by factors of 1.000001 and 1.0007071 in dimensions 8 and 24, respectively.
(The best bounds previously known were oﬀby factors of 1.01216 and 1.27241.)
We conjecture that our techniques can be used to prove sharp bounds in 8 and
24 dimensions.
The sphere packing problem in Rn is trivial for n = 1, and the answer has
long been known for n = 2: the standard hexagonal packing is optimal. For
n = 3, Hales [Ha] has proved that the obvious packing, known as the “face-
centered cubic” packing (equivalently, the A3 or D3 root lattice), is optimal,
but his proof is long and diﬃcult, and requires extensive computer calculation;
as of December, 2002, it has not yet been published, but it is widely regarded
as being likely to be correct. For n ≥4 the problem remains unsolved. Upper
and lower bounds on the density are known, but they diﬀer by an exponential
factor as n →∞. Each dimension seems to have its own peculiarities, and
it does not seem likely that a single, simple construction will give the best
packing in every dimension.
We begin with some basic background on sphere packings; for more in-
formation, see [CS]. Recall that a lattice in Rn is a subgroup consisting of the
integer linear combinations of a basis of Rn. One important way to create a
sphere packing is to start with a lattice Λ ⊂Rn, and center the spheres at
the points of Λ, with radius half the length of the shortest nonzero vectors in
Λ. Such a packing is called a lattice packing. Not every sphere packing is a
lattice packing, and in fact it is plausible that in all suﬃciently large dimen-
sions, there are packings denser than every lattice packing. However, many
important examples in low dimensions are lattice packings.
A more general notion than a lattice packing is a periodic packing. In
periodic packings, the spheres are centered on the points in the union of ﬁnitely
many translates of a lattice Λ. In other words, the packing is still periodic
under translations by Λ, but spheres can occur anywhere in a fundamental
parallelotope of Λ, not just at its corners (as in a lattice packing).
1W.-Y. Hsiang has recently announced a solution of the 8-dimensional sphere packing problem
[Hs], but the details are not yet public. His methods are apparently quite diﬀerent from ours.
NEW UPPER BOUNDS ON SPHERE PACKINGS I
691
The density ∆of a packing is deﬁned to be the fraction of space covered
by the balls in the packing. Density is not necessarily well-deﬁned for patho-
logical packings, but in those cases one can take a lim sup of the densities for
increasingly large ﬁnite regions. One can prove that periodic packings come
arbitrarily close to the greatest packing density, so when proving upper bounds
it suﬃces to consider periodic packings. Clearly, density is well-deﬁned for pe-
riodic packings, so we will not need to worry about subtleties. See Appendix A
for more details.
For many purposes, it is more convenient to talk about the center den-
sity δ. It is the number of sphere-centers per unit volume, if unit spheres are
used in the packing. Thus,
∆= πn/2
(n/2)!δ,
since a unit sphere has volume πn/2/(n/2)!. Of course, for odd n we interpret
(n/2)! as Γ(n/2 + 1).
In most dimensions, there are not even any plausible conjectures for the
densest sphere packing. The only exceptions are low dimensions (up to perhaps
8 or 10), and a handful of higher dimensions (such as 12, 16, and 24). The
most striking examples are 8 and 24 dimensions.
In those dimensions, the
densest packings are undoubtedly the E8 root lattice and the Leech lattice,
respectively. The E8 lattice is easy to deﬁne. It consists of all points of R8
whose coordinates are either all integers or all halves of odd integers, and
sum to an even integer. A more illuminating characterization is as follows:
E8 is the unique lattice in R8 of covolume 1 such that all vectors v in the
lattice have even norm ⟨v, v⟩.
Such a lattice is called an even unimodular
lattice. Even unimodular lattices exist only in dimensions that are multiples
of 8, and in R8 there is only one, up to isometries of R8. The Leech lattice
is harder to write down explicitly; see [CS] for a detailed treatment. It is the
unique even unimodular lattice in R24 with no vectors of length
√
2. These two
lattices have many remarkable properties and connections with other branches
of mathematics, but so far these properties have not led to a proof that they are
optimal sphere packings. We conjecture that our linear programming bounds
can be used to prove optimality.
If linear programming bounds can indeed be used to prove the optimality
of these lattices, it would not come as a complete surprise, because other pack-
ing problems in these dimensions can be solved similarly. The most famous
example is the kissing problem: how many nonoverlapping unit balls can be
arranged tangent to a given one? If we regard the points of tangency as a spher-
ical code, the question becomes how many points can be placed on a sphere
with no angles less than π/3. Odlyzko and Sloane [OS] and Levenshtein [Lev]
independently used linear programming bounds to solve the kissing problem in
692
HENRY COHN AND NOAM ELKIES
4
8
12
16
20
24
28
32
0
1
2
3
4
−1
−2
−3
upper curve: Rogers’ upper bound
lower curve: New upper bound
bottom line: Best packing known
Figure 1. Plot of log2 δ + n(24 −n)/96 vs. dimension n.
8 and 24 dimensions. (The solutions in dimensions 8 and 24 are obtained from
the minimal nonzero vectors in the E8 and Leech lattices.) Because we know
a priori that the answer must be an integer, any upper bound within less than 1
of the truth would suﬃce. Remarkably, the linear programming bound gives
the exact answer, with no need to take into account its integrality. By contrast,
in most dimensions it gives a noninteger. The remarkable exactness seems to
occur only in dimensions 1, 2, 8, and 24. We observe the same numerically in
our case, but can prove it only for dimension 1.
Figure 1 compares our results with the best packings known as of Decem-
ber, 2002 (see Tables I.1(a) and I.1(b) of [CS, pp. xix, xx]), and the best upper
bounds previously known in these dimensions (due to Rogers [Ro]). The graph
was normalized for comparison with Figure 15 from [CS, p. 14].
