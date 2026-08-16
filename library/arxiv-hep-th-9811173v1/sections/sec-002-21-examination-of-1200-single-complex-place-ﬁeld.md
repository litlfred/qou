---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-002-21-examination-of-1200-single-complex-place-ﬁeld
section_title: "Examination of 1,200 single-complex-place ﬁelds"
section_number: 2.1
pages: 3-4
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
It became clear, from studying [16, 17, 18, 19], that there are uns peciﬁed rational rela-
tions of the form (2) between Dedekind zeta values and volumes of s ome, but not all,
of the manifolds in the Hodgson–Weeks census. We soon found that 30 of the ﬁrst 32
census manifolds have rational Dedekind-zeta invariants, with a ≤ 46 and b ≤ 3. The 2
exceptions are manifolds m003( −4, 1) and m004(+7, 1), whose invariant trace ﬁelds have
2 complex places.
The next step was to obtain systematic listings of ﬁelds with precisely one complex
place. Thanks to the numberfields directory2 at the University of Bordeaux, we found
ﬁles that order single-complex-place ﬁelds, for each degree n ≤ 7, by the magnitudes, −D,
of the discriminant. We selected the ﬁrst 200 ﬁelds for each degree n ∈ {2, 3, 4, 5, 6, 7} and
used the zetak command of Pari to compute 19 digits of the Dedekind zeta values, ζK(2),
2ftp://megrez.math.u-bordeaux.fr/pub/numberfields
2
of these 1,200 ﬁelds. Forming ZK, deﬁned in (1), we made 1200 × 11031 = 13 , 237, 200
indiscriminate comparisons between these target ﬁelds and the cen sus entries. This took
19 seconds on a 233MHz Pentium. We found 842 manifolds, with 175 dis tinct volumes,
rationally related to 96 distinct Dedekind zeta values, with numerato rs and denominators
of the rational invariants bounded by a ≤ 46 and b ≤ 5.
Since the census provided 17-digit volumes, the probability of any of these simple
rational results being spurious is comfortably less than 10 − 12. Conversely, one needs only
5-digit precision for the volume to discover the rational Dedekind-z eta invariant in these
842 cases, and hence to obtain an accurate volume from (1). Only f or degrees n ≥ 8 do
precision, core memory and CPUtime become issues. In the n = 12 case of Table 12, with
|D| = 12, 476, 239, 474, 594, 496, these issues require close attention.
The 96 ﬁelds that were caught by this 19-second trawl comprise all those of Tables 2
and 3 and all those above the lines drawn in Tables 4–7. Below the lines, and in Tables 8–
12, we took assistance from Melbourne [7].
