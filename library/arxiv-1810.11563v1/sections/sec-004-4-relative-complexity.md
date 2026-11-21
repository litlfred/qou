---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-004-4-relative-complexity
section_title: "Relative Complexity"
section_number: 4
pages: 7-9
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.995
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The enormity of the space of states of quantum systems begs the question of how to measure the distance between states. Are some states close to each other and others enormously far? The usual metric in state space (by which I mean $CP(N)$) is the inner-product metric. It's also called the Fubini-Study (FS) metric. The FS distance between two vectors $|A\ra$ and $|B\ra$ is,
\be 
d_{fs}(A,B) = \arccos{|\la A |B\ra|}.
\ee
It varies from $d_{fs}=0$ when $|A\ra = |B\ra$ to $\pi/2$ when $|A\ra$ and $ |B\ra$ are orthogonal. The space with the FS metric is ``small" in the sense that the furthest distance between points is $\pi/2.$


The FS metric has its purposes but it fails to capture something important. Imagine an intricate piece of machinery with a microscopic switch---a control qubit---that can be flipped on or off. Compare the distance between these two states, 
$$
|\bf{on}\ra     \ \ \   \ \ \   |\bf{off}\ra
$$

 with the distance between two other states: a brand new machine,  and  a pile of rust,
$$
|\bf{new}\ra        \ \ \  \ \ \   |\bf{rust \ pile}\ra
$$ 
 
 
  The FS distance between states $|\bf{new}\ra $ and $|\bf{rust \ pile}\ra$ is exactly the same as the distance between $|\bf{on}\ra $ and $|\bf{off}\ra $, namely $\pi/2$. If the only criterion was the FS distance it would be just as easy to:


\begin{enumerate}
\item Make a transition from $|\bf{new}\ra $ to 
$|\bf{rust \ pile}\ra $ as to make a transition from $|\bf{on}\ra $ to $|\bf{off}\ra $.

\item Create a coherent superposition of $|\bf{new}\ra $ and $|\bf{rust \ pile}\ra$, or a coherent superposition of $|\bf{on}\ra $ and $|\bf{off}\ra $.

\item Do a measurement that would be sensitive to the relative phases of such superpositions in the two cases.
\end{enumerate}

But of course this is not true. It is much easier  make a superposition of $|\bf{on}\ra $ and $|\bf{off}\ra $ (it just involves superposing two single-qubit states) than of $|\bf{new}\ra $ and $|\bf{rust \ pile}\ra $. Evidently the FS metric fails to capture the difference between these two cases.

If it were equally possible to physically apply \it any \rm operator to a system, then it would be no harder to superpose the machine and the rust pile, than the on-off states. But in the real world an operator that takes a machine to a rust pile is much more \it complex \rm than an operator that flips a qubit. In practice, and maybe in principle, we carry out very complex operations as sequences of simple operations. Once a set of  ``allowable" simple operations has been identified, a new measure of distance between states becomes possible. It can be defined as:

\bn
\it The minimal number of simple operations needed to go from 
$|A\ra$    to $|B \ra $.\rm  

\bn
In (quantum)information theory the simple operations are called gates and new distance measure is called relative complexity:

\bn \it

The relative complexity of $|A\ra$ and $|B\ra $  is the minimum number of gates required to go from $|A\ra$ to $|B\ra $.
\rm

\bn
One might object that relative complexity is a somewhat subjective idea since it depends on a choice of simple operations. But in a qubit context a simple operation is one that involves a small number of qubits. For example we might allow all one and two-qubit gates  as simple operations. Relative complexity would then be fairly well defined\footnote{There are still details associated with how precisely a product of gates must approximate a target state.} But then a skeptic may say: Yes, but what happens to your definition of complexity if I decide to allow three qubit gates?

I expect (but cannot prove) that the answer is: Not much happens at least for large complexity.  There are two kinds of ambiguities to worry about---additive and multiplicative. The additive ambiguities are associated with precision---how close do we have to get to the target to declare success? If we are required to get within inner-product distance $\epsilon,$ then there is an additive term in the complexity,  logarithmic in $\epsilon.$  It is closely related to the logarithmic ambiguity in  \ref{balls-in-CP}. 


There is also a multiplicative ambiguity when we go from allowing only one and two qubit gates to allowing three qubit gates. That is because a three qubit gate can be approximated by some number of one and two qubit gates. That ambiguity  can be accounted for as long as the complexity is not too small. 

A basic assumption is that there a set of definitions of quantum complexity that exhibit a universal behavior up to additive and multiplicative ambiguities. 
The important rule is that the allowable gates must be restricted to be \kl \ with $k$ much smaller than the number of qubits comprising the system. What \kl \ means is that the gate involves no more than $k$ qubits.





We'll have more to say about relative complexity but let's first discuss the dual role of unitary operators.
