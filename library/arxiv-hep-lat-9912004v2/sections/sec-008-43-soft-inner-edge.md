---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "arXiv:hep-lat/9912004v2 9 Mar 2000"
section_id: sec-008-43-soft-inner-edge
section_title: "Soft inner edge"
section_number: 4.3
pages: 7-8
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-lat/9912004v2 9 Mar 2000 — 11 sections: Front matter; Chiral Random Matrix Theory; Introduction"
---
We now turn to the results for $T>T_c$. In our results for $24^3\times 12$ at $\beta=5.85$ (Fig. [\[all-dist\]](#all-dist){reference-type="ref" reference="all-dist"}(c)) a gap in the spectral distributions is obvious. However even at $\beta=5.8$ we may speculate, that a clear signal of a gap is only prevented by the (topological) quasi-zero modes responsible for the small bump at small eigenvalues.

Recall, that chRMT[@JaVe96] predicts the presence of a gap in the spectral density $\rho(\lambda)$ of the Dirac operator centered around $\lambda=0$. Furthermore, the inner edge of this gap is predicted to show a singularity, at a point $A$, in the macroscopic spectral density [@KaFr98] $$\rho(\lambda,u)=K\left(\frac{\lambda^2}{A^2}-1\right)^{u+1/2} \ ,
\ \ u=0,2,4,...  \  \ ,  
\label{AiSingularity}$$ where $K$ is a known constant. The constant $u$ takes the value $u=0$ in the generic chRMT, i. e. without fine-tuning the matrix potential in ([\[Z\]](#Z){reference-type="ref" reference="Z"}) (which would be necessary in order to obtain higher values of $u$). This corresponds to a square-root-like eigenvalue density near $A$.

One concern here is to measure $u$. With the limited amount of data available it is not possible to do this based on the spectral density only. Instead we propose to study the average distance between the smallest and the sequel eigenvalues $\langle q_{i-\frac{1}{2}}\rangle
\equiv\langle\lambda_{i+1}-\lambda_1\rangle$; the extraction of $u$ is carried out by noting the following scaling relation in the index $i$, ordering by size the eigenvalues which follow the smallest, $$\langle q_{i-\frac{1}{2}}\rangle\propto \left(i-\frac{1}{2}\right)^\frac{1}{u+3/2} \ .
\label{qi}$$ This proportionality follows by integration in ([\[AiSingularity\]](#AiSingularity){reference-type="ref" reference="AiSingularity"}).

In Fig. [1](#AND){reference-type="ref" reference="AND"} we display the seven average distances, $\langle
q_i\rangle$, from the ensemble of 146 configurations on a $24^3\times12$ lattice for $\beta_g=5.85$. We also exhibit the best fit to ([\[qi\]](#qi){reference-type="ref" reference="qi"}) with respect to $u$, giving $u=0.117(71)$. Also shown are the corresponding curves for $u=0$ and $u=2$. The value $u=0$ is clearly favored.

<figure id="AND">

<figcaption>The behavior of the average distance from the smallest eigenvalue to the <span class="math inline"><em>i</em></span>’th eigenvalue for the <span class="math inline">24<sup>3</sup> × 12</span> ensemble at <span class="math inline"><em>β</em> = 5.85</span>.</figcaption>
</figure>

Since the two-point correlations behave as expected from RMT, we now turn to the one-point distribution. The microscopic behavior of the spectral density in the vicinity of this singularity is universal in the chRMTsense, but depends on the value of $u$ [@KaFr98]. For $u=0$ the exact analytical prediction for the microscopic spectral density in the vicinity of the inner edge is [@Fo93] $$\rho_{\rm Ai}(z,0)=({\rm Ai}'(z))^2-z\,({\rm Ai}(z))^2 \ .  
\label{AiDens}$$ Here the origin has been moved to the inner spectral endpoint $A$ by means of the rescaled eigenvalue $z$, which is defined through $$\lambda=A\left[1+\frac{z}{2}\left(\frac{2}{\pi AK}\right)^\frac{1}{u+\frac{3}{2}}\right] \ .$$

The consistency with the prediction ([\[qi\]](#qi){reference-type="ref" reference="qi"}) for $u=0$ and the approximate validity of chRMTcorrelations in the level spacing statistics above $T_c$ suggest that the Airy-density ([\[AiDens\]](#AiDens){reference-type="ref" reference="AiDens"}) corresponding to the value $u=0$ should fit the spectral density. If it does, then we can extract the inner-endpoint $A$ of the spectrum in the thermodynamic limit, by fitting $\rho_{\rm Ai}(z,0)$ with respect to $A$ to the lowest part of the spectral density, see Fig. [2](#AiryFig){reference-type="ref" reference="AiryFig"}.

<figure id="AiryFig">

<figcaption>The <span class="math inline"><em>u</em> = 0</span> Airy density with endpoint <span class="math inline"><em>λ</em> = <em>A</em> = 0.0205</span>. Approximately the domain of the first three eigenvalues is shown.</figcaption>
</figure>

This fit does not convincingly confirm Airy density. However, the statistical fluctuations at this $\beta$-value affect the *one-point distribution* substantially and prevent a decisive comparison.
