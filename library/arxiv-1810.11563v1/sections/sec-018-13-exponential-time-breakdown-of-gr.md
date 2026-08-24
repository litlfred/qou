---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-018-13-exponential-time-breakdown-of-gr
section_title: "Exponential Time Breakdown of GR"
section_number: 13
pages: 43-44
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
According to classical general relativity an Einstein-Rosen bridge (ERB), or a one-sided
bridge-to-nowhere, grows forever. It is interesting that this growth is bounded by quantum
mechanics. To see why we consider a diagnostic of the length of the wormhole, namely the
equal time correlation between CFT ﬁelds outside the black hole horizons. If the two ﬁelds
are on the same side then the correlation will be time-independent because the density
matrix on each side is thermal, and therefore stationary. But if we consider correlations
between opposite sides it is well known that the correlation is large at t = 0 and decreases
with the magnitude of t. The cause of the decrease is simple; the wormhole separating the
two sides grows. Roughly speaking we expect the correlation to exponentially decreases
with the distance through the wormhole,
⟨φLφR⟩∼ e−L(t)/lads (13.44)
42
where L(t) is the length of the wormhole 15 at time t.
Recall that in quantum mechanics there is a theorem called the quantum-recurrence
theorem:
Quantum Recurrence Theorem:
The state of a (non-integrable) system with a ﬁnite density of states will be quasiperiodic
with a recurrence time doubly exponential in the entropy. This applies both to black holes
in AdS and to generic states of systems of K∼S qubits. The quantum recurrence time is
exp (expS ). Over this enormous time scale the state will quasiperiodically return arbitrarily
close to its initial value.
It follows that over such long time scales the two-sided correlation⟨φLφR⟩ will return to its
initial TFD value, and from 13.44 the distance through the wormhole will also return to
its minimal value. The classical phenomenon of eternal growth must break down quantum
mechanically as a consequence of the ﬁnite entropy of black holes (recall that classically
the entropy diverges like 1/ℏ).
I believe we can do better and argue that classical geometry must break down at a
singly exponential time ∼ expS. The argument goes as follows: As the wormhole grows
the evolving quantum state must pass through a series of orthogonal states. The time scale
for the state to become orthogonal is the Anandan-Aharonov time 1 /∆E. As an example,
for a 4-dimensional Schwarzschild black hole the uncertainty in the energy is the Planck
mass. Thus the system must pass through orthogonal states at the rate of one per Planck
time.
The problem is that there are only a limited number of available mutually orthogonal
states, the number being of order exp(S). After an exponential time we run out of orthog-
onal states. Subsequent states must become superpositions of the previous states, all of
which have sub-exponential wormhole length. This implies that the expectation value of
the length of the wormhole must stop growing when t∼ expS. This behavior is distinctly
non-classical. We’ll return to this issue.
