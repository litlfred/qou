The Hecke energy $\kappa_c^{\mathrm{comp}}(L, q)$
([Skein resolution obstruction](#def:skein-resolution-obstruction))
admits an algorithmic reading through the Gröbner--Shirshov
reduction theory of the Iwahori--Hecke algebra $H_n(q)$
([GS reduction on $H_n(q)$](#unital-groebner-bases:prop:gs-cost-jones-recursion)).

**Identification.** For a braid $\beta \in B_n$ with closure
$L = \widehat{\beta}$ and Hecke image $\rho(\beta)$,

$$
  J_L(q)
  \;=\;
  \mathrm{tr}_M\!\bigl(\mathrm{NF}(\rho(\beta))\bigr),
  \qquad
  \kappa_c^{\mathrm{comp}}(L, q)
  \;=\;
  \mathrm{heckeCost}\!\bigl(\mathrm{NF}(\rho(\beta))\bigr),
$$

where $\mathrm{NF}$ is the unique Gröbner--Shirshov normal form
under (H1)/(H2)/(H3) and $\mathrm{tr}_M$ is the Markov trace
([Markov trace](#thm:jones-markov-trace)). The Jones polynomial
and the Hecke energy are therefore two evaluations of the same
normal form.

**Strand picture.** The (H1) rule
$T_i^2 \to (q - q^{-1})\,T_i + 1$ replaces a double crossing of
two strands by a skein-weighted branch with coefficient
$q - q^{-1}$ on the single crossing and coefficient $1$ on the
smoothing. Rule (H2) is a Reidemeister-III move and rule (H3) is
a distant-strand commutation; both preserve the multiset of
leading coefficients.

**Locus of the obstruction.** Rule (H1) is the unique source of
skein arithmetic: each application contributes one factor
$(q - q^{-1})$ to one branch and one factor $1$ to the other.
Rules (H2) and (H3) permute monomials without changing
$\mathrm{heckeCost}$. The exponential depth of the skein
resolution tree $\mathcal{R}(L)$
([Skein Turing machine](#rem:skein-turing-machine)) accumulates
entirely through iterated (H1) applications. At non-torsion
$q_0 \approx 1.1097$, the algebra $H_n(q_0)$ is semisimple, no
branch collapses, and $\kappa_c^{\mathrm{comp}}$ is non-vanishing
([Skein resolution obstruction](#def:skein-resolution-obstruction)).

**Physical instances.** The Hecke energy $\Delta E$ at torus-knot
shell boundaries
([Torus-knot shell binding](#prop:torus-knot-shell-binding)) and
the Jones-polynomial cost bounds used in strangelet stability
([Strangelet Witten stability](#rem:strangelet-witten-stability))
are both specialisations of this identity, with (H1) supplying
the skein arithmetic and (H2)/(H3) redistributing it along the
reduction path.
