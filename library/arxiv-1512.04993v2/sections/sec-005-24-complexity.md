---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-005-24-complexity
section_title: "Complexity"
section_number: 2.4
pages: 12-14
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
system in a general quantum state. Building on the work of Aharonov-Anandan-Bohm,
Margolus-Levitin, and Lloyd, we conjecture a similar bound on the rate of growth of
complexity. Informally this is the rate of growth of the number of simple gates needed
to prepare the state of the computer from a reference state,
dgates
dt ≤ 2E
πℏ. (2.12)
Eq. 2.12 is fast. A 100 g 2015-era CPU manages about 10 12 classical operations
per second, 4 much less than the permitted 10 50. The slowdown is largely the fault of
wastefully locking up most of the energy in the rest mass of atoms, where it does no
useful computation. (Indeed, counting just the energy in the logical qubits, modern
cold atom experiments come close to saturating Eq. 2.12). A fast computer should avoid
massive particles, and should interact strongly. A good candidate for a fast computer is
therefore a highly energetic strongly coupled conformal ﬁeld theory—these are known
under some circumstances to be holographically dual to black holes.
Unlike in the case of information storage, there is no tight argument that black
holes must be the fastest information processors in nature. There is no thought ex-
periment that tells us that if a mountain of CPUs undergoes gravitational collapse, it
must thereafter compute faster. Nevertheless, in light of the above considerations, it
seems reasonable to conjecture that black holes excel as much here as they do in other
information theoretic tasks. We conjecture that black holes are the fastest computers,
4The world’s fastest “supercomputer” is the collection of all the bitcoin miners, which have a
total FLOP rate of 5 million petaFLOPs, about a thousand times more than all the single site
supercomputers combined.
11
in the sense that they saturate the complexiﬁcation bound Eq. 2.12. 5
2.4 Complexity
Given a state|ψ⟩ on n qubits, the state complexity of |ψ⟩ is the minimum number of
gates necessary to construct |ψ⟩. We ﬁx a simple reference state |ψ0⟩ and a universal
gate set of elementary unitaries {Gα} and deﬁne the complexity of |ψ⟩ to be the
minimum number of gates necessary to produce |ψ⟩ from|ψ0⟩. More generally, we
require only that |ψ⟩ be closely approximated by a state produced from |ψ0⟩. The
complexity of |ψ⟩ in principle depends on all the details of the construction, but is
expected to be relatively robust in its basic properties, e.g. the distinction between
states of poly(n) complexity and exp(n) complexity is independent of the details.
In this paper we conjecture the existence of a more reﬁned notion of complexity
appropriate for continuum ﬁeld theories. Our reﬁned notion of complexity should have
the key property that, until it saturates, it grows linearly in time under evolution by a
local Hamiltonian. The rate of complexity growth should also be proportional to the
number of active degrees of freedom. We assume that a deﬁnition including all these
details exists, at least for semiclassical bulk states, but many of our conclusions are
robust even if such a unique deﬁnition cannot be constructed. An incomplete discussion
of these open questions is given in Appendix A.
So long as we are considering the late time rate of change of complexity growth, the
reference state|ψ0⟩ may be taken to be the thermoﬁeld double state. (For one-sided
systems the reference state would be a locally perturbed ground state.) We will discuss
the reference state in more detail in [41].
5We have argued that black holes may be the fastest computers in nature, at least within some
restricted class. Even assuming this is true, it is important to appreciate what this does and does not
mean. It means that nothing can implement quantum gates any faster than a black hole (at ﬁxed
energy). It certainly means that nothing can simulate the complete output from a black hole any
faster than the black hole itself can produce that output (at ﬁxed energy). It does not mean that a
black hole can beat you at chess.
This is not a phenomenon unique to black holes. For our purposes, a “computer” is a device that
implements a unitary operation. This is useful if you are interested in implementing that unitary—if
you are interested in the state of the Hawking radiation that emerges after a certain input has been
thrown into the black hole, for example. If instead you have another question in mind—factorization,
chess strategy, etc.—then the unitary is useful to you only if combined with other computing resources
to “encode” the problem instance in terms of ingoing perturbations into the black hole, and to “decode”
the Hawking radiation output of the black hole in terms of a strategy recommendation. For a generic
problem, the computational resources needed to encode and decode the question are expected to be no
smaller than the computational resources required to just solve the problem directly, without reference
to the black hole. For generic problems, therefore, black holes don’t help. (See Chapter 6 of [40].)
12
