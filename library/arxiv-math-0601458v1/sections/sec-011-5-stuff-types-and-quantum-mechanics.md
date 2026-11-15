---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-011-5-stuff-types-and-quantum-mechanics
section_title: "Stuff Types And Quantum Mechanics"
section_number: 5
pages: 30-30
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
[]{#stuff-quantum-sec label="stuff-quantum-sec"}

Now we will return to our original motivation - seeing stuff types as a categorification of states of the quantum harmonic oscillator. We have already seen how stuff types can take the role of formal power series, at least up to the level of linear structure. The space of formal power series should be the Hilbert space of states of the quantum oscillator: so composition of stuff types, which we have explored, will not enter into this picture, though the linear structure will. If stuff types are categorified power series, and the 2-category $\boldsymbol{\operatorname{{StuffTypes}}}$ is a categorified Fock space some of the basic structure for a Hilbert space[^1]. One difficulty is that we do not have additive inverses, and another is that we lack an inner product (which any Hilbert space must have, and which we need to calculate probabilities in a quantum system).

Interestingly, while the additive inverses are rather tricky to define, and will have to wait until section [\[mstuff\]](#mstuff){reference-type="ref" reference="mstuff"} when we define $M$-stuff types, the inner product does not even need to be defined as a special construction, or imposed as extra structure: a canonical one arises directly from the categorified framework as a (in part because by describing stuff types as functors into $\boldsymbol{\operatorname{{Set}}}$, we are in effect choosing an ordered basis for this categorified equivalent of a Hilbert space). What is more, a Hilbert space should have an algebra of linear operators - endofunctions - which acts on it. We need to see what the equivalents of operators on stuff types are before we can use them to categorify the oscillator. We will see that these are directly related to the inner product.

[^1]: A treatment of the construction of Hilbert spaces from structure types appears in [@maassen].
