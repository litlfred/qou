---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-018-322-baby-example-b
section_title: "Baby example B"
section_number: 3.2.2
pages: 14-15
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.767
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
In Example A we never used that $m_{sr}=3$ in our calculations. The point is that if $m_{sr}\neq 3$ then $b_{s}b_{r}b_{s}-b_{s}\neq b_{r}b_{s}b_{r}-b_{r}$. In our baby example **(B)** we have $m_{sr}=4.$ For the same reasons as before we have

-   $b_{sr}=b_{s}b_{r}$

-   $b_{srs}=b_{s}b_{r}b_{s}-b_{s}$

-   $b_{rsr}=b_{r}b_{s}b_{r}-b_{r}.$

So we just need to calculate $b_{srsr}.$ We start again with $$b_{s}b_{r}b_{s}b_{r}=(h_{sr}+vh_s+vh_r+v^2)(h_{sr}+vh_s+vh_r+v^2).$$ When we expand the right hand side, the only terms in the sum that do not give elements of the form ([\[KL\]](#KL){reference-type="ref" reference="KL"}) are $(vh_s)(h_{sr})=(1-v^2)h_{sr}+vh_r$ and $(h_{sr})(vh_r)=(1-v^2)h_{sr}+vh_s,$ so if we substract $2b_{sr},$ we eliminate the two "problematic\" terms and we obtain

$$\begin{aligned}
b_{srsr}&=&b_{s}b_{r}b_{s}b_{r}-2b_{s}b_{r}\nonumber\\
&=&h_{srsr}+vh_{srs}+vh_{rsr}+v^2h_{sr}+v^2h_{rs} +v^3h_s+v^3h_r+v^4\nonumber\\
&=& \sum_{y\leq srsr}v^{4-l(y)}h_y
\end{aligned}$$
