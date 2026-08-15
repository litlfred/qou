---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-004-23-bounds-on-quantum-evolution
section_title: "Bounds on quantum evolution"
section_number: 2.3
pages: 11-12
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
As well as being concerned with how much information may be stored, or how fast
information may be scrambled, we are interested in how fast the system can change
its global state. The time for the system to reach an orthogonal state is perhaps the
simplest way to measure the rate of change of the global state. In this direction, there
are two proved theorems, the Aharonov-Anandan-Bohm bound and the Margolus-
Levitin bound. However, the orthogonality time is not the right measure to associate
with the growth of the black hole interior, so we turn instead to the rate of growth of
quantum gate complexity to measure how the global state is changing. The existing
bounds on complexity growth are UV sensitive and not useful for our purposes, so
we conjecture a new bound on the rate of growth of complexity inspired by Lloyd’s
conjecture.
We ﬁrst review the bounds on orthogonality time. Then we recall Lloyd’s conjecture
and formulate our own conjecture on the rate of complexiﬁcation.
The Aharonov-Anandan-Bohm bound involves the standard deviation of the energy,
orthogonality time ≥ πℏ
2∆E. (2.9)
Since time is not an operator in quantum mechanics, the energy-time uncertainty
relation does not say that the time must be uncertain [31,32], instead it says that time
must be spent to evolve to an orthogonal state. The Aharonov-Anandan-Bohm bound
is saturated by a two state system
|ψ(t)⟩ = 1√
2
(
|0⟩ +eiEt|E⟩
)
→ |⟨ψ(t)|ψ(0)⟩| = cosEt
2ℏ. (2.10)
The Margolus-Levitin bound involves the expectation value of the energy above the
ground state [33]
orthogonality time≥ πℏ
2⟨E⟩. (2.11)
This is saturated by the same two state system that saturates the Aharonov-Anandan-
Bohm bound, Eq. 2.10. Depending on state, either of the Margolus-Levitin and
Aharonov-Anandan-Bohm bounds may be tighter.
10
Inspired by these bounds on orthogonality time, Lloyd conjectured that they imply
a bound on the rate of computation, loosely deﬁned [14]. If we had a computer where
after each time step the logical state of the computer was given by a classical bit string
(a quantum state in the “computational basis”), then because any two distinct bit
strings correspond to orthogonal states the maximum rate at which the system can cycle
through bit strings is given the tighter of the two orthogonality time bounds. Lloyd also
noted thatN parallel copies of a computer could be understood to computeN times as
fast; while the expected energy scales asN, the standard deviation of the energy would
only increase by
√
N. In light of this, Lloyd conjectured [14] that by allowing parallel
computation the total rate of computation is proportional to the average energy. This
work is related to other bounds on computation and communication [34–36] and to
some ideas about quantum gravity [37–39].
To generalize and make precise Lloyd’s notion of “operations per second”, we would
