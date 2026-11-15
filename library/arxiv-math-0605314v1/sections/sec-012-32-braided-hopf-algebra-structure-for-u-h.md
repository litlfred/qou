---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-012-32-braided-hopf-algebra-structure-for-u-h
section_title: "Braided Hopf algebra structure for $U_h$"
section_number: 3.2
pages: 13-14
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.672
latex_coverage_ratio: 0.965
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec3 label="sec3"}

In this section, we recall a ribbon Hopf algebra structure for $U_h$ and show that the associated braided Hopf algebra structure for $U_h$ induces that for $\tUqv$.

## Ribbon structure for $U_h$ {#sec:ribbon-structure-uh}

The Hopf algebra $U_h$ has a ribbon Hopf algebra structure as follows. The universal $R$-matrix and its inverse are given by $$\begin{gathered}
  R = D\Bigl(\sum_{n\ge 0} v^{n(n-1)/2}
  \frac{(v-v^{-1})^n}{[n]!} F^n\otimes E^n\Bigr),\\
  \begin{split}
  R^{-1}
  &= \Bigl(\sum_{n\ge 0} (-1)^n v^{-n(n-1)/2}
  \frac{(v-v^{-1})^n}{[n]!}  F^n\otimes E^n\Bigr)D^{-1},
  \end{split}
\end{gathered}$$ where $$D=v^{\hf H\otimes H}=\exp (\frac h4 H\otimes H)\in U_h^{\ho2}.$$

In what follows, we use the following notations. $$R=\sum\alpha \otimes \beta ,\quad R^{-1}=\sum\bar\alpha \otimes \bar\beta 
  \bigl(=\sum S(\alpha )\otimes \beta \bigr).$$

The ribbon element and its inverse are given by $$\begin{gathered}
  \modr  = \sum S(\alpha )K^{-1}\beta =\sum\beta KS(\alpha ),\quad
  \modr ^{-1} = \sum \alpha K\beta =\sum\beta K^{-1}\alpha .
\end{gathered}$$ The associated grouplike element $\kappa \in U_h$ defined by $$\kappa =\bigl(\sum S(\beta )\alpha \bigr)\modr ^{-1}$$ satisfies $\kappa =K^{-1}$.

We also use the following notations. $$\begin{gathered}
  D = \sum D_{[1]}\otimes D_{[2]},\quad
  D^{-1} = \sum \bar D_{[1]}\otimes \bar D_{[2]}.
\end{gathered}$$ The following properties of $D$ are freely used in what follows. $$\begin{gathered}
  \sum D_{[2]}\otimes D_{[1]}=D,\quad
  (\Delta \otimes 1)(D)=D_{13}D_{23},\\
  (\epsilon \otimes 1)(D)=1,\quad
  (S\otimes 1)(D)=D^{-1},\\
  \label{e31}
  D^{\pm 1}(1\otimes x)=(K^{\pm |x|}\otimes x)D\quad \text{for homogeneous $x\in U_h$},
\end{gathered}$$ where $D_{13}=\sum D_{[1]}\otimes 1\otimes D_{[2]}$ and $D_{23}=\sum1\otimes D_{[1]}\otimes D_{[2]}=1\otimes D$.

We can easily obtain the following formulas. $$\begin{gathered}
  \label{eq:11}
  \begin{split}
  R
  &=D\Bigl(\sum_{n\ge 0} q^{\hf n(n-1)}\tF^{(n)}K^{-n}\otimes e^n\Bigr),
  \end{split}\\
  \label{e30}
  \begin{split}
    R^{-1}
    &=D^{-1}\Bigl(\sum_{n\ge 0} (-1)^n\tF^{(n)}\otimes K^{-n}e^n\Bigr),
  \end{split}\\
  \label{eq:65}
  \modr =\sum_{n\ge 0}(-1)^n\tF^{(n)}v^{-\hf H(H+2)}e^n,\\
  \label{eq:66}
  \modr ^{-1}=\sum_{n\ge 0}q^{\hf n(n-1)}
  \tF^{(n)}K^{-2n}v^{\hf H(H+2)}e^n.
\end{gathered}$$ We have $R^{\pm 1}\in D^{\pm 1}(\tUq\tO\tUq)$, and $\modr ^{\pm 1}\in v^{\mp\hf H(H+2)}\tUqv$.

## Braided Hopf algebra structure for $U_h$ {#sec:transmutation}

Let $\ModUh$ denote the category of $h$-adically complete left $U_h$-modules and continuous left $U_h$-module homomorphisms. The category $\ModUh$ is equipped with a standard braided category structure, where the braiding $\psi _{V,W}\zzzcolon V\otimes W\rightarrow W\otimes V$ of two objects $V$ and $W$ in $\ModUh$ is defined by $$\psi _{V,W}(v\otimes w) = \sum \beta w\otimes \alpha v\quad \text{for $v\in V$, $w\in W$}.$$ The inverse $\psi _{V,W}^{-1}\zzzcolon W\otimes V\rightarrow V\otimes W$ of $\psi _{V,W}$ is given by $$\psi _{V,W}^{-1}(w\otimes v) = \sum S(\alpha ) v\otimes \beta w\quad \text{for
  $v\in V$, $w\in W$}.$$ We regard $U_h$ as an object of $\ModUh$, equipped with the adjoint action. For simplicity, we write $\psi =\psi _{U_h,U_h}$. Thus the braiding and its inverse for $U_h$ satisfy $$\begin{gathered}
  \psi (x\otimes y) = \sum( \beta \trr y)\otimes (\alpha \trr x),\\
  \psi ^{-1}(x\otimes y) = \sum (S(\alpha )\trr y)\otimes (\beta \trr x)
\end{gathered}$$ for $x,y\in U_h$.

Let $\bUh=(U_h,\mu ,\eta ,\bD,\epsilon ,\bS)$ denote the transmutation [@Majid:algebras; @Majid:foundations] of $U_h$, which is a standard braided Hopf algebra structure in $\ModUh$ associated to $U_h$. Here $$\mu \zzzcolon U_h^{\ho2}\rightarrow U_h,\quad
  \eta \zzzcolon \modQ [[h]]\rightarrow U_h,\quad
  \epsilon \zzzcolon U_h\rightarrow \modQ [[h]],$$ are the structure morphisms of $U_h$, and $$\bD\zzzcolon U_h\rightarrow U_h^{\ho2}, \quad \bS\zzzcolon U_h\rightarrow U_h$$ are the twisted versions of comultiplication and antipode defined by $$\begin{gathered}
  \bD(x) = \sum x_{(1)}S(\beta )\otimes (\alpha \trr x_{(2)}),\\
  \label{eq:27}
  \bS(x) = \sum \beta \; S(\alpha \trr x)
\end{gathered}$$ for $x\in U_h$. The inverse $\bS^{-1}\zzzcolon U_h\rightarrow U_h$ of $\bS$ is given by $$\label{eq:28}
  \bS^{-1}(x) = \sum S^{-1}(\alpha \trr x) \beta .$$

## Braided Hopf algebra structure for $\tUqv$ {#sec:braid-hopf-algebra}

Unlike $\tUq$, the even part $\tUqv$ of $\tUq$ does not inherit a Hopf algebra structure from $U_h$. However, we have the following.

::: theorem
[]{#thm:26 label="thm:26"} The braided Hopf algebra structure of $\bUh$ induces a braided Hopf algebra structure with invertible antipode for $\tUqv$. In other words, for $$f\in \{\psi ,\psi ^{-1},\mu ,\eta ,\bD,\epsilon ,\bS,\bS^{-1}\}$$ with $f\zzzcolon U_h^{\ho i}\rightarrow U_h^{\ho j}$ ($i,j\ge 0$) we have $$f((\tUqv)^{\tO i})\subset (\tUqv)^{\tO j},$$ and the induced map $f\zzzcolon (\tUqv)^{\tO i}\rightarrow (\tUqv)^{\tO j}$ is continuous.
:::

::: corollary
[]{#thm:20 label="thm:20"} Suppose that $f\zzzcolon U_h^{\ho i}\rightarrow U_h^{\ho j}$, $i,j\ge 0$, is a $\modQ [[h]]$-module homomorphism obtained from finitely many copies of $$\begin{gathered}
    1_{U_h}\zzzcolon U_h\rightarrow U_h,\quad \psi ^{\pm 1}\zzzcolon U_h^{\ho2}\rightarrow U_h^{\ho2},\quad
    \mu \zzzcolon U_h^{\ho2}\rightarrow U_h,\quad \eta \zzzcolon \modQ [[h]]\rightarrow U_h,\\
    \bD\zzzcolon U_h\rightarrow U_h^{\ho2},\quad \epsilon \zzzcolon U_h\rightarrow \modQ [[h]],\quad
    \bS^{\pm 1}\zzzcolon U_h\rightarrow U_h
  
\end{gathered}$$ by taking iterated tensor products and compositions. Then we have $$f(\tUqvx i)\subset \tUqvx j.$$
:::

Theorem [\[thm:26\]](#thm:26){reference-type="ref" reference="thm:26"} follows immediately from the following.

::: proposition
[]{#r51 label="r51"} If $f\in \{\psi ,\psi ^{-1},\mu ,\eta ,\epsilon ,\bS,\bS^{-1}\}$ with $f\zzzcolon U_h^{\ho
  i}\rightarrow U_h^{\ho j}$ ($i,j\ge 0$), then we have $$f(\modF _p(\tUqvx i))\subset \modF _p(\tUqvx j)$$ for $p\ge 0$. Moreover, we have $$\label{eq:39}
    \bD(\modF _p(\tUqv))\subset \modF _{\floor{\frac{p+1}2}}(\tUqvx2)$$ for $p\ge 0$.
:::

::: proof
*Proof.* The assertion is obvious for $f=\mu ,\eta ,\epsilon$.

The case $f=\psi ^{\pm 1}$ follows from the following formulas $$\begin{gathered}
  \psi (x\otimes y)
  =\sum_{n=0}^\infty  q^{-\hf n(n+1)+(|x|-n)|y|}
  (e^n\trr y)\otimes (\tF^{(n)}\trr x),\\
  \psi ^{-1}(x\otimes y)
  =\sum_{n=0}^\infty (-1)^n q^{-(|x|+n)|y|}
  (\tF^{(n)}\trr y)\otimes (e^n\trr x)
\end{gathered}$$ for homogeneous elements $x,y\in U_h$.

Consider the case $f=\bS^{\pm 1}$. Using [\[eq:27\]](#eq:27){reference-type="eqref" reference="eq:27"} and [\[eq:28\]](#eq:28){reference-type="eqref" reference="eq:28"}, we obtain $$\begin{gathered}
  \label{eq:16}
  \bS(x)=\sum_{n=0}^\infty q^{-\hf n(n+1)}
  e^nK^{|x|-n}S(\tF^{(n)}\trr x),\\
  \label{eq:17}
  \bS^{-1}(x)=\sum_{n=0}^\infty q^{\hf n(n-1)-n|x|}
  S^{-1}(\tF^{(n)}\trr x)K^{|x|-n}e^n.
\end{gathered}$$ Using these formulas, we see easily that $\bS(\modF _p(\tUqv))\subset \modF _p(\tUq)$. Hence, it remains to show that if $x,y\in \Uqv$ are homogeneous, then each term in [\[eq:16\]](#eq:16){reference-type="eqref" reference="eq:16"} and [\[eq:17\]](#eq:17){reference-type="eqref" reference="eq:17"} is contained in $\Uqv$. This follows, since for any homogeneous $x\in \Uqv$ we have $  K^{|x|}S^{\pm 1}(x)\in \Uqv$ by [\[eq:53\]](#eq:53){reference-type="eqref" reference="eq:53"} and [\[eq:55\]](#eq:55){reference-type="eqref" reference="eq:55"}.

Finally, we prove [\[eq:39\]](#eq:39){reference-type="eqref" reference="eq:39"}. By computation, $$\label{eq:18}
  \bD(x)
  =\sum_{n=0}^\infty (-1)^n q^{-n}
  x_{(1)}K^{-|x_{(2)}|}e^n\otimes (\tF^{(n)}\trr x_{(2)}),$$ where $\Delta (x)=\sum x_{(1)}\otimes x_{(2)}$. Using this formula, we easily see that $\bD(\modF _p(\tUqv))\subset \modF _{\floor{\frac{p+1}2}}(\tUq\otimes \tUqv)$. It suffices to show that if $x\in \Uqv$ is homogeneous, then each term in [\[eq:18\]](#eq:18){reference-type="eqref" reference="eq:18"} is contained in $\Uqvx2$. This follows, since we have $$\begin{gathered}
  \label{eq:22}
  \Delta (\Uqv)\subset \Uqv\otimes (\Uqv)_0+K\Uqv\otimes (\Uqv)_1,
\end{gathered}$$ where $(\Uqv)_0$ (resp. $(\Uqv)_1$) denotes the $\Zqq$-submodule of $\Uqv$ spanned by the homogeneous elements of even (resp. odd) degrees. The inclusion [\[eq:22\]](#eq:22){reference-type="eqref" reference="eq:22"} can be easily verified using [\[eq:53\]](#eq:53){reference-type="eqref" reference="eq:53"} and [\[eq:54\]](#eq:54){reference-type="eqref" reference="eq:54"}. ◻
:::

::: remark
[]{#r15 label="r15"} $\tUq$ also has a braided Hopf algebra structure inherited from that of $\bUh$, i.e., Theorem [\[thm:26\]](#thm:26){reference-type="ref" reference="thm:26"} holds if we replace $\tUqv$ with $\tUq$. Moreover, the $(\modZ /2\modZ )$-grading for $\tUq$ is compatible with the braided Hopf algebra structure: $$\begin{gathered}
    \psi ^{\pm 1}(K^i\tUqv\tO K^j\tUqv)\subset K^j\tUqv\tO K^i\tUqv,\\
    \bD(K^i\tUqv)\subset K^i\tUqv \tO K^i\tUqv,\quad
    \bS^{\pm 1}(K^i\tUqv)\subset K^i\tUqv,
  
\end{gathered}$$ for $i,j\in \{0,1\}$.
:::
