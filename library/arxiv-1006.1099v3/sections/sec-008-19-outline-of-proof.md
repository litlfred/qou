---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-008-19-outline-of-proof
section_title: "Outline of proof"
section_number: 1.9
pages: 7-9
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
lences with quasi-isomorphic images
DπF(Σ)֒→DπF(Z) ←DπF(Q0∩Q1; 0).
Both F(Σ g) and F(Q0∩Q1) are naturally Z4g−4-graded, but only the underlying Z2-graded
categories are equivalent; from this perspective, that is because the intermediate category F(Z)
only admits a Z2-grading. At a technical level, the proof of Theorem 1.1 combines ﬁv e principal
ingredients.
(1) Lefschetz ﬁbrations provide the basic geometric setting in which all the investigations
take place. Thus, a hyperelliptic curve and the relative quadric Z are viewed as Lefschetz
ﬁbrations with categorically-equivalent ﬁbres.
(2) Eigenvalue splittings for Fukaya categories; in particular, we derive suﬃcient conditions
for a collection of Lagrangian spheres to split-generate a particula r summand.
(3) Quilt theory , in the sense of Mau-Wehrheim-Woodward; speciﬁcally, we appeal t o their
work to construct embeddings of categories associated to (idemp otent summands of) La-
grangian correspondences which arise from blowing up certain codim ension two complete
intersections.
8 IV AN SMITH
(4) Surgery and Z-gradings, whereby certain holomorphic polygons are constrained by knowl-
edge of related polygons for a Lagrange surgery at an isolated inte rsection point, or by
their intersection numbers with divisors of poles of holomorphic volum e forms.
(5) Finite determinacy , introduced in this setting in Seidel’s beautiful paper [93], which
relies on Kontsevich’s formality theorem to describe certain A∞-structures in terms of
polyvector ﬁelds. Eventually, the Fukaya categories of the curve and the relative quadric
are identiﬁed by singling out a quasi-isomorphism class of A∞-structures on an exterior
algebra with the desired Hochschild cohomology.
These ingredients are assembled as general tools in Section 3, and d eployed in the subsequent
parts of the paper. The connection ←֓between F(Z) and the Fukaya category of the base locus
seems to be part of a wider phenomenon for blow-ups; it also makes a connection to a well-
known “spinning” construction of Lagrangian spheres, which prov ides a link between algebra
and geometry useful for establishing Addendum 1.2. The material o n Fukaya categories of blow-
ups should be compared to the work of Abouzaid, Auroux and Katza rkov [3], who derive closely
related results from the “Strominger-Yau-Zaslow” perspective o f Lagrangian torus ﬁbrations;
similar techniques are also applied in Seidel’s recent [95]. These results m ight be viewed as an
open-string counterpart to the symplectic birational geometry p rogramme of Yongbin Ruan and
his collaborators.
Remark 1.12. The symplectic manifolds which occur in the paper are real surfaces or Fano vari-
eties, hence are monotone with minimal Chern number ≥ 1, and the Lagrangian submanifolds we
consider are monotone of minimal Maslov number ≥ 2. These hypotheses considerably simplify
the deﬁnition of F(•;λ), which can then be constructed using essentially classical tools, a nd allow
us to make systematic use of the quilted Floer theory of Mau, Wehrh eim and Woodward [65]. We
emphasise that Fukaya categories enter the main argument in a rat her formal manner, and the
properties we require would hold independent of the ﬁner details of t he construction. That under-
lying construction is nonetheless a very substantial undertaking, and we are accordingly indebted
to the foundational work of Fukaya-Oh-Ohta-Ono, of Seidel, and of Mau-Wehrheim-Woodward.
Organisation of the paper . Section 2 gives background on the spaces M(Σ g) and derives the results of
Sections 1.4 and 1.5, assuming Theorem 1.1. This section is l argely self-contained, though at one or two
points we refer ahead for general Floer-theoretical result s. Such results are collected in Section 3. The
proof of Theorem 1.1 itself takes up the remainder of the pape r, Sections 4 and 5. A low-dimensional
topologist happy to take the proof of Theorem 1.1 on faith can stop reading at the end of Section 2.
A symplectic topologist interested in Theorem 1.1 but uncon cerned with 3-manifolds can start reading
from Section 3.
Acknowledgements. I am extremely indebted to Mohammed Abouzaid, Denis Auroux and Pa ul
Seidel for all their help and their numerous patient explanations. Th is paper is written very
much in the shadow of Seidel’s [93]. Conversations with Tom Bridgeland, Alex Dimca, Tobias
Dyckerhoﬀ, Sasha Eﬁmov, Tobias Ekholm, Rahul Pandharipande, T im Perutz, Catharina Strop-
pel and Burt Totaro were also inﬂuential. Detailed and insightful com ments from the anonymous
referees have dramatically improved the paper, both clarifying and simplifying the exposition.
The author is partially supported by grant ERC-2007-StG-205349 from the European Research
Council. Part of this work was undertaken whilst the author held a Re search Professorship at
the Mathematical Sciences Research Institute, Berkeley; thank s to MSRI for hospitality.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 9
