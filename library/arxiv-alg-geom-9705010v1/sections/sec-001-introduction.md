---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "arXiv:alg-geom/9705010v1 7 May 1997"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
---
§1. Some physics background
Electromagnetism
Yang-Mills theory
Quantization
Supersymmetry
N = 2 super Yang-Mills
Duality
The Seiberg-Witten solution
Adding Matter
§2. Why integrable systems?
Algebraically integrable systems
Seiberg-Witten diﬀerentials
Linearity: complexiﬁed Duistermaat-Heckman
§3. Which integrable system?
Meromorphic Higgs bundles
The spectral curves
Elliptic solitons
Tests
Consistency with Seiberg-Witten
Mass to zero: the N=4 limit
τ to ∞: the ﬂow to pure N=2
Higgs to ∞: symmetry breaking
Singularities
§4. Other integrable systems
Pure N = 2 SYM
The Toda system
1991 Mathematics Subject Classiﬁcation. Primary: 81T13, 81T60, 58F07.
Secondary: 14D20, 14H40.
Work partially supported by NSF grant DMS95-03249, and by grants from the
Univesity of Pennsylvania Research Foundation and The Harmon Duncombe Foundation.
c
⃝1997 American Mathematical Society
1
2
RON Y. DONAGI
Periodic Toda
The spectral curves
Fundamental matter
Adjoint matter
Stringy integrable systems
References
Introduction
While many mathematicians are aware of the monopole equations [W] and of
the impact they have had in topology, probably not very many are as familiar with
the works [SW1, SW2] of Seiberg and Witten on which the monopole equations
are based. The appearance of these works was a major breakthrough in Quantum
Field Theory (QFT), and has to a large extent revolutionized and transformed the
subject. The actual achievement in [SW1] was an exact solution to a problem in
QFT (pure N=2 supersymmetric Yang-Mills in four dimensions with gauge group
SU(2)) which could traditionally be solved only approximately, by computing the
ﬁrst few terms in a perturbative expansion.
The solution is close to algebraic
geometry both in its details (involving families of elliptic curves) and in its general
approach, which is to use global properties (monodromy, symmetries) of a physical
theory to uniquely characterize a geometric model of the theory. This work opened
the doors to solutions, along similar lines, of many speciﬁc quantum theories, some
of which are reviewed here. It also led directly to the ongoing revolution in string
theory involving string dualities and the appearance of higher dimensional objects
(branes) on more or less equal footing with the strings themselves.
The purpose of these notes is to try to make this exciting and rapidly evolving
chapter of high energy physics accessible to mathematicians, particularly to alge-
braic geometers. I have had to make some choices: I decided to focus on the original
work and its further development within QFT, thus omitting the spectacular (but
well documented) applications to topology and strings. Even so, it was impossible
to render with mathematical rigor the enormous amount of background material
needed from the physics. I opted instead, in §1, for the telling of one uniform but
very imprecise story of the physics. My hope is that it will aﬀord, to a mathemat-
ical reader with no prior knowledge of the physics, at least a general sense of the
physical theory, of how the diﬀerent parts interact, and of what some of the basic
concepts mean. The remaining, mathematical, sections of these notes discuss what
is now known (and what is still missing) about Seiberg-Witten type solutions of
four-dimensional N = 2 supersymmetric Yang-Mills theories in algebro-geometric
terms, with the emphasis on an interpretation via integrable systems.
Section 1 starts with Maxwell’s classical description of electromagnetism. We
arrive at our central object of study, the duality in super Yang-Mills theory, after
discussing separately the three directions in which Maxwell’s theory needs to be
extended: nonabelian gauge groups, quantization, and supersymmetry.
We are
then ready for an overview of the Seiberg-Witten solution, [SW1], emphasizing its
algebro-geometric elements. The section concludes with a discussion of the other
theories which could be exactly solvable by algebro-geometric techniques. These
theories occupy us in the remainder of these notes.
SEIBERG-WITTEN INTEGRABLE SYSTEMS
3
Algebraically integrable systems are quickly reviewed in §2. The upshot is that
all the structures arising in the Seiberg-Witten physics of §1 are naturally realized
here, so algebraically integrable systems are the natural context for describing the
physics (cf. [DW], [F]). We also clarify the role of the Seiberg-Witten diﬀerential,
which occurs naturally in any integrable system of spectral type. One important
feature of this diﬀerential, the linear dependence of its residues on the mass param-
eters, turns out to be part of a very general phenomenon. We state and outline
a proof of an apparently new result, which is a complex analogue of the theorem
of Duistermaat-Heckman [DH] on variation of the symplectic structure in a family
of symplectic quotients. The complex case is somewhat subtler than the compact
version due to the presence of non-semisimple (e.g. nilpotent) orbits.
Section 3 is mostly an attempt to rewrite the solution [DW] of the SU(n)
theory with adjoint matter, with an emphasis on the math rather than the physics.
We review the work of Markman [Mn] and others on the integrable systems of
meromorphic Higgs bundles; among these systems we pick the particular subsystem
we need. The system (i.e. its spectral curves) is described explicitly, then compared
to the elliptic soliton description [T, TV]. A major part of [DW] conisted of “tests”
showing that this system accurately reproduces physical properties of the theory;
we describe some of these “tests” here.
In the ﬁnal section we discuss the other major class of integrable systems which
is known to solve the pure N = 2 SYM theories: the periodic Toda lattices [MW1].
In particular, we compare the various forms assumed by the spectral curves. We
then move to a common generalization of both systems, the elliptic Calogero-Moser
systems, which were proposed in [Mc] as a solution of the theory with adjoint
matter and arbitrary gauge group. This seems quite promising, but it still lacks
a satisfactory algebro-geometric description. We also mention brieﬂy some other
theories where at least the family of spectral curves is known, and conclude by
mentioning some recent ideas in string theory which exhibit the QFT integrable
systems discussed here as limits of stringy systems.
It is a pleasure to acknowledge pleasant and useful conversations, about some
of the topics covered here, with D. Freed, L. Jeﬀrey, A. Kirillov, D. Lowe, N.
Nekrasov, R. Plesser, N. Seiberg, S. Singer, R. Sjammar, J. Weitsman, and E.
Witten, as well as helpful comments on the manuscript by D. Freed, A. Grassi, A.
Ksir, N. Nekrasov, M. Verbitsky and E. Witten.
§1. Some Physics Background
Electromagnetism
The electric ﬁeld E and the magnetic ﬁeld B in R3 are governed by Maxwell’s
equations, of T-shirt fame. Think of E and B, respectively, as a 1-form and a 2-form
on R3. Both are time-dependent, so we combine them into the electromagnetic ﬁeld
F := E∧dt + B, a 2-form on R4. Maxwell’s equations in vacuo are:
dF = 0
d ∗F = 0.
Here ∗is the Hodge star operator on forms on R4, determined by the Minkowski
metric g = dx2 + dy2 + dz2 −c2dt2. (The speed of light c is usually set to 1 by
adjusting units.)
The same equations make sense for an unknown 2-form F on any (pseudo)
Riemannian manifold (X, g). They are clearly invariant under the group of global
4
RON Y. DONAGI
isometries of (X, g).
When dim X = 4, the equations are also invariant under
the duality F 7→∗F.
When X = R4 with the Minkowski metric, this duality
interchanges the electric and magnetic ﬁelds. The group of isometries in this case
is the Poincare group, an extension of the Lorentz group SO(3, 1) of rotations by
the group (R4, +) of translations.
Geometrically, we ﬁx a U(1)-bundle L on X and consider a connection A on L
as a new variable. The ﬁrst equation dF = 0 is interpreted as saying that (locally)
F = dA is the curvature. The remaining equation then is d ∗dA = 0. The group of
isometries of the triple (X, g, L) acts on the connections and preserves the equation.
This is an extension of the group of those isometries of (X, g) which preserve L by
the gauge group of C∞maps from X to U(1). The duality is still there, but is now
hidden.
Now impose an external ﬁeld j. (In R4, j is a 3-form whose dx∧dy∧dz com-
ponent is the charge density, while the other 3 components give the current.) The
equations become
dF = 0,
d ∗F = j,
and duality is lost. Geometrically, once we think of F as curvature, the ﬁrst equation
becomes a tautology (the Bianchi identity), while the second is an extra condition
which may or may not hold. Physically, we explain this asymmetry as due to the
absence of magnetic charges (“monopoles”).
Dirac proposed that some magnetic charges can be introduced by changing the
topology, or allowing singularities. For example, a monopole at the origin of R3 is
represented by a U(1)-bundle on (R3
x,y,z ∖0) × Rt. Such bundles are characterized
topologically by their Chern class c1 ∈Z, and this c1 is interpreted as the magnetic
charge at the origin. Indeed, the “magnetic charge” at the origin is just the total
magnetic ﬂux across a small sphere S2 around the origin in R3; this is the integral
over S2 of B, which equals the integral of F, which is c1. We can extend F to R4 as
a distribution, but now dF is the δ-function c1.δx,y,z instead of dF = 0. This is not
yet suﬃcient to restore the symmetry to Maxwell’s equations: the electric charge
is arbitrary, but the magnetic charge is allowed only in discrete “quanta”. This
does raise the possibility, though, that complete symmetry could be restored in a
quantum theory, where, as in the real world, electric charge also comes in discrete
units. Indeed, Dirac discovered that in quantum mechanics, where an electrically
charged particle is represented by a wave function satisfying Schrodinger’s equation,
the electric charge e of one particle and the magnetic charge g of another (in
appropriate units) satisfy eg ∈Z . This has the curious interpretation that all
electric charges are automatically quantized as soon as one magnetic monopole
exists somewhere in the universe.
In [MO], Montonen and Olive conjectured that in certain supersymmetric
Yang-Mills quantum ﬁeld theories the electric-magnetic duality is indeed restored.
This involves an extension of the basic picture in three separate directions: replac-
ing the “abelian” Maxwell equations by the non-abelian Yang-Mills; quantizing the
classical theory; and adding supersymmetry to the Poincar´e invariance.
