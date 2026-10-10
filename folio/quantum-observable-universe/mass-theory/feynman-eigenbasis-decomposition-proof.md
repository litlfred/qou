**Proof.**
By the $q$-analogue of Schur--Weyl duality
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(1)),
the tensor power decomposes as

$$
  V^{\otimes n}
  \cong
  \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  V_\lambda \otimes S_\lambda,
$$

where $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin
$j = (\lambda_1 - \lambda_2)/2$ and $S_\lambda$ is the irreducible
$H_n(R, q)$-module.  The braid $\beta \in B_n$ acts on $V^{\otimes n}$
via the braid group representation
$\rho_n \colon B_n \to \mathrm{Aut}(V^{\otimes n})$, and on each
$S_\lambda$ via the quotient map $B_n \to H_n(R, q)$.

The number of summands is $\lfloor n/2 \rfloor + 1$, corresponding to
spins $j = n/2, n/2 - 1, \ldots, \epsilon/2$ where
$\epsilon = n \bmod 2$.  This is finite for every $n$.  $\square$
