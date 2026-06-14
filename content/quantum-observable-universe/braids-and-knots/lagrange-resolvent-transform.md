*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $C_n$ act on a vector space $V$ of dimension $n$ with
coordinates $x_0, \ldots, x_{n-1}$, and let
$\zeta = e^{2\pi i/n}$.  The **Lagrange resolvent transform**
(discrete Fourier transform on $C_n$) is

$$
  w_k =  \frac{1}{\sqrt{n}}\sum_{j=0}^{n-1}\zeta^{kj}x_j,
  \qquad k \in \{0, \ldots, n-1\}.
$$

Then:

1. The cyclic permutation $\sigma \colon x_j \mapsto x_{j+1}$
   acts diagonally: $\sigma(w_k) = \zeta^{-k} w_k$.  The
   $C_n$ symmetry is manifest as phase rotation of the
   Fourier modes.

2. Any $C_n$-invariant polynomial constraint on the $x_j$
   transforms to a constraint on $C_n$-equivariant
   combinations of the $w_k$ (products pairing $w_k$ with
   $w_{n-k}$, i.e.\ conjugate modes).

For $n = 5$ (the case relevant to
[Bring's surface](#def:brings-surface)), the three power-sum
constraints transform to: $w_0 = 0$ (linear projection),
$w_1 w_4 + w_2 w_3 = 0$ (Hermitian quadric), and
$w_1^2 w_3 + w_4^2 w_2 + w_2^2 w_1 + w_3^2 w_4 = 0$
(symmetric cubic).


**Mathematical Novelty:** While using a Discrete Fourier Transform (DFT) to diagonalize a cyclic action is standard, the explicit $n=5$ Bring-surface formalization with the modular zeta-power reduction is a non-trivial mathematical contribution. (Note that the quadric/cubic constraint transforms mentioned in the examples are stated as part of the framework but not fully formalized).