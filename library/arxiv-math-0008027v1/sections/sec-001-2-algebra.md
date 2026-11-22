---
doc_id: arxiv-math-0008027v1
doc_title: "arXiv:math/0008027v1 [math.GT] 3 Aug 2000"
section_id: sec-001-2-algebra
section_title: "Algebra"
section_number: 2
pages: 2-4
source_pdf: 0008027v1.pdf
source_sha256: 8bce0b8a1bca372e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.979
doc_brief: "arXiv:math/0008027v1 [math.GT] 3 Aug 2000 — I follow Y."
---
[]{#sec:algebra label="sec:algebra"} In this section I describe Kashaev's link invariant [@Kashaev:MODPLA95] following Yokota. We fix an integer $N\ge2$ and put $q=\exp\left(2\pi\sqrt{-1}/N\right)$. Put $(x)_n=\prod_{k=1}^{n}(1-x^k)$ for $n\ge 0$. For integers $0{\le}k,l,m,n{\le}N-1$ we put $$\theta\!\left(\begin{smallmatrix} k & n \\ l & m \end{smallmatrix}\right)
  =
  \begin{cases}
    1\;&\text{if ${l}\ne{m}$ and $q^{k},q^{l},q^{m},q^{n}$ are on the unit
    circle counterclockwise}
    \\
    &\hfill\text{(other pairs may be the same)},
    \\
    0\;&\text{otherwise}.
  \end{cases}$$ Note that $\theta\!\left(\begin{smallmatrix} k & n \\ l & m \end{smallmatrix}\right)=1$ if and only if $${k}\le{l}<{m}\le{n},\quad
  {n}\le{k}\le{l}<{m},\quad
  {m}\le{n}\le{k}\le{l}\;(m<l),\;\text{or}\quad
  {l}<{m}\le{n}\le{k}.$$ For an integer $x$, we denote by $[x]\in\{0,1,2,\dots,N-1\}$ the residue modulo $N$.

Now Kashaev's $R$-matrix $R=\left(R_{l,m}^{k,n}\right)$ is an $N^2\times N^2$-matrix given by $$\begin{aligned}
  R_{l,m}^{k,n}
  =
  \frac
  {Nq^{1-(l-n+1)(m-k)}
  \theta\!\left(\begin{smallmatrix} k & n \\ l & m \end{smallmatrix}\right)}
  {(q)_{[m-l-1]}(q^{-1})_{[n-m]}(q)_{[k-n]}(q^{-1})_{[l-k]}}
  \\ \intertext{and}
  \left(R^{-1}\right)_{l,m}^{k,n}
  =
  \frac
  {Nq^{-1+(m-k-1)(l-n)}
  \theta\!\left(\begin{smallmatrix} k & n \\ l & m \end{smallmatrix}\right)}
  {(q^{-1})_{[m-l-1]}(q)_{[n-m]}(q^{-1})_{[k-n]}(q)_{[l-k]}}.
\end{aligned}$$ Let $\mu$ be an $N\times N$-matrix with $\mu_l^k=-\delta_{k,l+1}q^{1/2}$, where $\delta_{i,j}$ is Kronecker's delta. Then $(R,\mu,-q^{1/2},1)$ is an enhanced Yang--Baxter operator [@Turaev:INVEM88], i.e. the following equalities hold. (See [@Murakami/Murakami:volume] for a proof.)

::: prop
$$\begin{gathered}
    \left({R}\otimes{id}_{\mathbb{C}^N}\right)
    \left({id}_{\mathbb{C}^N}\otimes{R}\right)
    \left({R}\otimes{id}_{\mathbb{C}^N}\right)
    =
    \left({id}_{\mathbb{C}^N}\otimes{R}\right)
    \left({R}\otimes{id}_{\mathbb{C}^N}\right)
    \left({id}_{\mathbb{C}^N}\otimes{R}\right),
    \\
    \left(\mu\otimes\mu\right)R=R\left(\mu\otimes\mu\right),
    \\
    \sum_{m=0}^{N-1}\left(R^{\pm1}({id}_{\mathbb{C}^N}\otimes\mu)\right)_{lm}^{km}
    =\left(-q^{1/2}\right)^{\pm1}\delta_{k,l}
  
\end{gathered}$$ with ${id}_{\mathbb{C}^N}$ the identity on $\mathbb{C}^N$.
:::

Now I will describe how to calculate Kashaev's invariant for knots using this enhanced Yang-Baxter operator.

First we present a knot in a $(1,1)$-tangle formula so that the string comes from above and goes down and at each crossing both arcs also go down. We decompose the string into edges so that at each crossing four edges meet and at each maximum/minimum where the string go from the left to the right two edges meet. See Figure [1](#fig:label){reference-type="ref" reference="fig:label"} for example. A *labeling* is an assignment of an element in $\{0,1,2,\dots,N-1\}$ to each edge. Here we assign $0$ to the edge from the starting point and to the edge to the end point. We call the number assigned to an edge its label. Given a labeling we assign the following quantities to crossings and maxima/minima: $$\raisebox{-5mm}{\begin{picture}(10,10)
  \put(10,10){\vector(-1,-1){10}}
  \put( 6, 4){\vector( 1,-1){ 4}}
  \put( 4, 6){\line(-1, 1){ 4}}
  \put( 0,10){\makebox(0,0)[br]{$k$}}\put(10,10){\makebox(0,0)[bl]{$n$}}
  \put( 0, 0){\makebox(0,0)[tr]{$l$}}\put(10, 0){\makebox(0,0)[tl]{$m$}}
\end{picture}}
\, :\,R_{lm}^{kn},\qquad
\raisebox{-5mm}{\begin{picture}(10,10)
  \put( 0,10){\vector( 1,-1){10}}
  \put(10,10){\line(-1,-1){ 4}}
  \put( 4, 4){\vector(-1,-1){ 4}}
  \put( 0,10){\makebox(0,0)[br]{$k$}}\put(10,10){\makebox(0,0)[bl]{$n$}}
  \put( 0, 0){\makebox(0,0)[tr]{$l$}}\put(10, 0){\makebox(0,0)[tl]{$m$}}
\end{picture}}
\, :\,\left(R^{-1}\right)_{lm}^{kn},\qquad
\raisebox{-2.5mm}{\begin{picture}(10,5)
  \qbezier(0,5)(0,0)(5,0)
  \qbezier(5,0)(10,0)(10,5)
  \put(5,-1){\line(0,1){2}}
  \put(9,5.5){\vector(0,1){0}}
  \put(1,1){\makebox(0,0)[tr]{$k$}}
  \put(9,1){\makebox(0,0)[tl]{$l$}}
\end{picture}}
\, :\,\mu_{l}^{k},\qquad
\raisebox{-2.5mm}{\begin{picture}(10,5)
  \qbezier(0,0)(0,5)(5,5)
  \qbezier(5,5)(10,5)(10,0)
  \put(5,4){\line(0,1){2}}
  \put(10.1,-0.5){\vector(0,-1){0}}
  \put(1,4){\makebox(0,0)[br]{$k$}}
  \put(9,4){\makebox(0,0)[bl]{$l$}}
\end{picture}}
\,:\,\left(\mu^{-1}\right)_{l}^{k}.$$

The *weight* for a labeling is the product of all the quantities above. Then the Kashaev invariant $\langle{K}\rangle_N$ of a knot $K$ is defined to be the sum of all the weights up to some power of $q$ (which does not matter in our case), where the summation runs over all the labelings.

If four edges meeting at a crossing are labeled $k$, $l$, $m$ and $n$ as above, we call $[n-m]$, $[k-n]$, $[l-k]$ and $[m-l-1]$ the angles between the adjacent edges. Then we have the following proposition.

::: prop
[]{#prop:angle label="prop:angle"} The weight for a labeling vanishes unless all of the following conditions are satisfied. For a proof see [@Yokota:volume].

1.  the sum of the angles around any crossing is $N-1$.

2.  the sum of the angles contained in any bounded region is $N-1$.

3.  any angle in any of the two unbounded regions is zero.
:::

We will calculate the Kashaev invariant for the figure-eight knot.

From Proposition [\[prop:angle\]](#prop:angle){reference-type="ref" reference="prop:angle"} (3), we can assume that labels are as in Figure [1](#fig:label){reference-type="ref" reference="fig:label"}.

![Figure-eight knot with a labeling.](fig8_2.eps){#fig:label}

Then the Kashaev invariant $\langle{4_1}\rangle_{N}$ is $$\begin{aligned}
  &\sum_{j=0}^{N-1}\sum_{k\in[0,j-1]}\sum_{i\in[1,j]}
  \left(R^{-1}\right)_{0,i}^{0,0}\left(R^{-1}\right)_{0,1}^{j,i}
  R_{N-1,0}^{\phantom{N}k\phantom{1},0}R_{k,j}^{0,0}
  \left(\mu^{-1}\right)_{N-1}^{0}
  \mu_{1}^{0}
  \\
  &=
  N^4\sum_{j=0}^{N-1}\sum_{k\in[0,j-1]}\sum_{i\in[1,j]}
  \frac{q^{-1}}{(q^{-1})_{[i-1]}(q)_{[-i]}}\times
  \frac{q^{-1+(-j)(-i)}}{(q)_{[i-1]}(q^{-1})_{[j-i]}(q)_{[-j]}}
  \\
  &\phantom{N^4\sum_{j=0}^{N-1}\sum_{k\in[0,j-1]}\sum_{i\in[1,j]}}\times
  \frac{q^{1-(N)(-k)}}{(q)_{[k]}(q^{-1})_{[-k-1]}}\times
  \frac{q^{1-(k+1)j}}{(q)_{[j-k-1]}(q^{-1})_{[-j]}(q^{-1})_{[k]}}
  \\
  &=
  N^2\sum_{j=0}^{N-1}
  \frac{q^{-j}}{(q)_{[-j]}(q^{-1})_{[-j]}}
  \sum_{k\in[0,j-1]}
  \frac{q^{-kj}}
       {(q)_{[j-k-1]}(q^{-1})_{[k]}}
  \sum_{i\in[1,j]}
  \frac{q^{ij}}
       {(q)_{[i-1]}(q^{-1})_{[j-i]}}
\end{aligned}$$ up to some power of $q$, since $(q^{-1})_{[i-1]}(q)_{[-i]}=(q^{-1})_{i-1}(q)_{N-i}
=\dfrac{N}{(q)_{N-i}}(q)_{N-i}=N$ and $(q)_{[k]}(q^{-1})_{[-k-1]}=(q)_{k}\dfrac{N}{(q)_{k}}=N$. Here $a\in[b,c]$ means that $q^{b}$, $q^{a}$, and $q^{c}$ are on the unit circle counterclockwise (any pair may be the same). Note that $a\in[b,c]$ if and only if $[a-b]+[c-a]=[c-b]$.

From the lemma below we have $$\begin{aligned}
  \langle{4_1}\rangle_{N}
  &=
  N^2\sum_{j=0}^{N-1}
  \frac{(-1)^{[j-1]}q^{-j-([j-1]+1)([j-1]-2j)/2}}{(q)_{[-j]}(q^{-1})_{[-j]}}
  \sum_{k\in[0,j-1]}
  \frac{q^{-kj}}
       {(q)_{[j-k-1]}(q^{-1})_{[k]}}
  \\
  &=
  N^2\sum_{j=0}^{N-1}
  \frac{1}{(q)_{[-j]}(q^{-1})_{[-j]}}
  \\
  &=
  \sum_{j=0}^{N-1}(q)_{[N-1+j]}(q^{-1})_{[N-1+j]}
  \\
  &=
  \sum_{j=0}^{N-1}(q)_{j}(q^{-1})_{j}.
\end{aligned}$$ Note that the final formula coincides with Kashaev's [@Kashaev:LETMP97 (2.2)].

The following lemma is a key to reduce the summations of the Kashaev's invariant.

::: lem
Let $0\le{k},{l},{m}\le{N-1}$ be integers. Then $$\sum_{k\in[l,m]}
  \frac{q^{-(m-l+1)k}}{(q)_{[m-k]}(q^{-1})_{[k-l]}}
  =
  (-1)^{[m-l]}q^{([m-l]+1)([m-l]-2m)/2}.$$
:::

::: proof
*Proof.* We use the following equality [@Murakami/Murakami:volume Lemma 3.2]. $$\begin{split}
  &\sum_{i=0}^{N-1-\alpha}
  \frac{q^{(\beta-\alpha)i/2}}{(q)_{i}(q^{-1})_{N-1-\alpha-i}}
  \\
  &\quad=\frac{(-1)^{N-1-\alpha}q^{-N(N-1)/2-\beta(\alpha+1)/2}}{N}
   \frac{(q)_{\alpha}(q)_{N-1-\alpha+[(\alpha-\beta)/2]}}
        {(q)_{[(\alpha-\beta)/2]}}.
\end{split}$$

To prove the lemma, we put $\beta=-\alpha$. Then we have $$\sum_{i=0}^{N-1-\alpha}
  \frac{q^{-\alpha i}}{(q)_{i}(q^{-1})_{N-\alpha-i-1}}
  =
  (-1)^{N-1-\alpha}q^{-N(N-1)/2+\alpha(\alpha+1)/2}.$$ Putting $i=[m-k]$ and $N-\alpha-1=[m-l]$, the conclusion follows. ◻
:::
