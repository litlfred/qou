---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-013-42-the-bipyramid
section_title: "The bipyramid"
section_number: 4.2
pages: 25-28
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:bip label="sec:bip"}

As a simple but crucial example of a nontrivial 3-manifold, let us take $M$ to be the bipyramid, shown in the center of Figure [1](#fig:bip){reference-type="ref" reference="fig:bip"}. The bipyramid can be decomposed into either 2 or 3 tetrahedra, leading to two different UV descriptions of the theory $T_M$. It was shown in [@DGG] that, with an appropriate polarization, the gluing of two tetrahedra produces $N_f=1$ SQED, while the gluing of three tetrahedra produces the so-called XYZ model, a theory of three chiral multiplets coupled by a cubic superpotential. The fact that these theories are mirror symmetric [@AHISS] formed the basis of the argument that the construction of $T_M$ for general 3-manifolds is triangulation independent (see also [@CCV]).

![The bipyramid, in its two triangulations. The equatorial polarization $\Pi = (X_1,X_2;P_1,P_2)$ has positions $X_1$ and $X_2$ corresponding to the two equatorial edges in the front.](bip){#fig:bip width="5.3in"}

Here we calculate the index $\mathcal{I}_M$ for the bipyramid. The boundary phase space $\mathcal{P}_{\partial M}$ is four-dimensional, with two position coordinates corresponding to the $U(1)^2$ flavor symmetry of either $N_f=1$ SQED or the XYZ model. Let us choose an equatorial polarization for $\mathcal{P}_{\partial M}$, with position coordinates $x_{1,2}=\exp(X_{1,2})$ and momentum coordinates $p_{1,2}=\exp(P_{1,2})$ associated to the external edges shown in Figure [1](#fig:bip){reference-type="ref" reference="fig:bip"}.

For the decomposition into two tetrahedra $\Delta_R$ and $\Delta_S$, we first form the product index $\mathcal{I}_{\{\Delta_R,\Delta_S\},\{\Pi_R,\Pi_S\}}(m_R,m_S,e_R,e_S) = \mathcal{I}_\Delta(m_R,e_R)\,\mathcal{I}_\Delta(m_S,e_S)$. (We continue to suppress the dependence of indices on the parameter $q$.) Then observe that

$$\begin{pmatrix} X_1\\ X_2\\ P_1\\ P_2 \end{pmatrix}
 = \begin{pmatrix} R+S'' \\ R''+S \\ R'' \\ S'' \end{pmatrix}
 = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
 \begin{pmatrix} R \\ S\\ R'' \\ S'' \end{pmatrix}\,.
\label{pol2}$$

Therefore, $\Pi = \widetilde\Pi = g_{Sp}\cdot (\Pi_R\times\Pi_S)$, where $g_{Sp}$ is the symplectic matrix on the right side of [\[pol2\]](#pol2){reference-type="eqref" reference="pol2"}. There is no affine shift. Correspondingly, the index transforms as

$$\begin{aligned}
 \mathcal{I}_{M,\Pi}(m_1,m_2,e_1,e_2) &=
 \big(-q^{\frac12}\big)^{\langle 0,(m,e)\rangle}\mathcal{I}_{\{\Delta_R,\Delta_S\},\{\Pi_R,\Pi_S\}}\big(g_{Sp}^{-1}(m_1,m_2,e_1,e_2)\big) \notag \\
  &= \mathcal{I}_\Delta(m_1-e_2,e_1)\,\mathcal{I}_\Delta(m_2-e_1,e_2)\,.
 \label{ind2}
\end{aligned}$$

Since there are no internal edges, this is automatically the index of the bipyramid theory.

Physically, [\[ind2\]](#ind2){reference-type="eqref" reference="ind2"} counts states in $N_f=1$ SQED on $S^2\times S^1$. To be very explicit, this theory starts out with a flat-space Lagrangian

[^1]

$$\begin{aligned}
 &\mathcal{L}_{M,\Pi} = \frac{1}{4\pi}\int d^4\theta\big( \Sigma_1\,V_2+(\Sigma_1+2 V_2)V\big) +\int d^4\theta \big(\phi_R^\dagger e^{V+\frac12 V_1}\phi_R + \phi_{S''}^\dagger e^{-V+\frac12 V_1}\phi_{S''}\big)\,,
\end{aligned}$$

where $V$ is dynamical, $V_1$ is a background vector multiplet for the axial $U(1)$ symmetry, and $V_2$ is a background vector multiplet for a slightly modified topological $U(1)$ symmetry. Some additional background Chern-Simons couplings are turned on, and one can also work out the appropriate R-charges and fermions numbers chosen for putting the theory on $S^2\times S^1$ (corresponding to our equatorial polarization $\Pi$). Then

$$\mathcal{I}_{M,\Pi}(m_1,m_2;q,\zeta_1,\zeta_2) = {\rm Tr \,}_{\mathcal{H}_{m_1,m_2}} (-1)^F q^{\frac{R}2+j_3}\zeta_1^{e_1}\zeta_2^{e_2} = \sum_{e_1,e_2\in {\mathbb Z}} \mathcal{I}_{M,\Pi}(m_1,m_2,e_1,e_2;q)\zeta_1^{e_1}\zeta_2^{e_2}\,,$$

where $e_1$ and $e_2$ count axial and topological charges, and $m_1$ and $m_2$ specify the amount of axial and topological flux, respectively, through $S^2$.

For the triangulation into three tetrahedra $\Delta_Z,\Delta_W,\Delta_Y$, we again start with a product index $\mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}(m,e) = \mathcal{I}_\Delta(m_Z,e_Z)\,\mathcal{I}_\Delta(m_W,e_W)\,\mathcal{I}_\Delta(m_Y,e_Y)$. Now, however, the product phase space $\mathcal{P}_{\partial\Delta_Z}\times \mathcal{P}_{\partial\Delta_W}\times \mathcal{P}_{\Delta_Y}$ is six-dimensional, and there is an internal edge. We choose an intermediate polarization $\widetilde\Pi = (X_1,X_2,C;P_1,P_2,\Gamma)$ on the product phase space that is compatible with $\Pi$ and also includes $C = Z+W+Y$, the internal edge parameter, as a position coordinate. Here $\Gamma = -Y'$ (say) is a conjugate momentum to $C$ that commutes with the external edges. Then

$$\begin{pmatrix} X_1\\X_2\\ C\\P_1\\P_2\\\Gamma \end{pmatrix}
= \begin{pmatrix} Z \\ W \\ Z+W+Y \\ Z''+Y' \\ W''+Y' \\ -Y' \end{pmatrix}=
\begin{pmatrix} 1 &0&0&0&0&0 \\ 0&1&0&0&0&0 \\1&1&1&0&0&0 \\ 0&0&-1&1&0&-1 \\ 0&0&-1&0&1&-1 \\ 0&0&1&0&0&1\end{pmatrix}
\begin{pmatrix} Z\\W\\Y\\Z''\\W''\\Y''\end{pmatrix} +
\begin{pmatrix} 0\\0\\0\\i\pi+\tfrac\hbar2\\i\pi+\tfrac\hbar2\\-i\pi-\tfrac\hbar2 \end{pmatrix}\,,
\label{pol3}$$ so the affine symplectic transformation from $\{\Pi_i\}$ to $\widetilde\Pi$ is $\sigma(\alpha)\,g_{Sp}$ with $g_{Sp}$ the matrix appearing in [\[pol3\]](#pol3){reference-type="eqref" reference="pol3"} and a shift vector $\alpha = (0,0,0,1,1,-1)$. Correspondingly,

$$\begin{aligned}
 \mathcal{I}_{\{\Delta_i\},\tilde\Pi}(m,e) &= \big(-q^{\frac12}\big)^{\langle \alpha,(m,e)\rangle}\mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}\big(g_{Sp}^{-1}(m,e)\big) \notag \\
 &\hspace{-.8in}= \big(-q^{\frac12}\big)^{m_1+m_2-m_3}\mathcal{I}_\Delta(m_1,e_1+e_3)\mathcal{I}_\Delta(m_2,e_2+e_3)\mathcal{I}_\Delta(m_3-m_1-m_2,e_3+m_1+m_2-m_3)\,. \notag
\end{aligned}$$

Finally, to obtain the index of the bipyramid theory, we sum over the electric charge $e_3$ corresponding to the internal edge, and set $m_3=0$ :

$$\begin{aligned}
 \mathcal{I}_{M,\Pi}(m,e) &= \sum_{e_3\in {\mathbb Z}} \big(-q^{\frac12}\big)^{2e_3+m_1+m_2}\mathcal{I}_\Delta(m_1,e_1+e_3)\,\mathcal{I}_\Delta(m_2,e_2+e_3)\,\mathcal{I}_\Delta(-m_1-m_2,e_3+m_1+m_2) \notag \\
&= \sum_{e_3\in {\mathbb Z}} q^{e_3}\,\mathcal{I}_\Delta(m_1,e_1+e_3)\,\mathcal{I}_\Delta(m_2,e_2+e_3)\,\mathcal{I}_\Delta(m_1+m_2,e_3)
\label{ind3}
\end{aligned}$$

(the last simplification follows by parity symmetry [\[tetPem\]](#tetPem){reference-type="eqref" reference="tetPem"}). It is not too hard to see that [\[ind3\]](#ind3){reference-type="eqref" reference="ind3"} is a reasonable index for the XYZ model, with the cubic superpotential breaking a diagonal $U(1)$ flavor symmetry and leading to a sum over its charge sectors.

The equivalence of [\[ind2\]](#ind2){reference-type="eqref" reference="ind2"} and [\[ind3\]](#ind3){reference-type="eqref" reference="ind3"} can be proven using difference equations, much in the same way that we demonstrate $\sigma_eST$--invariance of the tetrahedron index in Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}. Of course, these two expressions must be equal on physical grounds, because they are indices for mirror symmetric theories. Computationally, it is very easy to check equivalence at any fixed charge $\gamma=(m,e)$, order by order in $q$. For example, both expressions give

$$\begin{aligned}
 \mathcal{I}_{M,\Pi}(0,0,0,0) &= 1-2q-3q^2+4q^4+12q^5+14q^6+6q^8+\ldots\,, \\
\mathcal{I}_{M,\Pi}(1,3,2,4) &= -q^6-2q^7-4q^8-6q^9-8q^{10}-9q^{11}-8q^{12}+\ldots\,,
\end{aligned}$$

*etc.* Only a finite number of terms in the sum [\[ind3\]](#ind3){reference-type="eqref" reference="ind3"} is needed at any given order. In [@KSV-index; @KW-index] the match was also proven at special values of $m=(m_1,m_2)$ using different methods.

The equivalence of [\[ind2\]](#ind2){reference-type="eqref" reference="ind2"} and [\[ind3\]](#ind3){reference-type="eqref" reference="ind3"} and the $\sigma_eST$-invariance of $\mathcal{I}_\Delta$ are the basic nontrivial ingredients in a combinatorial argument that $\mathcal{I}_{M,\Pi}$ is a topological invariant of $(M,\Pi)$ --- independent of triangulation or any other choices. Again, this must be the case physically as long as $T_M$ is well defined, but it us useful to have a more bottom-up understanding. The $\sigma_eST$-invariance shows that it does not matter how one labels edge parameters of individual tetrahedra in a triangulation, as long as their cyclic ordering (induced by the orientation of $M$) is preserved. The 2-3 invariance of the bipyramid index is then enough to show that the index of any triangulated 3-manifold is independent of triangulation. In particular, the 2-3 invariance must work for any boundary polarization of the bipyramid (it is trivial to show this), and seems to commute with the operation of gluing the bipyramid into a larger 3-manifold --- as long as the larger triangulation has no univalent edges.

[^2]

Then, conjecturally, the set of triangulations of $M$ with no univalent edges is fully connected by 2--3 moves, and triangulation invariance follows.

It would be useful to have a more rigorous understanding of convergence, its relation to combinatorics of triangulations, and how 2--3 moves act to connect restricted sets of triangulations --- such as those without univalent edges. Mathematically, this is still uncharted territory.

[^1]: This particular Lagrangian is found after doing an $\sigma_eST$ rotation (a mirror symmetry) of the $\Delta_S$ tetrahedron; see Section 4.2 of [@DGG].

[^2]: *Cf.* the end of Section [\[sec:rules\]](#sec:rules){reference-type="ref" reference="sec:rules"}. The potential issue here is that the sums [\[indsum\]](#indsum){reference-type="eqref" reference="indsum"} in the definition of the index may not converge uniformly --- so that order of summations can be interchanged. From all tested examples, it appears that avoiding univalent edges is sufficient for convergence. Otherwise, we should only use refined, "easy" triangulations. It is highly plausible that the set of "easy" triangulations is fully connected by 2--3 moves, but it is not yet known rigorously.
