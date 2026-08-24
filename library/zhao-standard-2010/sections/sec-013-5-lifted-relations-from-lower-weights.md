---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-013-5-lifted-relations-from-lower-weights
section_title: "Lifted relations from lower weights"
section_number: 5
pages: 14-16
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Note that when N = 3 there are no weight one relations nor (regularized)
distribution relations. When we deal with MZVs (resp. alter nating Euler sums)
we expect that all the linear relations come from RDS (resp. R DS and RDT).
Since there is no weight one relation when level N ≤ 3 it is natural to ask if
RDS and RDT are enough when N = 3. Surprisingly, the answer is no.
The ﬁrst counterexample is in weight four, i.e., ( w, N) = (4 , 3). Easy compu-
tation shows that there are 144 MPVs in this case among which t here are 239
nontrivial RDS of weight four which include 191 FDS of weight four (see (9)
and (10)). Furthermore, it is easy to verify that all the seve n RDT (including
four FDT) can be derived from RDS. Using these relations we ge t 127 indepen-
dent linear relations among the 144 MPVs. But we have d(4, 3) ≤ 16 by [17,
5.25], so there must be at least one more linearly independen t relation. Where
else can we ﬁnd it? The answer is the so-called lifted relations..
We know that a product of two weight two MPVs is of weight four. So on
each of the ﬁve RDS (including two FDS) of weight two in MPV (2, 3) we can
multiply any one of the nine MPVs of ( w, N) = (2 , 3) to get a relation in
MPV (4, 3). For instance, we have a FDS
Z(y1,1 ∗ y1,1 − y1,1xy1,1) = L3(2|2) + 2L3(1, 1|1, 1) − L3(1, 1|1, 0) = 0 .
Multiplying by L3(1, 1|1, 1) = Z(y1,1y1,2) we obtain a new relation which is
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 15
linearly independent from RDS of weight four in MPV (4, 3):
Z
(
y1,1y1,2x(y2,0 + 2y1,1y1,2 − 2y1,1y1,0)
)
=L3(1, 1, 2|1, 1, 0) + 2L3(1, 2, 1|1, 1, 0) + 2L3(2, 1, 1|1, 1, 0)
+L3(2, 1, 1|2, 2, 1) + 4L3({1}4|1, 1, 2, 1) + 8L3({1}4|1, 0, 1, 0)
−6L3({1}4|1, 0, 0, 1) − 4L3({1}4|1, 0, 1, 2) − 2L3({1}4|1, 1, 2, 0) = 0 .
Such relations coming from the lower weights are called lifted relations. In
this way, when ( w, N) = (4 , 3) we can produce 45 lifted RDS relations from
weight two, 58 from weight three. We may also lift RDT and obta in nine
and six relations from weight two and three, respectively. H owever, all the
lifted relations together only produce one new linearly ind ependent relation, as
expected. Hence we ﬁnd totally 128 linearly independent rel ations among the
144 MPVs with ( w, N) = (4 , 3). This implies that d(4, 3) ≤ 16 which is the
same bound obtained by [17, 5.25] and is proved to be exact und er a variant
of Grothendieck’s period conjecture by Deligne [16].
For levels N ≥ 4 one may lift not only RDS and RDT but also the weight
one relations. But by a moment reﬂection one sees that the lif ted weight one
relations are still weight one relations by themselves so on e doesn’t really need
to consider them after all.
Definition 5.1. We call a Q-linear relation among MPVs standard if it can
be produced by some Q-linear combinations of the following four families of
relations: regularized double shuﬄe relations, regulariz ed distribution relations,
weight one relations, and lifted relations from the above. O therwise, it is called
a non-standard relation.
In general, there are no inclusion relations among the four f amilies of the stan-
dard relations.
Computation in small weight cases supports the following
Conjecture 5.2. Suppose N = 3 or 4. Every MPV of level N is a linear
combination of MPVs of the form L({1}w|t1, . . . , tw) with tj ∈ { 1, 2}. Con-
sequently, the Q-dimension of the MPVs of weight w and level N is given by
d(w, N) = 2 w for all w ≥ 1.
Remark 5.3. The data in Table 2 in §7 shows that one cannot produce enough
relations by using only the standard relations when ( w, N) = (3 , 4). In fact,
even though one has d(3, 4) ≤ 8 and d(4, 4) ≤ 16 by [17, 5.25], one can only
show that d(3, 4) ≤ 9 and d(4, 4) ≤ 21 by using only the standard relations.
However, thanks to the octahedral symmetry of P1 − ({0, ∞} ∪µ 4) one can ﬁnd
(presumably all) the non-standard relations in these two ca ses (see Thm. 9.1).
Remark 5.4. Let N = 2, 3, 4 or 8. Assuming a variant of Grothendieck’s period
conjecture, Deligne [16] constructed explicitly a set of ba sis for MPV (w, N).
His results would also imply that d(w, 2) is given by the Fibonacci numbers,
d(w, 3) = d(w, 4) = 2 w, and d(w, 8) = 3 w under Grothendieck’s period conjec-
ture.
Documenta Mathematica 15 (2010) 1–34
