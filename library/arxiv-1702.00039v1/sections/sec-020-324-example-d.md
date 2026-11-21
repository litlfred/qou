---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-020-324-example-d
section_title: "Example D"
section_number: 3.2.4
pages: 17-18
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.852
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Kazhdan-Lusztig polynomials were discovered (or invented) in 1979, but it was only in 1990 that Matthew Dyer gave a formula [@Dy] to calculate inductively the Kazhdan-Lusztig basis for a Universal Coxeter system (we will not reproduce here the proof, although it is not a difficult one). In this case, every element has only one expression as a product of elements of $S$.

::: thm
[]{#Dy label="Dy"} Let $x\in U_n$ and $x=rs\cdots$ with $r,s, \ldots \in S.$ Then we have the following recursive formula $$\begin{aligned}
\label{universal}
b_rb_x  & = & (v+v^{-1})b_x \nonumber\\ 
b_tb_x&=&b_{tx}\hspace{1.7cm} \mathrm{if} \ t\neq r,s \nonumber \\
b_sb_x &=&b_{sx}+b_{rx}\ \hspace{.6cm}  \mathrm{if}\ \ s\neq r 
\end{aligned}$$
:::

Our baby examples A and B are particular cases of example C (the case of dihedral groups). We just saw in equation ([\[good\]](#good){reference-type="ref" reference="good"}) that Dyer's Formula is also true for Dihedral groups (the first case of the formula comes from the fact $b_sb_s=(v+v^{-1})b_s$ and the second case never appears in Dihedral groups). In fact the same proof works for the infinite Dihedral group as we said in Remark [\[univ\]](#univ){reference-type="ref" reference="univ"}. So the whole point of this theorem is that the calculation of the Kazhdan Lusztig basis in this case is local in nature, i.e. different strings of alternating simple reflections "don't intersect each other" in the following sense.

Let $x=\cdots psps$ be an alternating sequence of simple reflections ending by $s$, and $y=srsrs\cdots$ an alternating sequence of simple reflections starting by $s$. Then we use the following notation $$b_x\ast b_y:= \frac{b_xb_y}{(v+v^{-1})}$$ It is an exercice to prove that $b_x\ast b_y\in \mathcal H$ (hint: $b_x$ is divisible on the right and $b_y$ is divisible on the left by $b_s$). Consider the element $$x:={\color{red}s}{\color{blue}r}{\color{red}s}{\color{blue}r}{\color{red}s}{\color{blue}r}{\color{orange} p}{\color{blue}r}{\color{orange} p}{\color{blue}r}{\color{teal} u}{\color{olive}q}{\color{darkgray} t}{\color{olive}q} {\color{blue}r}{\color{olive}q}{\color{blue}r}{\color{olive}q}{\color{blue}r}{\color{olive}q}.$$ As we said, the calculation is local, we have $$b_x=b_{{\color{red}s}{\color{blue}r}{\color{red}s}{\color{blue}r}{\color{red}s}{\color{blue}r}}\ast b_{{\color{blue}r}{\color{orange} p}{\color{blue}r}{\color{orange} p}{\color{blue}r}}\ast b_{{\color{blue}r}{\color{teal} u}}\ast b_{{\color{teal} u}{\color{olive}q}} \ast b_{{\color{olive}q}{\color{darkgray} t}{\color{olive}q}}\ast b_{{\color{olive}q}{\color{blue}r}{\color{olive}q}{\color{blue}r}{\color{olive}q}{\color{blue}r}{\color{olive}q}}.$$

With Dyer's Formula in hand we could have done all the calculations we did in the other examples with no effort. We apply it three times and we obtain

-   $b_{sr}=b_sb_r$

-   $b_{sr}b_s=b_{srs}+b_s \longrightarrow b_{srs}=b_{s}b_rb_s-b_s$

-   $b_{srs}b_r=b_{srsr}+b_{sr} \longrightarrow  b_{srsr}=b_sb_rb_sb_r-2b_sb_r$

Aha!
