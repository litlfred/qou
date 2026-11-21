---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-015-52-symmetries-and-the-vector-of-riemann-constant
section_title: "Symmetries and the vector of Riemann constants"
section_number: 5.2
pages: 16-17
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.969
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section5.2 label="section5.2"}

We now describe how symmetries may be used to restrict the vector of Riemann constants by recalling some results we have established elsewhere.

Suppose that a curve has a nontrivial group of symmetries $\mathop{\rm Aut}\nolimits(\mathcal{C})$. Then the holomorphic differentials of the curve, $H\sp{1,0}(\mathcal{C},\mathbb{C})$, and the homology group $H_1(\mathcal{C},\mathbb{Z})$ are both $\mathop{\rm Aut}\nolimits(\mathcal{C})$-modules. Let $\sigma\in\mathop{\rm Aut}\nolimits(\mathcal{C})$ and denote the actions on these spaces by $$\sigma\sp\ast v_j= \sum_k v_k {L}\sp{k}_j,\qquad
\sigma_\ast\begin{pmatrix}\mathfrak{a}_i\\
  \mathfrak{b}_i\end{pmatrix}=M\begin{pmatrix}\mathfrak{a}_i\\
  \mathfrak{b}_i\end{pmatrix}:=
  \begin{pmatrix}{A}&B\\
    C&D\end{pmatrix}\begin{pmatrix}\mathfrak{a}_i\\
    \mathfrak{b}_i
  \end{pmatrix},$$ where ${L}\in GL(g,\mathbb{C})$, $M\in Sp(2g,\mathbb{Z})$ and $\{v_i\}$ is a (not necessarily normalized) basis of $H\sp{1,0}(\mathcal{C},\mathbb{C})$. Denote by $\Pi=\begin{pmatrix}\mathcal{A}\\
\mathcal{B}\end{pmatrix}$ the matrix of periods, where $\mathcal{A}_{ij}=\int_{\mathfrak{a}_i}v_j$ and $\mathcal{B}_{ij}=\int_{\mathfrak{b}_i}v_j$. Then $\tau=\mathcal{B}\mathcal{A}\sp{-1}$ and $\boldsymbol{\omega}=
\boldsymbol{v}\mathcal{A}\sp{-1}$. The identity $\oint_{\sigma_\ast\gamma}v=\oint_\gamma\sigma\sp\ast v$ (for any $\gamma\in H_1(\mathcal{C},\mathbb{Z})$) yields the relation $$\label{gensym}
M\Pi=\Pi {L}$$ which restricts the period matrix $\tau$. Now using ([\[vrcdelta\]](#vrcdelta){reference-type="ref" reference="vrcdelta"}) and ([\[Kcanonical\]](#Kcanonical){reference-type="ref" reference="Kcanonical"}) we have that (with $\hat{L}=\mathcal{A} {L}\mathcal{A}\sp{-1}$, so as to be working with normalized differentials)) $$2K_Q \hat{L}\equiv\int_\ast\sp{2\Delta}\sigma\sp\ast{\boldsymbol{\omega}}
-2(g-1)\int_\ast\sp{Q}\sigma\sp\ast{\boldsymbol{\omega}}$$ which yields $$2K_Q\big[\hat{L}-\mathop{\rm Id}\nolimits\big]\equiv\int_{2\Delta}\sp{\sigma(2\Delta)}{\boldsymbol{\omega}}-
2(g-1)\int_Q\sp{\sigma(Q)}{\boldsymbol{\omega}} .$$ If $\mathcal{K}_\mathcal{C}$ is the divisor of a differential $v$ then $\sigma\sp{-1}(\mathcal{K}_\mathcal{C})$ is the divisor of $\sigma\sp\ast(v)$, whence the uniqueness of the canonical class means that $\sigma(\mathcal{K}_\mathcal{C})\sim\mathcal{K}_\mathcal{C}$ and consequently $\sigma(2\Delta)\sim2\Delta$. This shows that we have an action of $\mathop{\rm Aut}\nolimits(\mathcal{C})$ on the theta characteristics and $$K_Q \hat{L}\equiv K_{\sigma(Q)}+\int_\Delta\sp{\sigma(\Delta)}{\boldsymbol{\omega}} ,$$ the last integral also being a theta characteristic. We have then the identity on the Jacobian $$2K_Q\left[\hat{L}-\mathop{\rm Id}\nolimits\right]\equiv-
2(g-1)\int_Q\sp{\sigma(Q)}{\boldsymbol{\omega}}.$$ This then establishes

::: lemma
[]{#lemtp label="lemtp"} Suppose the automorphism $\sigma$ has order $N>1$. If $L-\mathop{\rm Id}\nolimits$ is invertible and $Q$ is a fixed point of $\sigma$ then $K_Q$ is a $2N$-torsion point.
:::

::: remark
We have the map $\pi:\mathcal{C}\rightarrow\mathcal{C}/\langle \sigma\rangle$. Any holomorphic differential on $\mathcal{C}/\langle\sigma\rangle$ pulls back to an invariant differential on $\mathcal{C}$, and so the assumption that $L-\mathop{\rm Id}\nolimits$ is invertible is equivalent to $\mathcal{C}/\langle \sigma\rangle \cong\mathbb{P}\sp1$.
:::

::: corollary
[]{#cortp label="cortp"} Assuming the conditions of Lemma [\[lemtp\]](#lemtp){reference-type="ref" reference="lemtp"} and that $\psi\in\mathop{\rm Aut}\nolimits(\mathcal{C})$, then $\int_Q\sp{\psi(Q)}{\boldsymbol{\omega}}$ is a $2N(g-1)$-torsion point.
:::

Although these simple results do not necessarily give the best bound on the order of the torsion point for the vectors involved, we see that, given a suitable symmetry and fixed point, we have that $K_Q$ is a torsion point: $$2K_Q\mathcal{A}=\mathbf{n}\Pi\left[L-\mathop{\rm Id}\nolimits\right]\sp{-1}
=\mathbf{n}(M-\mathop{\rm Id}\nolimits)\sp{-1}\Pi=\mathbf{n}\left(\frac{1}{N}\sum_{k=1}\sp{N-1}
kM\sp{k}\right)\Pi.$$ The additional (we think) new idea we brought to this was to use some number theory associated with $M$ to restrict the form of $K_Q$. Suppose there exist $\mathbf{l}$, $\mathbf{m}\in\mathbb{Z}\sp{2g}$ such that $$\label{sfdef}
\mathbf{m}=\mathbf{l}(M-\mathop{\rm Id}\nolimits),$$ then $$\mathbf{m}\Pi=\mathbf{l}(M-\mathop{\rm Id}\nolimits)\Pi=
 \mathbf{l}\Pi\left[L-\mathop{\rm Id}\nolimits\right]$$ and $$\left(2K_Q\mathcal{A}+\mathbf{l}\Pi\right)\left[{L}-\mathop{\rm Id}\nolimits\right]=(\mathbf{n}+\mathbf{m})\Pi  \in
\mathbb{C}\sp{g}.$$ The idea is to use the freedom in choosing $\mathbf{l}$ here in ([\[sfdef\]](#sfdef){reference-type="ref" reference="sfdef"}) to make $\mathbf{n}+\mathbf{m}$ as simple as possible; as we are only interested in $2K_Q$ modulo the lattice we will have further restricted the choice of the vector of Riemann constants. For example, if $\mathbf{m}$ could be chosen arbitrarily then we could make $\mathbf{n}+\mathbf{m}=\mathbf{0}$ and so $2K_Q$ would be a lattice point. We implement the idea using the Smith normal form of $M-\mathop{\rm Id}\nolimits$. Recall this means in the present context that we may write $$M-\mathop{\rm Id}\nolimits=USV, \qquad S=\mathop{\rm Diag}\nolimits(d_1,\ldots,d_{2g}),\qquad d_i|d_{i+1},
\qquad U,V\in GL(2g,\mathbb{Z}).$$ The invertibility of $L-\mathop{\rm Id}\nolimits$ means that $d_i\ge1$ and that ([\[sfdef\]](#sfdef){reference-type="ref" reference="sfdef"}) becomes $$\mathbf{m}V\sp{-1}=(\mathbf{l}U)S.$$ Here we view $\mathbf{l}'=\mathbf{l}U$ as arbitrary and we are interested in the constraints this places on $\mathbf{m}$. We have $(\mathbf{m}V\sp{-1})_i=l_i'd_i$ and clearly the only constraints arise for $d_i\ne1$. Given our earlier observation that here $d_i\ge1$, we find that $\mathbf{m}$ is constrained only by $$\big(\mathbf{m}V\sp{-1}\big)_i\equiv0 \mod d_i,\qquad d_i>1.$$ Thus, given a suitable symmetry and fixed point $Q$, the Smith normal form of $M-\mathop{\rm Id}\nolimits$ enables us to restrict the possible torsion points for $2K_Q$. Considering further automorphisms and making use of Corollary [\[cortp\]](#cortp){reference-type="ref" reference="cortp"} may yield further restrictions. The final step in evaluating $K_Q$ is the choice of the appropriate half-period when taking the square root. This again may be restricted by the symmetry but may also be decided numerically from the $2^{2g}$ half-periods.
