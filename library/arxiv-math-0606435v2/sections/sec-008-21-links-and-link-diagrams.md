---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-008-21-links-and-link-diagrams
section_title: "Links and link diagrams"
section_number: 2.1
pages: 5-6
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Links are represented by diagrams; we assume diagrams are oriented (though sometimes orientation is not relevant).
A crossing p in a link diagram D is called reducible (or nugatory) if it looks like on the left of ﬁgure 2. D is called
reducible if it has a reducible crossing, else it is called reduced. The reducing of the reducible crossing p is the move
depicted on ﬁgure 2. Each diagram D can be (made) reduced by a ﬁnite number of these moves.
p
P Q − → P Q(1)
Figure 2
We assume in the following all diagrams reduced, unless otherwise stated.
The diagram on the right of ﬁgure 3 is called connected sum A #B of the diagrams A and B. If a diagram D can be
represented as the connected sum of diagrams A and B, such that both A and B have at least one crossing, then D
is called disconnected (or composite), else it is called connected (or prime). K is prime if whenever D = A#B is a
composite diagram of K, one of A and B represent an unknotted arc (but not both; the unknot is not co nsidered to be
prime per convention).
By c(D) we denote the number of crossings of D, n(D) the number of components of D (or K, 1 if K is a knot), and
s(D) the number of Seifert circles of D. The crossing number c(K) of a knot or link K is the minimal crossing number
of all diagrams D of K. ! D is the mirror image of D, and ! K is the mirror image of K. Clearly g(!D) = g(D) and
g(!K) = g(K).
A # B = A B
Figure 3
The Seifert graph Γ(D) of a diagram D is deﬁned to be the graph whose vertices are the Seifert circles of D and whose
edges are the crossings. The reduced Seifert graph Γ′(D) is deﬁned by removing multiple copies of an edge between
two vertices in Γ(D), so that a simple edge remains. (See [MP, MP2] for example.)
6 2 Preliminaries, basic deﬁnitions and conventions
The (Seifert) genus g (K) resp. Euler characteristic χ(K) of a knot or link K is said to be the minimal genus resp.
maximal Euler characteristic of Seifert surface of K. For a diagram D of K, g(D) is deﬁned to be the genus of the
Seifert surface obtained by Seifert’s algorithm on D, and χ(D) its Euler characteristic. We have χ(D) = s(D) − c(D)
and 2g(D) = 2 − n(D) − χ(D).
The numbering of knots we use is as in the tables of [Ro, append ix] for prime knots of crossing number ≤ 10, and
as in [HT] for those of crossing number 11 to 16. KnotScape’s n umbering is reorganized so that for given crossing
number non-alternating knots are appended after alternating ones, instead of using ‘a’ and ‘n’ superscripts.
