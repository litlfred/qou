---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-021-6-from-ptolemy-coordinates-to-shapes
section_title: "From Ptolemy coordinates to shapes"
section_number: 6
pages: 17-18
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.922
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:PtolemyToShapes}

We now define a monomial map $\mu$ from Ptolemy assignments to shape assignments.
Given a Ptolemy assignment $c$ on a simplex $\Delta^3_n$, define $z\colon\Delta^3_{n-2}(\Z)\times\dot\Delta_2^3(\Z)$ by
\begin{equation}\label{eqn:PtolemyToShapes}
\begin{aligned}
z_s^{1100}  = z_s^{0011} & = & & \frac{c_{s+1001}c_{s+0110}}{c_{s+1010}c_{s+0101}}\\
z_s^{0110}  = z_s^{1001} & =  & & \frac{c_{s+0101}c_{s+1010}}{c_{s+1100}c_{s+0011}}\\
z_s^{1010}  = z_s^{0101} & =  & - & \frac{c_{s+1100}c_{s+0011}}{c_{s+1001}c_{s+0110}}.
\end{aligned}
\end{equation}

\begin{lemma}
The assignment \eqref{eqn:PtolemyToShapes} is a shape assignment, i.e.~we have a well defined map 
\begin{equation}\mu\colon\text{\{Ptolemy assignments on $\Delta^3_n$\}}\to \text{\{shape assignments on $\Delta^3_n$\}}.
\end{equation}
\end{lemma}

\begin{proof}
Using the Ptolemy relation, we obtain
$$\frac{1}{1-z_s^{0101}}=\frac{1}{1+\frac{c_{s+1100}c_{s+0011}}{c_{s+1001}c_{s+0110}}}=\frac{c_{s+1001}c_{s+0110}}{c_{s+1100}c_{s+0011}+c_{s+1001}c_{s+0110}}=\frac{c_{s+1001}c_{s+0110}}{c_{s+1010}c_{s+0101}}=z_s^{1100}.$$
The other two equations in \eqref{eqn:shapeparamrel} follow similarly.
\end{proof}

\begin{lemma}\label{lemma:ReorderCompatibility}
The map $\mu$ respects pullbacks.
\end{lemma}
\begin{proof}
It is enough to prove this for the permutations $\sigma_{01}$, $\sigma_{12}$ and $\sigma_{23}$. We prove it for $\sigma_{01}$, the other cases being similar. Since $\sgn(\sigma_{01})=-1$, we must prove that 
\begin{equation}\label{eqn:murespectspullback}(\mu(\sigma_{01}^*c))^e_s=(\mu(c)_{\sigma_{01}(s)}^{\sigma_{01}(e)})^{-1}.\end{equation}
We prove this for the edge $e=1100$, the other cases being similar. Using \eqref{eq:PullbackPtolemy}, we obtain
\begin{equation}
(\mu(\sigma_{01}^*c))^{1100}_s=\frac{(\sigma_{01}^*c)_{s+1001}(\sigma_{01}^*c)_{s+0110}}{(\sigma_{01}^*c)_{s+1010})(\sigma_{01}^*c)_{s+0101}}=\frac{c_{s'+0101}c_{s'+1010}}{c_{s'+0110}c_{s'+1001}}=(\mu(c)_{s'}^{1100})^{-1}
\end{equation}
where $s'=\sigma_{01}(s)$. This proves \eqref{eqn:murespectspullback}, hence the result.
\end{proof}



\begin{theorem}\label{thm:PtolemyYieldsShapes}
Let $\mathcal{T}$ be a concrete triangulation of $M$, and let $c_{t,\Delta}$ be a Ptolemy assignment on $(M,\mathcal{T})$. The induced shape assignment on each simplex satisfies the generalized gluing equations and thus induces a shape assignment on $(M,\mathcal{T})$. \qed
\end{theorem}

\begin{corollary} The map $\mu$ induces a map $\mu\colon P_n(\T)\to V_n(\T)$.\qed


\end{corollary}




We divide the proof of Theorem~\ref{thm:PtolemyYieldsShapes} into three parts, one for each type of equation. The idea is to prove the result for the local model near an integral point of each type. Although the local model is not a manifold, Ptolemy assignments are defined in the obvious way, i.e.~by identifying Ptolemy coordinates of identified faces via the pullback of the face pairing permutations.
