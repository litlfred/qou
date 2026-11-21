---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-032-2-braiding-and-fusion
section_title: "Braiding and Fusion"
section_number: 2
pages: 24-25
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
The braiding and fusion rules for $\mathbb{Z}/N\mathbb{Z}$ theories are particularly simple. Braiding two identical particles, one encounters the Dirac string of the other, which introduces a phase:

$$R | a , n \rangle | a , n \rangle = e^{\frac{2 \pi i}{N} (n a) } | a , n \rangle  |a, n \rangle$$

For non-identical particles, only the monodromy operator makes sense: $$R^2 | a , n \rangle | a' , n' \rangle = e^{\frac{2 \pi i}{N} (n a' +n' a) } | a , n \rangle  |a', n' \rangle$$

The fusion rules for this theory amount to summing the charges and fluxes mod N:

$$| a , n \rangle \times | a' , n' \rangle = | [a+a'] , [n+n'] \rangle$$

Instantons in effect perform the modulo N summation. The charge conjugation operator takes each charge, flux combination to the additive inverse charge, flux mod N. This in fact corresponds to the antiparticle. Note that the only $\mathbb{Z}/N\mathbb{Z}$ gauge theories which contain a Majorana particle (i.e. a particle that is its own antiparticle) are those for which $N$ is even. In that case, the only Majorana particle has both flux and charge $\frac{N}{2}$.
