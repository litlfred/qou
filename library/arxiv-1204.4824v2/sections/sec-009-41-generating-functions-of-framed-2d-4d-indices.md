---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-009-41-generating-functions-of-framed-2d-4d-indices
section_title: "Generating functions of framed 2d-4d indices"
section_number: 4.1
pages: 19-20
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.935
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:gen-func}

The fundamental properties of $\fro'(L_{\wp,\vartheta}, a)$
are most elegantly expressed in terms of a formal generating function
$F(\wp,\vartheta)$.

The idea is to
introduce a formal variable $X_{\bar a}$ for each charge $\bar a \in \Gamma(z_1, z_2)$,
and then define
$ F(\wp,\vartheta) = \sum_{\bar a \in \Gamma(z_1,z_2)}  \fro'( L_{\wp,\vartheta},\bar a) X_{\bar a}$.
As we have noted in \S\ref{sec:tricky-sign}, though, we need to take some care here to deal with
sign ambiguities.  So more precisely, we introduce formal variables $X_a$ for each $a \in \tGamma(\tz_1, \tz_2)$,
subject to the relation that if $a$ and $a'$ project to the same class $\bar{a} \in \Gamma(z_1,z_2)$
then we have
\begin{equation} \label{eq:winding-rule-2}
 X_a / X_{a'} = (-1)^{w(a,a')}.
\end{equation}
We then choose one representative $a \in \tGamma(\tz_1,\tz_2)$ for each $\bar a \in \Gamma(z_1,z_2)$,
and define
\begin{equation}\label{eq:FLP-gen-prelim}
F(\wp,\vartheta) := \sum_{\bar a \in \Gamma(z_1,z_2)} \fro'( L_{\wp,\vartheta},a) X_{a}.
\end{equation}
$F(\wp,\vartheta)$ is independent of our choices of
representatives $a$, thanks to \eqref{eq:winding-rule-1}, \eqref{eq:winding-rule-2}.
