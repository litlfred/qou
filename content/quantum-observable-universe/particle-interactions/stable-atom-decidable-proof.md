1. *Compute the NF $T_w \in H_{n(K)}(q)$ via Gröbner–Shirshov
   reduction ([hecke normal form](#def:hecke-normal-form)) —
   terminates in finite time by the Diamond Lemma.*
2. *Compute the confinement level
   ([confinement level](#def:confinement-level)) $\ell(K, q)$ —
   sort the finite set of shadow prices, find the smallest
   $\ell$ with $T_w \in J^\ell(q)$.*
3. *Construct the LP-dual constraint matrix
   $\mathrm{G}(q) \in R^{N \times N}$ where $N$ is the number of primitive
   operators in $J^{\ell(K, q)}(q)$ — finite by
   [confinement-level-exists](#prop:confinement-level-exists).*
4. *Run an integer-linear-programming solver on $\{x \in
   \mathbb{Z}_{\geq 0}^N : \mathrm{G}(q) x \geq 0\}$.  By Lenstra's
   theorem, ILP feasibility in fixed dimension is decidable in
   polynomial time.*

*Each step is decidable; their composition is decidable.
$\qquad\blacksquare$
