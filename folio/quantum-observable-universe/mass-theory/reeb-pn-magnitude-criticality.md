*Let $R$ be a commutative ring, $v \in R$ invertible, $[2]_v = v + v^{-1}$,
and let*

```tex
\begin{align*}
  M(b) &= \begin{pmatrix} 1 & b \\ b & -1 \end{pmatrix},
  &S(a,w) &= \begin{pmatrix}
     0 & a & w & w\\
     a & 0 & w & w\\
     w & w & 0 & -a\\
     w & w & -a & 0
  \end{pmatrix}
\end{align*}
```

*denote the symmetric-sector exchange matrix and the uniform-magnitude
$[1^4]$ complete-graph exchange matrix on nucleon blocks $[p,p,n,n]$. Then:*

1. *(Deformation identity)* $5 + (v - v^{-1})^2 = 1 + [2]_v^2$.
2. *(Cayley–Hamilton form)* $M(b)^2 = (1 + b^2)\cdot\mathbf{1}$; in
   particular the classical $b = 2$ gives the scalar $5$.
3. *(Marginal stability)* $\det\bigl(\mathbf{1} + g\,M(b)\bigr)
   = 1 - g^2(1+b^2)$ for every $b$; hence, specializing to the deformed
   pn-degree $b = [2]_v$, any $g$ with $g^2(1 + [2]_v^2) = 1$ is exactly
   the point where the deformed symmetric-sector determinant
   $\det\bigl(\mathbf{1} + g\,M([2]_v)\bigr)$ vanishes.
4. *(pn-sign blindness)* With $D = \mathrm{diag}(1,1,-1,-1)$ one has
   $D\,S(a,w)\,D = S(a,-w)$, and consequently
   $\det(\mathbf{1} + S(a,w)) = \det(\mathbf{1} + S(a,-w))$ and
   $\mathrm{tr}\bigl(T\,S(a,w)^k\bigr) = \mathrm{tr}\bigl(T\,S(a,-w)^k\bigr)$
   for every $k$ and every $T$ commuting with $D$.

*In particular the magnitude $g$ with $g^2(1+[2]_v^2) = 1$ equals
$z/\sqrt{1+z^2}$ evaluated at the Markov bond factor $z = 1/[2]_v$ whenever
square roots are available, and satisfies
$g^2\,(5 + (v-v^{-1})^2) = 1$ by item 1.*

## Scope

The proposition is pure exchange-matrix algebra; it carries no physical
identification. The physical reading of $g$ as the pn-bond linking
amplitude is the separate [CWF linking normalization conjecture](reeb-linking-cwf-normalization.md).
Item 4 implies the $[1^4]$ pn writhe sign is invisible to every
grading-commuting observable class; sign sensitivity requires $p{\leftrightarrow}n$
mixing operators.
