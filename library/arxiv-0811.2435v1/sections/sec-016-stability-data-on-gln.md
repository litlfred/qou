---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-016-stability-data-on-gln
section_title: "Stability data on gl(n)"
section_number: null
pages: 43-45
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.973
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\g={\mathfrak{gl}}(n,\Q)$ be the Lie algebra of the general linear group. We consider it as a $\Gamma$-graded Lie algebra $\g=\oplus_{\gamma \in \Gamma}\g_{\gamma}$, where $$\Gamma=\{(k_1,\dots,k_n)|\,\,k_i\in \Z, \sum_{1\le i\le n}k_i=0\}$$ is the root lattice. We endow $\g$ with the Cartan involution $\eta$. Algebra $\g$ has the standard basis $E_{ij}\in \g_{\gamma_{ij}}$ consisting of matrices with the single non-zero entry at the place $(i,j)$ equal to $1$. Then $\eta(E_{ij})=-E_{ji}$. In what follows we are going to consider symmetric (with respect to $\eta$) stability data on $\g$.

We notice that $$\op{Hom}(\Gamma,\C)\simeq \C^n/\C\cdot(1,\dots,1)\,\,.$$ We define a subspace $\op{Hom}^\circ(\Gamma,\C)\subset \op{Hom}(\Gamma,\C)$ consisting (up to a shift by the multiples of the vector $(1,\dots,1)$) of vectors $(z_1,\dots,z_n)$ such that $z_i\ne z_j$ if $i\ne j$. Similarly we define a subspace $\op{Hom}^{\circ\circ}(\Gamma,\C)\subset \op{Hom}(\Gamma,\C)$ consisting (up to the same shift) of such $(z_1,\dots,z_n)$ that there is no $z_i,z_j,z_k$ belonging to the same real line as long as $i\ne j\ne k$. Obviously there is an inclusion $\op{Hom}^{\circ\circ}(\Gamma,\C)\subset \op{Hom}^\circ(\Gamma,\C)$.

For $Z\in \op{Hom}(\Gamma,\C)$ we have $Z(\gamma_{ij})=z_i-z_j$. If $Z\in \op{Hom}^{\circ\circ}(\Gamma,\C)$ then symmetric stability data with such $Z$ is the same as a skew-symmetric matrix $(a_{ij})$ with rational entries determined from the equality $a(\gamma_{ij})=a_{ij}E_{ij}$. Every continuous path in $\op{Hom}^\circ(\Gamma,\C)$ admits a unique lifting to $Stab(\g)$ as long as we fix the lifting of the initial point. The matrix $(a_{ij})$ changes when we cross walls in $\op{Hom}^\circ(\Gamma,\C)\setminus \op{Hom}^{\circ\circ}(\Gamma,\C)$. A typical wall-crossing corresponds to the case when in the above notation the point $z_j$ crosses a straight segment joining $z_i$ and $z_k, i\ne j\ne k$. In this case the only change in the matrix $(a_{ij})$ is of the form: $$a_{ik}\mapsto a_{ik}+a_{ij}a_{jk}\,\,.$$ This follows from the multiplicative wall-crossing formula which is of the form: $$\begin{array}{l}\exp(a_{ij}E_{ij})\exp(a_{ik}E_{ik})\exp(a_{jk}E_{jk})=\\
\qquad{}=\exp(a_{jk}E_{jk})\exp((a_{ik}+a_{ij}a_{jk})E_{ik})\exp(a_{ij}E_{ij})\,\,.
\end{array}$$ Same wall-crossing formulas appeared in [@CeVa] in the study of the change of the number of solitons in $N=2$ two-dimensional supersymmetric QFT. In [@CeVa] the numbers $a_{ij}$ were integers, and the wall-crossing preserved integrality. In our considerations, for any $Z\in \op{Hom}^{\circ\circ}(\Gamma,\C)$ the fundamental group $\pi_1(\op{Hom}^\circ(\Gamma,\C),Z)$ acts on the space of skew-symmetric matrices by polynomial transformations with integer coefficients. It can be identified with the well-known actions of the pure braid group on the space of upper-triangular matrices in the theory of Gabrielov bases of isolated singularities and in the theory of triangulated categories endowed with exceptional collections. Furthermore, the matrices $\exp(a_{ij}E_{ij})=1+a_{ij}E_{ij}$ can be interpreted as Stokes matrices of a certain connection in a neighborhood of $0\in \C$, which has irregular singularities ($tt^{\ast}$-connection from [@CeVa], see also [@GaMNeit]). This observation should be compared with the results about the irregular connection from the previous section.
