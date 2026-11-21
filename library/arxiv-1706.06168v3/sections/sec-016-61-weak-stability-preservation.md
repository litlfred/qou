---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-016-61-weak-stability-preservation
section_title: "Weak Stability Preservation"
section_number: 6.1
pages: 18-19
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.974
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
Borcea and Brändén define the following symbol: $$\mathop{\mathrm{Symb}}_{BB}(T) := T[(x+z)^\lambda] = \sum_{\mu \leq \lambda} \binom{\lambda}{\mu} z^{\lambda-\mu} T(x^\mu)$$ They then obtain the following characterization of stability-preserving linear operators.

::: BB_Cops_thm
**Theorem [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} 1** (Borcea-Brändén). *Fix $\lambda \in \mathbb{N}_0^m$ and any linear operator $T: \mathbb{C}^\lambda[x_1,\ldots,x_m] \to \mathbb{C}[x_1,\ldots,x_m]$. The following are equivalent.*

1.  *$T$ maps $\mathcal{H}_+^m$-stable polynomials to weakly $\mathcal{H}_+^m$-stable polynomials.*

2.  *One of the following holds:*

    1.  *$\mathop{\mathrm{Symb}}_{BB}(T)$ is $\mathcal{H}_+^{2m}$-stable.*

    2.  *$T$ has image of dimension at most one, and is of the form $$T: p \mapsto q \cdot \psi(p)$$ where $q \in \mathbb{C}[x_1,\ldots,x_m]$ is $\mathcal{H}_+^m$-stable, and $\psi$ is some linear functional.*
:::

Using our terminology, this is a characterization of weak stability-preserving linear operators. This fantastic result perhaps has but one unfortunate piece: the degeneracy condition $(ii)(b)$. Its necessity is demonstrated in the following.

::: example
Define $T: \mathbb{C}^n[x] \to \mathbb{C}[x]$ via: $$T: \sum_{k=0}^n \binom{n}{k} a_k x^k \mapsto (a_n + a_{n-2}) x^n$$ This operator obviously preserves weak $\mathcal{H}_+$-stability. We then have that $\mathop{\mathrm{Symb}}_{BB}(T) = (z^2 + 1)x^n$, which is not $\mathcal{H}_+^2$-stable.
:::

As we will see below, this condition can be removed once we only consider strong stability-preserving operators. So then, maybe strong stability is the more natural notion? However "natural" it is, unfortunately it leaves out operators one might wish to consider. The most fundamental of such operators is the derivative operator $\partial_x$. While $\partial_x$ preserves strong $\overline{\mathcal{H}_+}$-stability, it only preserves weak $\mathcal{H}_+$-stability. Specifically, $1 \in \mathbb{C}^n[x]$ is $\mathcal{H}_+$-stable (all its roots are at $\infty$), but $\partial_x 1 \equiv 0$. With this, one obviously wants to be able to include weak stability preserving operators in any characterization of $\mathcal{H}_+$-stability preserving operators. We discuss how to use our strong stability preservation characterization to deal with operators like $\partial_x$ in Example [\[deriv_ex\]](#deriv_ex){reference-type="ref" reference="deriv_ex"}.
