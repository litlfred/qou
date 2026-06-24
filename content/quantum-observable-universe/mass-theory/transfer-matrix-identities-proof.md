**(i)** Direct multiplication.  With $h = q - q^{-1}$:

$$
  \begin{pmatrix} h & 1 \\ 1 & 0 \end{pmatrix}
  \begin{pmatrix} 0 & 1 \\ 1 & -h \end{pmatrix}
  =
  \begin{pmatrix} h \cdot 0 + 1 \cdot 1 & h \cdot 1 + 1 \cdot (-h) \\
  1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot (-h) \end{pmatrix}
  =
  \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

The $(0,1)$ entry vanishes: $h + (-h) = 0$.
The reverse product $T_{nn} \cdot T_{pp}$ is identical by
the same computation.

This is the transfer matrix expression of the Hecke
relation: $T_{pp}$ encodes $\sigma$ (crossing coefficient
$d = 0$) and $T_{nn}$ encodes $\sigma^{-1}$ (coefficient
$d = -h$), so $T_{pp} \cdot T_{nn} = \sigma \cdot \sigma^{-1} = \mathbf{1}$.

**(ii)** Direct multiplication:

$$
  \begin{pmatrix} h/2 & 1 \\ 1 & -h/2 \end{pmatrix}^2
  =
  \begin{pmatrix} h^2/4 + 1 & 0 \\ 0 & 1 + h^2/4 \end{pmatrix}.
$$

The diagonal entries are $(h/2)(h/2) + 1 \cdot 1 = h^2/4 + 1$,
and the off-diagonals vanish: $(h/2)(1) + 1(-h/2) = 0$.  Then

$$
  1 + \frac{h^2}{4}
  = 1 + \frac{(q - q^{-1})^2}{4}
  = \frac{4 + q^2 - 2 + q^{-2}}{4}
  = \frac{(q + q^{-1})^2}{4}
  = \frac{[2]_q^2}{4}. \qquad\square
$$
