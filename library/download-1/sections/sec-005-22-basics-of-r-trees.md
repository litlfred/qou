---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-005-22-basics-of-r-trees
section_title: "Basics of R-trees."
section_number: 2.2
pages: 6-7
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Basics of R-trees.
Before reviewing the deﬁnition of R-trees, we recall some standard
terminologies in metric geometry. Let ðX; dXÞ be a metric space. A rectiﬁable
curve  : ½0; 1 ! X is called a geodesic if its arclength coincides with the distance
dXðð0Þ; ð1ÞÞ and it has a constant speed, i.e., parametrized proportionally to the
arc length. We say that ðX; dXÞ is a geodesic space if any two points in X are
joined by a geodesic between them. Let X be a geodesic space. A geodesic triangle
in X is the union of the image of three geodesics joining a triple of points in X
pairwise. A subset A  X is called convex if every geodesic joining two points in A
is contained in A.
A complete metric space ðT; dTÞ is called an R-tree if it satisﬁes the following
properties:
(1) For all z; w 2 T there exists a unique unit speed geodesic z;w from z to w.
(2) The image of every simple path in T is the image of a geodesic.
Denote by ½z; wT the image of the geodesic z;w. We also put ðz; wT :¼ ½z; wT n
fzg and ðz; wÞT :¼ ½z; wT n fz; wg. A complete geodesic space T is an R-tree if and
only if it is 0-hyperbolic, that is to say, every edge in any geodesic triangle in T is
included in the union of the other two edges. See [2] for another characterizations
of R-trees. Given z 2 T, we indicate by C TðzÞ the set of all connected components
of T n fzg. We also denote by C 0
TðzÞ the set of all fzg [ T 0 for T 0 2 C TðzÞ.
Although the following lemma is somewhat standard, we prove it for complete-
ness.
LEMMA 2.8.
Each T 0 2 C TðzÞ is convex.
PROOF.
By the property (2) of R-trees, it is suﬃcient to prove that T 0 is
arcwise connected. Taking a point v 2 T 0, we put
A :¼ fw 2 T 0 j v and w are connected by a path in T 0g:
It is easy to see that the set A is closed in T 0. Since every metric ball in T is arcwise
connected, the set A is also open. Since T 0 is connected, we get T 0 ¼ A. This
completes the proof.

A subset in an R-tree is called a subtree if it is a closed convex subset. Note
that a subtree itself is an R-tree.
PROPOSITION 2.9.
Every connected subset in an R-tree is convex.
488
K. FUNANO
PROOF.
Let T be an R-tree. Suppose that there exists a connected subset
T 0  T which is not convex. Then, there are points z; w 2 T 0 and ez 2 ðz; wÞT such
that ez =2 T 0. Since T 0 ¼ SfT 0 \ C j C 2 C TðezÞg and each C 2 C TðezÞ is open, by the
connectivity of T 0, there is C0 2 C TðezÞ such that T 0  C0. Since C0 is convex by
Lemma 2.8, we get ez 2 ½z; wT  C0. This is a contradiction since ez =2 C0. This
completes the proof.

