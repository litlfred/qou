---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-014-34-zero-traces-of-l-space-knots
section_title: "Zero-traces of L-space knots"
section_number: 3.4
pages: 19-19
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.812
latex_coverage_ratio: 1.0
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
We conclude this section by proving our main result, Theorem~\ref{thm:main}, which asserts that every L-space knot is detected by its $0$-trace. 

\begin{proof}[Proof of Theorem~\ref{thm:main}]
Suppose that $K$ is an L-space knot, and that $X_0(J) \cong X_0(K)$.  Then since Theorem~\ref{thm:trace-large-surgery} says that the diffeomorphism type of the 0-trace determines whether or not a given knot is an L-space knot, we see that $J$ must be an L-space knot as well.  Now both $J$ and $K$ are ffpf by Lemma~\ref{lem:ffpf-examples}, and comparing the boundaries of the $0$-traces tells us that $S^3_0(J) \cong S^3_0(K)$, so we conclude by Theorem~\ref{thm:zero-surgery-fpf} that $J=K$.
\end{proof}

The following can also be proved by exactly the same argument.

\begin{theorem} \label{thm:almost-l-space-zero}
If $K$ is an almost L-space knot of genus at least $3$, then $X_0(K)$ detects $K$.
\end{theorem}
