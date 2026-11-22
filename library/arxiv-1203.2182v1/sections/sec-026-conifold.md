---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-026-conifold
section_title: "Conifold"
section_number: null
pages: 59-60
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.962
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
We now repeat the above calculation for the conifold, whose ordinary mirror curve in general framing takes the form [@abmodel]: $$A^{\text{ref}} (x,y;q_1=1) = 1 - y + x(-y)^f + Q x (-y)^{f+1} \; = \; 0 \,.    \label{mirrorConif}$$ To find the refined and quantum version of this curve, we again consider the brane located along the preferred direction of the conifold. More precisely, we wish to consider the brane amplitude normalized by the closed string partition function. Such an amplitude can be written as $$Z_{\text{BPS}}^{\text{open}} \; = \; \sum_{k=0}^{\infty} a_k = \sum_{R=(k)}  s_R(x) f_R(q_1,q_2)^{-f} \frac{b_R}{b_{\bullet}},   \label{Zopen-coni}$$ where $$\begin{aligned}
b_R & = & \sum_{P} (-Q)^{|P|} C_{P\bullet R}(q_1^{-1},q_2^{-1})  C_{P^t \bullet \bullet}(q_2^{-1},q_1^{-1})  \nonumber\\
& = & \Big( \frac{q_1}{q_2} \Big)^{||R||^2/2}  P_{R^t}(q_1^{\rho};q_2^{-1},q_1^{-1})
\prod_{i,j=1}^{\infty} (1 - Q q_1^{-i+1/2} q_2^{-j+1/2+R_i})
\end{aligned}$$ and $Q$ denotes the Kähler parameter of the conifold. The normalization factor in this case is nothing but $$\begin{aligned}
Z_{\text{BPS}}^{\text{closed}} = b_{\bullet} & = & \sum_{P} (-Q)^{|P|} C_{P\bullet \bullet}(q_1^{-1},q_2^{-1})  C_{P^t \bullet \bullet}(q_2^{-1},q_1^{-1})  \nonumber  \\
& = & \prod_{i,j=1}^{\infty} (1 - Q q_1^{-i+1/2} q_2^{-j+1/2}),
\end{aligned}$$ and it follows that for representation $R=(k)$, *cf.* ([\[C00R\]](#C00R){reference-type="ref" reference="C00R"}): $$\frac{b_{(k)}}{b_{\bullet}} = C_{\bullet \bullet (k)}(q_1^{-1},q_2^{-1}) \prod_{j=1}^k \big(1 - Q q_1^{-1/2} q_2^{-j+k+1/2} \big)
= \Big(- \frac{q_1}{\sqrt{q_2}} \Big)^k \prod_{i=1}^k \frac{1 - Q q_1^{-1/2} q_2^{i-1/2}}{1 - q_1 q_2^{i-1}}.$$ Collecting the above ingredients, we find the following structure of the open BPS state partition function $$Z_{\text{BPS}}^{\text{open}} \; = \; \sum_{k=0}^{\infty} a_k
= \sum_{k=0}^{\infty} (-1)^{(f+1)k} q_2^{\frac{f}{2}k(k-1)} \Big(x \frac{q_1}{\sqrt{q_2}}\Big)^k \prod_{i=1}^k \frac{1 - Q q_1^{-1/2} q_2^{i-1/2}}{1 - q_1 q_2^{i-1}} \,.   \label{Zopen-BPS-coni}$$ We also find that the consecutive terms $a_k$ are related as $$(1 - q_1 q_2^k) a_{k+1} \; = \; (-1)^{f+1} q^{f k} \frac{q_1}{\sqrt{q_2}} x (1 - Q q_1^{-1/2} q_2^{k+1/2} ) a_k \,.$$ Summing both sides over $k$ gives rise to the inhomogeneous equation $$\Big(1 - \frac{q_1}{q_2} \widehat{y} + \frac{q_1}{\sqrt{q_2}} \widehat{x}(-\widehat{y})^f  + Q q_1^{1/2} \widehat{x}(-\widehat{y})^{f+1} \Big) Z_{\text{BPS}}^{\text{open}} \; = \; 1 - \frac{q_1}{q_2} \,.   \label{AquantumConiinhom}$$ This is the refined and quantum version of the conifold mirror curve ([\[mirrorConif\]](#mirrorConif){reference-type="ref" reference="mirrorConif"}). We can also bring this equation to the homogeneous form at the expense of increasing its degree in $\widehat{y}$, by multiplying both sides with $(1-\widehat{y})$. Commuting all $\widehat{y}$ operators to the right gives $$\Big(1 - \Big(1 + \frac{q_1}{q_2}\Big) \widehat{y} + \frac{q_1}{q_2}\widehat{y}^2 +
\frac{q_1}{\sqrt{q_2}} \widehat{x}(-\widehat{y})^f + \Big(Q\sqrt{q_1} +  q_1\sqrt{q_2} \Big) \widehat{x} (-\widehat{y})^{f+1}
+ Q\sqrt{q_1} q_2 \widehat{x} (-\widehat{y})^{f+2}
  \Big) Z_{\text{BPS}}^{\text{open}} = 0.$$
