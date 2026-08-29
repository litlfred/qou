---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra Miguel Tierz"
section_id: sec-007-0-aisu-aitu-du-figure-7b
section_title: "Ai(s+u) Ai(t+u) du. Figure 7(b)"
section_number: 0
pages: 24-27
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
doc_brief: "Edge universality in Floquet sideband spectra Miguel Tierz — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a"
---
shows the thermal crossover on the diagonal.
This makes condition (5) of the Introduction quantitative: the zero-temperature Airy edge is
sharp when
kBTel ≪ℏΩκA = ℏΩ(A/2)1/3,
(9.13)
and the crossover to thermal broadening occurs at θA ∼1, i.e., kBTel ∼ℏΩκA.
For a drive
frequency Ω/2π = 10 GHz and A = 50, one has hf/kB ≈0.48 K and κ50 = (50/2)1/3 ≈2.9, giving
Tcross ∼hfκA/kB ≈1.4 K—well above typical dilution-fridge base temperatures, confirming that
the Airy edge should be experimentally accessible.
For θA ≪1, a Sommerfeld expansion of (9.12) gives the leading thermal correction on the
diagonal:
K(θ)
Ai (s, s) = KAi(s, s) −π2
3 θ2 Ai(s) Ai′(s) + O(θ4).
(9.14)
This provides a practical formula for experimentalists who need the low-temperature correction
without computing the full integral: the leading effect of finite temperature is a shift proportional
to Ai(s) Ai′(s), which is antisymmetric about the edge and vanishes at s = 0.
Remark 9.2 (Scope of the finite-temperature result). This subsection analyzes the finite-temperature
crossover of the underlying edge kernel. Deriving the corresponding finite-T shot-noise plateau deficit
requires inserting the thermal distribution into the full noise formula (9.1), which yields a convo-
lution of the Airy kernel diagonal with a thermal broadening function; we do not carry out that
derivation here.
10
Conclusion and outlook
We close with a summary of the main results, a platform-by-platform assessment of where the
conditions for edge universality can be met, and a list of open problems.
10.1
Summary
This paper connects two objects that are usually treated separately in the Floquet literature [10, 9]:
the linear detection chain that turns a time trace into a measured number, and the Floquet scattering
matrix that describes how a periodic drive redistributes quantum states across energy sidebands.
The detection kernel Kphys encodes the instrument’s time gate, filter, and analysis frequency [3];
the outgoing correlator C encodes the device physics.
The projection identity (3.8) makes the
bridge between them explicit: the analysis frequency selects a definite coherence order k = n −p
of C, and with a commensurate gate this selection is exact. We have been careful to distinguish
what this bridge does and does not provide: it selects a coherence-order block, not an individual
sideband index. Accessing the soft edge requires spectral resolution beyond the coherence-order
projection: either energy-selective detection, or DC transport observables whose bias dependence is
sensitive to the edge. We have derived a concrete prediction for the latter: the photo-assisted shot
noise slope dSI/dV realizes the same diagonal discrete Bessel kernel K(disc)
A
(νV , νV ) as a function of
24
bias voltage, and the deficit from the high-bias plateau collapses onto KAi(s, s) under the universal
scaling s = (eV/ℏΩ−A)/κA.
Under the conditions enumerated in the Introduction—non-interacting fermions, monochromatic
spatially uniform phase drive, wide-band static scatterer, sharp Fermi step (or double step in the
two-terminal case), kBTel ≪ℏΩκA, and large drive amplitude A ≫1—the outgoing sideband
process at fixed central energy is determinantal.
In the single-step case (equilibrium or single
populated reservoir), the kernel is the discrete Bessel kernel K(disc)
A
, and its soft edge converges
to the Airy kernel on the A1/3 scale [23, 18]. In the two-terminal double-step case (Sec. 5.1), the
kernel is a weighted sum of two shifted Bessel kernels; when the bias window exceeds κA, the edge
correlations near each isolated edge are governed by a thinned Airy kernel τ KAi(s, t) with τ = T
or R, though the lower edge carries a smooth bulk background from the opposite step (negligible in
the tunnel limit). At finite temperature, the edge kernel crosses over to the finite-temperature Airy
kernel [34, 35, 36] with crossover parameter θA = kBT/(ℏΩκA) (Sec. 9.2). We have argued, on the
basis of the two-dimensional structure of Sambe space [24], that multi-tone drives can promote the
fold (Airy) edge to a cusp (Pearcey) edge [37, 43], but the rigorous derivation of this limit from the
explicit two-tone Fourier coefficients remains open.
10.2
Experimental platforms
The six conditions of the Introduction are restrictive but not unrealizable. We briefly assess the
main candidate platforms.
Two requirements pull in different directions. For the theorem (Airy edge of the sideband kernel),
the ideal setting is a channel with energy-independent transmission under monochromatic drive—a
QPC conductance plateau helps with the energy-independence part, but the sharp-step assumption
(condition (4)) is a separate requirement. For the transport prediction (shot-noise plateau deficit),
the signal carries the prefactor T (1−T ), which vanishes on a plateau where T ≈0 or 1. The cleanest
measurement therefore uses a partially transmitting single-channel beam splitter with approximately
energy-flat transmission over the relevant sideband window ∼2AℏΩ.
Condition (4) requires care: a biased two-terminal device has two Fermi steps, giving a double-
step occupation (Sec. 5.1), but when the bias window exceeds the edge width κA, the edge corre-
lations near each step are governed by a thinned Airy kernel; the upper edge is clean, while the
lower edge carries a smooth bulk background that is negligible for T ≪1. Condition (5) requires
Tel ≪Tcross ∼hfκA/kB, which at f = 10 GHz and A = 20 gives Tcross ≈1.1 K—easily satisfied
in a dilution refrigerator. Larger values A ∼50–200 sharpen the collapse but make the wide-band
requirement more demanding; moderate A may be the most practical starting point. Condition (6),
A = eVac/hf ≫1, requires Vac ∼0.8–8 mV at 10 GHz for A ∼20–200, which is accessible though
large enough that drive-induced heating must be monitored.
The most directly testable prediction is the Airy collapse of the shot-noise plateau deficit (Sec. 9).
Photo-assisted shot noise measurements in QPCs are well established [11, 12].
Metallic tunnel junctions [8] (Al/AlOx/Al) are multichannel devices, but in the tunnel limit
(Ti ≪1 for each channel) the shot noise is a sum of independent single-channel contributions,
each weighted by Ti(1 −Ti) ≈Ti. The plateau deficit for each channel carries the same Airy edge
structure; what changes is only the overall prefactor.
SIS junctions [7], the historical setting of Tien–Gordon physics, satisfy conditions (2) and (6)
but the BCS gap structure violates the wide-band condition (3) near the gap edge; whether the
A1/3 scaling survives there is open. Superconducting microwave circuits [3] are typically bosonic,
invalidating the determinantal structure, unless a fermionic channel (e.g., an embedded normal-
metal junction) is present. AC-gate-driven quantum dots [9] suffer from Coulomb blockade (violating
25
condition (1)) except in the open-dot regime, where achievable amplitudes (A ∼1–10) limit the edge-
scaling window. Cold atoms in driven optical lattices [1] realize non-interacting Floquet regimes,
but the Landauer scattering framework does not directly apply and a separate reformulation in
terms of quasienergy band structure would be needed.
10.3
Open directions
Several extensions of this work are worth pursuing. The most immediate is the explicit derivation of
the Pearcey edge scaling from the two-tone Fourier coefficients (7.1), including the identification of
the cusp-specific edge scale and the verification of the expected quartic normal form by stationary-
phase analysis [26, 40]. A second direction is extending the finite-temperature edge kernel of Sec. 9.2
to a full finite-T prediction for the photo-assisted shot-noise plateau deficit, by inserting the thermal
occupation into the noise formula [8] and tracking the crossover at θA ∼1.
Third, an intriguing question is the edge universality class for general drive waveforms. The
leviton program [16, 15] uses shaped voltage pulses with specific Fourier coefficients Fk to engineer
minimal-excitation states; for a Lorentzian pulse, Fk decays exponentially rather than through the
power-law turning-point structure of Jk(A), so the sideband edge is not a fold and the Airy kernel
does not apply. More generally, the edge universality class of the sideband kernel built from Fk
depends on the saddle-point structure of the integral defining Fk, and different pulse shapes may
realize different members of the catastrophe-kernel hierarchy. Classifying these edges for the exper-
imentally relevant pulse families (Lorentzian, cosine, square, multi-tone) is an open problem that
would connect the edge-universality picture of this paper to the electron quantum optics toolbox. A
distinct direction concerns the extension to interacting fermions, where condition (1) is relaxed. A
perturbative fluctuation relation has been shown [45] to extend the sideband transmission picture
to strongly correlated systems—Luttinger liquids, fractional quantum Hall edges, Josephson junc-
tions in dissipative environments—with the Bessel weights replaced by many-body matrix elements;
recent applications to AC-driven fractional quantum Hall systems [46] show that Levitov’s theorem
on minimal excitations is violated in that regime. Whether any analogue of the Airy edge structure
survives with interactions is an open question.
On the bosonic side, the analogue of the present analysis—where the Slater determinant is
replaced by a Gaussian state and the Airy kernel enters through the first-order coherence rather
than through fermionic Wick contractions [19]—is an open problem with potential applications to
parametrically driven photonic circuits. In that setting, the no-click probability takes the form of
a bosonic Fredholm determinant, P0 = det(Id + κK)−1, and the same soft-edge reduction would
imply Tracy–Widom–type tail exponents in directly measurable photostatistics; for phase-sensitive
(squeezed) states, anomalous correlators promote this to a symplectic block structure. Such predic-
tions are relevant to platforms where Kardar–Parisi–Zhang universality of bosonic phase fluctuations
has recently been established experimentally [47]. Finally, extending the connection between the
detection chain and the correlator to include the effects of feedback, adaptive measurement, and
quantum-limited amplification [3] would bring the formalism closer to the operational reality of
circuit-QED experiments.
Acknowledgements. The author is grateful to Leonardo Santilli and David Trillo for correspon-
dence. This work was supported by the Shanghai Institute for Mathematics and Interdisciplinary
Sciences (SIMIS-ID-2025-QT).
26
A
Technical proofs
This appendix collects the two technical proofs deferred from the main text: the Christoffel–Darboux
identity for the discrete Bessel kernel (Sec. A.1) and the Airy-limit convergence theorem (Sec. A.2).
A brief sketch connecting the standard shot-noise formula to the correlator framework is given in
Sec. A.3.
A.1
Christoffel–Darboux identity for the discrete Bessel kernel
We prove the identity (5.8). Start from the three-term recurrence for Bessel functions [20],
2(ν + r)
A
Jν+r(A) = Jν+r−1(A) + Jν+r+1(A).
(A.1)
For ν̸ = λ, multiply by Jλ+r(A) and subtract the same identity with ν and λ interchanged to obtain
2(ν −λ)
A
Jν+r(A)Jλ+r(A) = Jν+r−1(A)Jλ+r(A) −Jν+r(A)Jλ+r−1(A)
+ Jν+r+1(A)Jλ+r(A) −Jν+r(A)Jλ+r+1(A).
The right-hand side telescopes when summed over r = 0, 1, 2, . . . . Since Jk(A) →0 as k →∞for
fixed A, the boundary term at infinity vanishes. Collecting the surviving r = 0 boundary term and
dividing by 2(ν −λ)/A gives
K(disc)
A
(ν, λ) = A
2
Jν−1(A)Jλ(A) −Jν(A)Jλ−1(A)
ν −λ
.
A.2
Proof of the soft-edge Airy limit (Theorem 6.1)
The proof combines the turning-point estimate (6.5) with a Riemann-sum argument.
Step 1: Pointwise approximation.
The Debye–Olver uniform asymptotic [21] for integer order
n near argument A gives κAJn(A) = Ai((n −A)/κA) + O(A−2/3) uniformly on compact sets.
Composing with the floor in the rescaling νA(s) = ⌊A + sκA⌋introduces a shift δ/κA with |δ| ≤1
in the Airy argument. By Lipschitz continuity of Ai on compacts, the resulting error is O(A−1/3),
giving (6.5). The global tail bound |κAJνA(s)(A)| ≤Ce−cs for s ≥0 (the weaker corollary of the
piecewise estimate stated in the main text) carries over with the same adjustment.
Step 2: Riemann-sum approximation.
Fix a compact rectangle Q = [−M, M]2. For u ≥0
