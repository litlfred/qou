---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-019-5-testing-our-conjecture-with-static-shells
section_title: "Testing our conjecture with static shells"
section_number: 5
pages: 30-31
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.985
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:staticshells}
So far we have considered the complexification rate of an isolated black hole. We would like to test our proposal by adding controlled complications. One test is an ingoing shell (a shock wave), which will be considered in \S\ref{sec:shockwaves}; in this section we will instead consider a static shell (a Dyson sphere), see Fig.~\ref{fig-sarcophagus}.

\begin{figure}[h] 
   \centering
\hspace{2cm}    \includegraphics[width=3in]{fig-sarcophagus.pdf}
      \caption{A black hole surrounded by a static  sphere.}
      \label{fig-sarcophagus}
\end{figure}
Consider a static sphere at $r= \bar{r}$,  buttressed against collapse by its compressive strength. Outside the shell the metric is the Schwarzschild metric with mass $M + \delta M$,
\begin{equation}
ds^2  \Bigl|_{r> \bar{r}}=  - \left(1 - \frac{2G(M + \delta M)}{r}  + \frac{r^2}{\lads^2} \right) dt^2 + \frac{dr^2}{1 - \frac{2G(M + \delta M)}{r}  + \frac{r^2}{\lads^2} } + r^2 d \Omega_2^{\, 2 }.
\end{equation}
Inside the shell $r < \bar{r}$ the metric is the Schwarzschild metric with mass $M$ with a (locally unobservable) time dilation relative to infinity from being deep in the shell's gravitational well,
\begin{equation}
ds^2  \Bigl|_{r< \bar{r}} =  - {\frac{1 - \frac{2G(M + \delta M)}{\bar{r}}  + \frac{\bar{r}^2}{\lads^2}}{1 - \frac{2GM}{\bar{r}}  + \frac{\bar{r}^2}{\lads^2}}} \left(1 - \frac{2GM}{r}  + \frac{r^2}{\lads^2} \right) dt^2 + \frac{dr^2}{1 - \frac{2GM}{r}  + \frac{r^2}{\lads^2} } + r^2 d \Omega_2^{\, 2 }.
\end{equation}

Now let's calculate the action. The shell itself lies outside the horizon, and so only directly contributes to the time-independent (boost-invariant) part of the action. The only effect on the rate of change of action is indirect, through the change in the interior metric: the rate of change of action picks up exactly one gravitational time dilation factor,
\begin{equation}
\frac{d\CA}{dt_L} \Biggl|_\textrm{shell} = \sqrt{ {\frac{1 - \frac{2G(M + \delta M)}{\bar{r}}  + \frac{\bar{r}^2}{\lads^2}}{1 - \frac{2GM}{\bar{r}}  + \frac{\bar{r}^2}{\lads^2}}}} \frac{d \CA}{dt_L} \Biggl|_\textrm{no shell}.
\end{equation}
According to the action prescription, therefore, on the one hand, static shells do not compute, and, on the other hand, computers in gravitational wells slow down due to time dilation. Since both of these are exactly the behavior we would hope for, the proposal of Eq.~\ref{eq:CAformula} passes this test.

This argument applies to \emph{any} ordinary static matter outside the horizon---it does not compute to leading  order in $G$ and its only effect is that of gravitational time dilation, which is to slow the rate of computation of the black hole. This is consistent with the conjecture that an isolated  black hole is the fastest computer in nature.

Let us return now to the superconducting instability of charged black holes.
When the black hole becomes highly charged it will tend to expel charge into the atmosphere between the horizon and the AdS boundary. As discussed in Sec.\ref{sec:A Pattern}, the charge may then condense into a zero-entropy inert shell-like condensate. The remnant black hole at the center of the superconducting shell will not be close to extremality. Thus we will have an example of a far-from-extremal black hole surrounded by a static inert shell. The argument for static shells can be used to insure that the superconducting black holes do not violate the bound on computation.
