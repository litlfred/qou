---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-006-22-alternative-proofs
section_title: "Alternative proofs"
section_number: 2.2
pages: 6-6
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
There are many possible approaches to proving the Basic Lemma. The proof given above is a compromise of sorts, since it proves the existence of an appropriate element of $H_2(\tilde{C})$, but does so in a non-constructive way.

It is possible to give a more constructive proof which uses an explicit computation of $H_2(\tilde{C})$. One obtains a concrete description of an immersed genus two surface which can be seen to be the same as $(1-q)^2(1+qt)\tilde{\Sigma}(F)$ away from the puncture points. This is perhaps best done in private, since the details are only convincing to the person who figures them out. Some details of a computation of $H_2(\tilde{C})$ will be given in Section [\[lkmatrices\]](#lkmatrices){reference-type="ref" reference="lkmatrices"}. See also [@lawrence], where similar methods are used to calculate the middle homology of the space of *ordered* $k$-tuples of distinct points in the $n$-times punctured disc, where $k$ can be any positive integer.

It is tempting to seek a less constructive proof which makes no reference to $\tilde{\Sigma}_2(F)$. It is intuitively obvious that the problem of pushing intersections off to infinity does not arise in the context of forks and noodles. However this line of reasoning runs into some technical difficulties which I feel distract from the true nature of the problem at hand. A proof that $B_n$ acts faithfully on $H_2(\tilde{C})$ should refer to an element of $H_2(\tilde{C})$.

It is possible to prove that braid groups are linear without reference to $C$, let alone $H_2(\tilde{C})$. The Lawrence-Krammer representation can be defined to be the action of $B_n$ on a $\Lambda$-module consisting of formal linear combinations of forks subject to certain relations, as described by Krammer in [@krammer]. The pairing $\langle N,F \rangle$ can be defined solely in terms of winding numbers. One must check that this pairing respects the relations between forks. The Basic Lemma then follows immediately. The rest of the proof that the Lawrence-Krammer representation is faithful proceeds virtually unchanged.
