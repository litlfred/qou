---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
---
A knot or link in S3 is hyperbolic if its complement admits a complete hyperbolic structure. A
braid on n strands, which is represented by a word in the braid group, w∈Bn, is hyperbolic if its
braid closure,Lw, is. Hyperbolic braids formed from three strands have been characterized by Futer,
Kalfagianni, and Purcell [7], a characterization that depends on their representation in the braid
group. B3 has two generators, σ1 and σ2 shown in Figure 1, and one relation σ1σ2σ1 = σ2σ1σ2.
The square of this element is commonly denoted by C, which is central. In [7, Theorem 5.5], Futer,
Kalfagianni, and Purcell have shown that S3−Lw is hyperbolic if and only if w is conjugate to
Ckσp1
1 σ−q1
2 ··· σps
1 σ−qs
2 with k∈ Z and pi, qi, and s positive integers, and w is not conjugate to
σp0
1 σq0
2 for some integers p0 and q0 (closures of such braids are either unknots, torus knots, or
connected sums of torus knots). The proof is by contradiction; they show the required hyperbolic
structures exist without constructing associated triangulations. In this paper, we construct geometric
triangulations for braids with k = 2, s = 1, p1≥ 1, and q1 = 1 thus oﬀering a direct proof of the
“if” direction of their theorem in these cases.
σ1 σ2
Figure 1. The generators of B3, the braid group on three strands.
Let Lp be the braid closure of C 2σp
1σ−1
2 with p≥ 1, which has one component if p is odd and
two if p is even. The complement of Lp is homeomorphic to the complement of a ( −2, 3,p + 6)-
pretzel (Corollary 5.6), so proving C 2σp
1σ−1
2 is hyperbolic will cover those pretzel knots and links as
well. To show C 2σp
1σ−1
2 is hyperbolic, we will ﬁrst decompose its complement into ideal tetrahedra
whose faces are identiﬁed in pairs (Section 2). These topological triangulations (one for each p) are
very much in the spirit of the canonical decompositions ﬁrst described for 2-bridge knot and link
complements by Sakuma and Weeks in [18]. It turns out that, as in the 2-bridge case detailed by
Date: June 24, 2022.
2020 Mathematics Subject Classiﬁcation. 57K32.
1
arXiv:2108.09349v2  [math.GT]  22 Jun 2022
2 BARBARA NIMERSHIEM
Futer in [9, Appendix], our triangulations are not just topological; they are also geometric (though
not canonical). In other words, each ideal tetrahedron can be given a hyperbolic shape of positive
volume and, when the faces are paired by hyperbolic isometries, the resulting hyperbolic structure
on S3−Lp is metrically complete.
To prove that our topological triangulations are geometric, we will employ the “Casson-Rivin
program” laid out by Futer and Gu´ eritaud in [5] — their survey of Casson and Rivin’s technique
for ﬁnding the hyperbolic structure on a 3-manifold whose boundary consists of tori. Gu´ eritaud has
implemented this program for punctured torus bundles and 4-punctured sphere bundles [9] and Futer
for 2-bridge knots [9, Appendix], whereas Gu´ eritaud and Schleimer have applied it to layered solid
tori and Dehn ﬁllings [10] and Ham and Purcell used the same procedure to determine geometric
triangulations on highly twisted links [11].
Geometric triangulations can lead to better understandings of the geometry of ﬁnite-volume
hyperbolic 3-manifolds, including simpler proofs. However, it is not known whether every such 3-
manifold admits a geometric triangulation. Currently the list of inﬁnite families of ﬁnite-volume
hyperbolic 3-manifolds that have been shown to admit geometric triangulations is short: punctured
torus bundles and 4-punctured sphere bundles [9], 2-bridge knots and links [9, Appendix], and certain
Dehn ﬁllings of fully-augmented 2-bridge knots and links [11]. The main result of this paper is that
the (−2, 3,n )-pretzel knots and links with n≥ 7 can be added to the list.
