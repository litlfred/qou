---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-044-221-the-protocol
section_title: "The Protocol"
section_number: 22.1
pages: 73-75
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Here is the circuit that accomplishes the task:
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{clean1.pdf}
\caption{}
\label{Clean1}
\end{center}
\end{figure}

Let me explain figure \ref{Clean1}. The initial state is,
\be 
|\Psi\ra  = |max\ra \otimes |0\ra
\ee
The single-qubit gates $H$ are Hadamard gates, which have the following action,
\bea
H |0\ra &=& \frac{1}{\sqrt 2} \big{(}|0\ra + |1\ra\big{)} \cr
H |1\ra &=& \frac{1}{\sqrt 2} \big{(}|0\ra - |1\ra\big{)}
\eea
The protocol begins with a Hadamard acting on the clean qubit to transform it to $\big{(}|0\ra + |1\ra\big{)}$.

Next, a ``controlled" $G$ operation acts. The dot at the bottom indicates a controlled operation: if the clean qubit is in the state $|0\ra$ then the unitary operator $G$ acts on the remaining qubits; if the clean qubit is in state $|1\ra$ then $G$ does not act and $|max\ra$ is left undisturbed. The last element of the circuit is another Hadamard.

It is straightforward to follow the circuit and see that the final state is,
\bea 
|\Psi'\ra &=&{ \frac{1}{2} } \big{(} G+1 \big{)} \otimes |0\ra \cr \cr
 &+& 
\frac{1}{2} \big{(} G-1 \big{)} \otimes |1\ra
\eea
Finally we compute the expectation value of the $Z$ Pauli operator for the clean qubit (which by the way, is no longer clean).
\be 
\la Z \ra = \la max| \left( \frac{G^{\dag}+G}{2}\right) |max\ra
\ee

We now make use of the fact that $|max\ra$ is maximally complex. A maximally complex state is Haar-random, which allows us to replace the expectation value by the normalized trace,

\be 
\la Z \ra = \Tr \left( \frac{G^{\dag}+G}{2}\right) 
\ee

Thus the circuit transforms the initial state to a final state that indeed has information about $\Tr G.$ Of course that is not the end of the story; we still have to measure $Z$ and repeat the procedure enough times to determine the $\la Z \ra$ but that is not part of the reversible process that we define to be the computational work.

It is also possible to determine $ \Tr \left( \frac{G^{\dag}-G}{2}\right) $ by a similar method which I will leave to you.

One might complain that applying $G$ is not a \kl \ operation, but that is easy to repair assuming that $G$ can be written as a product of gates as in \ref{G=gg}. In that case the circuit in figure \ref{Clean1} can also be decomposed into local gates. This is shown in figure \ref{Clean2}.

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.2]{clean2.pdf}
\caption{}
\label{Clean2}
\end{center}
\end{figure}

The circuit can be simplified by using $H^2 =1$ to eliminate all the Hadamards except for the ones at the beginning and end.
I will leave you to ponder this circuit and show that it is the same as the original circuit in figure \ref{Clean1}.
