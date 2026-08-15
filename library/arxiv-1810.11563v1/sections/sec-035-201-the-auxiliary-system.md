---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-035-201-the-auxiliary-system
section_title: "The Auxiliary System"
section_number: 20.1
pages: 69-70
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
Instead of using operator complexity I’m going to work with state complexity for the rest
of this lecture. State complexity is the number of gates that it takes to go from a simple
unentangled state of K qubits to the state in question.
Physical states can be described as normalized vectors in the Hilbert space of K qubits
with the phase modded out. In other words they are points on CP (2K− 1). The evolution
of a state is represented by an “auxilliary system” https://arxiv.org/pdf/1701.01107.
pdf—a ﬁctitious classical system moving on CP (2K− 1).
One way of representing a state is by the coeﬃcients in the expansion of the state
in some basis—say the computational basis. Thus a state of K qubits is labeled by 2 K
complex numbers,
|ψ⟩→ (α1,α 2,......α 2K) (20.84)
The α can be thought of as coordinates of a point in the phase space of the Auxiliary
system. Since the dimension of the space is 2 K we can roughly picture the system as a
classical collection of 2K particles. That’s more than enough to do statistical mechanics.
68
As I explained in Lecture I, the entropy of this auxiliary system is the average com-
plexity of an ensemble of states. The second law of complexity (analogous to the second
law of thermodynamics) states that the complexity tends to increase https://arxiv.
org/pdf/1701.01107.pdf . In fact the second law of complexity is the second law of
thermodynamics applied to the auxiliary system. As in the case of thermodynamics, when
the number of degrees of freedom becomes large the tendency for complexity to increase
becomes overwhelming.
Starting with a simple unentangled state and evolving it for an exponential time will
bring the state to complexity equilibrium (maximal complexity) analogous to thermal
equilibrium. Complexity equilibrium is a far more thorough mixing of degrees of freedom
than thermal equilibrium and takes a much longer time to be established. Being out of
complexity equilibrium is much more subtle than being out of thermal equilibrium. Thermal
equilibrium is about local easily measured correlations: complexity equilibrium is about
extremely subtle global correlations which are very hard to detect. A system can easily be
in thermal equilibrium and still very far from complexity equilibrium.
The parallel with entropy suggests that we deﬁne a resource analogous to negentropy.
The term that Adam Brown and I coined for this resource is uncomplexity. We might have
called it Negcomplexity but we didn’t. Some people have suggested the term simplicity,
but a state can have lots of uncomplexity and still be very complex.
Uncomplexity is deﬁned by analogy with Negentropy,
Uncomplexity =Cmax− C (20.85)
where for a system of K qubits the maximum state complexity is 2 K. Just as negentropy
is the room for entropy to grow, uncomplexity is the room for complexity to grow. The
idea is that uncomplexity is a resource for doing some kind of work. In this case work does
not refer to lifting a weight, but of doing directed computation, i.e., computation with a
goal.
