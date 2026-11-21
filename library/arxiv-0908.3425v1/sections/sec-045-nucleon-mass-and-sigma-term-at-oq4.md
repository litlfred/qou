---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-045-nucleon-mass-and-sigma-term-at-oq4
section_title: "Nucleon mass and sigma term at O(q4)"
section_number: null
pages: 66-67
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.863
latex_coverage_ratio: 0.992
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
A full one-loop calculation of the nucleon mass also includes ${\cal O}(q^4)$ terms (see Fig. [1](#5:1:1:SEDiagrams){reference-type="ref" reference="5:1:1:SEDiagrams"}).

<figure id="5:1:1:SEDiagrams">
<div class="center">

</div>
<figcaption><span id="5:1:1:SEDiagrams" label="5:1:1:SEDiagrams"></span> Contributions to the nucleon self energy at <span class="math inline">${\cal O}(q^4)$</span>. The number <span class="math inline"><em>n</em></span> in the interaction blobs refers to <span class="math inline">${\cal L}_{\pi N}^{(n)}$</span>. The Lagrangian <span class="math inline">${\cal L}_{\pi N}^{(2)}$</span> does not produce a contribution to the <span class="math inline"><em>π</em><em>N</em><em>N</em></span> vertex.</figcaption>
</figure>

The quark-mass expansion up to and including ${\cal O}(q^4)$ is given by $$\label{mnoq4}
m_N=m+k_1 M^2+k_2 M^3+k_3 M^4\ln\left(\frac{M}{m}\right)+k_4 M^4
+{\cal O}(M^5),$$ where the coefficients $k_i$ in the EOMS scheme read [@Fuchs:2003qc] $$\begin{aligned}
\label{parki}
k_1&=&-4 c_1,\quad
k_2=-\frac{3 {\texttt{g}_A}^2}{32\pi F^2},\quad
k_3=-\frac{3}{32\pi^2 F^2 m}\left(\texttt{g}_A^2-8c_1m+c_2m+4 c_3m\right),
\nonumber\\
k_4&=&\frac{3 {\texttt{g}_A}^2}{32 \pi^2 F^2 m}(1+4 c_1 m)
+\frac{3}{128\pi^2F^2}c_2-\hat{e}_1.
\end{aligned}$$ Here, $\hat{e}_1= 16 e_{38}+2e_{115}+2e_{116}$ is a linear combination of ${\cal O}(q^4)$ coefficients [@Fettes:2000gb]. A comparison with the results using the infrared regularization [@Becher:1999he] shows that the lowest-order correction ($k_1$ term) and those terms which are non-analytic in the quark mass $\hat{m}$ ($k_2$ and $k_3$ terms) coincide. On the other hand, the analytic $k_4$ term ($\sim M^4$) is different. This is not surprising; although both renormalization schemes satisfy the power counting specified in Sec. [\[subsection_pcrd\]](#subsection_pcrd){reference-type="ref" reference="subsection_pcrd"}, the use of different renormalization conditions is compensated by different values of the renormalized parameters.

For an estimate of the various contributions of Eq. ([\[mnoq4\]](#mnoq4){reference-type="ref" reference="mnoq4"}) to the nucleon mass, we make use of the parameter set $$\label{parametersci}
c_1=-0.9\,m_N^{-1},\quad
c_2=2.5\, m_N^{-1},\quad
c_3=-4.2\, m_N^{-1},\quad
c_4=2.3\, m_N^{-1},$$ which was obtained in Ref. [@Becher:2001hv] from a (tree-level) fit to the $\pi N$ scattering threshold parameters. Using the numerical values $$\label{numericalvalues}
g_A=1.267,\quad F_\pi=92.4\,\mbox{MeV},\quad
m_N=m_p=938.3\,\mbox{MeV},\quad M_\pi=M_{\pi^+}=139.6\,\mbox{MeV},$$ one obtains for the mass of nucleon in the chiral limit (at fixed $m_s\neq 0$): $$m=m_N-\Delta m
=[938.3-74.8+15.3+4.7+1.6-2.3\pm 4]\,\mbox{MeV}
=(883\pm 4)\, \mbox{MeV}$$ with $\Delta m=(55.5\pm 4)\,\mbox{MeV}$. Here, we have made use of an estimate for $\hat{e}_1M^4=(2.3\pm 4)$ MeV obtained from the $\sigma$ term. (Note that errors due to higher-order corrections are not taken into account.) In terms of the SU(2)$_L\times$SU(2)$_R$-chiral-symmetry-breaking mass term of the QCD Hamiltonian, $${\cal H_{\rm sb}}=\hat{m}(\bar u u+\bar d d),$$ the pion-nucleon $\sigma$ term is defined as the proton matrix element $$\sigma=\frac{1}{2m_p}\langle p(p,s)|{\cal H_{\rm sb}}(0)|p(p,s)\rangle$$ at zero momentum transfer. The $\sigma$ term provides a sensitive measure of explicit chiral symmetry breaking in QCD, because it is a correction to a null result in the chiral limit rather than a small correction to a non-trivial result [@Pagels:1974se]. The quark-mass expansion of the $\sigma$ term reads $$\sigma=\sigma_1 M^2+\sigma_2 M^3 +\sigma_3 M^4 \ln\left(\frac{M}{m}\right)
+\sigma_4 M^4+{\cal O}(M^5),$$ with $$\begin{aligned}
\label{parsigmai}
\sigma_1&=&-4 c_1,\quad
\sigma_2=-\frac{9{\texttt{g}_{A}}^2}{64\pi F^2},\quad
\sigma_3=-\frac{3}{16\pi^2 F^2 m}\left(\texttt{g}_A^2-8c_1m+c_2m+4 c_3m\right),
\nonumber\\
\sigma_4&=&\frac{3}{8\pi^2 F^2m}\left[\frac{3 {\texttt{g}_{A}}^2}{8}
+c_1m(1+2 {\texttt{g}_A}^2)-\frac{c_3m}{2}\right]-2\hat{e}_1.
\end{aligned}$$ We obtain \[with $\hat{e}_1=0$ in Eq. ([\[parsigmai\]](#parsigmai){reference-type="ref" reference="parsigmai"})\] $$\label{sigmanum}
\sigma=(74.8-22.9-9.4-2.0)\,\mbox{MeV}=40.5\, \mbox{MeV}.$$ The result of Eq. ([\[sigmanum\]](#sigmanum){reference-type="ref" reference="sigmanum"}) has to be compared with, e.g., the dispersive analysis $\sigma=(45\pm 8)$ MeV of Ref. [@Gasser:1990ce] which would imply, neglecting higher-order terms, $-2\hat{e}_1 M^4 \approx (4.5\pm 8)$ MeV. As has been discussed, e.g., in Ref. [@Becher:1999he], a fully consistent description would also require to determine the low-energy coupling constant $c_1$ from a complete ${\cal O}(q^4)$ calculation of, say, $\pi N$ scattering. The results of Eqs. ([\[parki\]](#parki){reference-type="ref" reference="parki"}) and ([\[parsigmai\]](#parsigmai){reference-type="ref" reference="parsigmai"}) satisfy the constraints as implied by the application of the Hellmann-Feynman theorem to the nucleon mass [@Gasser:1987rb], $$\sigma =M^2 \ {\partial m_N\over \partial M^2}.
\label{fhrelation}$$
