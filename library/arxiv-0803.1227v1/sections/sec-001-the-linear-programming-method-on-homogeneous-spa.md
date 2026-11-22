---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-001-the-linear-programming-method-on-homogeneous-spa
section_title: "The linear programming method on homogeneous spaces"
section_number: null
pages: 2-3
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.992
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
We briefly describe the linear programming method on homogeneous spaces. For more details we refer to [@LEVEN], [@CS Chapter 9] for a treatment of 2-point homogeneous spaces, and to [@CHRISTINE1] for the prominent case of Grassmann codes.

Let $G$ be a compact group acting transitively and continuously on a compact space $X$, and $\tau : X\times X  \to Y$ such that $\tau$ characterizes the orbits of $G$ acting on $X\times X$. We mean here that, for all $x_1,x_2,x'_1,x'_2 \in X$, $$\tau(x_1,x_2)=\tau(x'_1,x'_2) \Leftrightarrow \exists  g \in G :
g(x_1,x_2)=(x'_1,x'_2).$$

Let $S$ be any subset of $Y$, we call a finite subset $\Code \subset
  X$ a $S$-code if for all $c_1 \ne c_2 \in \Code,\ \tau(c_1,c_2) \in S$.

A continuous function $P : Y \to \C$ is said to possess the positivity property if for any finite subset $\Code \subset X$ and any complex function $\alpha : X \to \C$,

$$\sum_{x,y \in \Code} \alpha(x) \conj{\alpha(y)} P\left(\tau(x,y)\right)
  \textrm{ is real non-negative.}$$ A canonical example is the constant function $P_0=1$; non-trivial examples are given by the so called zonal functions that we introduce now.

Let $L^2(X)=\left\{ u:X\to\C : \int_X |u(x)|^2 dx < \infty\right\}$ where $dx$ is the unique $G$-invariant Haar measure on $X$ such that $\int_X  dx =1$. This vector space is given the standard $G$-action defined by $g.u(x)=u(g^{-1}(x))$ and is endowed with the canonical $G$-invariant hermitian product : $(u_1,u_2)=\int_X u_1(x)\conj{u_2(x)} dx.$ The Peter-Weil theorem shows that $L^2(X)$ can be decomposed as a direct sum of $G$-irreducible subspaces $V_i$. The next step is to associate to each irreducible subspace $V_i$ a so-called zonal function $P_{V_i}$. A standard construction is the following: given an orthonormal basis $(u_1(x),...,u_d(x))$ of $V_i$, one can define $$\begin{aligned}
\label{DEFEQ}
   \tilde P_{V_i}(x,y)= \frac 1 d_i \sum_{i=1}^{d_i} u_i(x)\conj{u_i(y)}.
   
\end{aligned}$$ where $d_i=\dim(V_i)$. Since these functions are constant on $G$-orbits we can rewrite $\tilde P_{V_i}(x,y)=P_{V_i}\left(\tau(x,y)\right)$. From this property comes the term *zonal functions* used to qualify them. From equation ([\[DEFEQ\]](#DEFEQ){reference-type="ref" reference="DEFEQ"}) it is easy to prove that these zonal functions verify the positivity property and do not depend of the chosen orthonormal basis. It turns out that, when the irreducible subspaces $V_i$ are pairwise non isomorphic, the cone of continuous positive $G$-invariant functions is exactly the set of linear combinations with non negative coefficients of the $P_{V_i}$ (see [@BOCHNER]). In the remaining of this paper we assume that this condition is satisfied. We moreover let $V_0$ denote the one-dimensional subspace associated to the trivial representation of $G$.

The so-called linear programming bounds are obtained with the following theorem :

::: theorem
[]{#FUNDATHM label="FUNDATHM"} Let $P=\sum_{i} c_i P_{V_i}$ a linear combination of the zonal functions $P_{V_i}$ with a finite number of non zero coefficients. Assume furthermore that : $c_i\ge 0$, $c_0 >0$ and $\Re(P)$ (the real part of $P$) is non-positive on $S$. Then any $S$-code verifies $$\begin{aligned}
\label{FUNDA} |\Code| \le \frac{ P(\tau_0)}{c_0}
   
\end{aligned}$$ where $\tau_0=\tau(x,x)$ for any $x$.
:::

::: proof
*Proof.* On one hand, $$\begin{aligned}
   \sum_{x,y \in \Code} P(\tau(x,y))&= \sum_{x=y \in \Code}
   P(\tau(x,y)) + \sum_{x\ne y \in \Code} P(\tau(x,y))\\
 &\leq |\Code|P(\tau_0) 
\end{aligned}$$ On the other hand, $$\begin{aligned}
\sum_{x,y \in \Code} P(\tau(x,y)) &= \sum_{x,y \in \Code} c_0 P_0(\tau(x,y)) +
\textrm{non negative terms} \\
&\ge |\Code|^2c_0.
\end{aligned}$$ ◻
:::
