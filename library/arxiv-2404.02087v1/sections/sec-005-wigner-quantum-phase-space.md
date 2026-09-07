---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons Aakash A. Sahai 1 1Department of Electrical Engineering, University of Colorado Denver, Denver, CO 80204 ∗ Nanosciences largely rely on plasmons which are quasipar"
section_id: sec-005-wigner-quantum-phase-space
section_title: "Wigner quantum phase-space"
section_number: null
pages: 2-3
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
doc_brief: "Extreme plasmons Aakash A. Sahai 1 1Department of Electrical Engineering, University of Colorado Denver, Denver, CO 80204 ∗ Nanosciences largely rely on plasmons which are quasiparticles constituted b"
---
The dynamics of any many-body quantum system with
N quantum entities such as the quantum electron gas in
this work, is fully describable by suitably transforming
(Wigner-Weyl) the quantum variables representing the
ensemble over the real-space R3N. Instead of exact de-
termination of many-body wavefunction, the density ma-
trix, ρ(r, r′,t ) which allows determination of the statis-
tical distribution of states, is used to obtain the Wigner
function, fW (in Complex space, C):
fW (r, p,t ) =
Z
R3N→C
d3s e−is p
ℏ ρ

r + s
2, r− s
2,t

.
ρ =
Z
C→R3N
Z
a,b
fW (r, p)
(2πℏ)3N

ei[a(Q−r)+b(P−p)]

dx dp da db.
(2)
This representation overcomes the limitations imposed
by Heisenberg’s uncertainty principle. It allows treat-
ment of quantum mechanics in phase-space by simultane-
ous representation of the distribution of non-commuting
variables, here instantaneous position ( ˆQ) and momen-
tum ( ˆP ). Although, fW is a quasi probability distribu-
tion function, it allows modeling the evolution of a quan-
tum system using phase-space formalism. Density,n(r,t )
3
and momentum, n(p,t ) distributions are obtained from
the Wigner function, as follows:
Z
d3p fW (r, p,t ) =n(r,t ).
Z
d3r fW (r, p,t ) =n(p,t ).
(3)
The evolution of Wigner distribution function is de-
scribed by the Wigner equation [20].
∂fW
∂t + ℏkℓ
2m∗
∂fW
∂r =
Z
dk′
ℓ ϕW (r, k′
ℓ− kℓ,t )fW (r, k′
ℓ,t )
(4)
The Wigner transport equation, Eq.4 describes ballistic
carrier transport. Further correction terms are needed to
account for collisional dynamics. Here, kℓ (ˆp =−iℏ∇)
is the wavevector which determines the lattice or crystal
momentum of individual electrons with effective mass,
m∗
e. Naturally, when conduction electrons that sustain
the extreme plasmon individually attain large kℓ the col-
lective wavevector, k also becomes large.
The electromagnetic force due to long-range Coulomb
interaction (due to non-equilibrium distribution in space)
in the Wigner equation is accounted for by an electro-
static potential, ϕW (using mean-field approximation)
which is determined by Poisson equation:
∇2ϕW (r,t ) = 4πe(n(r,t )−n0). (5)
For the quantum electron gas, the Wigner-Poisson sys-
tem provides a framework similar to the Vlasov-Poisson
system for classical gasses.
In our work, the quantum electron gas on a surface is
strongly excited such that the displacement amplitude of
constituent conduction electrons approaches the wave-
length, in Eq.1. The resulting large-amplitude trajec-
tories cannot be perturbatively treated and linearized.
Such trajectories underlying extreme plasmons are dis-
cernible from Fig.2 which shows the planar cross-section
of electron density (of the 3D simulation in Fig.1).
FIG. 2. Cross-section of the surface crunch-in plasmon in a
conductive tube from 3D particle-tracking simulation same as
in Fig.1 using [31, 32].
Consequently, large-amplitude quantum gas oscilla-
tions cannot be modeled using fluid theory (tracking
macroscopic quantities such as moments of phase-space)
which uses macroscopic material properties and classi-
cal hydrodynamic model [21]. Similarly, small-amplitude
quantum mechanical framework [1] based upon pertur-
bative expansion around smallness of α (see sec.II D), is
not applicable to extreme plasmons.
Our analytical model below, therefore, uses quantum
kinetic theory to model large-amplitude plasmons. Par-
ticularly, we build upon the small-amplitude plasmon
model [1] that matches experimental observations.
C. Modified independent electron approximation
In kinetic modeling of quantum systems, under cer-
tain conditions it is sufficient to calculate the trajec-
tory of a single electron. When the energy of electron-
electron interaction (already minimized by Pauli’s exclu-
sion principle) becomes small relative to kinetic energy
and electron-lattice potential terms, particularly, in the
large-amplitude limit, the many-body electron model can
be decomposed into individual electron dynamics with
corrections for correlations.
The independent electron approximation allows for
the large-amplitude surface crunch-in plasmon model
based upon evolution of Wigner distribution function,
fW (r, p,t ) in Eq.4 to be fully accounted for by the dy-
namics of individual electrons. As this approximation is
applicable over collisionless timescale, our model is appli-
cable to the dynamics before collisions begin to dominate.
Accordingly, the quantum kinetic model especially at
the extreme limits is here approximated by a modified
single-particle kinetic equation utilizing the quantum fac-
tor, FQ(k, p) introduced in sec.II D.
Formal evaluation of the efficacy of assumptions by
comparing experiments against treatment using quantum
kinetic model and a modified single-particle approach
adopted here, is part of our future work.
