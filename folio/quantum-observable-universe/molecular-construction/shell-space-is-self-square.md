**Conjecture.**
*Write $V_j$ for the $\mathrm{SU}(2)_q$ irrep of spin $j$, of $q$-dimension $[2j+1]_q$, and let* $j_n = (n-1)/2$ *be the spin of the* **angular object** *of principal shell $n$, so that $\dim_q V_{j_n} = [n]_q$. Then the orbital state space of shell $n$ is the* **self-fusion** *of that one object with itself,*

$$
  \mathcal{O}_n \;\cong\; V_{j_n} \otimes V_{j_n} ,
$$

*the second tensor factor being a copy of the first, tied to it by the coproduct. In particular $\dim_q \mathcal{O}_n = [n]_q^2$.*

The spin labelling is the one used in the [normal-bundle orbital-space conjecture](#conj:orbital-space-normal-bundle): $V_\ell$ there is the sub-shell irrep of dimension $2\ell+1$, which is $V_j$ here at integer $j = \ell$.

This is the one step of the $2n^2$ shell-capacity account that is not derived. Everything downstream of it is exact.

**Excluded symmetry-doubling reading.** It is not a claim that a second symmetry group acts. The $(j,j)$ doubling that the hydrogenic shell classically receives from $\mathrm{SO}(4) = \mathrm{SU}(2)\times\mathrm{SU}(2)$ and its Runge–Lenz vector is here internal to a single object. The compact ($\cos/\sin$, root of unity) and non-compact ($\cosh/\sinh$, real $q$) pictures are the two real forms of one $\mathfrak{sl}(2,\mathbb{C})$, so no second compact $\mathrm{SU}(2)$ is required or postulated.

**Exact Clebsch–Gordan sub-shell decomposition.** Given the identification, the $q$-Clebsch–Gordan rule decomposes the self-square into the sub-shells,

$$
  V_{j_n} \otimes V_{j_n} \;\cong\; \bigoplus_{\ell=0}^{n-1} V_\ell ,
  \qquad\text{hence}\qquad
  [n]_q^2 \;=\; \sum_{\ell=0}^{n-1} [2\ell+1]_q ,
$$

which is the [self-square shell-capacity proposition](#prop:shell-capacity-self-square) and, at $q = 1$, the periodic-table capacities $2n^2 = 2,8,18,32,\ldots$. Clearing the common denominator $(q - q^{-1})$ turns this into an exact polynomial identity over $\mathbb{Z}[q,q^{-1}]$ for every $n$.

**Falsifiable content.** The conjecture asserts more than a coincidence of counts. It fixes the sub-shell multiplicities as the $q$-integers $[2\ell+1]_q$, and not only their $q \to 1$ values $2\ell+1$; a resolved sub-shell structure departing from $[2\ell+1]_q$ at $q \neq 1$ would refute it. In particular, the sub-shell decomposition $\dim_q \mathcal{O}_n = \sum_{\ell=0}^{n-1} [2\ell+1]_q$ is a consequence of the self-square hypothesis rather than an independent assumption, and an arbitrary linear dimension function fails the self-square identity.

**Relation to the normal-bundle model.** The [normal-bundle orbital-space conjecture](#conj:orbital-space-normal-bundle) describes the same space $\mathcal{O}_n$ geometrically, as framing-$k$ sections of the trefoil's normal bundle in Bring's surface cut off by a $q$-Laplacian eigenvalue bound. The two are independent descriptions of one object: the present conjecture supplies its categorical structure, the normal-bundle conjecture its geometric realisation. Establishing an isomorphism between them would close both at once.
