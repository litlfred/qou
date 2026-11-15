---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-039-112-asymptotic-expansions-and-mathcal-cinfty-fun
section_title: "Asymptotic expansions and ${\mathcal C}^{\infty}$ functions in Whitney sense"
section_number: 11.2
pages: 53-58
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.874
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsubtion:asymptoticsandWhitney label="subsubtion:asymptoticsandWhitney"}

::: lemm
[]{#lemm:ascle label="lemm:ascle"} Let $U$ be a $\Sigma$-invariant open set of ${\mathbf C}$ and $f \in {\mathscr{A}}(U_{\infty})$. Let $K\subset U$ be an invariant strict subset.

-   There exists a positive constant $C_K$ (depending on $f$) such that, for all $z_1,z_2 \in K \cup \{ 0\}$: $$\left |f(z_1)-f(z_2) \right |\leq C_K \left |z_1 - z_2 \right |.$$

-   For all $n\in{\mathbf N}$ there exists a positive constant $C_{K,n}$ (depending on $f$) such that, for all $z_1,z_2\in K\cup\{ 0\}$: $$\left |f(z_1) -\sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p \right |
    \leq C_{K,n} \left |z_1 - z_2\right |^{n+1}.$$

-   $$\lim_{z_1 \rightarrow 0, z_2 \rightarrow 0
    \atop ~z_1,z_2 \in K\cup\{ 0\},z_1 \neq z_2}
    \dfrac{1}{\left |z_1 - z_2 \right |^n}
    \left(f(z_1)-\sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p \right) = 0.$$
:::

::: proof
*Proof.* (i) We choose $\rho >0$ (depending on $K$) as in lemma [\[lemm:asderive\]](#lemm:asderive){reference-type="ref" reference="lemm:asderive"}; then $K_1:=\displaystyle\bigcup_{z\in K} \bar D(z,\rho\left |z\right |)$ is an invariant strict subset of $U$. We set: $$M_K := \sup_{z\in K} \frac{\left |f(z)-f(0)\right |}{\left |z\right |}~,\quad
M'_{K_1} := \sup_{z\in K_1} \left |f'(z)\right |~.$$

Let $z_1,z_2\in K\cup \{ 0\}$. We shall consider separately three cases: (a) $z_2=0$; (b) $z_2\neq 0$ and $\left |z_1 - z_2 \right |\leq \rho \left |z_2 \right |$; (c) $z_2\neq 0$ and $\left |z_1 - z_2 \right |> \rho \left |z_2 \right |$.

The cases (a) and (b) are easy. In fact, if $z_2=0$, then: $$\left |f(z_1) - f(z_2) \right |= \left |f(z_1)-  f(0) \right |\leq
M_K \left |z_1 \right |=M_K \left |z_1 - z_2\right |.$$ If $z_2 \neq 0$ and $\left |z_1 - z_2 \right |\leq \rho \left |z_2 \right |$, then $z_2 \in K$ and the closed interval $[z_1,z_2]$ is contained in $K_1$; therefore: $$\left |f(z_1) - f(z_2) \right |\leq M'_{K_1} \left |z_1 - z_2\right |.$$

Now consider case (c). If $z_2 \in K$ and $\left |z_1 - z_2 \right |> \rho \left |z_2 \right |$, then we write $f(z_1) - f(z_2) = f(z_1) - f(0) -\bigl(f(z_2)-f(0)\bigr)$ and we have: $$\left |f(z_1) - f(0) \right |\leq M_K \left |z_1 \right |\leq
M_K\bigl(\left |z_2 \right |+ \left |z_1 - z_2\right |\bigr)
\leq \left(\frac{1}{\rho}+1 \right) M_K \left |z_1 - z_2 \right |$$ and $$\left |f(z_2) - f(0) \right |\leq M_K \left |z_2 \right |\leq
\frac{1}{\rho} M_K \left |z_1 - z_2\right |,$$ whence: $$\left |f(z_1) - f(z_2) \right |\leq
\frac{2+\rho}{\rho} M_K \left |z_1 - z_2\right |.$$

Last, let $C_K := \max \left(M'_{K_1}, \frac{2+\rho}{\rho}M_K \right)$; then, for all $z_1,z_2 \in K \cup \{0\}$, we have: $$\left |f(z_1) - f(z_2)\right |\leq C_K \left |z_1 - z_2\right |.$$

\(ii\) We define $\rho$, $K_1$, $C_K$ as in (i). We set: $$C_{K,n} := \sup_{z\in K}
\left |f(z) - \sum_{p=0}^n \frac{f^{(p)}(0)}{p!} z^p \right |\left |z^{-n-1}\right |~,
\quad
M'_{K_1,n} := \sup_{z\in K_1} \left |f^{(n+1)}(z) \right |~.$$ The result is obviously true if $f$ is a polynomial. Therefore, fixing $n \in {\mathbf N}$ it suffices to prove the result when $f = z^{n+1}g$, $g \in {\mathscr{A}}(U_{\infty})$.

As in (i) we shall consider separately the three cases (a), (b), (c). If $z_2 = 0$, then the result merely comes from the following relation: $$\left |f(z_1) - \sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p \right |=
\left |f(z_1) - \sum_{p=0}^n \frac{f^{(p)}(0)}{p!} z_1^p \right |\leq
C_{K,n} \left |z_1\right |^{n+1}.$$

Next, if $z_2 \neq 0$ and $\left |z_1 - z_2\right |\leq \rho \left |z_2 \right |$, then the closed interval $[z_1,z_2]$ is contained in $K_1$, so that: $$\left |f(z_1) - \sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p \right |\leq
M'_{K_1,n} \left |z_1-z_2\right |^{n+1}.$$

It remains to deal with the case (c), that is, when $z_2 \neq 0$ and $\left |z_1 -z_2\right |> \rho \left |z_2 \right |$. If we set: $$\lambda_{K,n} :=
\sup_{z\in K \atop p=0,\ldots,n} \left |\frac{g^{(p)}(z)}{p!}\right |~,
\quad
\mu_K := \sup_{z\in K} \left |z \right |,$$ then, for any integer $p \in [0,n]$, we find: $$\left |\frac{ f^{(p)}(z_2)}{p!} \right |=
\left |\frac{(z^{n+1}g)^{(p)}(z_2)}{p!} \right |\leq
\lambda_{K,n}~\sum_{k=0}^p \binom{n+1}{k} \left |z_2 \right |^{n+1-k} \leq
\tilde{\lambda}_{K,n}~ \left |z_2 - z_1\right |^{n+1-p},$$ where: $$\tilde{\lambda}_{K,n} :=
\lambda_{K,n}~\rho^{p-n-1}~\sum_{k=0}^p\binom {n+1}k \mu_K^{p-k}~.$$ From this, it follows: $$\begin{aligned}
\left |f(z_1) - \sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p\right |
\leq& ~
\left |z_1^{n+1} g(z_1) \right |+
(n+1) \tilde{\lambda}_{K,n}~ \left |z_2-z_1\right |^{n+1} \\
\leq&
\left(\left(1+\frac{1}{\rho}~\right)^{n+1}~
\lambda_{K,n} +
(n+1) \tilde{\lambda}_{K,n}\right)~\vert z_2-z_1\vert^{n+1}~.
\end{aligned}$$

To summarize, in the three cases cases we have: $$\left |f(z_1) -\sum_{p=0}^n \frac{f^{(p)}(z_2)}{p!} (z_1-z_2)^p  \right |\leq ~
C_{K,n} \left |z_1-z_2 \right |^{n+1},$$ where $$C_{K,n} :=
\max \left(M'_{K_1,n},
\left(1 + \frac{1}{\rho}~\right)^{n+1}~\lambda_{K,n} +
(n+1) \tilde{\lambda}_{K,n}
\right)~.$$

\(iii\) The result follows immediately from (ii). ◻
:::

Before stating the next proposition, we first recall Whitney conditions and Whitney theorem [@Ma1 chap. I, §4], [@Ma2]. We give them here in the case of dimension $2$. Let $f$ be a function of $(x,y)$ with complex values, $\mathcal{C}^{\infty}$ in an open neighborhood $U'$ of some compact subset $K'$ of ${\mathbf C}$. (We keep the letters $U$ and $K$ to denote respectively a $\Sigma$-invariant open subset of ${\mathbf C}$ and an invariant strict subset of $U$.) We shall use the following standard conventions; for $k := (k_1,k_2) \in {\mathbf N}^2$, we set: $$f^{(k)} := \dfrac{\partial^{k_1}}{\partial x^{k_1}}
\dfrac{\partial^{k_2}}{\partial y^{k_2}} \,f \cdot$$ We also write $k ! := k_1 ! k_2 !$, $(x,y)^k := x^{k_1} y^{k_2}$, $\left |k \right |:= k_1 + k_2$, etc. We associate to $f$ the family $(f^{(k)})_{k \in {\mathbf N}^2}$ of its "Taylor fields\" *restricted to $K'$*.\
We agree to identify the $\mathcal{C}^{\infty}$ function $f$ on $U' \supset K'$ with the $\mathcal{C}^{\infty}$ function $g$ on $V' \supset K'$ if their associated families $(f^{(k)})_{k \in {\mathbf N}^2}$, $(g^{(k)})_{k \in {\mathbf N}^2}$ are equal. Such a class of functions is called a *$\mathcal{C}^{\infty}$ function in the Whitney sense* on $K'$. []{#not45 label="not45"} We write $\mathcal{C}^{\infty}_{Whitney}(K')$ the space of $\mathcal{C}^{\infty}$ functions[^1] in the Whitney sense on $K'$. As is customary when dealing with germs, we sometimes write $f$ the class of $f$; likewise, we write $(f^{(k)})$ the family of restrictions to $K'$ of the derivatives $f^{(k)}$: by definition, they depend only on the class of $f$.\
So let $f$ be a $\mathcal{C}^{\infty}$ function in the Whitney sense on $K'$. The functions $f^{(k)}$ are continuous on $K'$ and for all $n \in {\mathbf N}$, the family $\bigl(f^{(k)}\bigr)$ (restricted to $K'$) satisfies the following conditions, that are called *Whitney conditions of order $n \in {\mathbf N}$* []{#not46 label="not46"} and that we shall denote $W_n(K')$: $$\lim~\dfrac{
\left(f^{(k)}(x_1,y_1) -
\sum_{\left |h \right |\leq n} \frac{f^{(k+h)}(x_2,y_2)}{h!}
(x_1 - x_2,y_1 - y_2)^h \right)
}
{\left |\!|(x_1-x_2,y_1 - y_2) \right |\!|^{n - \left |k\right |}}
 = 0,$$ where the limit is taken for $(x_1,y_1) \to (x_0,y_0) \in K'$, $(x_2,y_2) \to (x_0,y_0) \in K'$, with $(x_1,y_1),(x_2,y_2) \in K'$ and $(x_1,y_1) \neq (x_2,y_2)$.\
Conversely a family $\bigl(f^{(k)}\bigr)_{k\in{\mathbf N}^2}$ of continuous functions on $K'$ is the family of Taylor jets of an element of $\mathcal{C}^{\infty}_{Whitney}(K')$ if and only if it satisfies Whitney conditions $W_n(K')$ for all $n \in {\mathbf N}$ (this is Whitney's theorem, see [@Ma1; @Ma2]). Note that, with the usual identification of ${\mathbf C}$ with ${\mathbf R}^2$, setting $z := x + {\text{i}}y$ and using $\frac{\partial}{\partial z}$, $\frac{\partial}{\partial \bar z}$ instead of $\frac{\partial}{\partial x}$, $\frac{\partial}{\partial y}$, for all $n \in {\mathbf N}$ we can replace Whitney conditions $W_n(K')$ []{#not47 label="not47"} by equivalent conditions $\tilde W_n(K')$, that we do not state more explicitly here. In our case of interest (functions satisfying the Cauchy-Riemann equation $\partial f/\partial \overline{z} = 0$), they take the form of condition (iii) of the lemma above.

::: prop
[]{#prop:asymptotiqueetWhitney label="prop:asymptotiqueetWhitney"} Let $U$ be a $\Sigma$-invariant open set of ${\mathbf C}$. Then, $f \in {\mathscr{A}}(U_{\infty})$ if, and only if, for every invariant strict subset $K \subset U$, one has: $$f_{\vert K}\in \text{Ker~}~ \left(\frac{\partial}{\partial \bar z}:
\mathcal{C}^{\infty}_{Whitney} \bigl({K\cup\{ 0\}},{\mathbf C}\bigr)
\rightarrow \mathcal{C}^{\infty}_{Whitney}\bigl({K\cup\{ 0\}},{\mathbf C}\bigr)\right).$$
:::

::: proof
*Proof.* Let $f\in \mathcal{C}^{\infty}_{Whitney}\bigl({K\cup\{ 0\}},{\mathbf C}\bigr)$. If for all invariant strict subset $K\subset U$, one has: $$f_{\vert K}\in \text{Ker~}~
\left(\frac{\partial}{\partial \bar z}:
\mathcal{C}^{\infty}_{Whitney}\bigl({K\cup\{ 0\}},{\mathbf C}\bigr)
\rightarrow
\mathcal{C}^{\infty}_{Whitney}\bigl({K\cup\{ 0\}},{\mathbf C}\bigr)\right),$$ then, the function $f$ is holomorphic on $V$, its Taylor jet $\hat f$ at $0$ is formally holomorphic (*i.e.* it satisfies the Cauchy-Riemann equation), $\hat f = \sum\limits_{n\geq 0} a_n z^n$ and $f$ is asymptotic to $\hat f$ on $V$, $f\in{\mathscr{A}}(U_{\infty})$.

Conversely let $f\in {\mathscr{A}}(U_{\infty})$; then, for all $p\in{\mathbf N}$, $f^{(p)} \in {\mathscr{A}}(U_{\infty})$ and for all $r \in {\mathbf N}^*$, we have $\frac{\partial^r}{\partial \bar {z}^r}f^{(p)}=0$.

We can apply lemma [\[lemm:ascle\]](#lemm:ascle){reference-type="ref" reference="lemm:ascle"} to each function $f^{(p)}$, $p\in{\mathbf N}$, to the effect that $f$ satisfies conditions $\tilde W_n(K)$ for all $n\in{\mathbf N}$ (this is assertion (iii) of the lemma); therefore it satisfies also Whitney conditions $W_n(K)$ for all $n\in{\mathbf N}$ and, using Whitney theorem, we get $f\in\mathcal{C}^{\infty}_{Whitney}\bigl({K\cup\{ 0\}},{\mathbf C}\bigr)$. ◻
:::

## Asymptotics and sheaves on ${\mathbf{E}_{q}}$ {#subsubsection:asymptoticsandsheaves}

Recall from paragraph [\[subsection:qAsymptotics\]](#subsection:qAsymptotics){reference-type="ref" reference="subsection:qAsymptotics"} the definition of the sheaves ${\mathscr{A}}$ and ${\mathscr{A}}_{0}$ on ${\mathbf{E}_{q}}$. There is a natural map from ${\mathscr{A}}$ to the constant sheaf ${{\mathbf C}[[z]]}$ sending a function to its asymptotic expansion. Although much weaker than the $q$-Gevrey theorem of Borel-Ritt [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"}, the following result does not directly flow from it, and we give here a direct proof.

::: theo
[]{#theo:BorelRittfaible label="theo:BorelRittfaible"} The natural map from the sheaf ${\mathscr{A}}$ to the constant sheaf ${{\mathbf C}[[z]]}$ is onto.
:::

::: proof
*Proof.* Starting from an open set $V \subset {\mathbf{E}_{q}}$ small enough that $U := p^{-1}(V) \subset {\mathbf C}^{*}$ is a disjoint union of open sets $U_{n} := q^{n} U_{0}$, where $U_{0}$ is mapped homeomorphically to $V$ by $p$, we divide ${\mathbf C}^{*}$ in a finite number of sectors $S_{i}$ such that each $U_{n}$ is contained in one of the $S_{i}$. Now, let $\hat{f} \in {{\mathbf C}[[z]]}$. Apply the classical Borel-Ritt theorem [@HS chap. XI, §1] within each sector $S_{i}$, yielding a map $f_{i}$ holomorphic and admitting the asymptotic expansion $\hat{f}$. Glueing the $f_{i}$ provides a section of ${\mathscr{A}}$ over $V$ having image $\hat{f}$. ◻
:::

[^1]: They are not really functions, but it usually causes no problem; moreover, in our case, they will be (according to the next proposition).
