---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-006-32-construction-of-n-cocycles
section_title: "Construction of n-cocycles."
section_number: 3.2
pages: 8-9
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.875
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an analysis of quantum Markov semi-groups."
---
The following proposition allows to construct cocycles at the expense of changing the bimodule. We will remedy this change by using Schatten-$\mathcal{S}_p$ properties below.

::: thm
[]{#Thm=Gdelta label="Thm=Gdelta"} Let $H$ be an $A$-$A$-bimodule and let $f\colon \mathcal{A}^{\otimes (n-1)} \rightarrow H$ be a linear map. Set $Gf\colon \mathcal{A}^{\otimes n} \rightarrow H_\nabla$ by, $$(G f)(a_1 \otimes \ldots \otimes a_{n}) := a_1 \otimes_\nabla f(a_2 \otimes \ldots \otimes a_{n}) \in H_\nabla.$$ Then $Gd + dG=0$, where $d$'s are the differentials of the appropriate cochain complexes. In particular, $G$ maps cocycles to cocycles and coboundaries to coboundaries, so it induces a map on the level of cohomology $G_{\ast}\colon H^{n}(\mathcal{A}, H) \to H^{n+1}(\mathcal{A}, H_{\nabla})$.
:::

::: proof
*Proof.* Let us first compute $G(df)$. We have $$\begin{aligned}
df(a_1\otimes \dots\otimes a_n) &= a_1 f(a_2\otimes \dots\otimes a_n) + \sum_{k=1}^{n-1} (-1)^{k} f(a_1\otimes \dots \otimes a_k a_{k+1}\otimes \dots \otimes a_n)  \\
&+ (-1)^n f(a_1\otimes\dots\otimes a_{n-1})a_n,
\end{aligned}$$ hence $$\begin{aligned}
G(df)(a_0\otimes\dots\otimes a_n) &= a_0\otimes_{\nabla} a_1 f(a_2\otimes \dots\otimes a_n) + \sum_{k=1}^{n-1} (-1)^k a_0\otimes_{\nabla} f(a_1\otimes\dots\otimes a_k a_{k+1}\otimes\dots\otimes a_n) \\
&+(-1)^n a_0\otimes_{\nabla} f(a_1\otimes\dots\otimes a_{n-1})a_n.
\end{aligned}$$ On the other hand: $$\begin{aligned}
-d(Gf)(a_0\otimes\dots\otimes a_n)&=-a_0(a_1\otimes_{\nabla} f(a_2\otimes\dots\otimes a_n))+a_0a_1\otimes_{\nabla} f(a_2\otimes\dots\otimes a_n) \\
&+ \sum_{k=1}^{n-1} (-1)^{k} a_{0}\otimes_{\nabla} f(a_1\otimes\dots\otimes a_k a_{k+1}\otimes\dots\otimes a_n) \\
&+ (-1)^n a_{0}\otimes_{\nabla} f(a_1\otimes\dots\otimes a_{n-1}) a_n.
\end{aligned}$$ Note that $$-a_0(a_1\otimes_{\nabla} f(a_2\otimes\dots\otimes a_n)) = -a_0 a_1 \otimes_{\nabla} f(a_2\otimes\dots\otimes a_n) + a_0\otimes_{\nabla} a_1 f(a_2\otimes \dots\otimes a_n).$$ It follows that $G(df) = -d(Gf)$, i.e. $dG+Gd=0$. ◻
:::

::: cor
[]{#Cor=Derivation label="Cor=Derivation"} The map, $$\partial_n: \mathcal{A}^{\otimes n} \rightarrow L_2(M)_{\nabla^{(n)}}: a_1 \otimes \ldots \otimes a_n \mapsto a_1 \otimes_\nabla\ldots \otimes_\nabla a_n \otimes_\nabla\Omega_\tau.$$ defines an $n$-cocycle, i.e. an element in $C^n(\mathcal{A}, L_2(M)_{\nabla^{(n)}})$.
:::

::: proof
*Proof.* For $n=1$ we get $\partial_1(ab) = ab \otimes_\nabla\Omega_\tau = a \cdot (b \otimes_\nabla\Omega_\tau) +
 (a \otimes_\nabla\Omega_\tau) \cdot b = a \partial_1(b) + \partial_1(a) b$ and so the corollary follows. For higher $n$ use Theorem [\[Thm=Gdelta\]](#Thm=Gdelta){reference-type="ref" reference="Thm=Gdelta"} inductively. ◻
:::
