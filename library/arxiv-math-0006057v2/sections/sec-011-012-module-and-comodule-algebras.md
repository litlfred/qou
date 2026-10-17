---
doc_id: arxiv-math-0006057v2
doc_title: "arXiv:math/0006057v2 [math.QA] 10 Jun 2000"
section_id: sec-011-012-module-and-comodule-algebras
section_title: "Module and comodule algebras"
section_number: 0.12
pages: 13-14
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 0.585
---
::: definition
[]{#module algebra label="module algebra"} An algebra $A$ is a (left) *$H$-module algebra* if $A$ is a left $H$-module via $h\otimes a \to h\cdot a$ and

1.  $h\cdot ab = (h_{(1)} \cdot a)(h_{(2)} \cdot b)$,

2.  $h\cdot 1 = \varepsilon_t(h)\cdot 1$.
:::

If $A$ is an $H$-module algebra we will also say that $H$ acts on $A$.

::: definition
[]{#comodule algebra label="comodule algebra"} An algebra $A$ is a (right) *$H$-comodule algebra* if $A$ is a right $H$-module via $\rho: a \to a^{(0)} \otimes a^{(1)}$ and

1.  $\rho(ab) = a^{(0)} b^{(0)} \otimes a^{(1)} b^{(1)}$,

2.  $\rho(1) = (\mbox{id}\otimes\varepsilon_t)\rho(1)$.
:::

It follows immediately that $A$ is a left $H$-module algebra if and only if $A$ is a right $\widehat H$-comodule algebra.

::: example
[]{#examples of actions label="examples of actions"}

1.  The target counital subalgebra $H_t$ is a trivial $H$-module algebra via $h\cdot z = \varepsilon_t(hz)$, $h\in H,\,z\in H_t$.

2.  $H$ is an $\widehat H$-module algebra via the dual action $\phi\rightharpoonup h = h_{(1)} \langle\,\phi,\,h_{(2)}\,\rangle$, $\phi\in \widehat H,\,h\in H$.

3.  Let $A = C_H(H_s) =\{ a\in H \mid ay=ya \quad\forall y\in H_s\}$, be the centralizer of $H_s$ in $H$, then $A$ is an $H$-module algebra via the adjoint action $h\cdot a = h_{(1)} a S(h_{(2)})$.
:::
