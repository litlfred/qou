---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-066-86-examples
section_title: "Examples"
section_number: 8.6
pages: 64-66
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.872
latex_coverage_ratio: 0.796
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sec:exprojectors label="sec:exprojectors"}

In this subsection, we use the local geometry of the flag Hilbert scheme to describe the homology of categorified projectors on two and three strands.

::: example
For the $S^2$ projector, we have $$Y=\left(\begin{matrix}
0 & 0\\
1 & 0\\
\end{matrix}\right).$$ The commutation relation implies that $X$ is of the form $$X=\left(\begin{matrix}
u_1 & 0\\
u_2 & u_1\\
\end{matrix}\right).$$ One has $\deg(u_1)=q$, $\deg(u_2)=q/t$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{1}{(1-q)(1-q/t)}.$$
:::

::: example
For the $\Lambda^2$ projector, we have $$X=\left(\begin{matrix}
x_1 & 0\\
1 & x_2\\
\end{matrix}\right),
Y=\left(\begin{matrix}
0 & 0\\
y_{21} & 0\\
\end{matrix}\right),$$ and the commutation relation $(x_1-x_2)y_{21}=0$. One has $\deg(x_1)=\deg(x_2)=q$, $\deg(y_{21})=t/q$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{1-t}{(1-q)^2(1-t/q)}=\frac{1}{(1-q)^2}+\frac{t/q}{(1-q)(1-t/q)}.$$
:::

::: example
[]{#ex:Sym n label="ex:Sym n"} For the $S^3$ projector, we have $$X=\left(\begin{matrix}
x_1 & 0 & 0\\
x_2 & x_1 & 0\\
x_3 & x_2 & x_1\\
\end{matrix}\right),
Y=\left(\begin{matrix}
0 & 0 & 0\\
1 & 0 & 0\\
0 & 1 & 0\\
\end{matrix}\right),$$ One has $\deg(x_1)=q$, $\deg(x_2)=q/t$, $\deg x_3=q/t^2$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{1}{(1-q)(1-q/t)(1-q/t^2)}.$$ More generally, for the $S^n$ projector, we have $$P(\mathring{\mathcal{A}}_T)=\prod_{i=1}^n{(1-qt^{1-i})^{-1}}.$$
:::

::: example
[]{#ex:Lambda n label="ex:Lambda n"} For the $\Lambda^3$ projector, we have $$X=\left(\begin{matrix}
x_1 & 0 & 0\\
1   & x_2 & 0\\
0 & 1 & x_3\\
\end{matrix}\right),
Y=\left(\begin{matrix}
0 & 0 & 0\\
y_{21} & 0 & 0\\
y_{31} & y_{32} & 0\\
\end{matrix}\right),$$ and the commutation relations $(x_1-x_2)y_{21}=(x_2-x_3)y_{32}=0$ and $$y_{21}-y_{32}=(x_{1}-x_{3})y_{31}.$$ Note that one can eliminate $y_{32}$ using the last equation. One has $\deg(x_1)=\deg(x_2)=\deg(x_3)=q$, $\deg(y_{21})=\deg(y_{32})=t/q$, $\deg(y_{31})=t/q^2$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{(1-t)^2}{(1-q)^3(1-q/t)(1-q/t^2)}.$$

More generally, for the $\Lambda^n$ projector, we have $$\mathring{\mathcal{A}}_T= \frac {\mathbb{C}[x_1,\ldots,x_n, y_{i,j}]_{i>j}}{y_{i,j}(x_i-x_j) - (y_{i-1,j} - y_{i,j+1})}$$ and $$P(\mathring{\mathcal{A}}_T)=\frac{(1-t)^{n-1}}{(1-q)^n}\prod_{i=1}^{n-1}(1-qt^{-i})^{-1}.$$ (which can also be seen directly from Proposition [\[prop:poincare\]](#prop:poincare){reference-type="ref" reference="prop:poincare"}.)
:::

::: example
For the hook-shaped projector with $(z_1,z_2,z_3)=(1,t,q)$, we have $$X=\left(\begin{matrix}
x_1 & 0 & 0\\
x_{21}   & x_1 & 0\\
1 & x_{32} & x_3\\
\end{matrix}\right),
Y=\left(\begin{matrix}
0 & 0 & 0\\
1 & 0 & 0\\
0 & y_{32} & 0\\
\end{matrix}\right),$$ with commutation relations $$x_{32}=x_{21}y_{32},\ (x_1-x_3)y_{32}=0,$$ In this case $\deg(x_1)=\deg(x_3)=q$, $\deg(x_{21})=q/t$, $\deg(x_{32})=t$, $\deg(y_{32})=t^2/q$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{(1-t^2)}{(1-q)^2(1-q/t)(1-t^2/q)}.$$

For the other hook-shaped projector we have $(z_1,z_2,z_3)=(1,q,t)$, so $$X=\left(\begin{matrix}
x_1 & 0 & 0\\
1   & x_2 & 0\\
0 & x_{32} & x_3\\
\end{matrix}\right),
Y=\left(\begin{matrix}
0 & 0 & 0\\
y_{21} & 0 & 0\\
1 & y_{32} & 0\\
\end{matrix}\right),$$ with commutation relations $(x_1-x_2)y_{21}=(x_2-x_3)y_{32}=0$ and $$x_1-x_3+y_{32}=x_{32}y_{21}.$$ In this case $\deg(x_1)=\deg(x_2)=\deg(x_3)=q$, $\deg(x_{32})=q^2/t$, $\deg(y_{21})=t/q$, $\deg(y_{32})=q$, so the Poincaré series equals $$P(\mathring{\mathcal{A}}_T)=\frac{(1-t)(1-q^2)}{(1-q)^3(1-t/q)(1-q^2/t)}.$$
:::
