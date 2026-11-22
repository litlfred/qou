---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-020-51-the-type-ii-helicity-supertrace
section_title: "The type II helicity supertrace"
section_number: 5.1
pages: 31-32
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
It is convenient to introduce a generating function, called the *helicity string partition function* in [@Kiritsis:1997hj]: $$Z( \upsilon, \bar{ \upsilon})=\text{Tr}(-1)^F e^{2\pi i  \upsilon J_3^{R}} e^{2\pi i \bar{ \upsilon} J_3^{L}} q^{L_0} \bar{q}^{\bar{L}_0},$$ where $( \upsilon, \bar{ \upsilon})$ are chemical potentials for the left- and right-moving spacetime helicities $(J_3^{R}, J_3^L)$. From the generating function $Z( \upsilon, \bar{ \upsilon})$ one can compute the associated helicity supertraces $B_n$ can then be computed by taking derivatives of the partition function: $$B_n=\left(\frac{1}{2\pi i} \frac{\partial}{\partial \upsilon}+\frac{1}{2\pi i} \frac{\partial}{\partial \bar\upsilon}\right)^n Z(\upsilon,\bar \upsilon)\Big|_{\upsilon=\bar \upsilon=0}\ .$$

The $B_n$'s should then be viewed as generating functions of the BPS-indices $\Omega_n$. For type IIA compactified on K3$\times T^2$, we have $$\label{ZIIA} Z^{\text{IIA}}(\upsilon,\bar \upsilon)=\frac{\vartheta_1(\upsilon/2)^2\bar\vartheta_1(\bar\upsilon/2)^2  }{\eta^2\bar\eta^2}\frac{\xi(\upsilon)\bar\xi(\bar\upsilon)}{\tau_2\eta^2\bar\eta^2}C
(\upsilon/2,\bar\upsilon/2)\frac{\Theta_{\Gamma^{2,2}} }{\eta^2\bar\eta^2}\ ,$$ where we defined $$\xi(\upsilon)=\prod_{n=1}^\infty \frac{(1-q^n)^2}{(1-e^{2\pi i \upsilon} q^n)(1-e^{-2\pi i \upsilon} q^n)}\ ,$$ and $\Theta_{\Gamma^{2,2}}$ is the usual Narain theta function of the lattice.

The contributions to $Z^{\text{IIA}}$ are as follows:

-   $\frac{\xi(\upsilon)\bar\xi(\bar\upsilon)}{\tau_2\eta^2\bar\eta^2}$ comes from the scalar fields along the two uncompactified transverse directions.

-   $C
     (\upsilon/2,\bar\upsilon/2)$ comes from the internal $\mathcal{N}=(4,4)$ SCFT with central charge $(c,\bar c)=(6,6)$ (non-linear sigma model on K3). For $\bar \upsilon=0$, this is just the elliptic genus of K3.

-   $\frac{\Theta_{\Gamma^{2,2}} }{\eta^2\bar\eta^2}$ comes from the oscillators and winding-momenta along $T^2$.

-   $\frac{\vartheta_1(\upsilon/2)^2}{\eta^2}$ and its complex conjugate come from left- and right-moving fermions along the two uncompactified transverse directions and along the torus $T^2$.

Since $\vartheta _1(0)=0$, the only non-vanishing contributions to the fourth helicity trace $B_4$ come from terms where all four derivatives act on the theta functions. Using $$\vartheta_1'(0)=2\pi \eta^3\ ,\qquad \xi(0)=1\ ,\qquad C
(0,0)=24$$we obtain the following expression for the fourth helicity supertrace: $$\begin{split}
 B_4&=\left(\frac{1}{2\pi i} \frac{\partial}{\partial \upsilon}+\frac{1}{2\pi i} \frac{\partial}{\partial \bar\upsilon}\right)^4 Z^{\text{IIA}}(\upsilon,\bar \upsilon)\Big|_{ \upsilon=0}
 \nonumber \\
 &= 6\left(\frac{1}{2\pi i} \frac{\partial}{\partial \upsilon}\right)^2\left(\frac{1}{2\pi i} \frac{\partial}{\partial \bar\upsilon}\right)^2 Z^{\text{IIA}}(\upsilon,\bar \upsilon)\Big|_{ \upsilon=0}
 \nonumber \\
 &=\frac{3}{2} C
 (0,0)\frac{\Theta_{\Gamma^{2,2}} }{\tau_2}
 
 =36\frac{\Theta_{\Gamma^{2,2}} }{\tau_2}\ .
 \end{split}$$
