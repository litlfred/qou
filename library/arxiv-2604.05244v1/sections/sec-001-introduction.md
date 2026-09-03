---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra Miguel Tierz"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
doc_brief: "Edge universality in Floquet sideband spectra Miguel Tierz — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a"
---
Periodically driven (Floquet) quantum systems are now routinely realized in superconducting cir-
cuits, optomechanical cavities, semiconductor quantum dots, and cold-atom platforms [1, 2, 3, 4, 5].
In all of these settings the experiment records a finite time trace of a linear output signal—a current,
a voltage, a homodyne photocurrent [6]—and then processes it: filtering, demodulating, gating. The
resulting number depends not only on the physics of the driven device but also on the details of
this linear analysis chain.
The theory of photon-assisted transport (PAT) through AC-driven conductors is by now a mature
field. Tien and Gordon [7] showed that a monochromatic phase drive eiA sin Ωt produces sideband
weights given by Bessel functions Jn(A)—the Fourier coefficients of the drive’s phase factor, with
A the dimensionless drive amplitude. Lesovik and Levitov [8] showed that the photo-assisted shot
noise (PASN) is sensitive to the AC drive even when the average current is featureless. Pedersen
and Büttiker [9] cast PAT in a current-conserving Floquet scattering language; Moskalets and
Büttiker [10] placed it in the broader framework of Floquet scattering theory for quantum pumps
and driven mesoscopic conductors (see also the monograph [4]). On the experimental side, PASN has
been quantitatively tested in quantum point contacts (QPCs) [11, 12]; subsequent work reinterpreted
it in terms of photon-created electron–hole pairs [13] and extended this picture to a full counting
statistics of elementary transfer events [14, 15], while the electron quantum optics program used
PASN as a spectroscopic tool for shaped voltage pulses and leviton states [16, 17]. A comprehensive
review of the field is given in [1]. The present paper does not revisit this established framework;
rather, it identifies a new asymptotic regime—the large-A soft edge of the sideband spectrum—
where the Floquet correlator acquires the universal Airy-kernel structure familiar from random
1
arXiv:2604.05244v1  [cond-mat.mes-hall]  6 Apr 2026
matrix theory (RMT) [18], and derives a concrete transport observable (the shot-noise plateau
deficit) that isolates this edge.
This paper has two goals. The first is to make the logical chain from the measured number
to the outgoing quantum state precise. Every linear readout of a Floquet signal can be written
as a projection of the outgoing one-body correlator C [10], weighted by a detection kernel Kphys
that encodes the instrument’s time gate, filter, and analysis frequency [3].
In matrix notation,
C = S∗NST ; for a single-channel scatterer, the scattering phase cancels and C reduces to JNJT
with the real Bessel matrix Jnm = Jn−m(A). The detection kernel belongs to the instrument; the
correlator belongs to the device. Both are needed to make a falsifiable prediction for the measured
signal, yet in much of the Floquet literature the analysis chain is left implicit. We make it explicit
because it clarifies what the experiment can and cannot access at the sideband level.
The second goal is to show that the correlator itself has universal structure at its spectral edge.
This universality does not hold for arbitrary Floquet systems; it requires a specific combination of
conditions:
1. Non-interacting (free) fermions. The outgoing state must be a Slater determinant [19]. In-
teractions, inelastic processes, and decoherence destroy the determinantal structure on which
the entire analysis rests.
