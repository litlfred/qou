---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
The goal of this paper is to prove new upper bounds on five invariants associated to a
closed, oriented, hyperbolic surfaceM:
(1) itssystolesys(M), the length of any shortest non-contractible closed curve inM;
(2) itskissing numberkiss(M), the number of homotopy classes of oriented non-
contractible closed curves of minimal length inM;
(3) thefirst positive eigenvalueλ 1(M) (which coincides with thespectral gap) of the
Laplace–Beltrami operator ∆M onM;
(4) themultiplicitym 1(M) of the eigenvalueλ 1(M), that is, the dimension of the
corresponding eigenspace;
(5) the numberN small(M), counting multiplicity, ofsmall eigenvaluesof ∆ M, that is,
those contained in the interval [0,1/4].
We bound the first four invariants in terms of the genus ofMonly, but the fifth one
in terms of the genus and the systole. In low genus (or for small systole), our bounds
are illustrated in Figures 1 and 2 (see also Tables 1 to 7). They beat all previous upper
bounds except for the systole and kissing number in genus 2, forλ 1 in genus 2, 3, 4,
and 6, and forN small when the systole is smaller than 2.317. Note thatN small(M)<
2 if and only ifλ 1(M)>1/4. We use this to show that there exist surfaces with a
spectral gap larger than 1/4 in genus 4 to 7, 14, and 17 (this was already known in
genus 2 and 3). Whether such surfaces exist in every genus is a well-known open problem
related to Selberg’s eigenvalue conjecture [Sel65] (see e.g. [Mon15, Question 1.1] and
[Wri20, Problem 10.4]). A lot of progress on this question in high genus was made recently
[MNP22, WX22, LW24, HM23, AM23, AM25, MPvH25, HMT25].
Date: February 10, 2026.
1
arXiv:2302.02540v3  [math.GT]  9 Feb 2026
2 MAXIME FORTIER BOURQUE AND BRAM PETRI
5 10 15 20
3
4
5
6
7
8
sys
genus g
previous bound
new bound
record holders
(a)Systole
5 10 15 20
0
50
100
150
200
250
kiss/(2g − 2)
genus g
previous bound
new bound
record holders (b)Kissing number
5 10 15 20
0
1
2
3
4
5
6
(λ1 − 1/4)log(g)2
genus g
previous bound
new bound
record holders
(c)First eigenvalue
5 10 15 20
0
5
10
15
20
25
30
35
40
m1
genus g
previous bound
new bound
Colin de Verdière's conjectured bound
Colbois and Colin de Verdière's examples
record holders (d)Multiplicity
Figure 1.Upper bounds and current record holders for the maximization
of geometric and spectral invariants associated to hyperbolic surfaces.
In higher genus (or for larger systole), our asymptotic bounds are as follows.
Theorem 6.4.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
sys(M)<2 log(g) + 2.409.
Theorem 7.8.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
kiss(M)< 30.608·g 2
log(g) + 1.2045.
Theorem 8.3.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
λ1(M)< 1
4 +
 π
log(g) + 0.7436
2
.
Theorem 9.5.There exists someg 0≥2such that every closed hyperbolic surfaceMof
genusg≥g 0 satisfies
m1(M)≤2g−1.
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 3
Theorem 10.2.IfMis a closed hyperbolic surface of genusg≥2, then
Nsmall(M)<min
24π2(g−1)
sys(M) 3 , 16(g−1)
sys(M) 2

.
These improve upon the previous best upper bounds established in [Bav96], [FBP22]
(previously [Par13]), [Che75], [S´ ev02], and [Hub76] respectively. While the previous bounds
used very different techniques from one invariant to another, our proofs are all based on
the same method, namely, linear programming applied to the Selberg trace formula. Note
that we have made no effort to estimate the required lower boundg 0 on genus in the above
theorems, though this could in principle be done by making certain calculations of limits
effective.
1 2 3 4 5 6 7 8
0.2
0.4
0.6
0.8
1
Nsmall/(2g − 2)
sys
previous bound
new bound
(a)Number of small eigenvalues.
5 10 15 20
3
4
5
6
7
8
sys
genus g
upper bound on systole
criterion for λ1 > 1/4
record holders for systole (b)Criterion forλ 1>1/4.
Figure 2.Upper bounds on the number of small eigenvalues and lower
bounds on the systole that imply a spectral gap larger than a quarter.
In addition to finding new examples of surfaces withλ 1 >1/4 as mentionned earlier, we
also improve the previous best lower bounds of Colbois and Colin de Verdi` ere [CCdV88]
on the maximum ofm 1 in genus 4, 7, 8, 10, 14 to 16, and 19. Note that Colin de Verdi` ere’s
conjectured upper bound [CdV86, CdV87] onm 1 appearing in Figure 1d has since been
disproved in genus 10 and 17 [FBGMPP23].
