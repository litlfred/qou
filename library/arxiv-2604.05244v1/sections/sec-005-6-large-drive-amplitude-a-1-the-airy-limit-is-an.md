---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra Miguel Tierz"
section_id: sec-005-6-large-drive-amplitude-a-1-the-airy-limit-is-an
section_title: "Large drive amplitude A ≫1. The Airy limit is an asymptotic statement as A →∞; the edge"
section_number: 6
pages: 2-7
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
doc_brief: "Edge universality in Floquet sideband spectra Miguel Tierz — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a"
---
region has width ∼A1/3 sidebands.
The main experimental platform is a quantum point contact or tunnel junction driven by a monochro-
matic AC voltage at low temperature—the setting of Tien–Gordon photon-assisted transport. The
exact single-step theorem applies when the device is in equilibrium or when a single populated
reservoir dominates the outgoing channel; the standard biased two-terminal case is handled by
the multi-step extension of Sec. 5.1. Superconducting microwave circuits can also approximate this
regime, but only when the circuit contains a fermionic channel (e.g., a normal-metal tunnel junction
embedded in a cavity) and the drive is monochromatic; purely bosonic Josephson-junction modes
do not satisfy the determinantal structure assumed here. Multi-mode, interacting, or strongly dissi-
pative Floquet platforms—such as driven many-body cold-atom systems or periodically modulated
strongly correlated materials—are not expected to exhibit the specific Bessel/Airy edge structure
derived here, though they may display other forms of universality.
2
The mathematical asymptotics that connect Bessel functions to the Airy function near a turning
point are classical [20, 21]: when the order n of a Bessel function approaches its argument A, Jn(A)
crosses over from oscillatory to exponentially decaying, and in the transition region of width ∼A1/3
the Bessel function is approximated by the Airy function. What is new in this paper is, first, the
identification of the discrete Bessel kernel as the exact correlation kernel of the outgoing sideband
process at any drive amplitude, and second, the derivation of a directly measurable transport
observable—the photo-assisted shot-noise plateau deficit—whose large-A scaling isolates the Airy
edge without requiring sideband-resolved detection. This observable converges to the Airy-kernel
diagonal KAi(s, s) = Ai′(s)2 −s Ai(s)2, not to Ai2(s)—the pointwise Debye–Olver envelope of the
individual Bessel weights J2
ℓ(A); the two functions have different structure in both the bulk and
the tail (Fig. 6), and the distinction is the concrete sense in which the result goes beyond classical
turning-point asymptotics.
Under conditions (1)–(6), the outgoing sideband occupations at fixed central energy form a
determinantal point process—all correlation functions are determinants of the two-point kernel [22,
18]. In the single-step case, the kernel is the discrete Bessel kernel K(disc)
A
; in the two-terminal
double-step case (Sec. 5.1), it is a weighted sum of two shifted Bessel kernels. In either case, the
edges of the process lie near n ∼mF + A, where mF is the Fermi cutoff, and in a turning-point
region of width ∼A1/3 the local kernel converges to the Airy kernel familiar from random matrix
theory [23, 18]. In the double-step case, each edge is governed by a thinned Airy kernel τ KAi plus a
smooth bulk background from the other step; the background is negligible in the tunnel limit T ≪1.
This is proved in Theorem 6.1 and illustrated numerically in Figs. 3–4. The same diagonal discrete
Bessel kernel also appears in a different observable: the first bias derivative of the photo-assisted
shot noise realizes K(disc)
A
(νV , νV ), with νV := ⌈eV/ℏΩ⌉, as a function of bias voltage, so that the
deficit from the high-bias plateau provides a parameter-free test of the Airy scaling in a standard
DC noise measurement (Sec. 9).
Two figures encode the two halves of this story. Figure 1 shows the measurement side: time gat-
ing, frequency windowing, and spectrogram analysis of the Floquet signal. Figure 2 shows the device
side: the sideband ladder, the Floquet scattering matrix Snm with mixing order k = n −m, and
the outgoing correlator C = S∗NST . A recurring theme is the two-dimensional structure of Sambe
space [24]—Floquet angle × quasienergy—which provides a natural physical control manifold. In
this manifold, cusp (Pearcey) edge singularities already known in random matrix theory [25, 26]
become accessible: extra control parameters, such as additional drive tones, make cusps realizable
in addition to folds (Airy).
The paper is organized as follows. Section 2 defines the detection kernel and explains why it
must be specified. Section 3 introduces the Floquet scattering formalism and derives the projection
identity that bridges the measurement and device sides. Section 4 specializes to the monochromatic
Tien–Gordon model and derives the Toeplitz (Bessel) structure. Section 5 identifies the outgoing
correlator as a discrete Bessel kernel under conditions (1)–(4) and extends the analysis to two-
terminal double-step occupations. Section 6 proves the Airy-kernel soft-edge limit (condition (6)).
Section 7 extends the discussion to multi-tone drives, where the fold edge can be promoted to a cusp
governed by the Pearcey kernel. Section 8 brings the threads together and discusses the measurement
signatures of both universality classes. Section 9 derives the concrete Airy-edge prediction for the
photo-assisted shot-noise plateau deficit and the finite-temperature crossover.
3
0
20
Time t (T = 2 / )
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
|ebb(t)|
tedge
t0
u0 = cedge(t0
tedge)
(a) time window
5
0
5
Angular frequency 
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Schematic magnitude
edge
0
u0 = cedge(
0
edge)
baseband comb at n
(b) frequency window
0
20
Time t (T = 2 / )
3
2
1
0
1
2
3
Angular frequency 
edge
0
u0 = cedge(
0
edge)
(c) spectrogram view
Figure 1: Windowed analysis of a Floquet signal.
A finite time/frequency window defines the
detection kernel that weights harmonics at ω = nΩ; the spectrogram shows their time localization.
See Sec. 2.
2
Measurement-side viewpoint: windowing, demodulation, and the
detection kernel
We begin on the instrument side. The key object is the detection kernel Kphys [3], which encodes
everything the acquisition chain does to the raw signal before reporting a number. We first define
it in the simplest case, then generalize and discuss its role.
2.1
A linear readout functional
Let ˆY (t) denote the Heisenberg operator associated with the measured output signal. Depending on
the implementation, ˆY (t) could be a photocurrent, a microwave voltage, a filtered current, or any
other linear transducer output. The simplest (and most common) readout consists of two operations:
a rectangular time gate W(t) = 1[t0−L, t0](t) that selects the acquisition interval, and multiplication
by e−iω0t to demodulate at the analysis frequency ω0. The measured complex number is then
ˆu0(ω0; t0) :=
Z t0
t0−L
dt e−iω0t ˆY (t).
(2.1)
This is the operator version of the standard IQ (in-phase/quadrature) projection [27, 28]: Re ˆu0
and Im ˆu0 are the familiar I and Q quadratures.
More generally, an additional low-pass filter or integrator with impulse response h(t) may precede
the readout, giving the detection kernel
Kphys(t; ω0, t0) := h(t0 −t) W(t) e−iω0t,
ˆu0(ω0; t0) =
Z ∞
−∞
dt Kphys(t; ω0, t0) ˆY (t).
(2.2)
4
m=−3
m=−2
m=−1
m=0
m=+1
m=+2
m=+3
µ
input sidebands
Em
n=−3
n=−2
n=−1
n=0
n=+1
n=+2
n=+3
output sidebands
+2Ω
+Ω
−Ω
−2Ω
Snm = U(E)Jn −m(A)
k = n −m  (mixing order)
eiAsinΩt
Cnp(E) =
X
m
Jn −m(A)Jp −m(A) ¯f(Em)
incoming
outgoing
Figure 2: Floquet scattering between harmonics. Sideband n receives amplitude from m via Snm
(mixing order k = n −m); outgoing correlations obey C = S∗NST . See Sec. 3.
The corresponding frequency response,
cdet(∆ω) :=
Z ∞
−∞
dt h(t0 −t)W(t)e−i∆ωt,
(2.3)
will be referred to as the detector response function. For the simple rectangular gate with h ≡1, this
reduces to cdet(∆ω) = e−i∆ω(t0−L/2)L sinc(∆ωL/2), where sinc(x) := sin(x)/x (with sinc(0) := 1).
Tapered windows (Hann, Blackman, etc. [29]) suppress spectral leakage at the cost of a broader
main lobe, but the rectangular gate suffices for the integer-period orthogonality argument used in
the rest of this paper.
Remark 2.1 (Heterodyne is convenient, not necessary). The signal-processing viewpoint is not
intrinsically heterodyne. Analog heterodyne detection is one physical way to implement the projec-
tion (2.2), but the same quantity can be obtained from a digitized trace by numerical Fourier binning
or short-time Fourier analysis. Homodyne detection corresponds to ω0 = 0 in the rotating frame,
heterodyne to ω0̸ = 0, and digital post-processing to the same integral carried out offline; see [6, 3].
2.2
Why the detection kernel must appear in the theory
The detection kernel is not an optional add-on; it is the mathematical representation of the experi-
mental fact that no apparatus records the full operator-valued function ˆY (t) directly. Every readout
scheme projects the time trace onto a finite temporal mode. A rectangular gate gives one mode,
a Hann window [29] another, a narrow intermediate-frequency (IF) filter yet another. Any theory
intended to predict what is actually reported by the experiment must include Kphys at the point
where the operator ˆY (t) is converted into the measured complex amplitude ˆu0.
This observation is especially important in Floquet systems because the signal naturally de-
composes into harmonics spaced by the drive frequency [24, 10]. The detection kernel determines
whether these harmonics are resolved, partially mixed, or averaged out. In particular, if the gate
spans an integer number of periods and the filter is ideal, then the analysis frequency ω0 = kΩpicks
5
out a single Fourier block exactly. That exact block-selection property will later allow us to connect
the measured signal directly to the sideband correlator Cnp.
3
Input–output Floquet scattering and outgoing correlators
We now turn to the device side. The periodically driven scatterer is described by a Floquet scattering
matrix Snm(E) [10, 30] that connects incoming and outgoing sideband operators. From S and the
incoming occupation N, we construct the outgoing one-body correlator C and derive the projection
identity that bridges the measurement and device sides.
3.1
Sideband operators and the Floquet scattering matrix
Let E ∈[0, ℏΩ) denote a central energy in a Floquet Brillouin zone [24]. For each lead or channel
α we introduce fermionic annihilation operators
aαm(E),
bαn(E),
m, n ∈Z,
which remove incoming and outgoing particles at energies
Em = E + mℏΩ,
En = E + nℏΩ.
They satisfy the canonical anti-commutation relations
{aαm(E), a†
βm′(E′)} = 2π δ(E−E′) δαβ δmm′,
{bαn(E), b†
βn′(E′)} = 2π δ(E−E′) δαβ δnn′, (3.1)
with all other anti-commutators zero.
For a periodically driven, phase-coherent scatterer, incoming and outgoing sidebands are related
by the Floquet scattering matrix [30, 10]:
bαn(E) =
X
β,m∈Z
Sαβ
nm(E) aβm(E).
(3.2)
The integer
k := n −m
(3.3)
is the mixing order: it counts the net number of drive quanta exchanged between input and output
sidebands. Figure 2 gives the corresponding bookkeeping picture.
If reservoir β is in equilibrium with distribution fβ [10, 4], then
⟨a†
βm(E)aβ′m′(E′)⟩= 2π δ(E −E′) δββ′ δmm′ fβ(Em).
(3.4)
The outgoing one-body correlator in lead α is therefore
C(α)
np (E) := ⟨b†
αn(E)bαp(E)⟩=
X
β,m
Sαβ∗
nm (E) fβ(Em) Sαβ
pm(E).
(3.5)
In matrix notation, C = S∗NST with Nmm′ = δmm′f(Em). In the single-channel Tien–Gordon
model, Snm = eiδ(E)Jn−m(A) where δ(E) is a scattering phase. Since δ is a scalar, it cancels in the
product S∗NST = JNJT (equivalently, SNS† = JNJT ), and the correlator depends only on the
real Bessel entries:
Cnp =
X
m
Jn−m(A) Jp−m(A) f(Em).
(3.6)
6
This simplification holds for any single-channel scatterer, regardless of the value of δ(E). For a
multi-channel device with a non-scalar Uαβ(E), the full matrix form C = S∗NST must be retained,
and the correlator acquires a channel-dependent prefactor (see Sec. 5 for the conditions under which
it reduces to a Bessel kernel).
Equation (3.5) is the correlation matrix represented at the output of the ladder diagram in
Fig. 2.
3.2
Connecting the measurement to the correlator
With the detection kernel defined on the instrument side and the correlator C defined on the device
side, we can now state the central identity that connects them. A closely related signal-processing
viewpoint on electronic coherences has been developed independently in the electron quantum optics
literature [31]. The physics is simple: because the output signal ˆYα(t) is bilinear in the outgoing field
operators, and because the detection kernel is a linear weighting in time, the measured expectation
value is a bilinear functional of C, weighted by the detector response cdet. The analysis frequency ω0
then acts as a tunable selector that picks out a specific off-diagonal block of the Floquet correlator.
Concretely, assume that the detector is sensitive to a linear, number-conserving output observ-
able in lead α [3]. Any such observable is a one-body operator, bilinear in the outgoing field, and
can be expanded in the Floquet basis [24, 10] as
ˆYα(t) =
X
n,p∈Z
Z ℏΩ
0
dE
2πℏei(n−p)Ωt G(α)
np (E) b†
αn(E)bαp(E),
(3.7)
where the coupling matrix G(α)
np (E) depends on the specific transducer and is in general not diagonal
in the sideband indices; for example, a current operator mixes different sidebands through the
velocity matrix elements. The decomposition (3.7) is the most general number-conserving one-body
form at fixed central energy E; it excludes anomalous terms (b b or b†b†) by the number-conservation
assumption. The key observation is that the time dependence of each term is carried entirely by
the phase ei(n−p)Ωt, so the detection kernel acts on it through the detector response evaluated at
the detuning ω0 −(n −p)Ω.
Inserting (3.7) into (2.2) and taking the expectation value gives the projection identity
⟨ˆu(α)
