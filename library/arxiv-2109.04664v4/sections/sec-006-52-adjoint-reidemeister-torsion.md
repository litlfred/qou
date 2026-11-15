---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER"
section_id: sec-006-52-adjoint-reidemeister-torsion
section_title: "Adjoint Reidemeister torsion"
section_number: 5.2
pages: 15-16
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.976
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — We study the asymptotic behavior of the N-dimensional colored Jones polynomial"
---
For a representation $\rho\colon\pi_1(X)\to\rm{SL}(2;\mathbb{C})$, one can consider the cochain complex $C^{\ast}(X;\mathfrak{sl}(2;\mathbb{C})_{\rho}):=\operatorname{Hom}_{\mathbb{Z}[\pi_1(X)]}(C_{\ast}(\tilde{X};\mathbb{Z}),\mathfrak{sl}(2;\mathbb{C}))$ twisted by the adjoint action of $\rho$. Here $\tilde{X}$ is the universal cover of $X$, $\pi_1(X)$ acts on $\tilde{X}$ as the deck transformation, and the Lie algebra $\mathfrak{sl}(2;\mathbb{C})$ is regarded as a $\mathbb{Z}[\pi_1(X)]$-module by the adjoint action of $\rho$. The Reidemeister torsion $\mathbb{T}_{\mu}(\rho)\in\mathbb{C}$ associated with the meridian $\mu$, twisted by the adjoint action of $\rho$ is defined as the torsion of the cochain complex $C^{\ast}(X;\mathfrak{sl}(2;\mathbb{C})_{\rho})$. The following formula is known for the case of the figure-eight knot: $${\mathbb{T}}_{\mu}(\rho)
  =
  \pm
  \frac{2}{\sqrt{(e^{\xi}+e^{-\xi}+1)(e^{\xi}+e^{\xi}-3)}}.$$ See [@Porti:MAMCAU1997; @Dubois:CANMB2006; @Murakami:JTOP2013].

## Chern--Simons invariant

Let $M$ be a three-manifold with boundary a torus $T$, and $\{\mu,\lambda\}$ be generators of $\pi_1(T)$. For a representation $\rho\colon\pi_1(M)\to\rm{SL}(2;\mathbb{C})$, we can define the Chern--Simons invariant as follows.

Let $A$ be an $\mathfrak{sl}(2;\mathbb{C})$-valued $1$-form $A$ on $M$ that defines the flat connection corresponding to $\rho$. Assume that $\rho\Bigm|_{T}$ is diagonalizable for simplicity. Then by a suitable conjugation, one has $$\rho(\mu)
  =
  \begin{pmatrix}
    e^{2\pi\sqrt{-1}\alpha}& 0               \\
    0               & e^{-2\pi\sqrt{-1}\alpha}
  \end{pmatrix},
  \quad
  \rho(\lambda)
  =
  \begin{pmatrix}
    e^{2\pi\sqrt{-1}\beta}& 0               \\
    0              &e^{-2\pi\sqrt{-1}\beta}
  \end{pmatrix}.$$ Then up to gauge equivalence, we can assume that $A$ is of the form $$\begin{pmatrix}
    \sqrt{-1}\alpha& 0       \\
    0       & -\sqrt{-1}\alpha
  \end{pmatrix}
  \,dx
  +
  \begin{pmatrix}
    \sqrt{-1}\beta& 0      \\
    0      &-\sqrt{-1}\beta
  \end{pmatrix}
  \,dy$$ near $T$, where $dx$ and $dy$ are the $1$-forms corresponding to $\mu$ and $\lambda$ respectively. Then the Chern--Simons invariant $\operatorname{cs}_{M}(\rho;\alpha,\beta)$ of $\rho$ associated with $(\alpha,\beta)$ is defined by $$\operatorname{CS}_{M}(\rho;\alpha,\beta)
  :=
  \frac{-1}{8}
  \int_{M}\operatorname{Tr}\left(dA\wedge A+\frac{2}{3}A\wedge A\wedge A\right)\in\mathbb{C}/(\pi^2\mathbb{Z}).$$ Note that $\operatorname{Im}\operatorname{CS}_{M}(\rho_0;0,0)$ coincides with the hyperbolic volume if the interior of $M$ possesses a complete hyperbolic structure, where $\rho_0$ is the Levi--Civita connection. See [@Kirk/Klassen:COMMP1993] for details.

In [@Murakami/Tran:2020], we proved the following theorem.

::: thm
The Chern--Simons invariant $\operatorname{CS}_{E}(\rho;\xi,\eta)$ of the representation $\rho$ associated with $(\xi,\eta)$ is given by $$\operatorname{CS}_{E}(\rho;\xi,\eta)
  =
  S(\xi)-\frac{\xi\eta}{2}.$$ Here we choose $\mu$ and $\lambda$ to be the meridian and the preferred longitude of $E$ respectively, and we assume that $\rho$ sends $$\mu
  \mapsto
  \begin{pmatrix}
    e^{\xi/2}&\ast \\
    0          &e^{-\xi/2}
  \end{pmatrix},
  \quad
  \lambda
  \mapsto
  \begin{pmatrix}
    e^{\eta/2}&\ast \\
    0         &e^{-\eta/2}
  \end{pmatrix}.$$ up to conjugation.
:::
