---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-002-references
section_title: "References"
section_number: null
pages: 2-4
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
Introduction
While many mathematicians are aware of the monopole equatio ns [ W] and of
the impact they have had in topology, probably not very many a re as familiar with
the works [ SW1, SW2 ] of Seiberg and Witten on which the monopole equations
are based. The appearance of these works was a major breakthr ough in Quantum
Field Theory (QFT), and has to a large extent revolutionized and transformed the
subject. The actual achievement in [ SW1] was an exact solution to a problem in
QFT (pure N =2 supersymmetric Yang-Mills in four dimensions with gauge gr oup
SU (2)) which could traditionally be solved only approximatel y, by computing the
ﬁrst few terms in a perturbative expansion. The solution is c lose to algebraic
geometry both in its details (involving families of ellipti c curves) and in its general
approach, which is to use global properties (monodromy, sym metries) of a physical
theory to uniquely characterize a geometric model of the the ory. This work opened
the doors to solutions, along similar lines, of many speciﬁc quantum theories, some
of which are reviewed here. It also led directly to the ongoin g revolution in string
theory involving string dualities and the appearance of hig her dimensional objects
(branes) on more or less equal footing with the strings thems elves.
The purpose of these notes is to try to make this exciting and r apidly evolving
chapter of high energy physics accessible to mathematician s, particularly to alge-
braic geometers. I have had to make some choices: I decided to focus on the original
work and its further development within QFT, thus omitting t he spectacular (but
well documented) applications to topology and strings. Eve n so, it was impossible
to render with mathematical rigor the enormous amount of bac kground material
needed from the physics. I opted instead, in §1, for the telling of one uniform but
very imprecise story of the physics. My hope is that it will aﬀ ord, to a mathemat-
ical reader with no prior knowledge of the physics, at least a general sense of the
physical theory, of how the diﬀerent parts interact, and of w hat some of the basic
concepts mean. The remaining, mathematical, sections of th ese notes discuss what
is now known (and what is still missing) about Seiberg-Witte n type solutions of
four-dimensional N = 2 supersymmetric Yang-Mills theories in algebro-geometr ic
terms, with the emphasis on an interpretation via integrabl e systems.
Section 1 starts with Maxwell’s classical description of el ectromagnetism. We
arrive at our central object of study, the duality in super Ya ng-Mills theory, after
discussing separately the three directions in which Maxwel l’s theory needs to be
extended: nonabelian gauge groups, quantization, and supe rsymmetry. We are
then ready for an overview of the Seiberg-Witten solution, [ SW1], emphasizing its
algebro-geometric elements. The section concludes with a d iscussion of the other
theories which could be exactly solvable by algebro-geomet ric techniques. These
theories occupy us in the remainder of these notes.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 3
Algebraically integrable systems are quickly reviewed in §2. The upshot is that
all the structures arising in the Seiberg-Witten physics of §1 are naturally realized
here, so algebraically integrable systems are the natural c ontext for describing the
physics (cf. [ DW], [ F]). We also clarify the role of the Seiberg-Witten diﬀerenti al,
which occurs naturally in any integrable system of spectral type. One important
feature of this diﬀerential, the linear dependence of its re sidues on the mass param-
eters, turns out to be part of a very general phenomenon. We st ate and outline
a proof of an apparently new result, which is a complex analog ue of the theorem
of Duistermaat-Heckman [ DH] on variation of the symplectic structure in a family
of symplectic quotients. The complex case is somewhat subtl er than the compact
version due to the presence of non-semisimple (e.g. nilpote nt) orbits.
Section 3 is mostly an attempt to rewrite the solution [ DW] of the SU( n)
theory with adjoint matter, with an emphasis on the math rath er than the physics.
We review the work of Markman [ Mn] and others on the integrable systems of
meromorphic Higgs bundles; among these systems we pick the p articular subsystem
we need. The system (i.e. its spectral curves) is described e xplicitly, then compared
to the elliptic soliton description [ T, TV]. A major part of [ DW] conisted of “tests”
showing that this system accurately reproduces physical pr operties of the theory;
we describe some of these “tests” here.
In the ﬁnal section we discuss the other major class of integr able systems which
is known to solve the pure N = 2 SYM theories: the periodic Toda lattices [ MW1].
In particular, we compare the various forms assumed by the sp ectral curves. We
then move to a common generalization of both systems, the ell iptic Calogero-Moser
systems, which were proposed in [ Mc] as a solution of the theory with adjoint
matter and arbitrary gauge group. This seems quite promisin g, but it still lacks
a satisfactory algebro-geometric description. We also men tion brieﬂy some other
theories where at least the family of spectral curves is know n, and conclude by
mentioning some recent ideas in string theory which exhibit the QFT integrable
systems discussed here as limits of stringy systems.
It is a pleasure to acknowledge pleasant and useful conversa tions, about some
of the topics covered here, with D. Freed, L. Jeﬀrey, A. Kiril lov, D. Lowe, N.
Nekrasov, R. Plesser, N. Seiberg, S. Singer, R. Sjammar, J. W eitsman, and E.
Witten, as well as helpful comments on the manuscript by D. Fr eed, A. Grassi, A.
Ksir, N. Nekrasov, M. Verbitsky and E. Witten.
§1. Some Physics Background
Electromagnetism
The electric ﬁeld E and the magnetic ﬁeld B in R3 are governed by Maxwell’s
equations, of T-shirt fame. Think of E andB, respectively, as a 1-form and a 2-form
on R3. Both are time-dependent, so we combine them into the electr omagnetic ﬁeld
F :=E∧dt +B, a 2-form on R4. Maxwell’s equations in vacuo are:
dF = 0 d ∗F = 0.
Here ∗ is the Hodge star operator on forms on R4, determined by the Minkowski
metric g = dx2 +dy2 +dz2 −c2dt2. (The speed of light c is usually set to 1 by
adjusting units.)
The same equations make sense for an unknown 2-form F on any (pseudo)
Riemannian manifold (X,g ). They are clearly invariant under the group of global
