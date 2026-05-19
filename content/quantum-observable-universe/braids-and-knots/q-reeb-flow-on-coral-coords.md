Fix the coral-sector parametrisation
$\mathfrak{r}(\phi,\psi),\,\mathfrak{g}(\phi,\psi),\,\mathfrak{b}(\phi,\psi)$
on the Reeb bundle $\mathcal{R}_p$ over the exceptional divisor
([coral-sector coordinates](#def:coral-sector-coords)).  The
$q$-Reeb flow $\phi^q_t$
([$q$-Reeb flow](#ex:q-reeb-flow)) acts on the coral-sector
coordinates by

$$
  \phi^q_t \cdot \mathfrak{r}(\phi,\psi)
  \;=\;  \mathfrak{r}(\phi,\,\psi + q\,t),
$$

and identically on the green and blue sectors.  The flow parameter
$t \in [0,\pi]$ ranges over the latitude direction of
$\mathcal{R}_p$: $t = 0$ at the **south foundry**
(input boundary $\phi = 0$) and $t = \pi$ at the **north foundry**
(output boundary $\phi = \pi$).

**Coral-twist accumulation.**  Substituting the explicit embedding
$\mathfrak{r}(\phi,\psi) = O + R(\sin\phi(\cos(\psi + q\phi)T_1
+ \sin(\psi + q\phi)T_2) - \cos\phi N)$
shows that the flow accumulates the coral-twist factor $q t$
linearly: a strand sitting at $\psi = 0$ on the south foundry is
delivered to the angular position $q\pi$ on the north foundry.
For the canonical traversal $t \mapsto \phi = t$ across the divisor,
the angular position of each sector advances by exactly $q$ full
turns, in agreement with the static embedding in
[coral-sector coordinates](#def:coral-sector-coords).

**Composition.**  Sequential flows compose additively:
$\phi^q_{t_1} \circ \phi^q_{t_2} = \phi^q_{t_1 + t_2}$, so a braid
word $\beta = \sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ acts as a
concatenation of partial flows, each of latitude length $\pi/k$.
This composition rule is the algebraic content of the substrate
condition $[\hat X,\hat P]_q = J\hbar_q$
([Heisenberg commutator](#rem:heisenberg-commutator)).

**Two-strand localisation.**  When a braid generator acts on only
a pair of adjacent strands, the flow restricts to the two
participating sectors: the third sector remains a spectator with
$\dot\psi = 0$.  This localisation is the geometric content of the
Hecke generator $\sigma_i$ acting nontrivially only on strands $i$
and $i+1$, and is the bridge between the algebraic braid action
and the explicit ODE on coral-sector coordinates exploited in
[six canonical knot operators](#prop:six-canonical-knot-operators).
