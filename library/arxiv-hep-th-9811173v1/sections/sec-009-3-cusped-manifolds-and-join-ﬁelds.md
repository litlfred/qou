---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-009-3-cusped-manifolds-and-join-ﬁelds
section_title: "Cusped manifolds and join ﬁelds"
section_number: 3
pages: 7-8
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
Now we turn to the study of cusped manifolds, complementary to kn ots and links. Pack-
aged with SnapPea [21], there are the 4,815 orientable cusped manifo lds of the Hildebrand–
Weeks census [9], triangulated by no more than 7 ideal tetrahedra, and 114 non-orientable
manifolds, triangulated by no more than 5. Making 4929 × 1200 comparisons with the
Dedekind zeta values of Section 2.1, we found 7 new single-complex-p lace ﬁelds, beyond
those from the Hodgson–Weeks census. Then the CGHN ﬁle cusped.fields conﬁrmed
these ﬁnds and yielded the remaining 5 ﬁelds of Table 14, with larger dis criminants. In
Table 14, we give the rational Dedekind-zeta invariant of a selected cusped manifold for
each of the 12 new ﬁelds.
Our tally of single-complex-place ﬁelds is now 96 + 44 + 7 + 5 = 152. Among the 4, 929
cusped manifolds, we found 312 whose volumes are rationally related to one of the 152
Dedekind zeta values, with numerators and denominators in (2) bou nded by a ≤ 2853
and b ≤ 7.
We also sought integer relations of the form
a vol(M) = b1ZK1 +b2ZK2 (18)
corresponding to a cusped or closed manifold M whose invariant trace ﬁeld is the join of
single-complex-place ﬁelds K1 and K2, or is a subﬁeld of this join. Restricting K1 and
K2 to the 152 ﬁelds of Tables 2–12 and Table 14, we found 91 census man ifolds, with 26
6
distinct volumes, rationally related, via (18), to pairs of Dedekind ze ta values. Details
of the 29 cusped and 62 closed manifolds are provided by Tables 15–1 8. Two of the 26
integer relations entail join ﬁelds noted in [7], namely the ﬁrst in Table 1 6 and the second
in Table 17. We used Pari’s nfisincl command to conﬁrm that all 6 of the quartic
invariant trace ﬁelds in Table 18 are subﬁelds of the octadic joins. In 4 of these 6 cases,
distinct values of b1/b 2 occur, for the same invariant trace ﬁeld.
We believe that we have exhausted the 3-term relations between ce nsus volumes and
pairs of the 152 target Dedekind zeta values. David Bailey’s impressiv ely eﬃcient, arbi-
trary precision [22], implementation of PSLQ [23] found the 91 relation s in 40 minutes
and then took 17 hours to exhaust the (4815 + 114 + 11031) ×
( 152
2
)
= 183, 156, 960 in-
discriminate possibilities. The PSLQ search rate was thus a healthy 3 k Hz. No reduction
to 3 distinct Dedekind zeta values was detected, presumably becau se the census volumes
are kept deliberately small.
