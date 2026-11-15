---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-028-52-the-mallows-measure
section_title: "The Mallows Measure"
section_number: 5.2
pages: 104-105
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.968
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Given a permutation of $n$ numbers $\pi\in S_n$, we define the inversion number $\mathrm{Inv}(\pi)$ to be $$\mathrm{Inv}(\pi)=\#\{(i,j) \; : \;i<j \;\mathrm{and}\; \pi(i)>\pi(j)\}$$ For each $q\in(0,1)$, the Mallows measure [@Mallows] is defined by $$\mu_{n,q}(\pi)=\frac{q^{\mathrm{Inv}(\pi)}}{Z_{n,q}}$$ where $Z_{n,q}$ is a normalization constant given by $$Z_{n,q}=\sum_{\pi\in S_n} q^{\mathrm{Inv}(\pi)}=\prod_{k=1}^n\frac{1-q^k}{1-q}=[n]_q!$$ where $[n]_q!$ is as stated in the previous chapter. The measure is related to the Iwahori-Hecke algebra as shown by Diaconis and Ram [@DiaconisRam]. Note that for $q=1$, the Mallows measure is just the uniform measure on $S_n$, with all $n!$ permutations equally likely.
