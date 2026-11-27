---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
For many years, it was thought that Landau’s theory
of symmetry breaking [1] could describe essentially all
phases and phase transitions. It appeared that all con-
tinuous phase transitions were associated with a broken
symmetry. However, after the discovery of the fractional
quantum Hall (FQH) eﬀect, it was realized that FQH
states contain a new type of order - topological order
- that is beyond the scope of Landau theory (for a re-
view, see Ref. [2]). Since then the study of topological
phases in condensed matter systems has been an active
area of research. Topological phases have been investi-
gated in a variety of theoretical and experimental sys-
tems, ranging from FQH systems [3–6], quantum dimer
models [7–10] , quantum spin models [11–19], to quan-
tum computing [20, 21], or even superconducting states
[22, 23]. This work has revealed a host of interesting
theoretical phenomena and applications, including frac-
tionalization, anyonic quasiparticles, and fault toleran t
quantum computation. Yet, a general theory of topolog-
ical phases is lacking.
One way to reveal the gaps in our understanding is
to compare with Landau’s theory of symmetry break-
ing phases. Landau theory is based on (a) the physical
concepts of long range order, symmetry breaking, and or-
der parameters, and (b) the mathematical framework of
group theory. These tools allow us to solve three impor-
tant problems in the study of ordered phases. First, they
provide low energy eﬀective theories for general ordered
phases: Ginzburg-Landau ﬁeld theories [24]. Second,
they lead to a classiﬁcation of symmetry-breaking states.
For example, we know that there are only 230 diﬀerent
crystal phases in three dimensions. Finally, they allow us
to determine the universal properties of the quasiparticle
excitations (e.g. whether they are gapped or gapless). In
addition, Landau theory provides a physical picture for
the emergence of ordered phases - namely particle con-
∗URL: http://dao.mit.edu/~wen
densation.
Several components of Landau theory have been suc-
cessfully reproduced in the theory of topological phases.
For example, the low energy behavior of topological
phases is relatively well understood on a formal level:
topological phases are gapped and are described by topo-
logical quantum ﬁeld theories (TQFT’s).[25] The prob-
lem of physically characterizing topological phases has
also been addressed. Ref. [2] investigated the “topologi-
cal order” (analogous to long range order) that occurs
in topological phases. The author showed that topo-
logical order is characterized by robust ground state de-
generacy, nontrivial particle statistics, and gapless edg e
excitations.[3, 13, 26] These properties can be used to
partially classify topological phases. Finally, the quasi -
particle excitations of topological phases have been ana-
lyzed in particular cases. Unlike the symmetry breaking
case, the emergent particles in topologically ordered (or
more generally, quantum ordered) states include (decon-
ﬁned) gauge bosons[27, 28] as well as fermions (in three
dimensions) [29, 30] or anyons (in two dimensions) [31].
Fermions and anyons can emerge as collective excitations
of purely bosonic models.
Yet, the theory of topological phases is still incomplete.
The theory lacks two important components: a physical
picture (analogous to particle condensation) that clariﬁe s
how topological phases emerge from microscopic degrees
of freedom, and a mathematical framework (analogous
to group theory) for characterizing and classifying these
phases.
In this paper, we address these two issues for a large
class of topological phases which we call “doubled” topo-
logical phases. On a formal level, “doubled” topological
phases are phases that are described by a sum of two
TQFT’s with opposite chiralities. Physically, they are
characterized by parity and time reversal invariance. Ex-
amples include all discrete lattice gauge theories, and all
doubled Chern-Simons theories. It is unclear to what ex-
tent our results generalize to chiral topological phases -
such as in the FQH eﬀect.
We ﬁrst address the problem of the physical picture
for doubled topological phases. We argue that in these
String-net condensedNormal
t/U << 1 t/U >> 1
FIG. 1: A schematic phase diagram for the generic string-net
Hamiltonian (3). When t/U (the ratio of the kinetic energy
to the string tension) is small the system is in the normal
phase. The ground state is essentially the vacuum with a few
small string-nets. When t/U is large the string-nets condense
and large ﬂuctuating string-nets ﬁll all of space. We expect a
phase transition between the two states at some t/U of order
unity. We have omitted string labels and orientations for th e
sake of clarity.
phases, local energetic constraints cause the microscopic
degrees of freedom to organize into eﬀective extended
objects called “string-nets”. At low energies, the mi-
croscopic Hamiltonian eﬀectively describes the dynamics
of these extended objects. If the kinetic energy of the
string-nets dominates the string-net tension, the string-
nets “condense”: large string-nets with a typical size on
the same order as the system size ﬁll all of space (see
Fig. 1). The result is a doubled topological phase. Thus,
just as traditional ordered phases arise via particle con-
densation, topological phases originate from “string-net
condensation.”
This physical picture naturally leads to a solution
to the second problem - that of ﬁnding a mathemati-
cal framework for classifying and characterizing doubled
topological phases. We show that each topological phase
is associated with a mathematical object known as a
“tensor category.” [32] Here, we think of a tensor cat-
egory as a 6 index object F ijk
lmn which satisﬁes certain
algebraic equations (8). The mathematical object F ijk
lmn
characterizes diﬀerent topological phases and determines
the universal properties of the quasiparticle excitations
(e.g. statistics) just as the symmetry group does in Lan-
dau theory. We feel that the mathematical framework
of tensor categories, together with the physical picture
of string-net condensation provides a general theory of
(doubled) topological phases.
Our approach has the additional advantage of provid-
ing exactly soluble Hamiltonians and ground state wave
functions for each of these phases. Those exactly solu-
ble Hamiltonians describe local bosonic models (or spin
models). They realize all discrete gauge theories (in any
dimension) and all doubled Chern-Simons theories (in
(2 + 1) dimensions). One of the Hamiltonians - a spin-
1/2 model on the honeycomb lattice - is a simple theo-
retical realization of a fault tolerant quantum computer
[33]. The higher dimensional models also yield an in-
teresting result: we ﬁnd that (3 + 1) D string-net con-
densation naturally gives rise to both emerging gauge
bosons and emerging fermions. Thus, string-net conden-
sation provides a mechanism for unifying gauge bosons
and fermions in (3 + 1) and higher dimensions.
We feel that this constructive approach is one of the
most important features of this paper. Indeed, in the
mathematical community it is well known that topolog-
ical ﬁeld theory, tensor category theory and knot theory
are all intimately related [34–36]. Thus it is not sur-
prising that topological phases are closely connected to
tensor categories and string-nets. The contribution of
this paper is our demonstration that these elegant mathe-
matical relations have a concrete realization in condensed
matter systems.
The paper is organized as follows. In sections II and
III, we introduce the string-net picture, ﬁrst in the case
of deconﬁned gauge theories, and then in the general
case. We argue that all doubled topological phases are
described by string-net condensation.
The rest of the paper is devoted to developing a the-
ory of string-net condensation. In section IV, we con-
sider the case of (2 + 1) dimensions. In parts A and B,
we construct string-net wave functions and Hamiltonians
for each (2 + 1) D string-net condensed phase. Then, in
part C, we use this mathematical framework to calculate
the universal properties of the quasiparticle excitations
in each phase. In section V, we discuss the generaliza-
tion to 3 and higher dimensions. In the last section, we
present several examples of string-net condensed states -
including a spin-1/2 model theoretically capable of fault
tolerant quantum computation. The main mathematical
calculations can be found in the appendix.
