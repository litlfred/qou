---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-013-311-generalities
section_title: "Generalities"
section_number: 3.1.1
pages: 21-23
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
There is a beautiful SL(2, Z) action on the space of 3-dimensional conformal ﬁeld theories
with U(1) ﬂavor symmetry. This action was ﬁrst described in [ 25] as a way to understand
the meaning of diﬀerent choices of boundary conditions for an abelian gauge ﬁeld in AdS4 in
the context of AdS4/CFT 3.
To be precise, SL(2, Z) acts on the space of 3d theories equipped with a speciﬁc way to
couple a U(1) ﬂavor symmetry to a background U(1) gauge ﬁeld. The SL(2, Z) action can
be deﬁned by specifying the action of its generators S and T , which obey the relations
S4 = (ST )3 =id. (3.1)
The generatorT does not change the underlying 3d CFT. It only modiﬁes the prescription of
how to couple the theory to the background gauge ﬁeldA, by adding to the conserved current
for the background ﬂavor symmetry the Hodge dual ﬁeld strength ∗F =∗dA. In terms of a
Lagrangian, this is simply accomplished by adding a background Chern-Simons interaction
at level k = 1,
T : L→L + 1
4πA∧dA. (3.2)
In contrast, the S generator changes the structure of the 3d theory by making the back-
ground gauge ﬁeld A dynamical.10 The new 3d theory is then prescribed a coupling to a new
backgroundU(1) gauge ﬁeldAnew: the new ﬂavor current is the Hodge dual ﬁeld strength∗F
of the old, now dynamical, gauge ﬁeld. Equivalently, one prescribes a Lagrangian coupling
S : L→L + 1
2πAnew∧dA (A dynamical). (3.3)
It is the monopole operators for A that are charged under the new U(1) ﬂavor symmetry;
thus this U(1) is sometimes called “topological.” From the deﬁnitions of S and T , one can
prove that the relations S2 = C and (ST )3 = id. hold, where the transformation C (charge
conjugation) just inverts the sign of the background gauge ﬁeld. We will generally denote the
action of an SL(2, Z) group element g on a theoryT as g◦T .
There is a useful alternative interpretation of this SL(2, Z) action: it is the action of
electric-magnetic duality on the space of conformally invariant boundary conditions for a free
abelian four-dimensional gauge theory. Indeed, given a three-dimensional CFT with a pre-
scribed coupling to a background gauge ﬁeld, we can build a boundary condition by coupling
the CFT to the value of the 4d gauge ﬁeld at the boundary. This gives a generalization of
10One can add a Yang-Mills kinetic term at intermediate stages in the calculation. But for S to have the
correct properties, one must ﬂow to the IR at the end, and then gYM→∞ and this term is removed.
– 20 –
Neumann boundary conditions: the normal component of the 4d ﬁeld strength at the bound-
ary becomes proportional to the conserved current of the 3d CFT. If we denote the 3d theory
asT , we can denote the resulting boundary condition as B[T ].
Next, we can do an electric-magnetic duality transformation g∈ SL(2, Z) in the four-
dimensional bulk, and ask how the boundary condition B[T ] looks in the new duality frame.
This “new” boundary condition g◦B [T ] turns out to coincide with B[g◦T ]. This fact can
be shown readily with the help of “duality domain walls” [ 26]: the action of bulk dualities on
boundary conditions can be interpreted as the collision (or OPE) of these domain walls with
the boundary, as illustrated in Figure 17. For an abelian gauge theory the duality walls are
very easy to construct from the deﬁnition of electric-magnetic duality. The collision with the
boundary then reproduces the SL(2, Z) action deﬁned above.
gT g ◦ T=
Figure 17: The action of duality domain walls on boundary conditions. A duality transformation
g∈ Sp(2N, Z) maps a generalized Neumann boundary condition deﬁned by coupling to a 3d theory
T into a boundary condition associated with a boundary CFT g◦T .
TheSL(2, Z) action on boundary conditions is a little bit more general than theSL(2, Z)
action on 3d theories with a coupling to a background gauge ﬁeld. For example, there exists
an extra SL(2, Z) orbit of boundary conditions which includes the pure Dirichlet boundary
condition on the 4d gauge ﬁeld. This boundary condition is invariant under T , and it is sent
to the pure Neumann boundary condition by S.
Now, it is rather obvious how to generalize this SL(2, Z) action to an Sp(2N, Z) action
on boundary conditions for a general four-dimensional U(1)N abelian gauge theory, or to an
action on 3d CFTs with U(1)N ﬂavor symmetry: it is the action of the electric-magnetic
duality group of the U(1)N four-dimensional gauge theory. Notice that in this case, there
are several orbits of boundary conditions which involve at some point Dirichlet boundary
conditions for some of the bulk gauge ﬁelds. These orbits will look a bit singular from the
point of view of an action on 3d CFTs. Concretely, they signal situations where the ﬂavor
symmetry is spontaneously broken to a subgroup in the IR [ 26].
To make this a little more explicit, suppose we are given a Lagrangian description of a
3d CFT withU(1)N global symmetry, whose current is coupled toN background gauge ﬁelds
⃗A = (A1,...,A N). The generators of Sp(2N, Z) fall into three basic categories: “ T -type,”
“S-type,” and “GL-type” (cf. [27]). Representing them as matrices in N×N blocks, we ﬁnd
– 21 –
Lagrangian transformations
“T -type” g =
(
I 0
B I
)
, B symmetric : L[⃗A]→L [⃗Anew] + 1
4π
⃗Anew·Bd ⃗Anew ; (3.4)
“S-type” g =
(
I−J −J
J I −J
)
: L[⃗A]→L [⃗A] + 1
2π
⃗Anew·Jd ⃗A (3.5)
(where J = diag(j1,...,j N) with ji∈{ 0, 1}, and we have gauged every Ai for which ji = 1,
replacing its U(1) with a new topological ﬂavor symmetry); and
“GL-type” g =
(
U 0
