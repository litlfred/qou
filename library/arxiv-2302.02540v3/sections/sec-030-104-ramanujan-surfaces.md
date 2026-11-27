---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-030-104-ramanujan-surfaces
section_title: "Ramanujan surfaces"
section_number: 10.4
pages: 43-45
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
hyperbolic surfaceMof finite area isRamanujanifλ 1(M)≥1/4. We will also say thatM
isstrictly Ramanujanifλ 1(M)>1/4. Selberg’s eigenvalue conjecture [Sel65] states that
all congruence covers of the modular curve are Ramanujan (hence such surfaces could also
be calledSelberg). A related question is whether there exist closed Ramanujan surfaces in
every genus (see [Mon15, Question 1.1] and [Wri20, Problem 10.4]). Thanks to the work of
Hide and Magee [HM23] (see also [AM25, HMT25, MPvH25]), we now know that in large
44 MAXIME FORTIER BOURQUE AND BRAM PETRI
genus, there exist closed surfaces that arenearly Ramanujanin the sense that their first
eigenvalue is arbitrarily close to 1/4.
Observe that
λ1(M)>L⇐⇒N [0,L](M) = 1⇐⇒N [0,L](M)<2.
This means that one can prove lower bounds onλ 1 by boundingN [0,L] from above. In
particular,
λ1(M)> 1
4 ⇐⇒N small(M)<2⇐⇒ Nsmall(M)
2g−2 < 1
g−1
so the values in Table 6 give lower bounds on the systole that are sufficient for surfaces to
be strictly Ramanujan in genus 2 to 11. However, in obtaining these values we discarded
the term 1−bf(i/2) appearing in Theorem 10.1. The lower bounds on the systole (sufficient
to be strictly Ramanujan) that we have obtained by taking this term into account are listed
in Table 7 forgbetween 2 and 20 and plotted in Figure 2b. The corresponding ancillary file
isverify ramanujan.ipynb. According to Table 1, there exist hyperbolic surfaces with
systole larger than these bounds, hence strictly Ramanujan, in genus 2 to 7, 14, and 17. For
these specific surfaces, we can increaseLfurther as long asN [0,L] <2 to obtain improved
lower bounds onλ 1 still based only on the systole. The resulting bounds are listed in
Table 3 except in genus 2 to 4 where better data was already available. The corresponding
ancillary file isverify ramanujan examples.ipynb. These bounds are rigorous modulo
proving that the lower bounds on the systole in Table 1 are correct (as pointed out earlier,
some are rigorous but not all).
Table 7.Lower bounds on sys(M) sufficient forλ 1(M)>1/4.
genus lower bound on sys(M) sufficient forλ 1(M)>1/4 record systole
2 2.315 3.057141
3 3.218 3.983304
4 3.867 4.624499
5 4.380 4.91456
6 4.803 5.109
7 5.168 5.796298
8 5.482
9 5.760
10 6.010
11 6.236
12 6.443
13 6.632
14 6.808 6.887905
15 6.971
16 7.124
17 7.268 7.609407
18 7.403
19 7.531
20 7.651
It seems very likely that surfaces with systole larger than the values listed in Table 7
exist in the remaining genera up to 20 as well. However, our numerical experiments suggest
that this method cannot prove that the next Hurwitz surface (of genus 118) is Ramanujan
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 45
using only its systole. Based on Figure 1a, Figure 2b, and Theorem 6.4, it seems reasonable
to make the following conjecture.
Conjecture 10.4.There exist constantsc 1 >c 2 such that the smallest upper bound on the
systole that can be obtained from Theorem 6.1 and the smallest lower bound on the systole
sufficient to proveN small <2(equivalentlyλ 1 >1/4) using Theorem 10.1 are of the form
2 log(g) +cj +o(1)asg→∞.
It is unknown if there exist closed hyperbolic surfaces with systole asymptotic torlog(g)
for anyr >4/3, so even if the conjecture is true it is unlikely to be good enough to prove
the existence of Ramanujan surfaces in large genus.
