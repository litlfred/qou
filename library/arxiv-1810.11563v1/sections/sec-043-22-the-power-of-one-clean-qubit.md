---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-043-22-the-power-of-one-clean-qubit
section_title: "The Power of One Clean Qubit"
section_number: 22
pages: 73-73
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
That a resource analogous to negentropy can be vastly increased by merely adding a single qubit seems very counterintuitive. If I told you that by adding a single molecule to a gas of $10^{30}$ molecules in thermal equilibrium, it  would allow you to extract a large amount of useful work you would probably dismiss the claim as nonsense. You would of course be right. When I first thought about the fact that a single qubit can restore an exponential amount of uncomplexity I was skeptical about its meaning. So as I always do when I am confused about quantum information I went to Patrick Hayden. I asked him: Can adding one qubit to a computer significantly increase its power?


Patrick listened to my story and was less dismissive than I thought he would be. He said that it reminded him of something called \it one clean qubit computation. \rm \ After some Googling I found the original paper ``On the Power of One Bit of Quantum Information" by Ray Laflamme  (the same as in Gregory-Laflamme)  and Emanuel Knill (quant-ph/9802037). What I'm going to explain is a slightly modified version of their method.



To illustrate the power that we gain from a single clean qubit, let's consider the problem of computing the trace of a unitary operator in $SU(2^K).$ There are a number of problems that reduce to computing such a trace. Unfortunately computing the trace of a $2^K \times 2^K$ matrix is very hard for the simple reason that it means adding $2^K$ numbers. 

I will call the unitary whose trace is to be computed $G.$ $G$ itself has some complexity which is defined by the minimal number of gates satisfying 
\be 
G = g_n \ g_{n-1}....g_1.
\label{G=gg}
\ee
The object is to start with the maximally complex state of $K$ qubits, add a single qubit,
\be 
|max\ra |0\ra,
\ee
and then transform it to a state that has some accessible information about $\Tr G$. It would also be highly preferable to do it in a way that does not depend of the particular maximally entangled state $|max\ra$ since describing such a state is itself exponentially difficult.
