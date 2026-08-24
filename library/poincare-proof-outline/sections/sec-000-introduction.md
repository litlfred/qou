---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 3-3
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Poincaré disc is a model of hyperbolic geometry. That fact has been a mathematical folklore for more than
100 years. However, up to the best of our knowledge, fully precise, formal proofs of this fact are lacking. In
this paper we present a formalization of the Poincaré disc model in Isabelle/HOL, introduce its basic notions
(h-points, h-lines, h-congruence, h-isometries, h-betweenness) and prove that it models Tarski’s axioms except
for Euclid’s axiom. We shown that is satisﬁes the negation of Euclid’s axiom, and, moreover, the existence of
limiting parallels axiom. The model is deﬁned within the extended complex plane, which has been described
quite precisely by Schwerdfeger [ 8] and formalized in the previous work of the ﬁrst two authors [ 5].
Related work. In 1840 Lobachevsky [ 3] published developments about non-Euclidean geometry. Hyperbolic
geometry is studied through many of its models. The concept of a projective disc model was introduced by Klein
while Poincaré investigated the half-plane model proposed by Liouville and Beltrami and primarily studied the
isometries of the hyperbolic plane that preserve orientation. In this paper, we focus on the formalization of the
latter.
Regarding non-Euclidean geometry, Makarios showed the independence of Euclid’s axiom [ 4]. He did so by
formalizing that the Klein–Beltrami model is a model of Tarski’s axioms at the exception of Euclid’s axiom.
Latter Coghetto formalized the Klein-Beltrami model within Mizar [ 1, 2].
