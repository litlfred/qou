---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-008-31-parity-and-symmetry
section_title: "Parity and symmetry"
section_number: 3.1
pages: 17-18
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:tetkappa label="sec:tetkappa"}

Several identities satisfied by the tetrahedron index can be understood via discrete symmetries acting on $T_\Delta$. Let's first consider the action of parity $\mathbf{P}$ on $T_\Delta$. In is not an exact symmetry because it inverts the sign of the Chern-Simons level, from $k=-\tfrac12$ to $k=\tfrac12$. However, this can be compensated for by subtracting a Chern-Simons term, *i.e.* applying $T^{-1}\in Sp(2,{\mathbb Z})$. In the $S^2\times S^1$ background, it actually turns out that the R-charge and fermion number of the vacuum must also be shifted, so that altogether we get

$$\label{PonT}
T_\Delta\;\simeq\; \sigma_m^R\sigma_m^F T^{-1}\circ \mathbf{P}\,T_\Delta\,.$$

Acting on the index, $\mathbf P$ simply sends $m\to -m$, so [\[PonT\]](#PonT){reference-type="eqref" reference="PonT"} implies

$$\mathcal{I}_\Delta(m,e;q) = \big(-q^{\frac12}\big)^m\mathcal{I}_\Delta(-m,e+m;q)\,.
\label{tetPem}$$

This identity can be checked explicitly (see Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}), most easily after converting to the fugacity basis.

The $\rho$ symmetry of Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"} is more universal than parity, but also more subtle to implement. Naively, it sends $\mathcal{I}_\Delta(m;q,\zeta)$ to $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$; but the latter does not make sense for $|q|<1$. In order to properly apply the symmetry, we need to reorganize the Hilbert space $\mathcal{H}_{-m}$, and to reinterpret $\mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1})$ as a series in $q$. For the tetrahedron, this is actually straightforward.

Let us set $z=q^{\frac m2}\zeta$, $\overline z=q^{\frac m2}\zeta^{-1}$, noting that $\rho$ acts on $z$ by complex conjugation. Then

$$\begin{aligned}
 \mathcal{I}_\Delta(-m;q^{-1},\zeta^{-1}) &\,=\, \prod_{r=0}^\infty \frac{1-q^{-r-1}\,\overline z^{-1}}{1-q^{-r} z^{-1}}  \,=\, \exp\left(\, \sum_{n=1}^\infty \frac{-q^{-n}\overline z^{-n}+z^{-n}}{n(1-q^{-n})} \right) \notag \\
 &\simeq\; \exp\left(\, \sum_{n=1}^\infty \frac{-q^n z^{-n}+z^{-n}}{n(1-q^n)}  \right)\label{tetreorg} \\
 &\,=\, \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r \,\overline z^{-1}} = \mathcal{I}_\Delta(m;q,\zeta)\,. \notag
\end{aligned}$$

The necessary reorganization of cancellations happened in the middle step [\[tetreorg\]](#tetreorg){reference-type="eqref" reference="tetreorg"}, and established the $\rho$ symmetry. Note that this is *not* analytic continuation, since neither of the exponentials here make sense on the unit circle $|q|=1$ --- the expressions diverge at every root of unity.
