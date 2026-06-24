The Markov trace
([Jones--Markov trace](#thm:jones-markov-trace)) is $\mathbb{C}$-linear,
and the volume map $\mathrm{Vol}$ on link diagrams used in
$\tau_{\mathrm{arch}}$ vanishes on every diagram whose closure is the
unknot, the unlink, or any non-hyperbolic knot. We treat the two
summands separately.

1. **Identity term.** $\overline{1} = $ (n-component unlink), which
   is non-hyperbolic. Hence $\mathrm{Vol}(\overline{1}) = 0$
   ([Kashaev--Murakami--Murakami convention](#conj:kashaev-volume-conjecture);
   the right-hand side of the volume conjecture vanishes on
   non-hyperbolic links by definition).

2. **Generator terms.** Each $\sigma_i$ is a *single positive
   crossing*; its closure $\overline{\sigma_i}$ is the unknot
   together with $n-2$ disjoint unknotted strands (an $(n-1)$-component
   unlink). It is non-hyperbolic, so
   $\mathrm{Vol}(\overline{\sigma_i}) = 0$.

3. **Linearity.** The trace and volume map are linear on the
   Hecke algebra, so

   $$
     \mathrm{Vol}(\overline{\gamma})
     \;=\;
     \mathrm{Vol}(\overline{1})
     \;+\;
     \sum_{i=1}^{n-1} \phi_i\,\mathrm{Vol}(\overline{\sigma_i})
     \;=\;
     0.
   $$

This proves the claim.
$\qquad\blacksquare$
