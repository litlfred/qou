---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-005-24-saddle-point-method
section_title: "Saddle point method"
section_number: 2.4
pages: 7-8
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.906
---
We need to use the following version of saddle point method as illustrated in [@Oht18].

::: proposition
[]{#proposition-saddlemethod label="proposition-saddlemethod"} Let $A$ be a non-singular symmetric complex $3\times 3$ matrix, and let $\Psi(z_1,z_2,z_3)$ and $r(z_1,z_2,z_3)$ be holomorphic functions of the forms, $$\begin{aligned}
    \Psi(z_1,z_2,z_3)&=\mathbf{z}^{T}A\mathbf{z}+r(z_1,z_2,z_3), \\\nonumber
    r(z_1,z_2,z_3)&=\sum_{i,j,k}b_{ijk}z_iz_jz_k+\sum_{i,j,k,l}c_{ijkl}z_iz_jz_kz_l+\cdots
   
\end{aligned}$$ defined in a neighborhood of $\mathbf{0}\in \mathbb{C}^3$. The restriction of the domain $$\begin{aligned}
 \label{formula-domain0}
       \{(z_1,z_2,z_3)\in \mathbb{C}^3| \text{Re}\Psi(z_1,z_2,z_3)<0\}  
   
\end{aligned}$$ to a neighborhood of $\mathbf{0}\in \mathbb{C}^3$ is homotopy equivalent to $S^2$. Let $D$ be an oriented disk embeded in $\mathbb{C}^3$ such that $\partial D$ is included in the domain ([\[formula-domain0\]](#formula-domain0){reference-type="ref" reference="formula-domain0"}) whose inclusion is homotopic to a homotopy equivalence to the above $S^2$ in the domain ([\[formula-domain0\]](#formula-domain0){reference-type="ref" reference="formula-domain0"}). Then we have the following asymptotic expansion $$\begin{aligned}
    \int_{D}e^{N\psi(z_1,z_2,z_3)}dz_1dz_2dz_3=\frac{\pi^{\frac{3}{2}}}{N^{\frac{3}{2}}\sqrt{\det(-A)}}\left(1+\sum_{i=1}^d\frac{\lambda_i}{N^i}+O(\frac{1}{N^{d+1}})\right),
\end{aligned}$$ for any $d$, where we choose the sign of $\sqrt{\det{(-A)}}$ as explained in Proposition [@Oht16], and $\lambda_i$'s are constants presented by using coefficients of the expansion $\Psi(z_1,z_2,z_3)$, such presentations are obtained by formally expanding the following formula, $$\begin{aligned}
    &1+\sum_{i=1}^{\infty}\frac{\lambda_i}{N^i}\\\nonumber
    &=\exp\left(Nr\left(\frac{\partial }{\partial w_1},\frac{\partial }{\partial w_2},\frac{\partial }{\partial w_3}\right)\right)\exp\left(-\frac{1}{4N}(w_1,w_2,w_3)A^{-1}\begin{pmatrix}
      w_1 \\ w_2 \\ w_3  
    \end{pmatrix}\right)|_{w_1=w_2=w_3=0}.
\end{aligned}$$
:::

For a proof of the Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"}, see [@Oht16].

::: remark
[]{#remark-saddle label="remark-saddle"} As mentioned in Remark 3.6 of [@Oht16], we can extend Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} to the case where $\Psi(z_1,z_2,z_3)$ depends on $N$ in such a way that $\Psi(z_1,z_2,z_3)$ is of the form $$\begin{aligned}
        \Psi(z_1,z_2,z_3)=\Psi_0(z_1,z_2,z_3)+\Psi_1(z_1,z_2,z_3)\frac{1}{N}+R(z_1,z_2,z_3)\frac{1}{N^2}. 
    
\end{aligned}$$ where $\Psi_i(z_1,z_2,z_3)$'s are holomorphic functions independent of $N$, and we assume that $\Psi_0(z_1,z_2,z_3)$ satisfies the assumption of the Proposition and $|R(z_1,z_2,z_3)|$ is bounded by a constant which is independent of $N$.
:::
