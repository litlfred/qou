---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-024-64-localized-shocks
section_title: "Localized shocks"
section_number: 6.4
pages: 39-42
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.894
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Another generalization is to localize the precursor operators in the transverse space. In the context of scrambling these geometries were introduced in \cite{shock} and studied extensively in \cite{localshocks}. The $D=2+1$ case for a single localized precursor was also studied in purely two-dimensional CFT terms in \cite{Roberts:2014ifa}. Such a state is given by
\be
e^{-i H_L t_L}\, e^{-i H_R t_R}\, W_x(t_w) \TFD, \label{eq:sinlge-local-precursors}
\ee
where as usual $W_x(t_w) = e^{i H_L t_w}\, W_x\, e^{-i H_L t_w}$, and $W_x$ is a simple thermal scale operator localized on the boundary at spatial position $x$. In this case, the time fold of the operator insertion is position dependent. This is shown in Fig.~\ref{fig-localized-time-fold} for the state \eqref{eq:sinlge-local-precursors} with $t_L=t_R=0$. This also means that the strength of the shock wave dual to the operator insertion has a position dependent strength $h(x) \sim e^{\frac{2\pi}{\beta}(|t_w| - t_* - \mu|x|) }$, where $\mu$ is a positive constant and $|x|$ is the transverse distance from the shock. For more information, see \cite{localshocks}.

\begin{figure}
\begin{center}
\includegraphics[scale=.7]{position-dependent-time-fold.pdf}
\caption{A time fold for the state \eqref{eq:sinlge-local-precursors} with $t_L=t_R=0$. The length of the fold is dependent on position. The minimal tensor network for the state is given by fibering the time fold over the transverse space.}\label{fig-localized-time-fold}
\end{center}
\end{figure}

There are a few interesting differences in the complexity growth of the localized one-shock state and the spherically symmetric one-shock state. The early $|t_w|$ complexity growth is no longer linear in $t_w$.  This is because the operator can grow in spatial directions as well as the $N^2$ ``matrix'' directions, so the switchback effect now includes cancellations in the transverse space. A tensor network for a single localized precursor is shown in Fig.~\ref{fig-localized-tensor-network}. The precursor will grow ballistically with characteristic velocity $v_B$, which is known as the butterfly velocity \cite{shock,localshocks}. This velocity can be computed holographically for Einstein gravity, and for high temperatures is given by the dimension dependent formula \cite{shock,localshocks}
\be
v_B = \sqrt{\frac{D-1}{2(D-2)} }.
\ee
This spatial growth means that the tensor network Fig.~\ref{fig-localized-tensor-network} has the geometry of two solid cones. By considering the point (as a function of transverse coordinate $x$) where the boundary of $\CW$ moves off the singularity (e.g. the point $h(x)=v_0$ in Fig.~\ref{kruskal}) as a way of defining the geometry of the Wheeler-DeWitt patch, we find an exact match between the geometry of the tensor network shown in Fig.~\ref{fig-localized-tensor-network} and the geometry of $\CW$ inside the Einstein-Rosen bridge.

\begin{figure}
\begin{center}
\includegraphics[scale=.8]{position-dependent-tn.pdf}
\caption{A tensor network for the operator $W_x(t_w) = e^{i H_L t_w}\, W_x\, e^{-i H_L t_w}$. The red represents the evolution $e^{-i H_L t_w}$, the black dot represents the local insertion $W_x$, and the green represents the reverse evolution $e^{i H_L t_w}$. {\bf Left:} naive tensor network before cancellation. {\bf Right:} tensor network after cancellations outside the influence of the insertion $W_x$.}\label{fig-localized-tensor-network}
\end{center}
\end{figure}

On the other hand, if the spatial topology of the field theory is still compact, the precursor will eventually run out of room to grow. Once this saturation occurs, the growth with $|t_w|$ will transition to being linear. However, in this case there is an additional delay in the growth as compared to \eqref{eq:one-shock-complexity-strong-shock} related to the size of the spatial boundary and time it takes for the operator to saturate. (Se, e.g. the caption in Fig.~11 in \cite{localshocks}.)

The spatially compact boundary situation is slightly complicated by the fact that the shock will collide with itself on the other side of the transverse sphere. Instead, let us consider the planar-AdS black hole geometry. Since the strength of the shock is position dependent, the action in $\CW$ is no longer simply linear in $t_w$. Let us match this action to the volume of the tensor network describing the state. Let $m$ be the energy density, $L$ the infinite length of a transverse direction, and $M = mL^{D-2}$ the total energy. Using the techniques of \S\ref{sec:one-shock}, it's not hard to show that the total action is
\be
\CA = 2M(t_L + t_R) +  \frac{4 m v_B^{D-2} (|t_w| - t_* - t_R)^{D-1}}{(D-1)(D-2)    }, \label{eq:one-precursor-complexity}
\ee
which is consistent with both the result from  CV-duality and the tensor network predictions of \cite{localshocks}. In particular, with $t_L = t_R=0$, the second term is exactly the volume of the two solid $D-1$-dimensional cones shown in Fig.~\ref{fig-localized-tensor-network}.

One can also consider states perturbed by multiple localized precursors
\be
e^{-i H_L t_L}\, e^{-i H_R t_R}\, W_{x_n}(t_{n}) \dots W_{x_1}(t_1) \TFD. \label{eq:multiple-localized-precursors}
\ee
The analysis is annoyingly complicated and does not provide any additional insight into the complexity equals action conjecture. Instead, we will simply state that all of the results from  CV-duality from \cite{localshocks} carry over. We can construct the tensor network by fibering the time fold for the state over the transverse directions \cite{localshocks}. As mentioned, we can determine the geometry of $\CW$ by considering the point (as a function of transverse coordinate $x$) where the boundary of $\CW$ moves off the singularity. This lets us find an exact match between the geometry of the tensor network that constructs the state \eqref{eq:multiple-localized-precursors} and the geometry of $\CW$ inside the Einstein-Rosen bridge.
