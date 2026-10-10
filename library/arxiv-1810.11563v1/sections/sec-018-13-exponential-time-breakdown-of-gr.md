---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-018-13-exponential-time-breakdown-of-gr
section_title: "Exponential Time Breakdown of GR"
section_number: 13
pages: 43-44
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
text_source: latex
latex_prose_ratio: 0.773
latex_coverage_ratio: 0.981
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
\label{expTbreakdown}
According to classical general relativity an Einstein-Rosen bridge (ERB), or  a one-sided bridge-to-nowhere, grows forever. It is interesting that this growth is bounded by quantum mechanics. To see why we  consider a diagnostic of the length of the wormhole, namely the equal time correlation between CFT fields outside the black hole horizons. If the two fields are on the same side then the correlation will be time-independent because the density matrix on each side is thermal, and therefore stationary. But if we consider correlations between opposite sides it is well known that the correlation is large at $t=0$ and decreases with the magnitude of $t$. The cause of the decrease is simple; the wormhole separating the two sides grows. Roughly speaking we expect the correlation to  exponentially decreases with the distance through the wormhole,
\be 
\la \phi_L \phi_R \ra \sim e^{-L(t)/l_{ads}}
\label{correlate}
\ee
where $L(t)$ is the length of the wormhole\footnote{This formula holds until $L/l_{ads}$ is of order the entropy. Beyond that the correlation is dominated by noise. } at time $t$.

Recall that in quantum mechanics there is a theorem called the quantum-recurrence theorem:

\bn

\bf Quantum Recurrence Theorem: \it
\bn

 The state of a (non-integrable) system with a finite density of states will be quasiperiodic  with a recurrence time doubly exponential in the entropy. This applies both to black holes in AdS and to generic states of systems of $K \sim S$ qubits. The quantum recurrence time is $ exp \ (exp \  S).$ Over this enormous time scale the state will quasiperiodically  return arbitrarily close to its initial value. \rm 



\bn
It follows  that over such long time scales the two-sided correlation 
$\la\phi_L \phi_R \ra$ will  return to its initial TFD value, and from \ref{correlate}   the distance through the wormhole will also  return to its minimal value. The classical phenomenon  of eternal growth must break down quantum mechanically as a consequence of the finite entropy of black holes (recall that classically the entropy diverges like $1/\hbar$).

I believe we can do better and argue that classical geometry must break down at a singly exponential time $\sim \exp{S}$. The argument goes as follows:
As the wormhole grows the evolving quantum state must pass through a series of orthogonal states. The  time scale for the state to become orthogonal is the Anandan-Aharonov time $1/\Delta E.$ As an example, for a 4-dimensional \S \  black hole the uncertainty in the energy is the Planck mass. Thus the system must pass through orthogonal states at the rate of one per Planck time.

The problem is that there are only a limited number of available  mutually orthogonal states, the number being of order $\exp(S).$ After an exponential time we run out of orthogonal states. Subsequent states   must become  superpositions of the previous states, all of which have sub-exponential wormhole length. This implies that the expectation value of the length of the wormhole must stop growing when $t\sim \exp{S}.$ This behavior is distinctly non-classical. We'll return to this issue.


\subsection{C=V}
Let's come back now to the  puzzle:  what grows long after thermal equilibrium is attained? 
 I only know one thing that has all the right features: quantum complexity. As I explained in Lecture I, quantum complexity has many of the characteristics of entropy but on a grand exponential time scale. It may be thought of as the entropy of the classical auxiliary system $\CA$ that I defined in Lecture I.
 
 
 To relate complexity to the spatial volume of the wormhole or Bridge-to-Nowhere we go back to equation \ref{CV},
$$\CC=\frac{V}{Gl_{ads}}.$$
This is the complexity=volume duality proposal.  The mysterious bounce shown in figure \ref{Foliated-BTZ2} is evidently a complexity bounce, not an  ordinary thermal entropy bounce.
 


Now let's turn to the confirmation of the CV hypothesis, not by deriving it but by detailed comparison of the behavior of volume (as determined from GR), and complexity (from the study of quantum circuits).
