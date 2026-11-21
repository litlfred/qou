---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-030-7-mass-terms
section_title: "Mass terms"
section_number: 7
pages: 22-22
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 0.821
latex_coverage_ratio: 0.918
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
[]{#sec:mass label="sec:mass"}

We now put the formalism developed to some use. We search for a \"Higgs\" field that can break the ${\rm Spin}(11,3)$ symmetry, and also be used to write mass terms for the semi-spinor $S_+={\mathbb O}\otimes\tilde{{\mathbb O}}$. We thus need a field that lives in the tensor product of the representation $S_+$ with itself. We have the following decomposition of this tensor product $$\begin{aligned}
S_+\times S_+ = \Lambda^1 ({\mathbb R}^{11,3}) \oplus \Lambda^3 ({\mathbb R}^{11,3}) \oplus \Lambda^5 ({\mathbb R}^{11,3}) \oplus \Lambda^7_{sd} ({\mathbb R}^{11,3}).
\end{aligned}$$ Here $\Lambda^k ({\mathbb R}^{11,3})$ is the space of anti--symmetric tensors of rank $k$ in ${\mathbb R}^{11,3}$. The space of 7-forms is not an irreducible representation, but the space $\Lambda^7_{sd}$ of self-dual 7-forms is. The first factor in this sum is anti-symmetric, i.e. projection on it does not vanish only if we assume that the two $S_+$ factors anti-commute. The second term is symmetric. We are interested in the mass terms arising by projecting onto this representation. Thus, we are interested in the symmetric bilinear forms on $S_+$ that can be written as $$\begin{aligned}
C^{\mu\nu\rho} \langle\!\langle\Psi, \Gamma_\mu \Gamma_\nu \Gamma_\rho\Psi \rangle\!\rangle.
\end{aligned}$$

## Projection onto $\Lambda^3 {\mathbb R}^{11,3}$

Three copies of $\Gamma$-matrices can be inserted between two $S_+$ states and produce a ${\mathfrak so}(11,3)$ invariant expression. The different arising components are $$\begin{aligned}
\langle\!\langle\Psi, \Gamma_{x_1 x_2 x_3} \Psi \rangle\!\rangle= \langle\!\langle\Psi, L_{x_1} L_{x_2} L_{x_3} \otimes {\mathbb I}\Psi \rangle\!\rangle, 
\quad
\langle\!\langle\Psi, \Gamma_{y_1 y_2 y_3} \Psi \rangle\!\rangle= - \langle\!\langle\Psi, {\mathbb I}\otimes L_{y_1} L_{y_2} L_{y_3}  \Psi \rangle\!\rangle, 
\\ \nonumber
\langle\!\langle\Psi, \Gamma_{x_1 x_2 y_1} \Psi \rangle\!\rangle= \langle\!\langle\Psi, L_{x_1} L_{x_2}  \otimes  L_{y_1} \Psi \rangle\!\rangle, 
\quad
\langle\!\langle\Psi, \Gamma_{x_1 y_1 y_2} \Psi \rangle\!\rangle= - \langle\!\langle\Psi,   L_{x_1} \otimes L_{y_1} L_{y_2}  \Psi \rangle\!\rangle.
\end{aligned}$$ This means we have the following expression for the projection $S_+\times S_+ \to \Lambda^3 {\mathbb R}^{11,3}$ $$\begin{aligned}
\label{364-rep}
\langle\!\langle\Psi, \Gamma\Gamma\Gamma \Psi \rangle\!\rangle= \langle\!\langle\Psi, E^i E^j E^k \otimes {\mathbb I}\Psi \rangle\!\rangle e^{ijk} + \langle\!\langle\Psi, E^i E^j \otimes  \tilde{E}^k  \Psi \rangle\!\rangle e^{ij} \tilde{e}^k \\ \nonumber
-\langle\!\langle\Psi,   E^i \otimes \tilde{E}^j \tilde{E}^k  \Psi \rangle\!\rangle e^i \tilde{e}^j \tilde{e}^k 
-\langle\!\langle\Psi, {\mathbb I}\otimes \tilde{E}^i \tilde{E}^j \tilde{E}^k   \Psi \rangle\!\rangle\tilde{e}^i \tilde{e}^j \tilde{e}^k.
\end{aligned}$$
