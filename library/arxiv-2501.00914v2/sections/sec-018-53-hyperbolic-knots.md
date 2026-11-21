---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-018-53-hyperbolic-knots
section_title: "Hyperbolic knots"
section_number: 5.3
pages: 27-28
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.969
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
In this subsection we determine when a fibered hyperbolic knot can have some surgery in common with a torus knot.

\begin{proposition} \label{prop:hyperbolic}
If $S^3_0(K) \cong S^3_0(T_{p,q})$ but $K$ is not isotopic to $T_{p,q}$, then $K$ is a fibered hyperbolic knot, and its monodromy is not veering.  In particular, neither $K$ nor its mirror is an L-space knot.
\end{proposition}

\begin{proof}
Since 0-surgery detects whether a knot is fibered \cite{gabai-foliations3}, and $T_{p,q}$ is fibered, we know that $K$ must be fibered as well.  Now if $K$ is not hyperbolic then it is either a torus knot or a satellite knot \cite[Corollary~2.5]{thurston-kleinian}.

If $K$ is a torus knot other than $T_{p,q}$, then Lemma~\ref{lem:torus-knots-different-0-surgery} says that $S^3_0(K) \not\cong S^3_0(T_{p,q})$.  Similarly, if $K$ is a satellite knot, then we cannot have $S^3_0(K) \cong S^3_0(T_{p,q})$.  Assuming otherwise, Lemma~\ref{lem:prelim-satellite-surgeries} says that the companion torus of $K=P(C)$ is incompressible in $S^3_0(K)$, so then $S^3_0(T_{p,q})$ must also be toroidal, whence $S^3_0(K) \cong S^3_0(T_{\pm2,3})$ by Lemma~\ref{lem:torus-surgery-essential}.  But then $K$ must be a genus-1 fibered knot, since it has the same $0$-surgery as another genus-1 fibered knot \cite{gabai-foliations3}, and we have a contradiction because the only genus-1 fibered knots are not satellites.

The only remaining possibility if $K\neq T_{p,q}$ is that it must be a fibered hyperbolic knot.  In this case, since $S^3_0(K) \cong S^3_0(T_{p,q})$ is small Seifert fibered, Corollary~\ref{cor:not-veering} tells us that the monodromy $h$ of $K$ cannot be veering, as claimed.  Moreover, if $K$ were an L-space knot then $h$ would have to be veering by Lemma~\ref{lem:ffpf-examples}, so $K$ cannot be an L-space knot.  Similarly, if the mirror $\mirror{K}$ were an L-space knot then its monodromy $h^{-1}$ would be veering, and then $h$ would be veering, so $\mirror{K}$ cannot be an L-space knot either.
\end{proof}

Proposition~\ref{prop:hyperbolic} has the following consequence, for which we recall that L-space knots have right-veering monodromy.

\begin{proposition} \label{prop:compare-hyperbolic-surgeries}
Let $T_{p,q}$ be a torus knot, and suppose there is some rational $r\in\Q$ and some fibered hyperbolic knot $K \subset S^3$ with right-veering monodromy such that $S^3_r(K) \cong S^3_r(T_{p,q})$.  Then $0 < r \leq 4g(K)$, and if $K$ is additionally an L-space knot then $r \neq 4g(K)$.
\end{proposition}

\begin{proof}
Write $g=g(K)$ for convenience.  We know that $S^3_r(T_{p,q})$ is always either reducible, a lens space, or small Seifert fibered \cite{moser}, so $S^3_r(K)$ is not hyperbolic.  Since $K$ is fibered and hyperbolic with right-veering monodromy, Ni \cite[Theorem~1.1]{ni-exceptional} proved that $0 \leq r \leq 4g$, and that $S^3_{4g}(K)$ is not a small Seifert fibered L-space.  Now Proposition~\ref{prop:hyperbolic} says that $K$ cannot have right-veering monodromy if $S^3_0(K) \cong S^3_0(T_{p,q})$, so we must have $r\neq 0$ as well.

In the case $r=4g$, we observe that $S^3_{4g}(K)$ is neither reducible nor a lens space.  Indeed, if we assume otherwise then its universal cover is not contractible, so it does not admit an essential lamination \cite[Theorem~6.1]{gabai-oertel}.  On the other hand, the monodromy of $K$ is pseudo-Anosov, and the suspension of its stable lamination has some degeneracy slope $d$, which satisfies either $|d| \leq 4g-2$ or $d=\frac{n}{0}$ for some integer $n\geq 1$ \cite[Theorem~8.8]{gabai-problems}.  Now by \cite[Theorem~5.3]{gabai-oertel} this suspension gives rise to an essential lamination on $S^3_{4g}(K)$ as long as $\Delta(d,4g) \geq 2$, so we must have $\Delta(d,4g) \leq 1$, hence $d = \frac{1}{0}$.  On the other hand, since $K$ has right-veering monodromy $h$, we know that the fractional Dehn twist coefficient $c(h) = \frac{1}{d}$ is strictly positive \cite[Proposition~3.1]{hkm-veering} and this is a contradiction.

Thus $S^3_{4g}(K) \cong S^3_{4g}(T_{p,q})$ implies that $S^3_{4g}(K)$ can only be small Seifert fibered.  If $K$ were an L-space knot, then all surgeries on $K$ of slope at least $2g-1$ would be L-spaces; but then $S^3_{4g}(K)$ would be a small Seifert fibered L-space, contradicting \cite{ni-exceptional} as mentioned above, so $K$ cannot be an L-space knot after all.
\end{proof}

Proposition~\ref{prop:compare-hyperbolic-surgeries} was the last remaining step in the proof of Theorem~\ref{thm:negtracetorus-restated}, so the latter proof is now complete. \hfill\qed
