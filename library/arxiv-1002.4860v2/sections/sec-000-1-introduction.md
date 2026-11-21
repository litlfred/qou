---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.935
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
In [@Jones], Jones gave a construction of the two-variable HOMFLY-PT polynomial invariant using a recursively defined Markov trace on certain representations of the braid group. These representations all factor through the Iwahori-Hecke algebra $\mathcal{H}_n$ (of type A), which enjoys a character theory [@Geck] deforming that of the symmetric group. The Markov trace can be decomposed as a linear combination of irreducible characters $\chi_\lambda$ of the Hecke algebra: $$\label{jones}
\tau = \sum_{\lambda\vdash n} \omega_\lambda(q,z) \chi_\lambda.$$ The coefficients $\omega_\lambda(q,z)$ in this "Fourier expansion" were calculated by Ocneanu using Schur functions (see, e.g., [@GeckJacon]). By summing only the components corresponding to hook partitions, and specializing $z \to q^{-1}$, the Alexander polynomial $\Delta(L)$ of a link $L$ is recovered. In this paper, we use ([\[jones\]](#jones){reference-type="ref" reference="jones"}) to develop a diagrammatic formalism for calculating $\Delta(L)$ as a state-sum derived from a braid presentation of the link $L$.

The rest of the paper is organized as follows. In Section [\[sec s-n\]](#sec s-n){reference-type="ref" reference="sec s-n"}, we review some of the representation theory of the Hecke algebras of type A, using the Hecke algebra analogue of Young's semi-normal form from [@Hoefsmit]. We introduce some combinatorics specific to tableaux of hook shape, and recast the formulas in this language. In Section [\[sec constr\]](#sec constr){reference-type="ref" reference="sec constr"}, we describe the construction of the state-sum and derive the main theorem (Theorem [\[main thm\]](#main thm){reference-type="ref" reference="main thm"}). An example is calculated explicitly in Section [\[sec ex\]](#sec ex){reference-type="ref" reference="sec ex"}.

It is also possible to give a direct proof of our main theorem by verifying that our formulae give a link invariant satisfying the Conway skein relations; see [@Black]. In subsequent work, I hope to generalize these results to colored braids and the multivariable Alexander polynomial.

*Acknowledgements.* I thank my advisor Arkady Vaintrob for suggesting this work and Jonathan Brundan for showing me that an analogue of Young's semi-normal form exists for Hecke algebras. I would also like to thank Victor Ostrik for many interesting conversations along the way.
