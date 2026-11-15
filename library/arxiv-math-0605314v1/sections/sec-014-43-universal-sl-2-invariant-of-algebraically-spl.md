---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-014-43-universal-sl-2-invariant-of-algebraically-spl
section_title: "Universal $sl_2$-invariant of algebraically-split, $0$-framed bottom tangles"
section_number: 4.3
pages: 16-17
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.919
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:invariant label="sec:invariant"}

For any left $U_h$-module $W$, let $\Inv(W)$ denote the *invariant part* of $W$, defined by $$\Inv(W) =\{w\in W\zzzvert  x\cdot w=\epsilon (x)w\quad \forall x\in U_h\}.$$

Recall that we regard $U_h$ as a left $U_h$-module via the adjoint action. For $n\ge 0$, the completed tensor product $\Uhn$ is equipped with a left $U_h$-module structure $\trrn$ in the standard way: For $x=\sum x_1\otimes \cdots\otimes x_n\in \Uhn$ and $y\in U_h$ we have $$y\trrn x = \sum (y_{(1)}\trr x_1)\otimes \cdots\otimes (y_{(n)}\trr x_n).$$ In particular, $\Uhx0=\modQ [[h]]$ is given the trivial left $U_h$-module structure. For any subset $X\subset \Inv(U_h^{\ho n})$, we set $$\Inv(X) = \Inv(U_h^{\ho n})\cap X.$$

For $n\ge 0$, we set $$\modK _n= \Inv(\tUqvn)\subset \tUqvn.$$ One can easily see that $\modK _n$ is the $\tUq$-invariant part of the $\tUq$-module $\tUqvn$, i.e., we have $$\modK _n =\{x\in \tUqvn\zzzvert y\trrn x=\epsilon (y)x\quad \text{for all $y\in \tUq$}\}.$$

The main result of this subsection is the following.

::: theorem
[]{#thm:8 label="thm:8"} If $T\in \BT^0_n$, $n\ge 0$, then we have $J_T\in \modK _n$.
:::

To prove Theorem [\[thm:8\]](#thm:8){reference-type="ref" reference="thm:8"}, we use the following two results from [@H:universal].

::: proposition
[]{#r19 label="r19"} For any $n$-component bottom tangle $T\in \BT_n$, we have $J_T\in \Inv(U_h^{\ho n})$.
:::

::: proposition
[]{#lem:1 label="lem:1"} Let $X_n\subset U_h^{\ho n}$, $n\ge 0$, be subsets satisfying the following conditions.

1.  $1\in X_0$, $1\in X_1$, and $J_B\in X_3$. Here $B\in \BT^0_3$ is the *Borromean tangle* depicted in Figure [\[fig:borromean\]](#fig:borromean){reference-type="ref" reference="fig:borromean"}.

2.  If $x\in X_l$ and $y\in X_m$ with $l,m\ge 0$, then $x\otimes y\in X_{l+m}$.

3.  For $p,q\ge 0$ and $f\in \{\psi ^{\pm 1},\mu ,\bD,\bS\}$ with $f\zzzcolon U_h^{\ho i}\rightarrow U_h^{\ho j}$, we have $$(1^{\otimes p}\otimes f\otimes 1^{\otimes q})(X_{p+i+q})\subset X_{p+j+q}.$$

Then, for any $T\in \BT^0_n$, we have $J_T\in X_n$.
:::

::: proof
*Proof of Theorem [\[thm:8\]](#thm:8){reference-type="ref" reference="thm:8"}.* By Proposition [\[r19\]](#r19){reference-type="ref" reference="r19"}, it suffices to show that $J_T\in \tUqvx n$. We have only to verify the conditions in Proposition [\[lem:1\]](#lem:1){reference-type="ref" reference="lem:1"}, where we set $X_n=\tUqvx n$.

The condition (2) is obvious.

The condition (3) follows from Corollary [\[thm:20\]](#thm:20){reference-type="ref" reference="thm:20"}.

To prove (1), it suffices to prove $J_B\in \tUqvx3$. Using Figure [\[fig:borromean\]](#fig:borromean){reference-type="ref" reference="fig:borromean"}, we obtain $$J_B
    = \sum
    \bar\alpha _3 \beta _1         \alpha _3 S^2(\bar\beta _1)\otimes 
    \bar\alpha _1 \beta _2         \alpha _1 S^2(\bar\beta _2)\otimes 
    \bar\alpha _2 S^{-2}(\beta _3) \alpha _2 \bar\beta _3,$$ where $R=\sum \alpha _i\otimes \beta _i$ and $R^{-1}=\sum \bar\alpha _i\otimes \bar\beta _i$ for $i=1,2,3$. Using [\[eq:11\]](#eq:11){reference-type="eqref" reference="eq:11"} and [\[e30\]](#e30){reference-type="eqref" reference="e30"}, we obtain $$\begin{split}
      J_B
      &=
      \sum_{m_1,m_2,m_3,n_1,n_2,n_3\ge 0}
      (-1)^{n_1+n_2+n_3}
      q^{-\hf m_1(m_1+1)-\hf m_2(m_2+1)-\hf m_3(m_3+1)}\\&\quad
      \tF^{(n_3)}\bar D'_3 e^{m_1}D''_1        D'_3\tF^{(m_3)} S^2(\bar D''_1e^{n_1})\otimes 
      \tF^{(n_1)}\bar D'_1 e^{m_2}D''_2         D'_1\tF^{(m_1)} S^2(\bar
      D''_2e^{n_2})\\
      &\quad \otimes \tF^{(n_2)}\bar D'_2 S^{-2}(e^{m_3}D''_3) D'_2\tF^{(m_2)} \bar D''_3e^{n_3},
    \end{split}$$ where $D=\sum D'_i\otimes D''_i$ and $D^{-1}=\sum \bar D'_i\otimes \bar D''_i$ for $i=1,2,3$. We slide the tensor factors of the copies of $D^{\pm 1}$ using [\[e31\]](#e31){reference-type="eqref" reference="e31"} so that these copies cancel at the cost of inserting powers of $K$. Thus we obtain $$\label{eq:7}
      \begin{split}
    J_B
    &=
    \sum_{m_1,m_2,m_3,n_1,n_2,n_3\ge 0}q^{m_3+n_3}
    (-1)^{n_1+n_2+n_3}
    q^{\sum_{i=1}^3( -\hf m_i(m_i+1)-n_i+m_im_{i+1}-2m_in_{i-1})}\\
    &\quad \tF^{(n_3)} e^{m_1}   \tF^{(m_3)} e^{n_1}K^{-2m_2}\otimes 
    \tF^{(n_1)} e^{m_2}    \tF^{(m_1)} e^{n_2}K^{-2m_3}\otimes 
    \tF^{(n_2)} e^{m_3}    \tF^{(m_2)} e^{n_3}K^{-2m_1},
      \end{split}$$ where the index $i$ should be considered modulo $3$. Each term in [\[eq:7\]](#eq:7){reference-type="eqref" reference="eq:7"} is in $\Uqvx3$. For any $p\ge 0$, all but finitely many terms in [\[eq:7\]](#eq:7){reference-type="eqref" reference="eq:7"} involve $e^r$ with $r\ge p$, and therefore are contained in $\modF _p(\Uqvx3)$. Therefore, we have $J_B\in \tUqvx3$. ◻
:::
