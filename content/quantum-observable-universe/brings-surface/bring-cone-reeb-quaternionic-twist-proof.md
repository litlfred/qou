**Proof.** The three operators are right-multiplications, so composing them
multiplies on the right in the opposite order: for $p \in \mathbb{H}$,

$$
  (M_y \circ M_x)(p) \;=\; (p\,x)\,y \;=\; p\,(xy).
$$

Hence

$$
  [M_x, M_y](p)
  \;=\; p\,(xy) - p\,(yx)
  \;=\; p\,(xy - yx).
$$

For distinct imaginary units the quaternion relations give $xy = -yx$ and
$xy = x \cdot y$ in the cyclic sense $\mathbf{i}\mathbf{j} = \mathbf{k}$,
$\mathbf{j}\mathbf{k} = \mathbf{i}$, $\mathbf{k}\mathbf{i} = \mathbf{j}$.
Therefore $xy - yx = 2(x \cdot y)$ and

$$
  [M_x, M_y](p) \;=\; 2\,p\,(x \cdot y) \;=\; 2\,M_{x \cdot y}(p).
$$

Taking $(x,y) = (\mathbf{i},\mathbf{j}), (\mathbf{j},\mathbf{k}),
(\mathbf{k},\mathbf{i})$ gives the three stated brackets. Right-multiplication
rather than left is what produces the $+2$ rather than $-2$; the same
computation with left multiplication yields the opposite sign.

Nothing in the argument uses an ordering, a radical, or any other archimedean
construct — only the quaternion multiplication table — so the Lean statement is
made over a generic commutative ring and specializes to $\mathbb{H} =
\mathrm{Quaternion}\,\mathbb{R}$ for the quaternionic-contact geometry.
$\blacksquare$
