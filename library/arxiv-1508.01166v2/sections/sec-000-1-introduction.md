---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
When solving a partial di ﬀerential equation numerically, various measures
(e.g. convergence, stability and consistency) are usually investigated to verify
the implemented discretization. Such measures, although reﬂecting the mathe-
matical ﬁdelity of the discretization, may not give insight into the physical ﬁdelity
of the discretization. By physical ﬁdelity we mean how well does the discrete sys-
tem of equations conserve secondary quantities, such as kinetic energy, implied
in the continuous equation but not explicitly constructed or built into the numeri-
cal scheme. The development of such physically conservative discretizations, for
Navier-Stokes (NS) equations for example, is favorable for many physical appli-
cations (e.g. turbulent ﬂows and shallow-water simulations) to avoid undesirable
numerical artifacts. Among other discretization approaches, some staggered mesh
schemes are known for their conservation of both primary (i.e. mass and momen-
tum) and secondary (e.g. kinetic energy and vorticity) physical quantities [1].
Staggered mesh methods were ﬁrst developed by Harlow and Welch [2] for
structured Cartesian meshes by placing the velocity and pressure degrees of free-
dom at diﬀerent positions on the mesh. Later on, the approach was extended to
unstructured meshes by Nicolaides [3] and Hall et al. [4], which is now known as
the covolume (or dual-variable) method. The covolume method was originally in-
troduced as a low order method that does not experience spurious modes that were
common in low order discretizations of viscous ﬂows. The derivation of such dis-
cretization commences by taking the dot product of the momentum equation with
the unit normal vector to each face of the triangular /tetrahedral elements. This
reduces the velocity vector ﬁeld to a scalar ﬂux (equal to the mass ﬂux across the
face for an incompressible ﬂow with constant density) deﬁned on each face. In
this approach, the pressure is consequently deﬁned at the circumcenter of each tri-
angular/tetrahedral element. The accuracy of the covolume scheme was estimated
by Nicolaides [5] to be second order for a mesh with all its triangular elements
having the same circumradii (i.e. structured-triangular mesh) and ﬁrst order ac-
curate otherwise. These accuracy estimates were in agreement with numerical
experiments [4]. Several forms of the covolume method were then developed for
both two-dimensional (2D) (only on planar domains) and three-dimensional (3D)
domains, where the di ﬀerence was mainly in the convective term discretization
[6, 7, 8, 9].
The conservation properties of the covolume method were later revealed by
Perot [10]. The divergence form of Navier-Stokes equations was proved to con-
serve the momentum and kinetic energy both locally and globally. On the other
2
hand, the rotational form of Navier-Stokes equations was found to conserve the
circulation and kinetic energy locally and globally for both 2D [10] and 3D [11]
discretizations. These conservation properties of the covolume method, in addi-
tion to the attractive properties of its diﬀerential operators that mimic the behavior
of their continuous counterparts, shed light on the merit of using discrete calculus
methods to solve other physics problems [12].
Another approach to develop conservative discretizations for incompressible
ﬂows emerged from the computer graphics community, aiming to mitigate the ef-
fects of numerical viscosity that causes detrimental visual consequences [13, 14].
In this approach, the Navier-stokes equations were discretized through the dis-
crete exterior calculus (DEC) framework; the discretization of the smooth exterior
calculus operators [15, 16]. A main advantage of DEC discretizations is the ap-
plicability to simulate ﬂows over curved surfaces, unlike the covolume approach.
The resulting discrete equations had similarities with the covolume method, with
the diﬀerences mainly in the convective term discretization. In practice, the con-
vective term was not discretized using DEC but employed a method of charac-
teristics with an interpolation scheme based on Kelvin’s circulation theorem [13],
or a ﬁnite volume based approach [14]. However, the presented numerical test
cases using the DEC approach lacked comprehensive quantitative analysis of the
scheme’s accuracy and its conservative behavior.
This paper presents a discretization of the Navier-Stokes equations through
discrete exterior calculus. Hence, similar to previous DEC-based discretizations,
the developed discretization is capable of simulating ﬂows over curved surfaces,
which distinguishes it from the covolume method. In addition, the convective
term in the presented discretization is diﬀerent from previous DEC-based and co-
volume discretizations. The Navier-Stokes equations are ﬁrst rephrased using the
exterior calculus notation in Section 2. The DEC discretization of NS equations
is then derived in Section 3 for both 2D and 3D cases, highlighting its distinction
from the covolume method and previous DEC-based discretizations. In Section
4, several numerical experiments are illustrated for incompressible ﬂows over 2D
ﬂat/curved domains to benchmark the convergence and conservative behavior of
the developed scheme. The paper closes with conclusions summarizing the main
features of the presented discretization, and addressing potential future develop-
ments.
3
