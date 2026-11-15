---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-7
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
DERIVED CATEGORIES
AMNON YEKUTIELI
Dedicated to Alexander Grothendieck, in Memoriam
Abstract. This is the fourth (and last) prepublication version of a book on
derived categories, that will be published by Cambridge University Press. The
purpose of the book is to provide solid foundations for the theory of derived
categories, and to present several applications of this theory in commutative
and noncommutative algebra. The emphasis is on constructions and examples,
rather than on axiomatics.
Here is a brief description of the book. After a review of standard facts
on abelian categories, we study diﬀerential graded algebra in depth (including
DG rings, DG modules, DG categories and DG functors).
We then move to triangulated categories and triangulated functors between
them, and explain how they arise from the DG background. Speciﬁcally, we
talk about the homotopy category K(A, M) of DG A-modules in M, where A
is a DG ring and M is an abelian category. The derived category D(A, M) is
the localization of K(A, M) with respect to the quasi-isomorphisms. We deﬁne
the left and right derived functors of a triangulated functor, and prove their
uniqueness. Existence of derived functors relies on having enough K-injective,
K-projective or K-ﬂat DG modules, as the case may be. We give constructions
of resolutions by such DG modules in several important algebraic situations.
There is a detailed study of the derived Hom and tensor bifunctors, and
the related adjunction formulas. We talk about cohomological dimensions of
functors and how they are used.
The last sections of the book are more specialized. There is a section on
dualizing and residue complexes over commutative noetherian rings, as deﬁned
by Grothendieck. We introduce Van den Bergh rigidity in this context. The
algebro-geometric applications of commutative rigid dualizing complexes are
outlined.
A section is devoted to perfect DG modules and tilting DG bimodules over
NC (noncommutative) DG rings. This includes theorems on derived Morita
theory and on the structure of the NC derived Picard group.
Three sections are on NC connected graded rings. In the ﬁrst of them we
give some basic deﬁnitions and results on algebraically graded rings, including
Artin-Schelter regular rings. The second section is on derived torsion for NC
connected graded rings, it relation to the χ condition of Artin-Zhang, and the
NC MGM Equivalence. In the third section we introduce balanced dualizing
complexes, and we prove their uniqueness, existence and trace functoriality.
The ﬁnal section of the book is on NC rigid dualizing complexes, following
Van den Bergh. We prove the uniqueness and existence of these complexes,
give a few examples, and discuss their relation to Calabi-Yau rings.
Feedback from readers (corrections and suggestions) is most welcome.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
1
arXiv:1610.09640v4  [math.CT]  14 Apr 2019
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Contents
0.
Introduction
7
0.1.
On the Subject
7
0.2.
A Motivating Discussion: Duality
9
0.3.
On the Book
13
0.4.
Synopsis of the Book
14
0.5.
What Is Not in the Book
22
0.6.
Prerequisites and Recommended Bibliography
23
0.7.
Credo, Writing Style and Goals
23
0.8.
Acknowledgments
24
1.
Basic Facts on Categories
25
1.1.
Set Theory
25
1.2.
Notation and Conventions
25
1.3.
Epimorphisms and Monomorphisms
26
1.4.
Products and Coproducts
27
1.5.
Equivalence of Categories
28
1.6.
Bifunctors
29
1.7.
Representable Functors
29
1.8.
Inverse and Direct Limits
30
2.
Abelian Categories and Additive Functors
33
2.1.
Linear Categories
33
2.2.
Additive Categories
33
2.3.
Abelian Categories
34
2.4.
A Method for Producing Proofs in Abelian Categories
38
2.5.
Additive Functors
42
2.6.
Projective Objects
46
2.7.
Injective Objects
47
3.
Diﬀerential Graded Algebra
51
3.1.
Graded Algebra
51
3.2.
DG K-Modules
58
3.3.
DG Rings and Modules
59
3.4.
DG Categories
62
3.5.
DG Functors
64
3.6.
Complexes in Abelian Categories
65
3.7.
The Long Exact Cohomology Sequence
66
3.8.
The DG Category C(A, M)
71
3.9.
Contravariant DG Functors
74
4.
Translations and Standard Triangles
79
4.1.
The Translation Functor
79
4.2.
The Standard Triangle of a Strict Morphism
82
4.3.
The Gauge of a Graded Functor
83
4.4.
The Translation Isomorphism of a DG Functor
84
4.5.
Standard Triangles and DG Functors
85
4.6.
Examples of DG Functors
87
5.
Triangulated Categories and Functors
91
5.1.
Triangulated Categories
91
5.2.
Triangulated and Cohomological Functors
94
5.3.
Some Properties of Triangulated Categories
96
5.4.
The Homotopy Category is Triangulated
102
5.5.
From DG Functors to Triangulated Functors
109
5.6.
The Opposite Homotopy Category is Triangulated
110
6.
Localization of Categories
113
3
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
6.1.
The Formalism of Localization
113
6.2.
Ore Localization
114
6.3.
Localization of Linear Categories
124
7.
The Derived Category D(A, M)
127
7.1.
Localization of Triangulated Categories
127
7.2.
Deﬁnition of the Derived Category
132
7.3.
Boundedness Conditions in K(A, M)
135
7.4.
Thick Subcategories of M
138
7.5.
The Embedding of M in D(M)
139
7.6.
The Opposite Derived Category is Triangulated
140
8.
Derived Functors
143
8.1.
2-Categorical Notation
143
8.2.
Functor Categories
145
8.3.
Abstract Derived Functors
147
8.4.
Triangulated Derived Functors
155
8.5.
Contravariant Triangulated Derived Functors
162
9.
DG and Triangulated Bifunctors
165
9.1.
DG Bifunctors
165
9.2.
Triangulated Bifunctors
167
9.3.
Derived Bifunctors
171
10.
Resolving Subcategories of K(A, M)
175
10.1.
K-Injective DG Modules
175
10.2.
K-Projective DG Modules
179
10.3.
K-Flat DG Modules
181
10.4.
Opposite Resolving Subcategories
182
11.
Existence of Resolutions
185
11.1.
Direct and Inverse Limits of Complexes
185
11.2.
Totalizations
187
11.3.
K-Projective Resolutions in C−(M)
194
11.4.
K-Projective Resolutions in C(A)
200
11.5.
K-Injective Resolutions in C+(M)
208
11.6.
K-Injective Resolutions in C(A)
214
12.
Adjunctions, Equivalences and Cohomological Dimension
221
12.1.
Boundedness Conditions Revisited
221
12.2.
The Bifunctor RHom
223
12.3.
The Bifunctor ⊗L
225
12.4.
Cohomological Dimensions of Functors and Objects
227
12.5.
Theorems on Functors Satisfying Finiteness Conditions
231
12.6.
Derived Restriction, Induction and Coinduction Functors
235
12.7.
DG Ring Quasi-Isomorphisms
238
12.8.
Existence of DG Ring Resolutions
240
12.9.
The Derived Tensor-Evaluation Morphism
245
12.10.
Hom-Tensor Formulas for Weakly Commutative DG Rings
248
13.
Dualizing Complexes over Commutative Rings
253
13.1.
Dualizing Complexes
253
13.2.
Interlude: The Matlis Classiﬁcation of Injective Modules
263
13.3.
Residue Complexes
265
13.4.
Van den Bergh Rigidity
273
13.5.
Rigid Dualizing and Residue Complexes
280
14.
Perfect and Tilting DG Modules over NC DG Rings
285
14.1.
Algebraically Perfect DG Modules
285
14.2.
Derived Morita Theory
295
4
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
14.3.
DG Bimodules over K-Flat DG Rings
302
14.4.
Tilting DG Bimodules
308
14.5.
Tilting Bimodule Complexes over Rings
314
15.
Algebraically Graded Noncommutative Rings
323
15.1.
Categories of Algebraically Graded Modules
323
15.2.
Properties of Algebraically Graded Modules
331
15.3.
Resolutions and Derived Functors
338
15.4.
Artin-Schelter Regular Graded Rings
345
16.
Derived Torsion over NC Graded Rings
351
16.1.
Quasi-Compact Finite Dimensional Functors
351
16.2.
Weakly Stable and Idempotent Copointed Functors
355
16.3.
Graded Torsion: Weak Stability and Idempotence
358
16.4.
Representability of Derived Torsion
367
16.5.
Symmetry of Derived Torsion
371
16.6.
NC MGM Equivalence
377
17.
Balanced Dualizing Complexes over NC Graded Rings
385
17.1.
Graded NC Dualizing Complexes
385
17.2.
Balanced DC: Deﬁnition, Uniqueness and Local Duality
389
17.3.
Balanced DC: Existence
392
17.4.
Balanced Trace Morphisms
402
18.
Rigid Noncommutative Dualizing Complexes
411
18.1.
Noncommutative Dualizing Complexes
411
18.2.
Rigid NC DC: Deﬁnition and Uniqueness
418
18.3.
Interlude: Graded Rings of Laurent Type
425
18.4.
Graded Rigid NC DC
429
18.5.
Filtered Rings and Existence of Rigid NC DC
435
18.6.
Twisted Calabi-Yau Rings
440
References
447
Index
454
5
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
