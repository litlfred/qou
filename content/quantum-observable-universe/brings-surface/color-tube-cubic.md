At fixed $z \in \mathbb{P}^1(\mathbb{C})$, the three color roots of the
elliptic cubic ([color elliptic curve](#prop:color-elliptic)) each satisfy the cubic in
the color tube coordinate $\mathbf{c} \in \{\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z\}$
obtained by substituting $X = \mathbf{c} + z$
into the color elliptic equation.  Expanding gives the
*color tube cubic*:

```tex
\begin{equation}\label{eq:color-tube-cubic}
  \mathbf{c}^3 + (4z+1)\mathbf{c}^2 + (6z^2+3z+1)\mathbf{c}
  + (4z^3+3z^2+2z+1) =  0.
\end{equation}
```

This polynomial lies in $\mathbb{Z}[z][\mathbf{c}]$ and defines a
variety over $\mathbb{Z}$.  The leading $z$-coefficients $4, 6, 4$
equal $\binom{4}{1}$, $\binom{4}{2}$, $\binom{4}{3}$, and the
constant term satisfies

$$
  4z^3 + 3z^2 + 2z + 1 =  \frac{d}{dz}(z^4 + z^3 + z^2 + z).
$$

Vieta's formulas for the three roots give:

```tex
\begin{align}
  \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z
    &=  -(4z+1),
    \label{eq:vieta-sum}\\[4pt]
  \mathbf{r}_z\mathbf{g}_z + \mathbf{r}_z\mathbf{b}_z
    + \mathbf{g}_z\mathbf{b}_z
    &=  6z^2+3z+1,
    \label{eq:vieta-pairs}\\[4pt]
  \mathbf{r}_z\mathbf{g}_z\mathbf{b}_z
    &=  -(4z^3+3z^2+2z+1).
    \label{eq:vieta-product}
\end{align}
```
