---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-002-12-linear-equations-in-a-multiplicative-group
section_title: "Linear equations in a multiplicative group"
section_number: 1.2
pages: 3-3
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
Another application of our construction is to provide new lower bounds for the number of solutions to linear equations in a multiplicative group.

::: theorem
[]{#th-linearmain label="th-linearmain"} There is an absolute constant $C>1$ such that the following holds. Let $k\geq C$ be any integer. There exist infinitely many $d\geq 2$ and multiplicative groups $\Gamma\leq\mathbb{R}^\times$ of rank $\leq d$ such that there are at least $$\geq (Ck)^{kd}$$ solutions to $$x_1+\cdots+x_k=1$$ with $x_i\in \Gamma$ and $x_i>0$ for $1\leq i\leq k$.
:::

In particular this shows that the dependence on $d$ in the corresponding upper bound of Evertse, Schlickewei, and Schmidt [@ESS02] is the best possible (for subgroups of $\mathbb{R}^\times$). Similarly, we produce a new lower bound for the number of solutions to the unit equation $x_1+\cdots+x_k=1$ with $x_i\in \mathcal{O}_K^\times$, provided $k$ is sufficiently large (in absolute terms).

::: theorem
[]{#th-unitlower label="th-unitlower"} There exists an integer $k\geq 2$ and an absolute constant $C>1$ such that, for infinitely many $d$, there exists a number field $K$ of degree $d$ such that the equation $$x_1+\cdots+x_k=1$$ has at least $C^d$ many solutions with $x_i\in \mathcal{O}_K^\times$.
:::

By contrast, when $k=2$ this equation is conjectured to have sub-exponential in $d$ many solutions. For more details, and further discussion of related results, see Section [\[sec-linear\]](#sec-linear){reference-type="ref" reference="sec-linear"}.
