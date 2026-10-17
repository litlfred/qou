---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-017-5-the-maximal-volume-occurs-at-a-positive-angle
section_title: "The maximal volume occurs at a positive angle structure"
section_number: 5
pages: 20-23
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.988
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:proofq=1}

Corollary~\ref{cor:positiveanglestructure} shows that the space of positive angle structures on each triangulation~$\tau_{p}$ is nonempty, so we have accomplished the first step of the Casson-Rivin program described by  Futer and Gu\'eritaud in~\cite{AngledtoHyperbolic} and summarized in~\ref{sec:CR}.  In this section, we complete the program, proving the main result.

\begin{thm}\label{thm:q=1}
Let $L_p$ be the closure of the 3-braid $C^2\sigma_1^p\sigma_2^{-1}$ and $X_{p}$ be its complement in the 3-sphere.  Then there is an ideal triangulation of $X_{p}$ that is geometric.
\end{thm}

\begin{proof}

Let $\tau_{p}$ be the triangulation defined in~\ref{sec:anyp}. By  Corollary~\ref{cor:positiveanglestructure}, $\mathcal{A}(\tau_{p})\ne\emptyset$, which means the volume functional $\mathcal{V}$ attains its maximum on the compact set $\overline{\mathcal{A}(\tau_{p})}$, say at the point~$\alpha$.  A maximal point has two important properties.  The first was proved in Lemma~\ref{lem:00pi}.

\begin{property}\label{property:1}
If $\alpha$ is maximal and assigns an angle in $\{0,\pi\}$ to a tetrahedron, then the tetrahedron must be flat, i.e., its angles are $0$, $0$, $\pi$ in some order.  
\end{property}

The second important property derives from a symmetry of the coordinates of a maximal point.  Let the involution $\iota:\tau_{p}\rightarrow\tau_{p}$ be as in Proposition~\ref{prop:symmetry}, so $\iota$ fixes~$s$ and takes $w_i^\prime$ to $w_{p-i}$.  Then $\iota$ induces a symmetry on $\overline{\mathcal{A}(\tau_{p})}$, which rearranges the coordinates of an angle structure tetrahedron by tetrahedron, so, just as in Observation~\ref{obs:equalvolume}, $\mathcal{V}(\iota\alpha)=\mathcal{V}(\alpha)$.  Thus, if $\alpha$ is maximal, so is $\iota\alpha$, but  maximal points are unique by Proposition~\ref{prop:maxunique}, so $\iota\alpha=\alpha$, and  Corollary~\ref{cor:symmetryedgeeqs} together with Definition~\ref{def:anglestructure} guarantee the following.

\begin{property}\label{property:2}
If $\alpha$ is maximal, then the angles assigned by $\alpha$ belong to $[0,\pi]$; sum to~$\pi$ within a tetrahedron; and are determined by the angles assigned to $w_1, w_2, \dots, w_p$ and $s$, which must satisfy Equations~\eqref{eq:deg4p+4}--\eqref{eq:diagonals}.
\end{property}

Our goal is to use these properties to show that the maximal point, $\alpha$, is in~$\mathcal{A}(\tau_{p})$, not its boundary.  Then we can apply the Casson-Rivin Theorem from~\ref{sec:CR} \cite[Theorem 1.2]{AngledtoHyperbolic} and conclude that $\alpha$ corresponds to the complete hyperbolic structure on $X_{p}$, thus proving Theorem~\ref{thm:q=1}.  We will show that $\alpha$ is in $\mathcal{A}(\tau_{p})$ by showing that points in $\mathcal{B}=\overline{\mathcal{A}(\tau_{p})}-\mathcal{A}(\tau_{p})$ will never maximize the volume.  We do so by proving the following.

\begin{prop}\label{prop:volume=0}
Any $\beta\in\mathcal{B}$ satisfying Properties~\ref{property:1} and~\ref{property:2} must have $\mathcal{V}(\beta)=0$.
\end{prop}

\begin{proof}[Proof of Proposition~\ref{prop:volume=0}]

Let $\beta\in\mathcal{B}$ satisfy both Property~\ref{property:1} and Property~\ref{property:2}.  Because $\beta$ is in the boundary of the space of positive angle structures, there is a tetrahedron in $\tau_{p}$ to which $\beta$ assigns  angles from the set $\{0, \pi\}$.  By Property~\ref{property:1}, this tetrahedron is flat (has angles $0$, $0$, and $\pi$).  Using Property~\ref{property:2}, we can conclude that $\beta$ must assign~$\pi$ to at least one of the edges of $w_1, w_2, \dots w_p$ or $s$.  We now explore which edges can have such assignments and determine the resulting volume.

Observe that, because all angle assignments are nonnegative, assigning an angle measure of~$\pi$ to any $R$ edge of a $w$ tetrahedron violates Equation~\eqref{eq:deg4p+4} of Corollary~\ref{cor:symmetryedgeeqs} and thus Property~\ref{property:2}.  Therefore, no $\beta_R w_i$ can equal $\pi$.  We will use this result often, so we record it as a lemma and follow with another useful lemma.

\begin{lem}\label{lem:noRsarepi}
If $\beta\in\mathcal{B}$ satisfies both Property~\ref{property:1} and~\ref{property:2}, $\beta_R w_i$ cannot equal $\pi$ for $i=1,\dots,p$.\qed
\end{lem}


\begin{lem}\label{lem:wporsflat}
If $\beta\in\mathcal{B}$ satisfies both Property~\ref{property:1} and~\ref{property:2}, and either $w_p$ or $s$ is flat, then all tetrahedra are flat, so $\mathcal{V}(\beta)=0$.
\end{lem}

\begin{proof}[Proof of Lemma~\ref{lem:wporsflat}]

If a tetrahedron is flat, one of its edges is assigned an angle of~$\pi$.  By Lemma~\ref{lem:noRsarepi}, $\beta_R w_p$ cannot equal~$\pi$.  However, $\beta_R s$ could equal~$\pi$, and, if this is the case, Equation~\eqref{eq:deg4p+4} forces $\beta_R w_i$ to equal~$0$ for all $i=1,\dots,p$, so, by Property~\ref{property:1}, the non-$s$ tetrahedra are also flat.  Because, $\beta_D w_p$ also appears in Equation~\eqref{eq:deg4p+4}, a similar argument shows that if $\beta_D w_p=\pi$, all tetrahedra are flat.  By Equation~\eqref{eq:diagonals}, $\beta_D w_p=\beta_D s$, so the same holds if $\beta_D s=\pi$.  Thus, it only remains to check what happens if the angle at a $B$ edge of $w_p$ or $s$ equals $\pi$.
\begin{itemize}
    \item If $\beta_B w_p=\pi$, Equation~\eqref{eq:deg5a} implies that $\beta_B s=0$, so, by Property~\ref{property:1}, there is a $\pi$ angle at either the $R$ or $D$ edge of $s$, and, in either case, as observed above, all tetrahedra are flat.  
    \item If $\beta_B s=\pi$, then $\beta_D s=0$, so $\beta_D w_p$ also equals~$0$ (Equation~\eqref{eq:diagonals}), and, by Property~\ref{property:1}, either $\beta_R w_p$ or $\beta_B w_p$ equals~$\pi$.  Because of Lemma~\ref{lem:noRsarepi}, $\beta_B w_p$  must be~$\pi$, so, by the previous case, all tetrahedra are flat.
\end{itemize}
Therefore, if either $w_p$ or $s$  has an  assigned angle of~$\pi$, $\mathcal{V}(\beta)=0$.
\end{proof}

Returning to the proof of Proposition~\ref{prop:volume=0}, recall that $\beta\in\mathcal{B}$ must assign~$\pi$ to at least one of the edges of $w_1, w_2, \dots w_p$ or~$s$.  Lemmas~\ref{lem:noRsarepi} and~\ref{lem:wporsflat} cover the $R$ edges and the tetrahedra $w_p$ and $s$, so the only edges left to consider are the $B$ and $D$ edges of $w_1, w_2, \dots w_{p-1}$.  We start with the $B$ edges and first examine the case when $\beta_B w_1=\pi$.

If $\beta_B w_1=\pi$, then $\beta_D w_1$ equals~$0$ and, by Equation~\eqref{eq:diagonals}$_{i=1}$, so does $\beta_D w_{p-1}$.  Property~\ref{property:1} implies that in $w_{p-1}$ one of the other angles must be $\pi$, but, because of  Lemma~\ref{lem:noRsarepi}, it cannot be the angle at the $R$ edge. Consequently, $\beta_B w_{p-1}$ equals~$\pi$ and Equation~\eqref{eq:deg4c} implies
$\beta_D s$ must equal~$0$, so $s$ is flat and, by Lemma~\ref{lem:wporsflat}, $\mathcal{V}(\beta)=0$.  

Having shown that if $\beta$ assigns the angle $\pi$ to a $B$ edge of $w_1$, then $\mathcal{V}(\beta)=0$, we now consider the $B$ edges of $w_j$ with $1<j\le k$.  By repeatedly applying Equations~\eqref{eq:diagonals} and~\eqref{eq:deg4a} together with Property~\ref{property:1} and Lemma~\ref{lem:noRsarepi}, we will push the flatness of $w_j$ all the way down to $w_1$, allowing us to once again conclude $\mathcal{V}(\beta)=0$.  In particular, if $\beta_B w_j=\pi$, then $\beta_D w_j$ equals~$0$ and, by Equation~\eqref{eq:diagonals}$_{i=j}$, so does $\beta_D w_{p-j}$.  There is a $\pi$ angle in $w_{p-j}$ (Property~\ref{property:1}) and it cannot occur at the $R$ edge (Lemma~\ref{lem:noRsarepi}), so $\beta_B w_{p-j}$, will equal~$\pi$.  With both $\beta_B w_j$ and $\beta_B w_{p-j}$ equal to $\pi$, Equation~\eqref{eq:deg4a}$_{i=j}$ implies that $\beta_D w_{j-1}=0$, so, by  Equation~\eqref{eq:diagonals}$_{i=j-1}$, $\beta_D w_{p-(j-1)}=0$ also.  Another application of Property~\ref{property:1} and Lemma~\ref{lem:noRsarepi} shows both $\beta_B w_{j-1}$ and $\beta_B w_{p-(j-1)}$ are equal to $\pi$ and we can apply Equation~\eqref{eq:deg4a}$_{i=j-1}$ to conclude $\beta_D w_{j-2}=0$.  Continuing in this manner and eventually applying Equation~\eqref{eq:deg4a}$_{i=2}$ when both $\beta_B w_2$ and $\beta_B w_{p-2}$ are equal to $\pi$, allows us to conclude that $\beta_D w_1=0$.  Thus (by Property~\ref{property:1} and Lemma~\ref{lem:noRsarepi}), $\beta_B w_1=\pi$, so $\mathcal{V}(\beta)=0$.

It remains to examine the $B$ edges of $w_j$ where $j>k$.  If $\beta_B w_j$ equals $\pi$, then $\beta_D w_j=0$, so applying Equation~\eqref{eq:diagonals}$_{i=p-j}$, Property~\ref{property:1}, and Lemma~\ref{lem:noRsarepi} shows that $\beta_B w_{p-j}=\pi$.  Because $p-j\le k$, this case has already been covered.  Therefore, if any of the $B$ edges of $w_1, w_2, \dots w_{p-1}$ have angle equal to~$\pi$, then $\mathcal{V}(\beta)=0$.

The proof for the $D$ edges is a little simpler, because there is no need to appeal to Lemma~\ref{lem:noRsarepi}. If $\beta_D w_1=\pi$, then, by Equation~\eqref{eq:diagonals}$_{i=1}$, $\beta_D w_{p-1}=\pi$, so both $\beta_B w_1$ and $\beta_B w_{p-1}$ are equal to~$0$. In this situation, applying Equation~\eqref{eq:deg4c} yields $\beta_D s=\pi$,
so $s$ is flat and, by Lemma~\ref{lem:wporsflat}, $\mathcal{V}(\beta)=0$.  If $j\le k$ and $\beta_D w_j$ equals $\pi$, then, by Equation~\eqref{eq:diagonals}$_{i=j}$, so does $\beta_D w_{p-j}$, and both $\beta_B(w_j)$ and $\beta_B(w_{p-j})$ equal~$0$, so Equation~\eqref{eq:deg4a}$_i$ implies $\beta_D w_{j-1}=\pi$.  Continuing in this manner shows that if $\beta_D w_j$ equals~$\pi$, so does $\beta_D w_1$, and thus $\mathcal{V}(\beta)=0$.  If $j> k$ and $\beta_D w_j=\pi$, then, by Equation~\eqref{eq:diagonals}$_{i=p-j}$, $\beta_D w_{p-j}=\pi$ with $p-j\le k$, a previous case.  
\end{proof}

Any point maximizing the volume functional must satisfy Properties~\ref{property:1} and~\ref{property:2}.  By proving Proposition~\ref{prop:volume=0}, we have shown that any point, $\beta$, on the boundary of $\mathcal{A}(\tau_{p})$ satisfying these properties has $\mathcal{V}(\beta)=0$.  Therefore, the maximal point $\alpha$ must be on the interior of $\mathcal A(\tau_{p})$, and, by the Casson-Rivin Theorem (\ref{sec:CR} and \cite[Theorem 1.2]{AngledtoHyperbolic}), $\alpha$ corresponds to the complete hyperbolic structure on~$X_{p}$.  Thus, the triangulation $\tau_{p}$ is geometric, which concludes the proof of Theorem~\ref{thm:q=1}.
\end{proof}

\begin{cor}\label{cor:notconjugate}
In the braid group, $C^2\sigma_1^p\sigma_2^{-1}$ is not conjugate to $\sigma_1^{p_0}\sigma_2^{q_0}$ for integers $p_0$ and $q_0$.
\end{cor}

\begin{proof}
Closures of braids of the form $\sigma_1^{p_0}\sigma_2^{q_0}$ are not hyperbolic, but Theorem~\ref{thm:q=1} shows that the closure of $C^2\sigma_1^p\sigma_2^{-1}$ is.
\end{proof}

\begin{cor}\label{cor:pretzelstoo}
The complements of the $(-2,3,n)$-pretzel knots and links admit geometric triangulations for $n\ge7$.
\end{cor}

\begin{proof}
 Recall that the braid group has the single relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2 $ and that $C$, which is this element's square, is central.
 Conjugate words in the braid group yield equivalent braid closures, so, using the relation and the centrality of~$C$, $L_p$, the closure of $C^2\sigma_1^p\sigma_2^{-1}$ with $p\ge1$, is also the closure of 
\begin{align*}
    (\sigma_2\sigma_1\sigma_2)(\sigma_1\sigma_2\sigma_1)C\sigma_1^p\sigma_2^{-1} &\sim \sigma_2\sigma_1\sigma_2 C\sigma_1^{p+2}\\
    &=\sigma_1\sigma_2C\sigma_1^{p+3}\\
    &\sim\sigma_2(\sigma_1\sigma_2\sigma_1)(\sigma_1\sigma_2\sigma_1)         \sigma_1^{p+4}\\
    &=\sigma_1\sigma_2\sigma_1\sigma_1\sigma_1\sigma_2\sigma_1^{p+5}\\
    &\sim\sigma_1^3\sigma_2\sigma_1^{p+6}\sigma_2;
\end{align*}
here $\sim$ denotes the equivalence relation of conjugacy.  

As indicated in Figure~\ref{fig:pretzel}, the closure of $\sigma_1^3\sigma_2\sigma_1^{p+6}\sigma_2$ is a pretzel. Using our definitions, $\sigma_1$ and  $\sigma_2$ generate left-handed (negative) twists, so $L_p$ is a pretzel with $-(p+6)$, $2$, and $-3$ half-twists, or equivalently  --- after rolling the $p+6$ half-twists to the right --- $L_p$ is the $(2,-3, -(p+6))$-pretzel, and $X_p$ is its complement. By Theorem~\ref{thm:q=1}, $X_p$ admits a geometric triangulation.  But the complement of the $(-2,3,p+6)$-pretzel is homeomorphic (via a reflection) to $X_p$, so it also has a geometric triangulation.
\end{proof}
\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{arepretzels.pdf}
\put(-.5,3.2){\small{$p+6$}}
\put(.7,3.2){$\Bigg\{$}
\end{overpic}
\caption{The $(-(p+6),2,-3)$-pretzel is also the closure of the braid $\sigma_1^3\sigma_2\sigma_1^{p+6}\sigma_2$.  Start at the dashed line and read the braid counterclockwise (strands numbered from the outside in).\label{fig:pretzel}}
\end{figure}

The braid relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2 $ and the centrality of $C=(\sigma_1\sigma_2)^{3}$ can also be used to show that $L_p$ is equivalent to the braid closure of $\sigma_1^{p+1}(\sigma_1\sigma_2)^{5}$:
$$
C^2\sigma_1^p\sigma_2^{-1}=\sigma_1^p(\sigma_1\sigma_2)^{6}\sigma_2^{-1}=\sigma_1^p(\sigma_1\sigma_2)^{5}\sigma_1\sim \sigma_1^{p+1}(\sigma_1\sigma_2)^{5}.
$$
In this form, $L_p$ is a T-link as defined by Birman and Kofman in~\cite{TLinks}, where they show that T-links are in one-to-one correspondence with Lorenz links.
\begin{cor}\label{cor:Tlinkstoo}
The complements of the T-links/Lorenz links formed as closures of the braids $\sigma_1^{p+1}(\sigma_1\sigma_2)^{5}$ admit  geometric triangulations for $p>1$. \qed
\end{cor}
