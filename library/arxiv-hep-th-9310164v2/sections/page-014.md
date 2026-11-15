---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-014
section_title: "Page 14"
section_number: null
pages: 14-14
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
14
JOHN W. BARRETT & BRUCE W. WESTBURY
Proposition 3.7. Let A be a spherical Hopf algebra. Let x be a left A-module.
Then End(x), the endomorphism algebra in the non-degenerate quotient, is semi-
simple.
Proof. Let EndA(x) be the endomorphism algebra of x in the category of left A-
modules. Then we show that the kernel of the map EndA(x) →End(x) contains
the nilpotent radical of EndA(x). Since the nilpotent radical is a two-sided ideal it
is suﬃcient to show that if θ ∈EndA(x) is nilpotent then trL(θ) = 0. However θ
and ω commute and so θω is also nilpotent. This shows that trL(θ) is the matrix
trace of a nilpotent endomorphism of a ﬁnite dimensional vector space over F and
so trL(θ) = 0.
Proposition 3.8. Let A be a spherical Hopf algebra.
Take the non-degenerate
quotient of the spherical category of left A-modules. Take J to be a set of objects
such that, if End(x) ∼= F then there is a unique a ∈J such that x ∼= a. Then, for
each object x in the non-degenerate quotient, there is a natural isomorphism
x ∼=
M
a∈J
Hom(x, a) ⊗a.
Proof. First we deﬁne, for each idempotent π ∈End(x), an object πx in the non-
degenerate quotient. Let π′ ∈EndA(x) be a lifting of π. Then π′x is a left A-module
and so also gives an object, πx, in the non-degenerate quotient. This object is
independent of the choice of lifting since πx is characterised by the property that,
for any w and y,
Hom(w, πx) = Hom(w, x).π
and
Hom(πx, y) = π. Hom(x, y).
Next we show that if π is primitive then End(πx) ∼= F. More generally, if π1 and
π2 are primitive idempotents then
Hom(π1x, π2x) ∼=
 F
if π1 and π2 are isomorphic
0
otherwise
If π is primitive then so is π′ and so EndA(π′x) is a local algebra. Hence End(πx)
is a non-trivial semisimple quotient of a local algebra and so is F. Alternatively,
End(πx) is π. End(x).π which is F since π is primitive.
Now write 1 ∈End(x) as a sum of orthogonal primitive idempotents.
This
decomposition is not canonical. However, for each a ∈J, deﬁne Ea to be the sum
of the idempotents, {π}, in the decomposition that satisfy πx ∼= a. Then each
non-zero Ea is a central idempotent in End(x) and the decomposition
x ∼=
M
a∈J
Eax
is canonical.
Furthermore it follows from this discussion that, for each a ∈J,
Eax can be naturally identiﬁed with V (x, a) ⊗a for some V (x, a).
Hence x ∼=
a∈J V (x, a) ⊗a.
