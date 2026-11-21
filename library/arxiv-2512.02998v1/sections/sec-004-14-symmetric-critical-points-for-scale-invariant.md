---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-004-14-symmetric-critical-points-for-scale-invariant
section_title: "Symmetric critical points for scale-invariant knot energies"
section_number: 1.4
pages: 4-5
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
The fractional Sobolev space $W^{\frac32, 2}(\R/\Z,\R^3)$ is the natural
energy space for  the 
\emph{M\"obius energy}
\begin{equation}\label{eq:emob}
E_\textnormal{M\"ob}(\g):=\int_{\R/\Z}\int_{\R/\Z}\left(
\frac1{|\g(s)-\g(t)|^2}-
\frac{1}{d_\g(\g(s),\g(t))^2}\right)|\g'(s)||\g'(t)|\,dsdt.
\end{equation}
Indeed, an arclength parametrized
curve $\g:\R/\Z\to\R^3$ has finite M\"obius energy  

if and only if 
$\g$ is embedded and of
class $W^{\frac32,2}(\R/\Z,\R^3)$ as shown in \cite{blatt_2012a} 
(see 
\cite[Theorem~3.2 (i)]{gilsbach-vdm_2018} for an explicit a priori bound
on the fractional seminorm in terms of  the energy). 
Freedman et al.\@ managed to
use the M\"obius invariance of $\emob$ to find minimizing knots in any given prime
knot class \cite[Theorem~4.3]{freedman-etal_1994}.
Critical points of the M\"obius energy were
shown to be smooth and even real-analytic 
\cite{blatt-etal_2016,blatt-vorderobermeier_2019} 
without using the invariance of $\emob$ under 
M\"obius transformations. 
But how can we find critical knots  possibly different from the absolute minimizers? 
One option is to use symmetry as carried out in \cite{gilsbach-vdm_2018} for 
O'Hara's
energies above scale-invariance whose energy spaces \emph{do} 
embed into $C^1$.

As in that 
paper we consider here for the M\"obius energy a discrete rotational symmetry. To be
more precise, for $p\in\N$, $p\ge 2$, we call a 
curve $\g\in C^0(\R/\Z,\R^3)$
\emph{($p$-rotationally) symmetric} if and only if
\begin{equation}
\label{eq:rot-symm}
\textstyle
\Rot_{\frac{2\pi}p}\circ\g(s -\frac1{p})=\g(s)\quad\Foa s\in\R/\Z, 
\end{equation}
where $\Rot_{\beta}\in SO(3)$ denotes the rotation about a fixed axis, say,
the $e_3$-coordinate axis, with rotation angle $\beta$.
Define for a given knot equivalence class $\mathcal{K}$ the 
\emph{($p$-rotationally) symmetric
subset}
\begin{equation}\label{eq:symmetric-subset}
\Sigma_p(\mathcal{K}):=\{\eta\in C^{0,1}(\R/\Z,\R^3):|\eta'|>0
\,\,\textnormal{a.e.},\, [\eta]=\mathcal{K},\,
\eta\,\,\textnormal{satisfies}\,\eqref{eq:rot-symm}\}.
\end{equation}
\begin{theorem}[Symmetric critical prime knots]
\label{thm:symm-crit-prime}
If the symmetric subset $\Sigma_p(\mathcal{K})$
of a prime knot equivalence class $\mathcal{K}$ contains a knot with
finite M\"obius energy or, equivalently, a 
$W^{3/2,2}$-knot,
then
there exists an arclength parametrized knot $\g\in C^\omega(\R/\Z,\R^3)
\cap\Sigma_p(\mathcal{K})$
such that
\begin{equation}\label{eq:minimizing}
\emob(\g)=\inf_{\Sigma_p(\mathcal{K})}\emob(\cdot),
\end{equation}
and  $\g$ is a critical knot, i.e., $d\emob (\g)[h]=0$ for all
$h\in W^{\frac32,2}(\R/\Z,\R^3)$. Moreover,
all torus knot classes $\mathcal{T}(a,b)$ for co-prime $a,b\in\Z\setminus\{0,\pm 1\}$
contain at least two different critical knots for the M\"obius energy.
\end{theorem}

One may prove a similar result for other scale-invariant knot energies
with energy spaces $W^{1+1/p,p}$
such as those from O'Hara's family; cf.\@ \cite{ohara_1992a,
blatt-etal_2022b}.

It might be easier to check the symmetries for polygonal
curves, so instead of a knot with finite M\"obius energy
we might require in Theorem \ref{thm:symm-crit-prime} that
$\Sigma_p(\mathcal{K})$ contains a polygonal knot.
Indeed, 
smoothing the corners such that the symmetry is preserved 
yields an immersed embedded smooth
curve in $\Sigma_p(\mathcal{K})$
which has finite Möbius energy due 
to~\cite{blatt_2012a} and the energy's invariance under reparametrization. We do not know, on the other hand, if it suffices
to assume in Theorem \ref{thm:symm-crit-prime} only
that $\mathcal{K}$ is tame and that
$\Sigma_p(\mathcal{K})$ is nonempty.



We mentioned before that two equivalent arclength parametrized tame
knots $\g_1,\g_2:\R/\Z\to\R^3$ are either already ambiently isotopic, or
$\g_1$ is ambiently isotopic to the mirror image $\g_2^*$ of $\g_2$.
The $O(3)$-invariance of the M\"obius energy therefore
allows us to 
strengthen Theorem~\ref{thm:symm-crit-prime} to ambient isotopy
classes.
\begin{corollary}[Symmetric critical prime knots in ambient isotopy
classes] \label{cor:symm-crit-prime}
Let $\mathcal{K}$ be an ambient isotopy class of prime knots and $\Sigma_p(\mathcal{K})$ be the class of $p$-rotationally symmetric regular Lipschitz
curves whose ambient isotopy class equals $\mathcal{K}$. If
$\Sigma_p(\mathcal{K})$ contains a knot of
finite M\"obius energy, then there is an arclength parametrized
minimizing real analytic knot in $\Sigma_p(\mathcal{K})$ such that
\eqref{eq:minimizing} holds, and this knot is $\emob$-critical. If,
more specifically,
$\mathcal{K}$ equals the ambient isotopy class of torus knots,
$\mathcal{T}(a,b)$ for co-prime $a,b\in\Z\setminus\{0,\pm 1\}$, then there
are at least two such $\emob$-critical knots.
\end{corollary}
Kim and Kusner use in \cite{kim-kusner_1993}
symmetric criticality to construct $\emob$-critical torus 
knots (even with explicit formulas for their energy values). 
Their numerical experiments suggest, that
for (co-prime) parameters $a,b$ with $|a|,|b|>2$ 
these critical
points seize to be stable. Analytically, this remains an
open question.
