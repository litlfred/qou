---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-004-5-dual-role-of-unitaries
section_title: "Dual Role of Unitaries"
section_number: 5
pages: 9-14
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.955
---
Complexity can be defined for states\footnote{We continue to work with systems of $K$ qubits. The space of states is $2^K$ dimensional.}, but in many ways it is more natural to start with the complexity of operations that you can do to a system. That means the complexity of unitary operators. Unitary matrices have a dual role in quantum information theory. First of all they are the matrix representation of unitary operators,  
\be 
U = \sum U_{ij}|i\ra \la j|
\ee

Secondly they can be used to represent
maximally entangled states of $2K$ qubits,
\be 
|\Psi\ra = \sum U_{ij}|i\ra |\bar{j}\ra
\ee
\footnote{The bar in $\bar{J}$  indicates time reversal or in relativistic quantum field theory the CPT operation.}
In asking about the complexity of unitary operators we are also asking about the complexity of maximally entangled states\footnote{In the case of maximally entangled systems I mean a restricted form of complexity in which gates are only permitted to act on each side of the entangled system separately, thus preserving the maximal entanglement.},

The space of (special ) unitary operators is $\suk.$ It is much bigger than the space of states $CP(2^K-1)$. Let's begin with a crude estimate of its size.
A unitary matrix in $SU(N)$ has $(N^2-1)$ real parameters. If each parameter can take on $m$ values the number of unitary operators is
$$
\#unitaries = m^{(N^2-1)} 
$$
Setting $N= 2^K,$
\bea  
\#unitaries \eq m^{(4^K-1)} \cr \cr
\log{(\#unitaries)} &\approx& 4^K \log{m}
\label{log-Nunit}
\eea
This is the same pattern that we saw for states except that $2^K$ is replaced by $4^K.$


\section{Volume of $SU(2^K)$}

Let's make a more refined calculation of the number of operators in $SU(N)$ by dividing its volume by the volume of an epsilon ball of the same dimensionality (the dimension of $SU(N)$ is $N^2-1.$).
The volume of $SU(N)$ is \  \url{https://arxiv.org/abs/math-ph/0210033} 
\be 
V[SU(N)] = \frac{2\pi^{\frac{(N+2)(N-1)}{2}}}{1!2!3!....(N-1)!}
\ee
The volume of an epsilon-ball of dimension $N^2-1$ is
$$\frac{\pi^\frac{N^2-1}{2}}{  \left( \frac{     N^2-1}{2}  \right)!         }$$









\bn
Using Stirling's formula, and identifying the number of unitary operatos with the number  of epsilon-balls in $SU(N)$ 
\bea   
\#unitaries  &\approx& 
\left( \frac{N}{\epsilon^2} \right)^{\frac{N^2}{2}} \cr \cr
&=&  \left(  \frac{2^K}{\epsilon^2} \right)^{4^K/2}
\label{V-in-e-balls}
\eea
Taking the logarithm,
\be 
\log{(\#unitaries)} \approx  \frac{4^K}{2}K\log{2} + 4^K\log{\frac{1}{\epsilon}}
\label{log-balls}
\ee
which is comparable to \ref{log-Nunit}.
Again, we see the strong exponential dependence on $K$ and the weak logarithmic dependence on $\epsilon.$ The $\log{\frac{1}{\epsilon}}$ term  is multiplied by the dimension of the space.


\section{Exploring $\suk $}

We've seen that the space of unitary operators is  gigantic. Now I want to discuss how  to move through it. I've already hinted that we don't make big complexity jumps, but instead move in little steps called gates. A sequence of gates is called a circuit although it has nothing to do with periodicity. It's just a name.

\bn
\bf Definition: \rm

A \kl \ gate is a nontrivial k-qubit unitary operator chosen from some allowed universal gate set. We assume that if $g$ is in allowed set, so is $g^{\dag} $. 

Figure \ref{gate} is a schematic representation of a 2-qubit gate.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{gate.pdf}
\caption{Time flows from left to right. A gate acts on an incoming state of two-qubits to give an outgoing state.}
\label{gate}
\end{center}
\end{figure}




\bn
Gates can be assembled into quantum circuits in the manner shown in figure \ref{circuit}.
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{circuit.pdf}
\caption{k-local all-to-all circuit}
\label{circuit}
\end{center}
\end{figure}


A \kl \ circuit is one made of \kl \ gates. k-locality is not the same as spatial locality although spatially local circuits are special cases of \kl \ circuits. In a spatially local circuit the qubits are arranged on a spatial lattice of some dimensionality. Gates are permitted only between near neigbors on the lattice. An example of a \kl  \ and spatially local circuit is shown in figure \ref{s-local}.
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{s-local.pdf}
\caption{Spatially local circuit}
\label{s-local}
\end{center}
\end{figure}
Such circuits would be valuable for simulating condensed matter systems but they are not the kind of circuits we will be interested in.

\bf Definition \rm
A \kl \ \it all-to-all\rm \ circuit is one which is \kl \ but permits any group of $k$ qubits to interact. Figure \ref{circuit} is 2-local \ and all-to-all.

In  figure \ref{circuit} the gates act in series, one gate at a time, but it is more efficient to allow parallel action of gates. The standard \kl \ all-to-all 
circuit architecture is shown in figure \ref{standard-circuit}.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{standard-circuit.pdf}
\caption{Standard circuit architecture. Note that in each step the 
gates all commute because they act on non-overlapping qubits.}
\label{standard-circuit}
\end{center}
\end{figure}

The rule is that at each step the qubits are grouped into pairs and each pair interacts by means of a two-qubit gate. 








We imagine that such a circuit is equipped with a clock, and with each tick of the clock $K/2$ gates act. We'll call this a ``step." The number of steps in a circuit is called its depth $D$. The depth of the circuit in figure \ref{standard-circuit} is $D=5.$  The number of gates in the circuit is $\frac{KD}{2}$.


Between steps the qubits may be permuted so that any pair can potentially interact. A circuit of this type can be called \kl \ (2-local in figure \ref{standard-circuit}) and all-to-all. The meaning of all-to-all is that any pair of qubits can potentially interact. Note that in a given time-step the different gates commute because they act on non-overlapping qubit pairs .

If we measure time $\tau$ in units of steps then the number of gates that act per unit time is $K/2.$

\bn

A given circuit prepares a particular unitary operator $U$.
Preparing $U$ by a series of steps can be viewed as a discrete motion of a fictitious classical particle, called the auxiliary system $\CA$ in Brown-Susskind
\url{https://arxiv.org/pdf/1701.01107.pdf}.

The auxiliary system represents the motion of $U(t)$ on $SU(N)$ as time unfolds.  The classical particle  starts at  the identity operator $I$ and ends at $U$.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{motion.pdf}
\caption{The auxiliary system: The evolution of the unitary operator $U(t)$ can be thought of as the motion of a classical particle moving through the group space \Suk.  }
\label{motion}
\end{center}
\end{figure}
