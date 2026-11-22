---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-007-monochromatic-phase-drive-and-toeplitz-floquet-s
section_title: "Monochromatic phase drive and Toeplitz Floquet scattering"
section_number: null
pages: 9-10
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.995
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:toeplitz label="sec:toeplitz"} We now specialize to the model that leads most naturally to Bessel functions. Consider a static scatterer with scattering matrix $\mathcal U^{\alpha\beta}(E)$, driven by a monochromatic, spatially uniform AC potential $$V(t) = V_{\rm ac}\cos(\Omega t).$$ The corresponding gauge phase is $$\phi(t) = \frac{e}{\hbar}\int^t V(t')\,dt' = A\sin(\Omega t),
  \qquad A := \frac{eV_{\rm ac}}{\hbar\Omega}.$$ The time-dependent phase factor is therefore $$e^{i\phi(t)} = e^{iA\sin(\Omega t)} = \sum_{k\in\mathbb Z} J_k(A)e^{ik\Omega t},
  \label{eq:JacobiAnger}$$ by the Jacobi--Anger expansion [@Watson1944]. Since the drive is spatially uniform, it does not modify the internal mode structure of the scatterer; it only shifts sideband index. Consequently, $$S^{\alpha\beta}_{nm}(E) = \mathcal U^{\alpha\beta}(E)J_{n-m}(A).
  \label{eq:ToeplitzS}$$ The dependence on $n$ and $m$ is Toeplitz: only the difference $n-m$ matters. The factored form [\[eq:ToeplitzS\]](#eq:ToeplitzS){reference-type="eqref" reference="eq:ToeplitzS"} requires that $\mathcal U^{\alpha\beta}(E)$ varies negligibly over the sideband window of width $\sim 2A\hbar\Omega$ centered at the Fermi energy; this wide-band condition is standard in the Tien--Gordon literature [@TienGordon1963; @MoskBuett2002] and is well satisfied whenever the static scattering is smooth on the scale of the drive quantum $\hbar\Omega$.

The same Bessel functions that govern a single phase-modulated tone therefore govern the quantum Floquet $S$ matrix [@TienGordon1963; @Roussel2017]. For a monochromatic, spatially uniform phase drive the signal-processing and scattering pictures are not merely analogous; they are literally described by the same harmonic coefficients.

More generally, any spatially uniform drive---not necessarily a single cosine---produces a Toeplitz Floquet scattering matrix of the form $S^{\alpha\beta}_{nm}=\mathcal U^{\alpha\beta}(E)\,\mathcal F_{n-m}$, where $\mathcal F_k = (2\pi)^{-1}\int_0^{2\pi}e^{i\phi(\theta)}e^{-ik\theta}d\theta$ are the Fourier coefficients of the gauge phase factor $e^{i\phi(t)}$. For a single tone $\phi(t)=A\sin\Omega t$ these reduce to $J_k(A)$; for a multi-tone drive such as $\phi(t)=A_1\sin\Omega t+A_2\sin 2\Omega t$ they become products or convolutions of Bessel functions. This general structure underlies the electron quantum optics program, where shaped voltage pulses with specific $\mathcal F_k$ profiles are used to generate minimal-excitation states (levitons) [@Dubois2013] and PASN serves as a spectroscopic tool for the pulse shape [@VanevicNazarovBelzig2007]. The Toeplitz structure and unitarity ($\sum_k|\mathcal F_k|^2=1$) hold in all cases; what changes is the detailed shape of the sideband envelope, and in particular the geometry of its edge (fold, cusp, or higher). The Bessel case treated below is the simplest and best-studied instance. Whether the same Airy edge persists for general $\mathcal F_k$ is plausible on the grounds that the integral defining $\mathcal F_k$ has the same stationary-phase structure as $J_k(A)$ near the turning point, but a proof would require a separate analysis of the relevant oscillatory integral; we do not pursue this here. For example, the Lorentzian pulse used in leviton generation [@Dubois2013] gives $\mathcal F_k$ that decay exponentially for large $k$, with no turning-point (fold) structure; in that case the sideband edge is *not* of Airy type, and the edge universality class of the corresponding kernel is an open question (see Sec. [\[sec:open\]](#sec:open){reference-type="ref" reference="sec:open"}).

::: lemma
[]{#lem:unitarity label="lem:unitarity"} For fixed $A\in\mathbb R$ one has $$\sum_{r\in\mathbb Z} J_{r+k}(A)J_{r+\ell}(A) = \delta_{k\ell}.
  \label{eq:BesselOrthogonality}$$ Hence the sideband matrix $[J_{n-m}(A)]_{n,m\in\mathbb Z}$ is unitary on $\ell^2(\mathbb Z)$, and if $\mathcal U(E)$ is unitary then so is the full Floquet scattering matrix [\[eq:ToeplitzS\]](#eq:ToeplitzS){reference-type="eqref" reference="eq:ToeplitzS"}.
:::

::: proof
*Proof.* Expand the phase factor [\[eq:JacobiAnger\]](#eq:JacobiAnger){reference-type="eqref" reference="eq:JacobiAnger"} and use Parseval's identity on the unit circle [@Watson1944]: $$\delta_{k\ell}
  = \frac{1}{2\pi}\int_0^{2\pi} e^{-ik\theta}e^{i\ell\theta}\,d\theta
  = \frac{1}{2\pi}\int_0^{2\pi}
    \left(\sum_r J_{r+k}(A)e^{-ir\theta}\right)
    \left(\sum_s J_{s+\ell}(A)e^{is\theta}\right)
    d\theta.$$ Orthogonality of the Fourier exponentials gives [\[eq:BesselOrthogonality\]](#eq:BesselOrthogonality){reference-type="eqref" reference="eq:BesselOrthogonality"}. ◻
:::
