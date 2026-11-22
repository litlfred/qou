**Proof.**
The hyperbolic volume vanishes on every non-hyperbolic link, by
convention ([Kashaev--Murakami--Murakami convention](#conj:kashaev-volume-conjecture)).

1. **Identity.** $\overline{\mathbf{1}}$ is the $n$-component unlink, which is
   not hyperbolic, so $\mathrm{Vol}(\overline{\mathbf{1}}) = 0$.

2. **One crossing.** $\sigma_i^{\pm 1}$ joins strands $i$ and $i+1$ by a single
   crossing; its closure is an unknot together with $n-2$ disjoint unknotted
   strands, an $(n-1)$-component unlink. It is not hyperbolic, so
   $\mathrm{Vol}(\overline{\sigma_i^{\pm 1}}) = 0$.

These are all the words in the support of $\gamma$. $\blacksquare$

**Why the volume is not linear.** The earlier version of this proof added the
two cases using linearity of a volume map on $H_n(q)$. No such map exists. The
six positive permutation braids $\mathbf{1}, \sigma_1, \sigma_2, \sigma_1\sigma_2,
\sigma_2\sigma_1, \sigma_1\sigma_2\sigma_1$ span $H_3(q)$, and their closures
(unlinks, the unknot, the Hopf link) all have volume $0$. A linear map that
agreed with $\mathrm{Vol}$ on them would vanish on all of $H_3(q)$, including on
$\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$, whose closure is $4_1$ with
$\mathrm{Vol}(4_1) = 2.0299\ldots \neq 0$. The first
half of this argument is proved: a linear map that vanishes on a set vanishes on its span.

**Scope.** The lemma establishes only the *archimedean shadow* — the
real-valued volume image. It does **not** identify $\gamma$ with the
gauge boson of any physical theory; that identification is interpretive
and is discussed in [breit-wheeler-vertex](#rem:breit-wheeler-vertex)
and the photon-energy section of the manuscript.

**Exclusion.** Every braid word in the support of a degree-one element has
volume $0$, so a degree-one element cannot reach a hyperbolic closure through any
of its words. A hyperbolic closure needs a word with at least two crossings
(in fact at least four, since every link with crossing number at most $3$ is
non-hyperbolic).

**Relation to higher-degree contributions.** When the photon couples to
a massive state $\beta_m$, the product $\gamma \cdot \beta_m$ shifts in
the degree-lex filtration by $+1$ but otherwise transforms representation
content through the Pieri rule
([Pieri photon shift](#prop:pieri-photon-shift)). The lemma here is the
*base case* of that ladder.
