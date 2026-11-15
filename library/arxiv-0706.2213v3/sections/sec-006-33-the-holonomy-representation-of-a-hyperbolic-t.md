---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-006-33-the-holonomy-representation-of-a-hyperbolic-t
section_title: "The holonomy representation of a hyperbolic twist knot"
section_number: 3.3
pages: 5-6
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{sechyp}

\subsubsection{Some generalities}
    It is well known that the complete hyperbolic structure of a hyperbolic knot complement determines a unique discrete faithful representation of the knot group in $\mathrm{PSL}_2(\CC)$, called the \emph{holonomy representation}. It is proved~\cite[Proposition 1.6.1]{HandBookGT} that such a representation lifts to $\SL$ and determines two irreducible representations in $\SL$.
    
    The trace of the peripheral--system at the holonomy is $\pm 2$ because their images by the holonomy are parabolic matrices. More precisely, Calegari~\cite{Calegari} proved that the trace of the longitude at the holonomy is always $-2$ and the trace of the meridian at the holonomy is $\pm 2$, depending on the choice of the lift. 
We summarize all this in the following important fact.

\begin{fact}\label{fact:Calegari}
Let $\rho_0$ be one of the two lifts of the discrete and faithful representation associated to the complete hyperbolic structure of a hyperbolic knot $K$ and let {$T^2 = \partial E_K$} denote the boundary of the knot exterior. The restriction of $\rho_0$ to $\pi_1(T^2)$ is conjugate to the parabolic representation such that
\[
\mu \mapsto 
\pm \left(
    \begin{array}{cc}
      1 & 1 \\
      0 & 1
    \end{array}
    \right), 
\quad 
\lambda \mapsto 
        \left(
        \begin{array}{cc}
          -1 & \hphantom{-}\cusp \\
          \hphantom{-}0 & -1
        \end{array}
        \right).
\]
Here $\cusp = \cusp(\lambda, \mu) \in \CC$ is called the cusp shape of $K$.
\end{fact}

\begin{remark}
The universal cover of the exterior of a hyperbolic knot is the hyperbolic $3$-space $\mathbb{H}^3$. The cusp shape can be seen as the ratio of the translations of the parabolic isometries of $\mathbb{H}^3$ induced by projections to $\mathrm{PSL}_2(\CC)$. Of course, the cusp shape $\cusp = \cusp(\lambda, \mu)$ depends on the choice of the basis $(\mu, \lambda)$ for $\pi_1 (T^2)$. A change in the basis of $\pi_1 (T^2)$ shifts $\cusp$ by an integral M\"obius transformation. 
\end{remark}


\subsubsection{Holonomy representations of twist knots}

This subsection is concerned with the $\SL$-representations which are lifts of the holonomy representation in the special case of (hyperbolic) twist knots. In particular, we want to specify the images, up to conjugation, of the group generators $x$ and $y$ (see the group presentation~(\ref{P:G2B})).


\begin{lemma}\label{L8}
Let $K$ be a hyperbolic two--bridge knot and 
suppose that its knot group admits the following presentation 
$\Pi(K)=\langle x,y \, | \, \Omega x=y \Omega\rangle$. 
If $\rho_0$ denotes a lift in $\SL$ of the holonomy representation, 
then $\rho_0$ is given, up to conjugation, {by}
\[
x \mapsto 
 \pm \left(
\begin{array}{cc}
 1 & 1 \\
 0 & 1 
\end{array}
\right)
, \quad
y \mapsto 
 \pm\left(
\begin{array}{cc}
 \hphantom{-}1 & 0 \\
 - u & 1 
\end{array}
\right),
\]
where $u$ is a root of Riley's equation $\phi_K(1, u) = 0$ of $K$.
\end{lemma}

\begin{proof}
It follows from Fact~\ref{fact:Calegari} that
each lift of the holonomy representation maps the meridian to 
$\pm \left(
\begin{smallmatrix}
1 & 1\\
0 & 1
\end{smallmatrix}
\right).$
It is known that the lifts of the holonomy representation are 
irreducible $\SL$-representations, 
in particular,  non--abelian ones.
Hence we can construct the $\SL$-representations which are conjugate to 
the lifts of the holonomy representation 
by using roots of Riley's equation.

Using Section \ref{ReviewCharK}, if $x$ is sent to $\pm \left(
\begin{smallmatrix}
1 & 1\\
0 & 1
\end{smallmatrix}
\right)$ then $y$ is sent to $\pm\left(
\begin{smallmatrix}
 \hphantom{-}1 & 0 \\
 - u & 1 
\end{smallmatrix}\right)$, where $u$ is a root of Riley's equation $\phi_K(1,u) = 0$.
\end{proof}

\begin{notation*}
If we let $A$ be an element of $\SL$, 
then the adjoint actions of $A$ and $-A$ are same.
So, we use the $\SL$-representation such that 
$$
x \mapsto 
\left(
\begin{array}{cc}
  1 & 1 \\
  0 & 1 
\end{array}
\right)
, \quad
y \mapsto 
\left(
\begin{array}{cc}
 \hphantom{-}1 & 0 \\
-u &  1 
\end{array}
\right) \quad (\text{where } u \text{ is such that } \phi_K(1, u) = 0)
$$
as a lift of the holonomy representation and we improperly call it the \emph{holonomy representation}. 
\end{notation*}
