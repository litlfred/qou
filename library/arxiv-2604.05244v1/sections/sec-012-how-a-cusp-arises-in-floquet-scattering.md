---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-012-how-a-cusp-arises-in-floquet-scattering
section_title: "How a cusp arises in Floquet scattering"
section_number: null
pages: 15-16
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.989
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
Consider a scatterer driven by two commensurate tones at frequencies $\Omega$ and $2\Omega$, with amplitudes $A_1$ and $A_2$. The time-dependent gauge phase becomes $$\phi(t) = A_1\sin(\Omega t) + A_2\sin(2\Omega t + \varphi),$$ and the Floquet scattering amplitudes involve products of Bessel functions (or, more generally, Fourier coefficients of $e^{i\phi(t)}$) that depend on both $A_1$ and $A_2$. The resulting correlator $C=S^*NS^T$ still has a spectral edge near the largest populated sideband, but the edge geometry now depends on two parameters.

For generic values of $A_2$ the edge near the largest populated sideband remains a fold (governed by the Airy kernel, as in the single-tone case). However, when $A_2$ is tuned to a critical value, two fold edges---each individually governed by the Airy kernel---can merge into a single cusp. On general grounds from catastrophe theory [@ArnoldSingularities; @BerryUpstill1980], this is the expected codimension-two singularity: the discriminant of the stationary-phase equation $\partial_\xi\Phi=0$ vanishes at the cusp point, and the normal form of the generating phase becomes quartic rather than cubic, $$\Phi(\zeta;\sigma,\gamma) = \tfrac{1}{4}\zeta^4 - \tfrac{\gamma}{2}\zeta^2 - \sigma\,\zeta,
  \label{eq:cusp-phase}$$ where $\sigma$ is the edge coordinate (analogous to $s$ in the fold case) and $\gamma\ge 0$ is the *unfolding parameter* that controls the distance from the cusp. Setting $\gamma=0$ gives the cusp itself; for $\gamma>0$ the cusp unfolds into two symmetric folds located at $\sigma_{\rm edge}(\gamma)=\pm\frac{2}{3\sqrt{3}}\gamma^{3/2}$.
