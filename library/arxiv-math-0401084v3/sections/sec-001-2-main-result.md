---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-001-2-main-result
section_title: "Main result"
section_number: 2
pages: 2-4
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.955
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — We calculate limits of the colored Jones polynomials of the ﬁgure- eight knot and conclude that in most cases they determine"
---
To state our main result we recall some of the results in [@Neumann/Zagier:TOPOL85; @Yoshida:INVEM85].

Let $K$ be a hyperbolic knot in the three-sphere $S^3$, that is, the complement $S^3\setminus{K}$ has a complete hyperbolic structure. The complete hyperbolic structure can be deformed by a complex parameter $u$ that is the logarithm of the ratio of the eigenvalues of the image of the meridian $K$ by the holonomy representation $\pi_1(S^3\setminus{K})\to\mathrm{SL}_2(\mathbb{C})$. We also denote by $v$ the logarithm of the eigenvalue of the image of the longitude. If the structure is complete, then $u=0$. Let $\Phi(u)$ be the potential function introduced in [@Neumann/Zagier:TOPOL85 Theorem 3] that satisfies $$\begin{cases}
  \dfrac{d\,\Phi(u)}{du}=2v,
  \\[3mm]
  \Phi(0)=0.
\end{cases}$$ We also put $$f(u):=\frac{\Phi(u)}{4}-\frac{uv}{4}.$$ (see [@Neumann/Zagier:TOPOL85 Equation (50)]).

Let $\ell$ be a loop on the boundary of the tubular neighborhood $N(K)$ of $K$ in $S^3$. Suppose that the hyperbolic structure parameterized by $u$ on $S^3\setminus{K}$ can be completed to an orbifold $K_{u}$ by attaching a solid torus such that its meridian coincides with $\ell$. It is called generalized Dehn surgery and if $pu+qv=2\pi\sqrt{-1}$ for coprime integers $p$ and $q$, then it is usual $(p,q)$-Dehn surgery and $K_{u}$ becomes a closed three-manifold [@Thurston:GT3M Chapter 4] and $\ell$ is homotopic to $p\cdot\text{meridian}+q\cdot\text{longitude}$ in $\pi_1(\partial{N(K)})$. Let $\gamma$ be the core of the solid torus. It is a geodesic in $K_{u}$, and its length and torsion are denoted by $\operatorname{length}(\gamma)$ and $\operatorname{torsion}(\gamma)$ respectively. (If one travels around $\gamma$ then the plane perpendicular to it is rotated by $\operatorname{torsion}(\gamma)$. See [@Yoshida:INVEM85 Definition 1.1] for the precise definition.) Then the volume and the Chern--Simons invariant of $K_{u}$ can be obtained as follows ([@Yoshida:INVEM85 Theorem 2], which was conjectured in [@Neumann/Zagier:TOPOL85 Conjecture]).

::: thm
[]{#thm:Yoshida label="thm:Yoshida"} Put $\lambda(\gamma):=\operatorname{length}(\gamma)+\sqrt{-1}\operatorname{torsion}(\gamma)$. Then we have $$\begin{gathered}
  \operatorname{Vol}(K_{u})+\sqrt{-1}\operatorname{CS}(K_{u})
  \equiv
  \frac{f(u)}{\sqrt{-1}}
  -\frac{\pi}{2}\lambda(\gamma)
  +\operatorname{Vol}\left(S^3\setminus{K}\right)+\sqrt{-1}\operatorname{CS}\left(S^3\setminus{K}\right)
  \\
  \mod{\pi^2\sqrt{-1}\mathbb{Z}}.
\end{gathered}$$
:::

Now we study the case where the knot is the figure-eight knot $E$.

Let $u$ be a complex parameter near $0$. Put $$\begin{aligned}
  m&:=-\exp(u/2),
  \\
  z&:=\frac{-m^4+m^2+1+\sqrt{(m^2+m+1)(m^2+m-1)(m^2-m+1)(m^2-m-1)}}{2m^2},
  \\
  \intertext{and}
  w&:=\frac{m^4+m^2-1+\sqrt{(m^2+m+1)(m^2+m-1)(m^2-m+1)(m^2-m-1)}}{2m^2}.
\end{aligned}$$ We take the branch of the square root so that $z=w=\exp(\pi/3)$ when $u=0$. We also put $$v:=2\log\bigl(z(1-z)\bigr),$$ where the branch is chosen so that $v=0$ when $u=0$. Note that $z$ and $w$ satisfy the following equations. $$\begin{cases}
    \log{w}+\log\bigl(1-z\bigr)=u,
    \\
    \log{z}+\log\bigl(1-z\bigr)+\log{w}+\log\bigl(1-w\bigr)=0.
  \end{cases}$$

Put $$\begin{aligned}
  f(u)&:=\frac{1}{2\pi}\left\{R(z)+R(w)-\frac{\pi^2}{6}\right\}
        -\frac{\sqrt{-1}}{2\pi}\operatorname{Vol}\left(S^3\setminus{E}\right)
  \\
  \intertext{and}
  \Phi(u)&:=4f(u)+uv,
\end{aligned}$$ where $$R(\xi):=\frac{1}{2}\log{\xi}\log(1-\xi)
  -\int_{0}^{\xi}\frac{\log(1-\eta)}{\eta}d\eta$$ is Roger's dilogarithm function. Then $$\begin{gathered}
  \begin{cases}
    \dfrac{d\,\Phi(u)}{du}=2v,
    \\[3mm]
    \Phi(0)=0,
  \end{cases}
  \\
  \intertext{and}
  \operatorname{Vol}(E_u)+\sqrt{-1}\operatorname{CS}(E_u)
  \equiv
  \frac{f(u)}{\sqrt{-1}}-\frac{\pi}{2}\lambda(\gamma)
  +\operatorname{Vol}\left(S^3\setminus{E}\right)
  \mod{\pi^2\sqrt{-1}\mathbb{Z}},
\end{gathered}$$ since $\operatorname{CS}\left(S^3\setminus{E}\right)=0$.

Now we state our main result.

Let $J_N(K;t)$ be the colored Jones polynomial of a knot $K$ corresponding to the $N$-dimensional representation of $sl_2(\mathbb{C})$. We normalize it so that $J_N(\text{unknot};t)=1$. Then we have the following theorem.

::: thm
[]{#thm:main label="thm:main"} Let $E$ be the figure-eight knot. There exists a neighborhood $U$ of $0$ in $\mathbb{C}$ such that for any $u\in({U}\setminus\pi\sqrt{-1}\mathbb{Q})\cup\{0\}$, the following limit exists: $$(u+2\pi\sqrt{-1})
  \lim_{N\to\infty}
  \frac{\log\Bigl(J_N\bigl(E;\exp\left((u+2\pi\sqrt{-1})/N\right)\bigr)\Bigr)}
  {N}.$$ Moreover if we denote the limit by $H(u)$, then it can be extended to a complex analytic function and it satisfies the following equalities. $$\begin{cases}
  \dfrac{d\,H(u)}{du}=\dfrac{v}{2}+\pi\sqrt{-1},
  \\[3mm]
  H(0)=\sqrt{-1}\operatorname{Vol}(S^3\setminus{E}).
\end{cases}$$
:::

::: rem
The precise meaning of the limit is as follows. If the ratio $$\frac{J_N\bigl(E;\exp\left((u+2\pi\sqrt{-1})/N\right)\bigr)}
  {\exp\bigl(N\,h(u)\bigr)}$$ grows polynomially with respect to $N$, then we denote the limit $$\frac{\log\Bigl(J_N\bigl(E;\exp\left((u+2\pi\sqrt{-1})/N\right)\bigr)\Bigr)}
  {N}$$ by $h(u)$. So it is defined modulo $2\pi\sqrt{-1}$.
:::

As a corollary we can express the volume and the Chern--Simons invariant of a three-manifold obtained from the figure-eight knot by generalized Dehn surgery.

::: cor
[]{#cor:Vol_CS label="cor:Vol_CS"} Let $E_u$ be the three-manifold obtained from the figure-eight knot by generalized Dehn surgery corresponding to $u$ near $0$ such that $\pi{u}\notin\mathbb{Q}$. Then $$\operatorname{Vol}(E_u)+\sqrt{-1}\operatorname{CS}(E_u)
  \equiv
  \frac{H(u)}{\sqrt{-1}}-\pi{u}-\frac{uv}{4\sqrt{-1}}
  -\frac{\pi}{2}\lambda(\gamma)
  \mod{\pi^2\sqrt{-1}\mathbb{Z}}.$$
:::
