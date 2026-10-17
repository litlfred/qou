---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-007-4-example
section_title: "Example"
section_number: 4
pages: 7-7
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.818
latex_coverage_ratio: 1.0
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
[]{#sec ex label="sec ex"}

Let's use the braid presentation $w = \sigma_2^{-1} \sigma_1 \sigma_2^{-1} \sigma_1$ for the figure-eight knot, pictured below with its six possible states. $$\vcenter{\xy 0;/r.15pc/:
(0,0);(14,14)**@{-},
(16,16);(20,20)**@{-},
(20,20);(20,30)**@{-},
(20,30);(10,40)**@{-},
(10,0);(6,4)**@{-},
(4,6);(0,10)**@{-},
(0,10);(0,20)**@{-},
(0,20);(14,34)**@{-},
(16,36);(20,40)**@{-},
(20,0);(20,10)**@{-},
(20,10);(6,24)**@{-},
(4,26);(0,30)**@{-},
(0,30);(0,40)**@{-}
\endxy} \qquad
\begin {array} {c | c | c c c}
\mathbf{x} & \varepsilon& M(w, \mathbf{x}, \varepsilon) & & \\
\hline
& & & & \\
\multirow {7} {*}
{\quad $\vcenter{\xy 0;/r.10pc/:
(0,0);(0,40)**@{-},
(10,0);(10,40)**@{-},
(20,0);(20,40)**@{-}
\endxy}$} \quad
& + \, + \, + & v^{-1} \cdot v \cdot v^{-1} \cdot v &=& 1 \\
&&&& \\
&+ \, + \, - & \frac {-v^2} {[2]} \cdot v \cdot \frac {-v^2} {[2]} \cdot v &=& \frac {v^6} {[2]^2} \\
&&&& \\
&+ \, - \, + & \frac {v^{-2}} {[2]} \cdot (-v^{-1}) \cdot \frac {v^{-2}} {[2]} \cdot (-v^{-1}) &=& \frac {v^{-6}} {[2]^2} \\
&&&& \\
&+ \, - \, - & (-v) \cdot (-v^{-1}) \cdot (-v) \cdot (-v^{-1}) &=& 1 \\
&&&& \\
\hline
& & & & \\
\multirow {3} {*}
{\quad $\vcenter{\xy 0;/r.10pc/:
(0,0);(0,40)**@{-},
(10,0);(10,10)**@{-},
(10,10);(20,20)**@{-},
(20,20);(20,30)**@{-},
(20,30);(10,40)**@{-},
(20,0);(20,10)**@{-},
(20,10);(10,20)**@{-},
(10,20);(10,30)**@{-},
(10,30);(20,40)**@{-}
\endxy}$} \quad
&+ \, + \, - & \frac {[3]} {[2]} \cdot (-v^{-1}) \cdot \frac {[1]} {[2]} \cdot v &=& \frac {-[3]} {[2]^2} \\
&&&& \\
&+ \, - \, + & \frac {[1]} {[2]} \cdot v \cdot \frac {[3]} {[2]} \cdot (-v^{-1}) &=& \frac {-[3]} {[2]^2}
\end {array}$$\
Now, we calculate the sum, minding the signs associated to each state and the global rescaling. $$A(w) = \dfrac {1} {[3]} \left( 2 - \dfrac {v^6 + v^{-6}} {[2]^2} + \dfrac {2 [3]} {[2]^2} \right) = -v^2+3-v^{-2} = 1 - (v-v^{-1})^2$$
