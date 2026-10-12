---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-003-41-representation
section_title: "Representation"
section_number: 4.1
pages: 10-11
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 0.932
---
Let $x$ and $y$ be the Wirtinger generators of the fundamental group $\pi_1(S^3\setminus{E})$ (with a base point above the paper) of the complement of the figure-eight knot $E$ depicted in Figure [1](#fig:fig8_pi1){reference-type="ref" reference="fig:fig8_pi1"}.

![Generators of the fundamental group of the complement of the figure-eight knot](fig8_pi1.eps){#fig:fig8_pi1}

The group $\pi_1(S^3\setminus{E})$ has the following presentation: $$\pi_1(S^3\setminus{E})
  =
  \langle
    x,y
    \mid
    xy^{-1}x^{-1}yx=yxy^{-1}x^{-1}y
  \rangle.$$ Due to [@Riley:QUAJM31984] any non-abelian representation $\rho$ of $\pi_1(S^3\setminus{E})$ into $SL(2;\mathbb{C})$ is, up to conjugation, given as follows: $$\begin{aligned}
  \rho(x)&
  :=
  \begin{pmatrix}
    m^{1/2} & 1 \\
    0       & m^{-1/2}
  \end{pmatrix},
  \\
  \rho(y)
  &:=
  \begin{pmatrix}
    m^{1/2} & 0 \\
    -d      & m^{-1/2}
  \end{pmatrix},
\end{aligned}$$ where $$d=
  \frac{1}{2}
  \left(
    m+m^{-1}-3\
    \pm
    \sqrt{(m+m^{-1}+1)(m+m^{-1}-3)}
  \right).$$ Since the longitude $\lambda$ is given by $xy^{-1}xyx^{-2}yxy^{-1}x^{-1}$ if we read it off from the top right, we have $$\rho(\lambda)
  =
  \begin{pmatrix}
    \ell(m)^{\pm1}& (m^{1/2}+m^{-1/2})\sqrt{(m+m^{-1}+1)(m+m^{-1}-3)} \\
    0             & \ell(m)^{\mp1}
  \end{pmatrix},$$ where $$\ell(m)
  :=
  \frac{m^2-m-2-m^{-1}+m^{-2}}{2}
  +
  \frac{(m-m^{-1})}{2}\sqrt{(m+m^{-1}+1)(m+m^{-1}-3)}.$$ See also [@Murakami:ACTMV2008 Section 3.1].

Let $\rho_u$ be the representation given by putting $m:=e^u$. We introduce a parameter $v$ so that $\ell(e^u)=e^{v/2}$. Since we assume that $0<u<\log\bigl((3+\sqrt{5})/2\bigr)$, we have $2<e^u+e^{-u}<3$. Therefore we have $$|\ell(e^u)|^2
  =
  \frac{1}{4}
  (e^{2u}-e^u-2-e^{-u}+e^{-2u})^2
  -
  \frac{1}{4}
  (e^u-e^{-u})^2(e^u+e^{-u}+1)(e^u+e^{-u}-3)
  =
  1$$ and so $v$ is purely imaginary.

The representation $\rho_u$ gives an incomplete hyperbolic structure to $S^3\setminus{E}$ and its completion is the generalized Dehn surgery [@Thurston:GT3M] with parameter $(p,q)$ with $pu+qv=2\pi\sqrt{-1}$. Since $v$ is purely imaginary $p=0$ and $q=2\pi\sqrt{-1}/v$. Therefore the completion is a cone manifold whose underlying space is the $0$-surgery of $S^3$ along the figure-eight knot with singularity the core of the surgery and with cone angle $\alpha=\operatorname{Im}(v)=v/\sqrt{-1}$. Note that when $u=0$, the cone angle is $2\pi$ and when $u=\log\bigl((3+\sqrt{5})/2\bigr)$, the cone angle is $0$. See [@Hilden/Lozano/Montesinos:JMASU1995] for more details about the geometric structure of this manifold.

In the following two subsections we will calculate the Reidemeister torsion and the Chern--Simons invariant associated with $\rho_u$.
