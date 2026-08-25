**Remark.**

The shell capacity $2n^2$ was for a period recorded here as an open problem requiring an $\mathrm{SO}(4)$-type accidental degeneracy to bundle the angular-momentum levels $\ell = 0,\ldots,n-1$ into a single principal shell. That framing is withdrawn. The count is obtained in [`prop:shell-capacity-self-square`](#prop:shell-capacity-self-square) from the self-fusion of one angular object, and the mechanism it attributed the count to is not the one at work.

The classical route to $2n^2$ runs through the Runge–Lenz vector: the hydrogenic bound-state symmetry enlarges from $\mathrm{SO}(3)$ to $\mathrm{SO}(4) = \mathrm{SU}(2)\times\mathrm{SU}(2)$, and the shell is the $(j,j)$ representation of dimension $(2j+1)^2 = n^2$. The doubling is a product of two commuting factors, and asking which second compact $\mathrm{SU}(2)$ supplies the second factor is the natural question in that setting.

In the present framework the doubling is not a product of two symmetries. The shell-$n$ object is one Chebyshev element $U_{n-1}$, whose bar-even evaluation at $(q + q^{-1})/2$ is the angular $q$-dimension $[n]_q$ and whose bar-odd evaluation at $(q - q^{-1})/2$ is the radial tower. Its self-fusion $V \otimes V$ supplies the second factor as a copy of the first, tied by the coproduct, and $q$-Clebsch–Gordan then returns the sub-shells:

$$
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q ,
  \qquad
  2[n]_q^2\big|_{q=1} \;=\; 2n^2 .
$$

The compact ($\cos/\sin$, root of unity) and non-compact ($\cosh/\sinh$, real $q$) forms are the two real forms of one $\mathfrak{sl}(2,\mathbb{C})$, unified by the complex volume. No second compact $\mathrm{SU}(2)$ is required, and none is postulated.

What survives as open is narrower, and is stated separately as [`conj:shell-space-is-self-square`](#conj:shell-space-is-self-square): that the shell state space *is* the self-square, rather than carrying a dimension that happens to agree with it. The remaining shell-structure gap, the ordering of subshells beyond the capacity count, is a separate matter and is not addressed by either block.
