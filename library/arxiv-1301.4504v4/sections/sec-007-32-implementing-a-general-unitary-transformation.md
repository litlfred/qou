---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-007-32-implementing-a-general-unitary-transformation
section_title: "Implementing a General Unitary Transformation with Quantum Gates"
section_number: 3.2
pages: 19-23
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.985
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
[]{#compsec label="compsec"} In our world, the result of the previous section, that doing a quantum computation at worst takes a time which is double exponential in the entropy of the computer, had better not be optimal if we are ever to do any quantum computation at all. It can be improved upon of course, and the reason is that locality of interactions makes the dependence of $U_{comp}$ on time and computer size very special indeed.[^1] Since no quantum computer has yet been built we do not know exactly how one might be implemented physically, but there is a widely accepted model for quantum computation called the *quantum circuit model*. In the quantum circuit model one imagines having a "quantum memory" consisting of $n$ qubits, on which one can easily act with some finite set of one- or two-qubit unitary transformations, called *quantum gates*, on any qubit or pair of qubits. The computer builds up larger unitary transformations by applying the various gates successively. Interestingly the number of different types of gates needed to generate arbitrary unitary transformations with high precision is quite small. In fact, one is sufficient provided it is generic enough and that it can be applied to any two of the qubits (and in either order on those two). A set of gates having this property is called *universal*. A specific set of three gates which is universal is the *Hadamard* gate, which acts on a single qubit as $$\begin{aligned}
\nonumber
H|0\rangle=&\frac{1}{\sqrt{2}}\left(|0\rangle+|1\rangle\right)\\
H|1\rangle=&\frac{1}{\sqrt{2}}\left(|0\rangle-|1\rangle\right),
\end{aligned}$$ the $Z^{1/4}$ gate which acts on a single qubit as[^2] $$\begin{aligned}
\nonumber
Z^{1/4}|0\rangle=&|0\rangle\\
Z^{1/4}|1\rangle=&e^{\frac{i\pi}{4}}|1\rangle,
\end{aligned}$$ and the *CNOT* gate $U_{cnot}$, for "controlled not", which acts on two qubits as $$U_{cnot}|b_1,b_2\rangle=|b_1,b_1+b_2\rangle$$ with the addition being mod $2$. This gate flips the second bit if and only if the first bit is $1$. There is a standard graphical notation for representing circuits, which we have already used in figure [\[bigcomp\]](#bigcomp){reference-type="ref" reference="bigcomp"}, and we illustrate it some more in figure [1](#gates){reference-type="ref" reference="gates"}.

<figure id="gates">
<div class="center">
<embed src="gates.pdf" style="height:4cm" />
</div>
<figcaption>The standard representations of the three gates described in the text, as well as a simple circuit that maps the product basis <span class="math inline">|<em>b</em><sub>1</sub>, <em>b</em><sub>2</sub>⟩</span> to a basis each element of which has the two qubits maximally entangled. In the CNOT gate the addition is done at the hollow circle.</figcaption>
</figure>

We can now ask how many gates are needed to make a complicated unitary transformation like $U_R$ in equation [\[compPsi\]](#compPsi){reference-type="eqref" reference="compPsi"}. This is a good measure of the amount of time/space needed to actually do the computation, since we can imagine that the gates can be implemented one after another in a time that scales at most as a small power of $n$. For a set of $f$ fundamental gates, the number of circuits we can make which use $T$ total gates is clearly $$\left(\begin{pmatrix}
n\\
2
\end{pmatrix}f\right)^{T}\approx (n^2f)^{T}.$$

To proceed further we need some basic idea of size and distance for the unitary group. The unitary group on $n$ qubits is a compact manifold of dimension $2^{2n}$, and we can parametrize its elements as $$U=e^{i\sum_{a=1}^{2^{2n}}c_a t^a}.$$ Here $t^a$ are generators of the Lie algebra of $U(2^n)$, and we can very roughly think of the $c_a$'s as parametrizing a unit cube in $\mathbb{R}^{2^{2n}}$. Also roughly we can think of linear distance in this unit cube as a measure of distance between the unitaries. For example say we wish to compute the difference between acting on some pure state $|\Psi\rangle$ with two different unitary matrices $U_1$ and $U_2$ and then projecting onto some other state $\chi$: $$\langle\chi|(U_1-U_2)|\Psi\rangle=\langle\chi|\left(I-U_2U_1^\dagger\right)U_1|\Psi\rangle\approx -i\langle\chi|\sum_a \delta c_a t^a U_1|\Psi\rangle.$$ If the sum of the squares of the $\delta c_a$'s is less than $\epsilon^2$, the right hand side will be at most some low order polynomial in $2^n$ times $\epsilon$. This polynomial is irrelevant as we now see.

Around each of our $(n^2f)^{T}$ circuits we can imagine a ball of radius $\epsilon$ in $\mathbb{R}^{2^{2n}}$. The volume of all the balls together will be of order the full volume of the unitary group when $$(n^2 f)^{T}\epsilon^{2^{2n}}\approx 1.$$ Thus we see that in order to be able to make generic elements of $U(2^n)$ we need at least $$T\sim 2^{2n}\log\left(\frac{1}{\epsilon}\right)$$ gates, where we have kept only the leading dependence on $n$ and $\epsilon$. As promised, because $\epsilon$ appears inside a logarithm the crude nature of our definition of distance has not mattered. More importantly, we see that the number of gates is now only a single exponential in (twice) the entropy. The fact that this crude counting bound can be achieved by an appropriate sequence of gates is known as the Solovay-Kitaev theorem. So the quantum circuit model is able to do arbitrary quantum computations much faster than our calculation of the previous section suggested; this is essentially because locality enables us to dynamically isolate parts of of the computer in such a way that we can push the chaos of the system into heating the environment (not explicitly modeled here) instead of messing up our computation.

Given that we have so quickly beaten down a double exponential to a single exponential, one might be optimistic that further reduction in computing time is possible. Unfortunately, in our universe that does not seem to be the case. Simple modifications of the quantum circuit model such as changing the set of fundamental gates or considering higher spin fundamental objects instead of qubits, for example qutrits, make only small modifications to the analysis and don't change the main $2^{2n}$ scaling. One could imagine trying to engineer gates that act on some finite fraction of the $n$ qubits all at once, perhaps by connecting them all together with wires or something, but it is easy to see that any such construction requires a number of wires exponential in $n$. One could also try to parallelize by applying gates on non-overlapping qubits simultaneously whenever possible, as well as adding additional "ancillary" qubits. As long as the number of extra qubits scales like some power of $n$, however, it is clear they cannot beat the $2^{2n}$. Even with exponentially many ancilla or wires just the travel time between the various parts of the computer will be exponential in $n$. In the face of these difficulties the reader might be tempted to try using some sort of exotic nonlocal system like a black hole to do the computation, but this would just give up what the circuit model accomplished and most likely return us to even worse situation of the previous section. In this paper we will adopt the widely held point of view that the quantum circuit model accurately describes what are physically realistic expectations for the power of a quantum computer.

Thus if $U_{R}$ has no special structure, we do not expect Alice to be able to implement it (or its inverse) in time shorter than $2^{2n}$. As discussed below equation [\[compPsi\]](#compPsi){reference-type="eqref" reference="compPsi"} however, $U_R$ was defined only by its action on a subspace of dimension $2^{k+m}$. In studying the complexity of $U_R$ we are free to quotient $U(2^n)$ by multiplication on the right by a block diagonal matrix which acts as the identity on the subspace spanned by states of the form $|bh0\rangle$. The dimensionality of this quotient is $2^{k+m+n}$, and since it is good enough to find a circuit which produces any element of the coset containing $U_R$ the counting argument of this section suggests that Alice will be able to use a decoding circuit implementable in a time scaling like $$\label{dectime}
T\sim2^{k+m+n}.$$

[^1]: This subsection is entirely pedagogical and contains no original material, good references are [@kitaev2002classical; @preskillnotes; @nielsen2010quantum].

[^2]: In this equation we see the unfortunate but standard convention in quantum computation theory that the Pauli-$z$ operator, usually written as $Z$, acts as $Z|0\rangle=|0\rangle$ and $Z|1\rangle=-|1\rangle$. The Hadamard operator can then be interpreted as switching from the $Z$ eigenbasis to the $X$ eigenbasis. As an example it is worth seeing to see how to build the Pauli operators $X$, $Y$, and $Z$ out of $H$ and $Z^{1/4}$ gates.
