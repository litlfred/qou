---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-009-9-periodic-braids
section_title: "Periodic Braids"
section_number: 9
pages: 61-64
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.963
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the Weyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
[]{#sec:periodic label="sec:periodic"}

## 

In this section and the next, *we no longer assume that $W$ is crystallographic*. Let $w_0$ be the longest element of $W$ with respect to the chosen Coxeter presentation (see §[\[subsec:coxeter-group\]](#subsec:coxeter-group){reference-type="ref" reference="subsec:coxeter-group"}). The **full twist** of $\mathit{Br}_W$ is the positive braid $$\begin{aligned}
\pi = \sigma_{w_0}^2 \in \mathit{Br}_W^+.
\end{aligned}$$ It is central in $\mathit{Br}_W$ [@bm_1997 §2]. We say that a braid $\beta \in \mathit{Br}_W$ is **periodic** iff $$\begin{aligned}
\beta^n = \pi^m
\end{aligned}$$ for some $\frac{m}{n} \in \bb{Q}$, in which case we say that $\frac{m}{n}$ is the **slope** of $\beta$.

::: thm
[]{#thm:ll label="thm:ll"} If $\beta \in \mathit{Br}_W$ is periodic of slope $\frac{m}{n}$, then $\beta = \gamma^m$ and $\pi = \gamma^n$ for some $\gamma \in \mathit{Br}_W$.
:::

::: proof
*Proof.* Let $d$ be the minimal positive exponent such that $\sigma_{w_0}^d$ is central in $\mathit{Br}_W$. Either $d = 1$ or $d = 2$.

In [@ll], E.-K. Lee and S.-J. Lee say that an element $\gamma \in \mathit{Br}_W$ is **primitive** iff, whenever $\gamma = \delta^\ell$ for some $\delta \in \mathit{Br}_W$, we have $\ell = \pm 1$. Theorem 3.14 of *ibid.* implies that if $\gamma$ is primitive and periodic, then $\gamma$ is a positive root of $\sigma_{w_0}^d$.

If $\beta$ is periodic, then any root of $\beta$ is also periodic. So it remains to check that some root of $\beta$ is primitive. Indeed, this follows from the well-ordering principle, because the writhe of $\beta$ is an integer. ◻
:::

::: rem
In type $A$, where the elements of $\mathit{Br}_W$ represent topological braids, Theorem [\[thm:ll\]](#thm:ll){reference-type="ref" reference="thm:ll"} was first shown in 1934 by Kerékjártó--Eilenberg [@eilenberg].
:::

::: rem
A result of Bessis implies that if an $n$th root of $\pi$ exists, then the $n$th roots of $\pi$ form a single conjugacy class in $\mathit{Br}_W$ [@bessis Thm. 12.4(ii)].
:::

## 

The following result, an incarnation of Schur's lemma, is [@gp Thm. 9.4.3].

::: thm
For all $\phi \in \hat{W}$, the full twist acts on the underlying $H_W$-module of $\phi_{\bm{q}}$ by the scalar $\bm{q}^{\bb{c}(\phi)}$, where $\bb{c}(\phi)$ is the content of $\phi$ (see §[\[subsec:families\]](#subsec:families){reference-type="ref" reference="subsec:families"}). In particular, $\phi_{\bm{q}}(\pi) = \bm{q}^{\bb{c}(\phi)}\phi(1)$.
:::

The following corollary is a mild generalization of [@bm_1997 Prop. 9.2.8], but we give the proof anyway. The proof is based on [@jones Lem. 9.4], which Jones used to calculate the HOMFLY polynomials of torus knots.

::: cor
[]{#cor:br-to-w label="cor:br-to-w"} If $\phi \in \hat{W}$ and $\beta \in \mathit{Br}_W$ is periodic of slope $\nu\in \bb{Q}$, then $$\begin{aligned}
\phi_{\bm{q}}(\beta) = \bm{q}^{\nu\bb{c}(\phi)} \phi(w),
\end{aligned}$$ where $w \in W$ is the image of $\beta$ under the surjection $\mathit{Br}_W \surject W$.
:::

::: proof
*Proof.* It suffices to prove the result when $\bm{q}^{\frac{1}{2}}$ has been specialized to a generic complex number $q^{\frac{1}{2}}$. We set $$\begin{aligned}
H_W[q^{\frac{1}{2}}] = H_W \otimes_{\bb{Z}[\bm{q}^{\pm 1/2}]} \bb{C},
\end{aligned}$$ where $\bb{Z}[\bm{q}^{\pm\frac{1}{2}}] \to \bb{C}$ sends $\bm{q}^{\frac{1}{2}} \mapsto q^{\frac{1}{2}}$, and $$\begin{aligned}
\phi_q = \phi_{\bm{q}}|_{\bm{q}^{1/2} = q^{1/2}}.
\end{aligned}$$ Write $\nu= \frac{m}{n}$ in lowest terms. By the theorem, $q^{-m\bb{c}(\phi)}\pi^m$ acts on the underlying $H_W[q^{\frac{1}{2}}]$-module of $\phi_q$ by the identity operator $I$. Since $\beta^n = \pi^m$, we deduce that $q^{-\nu\bb{c}(\phi)} \beta$ acts by an $n$th root of $I$.

Recall that $H_W|_{q = 1} = \bb{Z}[W]$. Choose a generic path in the complex plane from $q$ to $1$. Since the (diagonalizable) roots of $I$ do not deform, the deformation of $q$ along this path shows that the following operators must have the same eigenvalue spectrum:

-   The action of $q^{-\nu\bb{c}(\phi)}\beta$ on the underlying $H[q^{\frac{1}{2}}]$-module of $\phi_q$.

-   The action of $w$ on the underlying $\bb{C}[W]$-module of $\phi$.

The result follows. ◻
:::

## 

Let $\bb{V}$ be a realization of $W$ over $\bb{C}$ such that $\bb{V}^W = 0$. A vector of $\bb{V}$ is **regular** with respect to $W$ iff its stabilizer in $W$ is trivial, or equivalently, it avoids the reflecting hyperplanes that generate the $W$-action. Suppose that an element $w \in W$ admits a regular eigenvector in $\bb{V}$ with eigenvalue $\zeta \in \bb{C}^\times$. In this case, $\zeta$ must be a root of unity. We say that $\zeta$ is **regular** with respect to $W$ and that $w$ is a **$\zeta$-regular element** of $W$. The following results are parts (iv) and (v) of [@springer_1974 Thm. 4.2], respectively.

::: thm
[]{#thm:conjugacy label="thm:conjugacy"} For any $\zeta \in \bb{C}^\times$, the set of $\zeta$-regular elements of $W$ is either empty or forms a single conjugacy class.
:::

::: thm
[]{#thm:fake-deg label="thm:fake-deg"} If $w \in W$ is a $\zeta$-regular element, then $$\begin{aligned}
\phi(w) = \mathrm{Feg}_\phi(\zeta^{-1}) = \mathrm{Feg}_\phi(\zeta)
\end{aligned}$$ for all $\phi \in \hat{W}$, where $\mathrm{Feg}_\phi$ is the fake degree of $\phi$ (see §[\[subsec:degrees\]](#subsec:degrees){reference-type="ref" reference="subsec:degrees"}).
:::

::: rem
In [@springer_1974 170], Springer claims that if $n$ is a fixed integer, then the regular elements of $W$ of order $n$ form a single conjugacy class. This claim, which is stronger than Theorem [\[thm:conjugacy\]](#thm:conjugacy){reference-type="ref" reference="thm:conjugacy"}, fails when $W$ is not crystallographic. For example, let $W$ be the Coxeter group of type $I_2(5)$ and let $w$ be a Coxeter element. Then $w$ and $w^2$ are both regular elements of order $5$, but they are not conjugate.
:::

Regular elements of $W$ are related to periodic elements of $\mathit{Br}_W$ by the following results, which are respectively Proposition 3.11 and Théorème 3.12 in [@bm_1997].

::: prop
[]{#prop:broue-michel label="prop:broue-michel"} If $w \in W$ is regular of order $n$, then $\sigma_w^n = \pi$.
:::

::: thm
[]{#thm:broue-michel label="thm:broue-michel"} If $\gamma \in \mathit{Br}_W^+$ satisfies $\gamma^n = \pi$ for some $n$, then its image in $W$ is a $e^{\frac{2\pi i}{n}}$-regular element.
:::

::: cor
[]{#cor:regular label="cor:regular"} If $\beta \in \mathit{Br}_W$ is periodic of slope $\nu \in \bb{Q}$, then the image of $\beta$ in $W$ is a $e^{2\pi i\nu}$-regular element.
:::

::: proof
*Proof.* This is immediate from Theorem [\[thm:broue-michel\]](#thm:broue-michel){reference-type="ref" reference="thm:broue-michel"} when $\beta$ is a root of $\pi$. Theorem [\[thm:ll\]](#thm:ll){reference-type="ref" reference="thm:ll"} lets us bootstrap to the general case. ◻
:::

::: rem
We emphasize that Theorem [\[thm:broue-michel\]](#thm:broue-michel){reference-type="ref" reference="thm:broue-michel"} is deeper than Proposition [\[prop:broue-michel\]](#prop:broue-michel){reference-type="ref" reference="prop:broue-michel"}: Its proof relies on results used by Charney to prove the biautomaticity of Artin groups [@bm_1997 §3.19].
:::

## 

Theorem [\[thm:periodic\]](#thm:periodic){reference-type="ref" reference="thm:periodic"} states that if $\beta \in \mathit{Br}_W$ is periodic of slope $\nu\in \bb{Q}$, then its $R(W)$ trace is given by $$\begin{aligned}
\langle{\beta}\rangle_{\bm{q}} 
=
    \sum_{\psi \in \hat{W}} 
    {\bm{q}^{\nu\bb{c}(\psi)}}
    \mathrm{Deg}_\psi(\zeta) \psi,
\end{aligned}$$ where $\zeta = e^{2\pi i\nu}$ and $\mathrm{Deg}_\phi$ is the unipotent degree of $\phi$ (see §[\[subsec:degrees\]](#subsec:degrees){reference-type="ref" reference="subsec:degrees"}).

::: proof
*Proof of Theorem [\[thm:periodic\]](#thm:periodic){reference-type="ref" reference="thm:periodic"}.* By Corollary [\[cor:regular\]](#cor:regular){reference-type="ref" reference="cor:regular"}, the image of $\beta$ in $W$ is a $\zeta$-regular element. Therefore, by Corollary [\[cor:br-to-w\]](#cor:br-to-w){reference-type="ref" reference="cor:br-to-w"} and Theorem [\[thm:fake-deg\]](#thm:fake-deg){reference-type="ref" reference="thm:fake-deg"}, $$\begin{aligned}
\phi_{\bm{q}}(\beta) = \bm{q}^{\nu\bb{c}(\phi)} \mathrm{Feg}_\phi(\zeta).
\end{aligned}$$ Therefore, by Lemma-Postulate [\[lempost:fourier\]](#lempost:fourier){reference-type="ref" reference="lempost:fourier"}(2) and Corollary [\[cor:content\]](#cor:content){reference-type="ref" reference="cor:content"}, $$\begin{aligned}
\begin{split}
\sum_{\phi \in \hat{W}} 
{\{\phi, \psi\}} \phi_{\bm{q}}(\beta) 
&=  \bm{q}^{\nu\bb{c}(\psi)}
    \sum_{\phi \in \hat{W}} 
    {\{\phi, \psi\}}
    \mathrm{Feg}_\phi(\zeta) \\
&=  \bm{q}^{\nu\bb{c}(\psi)}
    \mathrm{Deg}_\psi(\zeta),
\end{split}
\end{aligned}$$ as needed. ◻
:::
