---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-005-3-axioms-for-the-tetrahedron-index
section_title: "Axioms for the tetrahedron index"
section_number: 3
pages: 8-10
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.917
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sec.axioms label="sec.axioms"}

In this section we discuss an axiomatic approach to the tetrahedron index. Let $\mathbb Z((q^{1/2}))$ (resp., $\mathbb Z[[q^{1/2}]]$) denote the ring of series of the form $$f(q)=\sum_{n \in \frac{1}{2}\mathbb Z} a_{n} q^{n}$$ where there exists $n_0=n_0(f)$ such that $a_n=0$ for all $n < n_0$ (resp., $n < 0$). For $f(q) \in \mathbb Z((q^{1/2}))$, its *degree* $\delta(f(q))$ is the largest half-integer (or infinity) such that $f(q) \in q^{d(f)}\mathbb Z[[q^{1/2}]]$. We will say that $f(q) \in \mathbb Z((q^{1/2}))$ is $q$-*positive* if $\delta(f(q)) \geq 0$.

::: definition
[]{#def.2rec label="def.2rec"} A *tetrahedron index* is a function $f: \mathbb Z^2 \longrightarrow\mathbb Z((q^{1/2}))$ that satisfies the equations $$\begin{equation} 
\label{eq.rec1}
 q^{\frac{e}{2}} f(m + 1, e) + q^{-\frac{m}{2}} f(m, e + 1) - f(m, e)=0
  \end{equation} 
  \begin{equation} 
\label{eq.rec2} 
 q^{\frac{e}{2}} f(m - 1, e) + q^{-\frac{m}{2}} f(m, e - 1) - f(m, e)=0
  \end{equation}$$ for all integers $m,e$, together with the parity condition $f(m,e) \in
q^{\frac{e m}{2}}\mathbb Z((q))$ for all $m$ and $e$. Let $V$ denote the set of all tetrahedron indices, and $V_+$ denote the set of all $q$-positive tetrahedron indices.
:::

::: theorem
[]{#thm.1 label="thm.1"} (a) $V$ is a free $q$-holonomic $\mathbb Z((q))$-module of rank $2$. (b) $V_+$ is a free $q$-holonomic $\mathbb Z[[q]]$-module of rank $1$. (c) If $f \in V$, then it satisfies the equation $$\label{eq.Z3}
f(m,e)(q)=(-q^{\frac{1}{2}})^{-e}f(e,-e-m)(q)
=(-q^{\frac{1}{2}})^m f(-e-m,m)(q)$$ for all integers $m$ and $e$. (d) If $f \in V$, then it satisfies the equations

$$\begin{equation} 
\label{eq.rec1a}
f(m, e+1) + (q^{e + \frac{m}{2}} - q^{-\frac{m}{2}} - q^{\frac{m}{2}}) 
f(m, e) + f(m, e - 1)  = 0
  \end{equation} 
  \begin{equation} 
\label{eq.rec2a} 
f(m+1, e) + (q^{- \frac{e}{2} - m} - q^{-\frac{e}{2}} - q^{\frac{e}{2}}) 
f(m, e) +  f(m - 1, e) =   0 
  \end{equation}$$ for all integers $m,e$.
:::

::: question
[]{#que.basisV label="que.basisV"} What is a basis for $V$?
:::

::: remark
[]{#rem.thm1a label="rem.thm1a"} The proof of part (a) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} implies that if $f(m,e)$ is a tetrahedron index, then $f(m,e)$ is a a unique $\mathbb Z[q^{\pm 1/2}]$ linear combination of $A$ and $B$ where $(f(0,0),f(0,1))=(A,B)$. For example, if $C=(f(m,e))_{-2 \leq m,e \leq 2}$, then $C=M_A A + M_B B$ where

$$\begin{aligned}
M_A &=& 
\left(
\begin{array}{ccccc}
 1-\frac{1}{q^3}+\frac{1}{q^2}+\frac{1}{q}-q^2 & \frac{1}{q}-q & -1 & -\frac{1}{q} & -\frac{1}{q^2}+\frac{1}{q} \\
 1-\frac{1}{q^2}+\frac{1}{q} & \frac{1}{\sqrt{q}} & 0 & -\frac{1}{\sqrt{q}} & -\frac{1}{q} \\
 1-\frac{1}{q} & 1 & 1 & 0 & -1 \\
 -1 & 0 & 1 & \frac{1}{\sqrt{q}} & \frac{1}{q}-q \\
 -q & -1 & 1-\frac{1}{q} & 1-\frac{1}{q^2}+\frac{1}{q} & 1-\frac{1}{q^3}+\frac{1}{q^2}+\frac{1}{q}-q^2 \\
\end{array}
\right)
\\
M_B &=& 
\left(
\begin{array}{ccccc}
 \frac{1}{q^3}-\frac{2}{q^2}-\frac{1}{q}+q+2 q^2-q^3 & 1-\frac{1}{q}+2 q-q^2 & 2-q & -1+\frac{1}{q} & \frac{1}{q^2}-\frac{2}{q} \\
 -1+\frac{1}{q^2}-\frac{2}{q}+q & -\frac{1}{\sqrt{q}}+\sqrt{q} & 1 & \frac{1}{\sqrt{q}} & -1+\frac{1}{q} \\
 -2+\frac{1}{q} & -1 & 0 & 1 & 2-q \\
 1-q & -\sqrt{q} & -1 & -\frac{1}{\sqrt{q}}+\sqrt{q} & 1-\frac{1}{q}+2 q-q^2 \\
 2 q-q^2 & 1-q & -2+\frac{1}{q} & -1+\frac{1}{q^2}-\frac{2}{q}+q & \frac{1}{q^3}-\frac{2}{q^2}-\frac{1}{q}+q+2 q^2-q^3 \\
\end{array}
\right)
\end{aligned}$$
:::

::: remark
[]{#rem.thm1b label="rem.thm1b"} The proof of part (b) of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} implies that if $f(m,e)$ is a tetrahedron index, then $f(m,e)$ is uniquely determined by $f(0,0)=\sum_{n=0}^\infty a_n q^n$. In particular, if $f(0,1)=\sum_{n=0}^\infty b_n q^n$, then $b_n$ are $\mathbb Z$-linear combinations of $a_k$ for $k \leq n$. For example, we have: $$\begin{aligned}
b_{0} &=&  a_{0}
\\ 
b_{1} &=&  a_{0}+a_{1}
\\ 
b_{2} &=&  2 a_{0}+a_{1}+a_{2}
\\ 
b_{3} &=&  4 a_{0}+2 a_{1}+a_{2}+a_{3}
\\ 
b_{4} &=&  9 a_{0}+4 a_{1}+2 a_{2}+a_{3}+a_{4}
\\ 
b_{5} &=&  20 a_{0}+9 a_{1}+4 a_{2}+2 a_{3}+a_{4}+a_{5}
\\ 
b_{6} &=&  46 a_{0}+20 a_{1}+9 a_{2}+4 a_{3}+2 a_{4}+a_{5}+a_{6}
\\ 
b_{7} &=&  105 a_{0}+46 a_{1}+20 a_{2}+9 a_{3}+4 a_{4}+2 a_{5}+a_{6}+a_{7}
\\ 
b_{8} &=&  242 a_{0}+105 a_{1}+46 a_{2}+20 a_{3}+9 a_{4}+4 a_{5}+2 a_{6}+a_{7}+a_{8}
\\ 
b_{9} &=&  557 a_{0}+242 a_{1}+105 a_{2}+46 a_{3}+20 a_{4}+9 a_{5}+4 a_{6}+2 a_{7}+a_{8}+a_{9}
\\ 
b_{10} &=&  1285 a_{0}+557 a_{1}+242 a_{2}+105 a_{3}+46 a_{4}+20 a_{5}+9 a_{6}+4 a_{7}+2 a_{8}+a_{9}+a_{10}
\\ 
b_{11} &=&  2964 a_{0}+1285 a_{1}+557 a_{2}+242 a_{3}+105 a_{4}+46 a_{5}+20 a_{6}+9 a_{7}+4 a_{8}+2 a_{9}+a_{10}+a_{11}
\\ 
b_{12} &=&  6842 a_{0}+2964 a_{1}+1285 a_{2}+557 a_{3}+242 a_{4}+105 a_{5}+46 a_{6}+20 a_{7}+9 a_{8}+4 a_{9}+2 a_{10} \\ & & +a_{11}+a_{12}
\end{aligned}$$ In fact, it appears that $b_n$ is a $\mathbb N$-linear combination of $a_k$ for $k \leq n$, although we do not know how to show this, nor do we know of a geometric significance of this experimental fact.
:::

The next lemma computes the degree of the tetrahedron index.

::: lemma
[]{#lem.degID label="lem.degID"} The degree $\delta(m,e)$ of $I_{\Delta}(m,e)(q)$ is given by: $$\label{eq.degID}
\delta(m,e) = \frac{1}{2}\left( m_+(m+e)_+ + (-m)_+ e_+ + (-e)_+(-e-m)_+
+\max\{0,m,-e\} \right)$$ It follows that $\delta(m,e)$ is a piece-wise quadratic polynomial given by Figure [1](#fig.degI){reference-type="ref" reference="fig.degI"}.
:::

<figure id="fig.degI">
<div class="center">
<embed src="draws/degI.pdf" />
</div>
<figcaption>The degree of the tetrahedron index.</figcaption>
</figure>

The next theorem gives an axiomatic characterization of the tetrahedron index $I_{\Delta}$.

::: theorem
[]{#thm.2 label="thm.2"} $I_{\Delta}$ is uniquely characterized by the following equations:

-   $I_{\Delta}\in V_+$, $I_{\Delta}(0,0)(0) \neq 0$

-   $I_{\Delta}$ satisfies the pentagon identity $$\label{eq.pentagon}
    I_{\Delta}(m_1-e_2,e_1)I_{\Delta}(m_2-e_1,e_2)=\sum_{e_3 \in \mathbb Z}
    q^{e_3} I_{\Delta}(m_1,e_1+e_3)I_{\Delta}(m_2,e_2+e_3)I_{\Delta}(m_1+m_2,e_3)\,,$$ for all integers $m_1,m_2,e_1,e_2$.
:::

::: remark
[]{#rem.thm2 label="rem.thm2"} The uniqueness part of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"} uses only the facts that $I_{\Delta}\in V$, $\delta(I_{\Delta}(0,e)) \geq 0$ for all $e$ and $I_{\Delta}$ satisfies the special pentagon $$I_{\Delta}(0,0)^2=\sum_{e \in \mathbb Z} I_{\Delta}(0,e)^3 q^{e} \,.$$
:::
