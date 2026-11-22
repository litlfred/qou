---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-010-33-difference-equations
section_title: "Difference equations"
section_number: 3.3
pages: 19-21
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.907
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:tetdiff label="sec:tetdiff"}

A final interesting property of the tetrahedron index is the fact that it obeys two difference equations. In terms of operators $\hat x_{\pm}=\exp(\hat X_\pm)$ and $\hat p_\pm =\exp(\hat P_\pm)$ as defined in Section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"}, these are

$$\big(\hat p_++\hat x_+^{-1}-1\big)\mathcal{I}_\Delta = 0\,,\qquad
  \big(\hat p_-+\hat x_-^{-1}-1\big)\mathcal{I}_\Delta = 0\,.
\label{teteqs}$$

For example, writing these out in the charge basis we find

$$\label{teteqsem}
\begin{align}
 q^{\frac e2}\mathcal{I}_\Delta(m+1,e)+q^{-\frac m2}\mathcal{I}_\Delta(m,e+1)-\mathcal{I}_\Delta(m,e) = 0\,, \\
 q^{\frac e2}\mathcal{I}_\Delta(m-1,e)+q^{-\frac m2}\mathcal{I}_\Delta(m,e-1)-\mathcal{I}_\Delta(m,e) = 0\,,
\end{align}$$

for all $m,e$. These equations are compatible with the $\rho$ symmetry of the index, which interchanges the two $(\pm)$ sets of operators. The validity of [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} can be checked easily by writing the index in a fugacity basis, and using the product formula [\[Iztet2\]](#Iztet2){reference-type="eqref" reference="Iztet2"}. Also, in the semi-classical regime [\[tetasymp\]](#tetasymp){reference-type="eqref" reference="tetasymp"} each of the difference equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} turns into a differential equation, equivalent to the standard property of the dilogarithm function, $z\tfrac{d}{dz} \text{Li}_2 (z) =  \log (1-z^{-1})$.

Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} may look familiar from the study of "quantum Lagrangians" and $S^3_b$ partition functions in [@DG-Sdual; @DGG]. As anticipated in Section [\[sec:ops\]](#sec:ops){reference-type="ref" reference="sec:ops"}, these are the *same* difference equations obeyed by the $S^3_b$ partition function of $T_\Delta$, with an appropriate identification of the operators $\hat x_\pm,\,\hat p_\pm$. We will try to explain the reason behind this in Section [\[sec:3d4d\]](#sec:3d4d){reference-type="ref" reference="sec:3d4d"}. In essence, the same universal algebra of line operators is acting on both the index and the $S^3_b$ partition functions; Ward identities for the line operators then lead to [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"}.

::: wrapfigure
r2in ![image](tet){width="1.8in"}
:::

In terms of the tetrahedron $\Delta$ itself, Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} are two copies of the quantized Lagrangian $\hat \mathcal{L}_\Delta$ that describes which flat $SL(2,{\mathbb C})$ connections on the boundary $\partial\Delta$ can be extended as flat connections in the interior of $\Delta$. To see this, recall

[^1]

from [@Dimofte-QRS; @DGG] that the set of flat connections on $\partial\Delta$, *a.k.a.* the phase space $\mathcal{P}_{\partial\Delta}$, is described by three ${\mathbb C}^*$--valued edge coordinates $z,z',z''$, subject to the condition that $zz'z''=-1$. Upon quantization, these coordinates form an algebra of operators with $q$-commutation relations

$$\hat z\hat z'=q \hat z'\hat z\,,\qquad \hat z'\hat z''=q\hat z''\hat z'\,,\qquad \hat z''\hat z=q\hat z\hat z''\,,$$

and a central constraint

$$\hat z''\hat z'\hat z= -1\,. \label{zconst}$$

(For logarithms of the $\hat z$'s, written in uppercase letters, the constraint reads $\hat Z+\hat Z'+\hat Z''=i\pi+\hbar/2$.) Similarly, the classical Lagrangian $\mathcal{L}_\Delta = \{z''+z^{-1}-1=0\}$, describing flat connections in the interior of $\Delta$, becomes promoted to a quantum operator (*cf.* [@gukov-2003])

$$\hat\mathcal{L}_\Delta = \hat z''-\hat z^{-1}-1\,, \label{tetLag}$$

which must annihilate any putative wavefunction of the tetrahedron, in any representation. It should then be clear that Equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"} are just two copies of [\[tetLag\]](#tetLag){reference-type="eqref" reference="tetLag"}, with opposite quantization parameters $\hbar$ and $-\hbar$. Indeed, using the classical complex variables $z=q^{\frac m2}\zeta,\, \overline z=q^{\frac m2}\zeta^{-1}$, or logarithmically $Z = \tfrac m2\hbar+i\theta,\,\overline Z=\tfrac m2\hbar-i\theta$ (*cf.* [\[XPz\]](#XPz){reference-type="eqref" reference="XPz"}), we find that we can identify $(\hat P_+,\hat X_+) = (\hbar \partial_Z,Z)$ and $(\hat P_-,\hat X_-)=(-\hbar \partial_{\overline Z},\overline Z)$.

The Lagrangian [\[tetLag\]](#tetLag){reference-type="eqref" reference="tetLag"} is invariant under cyclic permutations $\hat z\to \hat z'\to\hat z''\to \hat z$ in the operator algebra for the tetrahedron. That is, the equation $\hat \mathcal{L}_\Delta\,\psi=0$ for any putative wavefunction $\psi$ can be written using any pair of consecutive variables $(\hat z'',\hat z)$, $(\hat z,\hat z')$, or $(\hat z',\hat z'')$, thanks to the constraint [\[zconst\]](#zconst){reference-type="eqref" reference="zconst"}. Moreover, the generator of the ${\mathbb Z}_3$ cyclic symmetry is none other than our familiar affine $Sp(2,{\mathbb Z})$ element $\sigma_eST$, *cf.* [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}, acting on logarithms of the $\hat z$ operators. For example, if we identify $(\hat P_+,\hat X_+) = (\hat Z'',\hat Z)$ and $(\hat P_+',\hat X_+')=(\hat Z,\hat Z')$, then

$$\label{XPST}
\begin{pmatrix} \hat X_+' \\ \hat P_+ '\end{pmatrix}
 = \sigma_eST \begin{pmatrix} \hat X_+ \\ \hat P_+ \end{pmatrix}
 = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} \hat X_+ \\ \hat P_+ \end{pmatrix}+\begin{pmatrix} i\pi+\tfrac\hbar2 \\ 0 \end{pmatrix}\,.$$

Together with the intertwining property [\[intertwine\]](#intertwine){reference-type="eqref" reference="intertwine"} for the index, the cyclic symmetry of the quantized Lagrangian guarantees that $\mathcal{I}_\Delta$, $\mathcal{I}_{\sigma_eST\circ \Delta}$, and $\mathcal{I}_{(\sigma_eST)^2\circ\Delta}$ all satisfy the *same* equations [\[teteqs\]](#teteqs){reference-type="eqref" reference="teteqs"}. This constitutes the basis for a proof that $\mathcal{I}_\Delta = \mathcal{I}_{\sigma_eST\circ \Delta} = \mathcal{I}_{(\sigma_eST)^2\circ\Delta}$, as in [\[tetST\]](#tetST){reference-type="eqref" reference="tetST"}, since the solutions to the difference equations are unique given appropriate boundary conditions. Details appear in Appendix [\[app:ST\]](#app:ST){reference-type="ref" reference="app:ST"}.

[^1]: Throughout this paper, we will be quite brief with details of flat connections and 3d geometry. We direct the reader to the summary of triangulations in Section 2 of [@DGG] and references therein (especially the classic [@Thurston-1980; @NZ]) for some potentially useful background.
