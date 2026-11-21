---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-038-11-asymptotics
section_title: "Asymptotics"
section_number: 11
pages: 51-53
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.761
latex_coverage_ratio: 0.945
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:asymptotics label="section:asymptotics"}

We shall need a $q$-analogue of asymptotics *in the sense of Poincaré*. In chapter [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"} we shall develop a more restrictive notion of asymptotics.\
The underlying idea, coming from the thesis [@JLM] of Jose-Luis Martins, is that an asymptotic theory is related to a dynamical system. In the "classical" case of Poincaré asymptotics for ordinary differential equations, say locally at $0$ in ${\mathbf C}^{*}$, the dynamical system is given by the action of the semi-group $\Sigma := e^{]- \infty,0[}$; in our case, the semi-group is plainly $\Sigma := q^{- {\mathbf N}}$ (in the case of difference equations there are two semi-groups: $\Sigma :={\mathbf N}$ and $\Sigma :=-{\mathbf N}$; this was used by J. Roques in [@Ro]). Likewise, the sheaves of functions admitting an asymptotic expansion will be defined on the *horizon*, that is on the quotient space ${\mathbf C}^{*}/\Sigma$. In the classical case, this is the circle $S^{1}$ of directions (rays from $0$) in ${\mathbf C}^{*}$; in our case, this is the elliptic curve ${\mathbf{E}_{q}}= {\mathbf C}^{*}/q^{{\mathbf Z}} = {\mathbf C}^{*}/q^{-{\mathbf N}}$ (in the difference case this is a pair of cylinders).

## $q$-Asymptotics {#subsection:qAsymptotics}

Recall from the introduction that we denote $p: {\mathbf C}^* \rightarrow {\mathbf{E}_{q}}$ the quotient map. We set $$\label{not41}
\Sigma := q^{- {\mathbf N}} \; \text{~and, for~} A \subset {\mathbf C}, \;
\Sigma (A) := \bigcup\limits_{a\in A}  q^{- {\mathbf N}}\{ a\}.$$ Let $U$ be an open set of ${\mathbf C}$ invariant by the semi-group $\Sigma := q^{- {\mathbf N}}$, that is, $q^{-1} U \subset U$ (we shall also call it "stable"). We shall say that a $\Sigma$-invariant subset $K$ of $U$ is a *stable strict subset* if there exists a compact subset $K'$ of $U$ such that $K = \Sigma (K')$; then $K \cup \{ 0\}$ is compact in ${\mathbf C}$. An invariant subset $K \subset U$ is strict if and only if $p(K)$ is a compact subset of ${\mathbf{E}_{q}}$.\
Let $f$ be a function holomorphic on the $\Sigma$-invariant open subset $U$ of ${\mathbf C}^*$ and let $\hat f =\sum\limits_{n\geq 0} a_nz^n \in {{\mathbf C}[[z]]}$. We shall say that $f$ is *$q$-asymptotic* to $\hat f$ on $U$ if, for all $n \in {\mathbf N}$ and every $\Sigma$-invariant strict subset $K \subset U$: $$z^{-n}\bigl(f(x)-S_{n-1} \hat{f}\bigr)$$ []{#not42 label="not42"} is bounded on $K$. Here, $S_{n-1} \hat{f} :=\sum\limits_{p=0}^{n-1} a_p z^p$ stands for \"truncation to $n$ terms\" of $\hat f$. If $f$ admits a $q$-asymptotic expansion it is plainly unique. In the following we will say for simplicity "asymptotic expansion\" for "$q$-asymptotic expansion\". For $n \in {\mathbf N}$ we shall denote $f^{(n)}(0) := n! \, a_n$.\

We denote: []{#not43 label="not43"}

-   ${\mathscr{A}}(U)$ the space of holomorphic functions admitting a $q$-asymptotic expansion on $U$,

-   ${\mathscr{A}}_{0}(U)$ the subspace of ${\mathscr{A}}(U)$ made up of (infinitely) flat functions, *i.e.* those such that $\hat{f} = 0$ and

-   ${\mathscr{B}}(U)$ the space of holomorphic functions bounded on every stable strict subset of $U$.

If $f$ is holomorphic on $U$, then $f \in {\mathscr{A}}(U)$ if and only if $z^{-n} \bigl(f(z) -S_{n-1} \hat{f}(z)\bigr) \in {\mathscr{B}}(U)$ for all $n \in {\mathbf N}$. We check easily that ${\mathscr{A}}(U)$ is a ${\mathbf C}$-algebra and that ${\mathscr{A}}_{0}(U)$ is an ideal of ${\mathscr{A}}(U)$.\
Let again $U$ be a $\Sigma$-invariant open subset of ${\mathbf C}^*$ and let $U_{\infty} := p(U)$; we think of $U_{\infty}$ as the *horizon* of $U$. Every open subset of ${\mathbf{E}_{q}}$ is the horizon of some $\Sigma$-invariant open subset of ${\mathbf C}^*$ (actually, of a great many of them !) and, from now on, we shall often write $U_{\infty}$ an arbitrary open subset of ${\mathbf{E}_{q}}$ and $U$ some adequate $\Sigma$-invariant open subset of ${\mathbf C}^*$ such that $U_{\infty} := p(U)$.\
We introduce three sheaves on ${\mathbf{E}_{q}}$, also denoted ${\mathscr{A}}$, ${\mathscr{A}}_{0}$ and ${\mathscr{B}}$; no confusion should be caused by this overloading of notations. The reader is invited to check that these are indeed sheaves:

-   ${\mathscr{A}}(U_{\infty})$ is the direct limit of all ${\mathscr{A}}(U)$,

-   ${\mathscr{A}}_{0}(U_{\infty})$ is the direct limit of all ${\mathscr{A}}_{0}(U)$ and

-   ${\mathscr{B}}(U_{\infty})$ is the direct limit of all ${\mathscr{B}}(U)$.

In each case the limit is taken for all $\Sigma$-invariant open subset $U$ of ${\mathbf C}^*$ such that $U_{\infty} := p(U)$. Then the ${\mathscr{A}}(U_{\infty})$ form a sheaf of ${\mathbf C}$-algebras and the ${\mathscr{A}}_{0}(U_{\infty})$ a sheaf of ideals.

::: lemm
[]{#lemm:asderive label="lemm:asderive"} Let $U \subset {\mathbf C}$ be a $\Sigma$-invariant open set and $K \subset V$ be a $\Sigma$-invariant strict subset of $U$. There exists a real number $\rho > 0$ such that the closed disc of radius $\rho \left |z \right |$ and center $z$ lies in $U$ for all $z \in K$. Moreover it is possible to choose $\rho >0$ such that $\displaystyle\bigcup_{z\in K} \bar D(z,\rho\left |z\right |)$ be a $\Sigma$-invariant strict subset of $U$.
:::

::: proof
*Proof.* There exists by definition a subset $K'$ of $K$, compact in $U$, such that $K = \Sigma (K')$. By compacity the result of the lemma is true for every $z\in K'$; using the action of $\Sigma$ we get that it is also true for all $z\in K$. ◻
:::

Let $f \in {\mathscr{A}}(U_{\infty})$ and $\hat f := \sum\limits_{n\geq 0} a_n z^n$ its asymptotic expansion. We set $R_n := z^{-n}\bigl(f-S_{n-1} \hat{f}\bigr)$. We have $\displaystyle f=\sum_{p=0}^n a_pz^p+z^{n+1}R_{n+1}$; therefore the derivative $f'$ is given by: $$f' = \sum_{p=1}^n p a_p z^{p-1} + (n+1) z^n R_{n+1} + z^{n+1} R'_{n+1}.$$ If $K\subset U$ is a $\Sigma$-invariant strict subset, then $R_{n+1}$ is bounded by $M_{K,n+1}$ on $K$. Therefore, using Cauchy formula for the derivative and lemma [\[lemm:asderive\]](#lemm:asderive){reference-type="ref" reference="lemm:asderive"}, $R'_n$ is bounded by some positive constant $\frac{M_{K,n+1}}{\rho\left |z\right |}$ on $K$.\
We have $\displaystyle f'=\sum_{n\geq 1} na_nz^{n-1}$ and: $$z^{-n}\bigl(f'(x)-S_{n-1} \hat{f'}\bigr) =
z^{-n}\left(f'(x)- \sum_{p=1}^n n a_p z^{p-1}\right) =
(n+1)R_{n+1} + z R'_{n+1}.$$ Since $\left |(n+1)R_{n+1}+zR'_{n+1} \right |\leq
\bigl(n + 1 + \frac{1}{\rho}\bigr)M_{K,n+1}$, then $z^{-n} \bigl(f'(x)-S_{n-1} \hat{f'}\bigr)$ is bounded on $K$, so that $f'$ admits $\hat f'$ as a $q$-asymptotic expansion on $U$. Hence ${\mathscr{A}}(V_{\infty})$ is a differential algebra and ${\mathscr{A}}_{0}(V_{\infty})$ is a differential ideal of ${\mathscr{A}}(V_{\infty})$.
