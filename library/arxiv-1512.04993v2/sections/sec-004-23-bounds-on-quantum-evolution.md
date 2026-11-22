---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-004-23-bounds-on-quantum-evolution
section_title: "Bounds on quantum evolution"
section_number: 2.3
pages: 11-13
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.793
latex_coverage_ratio: 0.988
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
As well as being concerned with how much information may be stored, or how fast information may be scrambled, we are interested in how fast the system can change its global state. The time for the system to reach an orthogonal state is perhaps the simplest way to measure the rate of change of the global state. In this direction, there are two proved theorems, the Aharonov-Anandan-Bohm bound and the Margolus-Levitin bound. However, the orthogonality time is not the right measure to associate with the growth of the black hole interior, so we turn instead to the rate of growth of quantum gate complexity to measure how the global state is changing. The existing bounds on complexity growth are UV sensitive and not useful for our purposes, so we conjecture a new bound on the rate of growth of complexity inspired by Lloyd's conjecture. 

We first review the bounds on orthogonality time. Then we recall Lloyd's conjecture and formulate our own conjecture on the rate of complexification.

The Aharonov-Anandan-Bohm bound involves the standard deviation of the energy,
\begin{equation}
\textrm{orthogonality time} \ \geq \frac{\pi \hbar }{2  \Delta E} .
\end{equation}
Since time is not an operator in quantum mechanics, the energy-time uncertainty relation does not say that the time must be uncertain \cite{Anandan:1990fq,Aharonov:1961mka}, instead it says that time must be spent to evolve to an orthogonal state. The Aharonov-Anandan-Bohm bound is saturated by a two state system
\begin{equation}
| \psi (t) \rangle = \frac{1}{\sqrt{2}} \left( | 0 \rangle + e^{i E t} | E \rangle \right) \ \rightarrow  \ |\langle \psi(t) | \psi (0) \rangle | = \cos \frac{E t}{2 \hbar}. \label{eq:Heisenbergexample}
\end{equation}

The Margolus-Levitin bound involves the expectation value of the energy above the ground state \cite{Margolus:1997ih}
\begin{equation}
\textrm{orthogonality time} \geq \frac{\pi \hbar}{2 \langle E \rangle} .
\end{equation}
This is saturated by the same two state system that saturates the Aharonov-Anandan-Bohm bound, Eq.~\ref{eq:Heisenbergexample}. Depending on state, either of the Margolus-Levitin and Aharonov-Anandan-Bohm bounds may be tighter.

Inspired by these bounds on orthogonality time, Lloyd conjectured that they imply a bound on the rate of computation, loosely defined \cite{lloyd2000ultimate}. If we had a computer where after each time step the logical state of the computer was given by a classical bit string (a quantum state in the ``computational basis"), then because any two distinct bit strings correspond to orthogonal states the maximum rate at which the system can cycle through bit strings is given the tighter of the two orthogonality time bounds. Lloyd also noted that $N$ parallel copies of a computer could be understood to compute $N$ times as fast; while the expected energy scales as $N$, the standard deviation of the energy would only increase by $\sqrt{N}$. In light of this, Lloyd conjectured \cite{lloyd2000ultimate} that by allowing parallel computation the total rate of computation is proportional to the average energy. This work is related to other bounds on computation and communication \cite{otherbounds1,otherbounds2,otherbounds3} and to some ideas about quantum gravity \cite{lloyd_qg1,lloyd_qg2,lloyd_qg3}.

To generalize and make precise Lloyd's notion of ``operations per second", we would like to consider how complexity builds up in an isolated unitarily evolving quantum system in a general quantum state. Building on the work of Aharonov-Anandan-Bohm, Margolus-Levitin, and Lloyd, we conjecture a similar bound on the rate of growth of complexity. Informally this is the rate of growth of the number of simple gates needed to prepare the state of the computer from a reference state,
\begin{equation}
\frac{d \textrm{gates}}{dt} \leq \frac{2E}{\pi \hbar}. \label{eq:LloydBound}
\end{equation}


\eqref{eq:LloydBound} is fast. A 100$g$ 2015-era CPU manages about $10^{12}$ classical operations per second,\footnote{The world's fastest ``supercomputer'' is the collection of all the bitcoin miners, which have a total FLOP rate of 5 million petaFLOPs, about a thousand times more than all the single site supercomputers combined.} much less than the permitted $10^{50}$. The slowdown is largely the fault of wastefully locking up most of the energy in the rest mass of atoms, where it does no useful computation. (Indeed, counting just the energy in the logical qubits, modern cold atom experiments come close to saturating Eq.~\ref{eq:LloydBound}). A fast computer should avoid massive particles, and should interact strongly. A good candidate for a fast computer is therefore a highly energetic strongly coupled conformal field theory---these are known under some circumstances to be holographically dual to black holes.

Unlike in the case of information storage, there is no tight argument that black holes must be the fastest information processors in nature. There is no thought experiment that tells us that if a mountain of CPUs undergoes gravitational collapse, it must thereafter compute faster. Nevertheless, in light of the above considerations, it seems reasonable to conjecture that black holes excel as much here as they do in other information theoretic tasks. We conjecture that black holes are the fastest computers, in the sense that they saturate the complexification bound Eq.~\ref{eq:LloydBound}.\footnote{We have argued that black holes may be the fastest computers in nature, at least within some restricted class. Even assuming this is true, it is important to appreciate what this does and does not mean. It means that nothing can implement quantum gates any faster than a black hole (at fixed energy). It certainly means that nothing can simulate the complete output from a black hole any faster than the black hole itself can produce that output (at fixed energy). It does not mean that a black hole can beat you at chess.

This is not a phenomenon unique to black holes. For our purposes, a ``computer'' is a device that implements a unitary operation. This is useful if you are interested in implementing that unitary---if you are interested in the state of the Hawking radiation that emerges after a certain input has been thrown into the black hole, for example. If instead you have another question in mind---factorization, chess strategy, etc.---then the unitary is useful to you only if combined with other computing resources to ``encode'' the problem instance in terms of ingoing perturbations into the black hole, and to ``decode'' the Hawking radiation output of the black hole in terms of a strategy recommendation. For a generic problem, the computational resources needed to encode and decode the question are expected to be no smaller than the computational resources required to just solve the problem directly, without reference to the black hole. For generic problems, therefore, black holes don't help. (See Chapter~6 of \cite{DBLP:journals/corr/abs-1108-1791}.) \label{eq:footnotecomputionalism}}
