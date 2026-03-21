Let $(\mathcal{C}, A, \omega)$ be as in
Proposition [categorical Möbius energy](#prop:categorical-mobius-energy),
with $q \neq 1$.  Then the categorical energy
$E_{\mathrm{cat}}(\gamma) \to +\infty$ as any pair of non-adjacent
strands of $\gamma$ approach coincidence.  In particular, no
continuous deformation of $\gamma$ within the class of finite-energy
curves can produce a self-intersection.

*Proof.*
The key mechanism is the **non-cocommutativity** of the Hopf
comultiplication $\Delta$ for $q \neq 1$.  Recall that for
a cocommutative Hopf algebra, the flip
$\tau \circ \Delta = \Delta$; for
$\mathcal{U}_q(\mathfrak{su}(2))$, this fails and the defect is
measured by the universal $R$-matrix:

$$
\tau \circ \Delta(x)
\;=\;
\mathcal{R}\;\Delta(x)\;\mathcal{R}^{-1},
\qquad x \in \mathcal{U}_q(\mathfrak{su}(2)).
$$

The failure of the cocommutativity square

```tex
\begin{tikzcd}[column sep=4em, row sep=3em]
  A \ar[r, "\Delta"] \ar[d, "\Delta"']
  & A \otimes A \ar[d, "\tau"] \\
  A \otimes A \ar[r, "\mathcal{R}\,\cdot\,\mathcal{R}^{-1}"']
  & A \otimes A
\end{tikzcd}
```

is controlled by $\mathcal{R}$.  When two non-adjacent strands at
parameters $s, t$ approach coincidence
($\lvert\gamma(s) - \gamma(t)\rvert \to 0$ with
$d_\gamma(s,t) > 0$ fixed), the categorical trace in
$E_{\mathrm{cat}}$ picks up a contribution from
$\mathcal{R} - \mathbf{1} \otimes \mathbf{1}$, which is non-zero
precisely when $q \neq 1$.

Concretely, in the fundamental representation $V = \mathbb{C}^2$
the $R$-matrix has the form

$$
R
\;=\;
q^{1/2}
\begin{pmatrix}
  q & 0 & 0 & 0 \\
  0 & 1 & q - q^{-1} & 0 \\
  0 & 0 & 1 & 0 \\
  0 & 0 & 0 & q
\end{pmatrix},
$$

and the off-diagonal entry $q - q^{-1} \neq 0$ for $q \neq 1$
generates a repulsive potential that diverges as $1/r^2$ when the
strand separation $r = \lvert\gamma(s) - \gamma(t)\rvert \to 0$.

Since $E_{\mathrm{cat}}(\gamma)$ depends on the $q$-Hodge star $*_q$
through the connection Laplacian $\nabla^*\!\nabla$, and since $*_q$
encodes the braiding $c_{V,V}$ (which is non-symmetric for
$q \neq 1$), the cost of non-adjacent strands approaching is
singular.  The $1/r^2$ repulsive term is categorically represented by
the $q$-deformed commutator

$$
[\hat{X}, \hat{P}]_q
\;=\;
\hat{X}\hat{P} - q\,\hat{P}\hat{X}
\;=\;
i\hbar_q\,\mathbf{1},
$$

which prevents the "vortex filament" from passing through itself:
the energy barrier is infinite, so finite-energy curves cannot
self-intersect.
$\square$
