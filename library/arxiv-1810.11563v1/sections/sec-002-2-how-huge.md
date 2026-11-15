---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-002-2-how-huge
section_title: "How Huge?"
section_number: 2
pages: 5-6
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Let's consider the space of states of $K$ qubits and make a simple estimate of its size. By size I don't mean the dimensionality of the space defined by the number of mutually orthogonal vectors. I mean something more like the total number of unit vectors. It's of course infinite but we can regulate it.

The dimension of the Hilbert space is $2^K$ and a general vector has the form,

$$|\Psi\ra  = \sum_1^{2^K} \alpha_i |i\ra$$

The $\alpha$ are arbitrary complex numbers. At the moment we won't worry about normalizing $|\Psi\ra$ or dividing out the overall phase. Now let's regulate the infinities by restricting each 
$\alpha_i$ to be one of $m$ values. The total number of states is,

\be
\#states = m^{2^K} = \exp{(2^K \log{m})}
\label{states}
\ee
For $K=4, \ m=4$ the number of states is $4,294,967,296.$




The logarithm of the number of states is more manageable,
\be
\log{(\#states})=2^K \log{m} \approx 22.
\label{logstates}
\ee

There are two interesting things about \ref{logstates}. The first is how strongly it depends on $K,$ namely it grows as $2^K$. The second is how weakly it depends on the regulator parameter $m$. We'll see this trend many times  in what follows.
