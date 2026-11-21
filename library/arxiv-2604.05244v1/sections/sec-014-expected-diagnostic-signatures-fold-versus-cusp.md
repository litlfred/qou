---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-014-expected-diagnostic-signatures-fold-versus-cusp
section_title: "Expected diagnostic signatures: fold versus cusp"
section_number: null
pages: 16-16
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.967
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
If the Pearcey kernel indeed governs the cusp edge, the fold and cusp classes would be distinguished by their tail exponents. At a fold, the rescaled edge density converges to the Airy diagonal $K_{\mathop{\mathrm{Ai}}}(s,s)$ with scale $\kappa_A=(A/2)^{1/3}$ (Sec. [\[sec:airy\]](#sec:airy){reference-type="ref" reference="sec:airy"}). At a cusp, the natural edge scale is different---it is set by the quartic normal form [\[eq:cusp-phase\]](#eq:cusp-phase){reference-type="eqref" reference="eq:cusp-phase"} and generically involves a power of the drive amplitude distinct from $A^{1/3}$. The precise cusp scale depends on the stationary-phase geometry of the two-tone Fourier integral [\[eq:two-tone-Fk\]](#eq:two-tone-Fk){reference-type="eqref" reference="eq:two-tone-Fk"} and has not been derived here.

Regardless of the specific scale, the two classes are distinguished by the *functional form* of the tail. At a fold [@TracyWidom1994; @Forrester2010], $$K_{\mathop{\mathrm{Ai}}}(s,s) \sim \frac{1}{8\pi s}\,e^{-\frac{4}{3}s^{3/2}}
  \qquad\text{(fold)},
  \label{eq:fold-tail}$$ so a log-linear plot in $s^{3/2}$ gives a straight line with slope $-4/3$. At a cusp, the quartic phase produces a tail whose exponent is a different power of the edge coordinate $\sigma$; the specific power depends on the path in the $(\sigma,\gamma)$ unfolding plane and on whether the pure cusp ($\gamma=0$) or a nearby fold ($\gamma>0$) is being probed. What matters for the diagnostic is that the tail is *not* $e^{-\mathrm{const}\cdot s^{3/2}}$: a log-linear plot in $s^{3/2}$ would curve, signaling departure from the fold class.

Two-point fluctuations provide a second diagnostic. At a fold, the sideband-resolved connected correlator scales as $\kappa_A^2\langle N_{\nu_A(s)}N_{\nu_A(t)}\rangle_c\to -|K_{\mathop{\mathrm{Ai}}}(s,t)|^2$ [@TracyWidom1994; @Forrester2010], with the same $e^{-4s^{3/2}/3}$ tail. At a cusp, the analogous scaling involves the cusp-specific edge scale (not $\kappa_A$) and the Pearcey two-point kernel; the precise form remains to be worked out.
