---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-005-15-strategy-and-outline-of-the-paper
section_title: "Strategy and outline of the paper"
section_number: 1.5
pages: 5-6
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.969
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:strategy}
In Section~\ref{sec:distortion} we analyze the effects
of the smallness
condition on local distortion  on general
closed, path-connected subsets $M\subset\R^n$. For 
each $x$ near (but not in) $M$ we find
a direction that ``points away from $M$''. These
directions are glued together in Section~\ref{sec:pseudo}
with a partition of unity to construct a kind of
pseudo-gradient vector field for the distance function $\dist(\cdot,M)$.  We solve
uniquely and globally two different flow equations with respect
to this vector field to define homotopies in the complement
$\R^n\setminus M$ of $M$. These mappings are then used in Section~\ref{sec:iso} 
for $M:=M_1$ and $M_2$ in combination with the sets' 
controlled local distortion
to construct  an
isomorphism between the fundamental groups
$\pi_1(\R^n\setminus M_1)$ and $\pi_1(\R^n\setminus M_2)$ as stated in 
Theorem~\ref{thm:isomorphic}. 

We use in Section~\ref{sec:stability} the immediate Corollary
\ref{cor:equiv-knots} to prove the Lipschitz stability and fractional stability
of knot equivalence, i.e., Corollaries \ref{cor:lipschitz-stability} and
\ref{cor:fractional-stability}. The first one relies on the fact that for curves the smallness condition on local 
distortion  
is stable with respect to Lipschitz perturbations. 
For
the fractional stability we recall in Corollary \ref{cor:seminorm-bilip}
that a small local fractional semi-norm of the
tangent implies a local bilipschitz estimate, which can be turned into a local
distortion bound for embeddings.

More analytical work is required for the existence
of symmetric $\emob$-critical prime knots as stated in
Theorem~\ref{thm:symm-crit-prime}. Since minimizing sequences converge only
weakly in $W^{\frac32,2}$ to a 
limit curve, we can \emph{not} relie on the (strong) 
$W^{\frac32,2}$-stability of Corollary \ref{cor:fractional-stability} to
guarantee the prescribed knot equivalence class in the limit. Nevertheless, 
the limiting
curve $\g$ has finite M\"obius energy because of the energy's lower-semicontinuity, 
so that we have
an arclength parametrized tame
$W^{\frac32,2}$-knot $\g$ as a limit. Exactly as in the proof of
Corollary \ref{cor:fractional-stability} we therefore find a scale  at which
$\g$ has its local distortion strictly
below the universal constant
$g_3$. The same holds true for all members of
the minimizing sequence, because each of them is an arclength parametrized
$W^{\frac32,2}$-knot as well. But the $L^\infty$-convergence of that sequence
towards $\g$ might be too slow to satisfy the assumptions of Corollary \ref{cor:equiv-knots}
for any sequence member.
In other words, the scales at which 
the members of the minimizing sequence have local 
distortion below $g_3$
might decay to zero much faster than their $L^\infty$-distance to $\g$. 
The analytic reason for that behaviour lies in the fact that we do \emph{not}
have uniform absolute continuity of the integrals defining the fractional
semi-norms of the tangents of the minimizing sequence. So, we are led to 
study possible concentrations in these semi-norms to cut them out, and replace
the corresponding subarcs of the curves by straight segments. Since such a substitution
generally destroys the $W^{\frac32,2}$-regularity\footnote{\label{foot:harmonic-substitution}For arclength parametrized embedded curves, $W^{\frac32,2}$-regularity is equivalent to finite Möbius energy according to~\cite{blatt_2012a}.
Due to~\cite[Corollary~1.3]{freedman-etal_1994}, such a curve has a local bilipschitz constant (cf.\@ Footnote~\ref{foot:bilip}), arbitrarily close to~$1$.
However, replacing a subarc of a curve 
by a line is likely to produce sharp corners at its endpoints
which results in a bilipschitz constant strictly larger 
than~$1$.},
a careful analytic
investigation of that
procedure based on some subtle BMO-type estimates
is required in order to keep the local
distortion of these modified curves under control. This analysis is carried out
in Section~\ref{sec:harmonic}.

In Section~\ref{sec:compactness} we interpret
the fractional semi-norms of sequences of $W^{\frac32,2}$-knots as Radon measures
on $\R/\Z\times\R/\Z$ to pass to a weak limiting  Radon measure in order to analyze
its set of concentration points.  At  a carefully chosen scale around these 
concentration points we apply the cutting procedure of 
Section~\ref{sec:harmonic}
to members of the minimizing sequence with sufficiently large
index. The result
is a weak fractional compactness theorem in the set of symmetric, arclength 
parametrized $W^{\frac32,2}$-knots (see Theorem~
\ref{thm:fractional-compactness}), which
might be of independent interest. This is the main tool in the existence proof
for symmetric $\emob$-minimizing knots in Section~\ref{sec:symm-critical}. A simple
symmetrization argument which  uses the invariance of the M\"obius energy under rotations
then leads to the fact that these minimizing knots are also critical points for
$\emob$, and therefore are real analytic. This
finalizes the proof of Theorem~\ref{thm:symm-crit-prime}.
