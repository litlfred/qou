---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-014-51-the-vector-of-riemann-constants
section_title: "The vector of Riemann constants"
section_number: 5.1
pages: 15-16
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.837
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section5.1 label="section5.1"} Riemann established the fundamental result, $$\theta(e\,|\,\tau)=0 \ \Longleftrightarrow \
e\equiv
\mathcal{A}_Q\left(\sum_{i=1}\sp{g-1}P_i\right)-K_Q\in\mathop{\rm Jac}\nolimits{\mathcal{C}},$$ where $\theta$ is Riemann's theta function, $\mathcal{A}_Q$ is the Abel map with base point $Q\in\mathcal{C}$, $\tau$ is the period matrix, $g$ is the genus of $\mathcal{C}$, $P_i\in\mathcal{C}$ and the equivalence holds in the Jacobian $\mathop{\rm Jac}\nolimits\mathcal{C}=\mathbb{C}\sp{g}/(\mathbb{Z}\sp{g}+\tau\mathbb{Z}\sp{g})$. (We are assuming that $g\ge1$ in what follows.) Both the period matrix $\tau$ and the Abel map depend on a choice of homology basis, the latter through the basis of normalized holomorphic differentials $\boldsymbol{\omega}$ where $\mathcal{A}_Q(P)=\int_Q\sp{P}\boldsymbol{\omega}$. The vector $K_Q$ is known as the vector of Riemann constants[^1] (with base point $Q$) and it also depends on the choice of homology basis. Let ${\left\{\gamma_i\right\}_{i=1}\sp{2g}}=
\left\{\mathfrak{a}_i,\mathfrak{b}_i\right\}_{i=1}\sp{g}$ be our choice of homology basis of $H_1(\mathcal{C},\mathbb{Z})$, where $\mathfrak{a}_i$ and $\mathfrak{b}_i$ are canonically paired. One has that $$K_{Q j}  = -\frac{1}{2}\left( \tau_{jj} + 1\right) +
    \sum_{k\ne j}\oint_{\mathbf{\mathfrak{a}}_{k}}
    \omega_{k}(P)\int^{P}_{Q}\omega_{j}.$$ Because of the integrations involved, both $\tau$ and $K_Q$ are rather transcendental objects. One may also express $$\label{vrcdelta}
K_Q\equiv\mathcal{A}_\ast\left(\Delta-(g-1)Q\right)
=\int_\ast\sp{\Delta}{\boldsymbol{\omega}}-(g-1)\int_\ast\sp{Q}{\boldsymbol{\omega}}
=\mathcal{A}_Q\left(\Delta\right),$$ which holds for any base point $\ast$ of the Abel map and where the degree $(g-1)$ divisor $\Delta$ is that of the Szëgo-kernel [@fay]. The critical relation for us is the linear equivalence $$\label{deltacanonical}
2\Delta\sim
    \mathcal{K}_\mathcal{C},$$ and so $$\label{Kcanonical}
2K_Q\equiv\mathcal{A}_Q(\mathcal{K}_\mathcal{C}).$$ Here $\mathcal{K}_\mathcal{C}$ is the canonical divisor of $\mathcal{C}$, the unique divisor class of degree $2g-2$ of any meromorphic differential on the curve, and (hereafter) $\sim$ denotes linear equivalence. Thus $\Delta$ gives a square root of the canonical bundle or spin-structure on $\mathcal{C}$; the set $\Sigma$ of divisor classes $\mathcal{D}$ such that $2\mathcal{D}\sim\mathcal{K}_\mathcal{C}$ is called the set of *theta characteristics* of $\mathcal{C}$. The vector of Riemann constants gives us the shift in the Jacobian necessary to identify spin structures with the $2$-torsion points of the Jacobian. (Recall, an $N$-torsion point $x$ is such that $Nx$ lies in the period lattice.)

[^1]: The choice of sign of this vector depends on author. We will use that of Fay [@fay] whose convention is the negative of Farkas and Kra [@farkaskra].
