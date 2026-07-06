*Lean sibling resolves to [`QOU.Molecular.shell_capacity_self_square`](lean/QOU/Molecular/ShellCapacitySelfSquare.lean) — a sorry-free formalisation. The combinatorial content is over $\mathbb{N}$; the $q$-deformation is the bar-even Chebyshev evaluation, specialised here at $q=1$.*

**Proposition.**
*For every principal shell level $n \in \mathbb{N}$, the number of orbital sub-states equals the sum of the sub-shell multiplicities $2\ell+1$ over $\ell = 0,\ldots,n-1$:*

$$
  \sum_{\ell=0}^{n-1} (2\ell+1) \;=\; n^2.
$$

*The electron capacity of the shell, incorporating the spin factor $2$, is:*

$$
  \sum_{\ell=0}^{n-1} 2(2\ell+1) \;=\; 2n^2 .
$$

*Both expressions evaluate the $q\to 1$ limit of the bar-even self-square $[n]_q^2$.*

This identity reflects the self-fusion of a single angular $q$-dimension, not a product of two independent symmetries. The angular $q$-dimension is the bar-even (cosh) Chebyshev evaluation $[n]_q = U_{n-1}\!\bigl((q+q^{-1})/2\bigr)$ of the shell element. The $q$-Clebsch–Gordan rule decomposes its self-square into sub-shell multiplicities:

$$
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q
  \qquad\Longrightarrow\qquad
  2[n]_q^2\big|_{q=1} \;=\; 2n^2 ,
$$

since $[2\ell+1]_q\big|_{q=1} = 2\ell+1$. The standard $\mathrm{SO}(4)=\mathrm{SU}(2)\times \mathrm{SU}(2)$ doubling of the hydrogenic shell emerges here as the self-square $V\otimes V$ of a single object. The coproduct provides the second factor. No second compact $\mathrm{SU}(2)$ is required. The compact and non-compact forms realise the two real forms of one $\mathfrak{sl}(2,\mathbb{C})$.

The $q=1$ integer identities are proved in Lean via induction. The full $q$-deformed self-square is verified symbolically in `computations/shell_capacity_chebyshev_bridge.py`. We explicitly record the structural assumption that the electron shell space arises from this self-square operation.

| Shell $n$ | $n^2$ | Capacity $2n^2$ | Sub-shells $[2\ell+1]_{q=1}$ |
|:----------|:------|:----------------|:-----------------------------|
| 1 | 1 | 2 | 1 |
| 2 | 4 | 8 | 1 + 3 |
| 3 | 9 | 18 | 1 + 3 + 5 |
| 4 | 16 | 32 | 1 + 3 + 5 + 7 |
