---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-038-829-very-early-times
section_title: "Very early times"
section_number: 8.2.9
pages: 53-55
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Throughout this paper we have generally been considering the rate of complexification at times that are neither too early nor too late.

At early times, the rate of the increase of action is slow. For example, for the uncharged black hole in $D > 3$, $d\CA/dt$ is zero when $t_R = t_L = 0$, and remains zero up until the past light sheets first cross; it then grows,  asymptoting to the answer quoted in Eq.~\ref{eq:unchargedactionincrement}.

\begin{figure}[htbp] 
   \centering
   \includegraphics[width=5in]{fig-earlytimes.pdf}
   \caption{At early times, the action of the WDW patch of a neutral AdS black hole does not change with time. The action starts to increase only after enough time has passed that the light sheets cross.  The critical moment at which the action starts to increase is shown on the right.}
   \label{fig:earlytimes}
\end{figure}

So long as the ingoing light sheets don't meet before they hit the singularity, there are two separate time translation symmetries: a $t_L$ symmetry and a $t_R$ symmetry. Once the two light sheets meet, these two symmetries break to a single overall time translation symmetry in $t_L + t_R$. It is only then that the action can start growing. This is shown in Fig.~\ref{fig:earlytimes}. (This fact is particularly obvious from the perspective of the ``past wedge'' calculation of Appendix~\ref{sec:pastwedge}.)

The period of constant action  exists because the singularity of an AdS black hole bows in for $D \geq4$ \cite{Fidkowski:2003nf}; for small black holes the action begins to increase after about an AdS time (which can be very long compared to the Schwarzschild time), and for large black holes it increases after about a thermal time. (This effect is absent for one-sided black holes that form from the collapse of a null shell---in that case the complexity starts to increase the moment the shell is emitted from the boundary.)

If CA-duality can be trusted on time scales this short, it would be interesting to develop a CFT understanding of why the holographic dual does not immediately begin complexifying. For large black holes, this would involve understanding the reference state relative to which the computational complexity is defined. At late times it suffices to consider the reference state to be the thermofield double state, but the deviation from linear growth at early times suggests that there may be a more primitive reference state from which the thermofield double state and the $(t_L + t_R)=\lads/2$ state will be the same complexity distance. (We will return to this issue in \cite{ToAppear}.)

For small black holes it may be harder to understand the early time behavior because even outside the context of complexity small black holes are not holographically well understood.
