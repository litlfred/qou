---
doc_id: arxiv-nucl-th-0610105v2
doc_title: "Universal Properties of the Four-Body System with Large Scattering Length"
section_id: sec-002-the-two-body-sector
section_title: "The Two-Body Sector"
section_number: null
pages: 4-5
source_pdf: 0610105v2.pdf
source_sha256: 5f3bd6d31a419d4d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.987
doc_brief: "Universal Properties of the Four-Body System with Large Scattering Length — Few-body systems with large scattering length have universal properties that do not depend on the details of their"
---
[]{#sec:effT:2body label="sec:effT:2body"}

We write the leading order two-body effective potential in momentum space as: $$\langle {\bf p}|V|{\bf q}\rangle=
\langle {\bf p}|g \rangle \lambda_2 \langle g|{\bf q} \rangle ~,
\label{effpot_2}$$

where $\lambda_2$ denotes the two-body coupling constant and ${\bf q}$ (${\bf p}$) are the relative three-momenta in the incoming (outgoing) channel. The regulator functions $$\langle {\bf p}|g\rangle \equiv g(p)=\exp(-p^2/\Lambda^2)~,$$

suppress the contribution from high momentum states. In the few-body literature, they are often called "form factors". For convenience, we will work in units where Planck's constant $\hbar$ is set to unity: $\hbar=1$.

The interaction ([\[effpot_2\]](#effpot_2){reference-type="ref" reference="effpot_2"}) is separable and the Lippmann-Schwinger equation for the two-body problem can be solved analytically. The two-body t-matrix can be written as [@Ziegelmann]: $$\label{t-matrix}
t(E)=|g\rangle\tau(E)\langle g|~,$$

where $E$ denotes the total energy. The two-body propagator $\tau(E)$ is then given by $$\tau(E)=\left[1/\lambda_2-4\pi\int_0^\infty\hbox{d}q\,
  q^2\frac{g(q)^2}{mE-q^2}\right]^{-1}~.$$

A two-body bound-state appears as a simple pole in the two-body propagator $\tau$ at energy $E=-B_2$. Thus for $a>0$, the two-body coupling constant $\lambda_2(B_2,\Lambda)$ can be fixed from the binding energy $B_2$, which is directly related to the scattering length by $a=1/\sqrt{mB_2}$ up to higher order corrections in $l/|a|$. For negative scattering length, there is no shallow dimer state and the coupling constant $\lambda_2$ is fixed from matching to the effective range expansion for positive energies.
