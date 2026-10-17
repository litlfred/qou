---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-022-63-traces-that-detect-knot-floer-homology
section_title: "Traces that detect knot Floer homology"
section_number: 6.3
pages: 31-32
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.869
latex_coverage_ratio: 0.956
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
We now combine the results of the previous sections to prove that the $n$-trace of any $T_{2,2g+1}$ recovers the knot Floer homology of any knot with the same $n$-trace.

\begin{proposition} \label{prop:lspace-trace-hyperbolic}
Fix $g \geq 1$, and suppose for some knot $K \subset S^3$ and integer $n \in \Z$ that $X_n(K) \cong X_n(T_{2,2g+1})$.  Then
\[ \hfkhat(K) \cong \hfkhat(T_{2,2g+1}) \]
as bigraded $\F$-vector spaces, and if $K$ is not isotopic to $T_{2,2g+1}$ then it is hyperbolic.
\end{proposition}

\begin{proof}
If $n\leq 0$ then $K=T_{2,2g+1}$ by Theorem~\ref{thm:negtracetorus}, so from now on we assume that $n \geq 1$.

Since $T_{2,2g+1}$ is an L-space knot, Theorem~\ref{thm:lspace-detection-main} says that $K$ must be an L-space knot of the same genus as $T_{2,2g+1}$, namely $g$.  Since the knot Floer homology of an L-space knot is completely determined by its Alexander polynomial \cite{osz-lens}, we will show that $\Delta_K(t) = \Delta_{T_{2,2g+1}}(t)$.

The identification of the $n$-traces restricts to a homeomorphism $S^3_n(K) \cong S^3_n(T_{2,2g+1})$ between their boundaries, which are rational homology spheres.  The surgery formula for the Casson--Walker invariant \cite{walker} says that
\[ \lambda(S^3_n(K)) = \lambda(S^3_n(U)) + \frac{1}{n}\frac{\Delta''_K(1)}{2} \]
and likewise for $\lambda(S^3_n(T_{2,2g+1}))$, so since these two invariants are equal we must have
\[ \frac{\Delta''_K(1)}{2} = \frac{\Delta''_{T_{2,2g+1}}(1)}{2}. \]
But Proposition~\ref{prop:casson-t2n} says that this is only possible if $\Delta_K(t) = \Delta_{T_{2,2g+1}}(t)$, as promised, and so the knot Floer homologies of $K$ and $T_{2,2g+1}$ coincide as well.

Supposing now that $K$ is not hyperbolic, it must be either a torus knot or a satellite knot \cite[Corollary~2.5]{thurston-kleinian}.  But if $K$ is an L-space knot with $\Delta_K(t) = \Delta_{T_{2,2g+1}}(t)$, then we know by Proposition~\ref{prop:satellite-t2n} that $K$ cannot be a satellite knot.  Thus it must be a torus knot, and in this case $\hfkhat(K) \cong \hfkhat(T_{2,2g+1})$ implies that $K = T_{2,2g+1}$ after all.
\end{proof}

This suffices to complete the proof of Theorem~\ref{thm:positive-trace-t2n}.

\begin{proof}[Proof of Theorem~\ref{thm:positive-trace-t2n}]
Suppose that $X_n(K) \cong X_n(T_{2,2g+1})$ but that $K$ is not isotopic to $T_{2,2g+1}$.  Then by Proposition~\ref{prop:lspace-trace-hyperbolic} we know that $K$ is a hyperbolic L-space knot of genus $g$, with $\hfkhat(K) \cong \hfkhat(T_{2,2g+1})$.  In particular, since $K$ is an L-space knot, it is fibered with right-veering monodromy.

Identifying the boundaries of the $n$-traces now gives us a homeomorphism
\[ S^3_n(K) \cong S^3_n(T_{2,2g+1}). \]
Since $K$ is a fibered, hyperbolic L-space knot, it has right-veering monodromy, and then Proposition~\ref{prop:compare-hyperbolic-surgeries} tells us that $0 < n < 4g$, as claimed.
\end{proof}
