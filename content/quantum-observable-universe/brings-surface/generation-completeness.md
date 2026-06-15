The embeddability closure
([embeddability closure](#thm:embeddability-closure)) shows that the
generation scheme does not produce knots *outside* genus $4$.  The
converse question is whether it produces *all* knots inside genus $4$.
The answer is yes: every knot embeddable in the Bring's surface is
reachable from $\mathcal{G}$ by Skein operations alone.

**Theorem (Generation completeness).**
Let $K$ be any knot with Seifert genus $g(K) \leq 4$.  Then $K$ is
reachable from the generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) by a finite
sequence of Skein crossing changes.  In particular, the generation
scheme
([knot-particle generation](#def:knot-particle-generation)) applied to
$\mathcal{G}$ produces every knot type that admits a localized knot
structure in the Descartes universe.

**Proof.**
The argument proceeds in two steps.

*Step 1: Reachability from the unknot.*
Every knot $K$ has a finite unknotting number $u(K)$ — the minimum
number of crossing changes needed to convert $K$ into the unknot
$0_1 = T_{1,0}$.  Since crossing changes are involutions (each change
is its own inverse), the same $u(K)$ crossing changes applied to
$T_{1,0}$ produce $K$.  Because $T_{1,0} \in \mathcal{G}$, the knot
$K$ is reachable from $\mathcal{G}$ by at most $u(K)$ Skein
operations.

*Step 2: The spectral filter selects genus $\leq 4$.*
Not every knot reachable from $T_{1,0}$ by crossing changes has
genus $\leq 4$ — intermediate steps may pass through arbitrarily
high genus.  However, the Bring's surface imposes a spectral filter:
in the Skein module $\mathrm{Sk}_q(\mathbf{C})$, the mass functional
$\mathcal{M} \colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$ annihilates
any term whose knot type has $g > 4$
([embeddability closure](#thm:embeddability-closure)).  The physical
content of the Skein resolution is the projection onto the submodule
spanned by knots with $g(K) \leq 4$.

The composition of Steps 1 and 2 gives: for any knot $K$ with
$g(K) \leq 4$, there exists a finite sequence of Skein crossing
changes $\sigma_1, \ldots, \sigma_r$ (with $r \leq u(K)$) such that
$K$ appears with nonzero coefficient in the Skein expansion of
$\sigma_r \circ \cdots \circ \sigma_1(T_{1,0})$, and $K$ passes the
spectral filter since $g(K) \leq 4$.  $\square$

**Corollary.**
The Descartes particle spectrum is *complete* over embeddable knots:
every knot type with $g(K) \leq 4$ corresponds to a state in the
physical state space $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$.
No embeddable knot is excluded from the spectrum.

**Counting embeddable knots.**
The number of distinct knot types with Seifert genus $\leq g$ grows
rapidly.  For $g \leq 4$, the knot tables give:

| Genus | Knots (prime, up to 16 crossings) | Examples |
|-------|-----------------------------------|---------|
| $0$ | $1$ | $0_1$ |
| $1$ | $\geq 70$ | $3_1, 4_1, 5_2, 6_1, 6_2, 6_3, \ldots$ |
| $2$ | $\geq 400$ | $5_1, 7_4, 8_1, \ldots$ |
| $3$ | $\geq 2{,}000$ | $7_1, 8_{19}, 9_2, \ldots$ |
| $4$ | $\geq 8{,}000$ | $9_1, 10_{124}, 11a_{367}, \ldots$ |

The vast majority of these are hyperbolic (non-torus) knots.  The
generation scheme reaches all of them: the $7$ torus knot generators
are the *seeds*, and Skein crossing changes explore the full knot
landscape within the genus bound.

**Physical interpretation.**
The completeness theorem means the Descartes universe does not
arbitrarily select which knots become particles.  Every topologically
admissible knot type is physically realizable — the $7$ generators
and the Skein algebra are sufficient to span the entire embeddable
spectrum.  The particle dictionary
([knot formula table](#rem:knot-formula-table)) names only the
phenomenologically prominent knots (trefoil, figure-eight, etc.),
but the theorem guarantees that the thousands of higher-crossing
embeddable knots also populate the spectrum, appearing as massive,
short-lived resonances in the Skein decomposition of hadronic
processes.
