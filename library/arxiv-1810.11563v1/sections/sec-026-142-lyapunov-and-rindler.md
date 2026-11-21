---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-026-142-lyapunov-and-rindler
section_title: "Lyapunov and Rindler"
section_number: 14.2
pages: 49-51
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.992
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
\label{Sec: Lyap and Rind}

Let's come back to the relation between circuit clock time and Rindler time. You may think that the arguments were not very compelling  but equations \ref{difference equ} through \ref{expgro} provide a quantitative basis for the identification.
The exponential growth in \ref{expgro} is expected and should  be compared with the OTOC theory of scrambling, especially as applied to black holes.
There it is well known from the work of Kitaev and Maldacena, Shenker, and Stanford,  that in black hole physics size grows according to,
\be 
s(t) \approx e^{\frac{2\pi}{\beta}t}  \ \ \ \ 
\label{expgro-t}
\ee
The quantity $2\pi/\beta$ is called the quantum Lyapunov exponent and it is universal for large black holes as long as the \S \ radius is much  larger than the string scale.


Comparing  \ref{expgro-t} with \ref{expgro} we see that agreement indeed requires, 
\be 
\tau ={\frac{2\pi}{\beta}t}.
\ee

In other words circuit time is Rindler time.
  
\bn


\subsection{Back to Size and Complexity}



Let us now consider the total number of  un-cancelled gates in figure \ref{precursor-circuit1}. This number is the complexity of the precursor at time $\tau$. 

$$
\#\rm{uncanceled \ gates} = \CC(\tau).
$$


\bn
The number of such gates on the right side at any discrete time $n$ is the sum of the sizes for all times less than or equal to $n$. In terms of the continuous time we can write,
\be 
\CC(\tau) = \int_0^{\tau} s(\tau')d\tau'
\ee
or using \ref{logistic},
\be  
\CC(\tau) = K\log(1+ e^{\tau-\tau_*}).
\label{compcircuit}
\ee

For large $K$ the size and complexity of the precursor are negligibly small (compared to $K$) until the scrambling time at which they quickly grow to $K$. After that the size is constant and the complexity grows linearly. The delay in the growth of complexity by $\tau_*$ is called the switchback effect 
(Stanford and Susskind, \url{https://arxiv.org/pdf/1406.2678.pdf}) 
 and is an important diagnostic that we will use later. The time-dependence of size and complexity are shown in figures \ref{size} and \ref{complexity}.



\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{size.pdf}
\caption{size  as a function of time}
\label{size}
\end{center}
\end{figure}





\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{complexity.pdf}
\caption{ as a function of time}
\label{complexity}
\end{center}
\end{figure}



\bn

\bn

Now let us turn to precursors in black hole physics. We will see some remarkable correspondences between the geometry of black hole interiors and the equations that we have derived from the analysis of circuits.
