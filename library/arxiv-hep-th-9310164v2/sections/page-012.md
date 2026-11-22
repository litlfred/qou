---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-012
section_title: "Page 12"
section_number: null
pages: 12-12
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
12
JOHN W. BARRETT & BRUCE W. WESTBURY
Deﬁnition 3.1. A spherical Hopf algebra over F consists of a F-module A together
with the following data
(1) a multiplication µ
(2) a unit η: F →A
(3) a comultiplication ∆: A →A ⊗A
(4) a counit ǫ: A →F
(5) an antipodal map γ: A →A
(6) an element w ∈A
The data (A, µ, η, ∆, ǫ, γ) is required to deﬁne a Hopf algebra. The conditions
on the element w are the following:
(1) γ2(a) = waw−1 for all a ∈A.
(2) ∆(w) = w ⊗w.
(3) γ(w) = w−1.
(4) ǫ(w) = 1.
(5) tr(θw) = tr(θw−1) for any left A-module, V , which is ﬁnitely generated and
projective as an F-module and for all θ ∈EndA(V ).
It follows from the condition ∆(w) = w ⊗w that γ(w) = w−1 and that ǫ(w) = 1.
Such elements are called group-like.
Example 3.2. Examples of Hopf algebras which are spherical are:
(1) Any involutory Hopf algebra is spherical. The element w can be taken to
be 1.
(2) Any ribbon Hopf algebra, as deﬁned in [Reshetikhin and Turaev 1990], is
spherical. The element w can be taken to be uv−1 where the element u
is determined by the quasi-triangular structure and the element v is the
ribbon element.
Remark 3.3. A Hopf algebra with an element w that satisﬁes the ﬁrst two conditions
of deﬁnition 3.1 is spherical if, either w2 = 1, or all modules are self-dual.
Remark 3.4. If A is a Hopf algebra there may exist more than one element w such
that (A, w) is a spherical Hopf algebra. However, if w1 is one such element then
w2 = gw1 is another such element if and only if g satisﬁes the conditions:
(1) g is central
(2) g is group-like
(3) g is an involution
In particular, if A is ﬁnite dimensional over a ﬁeld, the set of g satisfying these
conditions form a group of the form Zk
2 for some integer k.
Example 3.5. This is an example of a ﬁnite dimensional Hopf algebra over C
which satisﬁes all the conditions for a spherical Hopf algebra except that the left
and right traces are distinct. This example is the quantised enveloping algebra of
the Borel subalgebra of SL2(C).
