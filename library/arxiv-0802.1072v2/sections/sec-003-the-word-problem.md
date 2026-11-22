---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-003-the-word-problem
section_title: "The word problem:"
section_number: null
pages: 4-5
source_pdf: 0802.1072v2.pdf
source_sha256: 6f4d93f0b7ba5cd7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
Xu's solution to the word problem builds directly on the analogous ideas in the work of Garside [@Ga]. Choose any word $W$ in the symbols $a_1,a_2,a_3$ and their inverses, representing an element $\beta\in B_3$. Using ([\[E:BKL presentation\]](#E:BKL presentation){reference-type="ref" reference="E:BKL presentation"})(i), all inverses of generators can be traded for powers of $\delta^{-1}$. Using ([\[E:BKL presentation\]](#E:BKL presentation){reference-type="ref" reference="E:BKL presentation"})(ii), all powers of $\delta$ may be collected, say, at the left, so that one may rewrite $W$ in the form $\delta^kP$, where $k\in \mathbb N$ and $P$ is a *positive* word. Positive words contain powers of $\delta$ if and only if two adjacent letters $a_{i+1}a_i$ appear, so after a simple search we may change $\delta^kP$ to a word of the form $\delta^qa_{r_1}a_{r_2}\cdots a_{r_s}$ where $q$ is maximal and the positive word $a_{r_1}a_{r_2}\cdots a_{r_s}$ contains no adjacent letters of the form $a_{i+1}a_i$. Rewriting our word in syllable form $X = \delta^qa_{\tau_1}^{s_1}\dots a_{\tau_t}^{s_t}$, we see that the subscripts must be strictly increasing. The integer $q$ is the *power*, and the positive word is the *tail*. This solves the word problem in $B_3$.

We give an example. The following set of moves bring the flype-admissible braid $W=a_1^{-2}a_2^{-3}a_1^5 a_2$, which is not in normal form, to its normal form $\delta^{-4}a_2^2a_3a_1^5a_2$: Use (i) to modify $W   = a_1^{-2}a_2^{-3}a_1^5 a_2$ to $(\delta^{-1}a_2)^2(\delta^{-1}a_3)^3a_1^5a_2$. Now use (ii) to modify $(\delta^{-1}a_2)^2(\delta^{-1}a_3)^3a_1^5a_2$ to $\delta^{-2} a_1a_2  \delta^{-3 }a_1 a_2a_3 a_1^5a_2$ and then to $\delta^{-5}a_1a_2 a_1a_2a_3a_1^5a_2^4$. Finally, observe that $\delta=a_2a_1$ is a subword of the tail of $\delta^{-5}a_1a_2 a_1a_2a_3a_1^5a_2^4$, so we can move it to the left to obtain $\delta^{-4}a_2^2a_3a_1^5a_2.$ The subscripts in the tail are strictly increasing, so we are done.
