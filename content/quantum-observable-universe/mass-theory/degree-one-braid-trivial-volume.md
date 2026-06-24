**Statement.**
*Let $\gamma \in H_n(q)$ be a degree-one element*

$$
  \gamma \;=\; 1 \;+\; \sum_{i=1}^{n-1} \phi_i\,\sigma_i,
  \qquad \phi_i \in \mathbb{C},
$$

*and write $\overline{\beta}$ for the closure of a braid word $\beta$.
Then under the
[archimedean realization functor](#def:archimedean-realization-functor)
the volume image vanishes:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\operatorname{tr}_M(\gamma)\bigr)
  \;=\; 0
  \quad\text{in the volume normalisation}
  \quad
  \mathrm{Vol}_{\tau}(\overline{\gamma}) \;=\; 0.
$$

**Scope.** The lemma establishes only the *archimedean shadow* — the
real-valued volume image. It does **not** identify $\gamma$ with the
gauge boson of any physical theory; that identification is interpretive
and is discussed in [breit-wheeler-vertex](#rem:breit-wheeler-vertex)
and the photon-energy section of the manuscript.

**What this rules out.** Any candidate algebraic photon constructed as
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
