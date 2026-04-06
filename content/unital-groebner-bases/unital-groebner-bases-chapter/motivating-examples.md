Let $k$ be a (commutative) field with unity.

1. Let $A$ be the polynomial algebra $k[x_1, \ldots, x_n]$ and
   consider the ideal $\mathfrak{m} = (x_1, \ldots, x_n)$. Taking a
   graded lexicographic ordering on $A$ with $x_i < x_j$ if $i < j$,
   $\mathfrak{m}^2$ has a Gröbner--Shirshov basis given by $\{x_i x_j\}$.
   Thus the quotient $A/\mathfrak{m}^2$ is an $(n+1)$-dimensional
   $k$-vector space with basis:

   $$
     A/\mathfrak{m}^2 = k\{1, x_1, \ldots, x_n\}.
   $$

2. If $\mathfrak{g}$ is a Lie algebra with bracket
   $[\,{,}\,]_{\mathfrak{g}}$ over $k$, then one forms the universal
   enveloping algebra $U\mathfrak{g}$ as the quotient of the tensor
   (free) algebra $T\mathfrak{g}$ by the two-sided ideal

   $$
     J = \bigl(xy - yx - [x,y]_{\mathfrak{g}}
       \;\big|\; x, y \in \mathfrak{g} \hookrightarrow T\mathfrak{g}\bigr).
   $$

   Choosing a total ordering $<$ on an index set $I$ for a $k$-basis
   $\mathfrak{g} = k\langle x_i \mid i \in I\rangle$, a Gröbner--Shirshov
   basis argument yields the Poincaré--Birkhoff--Witt (PBW) theorem:
   $U\mathfrak{g}$ has a basis of non-decreasing words.

In both cases, the fact that $k$ is a field is not essential — similar
statements hold over $\mathbb{Z}$, though not via classical Gröbner--Shirshov
basis techniques.
