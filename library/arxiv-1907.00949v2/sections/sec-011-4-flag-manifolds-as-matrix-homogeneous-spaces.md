---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-011-4-flag-manifolds-as-matrix-homogeneous-spaces
section_title: "Flag manifolds as matrix homogeneous spaces"
section_number: 4
pages: 9-10
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.987
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:homo label="sec:homo"}

We will discuss three representations of the flag manifold as *matrix homogeneous spaces*, i.e., where a flag is represented as an equivalence class of matrices: $$\begin{aligned}
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong \mathop{\mathrm{O}}(n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr), \label{eq:homo1}\\
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong \mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr),\label{eq:homo2}\\
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\cong  \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr).\label{eq:homo3}
\end{aligned}$$ The characterization [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} is standard [@Monk1959; @Borel1991] and generalizes the well-known characterization of the Grassmannian as $\mathop{\mathrm{Gr}}(k,n) \cong \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(k) \times \mathop{\mathrm{O}}(n-k)\bigr)$ whereas the characterization [\[eq:homo3\]](#eq:homo3){reference-type="eqref" reference="eq:homo3"} generalizes another well-known characterization of the Grassmannian as $\mathop{\mathrm{Gr}}(k,n) \cong \mathop{\mathrm{V}}(k,n)/\mathop{\mathrm{O}}(k)$.

Nevertheless, we will soon see that it is desirable to describe $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ as a homogeneous space $G/H$ where $G$ is a connected Lie group --- note that $\mathop{\mathrm{O}}(n)$ is not connected whereas $\mathop{\mathrm{V}}(n_d,n)$ is not a group, so [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"} and [\[eq:homo3\]](#eq:homo3){reference-type="eqref" reference="eq:homo3"} do not meet this criterion. With this in mind, we state and prove [\[eq:homo2\]](#eq:homo2){reference-type="eqref" reference="eq:homo2"} formally.

::: proposition
[]{#prop:equivalent definition of flag manifold label="prop:equivalent definition of flag manifold"} Let $0 < n_1< \dots < n_d < n$ be $d$ positive integers. The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ is diffeomorphic to the homogeneous space $$\mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr)$$ where $\mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n_d - n_{d-1}) \times \mathop{\mathrm{O}}(n-n_d) \bigr)$ is the subgroup of unit-determinant block diagonal matrices with orthogonal blocks, i.e., $$\begin{bsmallmatrix}
Q_1 & 0 & \dots & 0 \\
0 & Q_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & Q_{d+1}
\end{bsmallmatrix} \in \mathop{\mathrm{O}}(n), \quad Q_i\in \mathop{\mathrm{O}}(n_i-n_{i-1}), \quad i=1,\dots, d+1, \quad \prod_{i=1}^{d+1} \det (Q_i) = 1.$$
:::

::: proof
*Proof.* We start with the characterization [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"}, i.e., in this proof we assume '$=$' in place of '$\cong$' in [\[eq:homo1\]](#eq:homo1){reference-type="eqref" reference="eq:homo1"}. We claim that the required diffeomorphism $\tau$ is given as in the commutative diagram below: $$\begin{tikzcd}
\mathop{\mathrm{SO}}(n) \arrow{r}{j} \arrow[swap]{d}{\pi'} & \mathop{\mathrm{O}}(n) \arrow{d}{\pi} \\
\mathop{\mathrm{SO}}(n) / \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n-n_d) \bigr) \arrow{r}{\tau} & \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) 
\end{tikzcd}$$ Here $j$ is the inclusion of $\mathop{\mathrm{SO}}(n)$ in $\mathop{\mathrm{O}}(n)$, $\pi$ and $\pi'$ the respective quotient maps, and $\tau$ the induced map. Since $$\mathop{\mathrm{SO}}(n)  \cap  \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots  \times \mathop{\mathrm{O}}(n-n_d) \bigr)=  \mathop{\mathrm{S}}\bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2 - n_1) \times \dots \times \mathop{\mathrm{O}}(n - n_{d}) \bigr),$$ $\tau$ is injective. To show that it is surjective, let $\{\mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be a flag represented by some $A\in \mathop{\mathrm{O}}(n)$, i.e., $\pi(A) = \{\mathbb{V}_i\}_{i=1}^d$. If $\det(A) = 1$, then we already have $\tau (\pi_1(A)) = \{\mathbb{V}_i\}_{i=1}^d$ by commutativity of the diagram. If $\det(A) = -1$, take any $A_1\in \mathop{\mathrm{O}}(n_1)$ with $\det(A_1)=-1$, set $$B = A \begin{bsmallmatrix}
A_1 & 0 &\cdots & 0 \\
0 & I_{n_2 - n_1} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & I_{n - n_d}
\end{bsmallmatrix} \in \mathop{\mathrm{SO}}(n),$$ and observe that $\tau (\pi_1(B)) = \pi (B) = \pi (A)$. ◻
:::
