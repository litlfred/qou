---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
arXiv:math/0108011v1  [math.GT]  2 Aug 2001
The Homﬂy polynomial of the decorated
Hopf link
HUGH R. MORTON and SASCHA G. LUKAC 1
Department of Mathematical Sciences, University of Liverpool,
Peach St, Liverpool, L69 7ZL, England.
morton@liv.ac.uk, lukac@liv.ac.uk
Abstract
The main goal is to ﬁnd the Homﬂy polynomial of a link formed
by decorating each component of the Hopf link with the closure of a
directly oriented tangle. Such decorations are spanned in the Hom-
ﬂy skein of the annulus by elements Qλ, depending on partitions λ.
We show how the 2-variable Homﬂy invariant ⟨λ, µ⟩of the Hopf link
arising from decorations Qλ and Qµ can be found from the Schur
symmetric function sµ of an explicit power series depending on λ. We
show also that the quantum invariant of the Hopf link coloured by
irreducible sl(N)q modules Vλ and Vµ, which is a 1-variable speciali-
sation of ⟨λ, µ⟩, can be expressed in terms of an N × N minor of the
Vandermonde matrix (qij).
Keywords:
skein theory; Hopf link; Homﬂy polynomial; quantum
sl(N) invariants; symmetric functions; Schur functions; annulus; Hecke
algebras.
Introduction.
The roots of this paper lie in the work of Morton and Strickland, [11], where
the central role of the Hopf link in studying the invariants of satellite knots
became clear in the context of the coloured Jones invariants. The Hopf link
invariants also play a crucial part in the construction of 3-manifold invariants
based on the Jones polynomial. As noted in [11], the behaviour of the Hopf
link invariants for quantum groups such as sl(N)q was anticipated to be at
the heart of constructions of corresponding 3-manifold invariants for other
values of N > 2, as borne out by subsequent work such as that of Kohno and
Takata [5].
1Funded by DAAD under their HSP-III programme
1
It is of considerable interest to ﬁnd a general formula for the Homﬂy
polynomial of the Hopf link in which each component is decorated by, for
example, a closed braid. This will be a Laurent polynomial in the parameters
v and z, as used in [10], whose evaluation at the ‘sl(N) specialisation’, with
v = s−N and z = s −s−1, gives a Laurent polynomial in q = s2 which can be
viewed in terms of sl(N)q invariants of the Hopf link.
In this paper we give a formula in theorem 4.5 to determine the Homﬂy
polynomial ⟨λ, µ⟩of the Hopf link with components decorated by the closures
Qλ, Qµ of the Gyoja-Aiston idempotents, [2, 1], corresponding to any two
partitions λ, µ. Invariants determined using these decorations behave simply
under change of framing. The set {Qλ} spans a large subspace in the Homﬂy
skein of the annulus, including all elements represented by closed braids
or more general closed tangles without reverse strings.
Our calculations
therefore will ﬁnd in principle the Homﬂy polynomial of satellites of the
Hopf link with any such decorations and any framing.
As a key step in establishing the formula we present an attractive ex-
pression in theorem 4.2 for the sl(N) specialisation of ⟨λ, µ⟩as a Laurent
polynomial in the single variable q in terms of an N × N minor of the Van-
dermonde matrix (qij), when λ and µ each have at least N parts.
This
Laurent polynomial in q also determines, up to an explicit power of q, the
sl(N)q invariant of the Hopf link when its components are coloured by the
irreducible sl(N)q modules Vλ and Vµ.
Much of our work was originally inspired by a similar expression for the
further specialisation of this determinant to q = exp(2πi/r) used by Kohno
and Takata [5]. Our proofs for generic v and s do not draw on their work
and hence give an alternative skein theoretic way to interpret their formulae.
To describe and analyse the invariants under consideration we apply Hom-
ﬂy skein theory to the skein of the annulus and the Hecke algebras, coupled
with methods from the classical theory of symmetric functions. We start
with a brief review of this material before applying it to the Hopf link.
Much of the material in this paper appeared originally in the thesis of
Lukac, [6].
