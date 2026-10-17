---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-003-2-strong-rayleigh-property-stochastic-covering-p
section_title: "Strong Rayleigh property, stochastic covering property, and other negative dependence conditions"
section_number: 2
pages: 4-6
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.977
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#sec:covering label="sec:covering"}

Let $[n]$ denote $\{ 1 , \ldots , n \}$ and let ${\mathcal B}_n := \{ 0 , 1 \}^n$ denote the Boolean lattice of rank $n$, with coordinatewise partial order. The function $N : {\mathcal B}_n \to \mathbb{Z}^+$ will be used throughout to denote the counting function defined by $N(\omega) := \sum_{j=1}^n
\omega_j$. A measure $\nu$ on ${\mathcal B}_n$ is said to be **$k$-homogeneous** if $\nu$ is supported on the set of $\{ \omega : N(\omega) = k \}$. The probability measure $\nu$ on ${\mathcal B}_n$ is said to be **negatively associated** if $\int fg \, d\nu\leq (\int f \, d\nu) (\int g \, d\nu)$ for every pair of nonnegative monotone functions $f$ and $g$ such that for some set $S \subseteq [n]$, the function $f$ depends only on coordinates $\{ \omega_j : j \in S \}$ while the function $g$ depends only on coordinates $\{ \omega_j : j \in S^c \}$.

The **strong Rayleigh condition** is said to hold for a measure ${\mathbb P}$ on ${\mathcal B}_n$ if the generating function $$\sum_{\omega \in {\mathcal B}_n} {\mathbb P}(\omega) \prod_{j=1}^n z_j^{\omega_j}$$ has no roots $(z_1 , \ldots , z_n)$ all of whose coordinates lie in the (strict) upper half plane. This and many consequences are given in [@borcea-branden-liggett], including (implicitly) the **stochastic covering property** (see Proposition [\[pr:SR -\> SCP\]](#pr:SR -> SCP){reference-type="ref" reference="pr:SR -> SCP"}), which was conjectured [@pemantle-NA Conjecture 9] to follow from something a little weaker. Some of the relevant implications are summarized in Figure [1](#fig:implications){reference-type="ref" reference="fig:implications"} below.

The definition of the stochastic covering property requires a few preliminary definitions. Recall that a measure $\nu$ on a partially ordered set is said to **stochastically dominate** a measure $\rho$, denoted $\nu\succeq \rho$, if $\nu(A) \geq \rho(A)$ for every upwardly closed set $A$. An equivalent condition is that there exists a coupling, that is a measure $Q$ on ${\mathcal B}_n \times {\mathcal B}_n$ with respective marginals $\nu$ and $\rho$, supported on the set $\{ (x,y) : x \geq y \}$. If ${\mathbb P}$ is a measure on ${\mathcal B}_n$ making the coordinate variables $\{ X_i : 1 \leq i \leq n \}$ negatively associated, an immediate consequence of negative association is that the conditional measure $({\mathbb P}{\, | \, } X_n = 0)$ on ${\mathcal B}_{n-1}$ stochastically dominates the conditional measure $({\mathbb P}{\, | \, } X_n = 1)$.

![relations among negative dependence properties](implications){#fig:implications}

We say that the probability measure $\nu$ on ${\mathcal B}_n$ **stochastically covers** another probability measure $\rho$ if there is a measure on ${\mathcal B}_n^2$ with first marginal $\nu$ and second marginal $\rho$ (in other words, a coupling) supported on the set of pairs $(x,y)$ for which $x = y$ or $x$ covers $y$ in the coordinatewise partial order; here $x$ is said to cover $y$ when $x > y$ but there is no $z$ such that $x > z > y$. We denote the covering relation in ${\mathcal B}_n$ by $x \; \cdot \kern-5pt >y$, and one measure covering another by $\nu\triangleright\rho$. Stochastic covering is strictly stronger than stochastic domination, and may be thought of as "stochastic domination, but by at most 1".

Stochastic covering combines stochastic ordering with closeness in the so-called $L^\infty$-transportation metric, defined on probability measures on a given metric space as follows: $d_\infty
(\mu , \nu)$ is the least $\rho$ such that there is a coupling of $\mu$ and $\nu$ supported on the set $\{ (x,y) : |x-y| \leq \rho \}$. Thus $\mu \triangleright\nu$ implies $d_\infty (\mu , \nu) \leq 1$. This is useful because if $||f||_{\rm Lip}$ denotes the Lipschitz norm on Lipschitz functions, then $$\label{eq:transport}
\left | \int f \, d\mu - \int f \, d\nu \right |
  \leq ||f||_{\rm Lip} \; d_\infty (\mu , \nu) \, .$$

Suppose that $x \geq y$ and we compare the conditional laws ${\mathbb P}_x :=
({\mathbb P}{\, | \, } X_j = x_j, j \in S)$ and ${\mathbb P}_y := ({\mathbb P}{\, | \, } X_j = y_j, j \in S)$ on the remaining coordinates, that is as laws on $\{ 0 , 1 \}^{S^c}$. If ${\mathbb P}$ and all its conditionalizations are negatively associated, it follows that ${\mathbb P}_x \preceq {\mathbb P}_y$.

::: defn
We say that a probability measure $\nu$ on ${\mathcal B}_n$ has the stochastic covering property if for every $S \subseteq \{ 1 ,
\ldots , n \}$ and for every $x,y \in \{ 0 , 1 \}^S$ with $x \; \cdot \kern-5pt >y$, the conditional law $(\nu{\, | \, } X_j = x_j, j \in S)$ is covered by the conditional law $(\nu{\, | \, } X_j = y_j, j \in S)$.
:::

In [@borcea-branden-liggett Theorem 4.2] it was shown that strong Rayleigh property implies the **projected homogeneous Rayleigh** property (PHR), meaning that the measure can be embedded as the first $n$ coordinates of a homogeneous measure $\nu'$ on ${\mathcal B}_m$, for some $m \geq n$, that has the ordinary Rayleigh property; the ordinary Rayleigh property is that the partial derivatives of the generating function $F(z_1 , \ldots , z_n) := {\mathbb E}\prod_{j=1}^n z_j^{X_j}$ satisfy $F_i F_j \geq F_{ij} F$ at any point with positive real coordinates. We record two further consequences.

::: pr
[]{#pr:SR -> SCP label="pr:SR -> SCP"} PHR (and hence strong Rayleigh) implies the stochastic covering property.
:::

PHR implies negative association of all conditionalizations (CNA) [@borcea-branden-liggett Theorem 4.10]; the homogeneous extension $\nu'$ witnessing the PHR property is also PHR hence also CNA. By negative association, if $x \; \cdot \kern-5pt >y$ then $(\nu' {\, | \, } X_j = y_j , j \in S) \succeq
(\nu' {\, | \, } X_j = x_j , j \in S)$, when viewed as measures on the coordinates in $[m] \setminus S$. Because $\nu'$ is homogeneous, the coupling that witnesses this $\succeq$ relation in fact witnesses the relation $\triangleright$. Restricting to $[n] \setminus S$ we see that $(\nu{\, | \, } X_j = y_j , j \in S) \triangleright(\nu{\, | \, } X_j = x_j , j \in S)$. $\hfill \Box$

::: pr
[]{#pr:k cover label="pr:k cover"} Let ${\mathbb P}$ be a strong Rayleigh measure on ${\mathcal B}_n$. Let ${\mathbb P}_k$ denote ${\mathbb P}$ conditioned on $N = k$. Then for every $0 \leq k \leq n-1$ such that ${\mathbb P}(N=k)$ and ${\mathbb P}(N=k+1)$ are both nonzero, we have the covering relation ${\mathbb P}_{k+1} \triangleright{\mathbb P}_k$. $\hfill \Box$
:::
