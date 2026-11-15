---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-022-incompressible-surfaces-in-3-manifolds
section_title: "(In)compressible surfaces in 3-manifolds"
section_number: null
pages: 79-81
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
(In)compressible surfaces in 3-manifolds
Bulk incompressible surfaces.
Let S be a properly embedded orientable sur-
face in a 3-manifold M. If S has a boundary, we also assume that ∂S ⊂∂M. A
compressing disk D ⊂M for S is a disk with ∂D = D ∩S such that ∂D does not
bound a disk in S. The action of ‘pinching’ along the disk D is called a compression,
and it transforms S into a new simpler surface, e.g. compressing along a meridian
turns the torus into a (marked) 2-sphere. A properly embedded connected surface
S with Euler characteristic χ(S) ⩽0 is called compressible if it has a compressing
disk, and incompressible otherwise. In an incompressible surface, every disk D with
∂D = D ∩S bounds a ball in M, as depicted in the picture below:
−→
.
(A.1)
– 79 –
A basic characterization of incompressible surfaces is given by the following result: if
S is a π1-injective, orientable, connected and properly embedded surface with χ(S) ⩽
0, then S is incompressible. We also refer to such surfaces as bulk-incompressible, to
distinguish them from the ∂-incompressible surfaces that we discuss below.
A surface is called boundary-parallel if the embedding map ι : (D, ∂D) →
(M, ∂M) can be isotoped into ∂M. A surface S that is both bulk-incompressible
and non-boundary parallel is called essential.
There is a useful way to diagnose if a bulk-incompressible surface is boundary
parallel. Cutting M along a boundary-parallel incompressible surface cuts M into
two pieces. Moreover, one of the pieces is homotopic to S itself, while the other is
homotopic to the original manifold M. Thus if cutting M along a surface S yields a
connected manifold or a disconnected manifold where both pieces have fundamental
groups different from S itself, then S is not boundary parallel.
Boundary incompressible surfaces.
It is also useful to discuss the notion of a
boundary incompressible (or ∂-incompressible) surface. Roughly speaking, boundary
compressible surfaces are allowed to be compressed on the boundary, rather than in
the bulk. More precisely, a ∂-compressing disc for S is a disk whose boundary lies
on both S and ∂M such that ∂D does not bound another disk D′ with components
in S and ∂M, see the picture below:
−→
.
(A.2)
A surface S with no ∂-compressing disks is called ∂-incompressible. The two notions
of incompressibility are independent: a surface may be bulk incompressible but ∂-
compressible, or ∂-incompressible but bulk compressible.
Relation to hyperbolization theorem with geodesic boundaries.
Bulk in-
compressible cylinders (or equivalently, annuli) play an important role in Thurston’s
hyperbolization theorems quoted in section 4.4.
These annuli may be either ∂-
compressible or ∂-incompressible.
An example of a bulk incompressible annulus
inside the genus-2 handlebody is displayed in (4.45). This annulus is ∂-compressible.
Indeed, a known result about handlebodies is that they do not contain surfaces that
are both bulk-incompressible and ∂-incompressible, see e.g. [132]. For a discussion
and classification of incompressible annuli in the genus-g handlebody, see [133, 134].
We also mention here the notion of ∂-irreducibility of a manifold M, which
features in the variant of the hyperbolization theorem with geodesic boundaries.
This notion implies that all essential annuli are ∂-incompressible. More precisely,
Let M be irreducible and ∂M incompressible, i.e. ∂M is π1-injective.
Then an essential annulus S in M is also ∂-incompressible.
– 80 –
To show this, assume that S is ∂-compressible, i.e. that there exist a ∂-compressing
disk D.
Compressing along D turns the annulus S into a disk D′ ⊂M.
The
boundary of D′ is a circle in ∂M which is homotopically trivial in M. Since ∂M is
incompressible, it follows that ∂D′ bounds a disk in ∂M. The union of the boundary
disk and D′ defines a sphere inside M, but since M is prime (i.e. π2(M) is trivial),
this sphere must bound a ball. It follows that D′ is boundary parallel; however,
this means that the original annulus S is also boundary parallel. Thus, S cannot be
essential and we have reached a contradiction.
Let us now show how the presence of an essential cylinder is an obstruction to
the existence of a hyperbolic metric with a totally geodesic boundary. Let M be a
manifold with boundary ∂M, and suppose M contains an essential cylinder. We can
consider the doubled manifold M ∪M glued along the common boundary. Now sup-
pose that M admits a finite-volume hyperbolic metric with geodesic boundary, then
the doubled manifold M ∪M also admits a finite-volume hyperbolic metric. However,
an essential annulus in M uplifts to an essential torus in M ∪M (incompressibility
follows for one cycle from incompressibility of the annulus and for the other cycle
by non-boundary parallelness). Since M ∪M has an incompressible torus, it cannot
carry a finite-volume hyperbolic metric so we reached a contradiction. Hence M
cannot carry a finite-volume metric with a geodesic boundary.
There is a second obstruction to the existence of a finite-volume hyperbolic met-
ric. If the boundary ∂M is an incompressible surface, i.e. if the inclusion π1(∂M) →
π1(M) is injective, the manifold is said to be ∂-irreducible (or boundary-irreducible).
Manifolds that are not ∂-irreducible cannot carry a finite-volume hyperbolic metric
with geodesic boundary for the folloing argument. For such a manifold, there is a
curve γ on the boundary that is null-homotopic in the bulk, but not null-homotopic
on the boundary, i.e. bounds a disk D in the bulk. We can then run the same argu-
ment as above. In the doubled manifold M ∪M, D uplifts to a sphere in M ∪M,
i.e. the manifold is not irreducible and thus not hyperbolic.
Although the machine does not produce acylindrical manifolds, it does produce
manifolds which are ∂-irreducible, an example being the twisted I-bundles discussed
in section 5.2.
