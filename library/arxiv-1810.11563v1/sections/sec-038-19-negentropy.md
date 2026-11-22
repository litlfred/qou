---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-038-19-negentropy
section_title: "Negentropy"
section_number: 19
pages: 68-69
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
\bn


Let's begin with some examples of negentropy. Consider a box of gas composed of $n$ classical particles. The microstate of the box is defined by $n$ points in the phase space of a single particle. The macrostate can be described thermodynamically in terms of a much smaller number of thermodynamic variables including entropy.
If the entropy is maximal (subject to some constraint) then the gas is in equilibrium and the negentropy is zero. No work can be extracted. 


\bn

Now suppose we have two thermodynamically identical boxes of gas, where each box is in  thermal equilibrium.  Let's also assume the microstates are uncorrelated except for the fact that they are macroscopically similar. See figure \ref{2box-uncor} 
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{2box-uncor.pdf}
\caption{}
\label{2box-uncor}
\end{center}
\end{figure}

The entropy of either box is $S_{max}$ and the total entropy is 
$2S_{max}$. Moreover the maximum total entropy is also 
$2S_{max}$. It follows that the negentropy is zero and no work can be be extracted.

Now let's compare that with another example involving the same two boxes, each in equilibrium, but this time the microstates are \it identical \rm as illustrated in figure \ref{2box-cor} .

\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{2box-cor.pdf}
\caption{}
\label{2box-cor}
\end{center}
\end{figure}

Each box is in equilibrium but the combined system has much less entropy than the previous example. In fact the total entropy is exactly the same as for the individual boxes,
\bea 
S(total) \eq S_{max} \cr \cr
S_{max}(total) \eq 2S_{max} \cr \cr
\rm Negentropy \it &=& S_{max}
\eea
In other words the high degree of correlation between the microstates gives rise to  negentropy, a resource which in principle can be exploited to do a significant amount of work.

\bn

\bf Exercise: \rm
Design a machine to extract work from this setup.

 Then patent it.

\bn
