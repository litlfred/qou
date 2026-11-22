---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-003-22-examination-of-44-fields-found-by-snap
section_title: "Examination of 44 fields found by Snap"
section_number: 2.2
pages: 4-5
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.99
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
For the remaining $140-96=44$ results of Tables 2--12, we made reference to the impressive body of files[^1] at the University of Melbourne. These were obtained by Coulson, Goodman, Hodgson and Neumann [@CGHN] (hereafter referred to as CGHN) using 50-digit precision, in marked distinction to the 5 digits which suffice for the findings above.

CGHN make no reference to Dedekind zeta values; they do, however, find single-complex-place invariant trace fields for about 9% of the Hodgson--Weeks manifolds. The next step was to examine the overlap between our single-complex-place fields and theirs. We found that the CGHN file `closed_census_algebras` contains 95 of our 96 single-complex-place fields. The exception was the quintic field with $D=-14103$, for which our low-precision method had readily yielded the rational invariant $a/b=2$ of the manifold ${\rm s}784(+5,2)$, which was absent from the file `closed_census_algebras`, obtained by CGHN from 50-digit searches for fields of degree[^2] not exceeding 16. We then referred to the file `closed.fields`, where ${\rm s}784(+5,2)$ indeed appears, with the expected invariant trace field, $x^5-2x^4+2x^3-x^2-2x-1$.

Thus assured that all our 96 finds were genuine, we extracted all of the invariant trace fields from the CGHN files `closed_census_algebras` and `closed.fields`, and asked Pari to determine their signatures and discriminants. This revealed 44 cases beyond the ranges of our search, namely the 32 below the lines in Tables 4--7 and the 12 in Tables 8--12. Within our selected ranges, CGHN had found all and only our 96 single-complex-place fields, indicating the reliability of both their methods and ours.

The next step was obvious, yet computationally demanding: to determine rational Dedekind-zeta invariants for the manifolds associated by Snap to the remaining 44 large-discriminant single-complex-place fields. The `zetak` command of Pari was entirely adequate to complete Tables 4--7, at 19-digit precision, yielding numerators and denominators bounded by $a\le976$ and $b\le5$, for which merely 7-digit precision would have been amply sufficient. The 12 fields of Tables 8--12 presented a much tougher computational challenge.

At degree $n=8$, Pari-GP 2.0.11 began to falter, with `zetak` yielding results drastically below the requested precision (as warned in the Pari manual) or running out of memory (when allocated 100MB of core). Accordingly we devised a method based on the `dirzetak` command, which returns the multiplicities, $m_K(n)$, of the ideals of $K$ with norm $n$, up to some requested maximum, $N$, that may comfortably extend to $N=10^6$. These multiplicities are the numerators of the Dirichlet series $$\zeta_K(2)=\sum_{n>0}\frac{m_K(n)}{n^2}\label{dirz}$$ We then computed the truncated sums $S_N:=\sum_{n=1}^N m_K(n)/n^2$, and accelerated their convergence by forming $T_{N,M}:=(S_N N-S_M M)/(N-M)$, with $M\approx\frac12N$. This removes a predictable $O(1/N)$ truncation error, leaving an $O(1/N^{3/2})$ "random-walk" error. With $N\le10^6$, we were able to achieve 10-digit precision, by averaging out fluctuations in $T_{N,M}$. Even in the most demanding case of Table 12, where the rational invariant is a 7-digit integer, we were left with 3 vanishing decimal places for $a/b=9408656.000\pm0.001$.

Hence we completed the task for Hodgson--Weeks manifolds. Tables 2--12 give $140$ single-complex-place invariant trace fields of closed census manifolds, of which 96 were detected by us without reference to CGHN. The 224 distinct census volumes rationally related to the Dedekind zeta values of these fields are given in Tables 13a-f. These 224 distinct volumes correspond to 998 of the 11,031 entries of the Hodgson--Weeks census file `ClosedManifolds` available[^3] from the Geometry Center at the University of Minnesota.

[^1]: ` http://www.ms.unimelb.edu.au/`$\,\widetilde{}\,$`snap`

[^2]: We later ran Snap at 100-digit precision, and found a group field of degree 20.

[^3]: The 1995 file ` ftp://ftp.geom.umn.edu/pub/software/snappea/tables/ClosedManifolds` contains 11,031 entries; unfortunately some of the Dehn fillings do not correspond to those packaged, internally, with SnapPea. We enlisted Snap, to check all the surgeries given in Tables 2--13.
