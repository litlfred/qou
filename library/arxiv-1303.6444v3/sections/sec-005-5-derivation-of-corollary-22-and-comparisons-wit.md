---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-005-5-derivation-of-corollary-22-and-comparisons-wit
section_title: "Derivation of Corollary 2.2 and comparisons with previous results"
section_number: 5
pages: 7-7
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.871
latex_coverage_ratio: 0.964
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
[]{#sec: oldbounds label="sec: oldbounds"}

## Derivation of Corollary [\[cor:lebpenbound\]](#cor:lebpenbound){reference-type="ref" reference="cor:lebpenbound"}

We have the bound on cluster expansions from [@R69] as: $$|nb_n| \leq \frac{n^{n-1}}{n!}e^{2\beta B(n-2)}C(\beta)^{-1}$$ Where, the parameter $C(\beta)< \infty$ defines a tempered potential, which is defined in [\[Cbeta\]](#Cbeta){reference-type="eqref" reference="Cbeta"}, and $B$ is the stability parameter from Assumption [\[ass: stability\]](#ass: stability){reference-type="ref" reference="ass: stability"}. This corresponds to setting the parameters in the previous section to: $$\begin{aligned}
 a &= C(\beta)^{-1}e^{-4\beta B} \\
b &= e^{2\beta B}C(\beta) \\
ab &= e^{-2\beta B} \\
\mu = \frac{eab}{1+ab} &= \frac{e}{1+e^{2\beta B}} 
\end{aligned}$$ This gives: $$|c_n| \leq \frac{\beta^{-1}}{n}\left(C(\beta)e^{4\beta B} \frac{W\left(\frac{e}{1+e^{2\beta B}}\right)}{(W\left(\frac{e}{1+e^{2\beta B}}\right)-1)^2}\right)^{n-1}$$ with the radius of convergence satisfying: $$\mathcal{R}_{\text{Vir}} \geq C(\beta)^{-1}e^{-4\beta B}\frac{(W\left(\frac{e}{1+e^{2\beta B}}\right)-1)^2}{W\left(\frac{e}{1+e^{2\beta B}}\right)} \label{firstbound}$$
