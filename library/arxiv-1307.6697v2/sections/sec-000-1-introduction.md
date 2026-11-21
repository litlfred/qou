---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
Introduction
1
2.
Three geometric structures on three manifolds
4
3.
Flag tetrahedra
5
4.
Ideal triangulations by ﬂag tetrahedra
8
5.
Holonomy of a decoration
9
6.
Computational steps
12
7.
An example: the ﬁgure-eight knot
16
8.
Description of the unipotent solutions for the ﬁrst hyperbolic manifolds
20
References
27
1. Introduction
In this paper we are interested in obtaining representations of the fundamental group of a
3-manifold into PGL(3, C). They will be deﬁned via certain topological triangulations with
additional geometric data carried by the 0-skeleton of the triangulation.
The most important example being hyperbolic geometry we will mainly consider 3-
manifolds which carry a complete hyperbolic structure. That is, complete riemannian man-
ifolds with constant negative curvature equal to −1.
In order to simplify the description we ﬁrst treat open manifolds which are the interior
of manifolds with boundary. If the hyperbolic manifold is complete and of ﬁnite volume one
shows that its ideal boundary is a union of tori. In that case we consider ideal triangulations
such that the 0-skeleton is in the ideal boundary. That is, identifying each boundary to a
This work was supported in part by the ANR through the project "Structures Géométriques et
Triangulations".
1
2
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
point, we consider a triangulation of the quotient space such that the 0-skeleton coincides
with the set of boundary points.
In hyperbolic space the ideal tetrahedra are described by a conﬁguration of four points in
the boundary of hyperbolic space, that is, CP1. The cross-ratio is suﬃcient to parameterize
ideal tetrahedra up to the isometry group.
Ideal triangulations were used by Thurston
to obtain examples of hyperbolic manifolds (see [22]). A complete hyperbolic structure is
obtained on the manifold once a system of equations on the cross-ratio coordinates of those
ideal tetrahedra are solved. A very successful computational tool, SnapPea, was developed
by JeﬀWeeks (see its very readable description in [23]) which solves numerically the system
of equations.
Other geometric structures in 3-manifolds are associated to subgroups of PGL(3, C),
namely, ﬂag structures which are associated to PGL(3, R) and spherical Cauchy-Riemann
structures (CR structures) which are associated to the group PU(2, 1). These geometric
structures are not well understood, in particular one does not know which 3-manifolds can
carry one of them.
The ﬁrst step in trying to ﬁnd a structure is to obtain a representation of the funda-
mental group in one of these groups (see [10] for the case PU(2, 1)). We will use the raw
data of triangulation of 3-manifolds as obtained in SnapPea. Then we proceed as in [2];
to a triangulation we associate a decoration given by a choice of ﬂags at each vertex of
the tetrahedra. We set equations imposing that the gluing of the tetrahedra is compatible
with the decoration of ﬂags. The solution of the equations would give immediately a repre-
sentation of the fundamental group of the 3-manifold into PGL(3, C) (called the holonomy
representation). Imposing that the holonomy restricted to the boundary tori be unipotent
is a natural condition which is analogous to the condition of completeness in the hyperbolic
case. But more general conditions are very important too. In particular, a condition, which
is appropriate to the CR case is that the eigenvalues be of absolute value one. Indeed, par-
abolic boundary conditions in the CR case imply that condition and it would be interesting
to determine if there exist CR structures corresponding to boundary holonomies given by
parabolic conditions. Our methods to solve these equations are the same and we give in
section 7.5 solutions to some non-unipotent systems. More general boundary conditions
could be treated by our methods.
A generalization of the gluing equations for higher dimensions was described in [14], and
a simpliﬁed set of equations describing the particular case of representations into SL(n, C)
is also described in [15]. These equations are based on decorations of tetrahedra by aﬃne
ﬂags (see also the a-coordinates for aﬃne ﬂags in [2]) but, as there were initially designed
for ﬁnding representations into SL(n, C), they miss solutions related to PGL(n, C) repre-
sentations obtained via projective ﬂags.
However, the introduction of a cocycle and its
computation gives access to all boundary unipotent representation in PGL(n, C). This in-
teresting method has the advantage to introduce quadratic equations as systems to be solved
but is not adapted to non unipotent decorations and thus to describe other representations.
On the other hand, it is not clear whether the computations are actually simpler in the
aﬃne ﬂag case as shown by limitations in the computations in [16] (even for PGL(3, C)).
Indeed, the use of Gröbner bases discards immediately the initial structure of the equations
(symetries, sparsity, etc.) and the small degrees of the initial equations does not prevent the
appearance of very large degrees during the computations. Even if some classes of examples
3
are known to have a good behaviour (see [18] for 0-dimensional systems), up to our knowl-
edge, there does not exist any criteria on the initial equations that might help to decide if
such algorithm will be well behaved or not.
In this paper we deal with methods to solve the equations and obtain a list of solutions for
manifolds with low complexity. In particular we obtain all solutions for ideal triangulations
of complete cusped hyperbolic manifolds with less than four tetrahedra.
In the ﬁrst sections, in order to make the paper self-contained, we review results in [2] (see
also [10] for the PU(2, 1) case). That contains the parametrization of decorated tetrahedra
(conﬁgurations of four ﬂags in CP2), the description of decorated ideal triangulations, the
compatibility equations which will lead us to a system of equations and the computation of
the holonomy representation. The special case we deal mostly in this paper has unipotent
boundary holonomy.
In section 6 we describe the methods used to solve the system of equations.
In the remaining sections we describe several important examples which illustrate the
methods and the results. The complete census up to three tetrahedra is shown in Table 1
(more details can be obtained in our webpage .../SGT).
A very important observation which came out from the examples is that solutions of
the gluing equations with unipotent boundary holonomy might not be 0-dimensional even
in low complexity. Computations for representations in PGL(2, C) show that, for cusped
hyperbolic manifolds obtained with four tetrahedra, only two have a one parameter family
component (there are no examples with less than four tetrahedra), but we do not have an
eﬃcient method to decide when the solution will have a positive dimensional component. We
veriﬁed that the one dimensional components (in all examples) have at most a ﬁnite number
of PSL(2, C) solutions. Moreover, they are all in PSL(2, R) so the volumes presented in the
table concern indeed all PSL(2, C) representations arising from the given triangulation. On
the other hand, PU(2, 1) solutions might appear in families (of real dimension one or two)
inside 1-dimensional components (see the worked example m003 in [3] where there is a
whole complex 1-dimensional component consisting of CR solutions). In any case, all these
families arise from degenerate representations. Indeed, either they give rise to reducible
representations or they have trivial boundary holonomy.
In the case of the ﬁgure eight knot the non-hyperbolic representations in PGL(3, C)
were obtained in [10].
They happen to be discrete representations in PU(2, 1) and two
of them give rise to spherical structures on the complement of the ﬁgure eight knot (see
[8, 11]). In the case of the Whitehead link complement, R. Schwartz ([21]) was able to
analyse one representation (obtained in a completely independent way as a subgroup of
PU(2, 1) generated by reﬂections) and showed that the complement of the link has a spherical
CR structure. Other representations of the fundamental group of the complement of the
Whitehead link obtained similarly using reﬂection groups were analysed in [19]. In their case
the representations form a one parameter family parameterized by the boundary holonomy.
We obtain here independently the unipotent representation which is the holonomy of a CR
structure on the complement of the Whitehead link.
It turns out that for the examples of CR structures obtained until now, the boundary
holonomy of the PU(2, 1) representations are abelian of rank one. This fact made us try
to chase representations into PU(2, 1) with rank one boundary holonomy in the hope that
they will correspond to CR structures. We enumerate all these solutions. For the ideal
4
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
triangulation of the Whitehead link complement with four tetrahedra there is only one
unipotent representation with rank one boundary holonomy (it is the same one obtained
independently in [19]).
Above all, the computations encourage us to study CR structures.
There is a great
proportion of PU(2, 1) representations obtained among all PGL(3, C) representations and
some of them might correspond to holonomies of geometric structures. On the other hand
it is a challenging problem to decide if a 3-manifold has a geometric structure. It is not
clear when the representations obtained here are discrete (for general discrete subgroups of
PGL(3, C) see [6]) . On the other hand, a criterium for rigidity of representations is given
in [3] and a discussion of generic discreteness of the boundary holonomy is given in [17]. In
this paper we don’t address these questions.
Another interesting observation from Table 1 is the fact that the hyperbolic volume is
the maximum among the volumes of all unipotent PGL(3, C) representations. This was
shown recently using methods of bounded cohomology in [5]. On the other hand, PU(2, 1)
representations have null volume by cohomological reasons (see [12]).
A ﬁnal remark is the fact that no numerical method is available to solve these equations.
It is a remarkable fact that, due to Mostow’s rigidity, one knows that there is at most one
complete hyperbolic structure on a manifold.
This structure corresponds to the unique
solution with positive imaginary parts of the variables associated to a triangulation. The
numerical scheme introduced in SnapPea should converge to this solution. Then, the LLL-
algorithm makes the method very eﬃcient in ﬁnding exact solutions corresponding to the
hyperbolic structures. On the other hand, there is no knowledge of the number or location of
solutions to the equations for representations in PGL(3, C). Therefore, there is no numerical
scheme to obtain solutions and we are, for the moment, condemned to solve the equations
exactly.
We thank M. Thistlethwaite for introducing us to SnapPea and making available his list
of cusped 3-manifolds with particularly simple generators for the boundary fundamental
group. We used his list for our computations. We also thank N. Bergeron, M. Deraux, A.
Guilloux, M. Thistlethwaite and S. Tillmann for all the stimulating discussions.
