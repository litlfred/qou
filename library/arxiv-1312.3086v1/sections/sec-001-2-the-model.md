---
doc_id: arxiv-1312.3086v1
doc_title: "Quantum repeater with Rydberg blocked atomic ensembles in ﬁber-coupled cavities"
section_id: sec-001-2-the-model
section_title: "The model"
section_number: 2
pages: 2-3
source_pdf: 1312.3086v1.pdf
source_sha256: ff328e7c7cbdc70c
toc_source: inferred
doc_brief: "Quantum repeater with Rydberg blocked atomic ensembles in ﬁber-coupled cavities — 10 sections: Front matter; Introduction; The model"
---
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
