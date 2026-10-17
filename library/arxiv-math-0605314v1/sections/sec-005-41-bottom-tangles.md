---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-005-41-bottom-tangles
section_title: "Bottom tangles"
section_number: 4.1
pages: 14-18
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.952
doc_brief: "arXiv:math/0605314v1 [math.GT] 11 May 2006 — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring Z[q] such that the evaluation at"
---
[]{#sec:bottom-tangles label="sec:bottom-tangles"}

Here we recall from [@H:universal] the notion of bottom tangles.

An $n$-component *bottom tangle* $T=T_1\cup \cdots\cup T_n$ is a framed tangle in a cube, which is drawn as a diagram in a rectangle as usual, consisting of $n$ arcs $T_1,\ldots,T_n$ such that for each $i=1,\ldots,n$ the component $T_i$ runs from the $2i$th endpoint on the bottom to the $(2i-1)$st endpoint on the bottom, where the endpoints are counted from the left. For example, see Figure [\[fig:bt\]](#fig:bt){reference-type="ref" reference="fig:bt"} (a). (Here and in what follows, we use the blackboard framing convention.)

For each $n\ge 0$, let $\BT_n$ denote the set of the isotopy classes of $n$-component bottom tangles. Set $\BT=\bigcup_{n\ge 0}\BT_n$.

The *closure* $\cl(T)$ of $T$ is the $n$-component, oriented, ordered framed link in $S^3$, obtained from $T$ by pasting a "$\cup$-shaped tangle" to each component of $L$, as depicted in Figure [\[fig:bt\]](#fig:bt){reference-type="ref" reference="fig:bt"} (b). For any oriented, ordered framed link $L$, there is a bottom tangle whose closure is isotopic to $L$.

The *linking matrix* of a bottom tangle $T=T_1\cup \cdots\cup T_n$ is defined as that of the closure $T$. Thus the linking number of $T_i$ and $T_j$, $i\neq j$, is defined as the linking number of the corresponding components in $\cl(T)$, and the framing of $T_i$ is defined as the framing of the closure of $T_i$.

A link or a bottom tangle is called *algebraically-split* if the linking matrix is diagonal.

For $n\ge 0$, let $\BT^0_n$ denote the subset of $\BT_n$ consisting of algebraically-split, $0$-framed bottom tangles. Set $\BT^0=\bigcup_{n\ge 0}\BT^0_n\subset \BT$.

## Universal $sl_2$ invariant of bottom tangles {#sec:univ-sl2-invar}

For each ribbon Hopf algebra $H$, there is a "universal invariant" of links and tangles from which one can recover the operator invariants, such as the colored Jones polynomials. Such universal invariants has been studied in [@Lawrence:89; @Lawrence:90; @Reshetikhin:89; @Lee:90; @Ohtsuki:93; @Kauffman:93; @Kerler:97; @Kauffman-Radford:01]. Here we need only the case of bottom tangles, which is described in [@H:universal].

For $T=T_1\cup \cdots\cup T_n\in \BT_n$, we define the *universal $sl_2$ invariant* $J_T\in U_h^{\ho n}$ of $T$ as follows. We choose a diagram for $T$, which is obtained from copies of *fundamental tangle*, see Figure [\[fig:fundamental\]](#fig:fundamental){reference-type="ref" reference="fig:fundamental"}, by pasting horizontally and vertically.

For each copy of fundamental tangle in the diagram of $T$, we put elements of $U_h$ with the rule described in Figure [\[fig:fundamental2\]](#fig:fundamental2){reference-type="ref" reference="fig:fundamental2"}.

We set $$J_T =\sum J_{(T_1)}\otimes \cdots\otimes J_{(T_n)}\in U_h^{\ho n},$$ where for each $i=1,\ldots,n$, the $i$th tensorand $J_{(T_i)}$ is defined to be the product of the elements put on the component $T_i$. Here the elements read off along each component are written from right to left. Then $J_T$ does not depend on the choice of diagram, and defines an isotopy invariant of bottom tangles.

## Universal $sl_2$-invariant of algebraically-split, $0$-framed bottom tangles {#sec:invariant}

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

## Universal $sl_2$ invariant of bottom knots {#sec:case-n=1}

By a *bottom knot*, we mean a $1$-component bottom tangle. In what follows, we assume that bottom knots are given $0$-framing. Thus the set of bottom knots (up to isotopy) is $\BT^0_1$. By Theorem [\[thm:8\]](#thm:8){reference-type="ref" reference="thm:8"}, for any bottom knot $T\in \BT^0_1$, we have $$\label{e34}
  J_T\in \Inv(\tUqv)=Z(\tUqv).$$

Let us recall from [@H:uqsl2] the structure of $Z(\tUqv)$. (In [@H:uqsl2], $\tUqv$ is denoted by $\mathcal{G}_0(\tUq)$.) Set $$C = (v-v^{-1})^2 FE+vK+v^{-1}K^{-1}\in Z(U_h),$$ which is a well-known central element. We have $$C= (v-v^{-1}) \tF^{(1)}K^{-1}e+vK+v^{-1}K^{-1}
  \in vK\Uqv\cap Z(U_h).$$ Hence $C^2\in \Uqv\cap Z(U_h)=Z(\Uqv)$. As a $\Zqq$-algebra, $Z(\Uqv)$ is freely generated by $C^2$, i.e., we have $Z(\Uqv)\cong\Zqq[C^2]$. For $p\ge 0$, set $$\sigma _p = \prod_{i=1}^p(C^2-(q^i+2+q^{-i}))\in Z(\Uqv),$$ which is a monic polynomial of degree $p$ in $C^2$. Therefore, $$Z(\Uqv) = \Span_{\Zqq}\{\sigma _p\zzzvert p\ge 0\}.$$

As for the center of the completion $\tUqv$, we have the following.

::: theorem
[]{#thm:10 label="thm:10"} The isomorphism $Z(\Uqv)\cong \Zqq[C^2]$ induces an isomorphism $$Z(\tUqv) \cong \varprojlim_{p\ge 0} \Zqq[C^2]/(\sigma _p).$$ Thus, each element in $Z(\tUqv)$ is uniquely expressed as an infinite sum $\sum_{p\ge 0} a_p \sigma _p$, where $a_p\in \Zqq$ for $p\ge 0$.
:::

This implies the following.

::: theorem
[]{#thm:23 label="thm:23"} If $T$ is a bottom knot, then $J_T$ is uniquely expressed as $$\label{eq:74}
    J_T= \sum_{p\ge 0} a_p(T)\sigma _p,$$ where $a_p(T)\in \Zqq$ for $p\ge 0$.
:::

Note that the $a_p(T)$ are invariants of a bottom knot $T$. In Section [\[sec6\]](#sec6){reference-type="ref" reference="sec6"}, we give a formula which express $a_p(T)$ using the colored Jones polynomials of the closure of $T$.

::: remark
[]{#r6 label="r6"} There is an obvious one-to-one correspondence between bottom knots and *string knots* (i.e., a string link consisting of just one arc component running from the above to the bottom). A bottom knot and the corresponding string knot have the same value of the universal invariant. Therefore, we have the result announced in [@H:rims2001 Theorem 2.1], [@H:uqsl2 Theorem 1.2], which is the string knot version of Theorem [\[thm:23\]](#thm:23){reference-type="ref" reference="thm:23"}.
:::
