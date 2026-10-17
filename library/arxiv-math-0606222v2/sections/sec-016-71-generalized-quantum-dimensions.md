---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-016-71-generalized-quantum-dimensions
section_title: "Generalized quantum dimensions"
section_number: 7.1
pages: 30-32
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.875
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
We begin by giving an explicit expression for the generalized dimension $D_q(\lambda)$.

::: lem
[]{#explicitD label="explicitD"} We have $$D_q(\lambda)=a^{-|\lambda|}t^{-2(\rho,\lambda)}\prod_{i=1}^nv_i(\lambda_i;q)
\prod_{1\leq j<k\leq n}w_{j,k}^+(\lambda_j+\lambda_k;q)w_{j,k}^-(\lambda_j-\lambda_k;q),\qquad \lambda\in\Lambda_n,$$ where $v_i(m;q)$, $w_{j,k}^{\pm}(m;q)$ for $m\in\mathbb{Z}_+$ are given by $$\begin{split}
v_i(m;q)&=\frac{\bigl(at^{n-i}, q^{-1}abt^{n-i};q\bigr)_m}
{\bigl(qt^{n-i},bt^{n-i};q\bigr)_m}\frac{(1-q^{2m-1}abt^{2(n-i)})}
{(1-q^{-1}abt^{2(n-i)})},\\
w_{j,k}^+(m;q)&=\frac{\bigl(q^{-1}abt^{2n-j-k+1};q\bigr)_m}
{\bigl(abt^{2n-j-k-1};q\bigr)_m}\frac{(1-q^{m-1}abt^{2n-j-k})}
{(1-q^{-1}abt^{2n-j-k})},\\
w_{j,k}^-(m;q)&=\frac{\bigl(t^{k-j+1};q\bigr)_m}{\bigl(qt^{k-j-1};q\bigr)_m}
\frac{(1-q^mt^{k-j})}{(1-t^{k-j})}.
\end{split}$$
:::

::: proof
*Proof.* This follows from a direct computation using the evaluation formulas and the quadratic norm formulas for the multivariable little $q$-Jacobi polynomials. ◻
:::

The explicit expressions for the generalized dimensions associated to the fundamental partitions $\omega_r\in\Lambda_n$ ($r=0,\ldots,n$) simplify drastically.

::: prop
[]{#lemref label="lemref"} For $r=0,\ldots,n$ we have $$\label{fundamentalqformula}
D_q(\omega_r)=\frac{\bigl(qabt^{2n-r-1}, t^{n+1-r}, at^{n-r}, abt^{2n-r};t\bigr)_r}
{\bigl(q, t, bt^{n-r}, abt^{n-r-1};t\bigr)_r}
\left(\frac{1-abt^{2n-2r-1}}{1-abt^{2n-1}}\right)a^{-r}t^{r(r+1-2n)}.$$
:::

::: proof
*Proof.* Note that $$|\omega_r|=r,\qquad 2(\rho,\omega_r)=r(2n-r-1).$$ By Lemma [\[explicitD\]](#explicitD){reference-type="ref" reference="explicitD"} we thus obtain $$\label{Dq}
D_q(\omega_r)=a^{-r}t^{r(r+1-2n)}\prod_{i=1}^rv_i(1;q)
\prod_{1\leq j<k\leq r}w_{j,k}^+(2;q)\prod_{j=1}^r\prod_{k=r+1}^nw_{j,k}^+(1;q)
\prod_{j=1}^r\prod_{k=r+1}^nw_{j,k}^-(1;q).$$ By direct computations we obtain the explicit expressions $$\label{form}
\begin{split}
\prod_{i=1}^rv_i(1;q)&=\frac{\bigl(at^{n-r}, q^{-1}abt^{n-r};t\bigr)_r\bigl(qabt^{2n-2r};t^2\bigr)_r}
{\bigl(qt^{n-r}, bt^{n-r};t\bigr)_r\bigl(q^{-1}abt^{2n-2r};t^2\bigr)_r},\\
\prod_{1\leq j<k\leq r}w_{j,k}^+(2;q)&=\frac{\bigl(abt^{2n-r};t\bigr)_r\bigl(q^{-1}abt^{2n-2r}, qabt^{2n-2r-1};t^2\bigr)_r}
{\bigl(q^{-1}abt^{2n-2r}, qabt^{2n-2r-1}, abt^{2n-2r-1};t\bigr)_r}
\frac{(1-abt^{2n-2r-1})}{(1-abt^{2n-1})},\\
\prod_{j=1}^r\prod_{k=r+1}^nw_{j,k}^+(1;q)&=\frac{\bigl(q^{-1}abt^{2n-2r}, abt^{2n-2r-1};t\bigr)_r}
{\bigl(q^{-1}abt^{n-r}, abt^{n-r-1};t\bigr)_r},\\
\prod_{j=1}^r\prod_{k=r+1}^nw_{j,k}^-(1;q)&=\frac{\bigl(t^{n+1-r},
qt^{n-r};t\bigr)_r}{\bigl(t,q;t\bigr)_r}.
\end{split}$$ Only the second formula needs explanation. Set $$e_r(u;t)=\prod_{1\leq j<k\leq
r}\left(\frac{1-ut^{1-j-k}}{1-ut^{-j-k}}\right),$$ then we can write $$\prod_{1\leq j<k\leq r}w_{j,k}^+(2;q)=e_r(q^{-1}abt^{2n})
e_r(abt^{2n})e_r(abt^{2n-1})e_r(qabt^{2n-1}).$$ On the other hand, by induction to $r\in\{1,\ldots,n\}$, $$e_r(u;t)=\frac{\bigl(ut^{2-2r};t^2\bigr)_{r-1}}{\bigl(ut^{1-2r};t\bigr)_{r-1}}.$$ Combining both formulas we easily obtain the desired expression for $\prod_{1\leq j<k\leq r}w_{j,k}^+(2;q)$. The lemma now follows by substituting the expressions [\[form\]](#form){reference-type="eqref" reference="form"} in [\[Dq\]](#Dq){reference-type="eqref" reference="Dq"}, and by simplifying the resulting expression. ◻
:::

As a curiosity, note that the elementary identity $$\bigl(ut^{1-r};t\bigr)_r=(-u)^rt^{-\frac{1}{2}r(r-1)}\bigl(u^{-1};t\bigr)_r$$ allows us to rewrite [\[fundamentalqformula\]](#fundamentalqformula){reference-type="eqref" reference="fundamentalqformula"} as $$D_q\bigl(\omega_r)=\frac{\bigl(t^{-n},a^{-1}t^{1-n},
a^{-1}b^{-1}t^{1-2n},
q^{-1}a^{-1}b^{-1}t^{2-2n};t\bigr)_r}
{\bigl(t,q,b^{-1}t^{1-n},
a^{-1}b^{-1}t^{2-n};t\bigr)_r}\\
\left(\frac{1-a^{-1}b^{-1}t^{1+2r-2n}}{1-a^{-1}b^{-1}t^{1-2n}}\right)
\bigl(qa t^{2n-1}\bigr)^r$$ for $r=0,\ldots,n$, which one recognizes as the weight function for $t$-Racah polynomials, see e.g. [@KS].
