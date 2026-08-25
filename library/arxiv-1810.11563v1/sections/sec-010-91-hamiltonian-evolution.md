---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-010-91-hamiltonian-evolution
section_title: "Hamiltonian Evolution"
section_number: 9.1
pages: 30-32
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In the live lectures at PiTP I ran out of time before I had a chance to discuss how
complexity evolves when a system’s dynamics is governed by a time independent k-local
Hamiltonian. In that case the constraint of energy conservation restricts the motion of
U(t) to lie on a relatively low dimensional subspace of SU (2K). Let’s write U(t) in the
form,
U(t) = eiHt
=
2K
∑
i=1
|Ei⟩⟨Ei|e−iEit (9.30)
29
For a given Hamiltonian the motion is restricted to a torus deﬁned by the set of 2K phases,
eiθi =e−iEit. (9.31)
In other wordsU(t) moves on a 2K-dimensional torus embedded in the (4K−1)-dimensional
groupSU (2K). Although in itself a very large space the torus can only cover a tiny fraction
of the full SU (2K) space.
The ﬁrst question is whether U(t) ﬁlls the torus? Typically the answer is yes. If
the energy levels are incommensurate, as will be the case if the system is chaotic, then
the motion will be ergodic on the torus. The recurrence time for U to return to the
neighborhood of the identity is the time for all the phases to get simultaneously close to
1, and that takes time,
trecur∼ exp 2K. (9.32)
This is in contrast to the recurrence time ∼ exp 4K random (Brownian) circuits which ﬁll
the entire 4K-dimensional unitary group. Therefore it is not possible for U(t) to visit any
but an inﬁnitesimal fraction of the maximally complex unitaries with C∼ 4K.
On the other hand the unitaries of complexity ≤ 2K comprise a set with volume
comparable to the torus. It is therefore likely that for a Hamiltonian system the growth
of complexity in ﬁgure 15 reaches 2 K.
This raises an interesting question: In equation 8.24 I estimated the volume of the
portion of SU (2K) with complexityC and got,
eC logK.
That was the basis for the connection between complexity and the entropy of the auxiliary
system, 9.28,
SA≈C logK.
A similar question can be formulated for motion restricted to the torus: What is the
volume of the torus occupied by unitaries of complexity C? I expect that the answer is
exponential, eαC, but with α parametrically smaller than log K. My guess is that α is
30
independent of K. In that case 9.28 would be replaced by,
SA≈C . (9.33)
This concludes lecture I. In the next lecture I will explain what complexity and its
second law has to do with black holes.
Part II
Lecture II: Black Holes and the
Second Law of Complexity
