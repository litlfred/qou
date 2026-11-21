---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-006-3-cusped-manifolds-and-join-fields
section_title: "Cusped manifolds and join fields"
section_number: 3
pages: 7-8
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
Now we turn to the study of cusped manifolds, complementary to knots and links. Packaged with SnapPea [@SnapPea], there are the 4,815 orientable cusped manifolds of the Hildebrand--Weeks census [@HiW], triangulated by no more than 7 ideal tetrahedra, and 114 non-orientable manifolds, triangulated by no more than 5. Making $4929\times1200$ comparisons with the Dedekind zeta values of Section 2.1, we found 7 new single-complex-place fields, beyond those from the Hodgson--Weeks census. Then the CGHN file `cusped.fields` confirmed these finds and yielded the remaining 5 fields of Table 14, with larger discriminants. In Table 14, we give the rational Dedekind-zeta invariant of a selected cusped manifold for each of the 12 new fields.

Our tally of single-complex-place fields is now $96+44+7+5=152$. Among the $4,929$ cusped manifolds, we found 312 whose volumes are rationally related to one of the 152 Dedekind zeta values, with numerators and denominators in ([\[ab\]](#ab){reference-type="ref" reference="ab"}) bounded by $a\le2853$ and $b\le7$.

We also sought integer relations of the form $$a\,{\rm vol}({\cal M})=b_1Z_{K_1}+b_2Z_{K_2}
\label{ab12}$$ corresponding to a cusped or closed manifold ${\cal M}$ whose invariant trace field is the join of single-complex-place fields $K_1$ and $K_2$, or is a subfield of this join. Restricting $K_1$ and $K_2$ to the 152 fields of Tables 2--12 and Table 14, we found 91 census manifolds, with 26 distinct volumes, rationally related, via ([\[ab12\]](#ab12){reference-type="ref" reference="ab12"}), to pairs of Dedekind zeta values. Details of the 29 cusped and 62 closed manifolds are provided by Tables 15--18. Two of the 26 integer relations entail join fields noted in [@CGHN], namely the first in Table 16 and the second in Table 17. We used Pari's `nfisincl` command to confirm that all 6 of the quartic invariant trace fields in Table 18 are subfields of the octadic joins. In 4 of these 6 cases, distinct values of $b_1/b_2$ occur, for the same invariant trace field.

We believe that we have exhausted the 3-term relations between census volumes and pairs of the 152 target Dedekind zeta values. David Bailey's impressively efficient, arbitrary precision [@TRANSMP], implementation of PSLQ [@PSLQ] found the 91 relations in 40 minutes and then took 17 hours to exhaust the $(4815+114+11031)\times{152\choose2}=183,156,960$ indiscriminate possibilities. The PSLQ search rate was thus a healthy 3 kHz. No reduction to 3 distinct Dedekind zeta values was detected, presumably because the census volumes are kept deliberately small.
