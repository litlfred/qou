---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-008-22-ideals-in-c
section_title: "Ideals in C"
section_number: 2.2
pages: 4-5
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.929
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
\label{SS:ideals} There are two closely related notions of an ideal within a ribbon category.  The first we discuss is used in \cite{GKP} and defined via objects.  We discuss the second notion in Section~\ref{SS:homideals}.   Note that here and elsewhere if $f$ and $g$ are morphisms, then we write $fg$ for the composition $f \circ g$.

\begin{definition}\label{D:ideal} We say a full subcategory $\ideal$ of a ribbon category $\cat$ is an \emph{ideal} if the following two conditions are met:
\begin{enumerate}
\item  If $V$ is an object of $\ideal$ and $W$ is any object of $\cat$, then $V\otimes W$ is an object of $\ideal$.
\item  $\ideal$ is closed under retracts; that is, if $V$ is an object of $\ideal$, $W$ an object of $\cat$, and if there exists morphisms $f:W \rightarrow V$, $g:V\rightarrow W$ such that $gf=\Id_W$, then $W$ is an object of $\ideal$.
\end{enumerate}
\end{definition} Trivially, if $\ideal$ consists of just the zero object or $\ideal = \cat$, then $\ideal$ is an ideal of the category.  We say an ideal $\ideal$ is a \emph{proper} ideal if it contains a nonzero object and is not all of $\cat$.
