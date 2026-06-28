**Proof.**
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

This proves the claim. $\blacksquare$

**Scope.** The lemma establishes only the *archimedean shadow* — the
real-valued volume image. It does **not** identify $\gamma$ with the
gauge boson of any physical theory; that identification is interpretive
and is discussed in [breit-wheeler-vertex](#rem:breit-wheeler-vertex)
and the photon-energy section of the manuscript.

**Exclusion.** Any candidate algebraic photon constructed as
a degree-one element of the Hecke algebra is *automatically*
volume-trivial, hence cannot acquire mass through the
$\tau_{\mathrm{arch}}\circ\mathrm{Vol}_q$ pipeline. Mass generation
requires a closure that is genuinely hyperbolic, which forces the
braid word to have degree $\geq 2$ in the generators
$\sigma_i,\sigma_i^{-1}$.

**Relation to higher-degree contributions.** When the photon couples to
a massive state $\beta_m$, the product $\gamma \cdot \beta_m$ shifts in
the degree-lex filtration by $+1$ but otherwise transforms representation
content through the Pieri rule
([Pieri photon shift](#prop:pieri-photon-shift)). The lemma here is the
*base case* of that ladder.
