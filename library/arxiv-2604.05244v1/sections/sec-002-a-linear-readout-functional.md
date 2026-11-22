---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-002-a-linear-readout-functional
section_title: "A linear readout functional"
section_number: null
pages: 4-5
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.87
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
Let $\hat Y(t)$ denote the Heisenberg operator associated with the measured output signal. Depending on the implementation, $\hat Y(t)$ could be a photocurrent, a microwave voltage, a filtered current, or any other linear transducer output. The simplest (and most common) readout consists of two operations: a rectangular time gate $W(t)=\mathbf{1}_{[t_0-L,\,t_0]}(t)$ that selects the acquisition interval, and multiplication by $e^{-i\omega_0 t}$ to demodulate at the analysis frequency $\omega_0$. The measured complex number is then $$\hat u_0(\omega_0;t_0)
  := \int_{t_0-L}^{t_0} dt\; e^{-i\omega_0 t}\,\hat Y(t).
  \label{eq:u0simple}$$ This is the operator version of the standard IQ (in-phase/quadrature) projection [@Black2001; @Bjorklund1983]: $\mathrm{Re}\,\hat u_0$ and $\mathrm{Im}\,\hat u_0$ are the familiar $I$ and $Q$ quadratures.

More generally, an additional low-pass filter or integrator with impulse response $h(t)$ may precede the readout, giving the detection kernel $$K_{\rm phys}(t;\omega_0,t_0) := h(t_0-t)\,W(t)\,e^{-i\omega_0 t},
  \qquad
  \hat u_0(\omega_0;t_0)
  = \int_{-\infty}^{\infty} dt\; K_{\rm phys}(t;\omega_0,t_0)\,\hat Y(t).
  \label{eq:Kphys}$$ The corresponding frequency response, $$c_{\rm det}(\Delta\omega)
  := \int_{-\infty}^{\infty} dt\; h(t_0-t)W(t)e^{-i\Delta\omega t},
  \label{eq:cdet}$$ will be referred to as the detector response function. For the simple rectangular gate with $h\equiv 1$, this reduces to $c_{\rm det}(\Delta\omega)=e^{-i\Delta\omega(t_0-L/2)}L\,\mathrm{sinc}(\Delta\omega L/2)$, where $\mathrm{sinc}(x):=\sin(x)/x$ (with $\mathrm{sinc}(0):=1$). Tapered windows (Hann, Blackman, etc. [@Harris1978]) suppress spectral leakage at the cost of a broader main lobe, but the rectangular gate suffices for the integer-period orthogonality argument used in the rest of this paper.

::: remark
The signal-processing viewpoint is *not* intrinsically heterodyne. Analog heterodyne detection is one physical way to implement the projection [\[eq:Kphys\]](#eq:Kphys){reference-type="eqref" reference="eq:Kphys"}, but the same quantity can be obtained from a digitized trace by numerical Fourier binning or short-time Fourier analysis. Homodyne detection corresponds to $\omega_0=0$ in the rotating frame, heterodyne to $\omega_0\neq 0$, and digital post-processing to the same integral carried out offline; see [@YuenChan1983; @Clerk2010].
:::
