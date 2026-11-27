---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-016-appendix-a-the-complementary-contribution-to-the
section_title: "Appendix A The complementary contribution to the dual 2-cells boundary operator"
section_number: null
pages: 32-35
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
operator
After deﬁning the velocity 1-forms on primal/dual mesh entities and substitut-
ing with the appropriate discrete operator, the discretized Navier-Stokes equation
was expressed, as in Eq. (15), as
[−dT
0 ]Un+1− Un
∆t −µ[−dT
0 ]∗1 d0∗−1
0
[
[−dT
0 ]U + dbV
]
+ [−dT
0 ]∗1 Wv∗−1
0
[
[−dT
0 ]U + dbV
]
= 0, (A.1)
For the dual 2-cells touching the domain boundary; e.g. the 2-cell whose
dual is the primal nodes 0, 1, 3, 4, .. in Fig. 1, the discrete operators [ −dT
0 ]
in the viscous and convective terms are complemented by the operator d b that
closes such dual 2-cells boundaries by the primal boundary edges. Such domain
boundary contribution vanishes, however, for other [−dT
0 ] operators, underlined in
the above equation. Regarding the time derivative term, since the entries of the
tangential velocity forms vector V are calculated at an intermediate time step, the
domain boundary contributions complementing [−dT
0 ]Un+1 and [−dT
0 ]Un will then
cancel each other.
In regards to the viscous term, starting from its smooth exterior calculus form;
i.e. µd∗ d∗ du♭, it can be expressed as µdα, with α =∗d∗ du♭. Considering
the domain boundary contribution, the discrete viscous term is then expressed
as µ
[
[−dT
0 ]A + dbA′
]
, with A to be the vector containing the discrete α 1-forms
deﬁned on the dual edges, and A′ as the vector containing the discrete 1-forms
α′. Similar to α, the smooth form α′ is deﬁned as α′ = ∗d∗ du♭, whereas its
discrete version is deﬁned however on the primal edges. It follows accordingly,
based on the diagram in Eq. (12), that the discretization of d u♭ included in the
α′ form is deﬁned on the primal triangles. Since the smooth velocity form u♭ is
retrieved through Whitney map interpolation as a constant form over each triangle,
the exterior derivative of such constant velocity form then vanishes; i.e.
∫
σ2
du♭ =
0. This implies that α′, and therefore the domain boundary contribution, vanishes
for the viscous term. Using a similar argument for the convective term d ∗ (u♭∧
∗du♭), it follows that the discretization of du♭, in the wedge product, is also deﬁned
on the primal triangles, and therefore is equal to zero. Accordingly, the domain
boundary contribution to the ﬁrst (underlined) [ −dT
0 ] operator in the convective
term also vanishes.
32
References
[1] J. B. Perot, Discrete conservation properties of unstructured mesh schemes,
Annu. Rev. Fluid Mech. 43 (2011) 299–318.
[2] F. H. Harlow, J. E. Welch, Numerical calculation of time-dependent viscous
incompressible ﬂow of ﬂuid with free surface, Phys. Fluids 8 (12) (1965)
2182–2189.
[3] R. Nicolaides, Flow discretization by complementary volume techniques,
in: 9th AIAA Computational Fluid Dynamics Conference, V ol. 1, 1989, pp.
464–470.
[4] C. Hall, J. Cavendish, W. Frey, The dual variable method for solving ﬂuid
ﬂow diﬀerence equations on Delaunay triangulations, Comput. Fluids 20 (2)
(1991) 145–164.
[5] R. A. Nicolaides, Direct discretization of planar div-curl problems, SIAM J.
Numer. Anal. 29 (1) (1992) 32–56.
[6] J. Cavendish, C. Hall, T. Porsching, Solution of incompressible Navier-
Stokes equations on unstructured grids using dual tessellations, Int. J. Nu-
mer. Meth. Fl. 2 (6) (1992) 483–502.
[7] J. Cavendish, C. Hall, T. Porsching, A complementary volume approach
for modelling three-dimensional Navier-Stokes equations using dual Delau-
nay/Voronoi tessellations, Int. J. Numer. Meth. Fl. 4 (4) (1994) 329–345.
[8] S. Choudhury, R. Nicolaides, Discretization of incompressible vorticity–
velocity equations on triangular meshes, Int. J. Numer. Meth. Fl. 11 (6)
(1990) 823–833.
[9] R. Nicolaides, The covolume approach to computing incompressible ﬂow,
in: M. Gunzburger, R. Nicolaides (Eds.), Incompressible Computational
Fluid Dynamics (1993).
[10] B. Perot, Conservation properties of unstructured staggered mesh schemes,
J. Comput. Phys. 159 (1) (2000) 58–89.
[11] X. Zhang, D. Schmidt, B. Perot, Accuracy and conservation properties of a
three-dimensional unstructured staggered mesh scheme for ﬂuid dynamics,
J. Comput. Phys. 175 (2) (2002) 764–791.
33
[12] J. B. Perot, V . Subramanian, Discrete calculus methods for diﬀusion, J. Com-
put. Phys. 224 (1) (2007) 59–81.
[13] S. Elcott, Y . Tong, E. Kanso, P. Schr ¨oder, M. Desbrun, Stable, circulation-
preserving, simplicial ﬂuids, ACM T. Graphic. (TOG) 26 (1) (2007) 4.
[14] P. Mullen, K. Crane, D. Pavlov, Y . Tong, M. Desbrun, Energy-preserving
integrators for ﬂuid animation, ACM T. Graphic. (TOG) 28 (3) (2009) 38.
[15] A. N. Hirani, Discrete exterior calculus, Ph.D. thesis, California Institute of
Technology (2003).
[16] M. Desbrun, A. N. Hirani, M. Leok, J. E. Marsden, Discrete exterior calcu-
lus, arXiv preprint math/0508341.
[17] A. N. Hirani, K. B. Nakshatrala, J. H. Chaudhry, Numerical method for
Darcy ﬂow derived using Discrete Exterior Calculus, Int. J. Comput. Meth.
Eng. Sci. Mech. 16 (3) (2015) 151–169. doi:10.1080/15502287.2014.
977500.
[18] J. B. Perot, C. J. Zusi, Di ﬀerential forms for scientists and engineers, J.
Comput. Phys. 257 (2014) 1373–1393.
[19] R. Abraham, J. E. Marsden, T. Ratiu, Manifolds, tensor analysis, and appli-
cations, 2nd Edition, V ol. 75 of Applied Mathematical Sciences, Springer-
Verlag, New York, 1988.
[20] A. N. Hirani, K. Kalyanaraman, E. B. VanderZee, Delaunay Hodge star,
Comput. Aided Design 45 (2) (2013) 540–544.
[21] H. Flanders, Di ﬀerential forms with applications to the physical sciences,
Courier Corporation, 2012.
[22] W. Chang, F. Giraldo, B. Perot, Analysis of an exact fractional step method,
J. Comput. Phys. 180 (1) (2002) 183–199.
[23] D. Arnold, R. Falk, R. Winther, Finite element exterior calculus: from Hodge
theory to numerical stability, B. Am. Math. Soc. 47 (2) (2010) 281–354.
[24] D. N. Arnold, R. S. Falk, R. Winther, Finite element exterior calculus, ho-
mological techniques, and applications, Acta Numer. 15 (2006) 1–155.
34
[25] U. Ghia, K. N. Ghia, C. Shin, High-Re solutions for incompressible ﬂow
using the Navier-Stokes equations and a multigrid method, J. Comput. Phys.
48 (3) (1982) 387–411.
[26] A. Green, G. Taylor, Mechanism of the production of small eddies from
larger ones, in: Proc. Royal Soc. A, V ol. 158, 1937, pp. 499–521.
[27] J. Connors, Convergence analysis and computational testing of the ﬁnite el-
ement discretization of the Navier–Stokes alpha model, Numer. Meth. Part.
D. E. 26 (6) (2010) 1328–1350.
[28] E. VanderZee, A. N. Hirani, D. Guoy, E. A. Ramos, Well-centered trian-
gulation, SIAM J. Sci. Comput. 31 (6) (2010) 4497–4523. doi:10.1137/
090748214.
[29] J. B. Bell, P. Colella, H. M. Glaz, A second-order projection method for
the incompressible Navier-Stokes equations, J. Comput. Phys. 85 (2) (1989)
257–283.
[30] A. McKenzie, HOLA: a high-order Lie advection of discrete di ﬀerential
forms, with applications in ﬂuid dynamics, Ph.D. thesis, California Institute
of Technology (2007).
[31] D. Pavlov, P. Mullen, Y . Tong, E. Kanso, J. E. Marsden, M. Desbrun,
Structure-preserving discretization of incompressible ﬂuids, Physica D:
Nonlinear Phenomena 240 (6) (2011) 443–458.
[32] L. M. Polvani, D. G. Dritschel, Wave and vortex dynamics on the surface of
a sphere, J. Fluid Mech. 255 (1993) 35–64.
[33] J. Vankerschaver, M. Leok, A novel formulation of point vortex dynamics
on the sphere: geometrical and numerical aspects, J. Nonlinear Sci. 24 (1)
(2014) 1–37.
35
