---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-020-82-low-genus
section_title: "Low genus"
section_number: 8.2
pages: 26-28
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
optimization are presented in Table 3 for 2≤g≤20 and their verification is done in the
fileverify lambda.ipynb. Our bounds are smaller than the previous best upper bounds
in every genus except 2, 3, 4, and 6 where bounds from [KMcP24], [Bon22] or [YY80] are
better.
Some comments on the examples we used for the lower bounds are in order:
•Contrary to the other invariants considered in this paper, it is not known if the
supremum ofλ 1 is attained. For instance, we do not know if the entries equal to
1/4 in the table are attained (see below).
•In genus 2 and 3, the upper bounds from [KMcP24, Bon22] are tantalizingly close to
the value ofλ 1 at the Bolza surface and the Klein quartic approximated numerically
in [SU13] and [Coo18] respectively, so these surfaces are the conjectured maximizers
in these genera. The authors of [KMcP24] reproduced Cook’s numerical calculations
with more precision, arriving at the value 2.6779 instead of 2.6767 for the Klein
quartic. The surface in genus 4 is Bring’s curve. Note that the values in genus
3 and 4 are based on finite element methods and are not rigorous. The value in
genus 2 is obtained using the trace formula and can be made rigorous according to
Strohmaier and Uski.
•In genus 7, Mathieu Pineault calculated numerically that the Fricke–Macbeath
curveFsatisfiesλ 1(F)≈1.239 [Pin24] and it was shown thatλ 1(F)∈[1.23,1.26]
in [Lee23].
•In genus 5 to 6, 14, and 17, we apply linear programming to some of the surfaces
listed in Table 1 to obtain lower bounds on their first eigenvalue based on their
systole (see Section 10.4). The true value ofλ 1 for these surfaces is certainly
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 27
Table 3.Bounds on the supremum ofλ 1. The daggers indicate where the
linear programming bounds fail to beat the previous best upper bound.
genus lower bound LP bound previous upper bound
2 3.838887 [SU13] 4.625307† 3.838898 [KMcP24, Bon22]
3 2.6779 [Coo18] 2.816427† 2.678483 [KMcP24, Bon22]
4 1.91556 [Coo18] 2.173806† 2.000000 [YY80]
5 0.728167 (§10.4) 1.836766 1.852651 [KMcP24]
6 0.486360 (§10.4) 1.625596† 1.600000 [YY80]
7 1.23 [Lee23] 1.480008 1.513268 [KMcP24]
8 0.25 [BS07]+[BBD88] 1.372804 1.406905 [KMcP24]
9 0.25 [BS07]+[BBD88] 1.289024 1.323482 [KMcP24]
10 0.25 [BS07]+[BBD88] 1.222189 1.256022 [KMcP24]
11 0.25 [BS07]+[BBD88] 1.168169 1.200153 [KMcP24]
12 0.25 [BS07]+[BBD88] 1.122327 1.152986 [KMcP24]
13 0.25 [BS07]+[BBD88] 1.083260 1.112535 [KMcP24]
14 0.287470 (§10.4) 1.049217 1.077385 [KMcP24]
15 0.25 [BS07]+[BBD88] 1.018005 1.046501 [KMcP24]
16 0.25 [BS07]+[BBD88] 0.991735 1.019105 [KMcP24]
17 0.403200 (§10.4) 0.968260 0.994601 [KMcP24]
18 0.25 [BS07]+[BBD88] 0.947180 0.972525 [KMcP24]
19 0.25 [BS07]+[BBD88] 0.928091 0.952510 [KMcP24]
20 0.25 [BS07]+[BBD88] 0.911390 0.934260 [KMcP24]
larger than the estimates we give since we discard all the geometric terms and
the contribution of higher eigenvalues in the Selberg trace formula, while the test
functions we use have only finitely many zeros.
•IfX→Yis a finite-sheeted covering of hyperbolic orbifolds, thenλ 1(Y)≥λ 1(X)
since any eigenfunction onYlifts to an eigenfunction onXwith the same eigen-
value. We will use this in the next bullet point.
•For the entries equal to 1/4 in the table, we use the fact that Selberg’s conjecture
is known to hold for the congruence subgroups Γ 1(N) of square-free levelN <857
[BS07]. Since Γ 1(N)<Γ 0(N) as a finite-index subgroup, the conjecture also holds
for Γ 0(N) for the same levels. If Γ j(N) is torsion-free, thenX j(N) :=H 2/Γj(N)
(j= 0,1) has no cone points and we can join its cusps in pairs to create thin
handles following [BBD88]. By the results in that paper, the spectrum of the
plumbed surface will be close to that ofX j(N) (which has a discrete spectrum
and a continuous spectrum equal to [1/4,∞) like all cusped surfaces). Since the
spectral gap ofX j(N) is 1/4 for square-freeN <857 [BS07], the plumbed surfaces
thus haveλ 1 as close to 1/4 as we wish in these cases. The genus of the plumbed
surfaces is equal to the genus ofX j(N) plus half its number of cusps. Table 4
shows which congruence group we use for each genus concerned. The fact that
these groups are indeed torsion free and that their signatures are as listed can be
found in [Miy06, Section 4.2]. This information about congruence groups is also
implemented inSage.
•There are other well-known ways of proving lower bounds onλ 1. The first of these
is Cheeger’s inequalityλ 1≥h 2/4 wherehis the Cheeger constant [Che70]. In high
genus, this cannot be used to prove a lower bound of more than 1
π2 ≈0.1013...
28 MAXIME FORTIER BOURQUE AND BRAM PETRI
onλ 1 [BCP25]. However, it is not clear what bounds this approach might give
in low genus as there are no explicit calculations of Cheeger constants for closed
surfaces yet [AM99, Ben15, BLT21]. The second approach is to use the Jacquet–
Langlands correspondence [JL70], which allows one to derive lower bounds on the
first eigenvalue of certain compact arithmetic surfaces from lower bounds on the
first discrete eigenvalue of corresponding congruence covers of the modular curve
(see [Ber16, Example 8.27] and [Hej85] for concrete examples). We are not aware
of any examples where both of the following hold: a better lower bound than 1/4 is
known for the cusped surface (see [Hux85, BSV06] for examples) and the Jacquet–
Langlands correspondence gives rise to a closed surface of genus at most 20 without
cone points.
Table 4.Some congruence subgroups of the modular group, their signa-
tures, and the genus of their plumbing.
Γ (g,n) gplumbed
Γ1(13) (2,12) 8
Γ1(15) (1,16) 9
Γ0(107) (9,2) 10
Γ0(87) (9,4) 11
Γ0(86) (10,4) 12
Γ1(17) (5,16) 13
Γ0(78) (11,8) 15
Γ1(19) (7,18) 16
Γ0(134) (16,4) 18
Γ0(102) (15,8) 19
Γ0(227) (19,2) 20
