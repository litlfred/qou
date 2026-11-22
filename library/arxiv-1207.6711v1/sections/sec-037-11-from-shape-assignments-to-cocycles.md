---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-037-11-from-shape-assignments-to-cocycles
section_title: "From shape assignments to cocycles"
section_number: 11
pages: 39-41
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.935
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:ReconstructRep}

We now prove that the bottom row of diagram~\eqref{eqn:DiagramIntro} consists of one-one correspondences.
The idea is to first prove that a shape assignment determines a natural cocycle on each doubly truncated simplex. This is a consequence of the internal gluing equations. The face and edge equations imply that the cocycles glue together to a cocycle on $M$; the middle edges glue together because of the face equations, and the edge equations imply that we can fill in the prisms.

\begin{lemma}\label{lemma:AgreeonFaces}
If two shape assignments $z$ and $w$ agree on two faces $i$ and $j$, then $z=w$, i.e.~if $z_s^e=w_s^e$ when $e_i=s_i=0$ or $e_j=s_j=0$, then $z_s^e=w_s^e$ for all $(s,e)\in\Delta^3_{n-2}(\Z)\times\dot\Delta^3_2(\Z)$.
\end{lemma}

\begin{proof}
We may assume that $z$ and $w$ agree on face $2$ and $3$. It is enough to prove that $z_s^{1100}=w_s^{1100}$ for all $s=(s_0,s_1,s_2,s_3)\in\Delta^3_{n-2}(\Z)$. By assumption, this holds if either $s_2$ or $s_3$ is $0$. Suppose by induction that $z_s^{1100}=w_s^{1100}$ for all $s$ with $s_2+s_3<k$, and let $s\in\Delta^3_{n-2}(\Z)$ be a subsimplex with $s_2+s_3=k$. Since the result holds, when either $s_2$ or $s_3$ is $0$, we may assume that $s=\alpha+0011$, with $\alpha\in\Delta^3_{n-4}(\Z)$. Let $t=s+1100$. By Lemma~\ref{lemma:InternalEquation}, $z$ and $w$ satisfy the internal gluing equations, i.e.~we have
\begin{equation}
z^{0011}_{\alpha+1100}z^{0101}_{\alpha+1010}z^{0110}_{\alpha+1001}z^{1001}_{\alpha+0110}z^{1010}_{\alpha+0101}z^{1100}_s=w^{0011}_{\alpha+1100}w^{0101}_{\alpha+1010}w^{0110}_{\alpha+1001}w^{1001}_{\alpha+0110}w^{1010}_{\alpha+0101}w^{1100}_s,
\end{equation}
which equals $1$. Note that for all terms except $z_s^{1100}$ and $w_s^{1100}$, the lower index satisfies $s_2+s_3<k$. By induction, each term $z^{1111-I}_{\alpha+I}$ equals $w^{1111-I}_{\alpha+I}$. Hence $z^{1100}_s=w_s^{1100}$, completing the induction. 
\end{proof}

\begin{lemma}\label{lemma:UniqueFactorization}
The factorization of the middle edges is unique, i.e.~if
\begin{equation}\label{eq:UniqueFactorization}
\prod_{k=1}^{n-1}\left(\prod^{n-k}_{i=1}x_i(1)\prod_{i=1}^{n-k-1}H_i(a_{k,i})\right)=\prod_{k=1}^{n-1}\left(\prod^{n-k}_{i=1}x_i(1)\prod_{i=1}^{n-k-1}H_i(b_{k,i})\right),
\end{equation}
then $a_{k,i}=b_{k,i}$ for all $k,i$.
\end{lemma}

\begin{proof}
Suppose~\eqref{eq:UniqueFactorization} holds. In particular, all diagonal entries are equal. Hence, as in Remark~\ref{rm:DiagonalEntries}, the equality $\prod_{i=l}^{n-2}\prod_{k=1}^{n-1-i} a_{k,i}=\prod_{i=l}^{n-2}\prod_{k=1}^{n-1-i} b_{k,i}$ holds for all $l=1,\dots,n$. The result now follows by induction.





\end{proof}

\begin{proposition}\label{prop:ZisSurjective}
The map $\mathcal Z$ from generic decorations on $\Delta^3_n$ to shape assignments on $\Delta^3_n$ is surjective.
\end{proposition}

\begin{proof}
Let $z$ be a shape assignment. We wish to construct a decoration $D$ with $\mathcal Z(D)=z$. Let $D=(B, q_1B, \beta_{012} q_1 B, \gamma_{012} \beta_{013} q_1 B)$ and let $z'=\mathcal Z(D)$. By Lemma~\ref{lemma:AgreeonFaces}, it is enough to prove that $z'$ agrees with $z$ on face $2$ and $3$. 
We prove this for face $3$ ($s_3=0$), face $2$ being similar. We use induction on $s_2$. Let $\beta'$ and $\gamma'$ denote the labelings of the natural cocycle of $D$. Let $X_t$ and $X'_t$ denote the $X$ coordinates of $z$ and $z'$. Note that $\beta'_{012}=\beta_{012}$ and $\gamma'_{012}=\gamma_{012}$. Since $\gamma'_{012}=\gamma_{012}$, the equality $z_s^{1100}=w_s^{1100}$ holds for $s_2=0$ proving the induction start. Since $\beta'_{012}=\beta_{012}$, it follows from 
Lemma~\ref{lemma:UniqueFactorization} that $X_t=X'_t$ for all $t$ on face $2$ and $3$.
Now suppose by induction that $z_s^{1100}=w_s^{1100}$ holds for $s_2<k$. Let $t=s+1100$.  
We have
\begin{equation}
-z_s^{1100}z_{t-1010}^{1010}z^{0110}_{t-0110}=X_t=X'_t=-z_s'^{1100}z_{t-1010}'^{1010}z'^{0110}_{t-0110}.
\end{equation}
By induction, $z_{t-1010}^{1010}=z_{t-1010}'^{1010}$ and $z_{t-0110}^{0110}=z_{t-0110}'^{0110}$, so we must also have
$z_s^{1100}=z_s'^{1100}$. This proves the result.
\end{proof}


\begin{theorem}\label{thm:One-One}
The bottom row of diagram~\eqref{eqn:DiagramIntro} consists of one-one correspondences. 
\end{theorem}

\begin{proof}
We first prove this for a simplex. The map $\mathcal L_{\alpha\beta\gamma}$ is bijective by Remark~\ref{rm:CocycleToDecoration}. Injectivity of $\mathcal Z$ follows from Theorem~\ref{thm:NaturalCocycleShapes}, and surjectivity was proved in Proposition~\ref{prop:ZisSurjective}. Now suppose $z$ is a shape assignment on $(M,\T)$. We must prove that $z$ determines a generic decoration, or equivalently a natural cocycle. By Proposition~\ref{prop:ZisSurjective} $z$ determines a natural cocycle on each doubly truncated simplex. We must prove that these fit together to form a cocycle on $M$. The labelings of long edges obviously match up, and by \eqref{eq:NaturalCocycleFormula} and Remark~\ref{rm:HalfofFaceEq}, the middle edges match up if and only if the face equations are satisfied. 
Now all that is left to prove is that the induced labeling on the prisms are cocycles. This is a direct consequence of the edge equations.
\end{proof}

\begin{remark} 
It follows from Theorem~\ref{thm:One-One} that \eqref{eq:NaturalCocycleFormula} gives an explicit map from shape assignments to cocycles. Combined with Remark~\ref{rm:CocycleToDecoration} this gives explicit inverses of $\mathcal Z$ and $\mathcal L_{\alpha\beta\gamma}$. Similarly, we have explicit inverses of $\mathcal C$ and $\mathcal L_{\alpha\beta}$ via \eqref{eq:betaTrunc}.
\end{remark}
