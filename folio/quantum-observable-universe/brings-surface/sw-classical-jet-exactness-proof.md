The fibre coordinate $X$ is a meromorphic function on $\Sigma$, and the total derivative along the curve of a meromorphic function is meromorphic (at a ramification point with local coordinate $t$, where $z = z_c + t^2$, the first jet acquires a pole: $X^{(1)} = \frac{dX/dt}{dz/dt}$; higher jets acquire poles of higher order). Hence each $X^{(n-1)}$, $n \ge 1$, is a meromorphic function on $\Sigma$, and

$$
\lambda_{\mathrm{SW}}^{(n)} \;=\; X^{(n)}\,dz \;=\; \frac{d}{dz}\bigl(X^{(n-1)}\bigr)\,dz \;=\; d\bigl(X^{(n-1)}\bigr)
$$

is exact.

Exactness kills residues: in a local coordinate $t$ at any $p \in \Sigma$, write $X^{(n-1)} = \sum_k c_k t^k$ with finite principal part; then $d(X^{(n-1)}) = \sum_k k\,c_k\,t^{k-1}\,dt$ contains no $t^{-1}\,dt$ term (the $k = 0$ term differentiates to zero and every other term lands away from $t^{-1}$), so $\mathrm{Res}_p\,\lambda_{\mathrm{SW}}^{(n)} = 0$. Exactness kills periods: $\oint_\gamma d(X^{(n-1)}) = 0$ for every closed cycle $\gamma$ avoiding the poles of $X^{(n-1)}$, by Stokes' theorem on the curve. The residue-sum period of [SW period residue sum](#prop:sw-period-residue-sum) is $2\pi i$ times a sum of these vanishing residues, hence zero at every vertical degree $n \ge 1$.

The final claim follows because the classical binding period is nonzero: at $q = 1$, $a_D^{(m)} = \mathrm{lw}(m-1) = I(m)/m > 0$ with $I(m)$ the involution numbers, and a vanishing period cannot equal a nonzero number. The $t^{-1}$ coefficient of a termwise derivative vanishes over a generic commutative ring, and composing this with the residue-sum formula yields the non-realisability of the nonzero binding periods under classical-jet prolongation. $\qquad\blacksquare$
