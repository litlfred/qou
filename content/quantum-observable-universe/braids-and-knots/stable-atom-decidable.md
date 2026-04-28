**Proposition.**
*[Stability of an atom](#def:stable-atom) at fixed $q$ is
**decidable**: there is an algorithm that, given an atom-knot $K$
of type $(Z, N)$ and a substrate parameter $q$ in the generic
locus, returns `True` if $K$ is stable at $q$ and `False` otherwise.*

*Proof.*

1. *Compute the NF $T_w \in H_{n(K)}(q)$ via Gröbner–Shirshov
   reduction ([hecke normal form](#def:hecke-normal-form)) —
   terminates in finite time by the Diamond Lemma.*
2. *Compute the confinement level
   ([confinement level](#def:confinement-level)) $\ell(K, q)$ —
   sort the finite set of shadow prices, find the smallest
   $\ell$ with $T_w \in J^\ell(q)$.*
3. *Construct the LP-dual constraint matrix
   $G(q) \in R^{N \times N}$ where $N$ is the number of primitive
   operators in $J^{\ell(K, q)}(q)$ — finite by
   [confinement-level-exists](#prop:confinement-level-exists).*
4. *Run an integer-linear-programming solver on $\{x \in
   \mathbb{Z}_{\geq 0}^N : G(q) x \geq 0\}$.  By Lenstra's
   theorem, ILP feasibility in fixed dimension is decidable in
   polynomial time.*

*Each step is decidable; their composition is decidable.
$\square$*

**Complexity.**
*The bottleneck is step 4 (ILP feasibility) — exponential in $N$
in general, polynomial in fixed dimension.  For nuclear
applications ($N = O(k_{\max}^2)$ ~ tens of primitive operators),
ILP is tractable.*
