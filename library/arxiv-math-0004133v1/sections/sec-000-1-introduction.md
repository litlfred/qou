---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.996
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
Prediction is hard, especially when it comes to the future, but barring some unforeseen catastrophe, we can expect the amount of mathematics produced in the 21st century to dwarf that of all the centuries that came before. By the very nature of its subject matter, mathematics is capable of limitless expansion. Thanks to rapid improvements in technology, our computational power is in a phase of exponential growth. Even if this growth slows, we have barely begun to exploit our new abilities. Thus the interesting question is not whether the 21st century will see an unprecedented explosion of new mathematics. It is whether anyone will ever understand more than the tiniest fraction of this new mathematics --- or even the mathematics we already have.

Will mathematics merely become more sophisticated and specialized, or will we find ways to drastically simplify and unify the subject? Will we only build on existing foundations, or will we also reexamine basic concepts and seek new starting-points? Surely there is no shortage of complicated and interesting things to do in mathematics. But it makes sense to spend at least a little time going back and thinking about *simple* things. This can be a bit embarrassing, because we feel we are supposed to understand these things completely already. But in fact we do not. And if we never face up to this fact, we will miss out on opportunities to make mathematics as beautiful and easy to understand as it deserves to be.

For this reason, we will focus here on some very simple things, starting with the notion of equality. We will try to show that by taking pieces of elementary mathematics and *categorifying* them --- replacing equations by isomorphisms --- we can greatly enhance their power. The reason is that many familiar mathematical structures arise from a process of *decategorification*: turning categories into sets by pretending isomorphisms are equations.

In what follows, we start with a discussion of equality versus isomorphism, and a brief foray into $n$-categories and homotopy theory. Then we describe in detail how the natural numbers and the familiar operations of arithmetic arise from decategorifying the category of finite sets. This suggests that a deeper approach to arithmetic would work not with natural numbers but directly with finite sets. This philosophy has already been pursued in many directions, especially within combinatorics. As an example, we describe how formal power series rise from decategorifying André Joyal's 'structure types', or 'espèces de structures' [@Joyal; @Joyal2]. A structure type is any sort of structure on finite sets that transforms naturally under permutations; counting the structures of a given type that can be put on a set with $n$ elements is one of the basic problems of combinatorics. We also describe a useful generalization of structure types, which we call 'stuff types'.

To hint at some future possibilities, we conclude by showing how to understand some combinatorial aspects of quantum theory using stuff types. First we define an inner product of stuff types and note that, with this inner product, the category of stuff types becomes a categorified version of the Hilbert space of a quantized harmonic oscillator. Then we show that the theory of Feynman diagrams arises naturally from the study of 'stuff operators', which are gadgets that turn one stuff type into another in a linear sort of way.
