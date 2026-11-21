---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-042-21-uncomplexity-as-a-resource
section_title: "Uncomplexity as a Resource"
section_number: 21
pages: 72-73
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In discussing computational work it is helpful to separate what can be done by reversible (unitary) operations from what can be done by applying measurements. Starting with a maximally complex state, or any other state, the complexity can be eliminated by  measuring  all Pauli $Z$ operators. The outcome will be a unentangled product state which can be brought to the state $|000...0\ra$ by applying no more than $K$ single qubit gates. This would have the effect of restoring the uncomplexity to its maximal value\footnote{Notice that we did the same thing by adding a single clean qubit.}.



But measurements are not reversible operations, and necessarily dump heat into the environment. By computational work I will mean the part of a protocol that can be achieved reversibly. For example we may want to reversibly transform the state from some input to a target state that has some information that we can later extract by making a measurement. The computational work by definition is associated with the \it reversible transformation only, \rm and not with the \it final measurement.
\rm

For most purposes maximally complex pure states cannot be distinguished from maximally mixed density matrices. Both will give random results for almost all measurements. Since a reversible operation on a maximally mixed state does nothing, maximally mixed and maximally complex states are useless as a starting point for doing computational work.

Thus to do computational work we need some uncomplexity, i.e., some separation between the actual complexity of a computer, and maximal possible complexity $2^K.$ Uncomplexity is therefore a necessary resource, but it is not generally sufficient. What I am going to show you, by a concrete example, is how adding a single clean  qubit to a maximally complex system of $K$ qubits restores the ability to do a great deal of computational work.
