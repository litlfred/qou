---
doc_id: arxiv-2504.18825v2
doc_title: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
toc_source: outline
doc_brief: "Murnaghan-Nakayama rule for the cyclotomic Hecke algebra and applications — We establish a Murnaghan–Nakayama rule for the irreducible characters of the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s"
---
MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE
ALGEBRA AND APPLICATIONS
NAIHUAN JING AND NING LIU
Abstract. We establish a Murnaghan–Nakayama rule for the irreducible characters of
the cyclotomic Hecke algebra Hm,n(q, u) on Shoji’s standard elements. Combined with
Shoji’s determinacy result, our formula provides a direct combinatorial route to the full
irreducible character table of Hm,n(q, u). Our construction is based on our recent multi-
parameter Murnaghan–Nakayama rule for Macdonald polynomials and specializes uni-
formly to several previously known formulas, including those for the complex reflection
group of type G(m, 1, n) and the Iwahori–Hecke algebras of types A and B. In a dual
framework, using the vertex operator realization of Schur functions, we also derive a com-
plementary iterative formula for irreducible characters on upper multipartitions, which
may be viewed as a dual Murnaghan–Nakayama rule.
As applications, we obtain a Regev-type formula and a L¨ubeck–Prasad–Adin–Roichman-
type formula for cyclotomic Hecke algebras, extending the corresponding formulas for the
Iwahori–Hecke algebra of type A and the complex reflection group, respectively. We fur-
ther introduce the notion of multiple bitrace for cyclotomic Hecke algebras and give a
general combinatorial formula for the multiple bitrace. As a specialization, this yields the
second orthogonality relation for irreducible characters of the complex reflection group
Wm,n. For practical computation, we also include in an appendix a SageMath implemen-
tation of our Murnaghan–Nakayama rule, which computes individual character values and
the full character table.
Contents
1.
Introduction
2
2.
Preliminaries
7
3.
Murnaghan–Nakayama rule for the cyclotomic Hecke algebra
12
4.
Special cases of the Murnaghan–Nakayama rule
18
5.
A dual Murnaghan–Nakayama rule via vertex operators
20
6.
Application I: Regev-type formula
25
7.
Application II: L¨ubeck–Prasad–Adin–Roichman-type formula
34
8.
Multiple bitrace for the irreducible characters
43
Appendix A.
An alternative proof of Corollary 6.3
49
Appendix B.
SageMath implementation of the Murnaghan–Nakayama rule
51
References
55
2020 Mathematics Subject Classification. Primary: 20C08; Secondary: 05E10, 17B69.
Key words and phrases. Murnaghan–Nakayama rule, cyclotomic Hecke algebra, Ariki–Koike algebra,
vertex operators, Regev formula, L¨ubeck–Prasad–Adin–Roichman formula, multiple bitrace.
1
arXiv:2504.18825v2  [math.RT]  11 Mar 2026
2
NAIHUAN JING AND NING LIU
