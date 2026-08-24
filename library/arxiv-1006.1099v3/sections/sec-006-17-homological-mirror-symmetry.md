---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-006-17-homological-mirror-symmetry
section_title: "Homological Mirror Symmetry"
section_number: 1.7
pages: 6-7
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
category analogues of three well-known results concerning derive d categories of sheaves.
• (Bondal-Orlov) The derived category of sheaves on the intersection of two even-dimensional
quadrics has a semi-orthogonal decomposition in which one factor is the derived category
of sheaves on an underlying hyperelliptic curve [16].
• (Kapranov) The derived category of sheaves on an even-dimensio nal quadric has a semi-
orthogonal decomposition in which one factor is the derived catego ry of sheaves on a pair
of points [49].
• (Bondal-Orlov) If X→Y is the blow-up along a smooth centre B⊂Y of codimension at
least 2, the derived category of sheaves on B embeds in the derived category of sheaves
on X [16].
Obviously, Theorem 1.1 is exactly the symplectic analogue of the ﬁrst of these results. Our
proof of Theorem 1.1 relates both categories appearing in its state ment with the Fukaya category
of the relative quadric Z, given by blowing up P2g+1 along Q0∩Q1. We construct equivalences
with quasi-isomorphic images
DπF(Σ g)֒→DπF(Z) ←DπF(Q0∩Q1; 0).
Although it occupies only a small part of the ﬁnal proof, the geomet ric heart of֒→and arguably
of Theorem 1.1 is Section 4.1, which gives a derived equivalence betwee n the nilpotent summand
of the Fukaya category of a quadric Q⊂ P2g+1 and the Fukaya category of a pair of points
S0. This is precisely the symplectic analogue of Kapranov’s theorem. Fr om that perspective, a
hyperelliptic curve and the total space of the associated pencil of quadrics behave, categorically,
like ﬁbrations with the same ﬁbre and monodromy. To pass between DπF(Z) and DπF(Q0∩Q1)
involves relating the derived Fukaya category of a base locus and of a blow-up, akin to the second
mentioned theorem of Bondal-Orlov (in this case, however, the sym plectic story is carried out in
more restricted circumstances, for blow-ups of codimension two c omplete intersections satisfying
a raft of convenient hypotheses). In light of these analogies, one is led to compare the chains of
spaces
∅ ⊂ 2 points ⊂ Σ g ⊂ X
↕ ↕ ↕ ↕
P2g+1 ⊃ Q ⊃ Q0∩Q1 ⊃ X ∨
(1.2)
where the top line corresponds to double branched covers of proj ective space of dimensions
d =−1, 0, 1, 2 over divisors of degree 2 g + 2, and the lower line the base locus of a d-dimensional
family of quadrics in P2g+1. There are equivalences between the Fukaya category of a space in
the top line, and the nilpotent summand of the Fukaya category of t he space below it, in each
of the ﬁrst 3 columns, mirror to a small part of Kuznetsov’s “homolo gical projective duality”
[58]. The situation in the ﬁnal column is less clear. For instance, when g = 2, both X and X ∨
areK3 surfaces, but in general they don’t have equivalent derived cate gories of coherent sheaves
unless one introduces a twist by a class in the Brauer group. It would be interesting to know
whether this has any symplectic analogue. The hypersurface of de generate quadrics is singular
in codimension 3, so technical diﬃculties arise in pushing this any furth er.
Given the proposed Landau-Ginzburg mirror w : YQ0∩Q1→ C of Q0∩Q1 [50, 83], and the
proofs by Seidel and Eﬁmov of mirror symmetry for curves of genu s≥ 2, [93, 29], Theorem 1.1
essentially proves one direction of Homological Mirror Symmetry for the Fano variety which is
the complete intersection of two quadrics:
DπF(Q0∩Q1; 0) ≃ Db
sing(YQ0∩Q1,w|open subset )
(restricting w throws out certain “massive modes”). In particular, this gives the ﬁrst proof of
HMS for a moduli space of bundles on a curve of higher genus.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 7
Remark 1.10. Homological Mirror Symmetry typically relates symplectic and algebra ic geometry.
The relation of Theorem 1.1 to HMS is roughly as follows. The mirror of a Fano variety X is
a Landau-Ginzburg model w : Y → C; blowing up the Fano X ′→ X is expected to introduce
new singular ﬁbres Y ⊂ Y ′ w′
→ C into the LG-model. Blow-ups induce semi-orthogonal decom-
positions of the derived category Db(X ′) = ⟨Db(X),C⟩, hence corresponding semi-orthogonal
decompositions relating the Fukaya-Seidel categories of the mirro rs. On the other hand, the new
singular ﬁbre of ( Y ′,w ′) leads to a new summand to its derived category of singularities, whic h
should correspond to a new summand in the Fukaya category of X ′ (and perhaps some bulk
deformation of the summands coming from X). For more on the mirror symmetric background
and motivation for Theorem 1.1, see [51].
