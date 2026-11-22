---
doc_id: arxiv-2510.04782v2
doc_title: "$q$-Hodge complexes over the Habiro ring"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 2510.04782v2.pdf
source_sha256: 591d0bdf2c48d12f
toc_source: outline
doc_brief: "$q$-Hodge complexes over the Habiro ring — — Peter Scholze has raised the question whether some variant of the q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧ (qm−1)."
---
q-Hodge complexes over the Habiro ring
Ferdinand Wagner
October 9, 2025
Abstract. — Peter Scholze has raised the question whether some variant of the
q-de Rham complex is already defined over the Habiro ring H := limm∈N Z[q]∧
(qm−1).
Such a variant should then be called (algebraic) Habiro cohomology.
We show that algebraic Habiro cohomology exists whenever the q-de Rham
complex can be equipped with a q-Hodge filtration: a q-deformation of the Hodge
filtration, subject to some reasonable conditions. To any such q-Hodge filtration we
associate a small modification of the q-de Rham complex, which we call the q-Hodge
complex, and show that it descends canonically to the Habiro ring. This construction
recovers and generalises the Habiro ring of a number field from [GSWZ24] and
is closely related to the q-de Rham–Witt complexes from [Wag24] as well as,
conjecturally, to Scholze’s analytic Habiro stack [Sch25].
While there’s no canonical q-Hodge filtration in general, we show that it does
exist in many cases of interest. For example, for a smooth scheme X over Z, the
q-de Rham complex q9ΩX/Z can be equipped with a canonical q-Hodge filtration as
soon as one inverts all primes p ⩽dim(X/Z).
Contents
1. Introduction
3
1.1. Habiro cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.2. q-Hodge filtrations and Habiro descent . . . . . . . . . . . . . . . . . . . . . . .
4
1.3. Existence results for q-Hodge filtrations
. . . . . . . . . . . . . . . . . . . . . .
7
1.4. Organisation of this paper . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2. Habiro rings of étale extensions
13
2.1. A general descent principle
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.2. Habiro rings of étale extensions . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
3. Habiro descent for q-Hodge complexes
20
3.1. q-Hodge filtrations and the q-Hodge complex
. . . . . . . . . . . . . . . . . . .
20
3.2. The main result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3.3. Deformations of q-de Rham–Witt complexes . . . . . . . . . . . . . . . . . . . .
28
3.4. The Nygaard filtration on q-de Rham–Witt complexes . . . . . . . . . . . . . .
32
3.5. The twisted q-Hodge filtration . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3.6. Habiro descent for q-Hodge complexes . . . . . . . . . . . . . . . . . . . . . . .
45
1
arXiv:2510.04782v2  [math.AG]  8 Oct 2025
Contents
3.7. Habiro descent for q-de Rham complexes . . . . . . . . . . . . . . . . . . . . . .
48
3.8. Habiro descent in derived commutative algebras . . . . . . . . . . . . . . . . . .
50
4. Functorial q-Hodge filtrations
53
4.1. Functorial q-Hodge filtrations away from small primes . . . . . . . . . . . . . .
53
4.2. Functorial q-Hodge filtrations for certain quasi-regular quotients
. . . . . . . .
60
A. The q-de Rham complex
69
A.1. Rationalised q-crystalline cohomology
. . . . . . . . . . . . . . . . . . . . . . .
70
A.2. The global q-de Rham complex . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
B. Habiro-completion
77
References
81
2
