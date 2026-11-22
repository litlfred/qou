---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-009-10-appendix-the-uncited-theorem-hikmot-relies-on
section_title: "Appendix: The uncited theorem HIKMOT relies on"
section_number: 10
pages: 25-28
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
As pointed out in the introduction, the full system of equations for ﬁnding a hyperbolic
structure on a triangulation fails to have rank equal to the number of variables in both
the ﬁnite and ideal case. Thus, veriﬁcation by interval methods in the ideal case also
relies on a theorem showing that if a suitable subsystem is fulﬁlled, all equations are
fulﬁlled. Unfortunately, the paper [HIK+16] did not cite this crucial theorem correctly.
We want to point out that the algorithm in [HIK+16] is correct and its implementation
can be trusted since the theorem it relies on has been proven by [Mos09, Lemma 2.4].
However the theorem from [NZ85] cited in [HIK+16] is insufﬁcient since it assumes hy-
perbolicity to begin with and its conclusion is too weak. Being the counterpart of the
result in this paper in the ideal case, we will brieﬂy state the correct theorem missing
from [HIK+16].
Recall, that given an ideal triangulation with o vertices, Thurston [Thu80, Chapter 4]
gave compatibility equations in one complex variable z1,...,zm per tetrahedron which
are all of the form
m
X
j=1
ar,j log
³
z j
´
+br,j log
³
1
1−z j
´
+cr,j log
³
1−1
z j
´
−2πıdr = 0
such that a solution with Im(z j) > 0 (called a geometric solution) yields a complete hy-
perbolic structure on the manifold obtained by ﬁlling in some cusps. There is one such
equation with dr = 1 for each of the m edges, one with dr = 1 for each ﬁlled cusped and
one (sometimes two are given, but it is easy to see that one is sufﬁcient) with dr = 0
for each unﬁlled cusp. Note that this system of equations consists of m + o equations
in m variables and thus is overdetermined. To ﬁnd a non-overdetermined system, let
αr,j = ar,j −cr,j and βr,j = −br,j + cr,j and consider the m × m-matrices A = (αr,j) and
B = (βr,j) where r ranges over the edge equations:
Theorem 10.1. The matrix (A|B) has rank m−o. Pick m−o linearly independent rows
of (A|B) and consider the system of equations consisting of the corresponding m −o
edge equations and the o cusp equations.
(a) Any solution to this system fulﬁlls the remaining o edge equations as well.
(b) Near a geometric solution, the Jacobian of this system of equations is invertible.
26
Note that (a) is sufﬁcient for an algorithm to prove a manifold to be hyperbolic. State-
ment (b) ensures that such an algorithm succeeds if given a solution close enough to
the geometric one.
[NZ85] states the rank of (A|B) but assumes hyperbolicity. Neumann revisted the re-
sult in [Neu92] to give a purely combinatorial statement where the rank of (A|B) oc-
curs as rank of the map β in a certain chain complex. However, even Theorem 4.1 in
[Neu92] only implies that the remaining o edge equations in the above theorem are ful-
ﬁlled modulo 2πıQ since it does not involve the dr of the edge equations. For a proof of
the above Theorem, see [Mos09, Section 2.3.1].
References
[Bel15]
Mark C. Bell, Surface bundle censuses, available at https://github.com/
MarkCBell/bundles/ (09/09/2020, commit ec4d8cc), 2015.
[BGSS20]
David Bachmann, Matthias Goerner, Saul Schleimer, and Henry Segerman,
Cohomology fractals and Cannon–Thurston maps, in preparation.
[BPcR06]
Saugata Basu, Richard Pollack, and Marie-Françoise Roy, Algorithms in Real
Algebraic Geometry, 2nd ed., Berlin: Springer, 2006 (English).
[Bur18]
Benjamin A. Burton, Regina: Normal surface and 3-manifold topology soft-
ware, available at https://regina-normal.github.io/ (08/01/2018, ver-
sion 5.1), 2018.
[Cas]
Andrew Casson, Geo, a program for geometrizing 3-manifolds, http://
computop.org/.
[CDGW]
Marc Culler, Nathan M. Dunﬁeld, Matthias Goerner, and Jeffrey R. Weeks,
SnapPy, a computer program for studying the geometry and topology of 3-
manifolds, available at http://snappy.computop.org/ (06/30/2018, ver-
sion 2.6).
[FP04]
Roberto Frigerio and Carlo Petronio, Construction and recognition of hyper-
bolic 3-manifolds with geodesic boundary, Trans. Am. Math. Soc. 356 (2004),
no. 8, 3243–3282 (English), arXiv:math/0109012.
[GGZ15]
Stavros Garoufalidis, Matthias Goerner, and Christian Zickert, Gluing equa-
tions for PGL(n,C)-representations of 3-manifolds, Algebr. Geom. Topol. 15
(2015), no. 1, 565–622 (English), arXiv:1207.6711.
[Goe17]
Matthias Goerner,
Geodesic triangulations exist for cusped Platonic
manifolds,
New York Journal of Mathematics 23 (2017), 1363–1367,
arXiv:1602.02208.
[Goe19a]
, Data for veriﬁed computations for closed hyperbolic 3-manifolds,
available at https://unhyperbolic.org/veriClosedData/, 2019.
27
[Goe19b]
,
Source code for veriﬁed computations for closed hyperbolic
3-manifolds, available at https://github.com/3-manifolds/SnapPy/
tree/master/dev/vericlosed/ until the feature is fully integrated into
SnapPy, 2019.
[Hea]
Damian Heard, Orb, a computer program that can ﬁnd hyperbolic struc-
tures on a large class of hyperbolic 3-orbifolds and 3-manifolds, available at
https://github.com/DamianHeard/orb/ (06/30/2018).
[Hea05]
,
Computation of hyperbolic structures on 3-dimensional orb-
ifolds, Ph.D. thesis, University of Melbourne, 2005, https://github.com/
DamianHeard/orb-thesis/.
[HHGT17] Robert C. Haraway III, Neil Hoffman, Matthias Goerner, and Maria Trnkova,
Length spectrum estimates for hyperbolic 3-manifolds, Computational Ge-
ometry Young Researchers Forum (Brisbane, Australia), 2017, http://www.
computational-geometry.org/YRF/cgyrf2017.pdf.
[HIK+16]
N. Hoffman, K. Ichihara, M. Kashiwagi, H. Masai, S. Oishi, and A. Takayasu,
Veriﬁed computations for hyperbolic 3-manifolds,
Experiment. Math.
25 (2016), no. 1, 66–78, arXiv:1310.3410, http://www.oishi.info.
waseda.ac.jp/~takayasu/hikmot/.
[HW94]
Craig D. Hodgson and Jeffrey R. Weeks, Symmetries, isometries and length
spectra of closed hyperbolic three-manifolds, Exp. Math. 3 (1994), no. 4, 261–
274.
[LST08]
Feng Luo, Saul Schleimer, and Stephan Tillmann, Geodesic ideal triangu-
lations exist virtually, Proc. Amer. Math. Soc. 136 (2008), no. 7, 2625–2630,
arXiv:math/0701431.
[Mos09]
Harriet Moser, Proving a manifold to be hyperbolic once it has been approx-
imated to be so, Algebr. Geom. Topol. 9 (2009), no. 1, 103–133 (English),
arXiv:0809.1203.
[MP16]
Gabriele Mondello and Dmitri Panov, Spherical metrics with conical singu-
larities on a 2-sphere: angle constraints, Int. Math. Res. Not. 2016 (2016),
no. 16, 4937–4995 (English), arXiv:1505.01994.
[Neu92]
Walter D. Neumann, Combinatorics of triangulations and the Chern-Simons
invariant for hyperbolic 3-manifolds, Topology ’90 (Columbus, OH, 1990),
Ohio State Univ. Math. Res. Inst. Publ., vol. 1, de Gruyter, Berlin, 1992,
pp. 243–271.
[NZ85]
Walter D. Neumann and Don Zagier, Volumes of hyperbolic three-manifolds,
Topology 24 (1985), no. 3, 307–332.
[PW00]
Carlo Petronio and Jeffrey R. Weeks, Partially ﬂat ideal triangulations of
cusped hyperbolic 3-manifolds, Osaka J. Math. 37 (2000), no. 2, 453–466.
28
[Rat94]
John G. Ratcliffe, Foundations of hyperbolic manifolds, Graduate Texts in
Mathematics, vol. 149, Springer-Verlag, New York, 1994.
[Thu80]
William P. Thurston, The geometry and topology of three-manifolds, 1980,
Princeton lecture notes, available at http://library.msri.org/books/
gt3m/.
Matthias Goerner
email: enischte@gmail.com
http://unhyperbolic.org/
