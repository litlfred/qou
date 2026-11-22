---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-009-43-the-rank-of-v-part-b-of-theorem-32
section_title: "The rank of V+: part (b) of Theorem 3.2"
section_number: 4.3
pages: 11-12
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.94
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.rankV+ label="sub.rankV+"}

Consider a function $f(m,e)$ of two discrete integer variables $e,m$ which satisfies Equations [\[eq.rec1\]](#eq.rec1){reference-type="eqref" reference="eq.rec1"} and [\[eq.rec2\]](#eq.rec2){reference-type="ref" reference="eq.rec2"}. Section [\[sub.partd\]](#sub.partd){reference-type="ref" reference="sub.partd"} implies that $f(0,e)$ satisfies the 3-term recursion $$\label{eq.recI2}
f(0, e) - (2 - q^{e-1}) f(0, e - 1) + f(0, e - 2)=0$$ for all integers $e$. It follows that for every integer $e$, $f(0,e)$ is a $\mathbb Z[q^{\pm 1}]$-linear combination of $A$ and $B$ where $f(0,0)=A$ and $f(0,1)=B$. An induction on $e<0$ using the recursion relation [\[eq.recI2\]](#eq.recI2){reference-type="eqref" reference="eq.recI2"} shows that for all $e<0$ we have $$f(0,e) = q^{-\frac{e^2}{2}-\frac{e}{2}} \left( p_1(e) A + p_2(e) B \right)$$ where $p_1(e), p_2(e) \in \mathbb Z[q]$ are polynomials of maximum $q$-degree $e^2/2+e/2$ and constant term $(-1)^{e-1}$ and $(-1)^e$ respectively. For example, we have:

$$\begin{aligned}
f(0,-1)&=& A-B \\
q f(0,-2) &=&
A (-1+q) + B (1-2 q)
\\
q^3 f(0,-3) &=&
A \left(1-q-2 q^2+q^3\right) + B \left(-1+2 q+2 q^2-3 q^3\right)
\\
q^6 f(0,-4) &=&
A \left(-1+q+2 q^2+q^3-2 q^4-3 q^5+q^6\right) \\ & & 
+B \left(1-2 q-2 q^2+q^3+4 q^4+3 q^5-4 q^6\right)
\\
q^{10} f(0,-5) &=&
A \left(1-q-2 q^2-q^3+5 q^5+3 q^6+q^7-3 q^8-4 q^9+q^{10}\right) \\ & & 
+B \left(-1+2 q+2 q^2-q^3-2 q^4-7 q^5+3 q^7+6 q^8+4 q^9-5 q^{10}\right)
\end{aligned}$$ Let us write $$A=\sum_{n=0}^\infty a_n q^n  \qquad
B=\sum_{n=0}^\infty b_n q^n \,.$$ If we assume that $f(0,e) \in \mathbb Z[[q]]$, this imposes a system of linear equations on the coefficients $a_n$ and $b_n$ of $A$ and $B$. In fact, for fixed $e <0$, the system of equations $\mathrm{coeff}(f(0,e),q^j)=0$ for $j=-e^2/2-e/2, \dots, -2,-1$ is a triangular system of linear equations with unknowns $b_j$ for $j=0,1,\dots,e^2/2-e/2-1$ where all diagonal entries of the coefficient matrix are $1$. For example, we have: $$\left(
\begin{array}{cccccc}
 1 & 0 & 0 & 0 & 0 & 0 \\
 -2 & 1 & 0 & 0 & 0 & 0 \\
 -2 & -2 & 1 & 0 & 0 & 0 \\
 1 & -2 & -2 & 1 & 0 & 0 \\
 4 & 1 & -2 & -2 & 1 & 0 \\
 3 & 4 & 1 & -2 & -2 & 1 \\
\end{array}
\right) 
\left(
\begin{array}{c}
b_0 \\
b_1 \\
b_2 \\
b_3 \\
b_4 \\
b_5
\end{array}
\right)
=
\left(
\begin{array}{c}
 -a_{0} \\
 a_{0}-a_{1} \\
 2 a_{0}+a_{1}-a_{2} \\
 a_{0}+2 a_{1}+a_{2}-a_{3} \\
 -2 a_{0}+a_{1}+2 a_{2}+a_{3}-a_{4} \\
 -3 a_{0}-2 a_{1}+a_{2}+2 a_{3}+a_{4}-a_{5} \\
\end{array}
\right)$$ It follows that $b_n$ is a $\mathbb Z$-linear combination of $a_k$ for $k \leq n$. This proves that the rank of the $\mathbb Z[[q]]$-module $V_+$ is at most $1$. Since $I_{\Delta}\in V_+$ (as follows from the proof of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}), it follows that the rank of the $\mathbb Z[[q]]$-module $V_+$ is exactly $1$. This proves part (b) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}. 0◻

::: corollary
[]{#cor.V+ label="cor.V+"} The above proof implies that $f \in V_+$ is uniquely determined by its initial condition $f(0,0) \in \mathbb Z[[q]]$. It follows that if $f,g \in V_+$, then $$\label{eq.fg00}
g(0,0)f(m,e)=f(0,0)g(m,e)$$ for all integers $m$ and $e$.
:::
