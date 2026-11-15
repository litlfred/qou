---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-009-32-triality
section_title: "Triality"
section_number: 3.2
pages: 18-19
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.767
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:tri label="sec:tri"}

Experimentally, we observe that the tetrahedron index enjoys yet another more interesting discrete symmetry of order three:

$$\mathcal{I}_\Delta(m,e;q) = \big(-q^{\frac12}\big)^{-e}\mathcal{I}_\Delta(e,-e-m;q)=\big(-q^{\frac12}\big)^{m}\mathcal{I}_\Delta(-e-m,m;q)\,. \label{tettri}$$

For a visual demonstration of this symmetry, let us define ${\rm lead}(m,e)$ to be the leading power of $q$ that appears in $\mathcal{I}_\Delta(m,e;q)$ when written as a series in $q$. For example,

$$\begin{array}{ll}
 \mathcal{I}_\Delta(0,0;q) = 1-q-2q^2-2q^3-2q^4+q^6+5q^7+...\qquad &\Rightarrow\quad {\rm lead}(0,0)=0\,, \\[.1cm]
 \mathcal{I}_\Delta(1,0;q) = -q-q^2+q^4+3q^5+4q^6+6q^7+6q^8+...\qquad &\Rightarrow \quad {\rm lead}(1,0)=1\,, \\[.1cm]
 \mathcal{I}_\Delta(1,2;q) = -q^2-q^3-q^4-q^5+q^7+3q^8+5q^9+... \qquad &\Rightarrow\quad {\rm lead}(1,2) = 2\,,
\end{array}$$

*etc.* It can be shown from [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"} that ${\rm lead}(m,e)\geq 0$ for all $m,e$. A graph of ${\rm lead}(m,e)$ appears in Figure [1](#fig:lead){reference-type="ref" reference="fig:lead"}, which clearly hints at a ${\mathbb Z}_3$ "rotation" symmetry in the index as in [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"}. We will describe a method of proving [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} in Section [\[sec:tetdiff\]](#sec:tetdiff){reference-type="ref" reference="sec:tetdiff"}, using difference equations for the index.

![Leading powers of $q$ in the index. The graph interpolates smoothly between integer points.](lead){#fig:lead width="3.8in"}

In order to acquire further intuition for the triality symmetry of $\mathcal{I}_\Delta$, it is instructive to observe that [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} can be written as

$$\mathcal{I}_\Delta(m,e;q) = \mathcal{I}_{\sigma_eST\circ \Delta}(m,e;q)=\mathcal{I}_{(\sigma_eST)^2\circ\Delta}(m,e;q)\,, \label{tetST}$$

where $ST\in Sp(2,{\mathbb Z})$ and $\sigma_e \equiv \sigma_e^R\sigma_e^F$ are affine symplectic transformations of the tetrahedron theory, as described in Section [\[sec:actions\]](#sec:actions){reference-type="ref" reference="sec:actions"}. The transformation $\sigma_eST$ has order three. Then we recall from [@DGG] that the tetrahedron SCFT $T_\Delta$ is invariant

[^1]

under the cyclic action of $\sigma_eST$, due to 3d $\mathcal{N}=2$ mirror symmetry [@IS; @AHISS; @dBHOY; @dBHO]. In other words, the following UV theories flow to the same IR fixed point:

$$\begin{array}{r@{\quad}l}
T_\Delta\,: & \text{free chiral with global $U(1)$ symmetry at CS level $-\tfrac12$}\\[.2cm]
\sigma_eST\circ T_\Delta\,: & \text{gauged $U(1)$ theory at CS level $+\tfrac12$, coupled to a single chiral}\,.
\end{array}$$

Since these theories are mirror symmetric their indices must be the same, and that is precisely what we see in [\[tettri\]](#tettri){reference-type="eqref" reference="tettri"} and [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}.

[^1]: The decoration of the symplectic transformation $ST$ by an R-charge and fermion number shift $\sigma_e=\sigma^R_e\sigma^F_e$ is correlated with the precise definition of the tetrahedron theory in the twisted $S^2\times S^1$ geometry, as discussed above [\[Iztet\]](#Iztet){reference-type="eqref" reference="Iztet"}. Had we chosen different $R$ and $F$ assignments for $T_\Delta$, the affine shift would look slightly different.
