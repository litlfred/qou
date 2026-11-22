---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-007-22-homogeneous-spaces
section_title: "Homogeneous spaces"
section_number: 2.2
pages: 5-6
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.985
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We now recall some basic definitions and facts about homogeneous spaces. Throughout this article, we will use double brackets $\llbracket x\rrbracket$ to denote the equivalence class of $x$.

::: definition
Let $G$ be a Lie group acting on a smooth manifold $M$ via $\varphi: G\times M \to M$. If the action $\varphi$ is smooth and transitive, i.e., for any $x,y\in M$, there is some $a\in G$ such that $\varphi(a,x) = y$, then $M$ is called a *homogeneous space* of the Lie group $G$.
:::

For a point $x\in M$, the subgroup $G_x =\{a\in G: \varphi(a,x) = x\}$ is called the *isotropy group* of $x$. We write $G/G_x$ for the quotient group of $G$ by $G_x$ and denote by $\llbracket a \rrbracket\in G/G_x$ the *coset* (or equivalence class) of $a\in G$. Since $G$ acts on $M$ transitively, we see that there is a one-to-one correspondence $F$ between $G/G_{x}$ and $M$ given by $$F: G/G_x \to M,\quad F(\llbracket a\rrbracket) = \varphi(a,x),$$ for any $x\in M$. In fact, $F$ defines a diffeomorphism between the two smooth manifolds, which is the content of the following theorem [@Boothby1975 Theorems 9.2 and 9.3].

::: theorem
[]{#thm:homogeneous structure label="thm:homogeneous structure"} Let $G$ be a Lie group acting on a smooth manifold $M$. For any $x \in M$, there exists a unique smooth structure on $G/G_x$ such that the action $$\psi: G \times G/G_x \to G, \quad \psi(a, \llbracket a' \rrbracket) = \llbracket aa' \rrbracket$$ is smooth. Moreover, the map $F: G/G_x \to M$ sending $\llbracket a \rrbracket$ to $\varphi(a,x)$ is a $G$-equivariant diffeomorphism, i.e., $F$ is a diffeomorphism such that $F\bigl(\psi(a, \llbracket a' \rrbracket)\bigr) = \varphi \bigl(a, F(\llbracket a' \rrbracket)\bigr)$.
:::

The Grassmannian $\mathop{\mathrm{Gr}}(k,n)$ of $k$-dimensional subspaces in $\mathbb{R}^n$ is probably the best known example of a homogeneous space in manifold optimization. Indeed, $\mathop{\mathrm{O}}(n)$ acts transitively on $\mathop{\mathrm{Gr}}(k,n)$ and as any $k$-dimensional subspace $\mathbb{W} \subseteq \mathbb{R}^n$ has isotropy group isomorphic to $\mathop{\mathrm{O}}(k)\times \mathop{\mathrm{O}}(n-k)$, we obtain the well-known characterization of Grassmannian $$\mathop{\mathrm{Gr}}(k,n) \cong \mathop{\mathrm{O}}(n)/\bigl(\mathop{\mathrm{O}}(k)\times \mathop{\mathrm{O}}(n-k)\bigr)$$ that is crucial for manifold optimization. Throughout this article '$\cong$' will mean diffeomorphism.

Let $G$ be a Lie group and $M$ a homogeneous space of $G$ with action $\varphi: G\times M \to M$. Fix any $x\in M$ and let $H$ denote its isotropy group. By Theorem [\[thm:homogeneous structure\]](#thm:homogeneous structure){reference-type="ref" reference="thm:homogeneous structure"} we may identify $M$ with $G/H$. The left translation map in Section [\[sec:Lie\]](#sec:Lie){reference-type="ref" reference="sec:Lie"} may be extended to this setting as $L_a : M \to M$, $L_a(y) =\varphi(a,y)$ for any $a \in G$. In particular, if $a\in H$, then $L_a(x) = x$, and we have a linear isomorphism $$(dL_a)_x : T_xM \to T_xM.$$ Let $g: M \to T^\ast M \otimes T^\ast M$ be a Riemannian metric on $M$. We say that $g$ is $G$-*invariant* if for every $y\in M$ and $a\in G$, we have $$g_{L_a(y)}\bigl((dL_a)_y(X), (dL_a)_y(Y)\bigr) = g_y (X,Y) \quad \text{for all }  X,Y\in T_yM.$$

As $M  = G/H$, we have $T_{\llbracket e \rrbracket} M  = \mathfrak{g}/\mathfrak{h}$ where $\mathfrak{g}$ and $\mathfrak{h}$ are the Lie algebras of $G$ and $H$ respectively. Here $e\in G$ is the identity element. This allows us to define the *adjoint representation* $\mathop{\mathrm{Ad}}_H: H \to \mathop{\mathrm{GL}}(\mathfrak{g}/\mathfrak{h})$, $a \mapsto d(L_a \circ R_{a^{-1}})_{\llbracket e \rrbracket}$. In other words, for any $a \in H$ and $X\in \mathfrak{g}/\mathfrak{h}$, $$\mathop{\mathrm{Ad}}_H (a) (X) = d (L_a\circ R_{a^{-1}} )_{\llbracket e \rrbracket}(X).$$ An inner product $\eta$ on the vector space $\mathfrak{g}/\mathfrak{h}$ is said to be *$\mathop{\mathrm{Ad}}_H$-invariant* if for every $a\in H$, $$\eta (\mathop{\mathrm{Ad}}_H(a)(X),\mathop{\mathrm{Ad}}_H(a)(Y)) = \eta (X,Y) \quad \text{for all } X,Y\in \mathfrak{g}/\mathfrak{h}.$$

We state an important result about their existence and construction [@CE2008 Proposition 3.16].

::: proposition
[]{#prop:metric inner product correspondence label="prop:metric inner product correspondence"} Let $G$ be a connected Lie group and $H$ a closed Lie subgroup with Lie algebras $\mathfrak{g}$ and $\mathfrak{h}$ respectively. If there is a subspace $\mathfrak{m}$ of $\mathfrak{g}$ such that $\mathfrak{g} = \mathfrak{m} \oplus \mathfrak{h}$ and $\mathop{\mathrm{Ad}}_H (\mathfrak{m}) \subseteq \mathfrak{m}$, then there is a one-to-one correspondence between $G$-invariant metrics on $M = G/H$ and $\mathop{\mathrm{Ad}}_H$-invariant inner products on $\mathfrak{m}$.
:::

Proposition [\[prop:metric inner product correspondence\]](#prop:metric inner product correspondence){reference-type="ref" reference="prop:metric inner product correspondence"} says that if $\mathfrak{h}\subseteq \mathfrak{g}$ admits a complement $\mathfrak{m}$, then we may obtain a $G$-invariant metric $g$ on $M$ by an $\mathop{\mathrm{Ad}}_H$-invariant inner product on $\mathfrak{m}$. Moreover, we may identify $T_xM$ with $\mathfrak{m}$, implying that the metric $g$ on $M$ is essentially determined by $g_x$ at a single arbitrary point $x \in M$.

If in addition $G$ is simple and compact, then $G$ admits the unique bi-invariant metric called the *canonical metric* on $M$ and $(M,g)$ is called a *normal homogeneous space*.

::: proposition
[]{#prop:nhs label="prop:nhs"} If $G$ is a compact Lie group, then $G$ admits a bi-invariant metric and this metric induces a $G$-invariant metric $g$ on $M = G/H$ for any closed subgroup $H\subseteq G$.
:::
