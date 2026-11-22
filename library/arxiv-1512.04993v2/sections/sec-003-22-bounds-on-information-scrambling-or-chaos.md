---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-003-22-bounds-on-information-scrambling-or-chaos
section_title: "Bounds on information scrambling or chaos"
section_number: 2.2
pages: 10-11
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.983
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
For a system with $N$ degrees of freedom, the scrambling time $t_*$ is a measure of how long it takes for information about a small $O(1)$ perturbation to spread over $O(N)$ degrees of freedom \cite{fastscramble}. Another useful definition \cite{Page:1993df} is that this is the time required for reduced density matrix of any subsystem with fewer than half the degrees of freedom  to look approximately thermal.\footnote{In general, this concept is only useful for systems described by  $k$-local Hamiltonian with $k \ll N$. For more discussion, see Appendix~\ref{sec:appendix:A1}}

 Black holes are the fastest scramblers in nature \cite{bhmirror,fastscramble,Maldacena:2015waa}. There are two senses in which this is true:

 First, for a system arranged on a $d$-dimensional lattice, the scrambling time can be no faster than $t_* \sim N^{1/d}$, where $d$ is the number of spatial dimensions of the system \cite{fastscramble}. $N^{1/d}$ is proportional to the system's linear dimensions and implies that the  scrambling is ballistic. It was conjectured \cite{bhmirror,fastscramble} (see also \cite{Lashkari:2011yi}) and then shown \cite{shock} that the scrambling time for black holes in AdS is given by
 \be
t_* \sim \beta \log N.
 \ee
For black holes the dimensionality of the lattice $d$ is effectively infinite.

Second, not only are black holes the fastest scramblers because the scrambling time is logarithmic in $N$, they also have the smallest possible coefficient in front of the logarithm
 \be
t_* = \lambda_{L}^{-1} \log N,
 \ee
where the rate of scrambling can be interpreted in terms of chaos as a Lyapunov exponent $\lambda_L$ \cite{kitaev,Maldacena:2015waa}. A useful measure of the strength of chaos is given by the out-of-time-order four-point correlator \cite{LarkinOvchinnikov}
\be
\langle W(t)\, V \,W(t)\, V\rangle_\beta,
\ee
where $\langle \cdot \rangle_\beta$ is the thermal expectation value, $W$ and $V$ are simple local Hermitian operators, and $W(t) \equiv e^{iHt} W e^{-iHt}$. In chaotic systems, this correlation function will exhibit chaotic Lyapunov behavior (the butterfly effect) and initially decay as \cite{LarkinOvchinnikov, kitaev, Maldacena:2015waa}
\be
\langle W(t)\, V \,W(t)\, V\rangle_\beta = f_0 - f_1\, e^{\lambda_L (t - t_*)} + O(N^{-2}),
\ee
with $O(1)$ constants $f_0, f_1$.
Quantum mechanics puts a bound on this exponent \cite{Maldacena:2015waa}
\be
\lambda_L \le \frac{2\pi k_B T}{\hbar},
\ee
and black holes saturate this bound \cite{shock,Shenker:2013yza,localshocks,kitaev,Shenker:2014cwa}.
