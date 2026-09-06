---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
2 Hyperbolic structures on ﬁnite triangulations 4
3 Cocycles 6
4 Extending cocycles on genus 0 surfaces 9
5 Extending cocycles on triangulations 12
6 Examples of (non-)gimbal lock 14
7 Algorithm 15
arXiv:1904.12095v2  [math.GT]  6 Jan 2021
2
8 Results 20
9 Discussion 21
10 Appendix: The uncited theorem HIKMOT relies on 25
1 Introduction
Up to isometry, a ﬁnite hyperbolic 3-simplex is determined by its 6 edge parameters, by
which we mean either the edge lengths li j or the respective entries of its vertex Gram
matrix vi j = − cosh(li j ). Thus, an assignment of a parameter to each edge of a ﬁnite
triangulation T of a closed 3-manifold determines a hyperbolic structure for each 3-
simplex of T . If certain conditions are fulﬁlled, the hyperbolic structures on the indi-
vidual simplices are compatible and form a hyperbolic structure on the manifold (see
[Hea05] and Section 2).
Existing software (such as Casson’ s Geo [Cas] and Heard’ s Orb [Hea]) ﬁnds a numerical
approximation for the edge parameters using Newton’ s method and reports whether the
necessary equations are fulﬁlled within an error smaller than a certain ε. This suggests
but does not prove hyperbolicity. The aim of this paper is to describe how to take such
a numerical approximation and rigorously prove hyperbolicity by giving real intervals
that are veriﬁed to contain a solution to all the necessary equations and inequalities.
An algorithm either returning such intervals or (conservatively) reporting failure is de-
scribed in Section 7. The algorithm is a hyperbolicity veriﬁcation procedure but not a
hyperbolicity decision procedure since its failure just means that the given candidate
approximation was not close enough to a hyperbolic structure or needs to be perturbed
to avoid “gimbal lock” (explained below). An implementation of this algorithm is avail-
able at [Goe19b]. Therefore, this paper is achieving for ﬁnite triangulations what Hoff-
man, Ichihara, Kashiwagi, Masai, Oishi, and Takayasu [HIK+16] did for ideal triangula-
tions (HIKMOT’ s functionality has been integrated into SnapPy [CDGW] by the author
since version 2.3).
This is motivated by applications that beneﬁt from using geometric ﬁnite triangulations
in place of geometric spun triangulation. In particular, such applications no longer
need to overcome the incompleteness locus. An example is the generation of cohomol-
ogy fractals for a closed hyperbolic 3-manifold. As shown in [BGSS20, Figure 8.7], the
incompleteness locus produces artifacts in the raytraced image of a cohomology frac-
tal which simply disappear when using ﬁnite triangulations instead. Another example
is the algorithm proposed in [HHGT17] to rigorously compute the length spectrum for
a hyperbolic 3-manifold. This algorithm requires tiling H3 with translates of a funda-
mental domain to cover a ball of speciﬁed radius and thus would not work if there is
incompleteness locus.
An even more basic motivation is proving hyperbolicity of a closed 3-manifold by ﬁnd-
ing a triangulation admitting a geometric structure. Restricting ourselves to just spun
3
triangulations introduces a bottleneck. For example, the obvious spun triangulation of
a closed census manifold such as m135(1,3) can fail to be geometric. Thus ﬁnding a
geometric spun triangulation requires drilling and ﬁlling (or, in other words, ﬁnding a
different closed geodesic γ such that there is a geometric triangulation spun about γ).
Even worse, some hyperbolic 3-manifolds such asm007(3,1) seem to lack any geomet-
ric spun triangulation unless we pass to a cover 1. Note that a geometric spun trian-
gulation is known for every orientable closed manifold in the SnapPy census (except
for m007(3,1) where a 3-fold cover is needed), see [HIK +16]. However, the process of
ﬁnding such (covers admitting) geometric spun triangulations can be tedious and is not
known to be possible in general. Furthermore, passing to a cover can complicate appli-
cations such as computing the length spectrum.
Potential future work might generalize the techniques of this paper to Heard’ s work
[Hea05] on 3-orbifolds and Frigerio and Petronio’ s work [FP04] on 3-manifolds with
geodesic boundary. To ﬁnd hyperbolic structures on these, Heard’ s program Orb [Hea]
uses triangulations with ﬁnite as well as ideal and “hyperinﬁnite” vertices. Note that
some of the theory in this paper also carries over to spherical and Euclidean geometry
and might generalize to yield methods for verifying spherical or Euclidean structures on
ﬁnite triangulations.
Like [HIK+16], we use interval arithmetic methods such as the interval Newton method
or the Krawczyk test. These methods can only show the existence of a solution to a
system of equations if the Jacobian matrix is invertible near that solution. If the Jacobian
fails to be invertible, these methods can only show the existence of a solution to a subset
of the equations. This applies to the edge equations whether we are solving for shapes
in the cusped case or for edge lengths in the closed case. Hence, in both cases, we need
an additional result showing that there is a redundancy among the edge equations such
that solving a suitable subset of them is sufﬁcient. For ideal triangulations, this result
is due to Neumann-Zagier [NZ85, Neu92] and Moser [Mos09] (see Appendix). For ﬁnite
triangulations, we derive such a result in this paper.
Note that while we actually have exactly as many variables as equations in the case of
ﬁnite triangulations (namely, one per edge), the Jacobian of this system of equations
has a kernel at a solution corresponding to a hyperbolic structure. This is because we
can move each individual ﬁnite vertex of a triangulation in the hyperbolic manifold and
obtain a whole family of solutions (see Theorem 9.4). Thus, we need to use a two-step
strategy to verify a hyperbolic structure: First, we drop some edge equations and ﬁx an
equal number of edge parameters such that we can apply interval arithmetic methods
to ﬁnd intervals veriﬁed to contain a solution to the subsystem of equations we kept.
Next, we show that this solution is also a solution to the equations we dropped earlier
and thus that the intervals for the edge parameters contain a point giving a hyperbolic
structure. Interval arithmetic can verify that the error of the dropped equations is small
and we will show that if the dropped equations are fulﬁlled approximately, then they are
fulﬁlled exactly provided that a certain condition we call “gimbal lock” is avoided.
1In not yet published work, Maria Trnkova has proven that there is no geometric spun triangulation of
m007(3,1) with a small number of tetrahedra.
4
To deﬁne gimbal lock, we will look at the complex of doubly-truncated simplices asso-
ciated to the triangulation and an assignment of PGL 2(C)-matrices to the edges of the
complex computed from the edge parameters (see Section 3). The cocycle condition
says that the matrices on the edges of a polygon must multiply to the identity. Since a
subset of the edge equations is known to be fulﬁlled, the cocycle condition is known to
hold for some polygons but not necessarily for others. The goal is to show that it holds
for all polygons so that we get a PGL 2(C)-representation of the fundamental group (see
Section 4 and 5 and examples in Section 6). Roughly speaking, the idea is that if the
product of three small rotations about three axes in generic position is the identity, then
each rotation must be the identity. Inspired by the mechanical device called gimbal
(see Figure 8), we say that we avoid “gimbal lock”: if a gimbal is not in its locked posi-
tion, then we can apply any small rotation to the inner-most ring, or equivalently, if we
ﬁx the inner-most ring, none of the other rings can be turned.
We describe the resulting algorithm to obtain real intervals in Section 7. The algorithm
is effective and able to verify a hyperbolic structure on all 36093 closed orientable man-
ifolds in the Hodgson-Weeks census [HW94] and in the census bundle by Bell [Bel15],
see Section 8. Branched double covers of knots or links (or more precisely: double cov-
ers of S3 branched over a knot or link) provide a good class of test cases since ﬁnding a
geometric spun-triangulation of some of them can be challenging. Using ﬁnite triangu-
lations instead, we are able to prove the following new result:
Theorem 1.1. Out of the 313230 knots with up to 15 crossings (not including the un-
knot), exactly 193839 have a hyperbolic branched double cover.
Out of the 120573 links with up to 14 crossings (with at least two components), exactly
37709 have a hyperbolic branched double cover.
Section 9 concludes with a conjecture that implies that a hyperbolic structure on a ﬁnite
triangulation can always be perturbed so that the algorithm can verify it.
The appendix in Section 10 points out a gap in the argument (but not the algorithm) of
the HIKMOT paper.
Acknowledgements
The author wishes to thank Marc Culler, Nathan Dunﬁeld, Damian Heard, Neil Hoff-
man, and Christian Zickert for helpful discussions. Special thanks goes to Nathan Dun-
ﬁeld for ﬁnding some mistakes and providing some of the examples and some Python
scripts for Regina.
2 Hyperbolic structures on ﬁnite triangulations
Consider the isometry class of a positively oriented, ﬁnite geodesic simplex ∆ with ver-
tices labeled 0,. .. ,3 in H3. We brieﬂy review the relationship of the edge lengths and
5
the angles of ∆ following [Hea05] with one difference though: we use a slightly simpler
deﬁnition for the vertex Gram matrix G where all diagonal entries are −1 since we are
not interested in generalized simplices here. To be consistent with the vertex labels, we
0-index the rows and columns of a matrix (so m00 denotes the top left-most entry).
0
1
3
2
η0,12
θ13
l01
0
1
3
2
β132
α123
γ123
Figure 1. Angles of simplex. Figure 2. A doubly trun-
cated simplex ∆, also
known as permutahedron.
Figure 3. A prism.
Let li j denote the length of the edge between vertex i and j . The vertex Gram matrix G
associated to the simplex is the symmetric 4 × 4-matrix with entries
vi j = −cosh(li j ).
The edge lengths as well as the vertex Gram matrix uniquely determine the isometry
class of the simplex. Let ci j denote the respective cofactor of G which is given by
ci j = (−1)i +j det(Gi j ),
where Gi j is obtained by deleting the i -th row and j -th column. The dihedral angle
between face i and j and the angle at vertex i of the triangle i j k (derived from the law
of cosines) are then given by (also see Figure 1):
θi j = arccos
( ci j
pci ic j j
)
and ηi ,j k = arccos


vi j vi k + v j k
√
v 2
i j − 1
√
v 2
i k − 1

. (2.1)
Deﬁnition 2.1. Let G be a real symmetric 4 × 4-matrix with −1 on the diagonal. We
say that G is realized if G is the vertex Gram matrix of some ﬁnite, non-ﬂat simplex.
The following theorem is a special case of [Hea05, Theorem 1.5] (also compare to [Rat94,
Theorem 7.2.2]):
6
Lemma 2.2. G is realized if and only if
(a) G has one negative and three positive eigenvalues (which is equivalent to the
characteristic polynomial pG(x) = det(xI −G) = x4 +4x3 +a2x2 +a1x +a0 having
coefﬁcients a2 < 0, a1 > 0, a0 < 0 by the Budan-Fourier theorem [BPcR06]),
(b) ci i < 0 for all i , and
(c) c2
i j < ci ic j j for all i and j ,
where ci j denotes the respective cofactor of G.
Let T be an oriented, ﬁnite 3-dimensional triangulation (i.e., all vertex links are 2-
spheres) and let E(T ) denote the set of edges of T . Assume we have an assignment
of a length le > 0, or equivalently, a parameter νe < −1 to each e ∈ E(T ) where the two
are related by the formula νe = −cosh(le). This induces a symmetric 4 × 4-matrix G∆ for
each simplex ∆ of T where vi i = −1 and vi j = νe if i ⁄= j and the edge of ∆ from vertex i
to j is incident to e. Let Θe denote the sum of all dihedral anglesθi j incident to the edge
e of T . We can now use [Hea05, Lemma 2.4] to check whether this assignment yields a
hyperbolic structure on T :
Theorem 2.3. An assignment of a parameter νe < −1 to each edge e of an oriented,
ﬁnite triangulation T induces a hyperbolic structure on T if
(a) each matrix G∆ is realized (i.e., fulﬁlls the conditions of Lemma 2.2) and
(b) Θe = 2π for every e ∈ E(T ).
