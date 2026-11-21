---
doc_id: symmetry-11-01298
doc_title: "Braids, 3-Manifolds, Elementary Particles: Number Theory and Symmetry in Particle Physics"
section_id: sec-018-drinfeldturaev-quantization-and-quantum-states
section_title: "Drinfeld–Turaev Quantization and Quantum States"
section_number: null
pages: 20-21
source_pdf: symmetry-11-01298.pdf
source_sha256: 595648c84501e8a6
toc_source: outline
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
duplicate_of: "arxiv-1910.09966v1"
---
In [66,67], we discussed the appearance of quantum states from knots known as Turaev–Drinfeld
quantization. The idea for the following construction can be simply expressed. We start with two
3-manifolds and consider a cobordism between them. This cobordism is a 4-manifold with a branched
covering branched over a surface with self-intersections. Here, it is enough to restrict to a special class
of these surfaces, so-called ribbon surfaces (see [68]). The 3-manifolds are chosen to be hyperbolic knot
complements, denoted by Y1, Y2. A hyperbolic structure is deﬁned by a homomorphism π1(Yi) →
SL(2, C) (∈Hom(π1(Yi), SL(2, C))) up to conjugation. Now, we extend this structure to the entire
cobordism, denoted by Cob(Y1, Y2). The branching set of Cob(Y1, Y2) is a surface S with non-trivial
fundamental group π1(S). This surface can be changed without any change of Cob(Y1, Y2). One
change can be described as crossing change. Now, we have all ingredients for the Drinfeld–Turaev
quantization:
•
The surface S (branching set of Cob(Y1, Y2)) is inducing a representation π1(S) →SL(2, C).
•
The space of all representations X(S, SL(2, C))
=
Hom(π1(S), SL(2, C))/SL(2, C) has a
natural Poisson structure (induced by the bilinear on the group) and the Poisson algebra
(X(S, SL(2, C), { }) of complex functions over them is the algebra of observables.
•
The Skein module K−1(S × [0, 1]) (i.e., t = −1) has the structure of an algebra isomorphic to the
Poisson algebra (X(S, SL(2, C)), { }). (see also [69,70]).
Symmetry 2019, 11, 1298
21 of 26
•
The skein algebra Kt(S × [0, 1]) is the quantization of the Poisson algebra (X(S, SL(2, C)), { })
with the deformation parameter t = exp(h/4) (see also [69]) .
To understand these statements, we have to introduce the skein module Kt(M) of a 3-manifold
M (see [71]). For that purpose, we consider the set of links L(M) in M up to isotopy and construct
the vector space CL(M) with basis L(M). Then, one can deﬁne CL[[t]] as ring of formal polynomials
having coefﬁcients in CL(M). Now, we consider the link diagram of a link, i.e., the projection of the
link to the R2 having the crossings in mind. Choose a disk in R2 so that one crossing is inside this disk.
If the three links differ by the three crossings Loo, Lo, L∞(see Figure 9) inside of the disk, then these
links are skein related.
Figure 9. Crossings L∞, Lo, Loo.
Then, in CL[[t]], one writes the skein relation L∞−tLo −t−1Loo which depends only on the
group SL(2, C). Furthermore, let L ⊔O be the disjoint union of the link with a circle. Then, one writes
the framing relation L ⊔O + (t2 + t−2)L. Let S(M) be the smallest submodule of CL[[t]] containing
both relations. Then, we deﬁne the Kauffman bracket skein module by Kt(M) = CL[[t]]/S(M). The
modiﬁcation of S by using the skein relations is one of the allowed changes of the branching set to
keep Cob(Y1, Y2).
Now, we list the following general results about this module:
•
The module K−1(M) for t = −1 is a commutative algebra.
•
Let S be a surface. Then, Kt(S × [0, 1]) carries the structure of an algebra.
The algebra structure of Kt(S × [0, 1]) can be simply seen by using the diffeomorphism between
the sum S × [0, 1] ∪S S × [0, 1] along S and S × [0, 1]. Then, the product ab of two elements a, b ∈Kt(S ×
[0, 1]) is a link in S × [0, 1] ∪S S × [0, 1] corresponding to a link in S × [0, 1] via the diffeomorphism.
The algebra Kt(S × [0, 1]) is in general non-commutative for t̸ = −1. For the following, we will omit
the interval [0, 1] and denote the skein algebra by Kt(S).
As shown in [23,66,72], the skein algebra serves as the observable algebra of a quantum ﬁeld
theory. For this approach via branched coverings, the branching sets of knot complements (representing
the fermions) are special braids (6-plats, see above). Any different braid is a different state or better
than a different quantum state but not a different particle. As explained above, the charge spectrum is
enough to describe one generation of particles (two leptons, two quarks). The appearance of different
generations will be discussed below.
