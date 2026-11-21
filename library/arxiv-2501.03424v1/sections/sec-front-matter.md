---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
arXiv:2501.03424v1  [math.RT]  6 Jan 2025
Soergel bimodules and Kazhdan-Lusztig
polynomials
ethan eugene wynner
University of California, Berkeley
Abstract
This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge-
bras, and their applications to various topics in Kazhdan-Lusztig theory. We ultimately exposit
a few of Soergel’s main results, which allowed him to give alternative proofs, using his theory, of
the Kazhdan-Lusztig conjectures. This paper should be viewed as a (very) condensed exposition
following the work of primarily Elias, Makisumi, Thiel, and Williamson in their lovely book Intro-
duction to Soergel Bimodules2. It is also important to note that much of Soergel’s theory has been
omitted from this paper in light of brevity, as well as the depth of proofs and lead-up information.
Many proofs concerning covered material are left out of this paper, again, due to their length, as
well as their residence in many of the texts listed in the references section. 5
1
Contents
1
Coxeter Systems, Hecke algebras, and Kazhdan-Lusztig preliminaries
4
1.1
Coxeter Systems
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.1.1
Remark: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.2
Hecke algebras
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.2.1
Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.3
Kazhdan-Lusztig polynomials, and a basis for the Hecke algebra
. . . . . . . . . . .
5
1.3.1
Lemma: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.3.2
Lemma: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2
Soergel Bimodules
6
2.1
Easing into it . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.1.1
Theorem (Chevalley-Shephard-Todd) . . . . . . . . . . . . . . . . . . . . . . .
6
2.1.2
Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Bott-Samelson bimodules
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2.1
Example of Soergel bimodule . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.2.2
Lemma
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.3
Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.4
Remark . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
Grothendieck groups, Soergel’s categorization . . . . . . . . . . . . . . . . . . . . . .
9
2.3.1
Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.3.2
Soergel’s Categoriﬁcation theorem
. . . . . . . . . . . . . . . . . . . . . . . .
9
2.3.3
Soergel’s Hom formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.3.4
Soergel’s conjecture
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.3.5
Important Remark . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3
Historical Interlude: The Kazhdan-Lusztig conjectures
11
3.1
Brieﬂy recognizing some Lie theory . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.1.1
Deﬁnition: Category O
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.1.2
Deﬁnition: Soergel module
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.2
Back to Kazhdan-Lusztig
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.2.1
Theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.2.2
The Kazhdan-Lusztig conjecture . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.2.3
Kazhdan-Lusztig Inversion Formula
. . . . . . . . . . . . . . . . . . . . . . .
12
3.2.4
Theorem (Polo) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.3
More on positivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.3.1
Flag and Schubert varieties . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
4
Soergel’s Proof of the Kazhdan-Lusztig conjecture
13
4.1
The V-functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
4.1.1
Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
4.1.2
Theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.1.3
Theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.2
Translation functors
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.2.1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.2.2
Lemma
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
2
4.2.3
Lemma
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.2.4
Lemma
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.2.5
Corollary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.3
Projectives
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.3.1
Proposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.4
Recontextualizing Soergel modules from Bott-Samelson modules
. . . . . . . . . . .
16
4.4.1
Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
4.4.2
Proposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
4.5
Proving the Kazhdan-Lusztig conjecture . . . . . . . . . . . . . . . . . . . . . . . . .
18
4.5.1
Restating the conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
4.5.2
Proposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
5
References
20
6
Appendic Miscellany
21
6.1
Computation of . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
6.2
Geometric representation of a Coxeter system . . . . . . . . . . . . . . . . . . . . . .
21
6.3
A fun but ancillary category
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
6.4
In aid of lemma 4.2.3,
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
6.4.1
Proposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
6.5
Berstein-Gelfand-Gelfand Reciprocity
. . . . . . . . . . . . . . . . . . . . . . . . . .
23
6.5.1
BGG Reciprocity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3
