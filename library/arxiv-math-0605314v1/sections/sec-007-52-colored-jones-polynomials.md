---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-007-52-colored-jones-polynomials
section_title: "Colored Jones polynomials"
section_number: 5.2
pages: 19-20
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.805
latex_coverage_ratio: 0.97
---
[]{#sec5 label="sec5"}

In this section, we recall the definition of the colored Jones polynomials of framed links.

## Finite-dimensional representations of $U_h$ {#sec:representations}

By a *finite-dimensional representation* of $U_h$, we mean a left $U_h$-module which is free of finite rank as a $\modQ [[h]]$-module.

It is well known that, for each $n\ge 0$, there is exactly one irreducible finite-dimensional representation $\V_n$ of rank $n+1$ up to isomorphism, which corresponds to the $(n+1)$-dimensional irreducible representation of $sl_2$.

The structure of $\V_n$ is as follows. Let $\vn0\in \V_n$ denote a highest weight vector of $\V_n$, which is characterized by $E\vn0=0$, $H\vn0=n\vn0$ and $U_h\vn0=\V_n$. It is useful to define the other basis elements by $$\vn i= \tF^{(i)}\vn0\quad \text{for $i=1,\ldots,n$}.$$ Then the action of $\Uq$ on $\V_n$ is given by $$\begin{gathered}
  K^{\pm 1} \vn i= v^{n-2i}\vn i,\\
  e^m \vn i= \{n-i+m\}_{q,m} \vn{i-m},\\
  \tF^{(m)} \vn i= q^{-mi}\bbq{i+m}{m}\vn{i+m},
\end{gathered}$$ for $i=0,\ldots,n$ and $m\ge 0$, where we understand $\vn i=0$ unless $0\le i\le n$.

## Colored Jones polynomials {#sec:color-jones-polyn}

Let $L=L_1\cup \cdots\cup L_m$ be an $m$-component, framed, oriented, ordered link, and let $W_1,\ldots,W_m\ge 0$ be finite-dimensional representations of $U_h$. We consider each $W_i$ as a *color* attached to the component $L_i$. Then the colored Jones polynomial $J_L(W_1,\ldots,W_m)$ of the colored link $(L;W_1,\ldots,W_m)$ is defined as follows.

We choose a diagram of $L$ which is obtained by pasting copies of the fundamental tangles, as in the definition of the universal $sl_2$ invariant in Section [\[sec:univ-sl2-invar\]](#sec:univ-sl2-invar){reference-type="ref" reference="sec:univ-sl2-invar"}. To each copy of a fundamental tangle in $L$, we associate a left $U_h$-module homomorphism. To a vertical line contained in $L_i$, we associate to the left $U_h$-module $W_i$ if the line is oriented downward, and the dual $W_i^*$ of $W_i$ if the line is oriented upward. To a positive crossing, we associate a braiding operator $$\psi _{W,W'}\zzzcolon W\otimes W'\rightarrow W'\otimes W, \quad x\otimes y\mapsto \sum\beta y\otimes \alpha x,$$ where $W$ (resp. $W'$) are the left $U_h$-modules associated to the string which connects the upper left corner and the lower right corner (resp. the upper right corner and the lower left corner). To a negative crossing, we associate $$\psi _{W',W}^{-1}\zzzcolon W\otimes W'\rightarrow W'\otimes W, \quad x\otimes y\mapsto \sum\bar\alpha y\otimes \bar\beta x,$$ where $W$ and $W'$ are as above. To the last four tangles in Figure [\[fig:fundamental2\]](#fig:fundamental2){reference-type="ref" reference="fig:fundamental2"}, we associate the following operators $$\begin{gathered}
  \ev_{W}\zzzcolon W^*\otimes W\rightarrow \modQ [[h]], \quad f\otimes x\mapsto f(x),\\
  \ev'_{W}\zzzcolon W\otimes W^*\rightarrow \modQ [[h]], \quad x\otimes f\mapsto f(\kappa x),\\
  \coev_{W}\zzzcolon \modQ [[h]]\rightarrow W\otimes W^*, \quad 1\mapsto \sum_ix_i\otimes x^i,\\
  \coev'_{W}\zzzcolon \modQ [[h]]\rightarrow W^*\otimes W, \quad 1\mapsto \sum_ix^i\otimes \kappa ^{-1}x_i,
\end{gathered}$$ respectively, where $W=W_i$ if $L_i$ is the component of $L$ containing the fundamental tangle, and where the $x_i$ are a basis of $W$ and the $x^i\in W^*$ are the dual basis.

By tensoring and composing the operators, we obtain a left $U_h$-module homomorphism from $\modQ [[h]]$ to $\modQ [[h]]$, and we define $J_L(W_1,\ldots,W_m)$ to be the trace of this homomorphism.

Note that "$J_L$" alone denotes the universal $sl_2$ invariant of $L$. The above definition of $J_L(W_1,\ldots,W_n)$ is an abuse of notation, but it should not cause confusion.

It is well known that $J_L\in q^{p/4}\Zqq\subset \modZ [q^{\pm 1/4}]$, where $p\in \modZ /4\modZ$ depends only on the linking matrix of $L$ and on $n_1,\ldots,n_m$. The invariant is normalized so that $J_{\emptyset}()=1$, and $J_U(\V_n)=[n+1]$ for $n\ge 0$, where $U$ denotes the $0$-framed unknot.
