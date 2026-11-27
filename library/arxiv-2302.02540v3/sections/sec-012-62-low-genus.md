---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-012-62-low-genus
section_title: "Low genus"
section_number: 6.2
pages: 11-12
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
optimization are listed in Table 1 for 2≤g≤20. The verification of these values is done
in the ancillary fileverify systole.ipynb. They are lower than the previous best upper
bounds except in genus 2 where the optimal bound is 2 arccosh(1+
√
2)≈3.057142 [Jen84].
In all other genera, the previous best upper bound was Bavard’s inequality [Bav96]
(6.1) sys(M)≤2 arccosh
 1
2 sin(π/(12g−6))

,
which comes from a sharp upper bound on the radius of an embedded disk inM.
We have also listed the largest recorded value of the systole in some genera. Those listed
in genus 7, 14, and 17 come from Hurwitz surfaces (these are (2,3,7)-triangle surfaces as
defined in Section 9.2). Technically, the values from [Vog03] and [SS22] were obtained by
numerical calculations in triangle groups and are not completely rigorous, but they could
be made rigorous in principle (this was done in [DT00] for the Klein quartic and in [Woo01]
for the Hurwitz surfaces of genus 14). For Hurwitz surfaces, the calculations from [SS22]
corroborate those of [Vog03].
Since the systole does not decrease under covers, one could fill in all the blanks in the
table with values in lower genera. Similarly, the value listed in genus 13 persists in every
genusg >13 [FBR22]. We decided not to list these since better constructions surely exist.
12 MAXIME FORTIER BOURQUE AND BRAM PETRI
Table 1.Bounds on the maximum of sys. The dagger indicates where the
linear programming bound fails to beat the previous best upper bound.
genus lower bound LP bound previous upper bound
2 3.057141 [Jen84] 3.156053† 3.057142 [Jen84]
3 3.983304 [Sch93] 4.194719 4.494373 [Bav96]
4 4.624499 [Sch93] 4.876863 5.176481 [Bav96]
5 4.91456 [Sch94] 5.381937 5.682841 [Bav96]
6 5.109 [CB05] 5.783671 6.086062 [Bav96]
7 5.796298 [Vog03] 6.117160 6.421249 [Bav96]
8 6.407734 6.708126 [Bav96]
9 5.376 [Sch93] 6.655635 6.958903 [Bav96]
10 6.880869 7.181671 [Bav96]
11 5.980406 [Sch93] 7.080715 7.382068 [Bav96]
12 7.262735 7.564184 [Bav96]
13 5.909039 [FBR22] 7.429527 7.731080 [Bav96]
14 6.887905 [Woo01, Vog03] 7.584859 7.885106 [Bav96]
15 7.729299 8.028108 [Bav96]
16 7.863529 8.161558 [Bav96]
17 7.609407 [Vog03] 7.988773 8.286655 [Bav96]
18 8.118854 8.404383 [Bav96]
19 7.358 [SS22] 8.220710 8.515562 [Bav96]
20 8.328393 8.620882 [Bav96]
