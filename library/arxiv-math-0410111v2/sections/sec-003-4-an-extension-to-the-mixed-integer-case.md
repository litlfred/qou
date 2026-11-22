---
doc_id: arxiv-math-0410111v2
doc_title: "Integer Polynomial Optimization in Fixed Dimension"
section_id: sec-003-4-an-extension-to-the-mixed-integer-case
section_title: "An extension to the mixed integer case"
section_number: 4
pages: 6-7
source_pdf: 0410111v2.pdf
source_sha256: 0ccaeeabd8de6b5f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.602
doc_brief: "Integer Polynomial Optimization in Fixed Dimension — 5 sections: Front matter; Introduction; Computational Complexity Bounds"
---
Now, we wish to discuss extensions of Theorem [\[main\]](#main){reference-type="ref" reference="main"} to the mixed integer scenario. If some of the variables are allowed to be continuous then we can describe the task as $$\hbox{maximize} \ f(x,y) \ \hbox{subject to} \ \{ (x,y) | Ax+By \leq
b, \ \hbox{with} \ x_i \in \mathbb Z\ \hbox{and} \ y_i \in \mathbb R\}.$$ Consider the sequence of integer polynomial optimization problems $\hbox{optimize} \ f(x,\frac{y}{n}) \ \hbox{subject to}\ (x,y) \in
\Gamma_n=\{ (x,y) | Ax+B(\frac{y}{n}) \leq b, \ \hbox{with} \ x_i \in
\mathbb Z\ \hbox{and} \ y_i \in \mathbb Z\},$ where each of the subproblems is equivalent to optimizing a polynomial over a "semi-dilated" polytope (in some coordinate directions but not others). As $n$ goes to infinity, the sequence of optimal solution values can have several limit points. Nevertheless, it is still possible to construct a subsequence of problems whose optimal values approximate the mixed integer optimum to arbitrary precision:

::: corollary
[]{#mip label="mip"} With the hypotheses of Theorem [\[main\]](#main){reference-type="ref" reference="main"}, we can construct a sequence of integer polynomial programming problems, over finer and finer grids, whose optimal values converge to the optimal value of the mixed integer program $$f^*=\hbox{maximize} \  f(x_1,x_2,\dots,x_d) \ \hbox{subject to} \ x \in P, \ \hbox{and} \ x_i \in \mathbb Z\
    \hbox{for} \ i \in I \subseteq  \{1,2,\dots,d\}.$$ By applying the algorithm of Theorem [\[main\]](#main){reference-type="ref" reference="main"} to the subproblems, we can approximate the optimum to arbitrary precision.
:::

When all variables are continuous, the original polytope $P$ is actually dilated uniformly in all directions by a parameter $n$, or equivalently, the integer grid is refined. Define $$r(q,n)=\sum_{\alpha \in (nP) \cap \mathbb Z^d} f^q(\alpha) z^\alpha,$$ for each power $q$ and dilation factor $n$. Note that for fixed $q$, then we can easily see that the sum $\sum_{\alpha \in (nP) \cap
  \mathbb Z^d} \frac{1}{n^d} f^q(\alpha) z^\alpha$ is essentially an approximation to the Riemann integral of $f^q$; thus $$\lim_{n \rightarrow \infty} r(q,n)/n^d = \int_P f^q(\bar{x})
d\bar{x}.$$ As $n,q$ grow, the values $\sqrt[q]{r(q,n)}$ approximate the sequence $\sqrt[q]{\int_P f^q(\bar{x}) d\bar{x}}$ which converges to $(\hbox{max}_{x \in P} f(x))\cdot \hbox{volume} (P)$. This is related to recent work (see [@deklerketal; @lasserre; @parrilosturmfels] and references therein) where the global optimum of a polynomial over a compact domain is investigated as the result of a grid refinement and properties of sums of squares.
