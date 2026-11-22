---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-021-122-rindler-time-and-cv
section_title: "Rindler Time and CV"
section_number: 12.2
pages: 41-43
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.994
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The standard architecture for quantum circuits (explained in Lecture I) is illustrated in figure \ref{cirkuit}.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.4]{cirkuit.pdf}
\caption{}
\label{cirkuit}
\end{center}
\end{figure}
We assume that the circuit comes equipped with a clock, and in each time-step $K/2$ gates act. For sub-exponential time the number of gates in a circuit corresponds to the complexity\footnote{This is the no-collisions assumption discussed at length in Lecture I. It is expected to be correct for sub-exponential time.} $\CC$ of the unitary operator prepared by the circuit satisfies,
\be 
\frac{d\CC}{\d\t} = \frac{K}{2}
\ee
or, assuming $K\sim S$,
\be 
\frac{d\CC}{\d\t} \sim S.
\label{dC-dtau=S}
\ee


If  black holes can be viewed as quantum circuits one may ask what the time-coordinate $\tau$ corresponds to on the black hole side. One hint is that since complexity and entropy are dimensionless, $\tau$ is also dimensionless. The ordinary Schwarzschild coordinate $t$ of a black hole has dimensions of time and therefore cannot be the same as $\t.$ There is however a universal dimensionless time for all non-extremal black holes, namely the Rindler time. The near-horizon geometry has the universal form,
\be 
ds^2 = -\rho^2 d\tau^2 + d\rho^2 +r(\rho)^2 d\Omega^2
\ee
where $\rho$ is proper distance from the horizon and $\tau $ is a hyperbolic boost angle. 
The natural candidate for the circuit time for a black hole is the Rindler time. For now let's accept this identification but 
later, in section \ref{Sec: Lyap and Rind} I will give a precise quantitative argument for identifying circuit time with Rindler time.

Thus I will therefore use the 
 same symbol $\t$ for circuit time, and for Rindler time. We may therefore assume that in the context of  black hole evolution the complexity grows according to \ref{dC-dtau=S} with $\tau$ being Rindler time.

An asymptotic   observer at infinity sees  rate of computation  red-shifted. It is a universal fact for all non-extremal black holes, that the asymptotic time $t$ is related to Rindler time by 
\be 
\t = \frac{2\pi t}{\beta} = 2\pi Tt.
\ee



It follows that the rate of computation as seen from infinity, is
\be 
\frac{d\CC}{dt}  
= ST.
\ee
Compare this with \ref{dCdt=ST1} and one sees that  the quantity $C$ is in fact the complexity $\CC.$ Accordingly \ref{CV} may be written in the form,
\be 
\CC =\frac{V}{G \l }.
\label{CV-dualtiy}
\ee
This formula connecting  complexity and the volume of the the wormhole is the called
 CV  correspondence. It is one of two versions of the complexity-geometry correspondence, the other being  complexity-action formulation. Time will not permit me to go over the CA correspondence, but there are many papers that you can consult.

\bn

Let me summarize and emphasize two points:
\begin{enumerate}
\item Circuit time, measured in steps, corresponds to the Rindler time of a black hole. 
Now repeat and memorize: 

 
\it
Circuit time, measured in steps, corresponds to the Rindler time of a black hole. \rm

\bn 

\item Complexity is proportional to the wormhole volume through
\ref{CV-dualtiy}
\end{enumerate}


Of course this latter point is a conjecture; it was not derived from  first-principles. The argument is due to Sherlock Holmes; I quote the great detective:  ``When you have excluded the impossible whatever remains, however improbable, must be the truth." We  can and will subject item 2 to rigorous testing.
