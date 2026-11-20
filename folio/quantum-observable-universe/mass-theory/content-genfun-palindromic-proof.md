**Proof.**

Partition conjugation $\lambda \mapsto \lambda'$ is an involution of the set of
partitions of $n$. It is weight-preserving, $f^{\lambda'} = f^\lambda$ (the standard
tableaux of $\lambda'$ are the transposes of those of $\lambda$), and content-reversing,
$\mathrm{content}(\lambda') = -\mathrm{content}(\lambda)$ (transposition exchanges the
row and column indices, negating each cell's content $j-i$).

**Palindromy.** Reindexing the sum by conjugation,

$$
C_n(q^{-1}) = \sum_{\lambda} f^\lambda q^{-\mathrm{content}(\lambda)}
= \sum_{\lambda} f^{\lambda'} q^{-\mathrm{content}(\lambda')}
= \sum_{\lambda} f^{\lambda} q^{\,\mathrm{content}(\lambda)} = C_n(q),
$$

using $f^{\lambda'}=f^\lambda$ and $-\mathrm{content}(\lambda') = \mathrm{content}(\lambda)$.

**Bar-even second order.** Writing $q = e^t$, the linear term of $C_n(e^t)$ in $t$ is
$\sum_\lambda f^\lambda\,\mathrm{content}(\lambda)$; the same reindexing gives
$\sum_\lambda f^\lambda\,\mathrm{content}(\lambda) = \sum_\lambda f^{\lambda'}\,\mathrm{content}(\lambda')
= -\sum_\lambda f^\lambda\,\mathrm{content}(\lambda)$, hence it is $0$. So $C_n(q) - C_n(1)$
has no linear term and is $O((q-1)^2)$. Finally $C_n(1) = \sum_\lambda f^\lambda = I(n)$
is the classical identity counting involutions by RSK shape. $\blacksquare$

**Machine verification.** The two structural steps — reindexing by an anti-invariant
involution for palindromy, and the vanishing first moment for bar-evenness — are proved
for arbitrary finite index sets in `QOU.AntiInvolutionPalindrome`
.
The Lean sibling checks the $n=4$ instance concretely
. Exact symbolic verification of the closed
form, palindromy, $C_n(1)=I(n)$ and the second-order rigidity has been carried out
for $n \leq 8$, together with the parallel result for the Plancherel weight $(f^\lambda)^2$.
