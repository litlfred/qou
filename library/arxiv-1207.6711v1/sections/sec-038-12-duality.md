---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-038-12-duality
section_title: "Duality"
section_number: 12
pages: 41-41
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.974
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:Duality}


In this section we make some observations about the relationship between the shape coordinates and the Ptolemy coordinates. Our observations suggest that there is a fundamental duality between the two sets of coordinates, which is interesting in its own right. We believe that this duality is a $3$-dimensional aspect of the duality (see Fock-Goncharov~\cite[p.~33]{FockGoncharov}) between $\mathcal A$-coordinates and $\mathcal X$-coordinates on higher Teichm\"{u}ller space of a simply connected Lie group (e.g.~$\SL(n,\C)$), respectively, its Langlands dual group (e.g.~$\PGL(n,\C)$).

Note that for each subsimplex, one shape parameter determines the other two. We single out one:

\begin{definition}
We call the parameters $z^{1100}_s$ \emph{shape coordinates}.
\end{definition}

As is customary for $n=2$, we can write the gluing equations entirely in terms of the shape coordinates. Let $\sub_n(\T)$ denote the set of all subsimplices of the simplices of $\T$.

\begin{observation}[Duality] The coordinates and their relations are parametrized by the following sets:
\begin{center}
\begin{tabular}{c|c}
Ptolemy coordinates & shape coordinates\\
$\dot\T_n(\Z)$ & $\sub_n(\T)$\\ \hline
Ptolemy relations & gluing equations\\
$\sub_n(\T$) & $\dot\T_n(\Z)$
\end{tabular}
\end{center}
In particular, we have
\begin{equation}\label{eq:Duality}
\begin{array}{rcl}
\#\mbox{\{Ptolemy coordinates\}} & = & \#\mbox{\{Gluing equations\}}\\
\#\mbox{\{Ptolemy relations\}} & = & \#\mbox{\{Shape coordinates\}}.
\end{array}
\end{equation}
\end{observation}

\begin{proposition}\label{prop:DualityTori}
If all boundary components of $M$ are tori, we have
\begin{equation}
\#\left\{\txt{Ptolemy\\ ~coord.}\right\}=\#\left\{\txt{Ptolemy\\relations}\right\}=\#\left\{\txt{Shape\\ ~coord.}\right\} =\#\left\{\txt{Gluing\\equations}\right\}=\binom{n+1}{3}t,
\end{equation}
where $t$ is the number of simplices of $\T$.
\end{proposition}
\begin{proof}
This follows immediately from Lemma~\ref{lemma:Rank}.
\end{proof}
