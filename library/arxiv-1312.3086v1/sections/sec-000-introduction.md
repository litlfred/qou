---
doc_id: arxiv-1312.3086v1
doc_title: "Quantum repeater with Rydberg blocked atomic ensembles in fiber-coupled cavities"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 1312.3086v1.pdf
source_sha256: ff328e7c7cbdc70c
doc_brief: "Quantum repeater with Rydberg blocked atomic ensembles in fiber-coupled cavities — 7 sections: Introduction; The sequence; At the end of this sequence, the s"
---
A possible route towards scalable quantum computers
and quantum communication networks combines small
quantum processor nodes which communicate via the ex-
change of moving information carriers, the so-called ﬂy-
ing qubits, which will typically be photons. The direct
exchange of a photon, either through free space or a ﬁber,
between a pair of nodes does not have unit success prob-
ability, and to safely communicate quantum states, one
can instead apply entangled state in teleportation proto-
cols [1, 2], where the entanglement of two remote nodes
can be achieved, e.g. after multiple attempts until a suit-
able heralding detection event certiﬁes the establishment
of the state. For long distances, photon loss makes the
success probability small, and hence the average time
needed to establish a state for transmission of a single
bit of quantum informsation very long. This problem,
however, can be solved by the quantum repeater setup [3]
which divides the transmission path between the nodes
into smaller segments with auxiliary nodes over which
losses are strongly diminished. The auxiliary nodes are
ﬁrst entangled with their nearest neighbors in a heralded
way followed by a succession of local measurements which
cause the graduate projection on quantum states with en-
tanglement distributed over longer and longer distances
(entanglement swapping).
The implementation of this
approach is compatible with diﬀerent physical setups in-
volving atomic ensembles and linear optical operations.
The most inﬂuential proposal is the so-called DLCZ pro-
tocol [4], whose feasibility was experimentally considered
in its two-node version in [5].
This manuscript presents a quantum repeater scenario,
based on the Rydberg blockade phenomenon. Rydberg
blockade refers to the strong dipole-dipole interaction be-
tween pairs of highly excited atoms, which after laser ex-
citation of a single atom shifts the resonance condition
for all the other atoms and hence blocks further exci-
tation by the laser ﬁeld. Rydberg blockade forbids the
resonant excitation of more than one Rydberg atom in
an atomic mesoscopic sample [6], and has been experi-
mentally observed, e.g., in [7, 8]. In [9] it was proposed
to take advantage of Rydberg blockade in quantum infor-
mation processing, leading to an intensive current ﬁeld of
research [10]. Diﬀerent theoretical proposals have been
recently put forward, which allow to take advantage of
the full spectroscopic richness of Rydberg interactions
for quantum information purposes [11–13], and a novel
framework for quantum information encoding and com-
puting has been proposed [10, 14–16], in which register
qubit states are physically implemented by the (symmet-
ric) occupational states |ni = 0, 1⟩of internal atomic lev-
els {|i⟩, i = 1, . . . , K} in an ensemble of Na (> K) iden-
tical atoms.
The collective laser manipulation of the system com-
bined with the Rydberg blocking interaction allows one
to store and universally process information in the sub-
space of symmetric ensemble states containing at most
one atom in each internal level.
The primary advan-
tage of ensembles over single atoms consists in their en-
hanced coupling to external control ﬁelds, which allows
for eﬃcient and rapid processing. A secondary practi-
cal advantage is that even in a multi-qubit register, one
merely needs to address the atoms collectively, contrary
to individual-atom encoding of qubits which requires the
precise control of each and every single particle in the
system.
In the quantum repeater we propose here, the nodes
are N identical atomic ensembles, placed in cavities
which are linked via optical ﬁbers. The internal struc-
ture of the atoms is such that each ensemble k = 1, . . . , N
accomodates three logical subnodes, called the left (Lk),
the right (Rk), and the auxiliary subnode (Ak) in the
following.
In the ﬁrst step of our protocol, we entan-
gle the logical state of the subnode (Rk) in the cavity
k with the polarization state of a single photon released
in the cavity.
This photon is then transmitted to the
neighboring cavity where it is absorbed by the left subn-
2
ode (Lk+1) degree of freedom of the atomic ensemble in
that cavity, which thus becomes entangled with (Rk). A
conditional gate applied to subnodes (Lk+1) and (Ak+1),
followed by appropriate ionization detection is used to
ensure that no error occurred during the entanglement
generation, in particular that the photon was not lost
during the transfer through the ﬁber between the cav-
ities. If needed, subnodes (Rk, Lk+1) are reset so that
the entanglement generation operation can be repeated
until successful. Once all pairs (Rk, Lk+1) have been cor-
rectly entangled, entanglement is swapped by ensemble
operations on every pair (Lk, Rk). Measurements using
Rydberg blockade and ionization detection on all subn-
odes {Lk, Rk, k = 2, . . . , (N −1)} ﬁnally heralds the en-
tangled state of the remote pair (R1, LN) which can be
transformed into any required Bell state by application
of a unitary operation on (LN) prescribed by the results
of the measurements. If one of the measurements fails,
the procedure must be repeated.
We note that the use of Rydberg blocked ensembles as
quantum repeaters has been proposed in [17, 18]. Though
related our proposal, however, never makes use of pho-
ton detection to generate entanglement between neigh-
bouring nodes, we solely rely on ensemble laser manip-
ulations (including ionizing pulses), ion detection whose
eﬃciency can be made very close to one ηd ∼1, and pho-
ton transmissions through optical ﬁbers. This allows for
a shortened entanglement generation average time whose
expression is derived in the Appendix.
The paper is structured as follows.
In Sec.
II, we
present our quantum repeater scheme using Rydberg
blockaded ensembles in optical cavities coupled by optical
ﬁbers. In Sec. III, we analyze the diﬀerent steps of our
protocol with emphasis on their robustness against er-
rors, and we compute the average duration of our scheme.
In Sec. IV, we suggest a physical implementation. In Sec.
V, we compare our scheme with other schemes for quan-
tum repeaters, and we conclude in Sec. VI.
II.
THE MODEL
Our quantum repeater setup consists of N atomic en-
sembles placed in cavities which are linked by optical
ﬁbers (see Fig. 1a). Neighboring cavities are separated
by the distance L0.
The atomic level structure is represented in Fig. 1b.
All the atoms are initially prepared in the “reservoir”
state |s⟩, and the atoms have, in addition, six metastable
states denoted by |0L⟩, |1L⟩, |0R⟩, |1R⟩, |0A⟩, |1A⟩, three
excited states |ϕ+⟩, |ϕ−⟩, |ϕA⟩and three high-lying Ry-
dberg states |r+⟩, |r−⟩, |rA⟩. We assume that the tran-
sitions given in Table I can be independently and se-
lectively addressed by appropriately tuned laser beams.
In particular, it implies that we can couple pairs of
states, |s⟩↔|r±,A⟩, |0L,R⟩↔|r−⟩, |1L,R⟩↔|r+⟩and
|0A⟩, |1A⟩↔|rA⟩via the intermediate states |ϕ+⟩, |ϕ−⟩
or |ϕA⟩.
|0, 1A⟩↔|ϕA⟩
|0L,R⟩↔|ϕ−⟩
|1L,R⟩↔|ϕ+⟩
|s⟩
σ±
←→|ϕ±⟩
|ϕA⟩↔|rA⟩
|ϕ±⟩↔|r±⟩
|0L,R,A⟩↔|1L,R,A⟩
Table I: The transitions required by our protocol.
We further suppose that the atomic samples are
small enough to operate in the full Rydberg block-
ade regime, i.e. their size should not exceed a few
µm.
As a consequence, when driving the transition
|s⟩↔|r±,A⟩on a sample with Na atoms initially
in the state |s . . . s⟩, multiply excited states are out
of resonance due to the strong dipole-dipole interac-
tion among Rydberg excited atoms, and the transfer of
more than a single atom to the Rydberg state |r±,A⟩
is blocked.
The ﬁelds are applied symmetrically to
all atoms in each sample, and they hence excite the
symmetric collective state with a single Rydberg exci-
tation, (|rks . . . s⟩+ |srks . . . s⟩+ . . . + |s . . . srk⟩) /√Na.
The associated coupling strength is easily seen to be
magniﬁed by the factor √Na with respect to the cou-
pling strength of the single atom transition |s⟩
↔
|rk⟩.
Applying a π pulse on the collective ensem-
ble transition, followed by the single-particle transi-
tion |rk⟩→|j⟩(j = 0L, 1L, 0R, 1R, 0A, 1A), prepares
the
sample
in
a
stable
symmetric collective state
|N0L, N1L, N0R, N1R, N0A, N1A⟩where the Nj’s denote
the populations of the diﬀerent internal levels, restricted
to values 0 and 1.
Unitary operations can be applied
in the eight-dimensional subspace of collective states,
{|N0L, (1 −N0L) , N0R, (1 −N0R) , N0A, (1 −N0A)⟩}, by
simply driving the corresponding single-atom transi-
tions |0L,A,R⟩↔|1L,A,R⟩and/or |0L,A,R⟩, |1L,A,R⟩↔
|r+,−,R⟩, as described in [13, 15].
The collective state
pairs (|0L⟩, |1L⟩), (|0R⟩, |1R⟩), and (|0A⟩, |1A⟩) at each
repeater node can thus be associated with three qubits,
referred to as the left (L), right (R) and auxiliary (A)
subnodes, in the following.
We shall use a simpliﬁed notation for ensemble states,
denoting the collective internal state population as ¯0
and ¯1, such that, e.g., |¯0L; ¯1R; ¯1A⟩denotes the state
|N0L = N1R = N1A = 1; N1L = N0R = N0A = 0⟩, where
both the right and the auxiliary subnodes occupy the
logic state 1, while the left subnode is in state 0.
It is a further requirement of our protocol that the
transitions |s⟩←→|ϕ±⟩couple non-resonantly to two
diﬀerent modes, ±, with equal frequency and with de-
tunings ∆± with respect to the atomic transitions, but
diﬀerent polarization in the cavity (this will legitimate
the assumptions we make below on the ﬁber transmis-
sion/losses).
Driving the upper transition |r±⟩←→
|ϕ±⟩with a laser ﬁeld with detuning ∆± and Rabi fre-
3
Blockade radius
Na atoms
a+,a-
s
R1
L2
R2
L3
R3
LN
(1)
(1)
(1)
(1)
(2)
(2)
(3)
(3)
(3)
(3)
a)
b)
c)
L0
0L
j-
D+
j+
D-
r-
s-
s+
g-
g+
W+ 
W-
r+
1L
0R
1R
0A
1A
jA
rA
Figure 1: (Color online) a) The physical set-up for our quan-
tum repeater.
N atomic ensembles are placed in two-mode
cavities linked by optical ﬁbers.
b) Atomic level structure.
The ﬁgure shows the “quantum-classical” two-photon transi-
tions, |s⟩←→|r±⟩driven via the intermediate states |ϕ±⟩
with coupling strength g± to the quantized cavity ﬁeld modes
± and with Rabi frequencies Ω± detunings ∆± to the classi-
cal laser control ﬁelds. c) The three steps of our scheme. (1)
entanglement of pairs of neighboring subnodes (Rk, Lk+1), en-
tanglement swapping through two-bit gates (2) on each pair
(Lk, Rk) and measurement (3) of all subnodes but (R1, LN).
quency Ω±, induces a second-order quantum-classical
process, described by the single-atom eﬀective Hamilto-
nian ℏg±Ω±
∆±
a†
± |s⟩⟨r±|+h.c. where a± denotes the annihi-
lation operator of the cavity mode ± and g± its coupling
strength. This Hamiltonian derives from the adiabatic
elimination of the intermediate state |ϕ±⟩[19], and is
valid for |∆±| ≫|Ω±| , |g±|.
Performing an ensemble
π pulse on the quantum-classical two-photon transition
|s⟩↔|ϕ±⟩↔|r±⟩hence converts a collective Rydberg
excitation |r±⟩into a cavity photon ± and the other way
around, with the coupling strength ℏ√Nag±Ω±/∆±. We
emphasize that, though only a single cavity photon is
emitted/absorbed during the process, the coupling can
be made strong, thanks to the atomic ensemble magni-
ﬁcation factor √Na [20]. To avoid spurious interference
eﬀects we suggest to apply diﬀerent detuning parameters
for the two transitions proceeding via the same interme-
diate state |ϕ±⟩.
Optical ﬁbers [21] couple the cavities to each other, and
we simply assume that the ﬁber between two neighboring
cavities (k, k + 1) achieves the coupling
Vk,k+1 =
X
j=0,1
ℏαk,j
h
ak,ja†
k+1,j + a†
k,jak+1,j
i
(1)
with a coupling strength αk,j between the modes j =
+, −in the kth cavity with annihilation operator ak,j,
and the same modes in the (k + 1)th cavity. Since the
modes (+, −) diﬀer by their polarizations but have the
same frequency, we make the reasonable assumption that
the αk,j’s have the same value α for all (k, j). We more-
over suppose that the coupling between two neighboring
cavities can be switched on and oﬀ, for instance by a
controlled Pockels cell : this will allow us to isolate and
separately deal with pairs of coupled nodes.
Due to ﬁber loss, the transmission of a photon from
one cavity to its neighbor is not perfect. We shall as-
sume that the transmission eﬃciency is the same for
all ﬁber connections and can be written under the form
ηt = exp (−L0/Latt) where Latt is the attenuation length,
typically of the order of 22km (corresponding to losses
of 0.2dB/km). The probability for loosing one photon
(+, −) during the transmission along a ﬁber mode of
length L0 is thus given by (1 −ηt).
III.
THE SCHEME
In this section, we describe how to entangle two remote
nodes using the model we presented in the previous sec-
tion. First, we brieﬂy sketch the diﬀerent steps of our
scheme in the ideal case without losses. Then, we show
how to make our method immune to photon loss and
spontaneous emission from the Rydberg level. Finally,
we analyze the eﬀects of other possible errors on the per-
formance of our protocol.
A.
The diﬀerent steps of the scheme
Initially, all the cavities are empty and all ensem-
ble atoms are in the reservoir state |s . . . s⟩.
The ﬁrst
step consists in entangling pairs of neighboring subnodes
(Rk, Lk+1) (see Fig. 1c). To this end, one applies the
sequence of operations given in Table II. In this table,
dashed-line arrows are used for non-resonant couplings
to the intermediate states. Moreover, the “ensemble” na-
ture of pulses is emphasized by a √Na factor above the
concerned arrows.
Finally, we indicate when a cavity
mode is involved in a transition |s⟩↔|ϕ±⟩by writing
“single photon ±” above the corresponding arrow.
4
i) simultaneous π pulses (same Rabi frequency) on ensemble (k)



|s⟩
√Na
99K |ϕ−⟩99K |r−⟩
|s⟩
√Na
99K |ϕ+⟩99K |r+⟩
ii) π pulse on ensemble (k) |r−⟩99K |ϕ−⟩
single photon -, √Na
99K
|s⟩
iii) π pulse on ensemble (k) |s⟩
√Na
99K |ϕ−⟩99K |r−⟩
iv) π pulse on ensemble (k) |r+⟩99K |ϕ+⟩
single photon +, √Na
99K
|s⟩
v) π pulse on ensemble (k) |s⟩
√Na
99K |ϕ+⟩99K |r+⟩
vi) π pulse on ensemble (k) |r−⟩99K |ϕ−⟩99K |0R⟩
vii) π pulse on ensemble (k) |r+⟩99K |ϕ+⟩99K |1R⟩
viii) Transfer of the photon through the ﬁber
from cavity (k) to cavity (k + 1)
ix) π pulse on ensemble (k + 1) |s⟩
single photon -, √Na
99K
|ϕ−⟩99K |r−⟩
x) π pulse on ensemble (k + 1) |r−⟩99K |ϕ−⟩99K |0L⟩
xi) π pulse on ensemble (k + 1) |s⟩
single photon +, √Na
99K
|ϕ+⟩99K |r+⟩
xii) π pulse on ensemble (k + 1) |r+⟩99K |ϕ+⟩99K |1L⟩
Table II: The diﬀerent steps of the entanglement generation procedure.
The ﬁrst seven pulses (i −vii) in Table II prepare
the subnode (Rk) and the cavity (k) in the entan-
gled state (|¯0R⟩⊗|−⟩+ |¯1R⟩⊗|+⟩) /
√
2 where |±⟩de-
notes the number state |n± = 1⟩of the cavity mode
±. The photon thus released is then transferred to the
cavity (k + 1) through the ﬁber (step viii).
The last
