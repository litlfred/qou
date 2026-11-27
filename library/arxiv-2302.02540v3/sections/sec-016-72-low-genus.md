---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-016-72-low-genus
section_title: "Low genus"
section_number: 7.2
pages: 21-22
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
subintervals, and then optimize to find a single functionffor each subinterval. One
subtlety is that to get an upper bound onK(s) whensbelongs to an interval [a,b], we
need an upper bound on
sinh(s/2)
−sf(s)
forsin the same interval. Once we find a candidate upper bound numerically, we appro-
ximate sinh(s/2) ande−s2/2 by Taylor polynomials from the correct direction and then use
Sturm’s theorem to certify that the bound is valid (recall thatf(s) =p(s 2)e−s2/2 for some
polynomialp).
In other words, if we know thatf(s)<0 for everys∈[a,b], then
sinh(s/2)
−sf(s) ≤B⇐⇒sinh(s/2) +Bsp(s 2)e−s2/2≤0.
IfS n(x)≥sinh(x/2) andE n(x)≤e −x2/2 are polynomial approximations, then it suffices
to check that
Sn(x) +Bxp(x 2)En(x)<0,
on [a,b] (we are assuming thatp(x 2)<0 there, hence the reversed inequality forE n). We
can perform this verification by checking thatS n(x) +Bxp(x 2)En(x) is negative at one
point (using interval arithmetic) and has no zeros in [a,b] (using Sturm’s theorem). ForEn,
we simply take the odd degree Taylor polynomials of the exponential evaluated at−x 2/2
(the resulting series is alternating). ForS n, we use Taylor’s theorem with the Lagrange
form of the remainder to get
sinh(x/2) =
n−1X
j=0
(x/2)2j+1
(2j+ 1)! + cosh(ξx)(x/2)2n+1
(2n+ 1)!
for someξ x∈[0,x] and thus
sinh(x/2)≤
n−1X
j=0
(x/2)2j+1
(2j+ 1)! + cosh(b)(b/2)2n+1
(2n+ 1)!
for everyx∈[a,b]⊂[0,b]. We defineS n(x) by the above formula except that we replace
the last term involvingbby a rational approximation from above, so that the computer
can apply Sturm’s theorem reliably.
The upper bounds on 1
2 kiss that result from the above strategy are shown in Table 2
for genus 2 to 20 and verified in the ancillary fileverify kissing.ipynb. They improve
upon the previous best bounds in every genus exceptg= 2, where the optimal bound is 12
for the number of unoriented systoles [Sch94]. We remark that these upper bounds depend
in a very sensitive way on the upper bounds on the systole from Table 1, which are not as
small as possible because we took precautions to make sure that they were rigorous. Con-
sequently, the upper bounds in Table 2 could be decreased with more precision (especially
those towards the end of the table).
22 MAXIME FORTIER BOURQUE AND BRAM PETRI
Table 2.Bounds on the maximum of 1
2 kiss. The dagger indicates where
the linear programming bound fails to beat the previous best upper bound.
genus lower bound LP bound previous upper bound
2 12 [Jen84] 14† 12 [Sch94]
3 24 [Sch93] 34 126 [MRT14]
4 36 [Sch93] 62 244 [FBP22]
5 48 [Sch93] 97 383 [FBP22]
6 39 [Ham01] 138 547 [FBP22]
7 126 [Vog03] 185 736 [FBP22]
8 240 950 [FBP22]
9 70 [Sch93] 299 1186 [FBP22]
10 364 1446 [FBP22]
11 120 [Sch93] 434 1728 [FBP22]
12 510 2032 [FBP22]
13 144 [FBR22] 591 2358 [FBP22]
14 364 [Vog03] 677 2706 [FBP22]
15 168 [FBR22] 771 3074 [FBP22]
16 180 [FBR22] 868 3464 [FBP22]
17 336 [Vog03] 970 3874 [FBP22]
18 204 [FBR22] 1083 4305 [FBP22]
19 216 [FBR22] 1209 4756 [FBP22]
20 228 [FBR22] 1333 5227 [FBP22]
