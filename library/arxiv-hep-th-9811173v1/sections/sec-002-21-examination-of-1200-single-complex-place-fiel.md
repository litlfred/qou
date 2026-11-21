---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-002-21-examination-of-1200-single-complex-place-fiel
section_title: "Examination of 1,200 single-complex-place fields"
section_number: 2.1
pages: 3-4
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.992
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
It became clear, from studying [@AMS:JB; @AMS:SB; @AMS:RK; @AMS:DZ], that there are unspecified rational relations of the form ([\[ab\]](#ab){reference-type="ref" reference="ab"}) between Dedekind zeta values and volumes of some, but not all, of the manifolds in the Hodgson--Weeks census. We soon found that 30 of the first 32 census manifolds have rational Dedekind-zeta invariants, with $a\le46$ and $b\le3$. The 2 exceptions are manifolds ${\rm m}003(-4,1)$ and ${\rm m}004(+7,1)$, whose invariant trace fields have 2 complex places.

The next step was to obtain systematic listings of fields with precisely one complex place. Thanks to the `numberfields` directory[^1] at the University of Bordeaux, we found files that order single-complex-place fields, for each degree $n\le7$, by the magnitudes, $-D$, of the discriminant. We selected the first 200 fields for each degree $n\in\{2,3,4,5,6,7\}$ and used the `zetak` command of Pari to compute 19 digits of the Dedekind zeta values, $\zeta_K(2)$, of these 1,200 fields. Forming $Z_K$, defined in ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}), we made $1200\times11031=13,237,200$ indiscriminate comparisons between these target fields and the census entries. This took 19 seconds on a 233MHz Pentium. We found 842 manifolds, with 175 distinct volumes, rationally related to 96 distinct Dedekind zeta values, with numerators and denominators of the rational invariants bounded by $a\le46$ and $b\le5$.

Since the census provided 17-digit volumes, the probability of any of these simple rational results being spurious is comfortably less than $10^{-12}$. Conversely, one needs only 5-digit precision for the volume to discover the rational Dedekind-zeta invariant in these 842 cases, and hence to obtain an accurate volume from ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}). Only for degrees $n\ge8$ do precision, core memory and CPUtime become issues. In the $n=12$ case of Table 12, with $|D|=12,476,239,474,594,496$, these issues require close attention.

The 96 fields that were caught by this 19-second trawl comprise all those of Tables 2 and 3 and all those above the lines drawn in Tables 4--7. Below the lines, and in Tables 8--12, we took assistance from Melbourne [@CGHN].

[^1]: `ftp://megrez.math.u-bordeaux.fr/pub/numberfields`
