---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-002-12-questions
section_title: "Questions"
section_number: 1.2
pages: 3-4
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.977
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Our results  above and their  comparisons with results about characterizing slopes raise many natural questions; we record a few of these here. The first asks whether we can upgrade our main result, Theorem \ref{thm:main}, to a statement about characterizing slopes:

\begin{question}
Is $0$ a characterizing slope for every L-space knot?
\end{question}

An affirmative answer   would follow from Theorem \ref{thm:main-lspace-zero} if one could show that  $0$-surgery, like the $0$-trace, detects whether a given knot is an L-space knot.

The class of ffpf knots contains but is much broader than the class of all nontrivial L-space knots, leading to the question below. Note that an affirmative answer would follow from Theorem \ref{thm:zero-surgery-fpf} if one could show that the 0-trace detects whether a knot is ffpf.

\begin{question}
Does the $0$-trace detect every ffpf knot?
\end{question}

One of the most important results on characterizing slopes is Lackenby's proof \cite{lackenby-characterizing} that every knot has one. On the other hand, Baker--Motegi showed in \cite{baker-motegi} that the knot $8_6$ has no \emph{integral} characterizing slope, which inspired the following question in the original version of this paper:

\begin{question}
Is every knot detected by at least one of its traces?
\end{question}

This question has since been answered in the negative by Baker--Kegel--Motegi in \cite{baker-kegel-motegi}.



Finally, our proof of Theorem \ref{thm:main} relies crucially on the fact that L-space knots are fibered with veering, fixed-point-free monodromy, as this guarantees that the closed monodromy has a unique fixed point such that the complement of the fiber over this fixed point recovers the knot complement. It is natural to ask whether there is an analogue of the ffpf condition for \emph{non-fibered} knots which guarantees something similar, for example:

\begin{question}
\label{ques:nonfibered}
Is there a condition on the knot Floer homology of a non-fibered hyperbolic knot $K\subset S^3$ which guarantees that there is  a pseudo-Anosov flow on $S^3_0(K)$ with exactly one orbit which generates the first homology of this surgery and whose complement recovers $S^3\setminus K$?
\end{question}

In \cite{baldwin-velavick}, Baldwin--Vela-Vick proved that if $K\subset S^3$ is a nontrivial fibered knot then \[\dim \hfkhat(K,g(K)-1) \geq \dim \hfkhat(K,g(K)) = 1.\] The ffpf condition is that this inequality is an \emph{equality}. So, perhaps the condition sought in Question \ref{ques:nonfibered} for a non-fibered knot $K$ is also that \[\dim \hfkhat(K,g(K)-1) = \dim \hfkhat(K,g(K)).\]
As noted in \cite{baldwin-velavick}, it is conjectured that the first is always greater than or equal to the second for non-fibered knots as well; this is still open.
