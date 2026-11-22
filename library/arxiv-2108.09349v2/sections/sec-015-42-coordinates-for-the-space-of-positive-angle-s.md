---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-015-42-coordinates-for-the-space-of-positive-angle-s
section_title: "Coordinates for the space of positive angle structures"
section_number: 4.2
pages: 17-18
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.975
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:coordinates}

The veering structure on~$\tau_{p}$ allows us to introduce convenient coordinates for a point $\theta$ in $\mathcal A(\tau_{p})$.  For $T$ in~$\tau_{p}$, let~$\theta_D T$ denote the angle assigned to the diagonals of~$T$, $\theta_R T$ the angle assigned to the red edges, and $\theta_B T$ to the blue edges.  Thus, we can write $\theta\in\mathcal{A}(\tau_{p})\subset(0,\pi)^{3(2p+1)}$ as
\begin{multline*}
(\theta_R w_0^\prime,
\theta_B w_0^\prime,
\theta_D w_0^\prime,\dots,
\theta_R w_{p-1}^\prime,
\theta_B w_{p-1}^\prime,
\theta_D w_{p-i}^\prime,\\
\theta_R w_1,
\theta_B w_1,
\theta_D w_1,\dots,
\theta_R w_p,
\theta_B w_p,
\theta_D w_p,
\theta_R s,
\theta_B s,
\theta_D s).
\end{multline*}
\begin{observation}\label{obs:edgeeqs}
Using this notation, the edge identifications in Observations~\ref{obs:veeringred} and~\ref{obs:veeringblue5} and Equations~\eqref{eq:deg4} and~\eqref{eq:s} together with Condition~(3) of Definition~\ref{def:anglestructure} yield the following \emph{edge equations}:
\begin{align*}
\left(\sum_{i=0}^{p-1} 2\theta_R w_i^\prime\right) +\left(\sum_{i=1}^{p} 2\theta_R w_i\right) +2\theta_R s + \theta_Dw_0^\prime+\theta_Dw_p&=2\pi\\
\theta_B w_0^\prime+\theta_D w_1+\theta_B s+\theta_D w_{p-1}^\prime+\theta_B w_p&=2\pi\\
\theta_B w_0^\prime+\theta_D w_1^\prime+\theta_B s+\theta_D  w_{p-1}+\theta_B w_p&=2\pi\\
\theta_D w_{i-1}+\theta_B w_{i}+\theta_B w_{i}^\prime+\theta_D  w_{i+1}^\prime&=2\pi&\text{ for } i=2, \dots p-2\\
\theta_D w_{i-1}^\prime+\theta_B w_{i}+\theta_B w_{i}^\prime+\theta_D  w_{i+1}&=2\pi&\text{ for } i=1, \dots p-1\\
\theta_D s+\theta_B w_1^\prime+\theta_B w_1+\theta_D  w_2^\prime&=2\pi\\
\theta_D s+\theta_B w_{p-1}^\prime+\theta_B w_{p-1}+\theta_D  w_{p-2}&=2\pi.
\end{align*}
These equations hold for $p>1$ as long as each term is defined.  (Recall that there are no tetrahedra labelled $w_0$ or $w_p^\prime$.)  

The first two equations also hold when $p=1$, and, after substituting $s(db)$ and~$s(ac)$ for the undefined terms $w_1^\prime(02)$ and $w_{p-1}(20)$ as in Observation~\ref{obs:veeringblue5}, so does the third:
$$
\theta_B w_0^\prime+\theta_D s+\theta_B s+\theta_D  s+\theta_B w_1=2\pi.
$$
\end{observation}

\begin{observation}\label{obs:diagonaleqs}
Several pairs of  edge equations above share angles coming from the blue edges.  These angles will cancel when one equation is subtracted from the other, yielding the following equalities for the diagonals:
\begin{align*}
    \theta_D w_1-\theta_D w_1^\prime
    =\theta_D w_3-\theta_D w_3^\prime
    =\theta_D w_5-\theta_D w_5^\prime
    =&\cdots
    \\
\theta_D w_2-\theta_D w_2^\prime
    =\theta_D w_4-\theta_D w_4^\prime
    =\theta_D w_6-\theta_D w_6^\prime
    =&\cdots.
\end{align*}
In addition,
\begin{align*}
      \theta_D w_{p-2}-\theta_D w_{p-2}^\prime
    &=\theta_D w_p-\theta_D s
      \\
       \theta_D s-\theta_D w_0^\prime
    &=\theta_D w_2-\theta_D w_2^\prime
    \\
 \theta_D w_{p-1}-\theta_D w_{p-1}^\prime
    &=\theta_D w_1-\theta_D w_1^\prime.
\end{align*}
These equations hold when $p>1$ and each term is defined.
The final equation, which is derived by taking the difference between the equations for the degree-5 edges implies that, if $p$ is odd (so $p-1$
 is even), then all of the differences listed above are equal.  If $p$ is even, all differences, $\theta_D w_j-\theta_D w_j^\prime$, with $j$ even are also equal to $\theta_D s-\theta_D w_0^\prime$ and $\theta_D w_p-\theta_D s$, but not necessarily to $\theta_D w_1-\theta_D w_1^\prime$, etc. 
 
 
\end{observation}
The corresponding equation for $p=1$ is:
$$
      \theta_D s-\theta_D w_0^\prime
    =\theta_D w_1-\theta_D s.
$$
