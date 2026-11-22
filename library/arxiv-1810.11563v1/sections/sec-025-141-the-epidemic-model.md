---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-025-141-the-epidemic-model
section_title: "The Epidemic Model"
section_number: 14.1
pages: 45-49
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.98
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The best source of confirmation of the $\CC=V$ hypothesis is to perturb the evolution of the black hole, and see if the correspondence  between GR and quantum circuits  continues to hold. For example we may allow some time-dependent perturbations to the CFT Hamiltonian and calculate the effect on the black hole geometry.  At the same time we may study the effects of time-dependent perturbations on the complexity of a quantum circuit. By comparing the two we can confirm the complexity-volume  correspondence. In this context so-called precursor operators are a useful tool.

 Let us consider an operator of the form,
\be 
W(t) = e^{iHt}We^{-iHt} =U^{\dag}(t)W U(t)
\ee
in the Schrodinger picture.
Here $H$ is some all-to-all  \kl \ Hamiltonian acting on a system of $K$ qubits and $W$ is some single qubit unitary operator. With no loss of generality we can take $W$ to act on the first qubit. The complexity of $W$ is $1$. We write that in the form,
\be 
\CC(0)=1.
\ee
The object of our investigation is  $
\CC(t)$---the complexity of $W(t)$ as a function of time. By definition
$
\CC(t)
$
is the \it minimum \rm number of gates that it takes to construct $W(t).$  

Let us first consider the analogous problem for a quantum circuit composed of gates. To that end we replace the evolution operator $e^{-iHt}$ by a product of gates with the usual parallel architecture illustrated in figure \ref{cirkuit}. I'll write it in the form,
\be 
U(t) = g_n g_{n-1}....g_1.
\ee
The precursor operator becomes
\be 
W(t) = g^{\dag}....g^{\dag}_{n-1}g^{\dag}_n \  W \   g_n g_{n-1}....g_1.
\label{W-circuit}
\ee
One might be tempted to ascribe a complexity of $(2n+1)$ to $W(t)$. This however is an overestimate. While it is true that the circuit in \ref{W-circuit} has $2n+1$ gates the definition of complexity requires us to find the \it minimal \rm circuit that prepares $W(t)$.

By assumption $W$ is a very small perturbation on the system of $K$ qubits in that it only affects the first qubit. For all other qubits $W$ acts as the unit operator. Let's first examine the case in which $W$ is just the unit operator, $W=1.$ In that case all the gates in \ref{W-circuit} cancel and the complexity is exactly zero.

In the case where $W\neq 1$ many gates still cancel. To illustrate the cancelation consider the circuit in figure \ref{precursor-circuit3}. The operator $W$ acts between two sub-circuits which are mirror images of each other as in \ref{W-circuit}.
 
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{precursor-circuit3.pdf}
\caption{Circuit  for a precursor}
\label{precursor-circuit3}
\end{center}
\end{figure}

Start at $W$ and let us work our way toward the right. We will say that $W$ infects the qubit that it acts on (colors it blue).  Each  time an infected (blue) qubit interacts with an uninfected (white) qubit it infects it. The result is a growing epidemic in which eventually all qubits are infected. On the left side there is a mirror image epidemic. The growth of the epidemic is shown in figure \ref{precursor-circuit1}.
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{precursor-circuit1.pdf}
\caption{Each infected (blue)  qubit  infects each each qubit that it interacts with. The epidemic grows until all qubits are infected.}
\label{precursor-circuit1}
\end{center}
\end{figure}


Notice  that any gate involving uninfected qubits can cancel a mirror image gate on the other side. The result, after canceling all un-infected gates, is shown in  figure \ref{precursor-circuit4}. 
 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{precursor-circuit4.pdf}
\caption{Uninfected gates cancel with their mirror images.}
\label{precursor-circuit4}
\end{center}
\end{figure}


Evidently the minimum  number of gates needed to prepare the precursor is less then the total number of gates in figure \ref{precursor-circuit3}. Let us quantitatively estimate it.

Suppose the circuit has evolved to the right by $n$ steps and at that stage the epidemic has \it size \rm $s(n).$ Then the average number of new infections that result in the next step is easy to compute. It is given by,
$$\Delta s = \frac{(K-s)s}{K-1}$$
The shift by one unit in the denominator can be ignored,
\be 
\Delta s = \frac{(K-s)s}{K}.
\label{difference equ}
\ee
We can replace this by a differential equation
\be 
\frac{ds}{d\tau} = \frac{(K-s)s}{K}
\ee
which is easily integrated,
\be 
s = \frac{Ke^{\tau}}{K + e^{\tau}}.
\label{logistic}
\ee

This ``epidemic function"\footnote{Also known as the logistic function.} governs the size of the precursor operator. 

Equation \ref{logistic} can written,
\be 
\frac{s}{K} = \frac{e^{\tau -\tau_*}}{1+e^{\tau -\tau_*}}
\ee
where $\tau_*$ is the \it scrambling  time \rm expressed in circuit time units.
\be 
\tau_* = \log{K}
\label{s-over-K}
\ee
The size $s(\t)$ has the following properties:
For small $\tau$ \ref{s-over-K} grows exponentially,
\be 
s(\tau) \approx e^{\tau}  \ \ \ \ \ \rm (small \ \tau)
\label{expgro}
\ee


\bn

For large $\tau$ the size saturates when all qubits become infected,
\be 
s(\tau) \to K.
\ee
and 
\be
\frac{s}{K}\to 1.
\ee
At the scrambling time a rather sharp crossover takes place and the size jumps rapidly to its saturation value $K$.
