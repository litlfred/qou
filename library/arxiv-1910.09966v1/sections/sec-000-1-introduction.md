---
doc_id: arxiv-1910.09966v1
doc_title: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1910.09966v1.pdf
source_sha256: 21798500c98ed25a
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
---
2 Preliminaries: Branched Coverings of 3- and 4-Manifolds 4
2.1 As Warmup: Branched Coverings of 2-Manifolds . . . . . . . . . 5
2.2 Branched Coverings of 3-Manifolds . . . . . . . . . . . . . . . . . 5
2.3 Branched Covering of 4-Manifolds . . . . . . . . . . . . . . . . . 6
2.4 Branched Coverings of Knot Complements . . . . . . . . . . . . . 7
3 Reconstructing a Spacetime: The K3 Surface and Particle Physics 8
1
arXiv:1910.09966v1  [physics.gen-ph]  16 Oct 2019
4 F rom K3 Surfaces to Octonions, 3-Braids and Particles 13
4.1 K3 Surfaces and Octonions . . . . . . . . . . . . . . . . . . . . . 13
4.2 From Immersed Surfaces in K3 Surfaces to Fermions and Knot
Complements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.3 Fermions as Knot Complements . . . . . . . . . . . . . . . . . . . 16
4.4 Torus Bundle as Gauge Fields . . . . . . . . . . . . . . . . . . . . 18
4.5 Fermions, Bosons and 3-Braids . . . . . . . . . . . . . . . . . . . 22
5 Electric Charge and Quasimodularity 23
5.1 Electric Charge as Dehn Twist of the Boundary . . . . . . . . . . 23
5.2 Electric Charge as a Frame of the Knot Complement . . . . . . . 24
5.3 The Charge Spectrum . . . . . . . . . . . . . . . . . . . . . . . . 26
5.4 Vanishing of the Magnetic Charge and Quasimodularity . . . . . 26
6 Drinfeld–T uraev Quantization and Quantum States 27
7 F ermions and Number Theory 29
8 The K3 Surface and the Number of Generations 29
9 Conclusions and Outlook 31
1 Introduction
General relativity (GR) deepens our view on space-time. In parallel, the appear-
ance of quantum ﬁeld theory (QFT) gives us a diﬀerent view of particles, ﬁelds
and the measurement process. One approach for the uniﬁcation of QFT and GR,
to a quantum gravity, starts with a proposal to quantize GR and its underlying
structure, space-time. Here, there is a unique opinion in the community about
the relation between geometry and quantum theory: the geometry as used in
GR is classical and should emerge from a quantum gravity in the usual limit that
Planck’s constant tends to zero. Most theories went a step further and try to get
the spacetime directly from quantum theory. As a consequence, the used model
of a smooth manifold cannot be used to describe quantum gravity. However,
currently, there is no real sign for a discrete spacetime structure or higher di-
mensions in current experiments [1]. Therefore, in this work, we conjecture that
the model of spacetime as a smooth 4-manifold can be also used in the quantum
gravitational regime. As a consequence, one has to ﬁnd geometrical/topological
representations for quantities in QFT (submanifolds for particles or ﬁelds, etc.)
as well in order to quantize GR. In this paper, we will tackle this problem to get
a geometrical/topological description of the standard model of elementary par-
ticle physics. Recently, there were eﬀorts by Furey [2, 3, 4, 5], Gresnigt [6, 7, 8]
and Stoica [9] to use octonions and Cliﬀord algebras to get a coherent model
to describe the particle generations in the standard model. In the past, the
stability of matter was related to topology like in the approach of Lord Kelvin
[10] with knotted aether vortices. The proposal to derive matter from space was
2
considered by Cliﬀord as well by Einstein, Eddington, Schr¨ odinger and Wheeler
with only partial success (see [11, 12]). Giulini [13] discussed the status of ge-
ometrodynamics in establishing particle properties like spin from spacetime by
using special solutions of general relativity. The usage of knots and links to
model particles, like the electron, neutrinos, etc., was ﬁrstly observed by Jehle
[14]. The phenomenological description of particle properties by using the quan-
tum groupSUq(n) is given in the work of Gavrilik [15]. Here, the (deformation)
parameter q of SUq(n) was linked with the ﬂavor mixing angle (Cabibbo an-
gle). Furthermore, torus knots as given by 2-braids were associated with vector
mesons (vector quarkonia) of diﬀerent ﬂavors. Later, Finkelstein [16] used the
representation of knots by quantum groups for his particle model. Similar ideas
are discussed in the model of Bilson–Thompson [17] in its loop theoretic exten-
sion [18]. Even for the Bilson–Thompson model, Gresnigt found a link between
Furey’s approach and this model. However, some properties of the Bilson–
Thompson model remained mysterious, like the deﬁnition of the charge. Open
is also the meaning of the braiding. If there is a connection between spacetime
and matter, then one has to construct the known fermions and bosons directly.
Here, it seems that the main problem is the determination of the underlying
spacetime. In this paper, we will follow this way with an heuristic argument
for the spacetime to be the K3 surface in Section 3. Then, we will analyze this
spacetime by using branched covers to ﬁnd two suitable substructures, a knot
complement representing the fermions and a link complement to represent the
bosons. Here, we proﬁt from ideas by Duston [19, 20, 21] as well from the work
of Denicola, Marcolli and al-Yasry [22]. As a byproduct, we also found interest-
ing relations to octonions. The representation of the knot and link complements
by branched covers gives the link to the original Bilson–Thompson model [17]
but also to Gresnigt’s work [6]. In Section 5, we will discuss the electric charge
and construct the corresponding operator by using the underlying U(1) gauge
theory by using the Hirzebruch defect. Finally, we will obtain the correct charge
spectrum: fermions carry the charges 0 ,± 1
3,± 2
3,±1 in units of the unit charge
e. Here, the factor 1
3 is related to 4-dimensional topology (Hirzebruch signa-
ture theorem). In Section 6, we will discuss the independence of the particular
braid from the particle. The braid is connected with the state of the particle as
shown by using the Drinfeld–Turaev quantization. Finally, we ﬁnish the paper
with some speculations about the number of generations, given by the number
of S2×S2 parts in the spacetime (K3 surface), and a global symmetry, the
group PGL (3, 4) of 3× 3 matrices of the 4-element ﬁeld F4, induced from the
K3 surface by using umbral moonshine.
Before we start with the description of the model, we will discuss the key
arguments and scope of the model. The model is based on a smooth spacetime
that is described by a smooth 4-manifold. First, it is argued that this spacetime
is the K3 surface where the evolution of the cosmos is submanifold. By using
this model, the calculation of cosmic parameters (cosmological constant, inﬂa-
tion parameters, etc.) matches with the experimental results. For the following,
we use the characterization of 4-manifold (i.e., the spacetime) by surfaces that
are connected to complements of links and knots (3-manifolds with boundary).
3
Interestingly, both 3-manifolds have a meaning by our previous work: knot
complements are fermions and link complements are bosons. Here, we ﬁnd a
representation of both 3-manifolds by braids of three strands (3-braids), which
is the connection to the work of Bilson–Thompson and Gresnigt. In case of
the K3 surface as spacetime, the surfaces mentioned above are arranged with
a strong connection to octonions, which is the link to Furey’s work. To con-
nect fermions, one needs a special class of link complements, so-called torus
bundles, which can be interpreted as gauge ﬁelds. Interestingly, there are only
three classes of torus bundles and we were able to connect them with the gauge
groups U(1),SU (2),SU (3). The main result of the paper is deﬁnition and in-
terpretation of the electric charge. The electric charge is a topological invariant
(Hirzebruch defect). For the fermions (knot complements), we obtained the
spectrum{0,±1,±2,±3} which agrees with the observation (normalized in e/3
units). The discussion about the quantization of the model and the number of
generations closes the paper.
The model uses a classical spacetime. Quantum properties are not included
in an obvious way. We obtained the correct charge spectrum, but we do not
know the direct connection between knot complement and fermion (electron,
neutrino, quark). There are ideas to use a quantization by a change of the
smoothness structure, known as Smooth Quantum Gravity [23]. In principle,
the number of generations is connected with the spacetime. We got the minimal
value of three generations, but it is only a lower bound. The model produces
only the particles of the standard model. No supersymmetry or other extensions
of the standard model can be derived by this model. Currently, we also have
no idea to calculate the coupling constants and masses. It seems that these
parameters are connected with the topological property of the spacetime.
2 Preliminaries: Branched Coverings of 3- and
4-Manifolds
According to Alexander (see [24] for instance), every manifold Mn can be rep-
resented as p-fold branched covering π :Mn→Sn along an n− 2 dimensional
subcomplex Nn−2⊂Sn, the branching set. In detail, the map π is a covering
except for the branching set, i.e., for every point b∈Sn\Nn−2 the map π−1(b)
consists of p points and the neighborhood U(b) is homeomorphic to one com-
ponent π−1U(b). Then, Mn\π−1(Nn−2)→ Sn\Nn−2 is a p−fold covering.
Usually,Nn−2 has the structure of a simplicial subcomplex. The p−fold cover-
ing is completely determined by the representation π1(Sn\Nn−2)→Sp in the
permutation group Sp of p symbols. Before going into the details, we will look
at some examples. First, there are no branched coverings for 1-manifolds except
for a trivial one. The ﬁrst interesting example is given by a compact 2-manifold,
i.e., by a surface of genus g. Here, the branching set consists of a ﬁnite num-
ber of points (0-dimensional branching set). The branching set of 3-manifolds
is a one-dimensional, complex and we will later see that knots and links are
4
Figure 1: 2-fold covering of torus, α is the equator and the four-point branching
set.
the appropriated structures. In case of 4-manifolds, one has a two-dimensional
complex as a branching set that was shown to be a surface. These facts are easy
to understand, but one parameter of a branched covering is open: how many
folds are minimally needed to represent every manifold in a ﬁxed dimension, or,
how large is p minimally for a manifold of dimension n?
