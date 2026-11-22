---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-023-open-directions
section_title: "Open directions"
section_number: null
pages: 26-27
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.996
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:open label="sec:open"}

Several extensions of this work are worth pursuing. The most immediate is the explicit derivation of the Pearcey edge scaling from the two-tone Fourier coefficients [\[eq:two-tone-Fk\]](#eq:two-tone-Fk){reference-type="eqref" reference="eq:two-tone-Fk"}, including the identification of the cusp-specific edge scale and the verification of the expected quartic normal form by stationary-phase analysis [@TracyWidomPearcey; @BleherKuijlaars2007]. A second direction is extending the finite-temperature edge kernel of Sec. [\[sec:finite-T\]](#sec:finite-T){reference-type="ref" reference="sec:finite-T"} to a full finite-$T$ prediction for the photo-assisted shot-noise plateau deficit, by inserting the thermal occupation into the noise formula [@LesovikLevitov1994] and tracking the crossover at $\theta_A\sim 1$.

Third, an intriguing question is the *edge universality class for general drive waveforms*. The leviton program [@Dubois2013; @VanevicNazarovBelzig2007] uses shaped voltage pulses with specific Fourier coefficients $\mathcal F_k$ to engineer minimal-excitation states; for a Lorentzian pulse, $\mathcal F_k$ decays exponentially rather than through the power-law turning-point structure of $J_k(A)$, so the sideband edge is not a fold and the Airy kernel does not apply. More generally, the edge universality class of the sideband kernel built from $\mathcal F_k$ depends on the saddle-point structure of the integral defining $\mathcal F_k$, and different pulse shapes may realize different members of the catastrophe-kernel hierarchy. Classifying these edges for the experimentally relevant pulse families (Lorentzian, cosine, square, multi-tone) is an open problem that would connect the edge-universality picture of this paper to the electron quantum optics toolbox. A distinct direction concerns the extension to *interacting* fermions, where condition (1) is relaxed. A perturbative fluctuation relation has been shown [@Safi2022] to extend the sideband transmission picture to strongly correlated systems---Luttinger liquids, fractional quantum Hall edges, Josephson junctions in dissipative environments---with the Bessel weights replaced by many-body matrix elements; recent applications to AC-driven fractional quantum Hall systems [@TaktakSafi2025] show that Levitov's theorem on minimal excitations is violated in that regime. Whether any analogue of the Airy edge structure survives with interactions is an open question.

On the bosonic side, the analogue of the present analysis---where the Slater determinant is replaced by a Gaussian state and the Airy kernel enters through the first-order coherence rather than through fermionic Wick contractions [@FetterWalecka]---is an open problem with potential applications to parametrically driven photonic circuits. In that setting, the no-click probability takes the form of a bosonic Fredholm determinant, $P_0=\det(\mathrm{Id}+\kappa K)^{-1}$, and the same soft-edge reduction would imply Tracy--Widom--type tail exponents in directly measurable photostatistics; for phase-sensitive (squeezed) states, anomalous correlators promote this to a symplectic block structure. Such predictions are relevant to platforms where Kardar--Parisi--Zhang universality of bosonic phase fluctuations has recently been established experimentally [@Fontaine2022]. Finally, extending the connection between the detection chain and the correlator to include the effects of feedback, adaptive measurement, and quantum-limited amplification [@Clerk2010] would bring the formalism closer to the operational reality of circuit-QED experiments.

**Acknowledgements.** The author is grateful to Leonardo Santilli and David Trillo for correspondence. This work was supported by the Shanghai Institute for Mathematics and Interdisciplinary Sciences (SIMIS-ID-2025-QT).
