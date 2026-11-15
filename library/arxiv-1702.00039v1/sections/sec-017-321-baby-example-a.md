---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-017-321-baby-example-a
section_title: "Baby example A"
section_number: 3.2.1
pages: 14-14
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.814
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
It is clear that $b_{\mathrm{id}}=1$. We have seen that $h_s+v$ is self-dual and it is of the form ([\[KL\]](#KL){reference-type="ref" reference="KL"}), so $b_s=(h_s+v).$ By symmetry between $s$ and $r$ we have that $b_r=(h_r+v).$

It is easy to see that $b_{sr}=b_{s}b_{r}$. It is self-dual because $d$ is a ring morphism and $b_{s}$ and $b_{r}$ both are. On the other hand it is of the form ([\[KL\]](#KL){reference-type="ref" reference="KL"}) $$b_{s}b_{r}=h_{sr}+vh_s+vh_r+v^2,$$ and again we obtain $b_{rs}$ by symmetry.

If we were very optimistic we would believe that $b_{srs}=b_{s}b_{r}b_{s}$, which is self-dual. Let us calculate $$\begin{aligned}
b_{s}b_{r}b_{s}&=&(h_{sr}+vh_s+vh_r+v^2)(h_s+v)\nonumber\\
&=&(h_{srs}+\underbrace{vh_s^2}+vh_{rs}+v^2h_s)+(vh_{sr}+v^2h_s+v^2h_r+v^3)
\end{aligned}$$ But $vh_s^2=(1-v^2)h_s +v,$ so $b_{s}b_{r}b_{s}$ is not of the form ([\[KL\]](#KL){reference-type="ref" reference="KL"}), we have a term that is $h_s$. To solve this issue we substract $b_{s}.$ We still have a self-dual element and we eliminate the $h_s$ from the sum, so finally we obtain $$\begin{aligned}
b_{srs}&=&b_{s}b_{r}b_{s}-b_{s}\nonumber\\
&=&h_{srs}+vh_{rs}+vh_{sr}+v^2h_s+v^2h_r+v^3
\end{aligned}$$
