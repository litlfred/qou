---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-007-16-proof
section_title: "Proof"
section_number: 1.6
pages: 5-6
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.951
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
[]{#subsecProof label="subsecProof"} We just honestly start from $n=1$: $$\begin{gathered}
 Q^{-1}u_1^{}Q=Q^{-1}u_1^{}
  b_1^{}b_2^{}b_3^{}\ldots b_{N-1}^{}=Q^{-1}
  b_1^{}\sum_{a=-\infty}^\infty q^{a^2+2a}u_2^a
  u_1^{}b_3^{}\ldots b_{N-1}^{}                \\
  =Q^{-1}b_1^{}b_2^{}q^{-1}u_2^{-1}
  u_1^{}b_3^{}\ldots b_{N-1}^{}=Q^{-1}b_1^{}
  b_2^{}b_3^{}u_2^{-1}u_1^{}u_3^{}b_4^{}
  \ldots b_{N-1}^{}=\cdots 
\end{gathered}$$ --- every step adds another factor, in the end parity of $N$ and that center-reducing condition ([\[eq:c1c2\]](#eq:c1c2){reference-type="ref" reference="eq:c1c2"}) make all the difference --- $$\cdots=Q^{-1}Q(u_2^{}u_4^{}\ldots
u_{N-2}^{})^{-1}u_1^{}u_3^{} \ldots u_{N-1}^{}=u_{N}^{}.$$ We may seem to have done only one very particular case, but, luckily, the rest is little more than tautology. It immediately follows that $Q^{-1}b_1Q=b_N$, which can be written as $$Q=b_1^{-1}Qb_N^{}
=b_2^{}b_3^{}\ldots b_N^{},$$ which in turn just means that $Q=\hat Q$ and therefore anything good for $n=1$ at once becomes just as good for all $n$. That is it.

In the process, a seeming contradiction between the "open-ended" appearance of the evolution operator and the cyclic nature of its action has resolved itself. Since $$Q=b_1b_2\ldots b_{N-1}=\hat Q=b_2b_3\ldots
b_N=\hat{\hat{Q}}=\cdots =b_Nb_{N+1}\ldots b_{N-2}\;,$$ whichever of these forms one chooses to express $Q$ in, it always remains an ordered product but each time starts from another point, in this sense it does not depend on the starting point, or rather does not have one. The next subsection offers an explanation of this miracle.
