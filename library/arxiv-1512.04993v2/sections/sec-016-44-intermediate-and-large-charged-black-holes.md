---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-016-44-intermediate-and-large-charged-black-holes
section_title: "Intermediate and large charged black holes"
section_number: 4.4
pages: 24-28
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
The situation for intermediate-sized  ($r_+ \sim \lads $) and large charged black holes ($r_+ \gg \lads $) is more complicated and leads to an apparent  violation of  the complexification bound Eq.~\ref{C-bound}. Let us consider the phase diagram in Fig.~\ref{fig-largechargedblackholes}. There are a number of important curves in the $(M,Q)$ diagram. The first  represents black holes at extremality. The extremality curve can be described by the parametric equations,
\bea
G^2M^2 \biggl|_\textrm{extremal} &=&\frac{\lads^2}{27}  (G\mu^2-1)(2G\mu^2 +1)^2 \cr \cr
Q^2 \biggl|_\textrm{extremal} &=& \frac{\lads^2}{3} \mu^2  (G\mu^2-1).
\eea
For small black holes it has the usual asymptotically flat form
\be
Q \biggl|_\textrm{extremal} =\sqrt{G}M.
\ee


The second class of curves shown in Fig.  \ref{fig-largechargedblackholes} are curves of constant chemical potential. The curves behave differently for $\sqrt{G}\mu<1$ and $\sqrt{G}\mu >1.$ The curve $ \sqrt{G}\mu=1 $  ends at $M=Q=0 $ where it is tangent to the extremal curve. For $\sqrt{G}\mu<1$ the constant-$\mu$ curves all end at $M=Q=0$, namely the AdS ground state. This is the minimum of $M - \mu Q$ for fixed $\mu < G^{-1/2}$.

For $\sqrt{G}\mu >1$ the constant-$\mu$ curves end on the extremal curve at some nonzero values of $M$ and $Q$. Where they intersect, the constant-$\mu$ curve and the extremal curve are tangent.  In these cases the nominal ground state at fixed  $\mu$ is the extremal black hole, which has $M - \mu Q$ negative.

\begin{figure}[h!]
\begin{center}
\includegraphics[width=4.5in]{fig-largechargedblackholes.pdf}
\caption{The phase diagram for charged Reissner-Nordstrom black holes in AdS. {\bf Top pane}: at fixed $M$, black holes exist only for small enough $Q$. For  black holes that are small compared to $\lads$, the extremal line is $Q=\sqrt{G} M$; for black holes that are large compared to $\lads$, the extremal line becomes $Q \sim M^{1/3}$. {\bf Middle pane}: curves of constant chemical potential $\mu$. Small extremal black holes have $\sqrt{G} \mu = 1$; larger extremal black holes have larger $\mu$. Thus for $\sqrt{G}  \mu < 1$ the lines of constant $\mu$ end at $M = Q = 0$, and for $\sqrt{G}  \mu > 1$ the lines of constant $\mu$ end on the extremal line. {\bf Bottom pane}: for a given large charged black hole (red star),  we may define $M_\mu$ (gray star) as the mass of the extremal black hole with the same chemical potential $\mu$, and $M_Q$ (blue star) as the mass of the extremal black hole with the same charge $Q$.}


\label{fig-largechargedblackholes}
\label{extremal-curve}
\end{center}
\end{figure}






\subsubsection{The case $\sqrt{G}\mu<1$}
For $\sqrt{G}\mu<1$, the ground state is at $M=Q=0$ so that there is no apparent reason for a ground state subtraction. Comparing the action growth with the complexification bound, we find that for any mass and nonzero charge, the bound is violated. The violation gets worse for larger $\mu$, so the worst case in this regime is at $\sqrt{G}\mu=1.$  One finds that along this curve
\be
\sqrt{G} \mu = 1: \ \ \ \ \ 2(M-\mu Q)  - 2(M-\mu Q)_\textrm{gs} = 2(M-\mu Q) =  \frac{\sqrt{G}Q^3}{\lads^2} \label{eq:muis1bound}.
\ee
On the other hand the calculation of $\frac{1}{\pi \hbar}\frac{d\CA\textrm{ction}}{dt}$ in Eq.~\ref{eq:chargedactionincrement} exceeds the bound in \eqref{eq:muis1bound} by a modest factor. In Fig.~\ref{fig-violationformuis1} we show the ratio of the calculated rate of action growth to the bound given by \eqref{eq:muis1bound}. We see that for large $Q$ the ratio is close to unity, but that for small $Q$ there is a  significant $O(1)$ violation.  We will return to this apparent violation after considering the case $\sqrt{G} \mu>1.$


\begin{figure}[htbp] 
   \centering
   \includegraphics[width=3.3in]{fig-violationformuis1.pdf}
   \caption{The rate of growth of action, Eq.~\ref{eq:chargedactionincrement}, divided by the bound of Eq.~\ref{eq:muis1bound}, along the line $\sqrt{G} \mu = 1$. The bound is violated everywhere along this line. For large $\mu =1$ black holes, the bound is violated by a small relative amount. For small $\mu = 1$ black holes, the black holes are almost extremal and  the bound is violated by a factor of 3. (Notice the subtle order of limits involved in keeping $\mu = 1$ for small black holes. If you first take $\lads \rightarrow 0$ then the bound is never violated, as in \S\ref{sec:smallchargedblackholescomplexity}: the extremality and ``small'' limits don't commute.)}
   \label{fig-violationformuis1}
\end{figure}


\subsubsection{The case $\sqrt{G}\mu>1$}
In the case of large charged AdS black holes, there is a serious mismatch between the action calculation and the complexity expectation.  
The mismatch is most easily seen for very large black holes ($r_+ \gg \lads$) in the near extremal limit.


Consider very large ($r_+ \gg \lads$) charged black holes in $D=4$ spacetime dimensions, for which
\be
f(r)= \frac{r^2}{\lads^2} - \frac{2GM}{r} + \frac{GQ^2}{r^2} \ \ \ \& \ \ \  \mu = \frac{Q}{r_+}.
\ee
Extremality occurs at
\be
Q^2_\textrm{ext} = \frac{3\lads^2}{G}\left(  \frac{GM}{2\lads}      \right)^{4/3}=\frac{G\lads^2\mu^4}{3}.
\label{extr-curv}
\ee
The extremal $Q$ for a given $M$, Eq.~\ref{extr-curv},  defines a curve in the $M,Q$ plane  and is plotted in Fig.~\ref{fig-largechargedblackholes}.













Along the extremal curve the chemical potential is equal to the inverse slope. In other words, the contours of constant $\mu$ are tangent to the extremal curve,
\be
\frac{dM}{dQ} \biggl|_\textrm{extremal} = \mu.
\ee

After some straightforward calculations, one can see (assuming the ground state is given by the extremal black hole) that near extremality,
\be
(M-\mu Q)-(M-\mu Q)_\textrm{gs}=

2(M-M_Q) + O(M-M_Q)^2. \label{eq:mismatch11}
\ee


In Eq.~\ref{3.15}  \rm
we found that in that limit the rate of change of action is
\be
\frac{d \CA}{dt} = \sqrt{6} \sqrt{M_{Q}(M-M_{Q})} + O(M - M_Q) .
\label{eq:mismatch22}
\ee
Near extremality Eq.~\ref{eq:mismatch22} is much bigger than Eq.~\ref{eq:mismatch11}, apparently violating the bound. In this case the apparent relative violation is not by an $O(1)$ factor but becomes infinite as extremality is approached.



Thus the action proposal apparently violates the complexification bound. It is worth pointing out that this puzzle is not specific to the new CA proposal. It occurs in essentially the same form in the older CV proposal.
