---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-016-43-a-symmetry-of-the-space-of-angle-structures
section_title: "A symmetry of the space of angle structures"
section_number: 4.3
pages: 18-20
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.945
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:symmetry}

Consider the closure of $C^2\sigma_1^p\sigma_2^{-1}$ as shown on the right of Figure~\ref{fig:6braid}.  Moving the lone half-twist up so that it occurs halfway along the $\sigma_1$ half-twists reveals an order 2 symmetry of $X_p$ --- rotate about a horizontal line through the lone half-twist.  This involution induces a symmetry on the triangulation $\tau_p$ --- rotate the tetrahedra in Figure~\ref{fig:anyp} about a horizontal line and take $s$ to itself.  This symmetry will respect  angle structures:

\begin{prop} \label{prop:symmetry}
An involution $\iota:\tau_{p}\rightarrow\tau_{p}$ that fixes $s$ and takes $w_i^\prime$ to $w_{p-i}$ by matching up their $R$, $B$, and $D$ edges induces a symmetry of $\mathcal A(\tau_{p})$.
\end{prop}

\begin{proof}
Let $\theta\in\mathcal A(\tau_{p})$.  According to Definition~\ref{def:anglespacesymmetry}, to verify that $\iota\theta$ is also in $\mathcal A(\tau_{p})$, we need to check that the sum of the dihedral angles at each edge of of~$X_{p}$ is~$2\pi$, when the angle measure is given by~$\iota\theta$.  Thus, it is enough to verify that $\iota\theta$ satisfies the edge equations listed in Observation~\ref{obs:edgeeqs} where
$$
\iota\theta_\star s=\theta_\star s, \quad
\iota\theta_\star w_i^\prime=\theta_\star w_{p-i},\quad \text{and}\quad 
\iota\theta_\star w_i=\theta_\star w_{p-i}^\prime
$$
for $\star=R, B$, and $D$.

The first equation describes the angle sum around the red edge of $X_{p}$, which consists of all $R$ edges and the red diagonals of $w_0^\prime$ and~$w_p$.  The involution $\iota$ permutes these edges, thereby permuting the terms of the sum:
\begin{align*}
\left(\sum_{i=0}^{p-1} 2\iota\theta_R w_i^\prime\right) +\left(\sum_{i=1}^{p} 2\iota\theta_R w_i\right) +2\iota\theta_R s + \iota\theta_Dw_0^\prime+\iota\theta_Dw_p&=\\
\left(\sum_{i=1}^{p} 2\theta_R w_i\right) +\left(\sum_{i=0}^{p-1} 2\theta_R w_i^\prime\right) +2\theta_R s + \theta_Dw_p+\theta_Dw_0^\prime&=2\pi,\\
\end{align*}
so the first edge equation is satisfied by $\iota\theta$.  The terms in the next two sums, those for the degree-5 edges, are also permuted by~$\iota$, so those equations are satisfied by $\iota\theta$ as well.  

Something a little different happens with the degree-4 edges (only present when $p>1$).  To confirm the final equation of Observation~\ref{obs:edgeeqs}, for example, we need to examine
$$
\iota\theta_D s+\iota\theta_B w_{p-1}^\prime+\iota\theta_B w_{p-1}+\iota\theta_Dw_{p-2},
$$
but this sum is just
$$
\theta_D s+\theta_B w_1+\theta_B w_1^\prime+\theta_D  w_2^\prime,
$$
which equals $2\pi$ by the penultimate equation in Observation~\ref{obs:edgeeqs}.  In this instance, the involution takes the terms in one sum to the terms in another, effectively permuting the edge equations themselves.  The same happens for the remaining degree-4 equations.  
\end{proof}

\begin{cor}\label{cor:symmetryedgeeqs}
Let $\iota:\tau_{p}\rightarrow\tau_{p}$ be as in Proposition~\ref{prop:symmetry} and let $k$ be such that $p=2k$ if $p$ is even and $p=2k+1$ if $p$ is odd.  Positive angle structures $\theta\in\mathcal A(\tau_{p})$ with the property that $\iota\theta=\theta$ have $w_i^\prime\cong_\theta w_{p-i}$ and thus satisfy a simpler list of edge equations: 
\begin{align}
\left(\sum_{i=1}^{p} 4\theta_R w_i\right) +2\theta_R s + 2\theta_Dw_p&=2\pi\label{eq:deg4p+4}\\
2\theta_B w_p+2\theta_D w_1+\theta_B s&=2\pi\label{eq:deg5a}\\
2\theta_B w_p+2\theta_D w_{p-1}+\theta_B s&=2\pi\label{eq:deg5b}\\
\theta_D w_{i-1}+\theta_B w_{i}+\theta_B w_{p-i}+\theta_D  w_{p-(i+1)}&=2\pi&\text{ for } i=2, \dots k\label{eq:deg4a}\\
\theta_D w_{p-(i-1)}+\theta_B w_{i}+\theta_B w_{p-i}+\theta_D  w_{i+1}&=2\pi&\text{ for } i=1, \dots k\label{eq:deg4b}\\
\theta_D s+\theta_B w_{p-1}+\theta_B w_1+\theta_D  w_{p-2}&=2\pi.\label{eq:deg4c}
\end{align}
In addition,
\begin{align}
 \theta_D w_p=\theta_D s\quad\text{ and }\quad\theta_D w_i=\theta_D w_{p-i} \quad\text{ for } i=1, \dots k.\label{eq:diagonals}
\end{align}
These equations hold for all $p\ge1$, with one exception.  When $p=1$, Equation~\eqref{eq:deg5b} reads:
$
2\theta_B w_1+2\theta_D s+\theta_B s=2\pi.
$
\end{cor}

\begin{proof}
By assumption,
$\iota\theta_\star w_i^\prime=\theta_\star w_i^\prime$ for $\star=R, B$, and $D$, and, by definition, $\iota\theta_\star w_i^\prime$ also equals $\theta_\star w_{p-i}$, so $\theta_\star w_i^\prime=\theta_\star w_{p-i}$, and the tetrahedra $w_i^\prime$ and $w_{p-i}$ have the same angle assignments under~$\theta$, so $w_i^\prime\cong_\theta w_{p-i}$.  This isometry allows us to obtain Equations~\eqref{eq:deg4p+4}--\eqref{eq:deg4c}, by replacing $w_i^\prime$ with $w_{p-i}$ in the edge equations of Observation~\ref{obs:edgeeqs} and eliminating redundancies.  

To obtain Equation~\eqref{eq:diagonals} for $p=1$, replace $w_0^\prime$ with $w_1$ in the $p=1$ equation of Observation~\ref{obs:diagonaleqs}, which shows 
$$
\theta_D s-\theta_D w_1
    =\theta_D w_1-\theta_D s,
$$
so $\theta_D w_1=\theta_D s$.  
If $p>1$, Equations~\eqref{eq:deg5a} and~\eqref{eq:deg5b} imply that $\theta_D w_1$ equals $\theta_D w_{p-1}$, which, because of the isometry, equals $\theta_D w_1^\prime$, so the difference $\theta_D w_1-\theta_D w_1^\prime$ equals~0 as do all odd-index differences listed in Observation~\ref{obs:diagonaleqs}. Replacing $w_i^\prime$ with $w_{p-i}$, yields Equation~\eqref{eq:diagonals} for odd~$i$.  The remaining equations are derived differently depending on the parity of~$p$.  As noted in Observation~\ref{obs:diagonaleqs}, when $p$ is odd, all differences are equal (in this case, equal to~0), so, after replacing $w_i^\prime$ with $w_{p-i}$, Equation~\eqref{eq:diagonals} holds for all $i$ when $p$ is odd. To see that Equation~\eqref{eq:diagonals} also holds when $p$ and $i$ are even, note that
$$
\theta_D w_p-\theta_D s
   =\theta_D w_2-\theta_D w_2^\prime
    =\theta_D w_{p-2}-\theta_D w_{p-2}^\prime
    =\theta_D s-\theta_D w_0^\prime
    =\theta_D s-\theta_D w_p
$$
so $\theta_D s=\theta_D w_p$. Thus, all differences in Observation~\ref{obs:diagonaleqs} with even index are also~0 and  replacing  $w_i^\prime$ with $w_{p-i}$ results in Equation~\eqref{eq:diagonals}.
\end{proof}
