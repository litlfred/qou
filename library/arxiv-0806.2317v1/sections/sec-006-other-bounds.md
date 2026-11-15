---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-006-other-bounds
section_title: "Other bounds"
section_number: null
pages: 18-19
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.989
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:otherbounds}

Certain cases of equality in Corollaries \ref{cor:onebound} and \ref{cor:twobound} also achieve equality for bounds on the size of the largest angle in a set of subspaces. For real Grassmannians, Conway, Hardin and Sloane \cite{chs} call these bounds the \defn{simplex} and \defn{orthoplex} bounds. Here we give their complex analogues. 

Recall that if $P_a$ be the $n \times n$ projection matrix for $a \in \gras{m}{n}$, then $P_a$ is Hermitian with trace $m$, so $P'_a = P_a - mI/n$ lies in a real space of dimension $n^2-1$. Moreover $||P'_a||^2 := \tr(P'_aP'_a) = m(1-m/n)$, so $P'_a$ is embedded onto a sphere of radius $\sqrt{m(1-m/n)}$ in $\re^{n^2-1}$. Further recall that the chordal distance on $\gras{m}{n}$ is defined by 
\begin{align*}
d_c(a,b)^2 & = m - \tr(P_aP_b) \\
& = \frac{1}{2}||P_a - P_b||^2 = \frac{1}{2}||P'_a - P'_b||^2.
\end{align*}
With this distance, the Grassmannians are isometrically embedded into $\re^{n^2-1}$. The ``Rankin bounds" given in Theorem \ref{thm:rankin} below (see \cite[Theorems 6.1.1 \& 6.1.2]{bor}) are bounds on the minimum distance between points on a real sphere as a function of the number of points and the dimension of the space. An \defn{equatorial simplex} refers to a set of $N$ points on the unit sphere that form a simplex in a hyperplane of dimension $N-1$.

\begin{theorem}
\label{thm:rankin}
Given $N$ points on a sphere of radius $r$ in $\re^D$, the minimum distance $d$ between any two points satisfies 
\[
d \leq r\sqrt{\frac{2N}{N-1}}.
\]
Equality requires $N \leq D+1$ and occurs if and only if the points form a regular equatorial simplex. For $N > D+1$, the minimum distance satisfies
\[
d \leq r\sqrt{2},
\]
and equality requires $N \leq 2D$. When $N = 2D$, equality occurs if and only if the points are the vertices of a regular orthoplex.
\end{theorem}

Conway, Hardin and Sloane \cite{chs} apply these bounds to get the simplex and orthoplex bounds for real Grassmannians: we can do the same for the complex Grassmannians.

\begin{corollary}
\label{cor:simortho}
Given a set $S$ points in $\gras{m}{n}$, the largest inner product value $\al = \ip{a}{b}$ between any two points satisfies 
\begin{equation}
\al \geq m\frac{m|S|-n}{n|S|-n}.
\label{eqn:albound}
\end{equation}
Equality requires $|S| \leq n^2$ and occurs if and only if the points form a regular equatorial simplex in $\re^{n^2-1}$. For $|S| > n^2$, the largest inner product $\be$ satisfies
\begin{equation}
\be \geq \frac{m^2}{n},
\label{eqn:albebound}
\end{equation}
and equality requires $|S| \leq 2(n^2-1)$. Equality occurs if the points are the $2(n^2-1)$ vertices of a regular orthoplex in $\re^{n^2-1}$.
\end{corollary}

If $S$ is an $\{\al\}$-code, then solving inequality \eqref{eqn:albound} for $|S|$ recovers the relative bound in Corollary \ref{cor:onebound}. Moreover, if $|S| = n^2$ (equality in the absolute bound of Corollary \ref{cor:abscodebnd1}), then
\[
\al = \frac{m(mn-1)}{n^2-1}.
\]
On the other hand, if $S$ is a $\{0,m^2/n\}$-code, and $m = n/2$, then the relative bound in Corollary \ref{cor:twobound} implies that 
\[
|S| \leq 2(n^2-1),
\]
which corresponds to equality in the orthoplex bound \eqref{eqn:albebound}.
