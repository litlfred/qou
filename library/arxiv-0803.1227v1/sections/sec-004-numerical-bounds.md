---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-004-numerical-bounds
section_title: "Numerical bounds"
section_number: null
pages: 7-9
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
Numerical programs give accurate approximations of the best linea r program-
ming bounds over a large interval of validity, not covered by the bou nds proved
in Section IV. The following curves plot the linear programming bound o n the
diversity functions as a function of the cardinality of the code. The programs
optimize the choice of a polynomial in the variables (cos θ1, . . . , cos θn), with
degree at most equal to some parameter D. Increasing D gives accurate re-
sults over a wider range of values for the diversity functions, but a lso increase
the computational time. We use D = 19 for n = 2 and D = 13 for n = 3.
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  500  1000  1500  2000  2500  3000
Diversity Sum
Cardinality
 Bounds for the Diversity Sum, n=2
Num degree=7
Num degree=19
7
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  50  100  150  200
Diversity Product
Cardinality
Bounds for the Diversity Product, n=2
Numerical degree=7
Numerical degree=19
Bound from dΣ (deg=19)
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  500  1000  1500  2000  2500  3000
Diversity Sum
Cardinality
 Bounds for the Diversity Sum, n=3
Num. degree=7
Num. degree=13
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  50  100  150  200
Diversity Product
Cardinality
Bounds for the Diversity Product, n=3
Numerical degree=7
Numerical degree=13
Bound from dΣ (deg=13)
8
N 24 48 64 80
bounds in [10] 0.6746 0.6193 0.5969 0.5799
B1 [7] 0.7598 0.6603 0.6131 0.5932
B2 [7] 0.7794 0.6734 0.6235 0.6026
LP dΣ 0.6547 0.5797 0.5488 0.5254
LP dΠ 0.5730 0.4989 0.4711 0.4504
N 100 120 128 1000
bounds in [10] 0.5632 0.5499 0.5452
B1 [7] 0.5578 0.5425 0.5347 0.3270
B2 [7] 0.5654 0.5496 0.5415 0.3285
LP dΣ 0.4999 0.4816 0.4753 0.2964
LP dΠ 0.4301 0.4144 0.4089 0.2574
Table 1: n = 2
N 24 48 64 80
LP dΣ 0.7178 0.6939 0.6797 0.6692
LP dΠ 0.6431 0.5942 0.5752 0.5628
N 100 120 128 1000
LP dΣ 0.6598 0.6532 0.6511 0.5586
LP dΠ 0.5482 0.5369 0.5332 0.4330
Table 2: n = 3
The Tables I and II compare the linear programming bounds for the d imen-
sions 2 and 3 with the previous results of [10] and [7] and show an impr ovement
in all cases.
These tables give upper bounds for the diversity when the cardinalit y N is
ﬁxed. All entries except the ones of the last line (LP dΠ ) are concerned with the
diversity sum. The second line tabulates the bounds settled in [10], ob tained
using Coxeter upper bounds. The two bounds of [7] were obtained using sphere
volume computations.
Moreover, concerning the diversity product, both our numerical results and
analytic results (compare (6) and (9)) show a large gap between th e bounds
for diversity sum and diversity product, in favor of the diversity pr oduct. This
is worth to point out since in previous publications bounds for the dive rsity
product were essentially deduced from the trivial inequality Σ V ≥ Π V and
hence appear to be weak.
