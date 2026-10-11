---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-067-93-the-state-sum-invariants-derived-from-ribbon
section_title: "The state-sum invariants derived from ribbon categories"
section_number: 9.3
pages: 139-140
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
A ribbon category is a monoidal category {Vi}i∈I equipped with a braiding
V ⊗W →W ⊗V and a twist V →V for any objects V and W which are
maps satisfying certain properties. We obtain an invariant of framed links from
a ribbon category by associating a braiding to a crossing of a link diagram and
a twist to a full-twist of a framing of a link. A monoidal category is called semi-
simple if any object is isomorphic to a direct sum of simple ones. The S-matrix
S = (Sij)i,j∈I of a semi-simple ribbon category {Vi}i∈I is deﬁned by putting
Sij to be the invariant of the Hopf link whose components are associated with
Vi and Vj . A modular category is a semi-simple ribbon category with ﬁnitely
many isomorphism classes of simple objects whose S-matrix is invertible. We
obtain the Reshetikhin-Turaev invariant of 3-manifolds and its TQFT from a
modular category by using surgery presentations of the 3-manifolds. See [23]
for details of this paragraph.
Monoidal category
=⇒State-sum invariant of 3-manifolds and its TQFT
?
+ braiding
+ twist
Ribbon category
=⇒Invariant of framed links
?
+ semi-simple
+ ﬁniteness of I
+ invertibility of S
Modular category
=⇒Reshetikhin-Turaev invariant of 3-manifolds and its TQFT
Figure 19: Monoidal, ribbon, modular categories and their consequences
The quantum 6j-symbols are typical 6j-symbols which induce modular cate-
gories. The square of the absolute value of the Reshetikhin-Turaev invariant
derived from a modular category is equal to the value of the state-sum invari-
ant derived from the category. It is suggested by Ocneanu that the monoidal
category of the quantum double of each of such subfactors would be braided,
and that the Reshetikhin-Turaev invariant derived from this quantum double
would be equal to the Turaev-Viro-Ocneanu invariant derived from the original
subfactor.
Problem 9.5
(Y. Kawahigashi) Suppose we have a semisimple ribbon cat-
egory C with ﬁnitely many isomorphism classes of simple objects. If the S-
Geometry & Topology Monographs, Volume 4 (2002)
512
T. Ohtsuki (Editor)
matrix is invertible, we can construct the Reshetikhin-Turaev invariant and
the state-sum invariant from C and the latter is the square of the absolute
value of the former. If the S-matrix is not invertible, do we still have a similar
description of the state-sum invariant?
Remark See also Problem 9.11 for a similar problem for the Turaev-Viro-
Ocneanu invariants.
Problem 9.6
(Y. Kawahigashi) Suppose we have a semisimple ribbon cat-
egory C1 with ﬁnitely many isomorphism classes of simple objects, but the
S-matrix is not invertible.
Then we can construct a new modular category
C2 containing C1 as a full subcategory by the “quantum double” construction
[315, 316, 182], but there may be another extension of C1 to a modular cate-
gory. Theorem 2.13 in [315] claims that we have a “minimal” extension in an
“essentially unique” way. Do we indeed have existence and certain uniqueness
of such an extension? If so, what is the relation between the two TQFT’s arising
from C1 and its minimal extension?
Problem 9.7
(Y. Kawahigashi) Suppose we have a semisimple ribbon cat-
egory C1 with a degenerate S-matrix as in Problem 9.6. By the method in
[288], we can also make a modular tensor category C2 from C1. What is the
relation between the two TQFT’s arising from C1 and C2?
Problem 9.8
(Y. Kawahigashi) There are some fusion rule algebras with
6j-symbols that do not seem to arise from quantum groups in [14] and more
conjectured candidates of such examples in [160]. What are the corresponding
TQFT’s? Especially if the series conjectured in [160] does exist, it would give
a parametrized family of TQFT’s. Does a diﬀerentiation by a parameter (af-
ter a certain reparametrization) give a more interesting invariant, possibly of
Vassiliev type?
9.4
