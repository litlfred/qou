---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-023-63-multiple-shocks
section_title: "Multiple shocks"
section_number: 6.3
pages: 38-39
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.847
latex_coverage_ratio: 0.977
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Next, let us comment on states perturbed by multiple precursors as in \eqref{eq:multiple-precursors}. As before, we will consider a compact boundary theory but this time perturbed $n$ spherically symmetric shock waves described by shifts $h_i\sim e^{ -\frac{2\pi}{\beta}(t_* \pm t_i )}$, with a ``$+$'' for $i$ odd and a ``$-$'' for $i$ even. We will also assume that all the shocks are strong, $h_i \gg 1$.  One can easily construct these geometries following the recipe of \cite{Shenker:2013yza}. In \cite{complexityshocks}, it was found that the total complexity of the state, using  CV-duality, is given by
\be
\CC \sim t_f - 2n_{sb}t_*, \qquad \text{(CV-duality)},
\ee
where $t_f$ is the length of the total time fold of the state, and $n_{sb}$ is the number of operators that are inserted at switchbacks.
A time fold is a convenient depiction of the construction of an out-of-time order state, such as \eqref{eq:multiple-precursors}. The total length of the time fold $t_f$ was defined in \cite{complexityshocks} as
\be
t_f \equiv |t_1-t_R| + |t_2 - t_1| + \dots |t_L - t_n|,
\ee
and it was assumed that $|t_i - t_{i+1}| > t_*$. We already discussed switchbacks in \S\ref{sec:one-shock}. From the perspective of the time fold, a switchback is an operator insertion where the time fold ``folds'' back on itself. An example time fold is shown in Fig.~\ref{fig-time-fold}. An insertion could fail at a switchback if the $(i+1)$th precursor in the state \eqref{eq:multiple-precursors} cancels against the time evolution of the $i$th precursor. See \cite{complexityshocks} for more details.

\begin{figure}
\begin{center}
\includegraphics[scale=.85]{time-fold.pdf}
\caption{A time fold with six operator insertions. This time fold depicts the construction of the out-of-time order state with six precursor insertions: $e^{-i H_L t_L}\,  W(t_6)W(t_5)W(t_4)W(t_3)W(t_2)W(t_1)\, e^{-i H_R t_R}\TFD$, where all the operators are understood to act on the left.
In this figure, all of the insertions except for $t_5$ occur at switchbacks.}\label{fig-time-fold}
\end{center}
\end{figure}



It's easy to see, following the procedure outlined \S\ref{sec:one-shock}, that the CA-duality reproduces this result. Let us prune the list of precursors so that only those at switchbacks are represented in the state \eqref{eq:multiple-precursors}. An example geometry with four shocks is shown in Fig.~\ref{fig-multiple-shocks}.
The gray ``postcollision'' regions are complicated and cannot be described by the $(u,v)$ coordinates. (For more details, see \cite{Shenker:2013yza}.) However, if the strengths of all of the shocks are strong $h_i \gg 1$, these regions become small and have vanishing action. The only contribution will be from the five-sided region $II$s. With $n$ shock waves, there will be $n+1$ five-sided region $II$s contributing to the action. The contribution of each one is given by \eqref{eq:action-region-II}, and the $i$th one (counting from the right) gives
\be
\CA_{i} = 2M\, \frac{\beta}{2\pi} \log h_{i-1} h_{i},
\ee
where we have abused notation so that $h_0 = v_0$, $h_{n+1} = u_0$, we have assumed $t_L, t_R >0$, and we have assumed an even number of shocks for simplicity. Summing over all regions, we get precisely that the action of the Wheeler-DeWitt patch grows as
\be
\CA_{n\textrm{\,shocks} } = 2M (t_f - 2n_{sb}t_*) \qquad \text{(CA-duality).}
\ee


\begin{figure}
\begin{center}
\includegraphics[scale=.70]{multiple-shocks.pdf}
\caption{Kruskal diagram of a geometry perturbed by four shock waves. The blue lines show the boundary of $\CW$, the shocks are drawn with double black lines, and the stars show their collisions. The intersection of $\CW$ and the Einstein-Rosen bridge is colored blue, green, and gray. The dominant contribution to the action is given by the five blue and green regions labeled $II$. The gray ``postcollision'' regions have negligible action. }\label{fig-multiple-shocks}
\end{center}
\end{figure}
