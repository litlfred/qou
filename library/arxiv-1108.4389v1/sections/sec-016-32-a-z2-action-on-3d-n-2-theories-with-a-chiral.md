---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-016-32-a-z2-action-on-3d-n-2-theories-with-a-chiral
section_title: "A Z2 action on 3d N = 2 theories with a chiral operator"
section_number: 3.2
pages: 24-25
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
The basic “matter” action on 3d N = 2 theories begins with a theory that has a coupling to
a background 3d chiral multiplet φ. In practice, what we mean is a choice of chiral operator
O that can be inserted in a superpotential
W =φO. (3.11)
Here and elsewhere, we will not keep track of the normalization of superpotential terms. In
particular, we will view a rescaling of O as a trivial operation.
We can deﬁne an operation F that makes φ dynamical (thus, setting O eﬀectively to
zero). The new theory can be coupled to a new background chiral ﬁeld φ′ by coupling to the
new chiral operatorO′ =φ, namely by the superpotential
W =φ′φ. (3.12)
It is easy to see that F 2 = 1. We can simply look at the combined superpotential
W =φ′′φ′ +φ′φ +φO (3.13)
and integrate out φ′.
Much like the “gauge” Sp(2N, Z) action of the previous subsection, the operation F can
be given an interesting four-dimensional interpretation. One can consider possible boundary
conditions on a four-dimensional hypermultiplet. If we split the four real scalar ﬁelds in the
hypermultiplet into two complex scalar ﬁelds, which we can denote asX andY , then the two
– 23 –
basic boundary conditions are either Neumann for X and Dirichlet for Y , or vice versa. A
way to understand this is that Y sits in a multiplet of the unbroken supersymmetry which
contains the normal derivative of X.
If we introduce extra degrees of freedom at the boundary, say a 3d theory with a preferred
chiral operatorO, then we can consider a deformed Dirichlet boundary conditionY =O. This
will be accompanied by a corresponding deformation of the Neumann boundary conditions
forX, involving the corresponding piece of the supermultipletO. This deﬁnes a certain class
of boundary conditions which we denote BY , so that the boundary condition associated to a
3d theory T is denoted by BY [T ]. An alternative way to describe this boundary condition
is to start with the undeformed boundary condition and add the boundary superpotential
coupling
W =XO. (3.14)
Naively, one can construct a completely diﬀerent class of boundary conditions BX as
Dirichlet boundary conditions with X =O′, whereO′ is a chiral operator in a 3d boundary
theoryT′. It turns out that these two classes actually coincide, as every member BY [T ] of
one class has a mirror BX[T′] in the other class. One simply takes T′ to be the image of T
under F , withO′ =φ; then we claim that
BY [T ] =BX[F◦T ]. (3.15)
To see this, we simply follow the deﬁnition of F◦T to obtain an overall superpotential
coupling
W =Yφ +φO. (3.16)
Integrating out φ setsY =−O. Furthermore, the boundary condition X =φ means that we
can simply “absorb” φ intoX, thus relaxing the Dirichlet boundary conditions. It takes a bit
more work to make sure that X acquires Neumann boundary conditions, but it follows from
the fact that the normal derivative ∂nX plays the role of auxiliary ﬁeld in the Y supermul-
tiplet. In summary, if we begin with Dirichlet boundary conditions for X and perform an F
transformation — adding a single boundary chiral multiplet φ and a superpotentialW =Yφ
— we will ﬂow in the IR to Dirichlet boundary conditions for Y .
