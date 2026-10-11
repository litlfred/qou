---
doc_id: arxiv-1206.6004v2
doc_title: ""
section_id: sec-008-52-symmetries-and-the-vector-of-riemann-constant
section_title: "Symmetries and the vector of Riemann constants"
section_number: 5.2
pages: 16-19
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.938
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

## Application to Bring's curve {#section5.3}

For Bring's curve we find that everything follows from study of the single (order 5) automorphism given in the Hulek--Craig representation by $$\phi : \  [\bar{x},\bar{y},\bar{z}] \mapsto \big[\zeta^2\bar{x}, \zeta^4 \bar{y}, \bar{z}\big].$$ This has fixed point $[0,0,1]$, or $Q=(0,0)$ in affine coordinates.

The first and easiest calculation is deriving its action on the differentials. We fix the ordered basis of (unnormalized) holomorphic differentials $$\begin{gathered}
  v_1  = \frac{(\bar{y}^3-\bar{x})\mathrm{d}\bar{x}}
    {\partial_y\mathcal{C}(\bar{x},\bar{y},1)}, \qquad
  v_2  = \frac{(\bar{y}^2\bar{x}-1)\mathrm{d}\bar{x}}
    {\partial_y\mathcal{C}(\bar{x},\bar{y},1)}, \qquad
  v_3  = \frac{(\bar{y}-\bar{x}^2)\mathrm{d}\bar{x}}
    {\partial_y\mathcal{C}(\bar{x},\bar{y},1)}, \qquad
  v_4  = \frac{\bar{y}(\bar{x}^2-\bar{y})\mathrm{d}\bar{x}}
    {\partial_y\mathcal{C}(\bar{x},\bar{y},1)}.
\end{gathered}$$ The construction of such holomorphic differentials is algorithmic (see [@DvH]). It is easy to check that $$\begin{gathered}
  \phi^*(v_1)  = \zeta v_1, \qquad
  \phi^*(v_2)  = \zeta^4 v_2,  \qquad
  \phi^*(v_3)  = \zeta^3 v_3, \qquad
  \phi^*(v_4)  = \zeta^2 v_4,
\end{gathered}$$ and so $\phi\sp\ast v_j= v_k {L}\sp{k}_j$ where $${L} =
  \begin{pmatrix}
    \zeta & 0 & 0 & 0 \\
    0 & \zeta^4 & 0 & 0 \\
    0 & 0 & \zeta^3 & 0 \\
    0 & 0 & 0 & \zeta^2
  \end{pmatrix}.$$ Thus there is no invariant differential and ${L}-\mathop{\rm Id}\nolimits$ and so $\hat{L}-\mathop{\rm Id}\nolimits$ are invertible. With $Q=(0,0)$ we see the conditions of Lemma [\[lemtp\]](#lemtp){reference-type="ref" reference="lemtp"} are satisfied.

We note in passing that the differential $v_3$ has a simple zero at $a=[0,0,1]$, a double zero at $b=[0,1,0]$ and a triple triple zero at $c=[1,0,0]_2 \sim [1,t,t^4]$ for the required total of $2g-2 = 6$. Thus we have $\mathcal{K}_\mathcal{C}\sim a+2b+3c$ expressing the canonical divisor in terms of rational points of $\mathcal{C}$.

To proceed with our strategy of determining $K_Q$ we first determine the action of $\phi$ on the homology cycles. With the program `extcurves` at hand this is a simple computational matter, complicated only slightly by the noncanonical nature of the paths we obtained in Section [\[section4.4\]](#section4.4){reference-type="ref" reference="section4.4"}. We obtain $\phi_*(\gamma_i) =\sum_j M_{ij} \gamma_j$ where $$M =
  \begin{pmatrix}
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    -1 & 0 & 0 & -1 & 0 & 0 & 0 & 0 \\
    0 & -1 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & -1 & -1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -1 & 1 & -1 & 1 \\
    0 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & -1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & -1 & 0
  \end{pmatrix}.$$ We remark that consideration of the equation ([\[gensym\]](#gensym){reference-type="ref" reference="gensym"}) for this order five symmetry already imposes that $$\mathcal{A}\sp{T}
  =
  \begin{pmatrix}
    a_1 & 0 & 0 & 0 \\
    0 & a_2 & 0 & 0 \\
    0 & 0 & a_3 & 0 \\
    0 & 0 & 0 & a_4
  \end{pmatrix}
  \begin{pmatrix}
    1 & -1-\zeta^4 & 1+\zeta^4+\zeta^3 & \zeta \\
    1 & -1-\zeta & 1+\zeta+\zeta^2 & \zeta^4 \\
    1 & -1-\zeta^2 & 1+\zeta^2+\zeta^4 & \zeta^3 \\
    1 & -1-\zeta^3 & 1+\zeta^3+\zeta & \zeta^2
  \end{pmatrix},$$ for some unknown $a_i$. These $a_i$ are related by the remaining symmetries and ultimately the period matrix ([\[RRstau\]](#RRstau){reference-type="ref" reference="RRstau"}).

Continuing with our determination of $K_Q$, calculating the Smith normal form of $M-1$ gives us unimodular matrices $U$, $V$ such that $$\begin{gathered}
  M - \mathop{\rm Id}\nolimits= U\mathop{\rm Diag}\nolimits(1, 1, 1, 1, 1, 1, 5, 5) V
\end{gathered}$$ and our earlier constraint $(\mathbf{m}V\sp{-1})_i\equiv0 \mod d_i$, $d_i>1$ takes the form $$\begin{gathered}
  -m_5 +  m_6 - m_7 - 4m_8  \equiv 0 \pmod{5}, \\
  -m_1 + 2m_2 - 3m_3 - m_4 - 11m_5 + 6m_6 - m_7 - 34m_8  \equiv 0 \pmod{5}.
\end{gathered}$$ This gives 25 possible unique candidates for $2K_Q$; we can vary $n_i$ arbitrarily (by adding an appropriate $\mathbf{l}$) without essentially changing $2K_Q$ for (say) $i=2,3,4,6,7,8$ but then $n_1$ and $n_5$ are fixed. Explicitly, every $2K_Q$ is equivalent to one generated by $$\mathbf{n} =
  \begin{pmatrix}
    n_1 & 0 & 0 & 0 & n_5 & 0 & 0 & 0
  \end{pmatrix}.$$ By considering a further symmetry we find further that $n_1 = n_5 = 3$ and at this stage we have $$2K_Q = \frac{1}{5}
  \begin{pmatrix}
    -12 & -3 & 3 & -3
  \end{pmatrix}
  + \tau_0
  \begin{pmatrix}
    -6 & -6 & 3 & 0
  \end{pmatrix}.$$ To determining the appropriate 2-torsion point for square root of the canonical bundle one could further study the action of the symmetries on the spin structures or simply numerically test the vanishing of the theta function. The latter approach yields that

::: theorem
For the Riera and Rodrı́guez homology basis of Bring's curve we have that the vector of Riemann constants is $$K_Q = \frac{1}{10}
    \begin{pmatrix}
      3 & 2 & -2 & -3
    \end{pmatrix}
    +
    \mathop{\rm Im}\nolimits(\tau_0)
    \begin{pmatrix}
      1 & -2 & -2 & 1
    \end{pmatrix}\mathrm{i},$$ where $\tau_0$ is defined by [\[deftau0\]](#deftau0){reference-type="eqref" reference="deftau0"}.
:::

The transformation of theta characteristics $$\mathfrak{g}\cdot(\boldsymbol{a},\boldsymbol{b})=
(\boldsymbol{a},\boldsymbol{b})\mathfrak{g}^{-1}
+\frac12\big(\mathrm{diag}\big(CD^T\big),\mathrm{diag}\big(AB^T\big) \big)$$ for any $\mathfrak{g}=\left(\begin{array}{cc}A&B\\C&D
\end{array}\right)\in\mathrm{Sp}(2g,\mathbb{Z})$ and characteristic $(\boldsymbol{a},\boldsymbol{b})\in\mathbb{Q}^{2g}$ together with the explicit representations of the symmetries yields

::: theorem
Bring's curve has a unique invariant spin-structure.
:::

::: remark
Klein's curve has a unique invariant spin structure [@ks10] and we have shown elsewhere that the vector of Riemann constants is the Abel image of this. To show the analogous result for Bring's curve requires a better understanding of this spin-structure.
:::

## Acknowledgements

We are grateful to Maurice Craig for helpful email exchanges and also to an anonymous referee for careful reading and suggested improvements to the paper.
