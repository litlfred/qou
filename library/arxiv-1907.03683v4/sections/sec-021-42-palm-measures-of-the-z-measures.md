---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-021-42-palm-measures-of-the-z-measures
section_title: "Palm measures of the z-measures"
section_number: 4.2
pages: 25-26
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 1.0
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
We now state in Theorem [\[thmpalmzmeas\]](#thmpalmzmeas){reference-type="ref" reference="thmpalmzmeas"} below the interpretation of Theorem [\[thmzmeas\]](#thmzmeas){reference-type="ref" reference="thmzmeas"} in terms of Palm measures of the $z$-measures.

::: thm
[]{#thmpalmzmeas label="thmpalmzmeas"} Let $\xi \in (0,1)$ and let $z, z'$ be admissible parameters. Let $u_1, \dots , u_k \in \mathbb{Z}'$ be pairwise distinct and denote by $\mathbb{P}^k_{z,z',\xi}$ the reduced Palm measure of the point process $\mathfrak{S}_*(M_{z,z',\xi})$ at points $u_1,\dots, u_k$. Then, the kernel $K_{z-k,z',\xi}^k$ defined by ([\[kernelmodifiedzmeas\]](#kernelmodifiedzmeas){reference-type="ref" reference="kernelmodifiedzmeas"}) is a correlation kernel for $\mathbb{P}^k_{z,z',\xi}$.
:::

::: proof
*Proof.* We start by proving that, up to multiplication by a factor, the correlation functions of the point process $\mathbb{P}^k_{z,z',\xi}$ are analytic in $\sqrt{\xi}$ with coefficients that are polynomials in $(z,z')$. From Proposition [\[propcvpalm\]](#propcvpalm){reference-type="ref" reference="propcvpalm"}, the point process $\mathbb{P}^k_{z,z',\xi}$ is a determinantal point process with kernel $$\begin{aligned}
K^{u_1, \dots , u_k}_{z,z',\xi}(x,y) &= \det \left( K_{z,z',\xi}^0(u_i,u_j) \right)_{1 \leq i,j \leq k }^{-1} \\
&\times \det \begin{pmatrix}
K_{z,z',\xi}^0(x,y) & K_{z,z',\xi}^0(x,u_1) & \dots & K_{z,z',\xi}^0(x,u_k) \\
K_{z,z',\xi}^0(u_1,y) & K_{z,z',\xi}^0(u_1,u_1) & \dots & K_{z,z',\xi}^0(u_1, u_k) \\
\dots & \dots & \dots & \dots \\
K_{z,z',\xi}^0(u_k,y) & \dots & \dots & K_{z,z',\xi}^0(u_k,u_k)     
\end{pmatrix}, 
\end{aligned}$$ where the kernel $K_{z,z',\xi}^0$ is defined by ([\[kernelmodifiedzmeas\]](#kernelmodifiedzmeas){reference-type="ref" reference="kernelmodifiedzmeas"}) with $k=0$. By similar arguments as in step 3 in the proof of Theorem [\[thmzmeas\]](#thmzmeas){reference-type="ref" reference="thmzmeas"}, the quantity $$\begin{aligned}
\det \left( K_{z,z',\xi}^0(u_i,u_j) \right)_{1 \leq i,j \leq k }  \cdot K^{u_1, \dots , u_k}_{z,z',\xi}(x,y) 
\end{aligned}$$ is analytic in $\sqrt{\xi}$ with coefficients that are polynomials in $(z,z')$. As an immediate consequence, for any $\{x_1, \dots, x_n \} \subset \mathbb{Z}'$, the quantity $$\begin{aligned}
\left\{ \det \left( K_{z,z',\xi}^0(u_i,u_j) \right)_{1 \leq i,j \leq k } \right\}^n & \cdot \det \left( K^{u_1, \dots , u_k}_{z,z',\xi}(x_i,x_j) \right)_{i,j= 1}^n \\
&= \left\{ \det \left( K_{z,z',\xi}^0(u_i,u_j) \right)_{1 \leq i,j \leq k } \right\}^n \cdot \mathbb{P}^k_{z,z',\xi} ( \{x_1, \dots, x_n\} \subset X)
\end{aligned}$$ is analytic in $\sqrt{\xi}$ with coefficients that are polynomials in $(z,z')$.

If now $z=N+k$ and $z' \in \mathbb{R}$ with $z' > z-1$, then $\mathbb{P}^k_{z,z',\xi}$ is the Christoffel deformation of the $N$-th Meixner ensemble shifted by $-N +1/2$, i.e. $$\begin{aligned}
\mathbb{P}^k_{z,z',\xi}( \{x_1,\dots, x_n \} \subset X)= M_{z-k,z',\xi}^k ( \{ x_1,\dots, x_n \} \subset \mathfrak{S}(\lambda)),
\end{aligned}$$ for any $\{x_1,\dots, x_n \} \subset \mathbb{Z}'$. By Lemma [\[lemmestep1\]](#lemmestep1){reference-type="ref" reference="lemmestep1"}, we thus have $$\begin{aligned}
 \label{eq:proofpalmzmeas}
\mathbb{P}^k_{z,z',\xi}( \{x_1,\dots, x_n \} \subset X) = \det \left( K_{z-k,z',\xi}^k(x_i,x_j) \right)_{i,j=1}^n.
\end{aligned}$$ Observe now that, up to the multiplication by $$\begin{aligned}
\left\{\det \left( K_{z,z',\xi}^0(u_i,u_j) \right)_{1 \leq i,j \leq k }\right\}^n,
\end{aligned}$$ both sides of equality ([\[eq:proofpalmzmeas\]](#eq:proofpalmzmeas){reference-type="ref" reference="eq:proofpalmzmeas"}) are analytic in $\sqrt{\xi}$ with coefficients that are polynomials in $z,z'$. We deduce that equality ([\[eq:proofpalmzmeas\]](#eq:proofpalmzmeas){reference-type="ref" reference="eq:proofpalmzmeas"}) holds for any choice of the parameters $z,z'$, and Theorem [\[thmpalmzmeas\]](#thmpalmzmeas){reference-type="ref" reference="thmpalmzmeas"} is proved. ◻
:::
