---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-043-222-expending-uncomplexity-and-negentropy
section_title: "Expending Uncomplexity and Negentropy"
section_number: 22.2
pages: 75-76
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.987
---
The uncomplexity of $|max\ra$ is zero but by adding the clean qubit we bought ourselves an uncomplexity $2^K.$ But the action of the circuit will inevitably increase the complexity by roughly the number of applied gates. Assuming that \ref{G=gg} is the minimal description of $G$ then we can expect the increase of complexity to  be of order $n$ which is also the complexity of $G$. To put it another way, the application of the circuit decreases the uncomplexity from $2^K$ to $ \big( 2^K - \CC(G) \big)$. In other words the computational work in computing $\Tr G$ expends an uncomplexity  equal to the complexity of $G$.


In this example uncomplexity is not the only resource we made use of. A maximally complex state is also a state of maximum entropy which in this case is $S = K \log 2.$ The addition of the clean qubit does not change the entropy, but after the circuit has acted the clean qubit is no longer clean. This implies that the entropy increases but only by an amount less than or equal to one bit. Thus we have also expended Negentropy, but no more than one bit.

One bit of negentropy can be stored in a single qubit, but obviously a single qubit cannot  by itself be used to calculate $\Tr G$. Evidently in this case we needed both the large uncomplexity and a tiny bit of negentropy to do the computation.
