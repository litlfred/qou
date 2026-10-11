---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-055-128-summary
section_title: "Summary"
section_number: 12.8
pages: 408-409
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
text_source: latex
latex_prose_ratio: 0.811
latex_coverage_ratio: 0.926
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We have proudly completed the proof of Theorem \ref{Seifert:geometrisation:teo}. We state that theorem again here:

\begin{teo} 
A closed orentable 3-manifold has a geometric structure modelled on one of the following six geometries:
$$S^3,\ \matR^3,\ S^2\times \matR,\ \matH^2\times \matR,\ \Nil,\ \widetilde{\SL_2}$$
if and only if it is a Seifert manifold of the appropriate commensurability class, as prescribed by Table \ref{Seifert:geometry:table}. It has a $\Sol$ geometric structure if and only if it is a torus (semi-)bundle of Anosov type.
\end{teo}

We can deduce that the eight geometries are mutually exclusive:

\begin{prop}
Two closed 3-manifolds admitting different geometries are not diffeomorphic, and not even commensurable.
\end{prop}
\begin{proof}
We already know that the six Seifert geometries form six distinct commensurability classes. A manifold of type $\Sol$ is not Seifert by Proposition \ref{torus:bundle:prop}. A closed hyperbolic manifold is neither Seifert nor Sol because its fundamental group is infinite and does not contain an infinite normal abelian subgroup by Corollary \ref{normal:abelian:cor} (as opposite to the other geometries, see Proposition \ref{infinite:K:prop}).

Two manifolds having different geometries cannot be commensurable, since a common finite cover would inherit both geometries. 
\end{proof}

In fact one can tell the geometry of the manifold directly from its fundamental group. 

\begin{prop}
Let $M$ be a closed manifold modelled on one $\matX$ of the eight geometries; this flowchart shows how to determine $\matX$ from $\pi_1(M)$:
\begin{itemize}
\item if $\pi_1(M)$ is finite, then $\matX = S^3$; otherwise
\item if $\pi_1(M)$ is virtually cyclic, then $\matX = S^2\times \matR$; otherwise
\item if $\pi_1(M)$ is virtually abelian, then $\matX = \matR^3$; otherwise
\item if $\pi_1(M)$ is virtually nilpotent, then $\matX = \Nil$; otherwise
\item if $\pi_1(M)$ is virtually solvable, then $\matX = \Sol$; otherwise
\item if $\pi_1(M)$ contains a normal cyclic group $K$, then:
\begin{itemize}
\item if a finite-index subgroup of the quotient lifts, then $\matX = \matH^2 \times \matR$, 
\item otherwise $\matX = \widetilde{\SL_2}$; 
\end{itemize}
\item otherwise $\matX = \matH^3$.
\end{itemize}
\end{prop}
\begin{proof}
The virtually abelian cases were settled in Section \ref{virtually:abelian:subsection}. The $\Nil$ and $\Sol$ geometries were considered by Corollaries \ref{Nil:is:Nil:cor} and \ref{Sol:not:Nil:cor}. 

If $\matX = \matH^2\times \matR$ or $\widetilde{\SL_2}$ then 
$\pi_1(M)$ surjects onto $\pi_1(S)$ for some closed hyperbolic surface $S$. 
This implies that $\pi_1(M)$ is not solvable, for otherwise
(by Propositions \ref{subgroup:prop} and \ref{solvable:normal:prop})
the group $\pi_1(S)$ would also be, and hence it would contain a normal cyclic subgroup, contradicting Corollary \ref{normal:abelian:cor}.

If $\matX = \widetilde{\SL_2}$ then $\pi_1(S) = \pi_1(M)/_K$ and no finite-index subgroup of $\pi_1(S)$ can lift to $\pi_1(M)$ by Proposition \ref{SL2:no:lift:prop}.

Finally, if $\matX=\matH^3$ then $\pi_1(M)$ contains no normal cyclic group $K$ by Corollary \ref{normal:abelian:cor} again.
\end{proof}

The boundary case is slightly different. Of the eight geometries, only three produce non-compact finite-volume complete orientable manifolds:
$$\matH^3,\ \matH^2 \times \matR,\ \widetilde{\SL_2}.$$
These non-compact finite-volume manifolds are diffeomorphic to the interior of a compact manifold $M$ with boundary consisting of tori.

\begin{teo}
Let $M$ be a compact orientable 3-manifold with boundary consisting of tori. The following are equivalent:
\begin{itemize}
\item $M$ has a finite-volume complete $\matH^2 \times \matR$ structure,
\item $M$ has a finite-volume complete $\widetilde{\SL_2}$ structure,
\item $M$ is Seifert with $\chi<0$.
\end{itemize}
\end{teo}

In contrast with the closed case, a non-closed $M$ may admit two different geometric structures of Seifert type. On the other hand, a manifold $M$ cannot admit both a hyperbolic and a Seifert structure.
