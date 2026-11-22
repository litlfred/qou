---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-005-sideband-operators-and-the-floquet-scattering-ma
section_title: "Sideband operators and the Floquet scattering matrix"
section_number: null
pages: 6-7
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.99
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
Let $E\in[0,\hbar\Omega)$ denote a central energy in a Floquet Brillouin zone [@Sambe1973]. For each lead or channel $\alpha$ we introduce fermionic annihilation operators $$a_{\alpha m}(E),\qquad b_{\alpha n}(E),\qquad m,n\in\mathbb Z,$$ which remove incoming and outgoing particles at energies $$E_m = E + m\hbar\Omega,\qquad E_n = E + n\hbar\Omega.$$ They satisfy the canonical anti-commutation relations $$\{a_{\alpha m}(E),a^\dagger_{\beta m'}(E')\}
  = 2\pi\,\delta(E-E')\,\delta_{\alpha\beta}\,\delta_{mm'},
  \qquad
  \{b_{\alpha n}(E),b^\dagger_{\beta n'}(E')\}
  = 2\pi\,\delta(E-E')\,\delta_{\alpha\beta}\,\delta_{nn'},
  \label{eq:CAR}$$ with all other anti-commutators zero.

For a periodically driven, phase-coherent scatterer, incoming and outgoing sidebands are related by the Floquet scattering matrix [@LiReichl1999; @MoskBuett2002]: $$b_{\alpha n}(E) = \sum_{\beta,m\in\mathbb Z} S^{\alpha\beta}_{nm}(E)\,a_{\beta m}(E).
  \label{eq:bSa}$$ The integer $$k := n-m
  \label{eq:mixingorder}$$ is the *mixing order*: it counts the net number of drive quanta exchanged between input and output sidebands. Figure [\[fig:floquet-ladder\]](#fig:floquet-ladder){reference-type="ref" reference="fig:floquet-ladder"} gives the corresponding bookkeeping picture.

If reservoir $\beta$ is in equilibrium with distribution $f_\beta$ [@MoskBuett2002; @MoskaletsBook], then $$\langle a^\dagger_{\beta m}(E)a_{\beta' m'}(E')\rangle
  = 2\pi\,\delta(E-E')\,\delta_{\beta\beta'}\,\delta_{mm'}\,f_\beta(E_m).
  \label{eq:inputocc}$$ The outgoing one-body correlator in lead $\alpha$ is therefore $$C^{(\alpha)}_{np}(E)
  := \langle b^\dagger_{\alpha n}(E)b_{\alpha p}(E)\rangle
  = \sum_{\beta,m} S^{\alpha\beta*}_{nm}(E)\, f_\beta(E_m)\, S^{\alpha\beta}_{pm}(E).
  \label{eq:C}$$ In matrix notation, $C=S^*NS^T$ with $N_{mm'}=\delta_{mm'}f(E_m)$. In the single-channel Tien--Gordon model, $S_{nm}=e^{i\delta(E)}J_{n-m}(A)$ where $\delta(E)$ is a scattering phase. Since $\delta$ is a scalar, it cancels in the product $S^*NS^T = JNJ^T$ (equivalently, $SNS^\dagger=JNJ^T$), and the correlator depends only on the real Bessel entries: $$C_{np} = \sum_m J_{n-m}(A)\,J_{p-m}(A)\,f(E_m).
  \label{eq:CJNJ}$$ This simplification holds for any single-channel scatterer, regardless of the value of $\delta(E)$. For a multi-channel device with a non-scalar $\mathcal U^{\alpha\beta}(E)$, the full matrix form $C=S^*NS^T$ must be retained, and the correlator acquires a channel-dependent prefactor (see Sec. [\[sec:discrete-bessel\]](#sec:discrete-bessel){reference-type="ref" reference="sec:discrete-bessel"} for the conditions under which it reduces to a Bessel kernel).

Equation [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"} is the correlation matrix represented at the output of the ladder diagram in Fig. [\[fig:floquet-ladder\]](#fig:floquet-ladder){reference-type="ref" reference="fig:floquet-ladder"}.
