The three typed transfer matrices satisfy two exact
identities in $\mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$.

## Statement

**Proposition.**

**(i)** $T_{pp} \cdot T_{nn} = T_{nn} \cdot T_{pp} = I$.

**(ii)** $T_{pn}^2 = \dfrac{[2]_q^2}{4} \cdot I$, where
$[2]_q = q + q^{-1}$.

## Proof

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

## Corollaries

**Nuclear binding from mixed crossings only.**
Identity (i) means that adjacent $pp$ and $nn$ crossings
cancel in the transfer matrix chain.  In the interleaved
ground-state ordering, $pp$ crossings (from proton-proton
pairs) and $nn$ crossings (from neutron-neutron pairs)
contribute zero net effect.  All nuclear binding energy
arises from the **mixed** ($pn$) crossings, whose transfer
matrix $T_{pn}$ has trace $0$ and determinant
$-(1 + h^2/4)$.

**Scalar pairing from mixed crossings.**
Identity (ii) means that every pair of mixed crossings
produces a **scalar** (proportional to $I$).  The binding
strength per pair is $[2]_q^2/4 = (q + q^{-1})^2/4$,
which is the square of half the quantum $2$-integer.
At $q_0$: $[2]_q^2/4 \approx 1.011$.
