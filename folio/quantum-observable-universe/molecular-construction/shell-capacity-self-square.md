**Proposition.**
*For every principal shell level $n \in \mathbb{N}$, the number of orbital sub-states is the sum of the sub-shell multiplicities $2\ell+1$ over $\ell = 0,\ldots,n-1$,*

$$
  \sum_{\ell=0}^{n-1} (2\ell+1) \;=\; n^2,
$$

*and the electron capacity of the shell, carrying the spin factor $2$, is*

$$
  \sum_{\ell=0}^{n-1} 2(2\ell+1) \;=\; 2n^2 .
$$

*Both are the $q\to 1$ value of the bar-even self-square $[n]_q^2$.*

This is the self-fusion of a single angular $q$-dimension, not a product of two independent symmetries. The angular $q$-dimension is the bar-even (cosh) Chebyshev evaluation $[n]_q = U_{n-1}\!\bigl((q+q^{-1})/2\bigr)$ of the shell element. The $q$-Clebsch–Gordan rule decomposes its self-square into the sub-shell multiplicities,

$$
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q
  \qquad\Longrightarrow\qquad
  2[n]_q^2\big|_{q=1} \;=\; 2n^2 ,
$$

since $[2\ell+1]_q\big|_{q=1} = 2\ell+1$. The $\mathrm{SO}(4)=\mathrm{SU}(2)\times\mathrm{SU}(2)$ "$(j,j)$ doubling" of the hydrogenic shell is here the self-square $V\otimes V$ of one object. The second factor is a copy of the first, tied by the coproduct. We require no second compact $\mathrm{SU}(2)$. The compact ($\cos/\sin$, root of unity) and non-compact ($\cosh/\sinh$, real $q$) forms are the two real forms of one $\mathfrak{sl}(2,\mathbb{C})$.

The $q=1$ integer identities above are proved (sum of the first $n$ odd numbers, by induction). The full $q$-deformed self-square, cleared of the denominator $(q - q^{-1})$, is a polynomial identity proved for every $n$; see [The shell state space is the self-square of the angular object](#conj:shell-space-is-self-square). The residual modeling assumption — that the electron shell space is this self-square, rather than the count merely agreeing with it — is recorded as structural input.

| Shell $n$ | $n^2$ | Capacity $2n^2$ | Sub-shells $[2\ell+1]_{q=1}$ |
|:----------|:------|:----------------|:-----------------------------|
| 1 | 1 | 2 | 1 |
| 2 | 4 | 8 | 1 + 3 |
| 3 | 9 | 18 | 1 + 3 + 5 |
| 4 | 16 | 32 | 1 + 3 + 5 + 7 |
