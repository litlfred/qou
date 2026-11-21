---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-003-why-the-detection-kernel-must-appear-in-the-theo
section_title: "Why the detection kernel must appear in the theory"
section_number: null
pages: 5-6
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.979
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
The detection kernel is not an optional add-on; it is the mathematical representation of the experimental fact that no apparatus records the full operator-valued function $\hat Y(t)$ directly. Every readout scheme projects the time trace onto a finite temporal mode. A rectangular gate gives one mode, a Hann window [@Harris1978] another, a narrow intermediate-frequency (IF) filter yet another. Any theory intended to predict what is actually reported by the experiment must include $K_{\rm phys}$ at the point where the operator $\hat Y(t)$ is converted into the measured complex amplitude $\hat u_0$.

This observation is especially important in Floquet systems because the signal naturally decomposes into harmonics spaced by the drive frequency [@Sambe1973; @MoskBuett2002]. The detection kernel determines whether these harmonics are resolved, partially mixed, or averaged out. In particular, if the gate spans an integer number of periods and the filter is ideal, then the analysis frequency $\omega_0=k\Omega$ picks out a single Fourier block exactly. That exact block-selection property will later allow us to connect the measured signal directly to the sideband correlator $C_{np}$.
