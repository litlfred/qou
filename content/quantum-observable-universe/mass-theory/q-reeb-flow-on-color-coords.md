Fix the color-sector parametrisation
$\mathfrak{r}(\phi,\psi),\,\mathfrak{g}(\phi,\psi),\,\mathfrak{b}(\phi,\psi)$
on the Reeb bundle $\mathcal{R}_p$ over the exceptional divisor
([color-sector coordinates](#def:color-sector-coords)).  The
$q$-Reeb flow $\phi^q_t$
([$q$-Reeb flow](#ex:q-reeb-flow)) acts on each color sector by

$$
  \phi^q_t \cdot \mathfrak{r}(\phi,\psi)
  \;=\;  \mathfrak{r}(\phi,\,\psi + k^{(r)}\,q\,t),
$$

and analogously on the green and blue sectors with their own
rate multipliers $k^{(g)}, k^{(b)} \in \mathbb{Z}$.  The
**signed rate multiplier** $k^{(s)}$ for a sector $s$ is determined
by the braid generator being applied: $k^{(s)} = 0$ when the
sector is a spectator under that generator, $k^{(s)} = +1$ when
the sector is the leading active strand of the two-strand
subsystem, $k^{(s)} = -1$ when it is the partner strand whose
angular coordinate counter-rotates so the two-strand
centre-of-mass is preserved.  The flow parameter
$t \in [0,\pi]$ ranges over the latitude direction of
$\mathcal{R}_p$: $t = 0$ at the **south foundry**
(input boundary $\phi = 0$) and $t = \pi$ at the **north foundry**
(output boundary $\phi = \pi$).

**Color-twist accumulation.**  Substituting the explicit embedding
$\mathfrak{r}(\phi,\psi) = O + R(\sin\phi(\cos(\psi + q\phi)T_1
+ \sin(\psi + q\phi)T_2) - \cos\phi N)$
shows that the flow accumulates the color-twist factor $q t$
linearly in the angular coordinate: a strand sitting at $\psi = 0$
on the south foundry is delivered to the angular position $q\pi$
on the north foundry, an angular advance of $q\pi$ radians
(equivalently $q/2$ full turns of the $2\pi$-periodic angle).
This matches the static embedding in
[color-sector coordinates](#def:color-sector-coords).

**Composition.**  Sequential flows compose additively:
$\phi^q_{t_1} \circ \phi^q_{t_2} = \phi^q_{t_1 + t_2}$, so a braid
word $\beta = \sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ acts as a
concatenation of partial flows, each of latitude length $\pi/k$.
This composition rule is the algebraic content of the substrate
condition $[\hat X,\hat P]_q = J\hbar_q$
([Heisenberg commutator](#rem:heisenberg-commutator)).

**Two-strand localisation.**  When an adjacent-transposition
generator acts on only a pair of adjacent strands, the third
sector remains a spectator ($k = 0$, $\dot\psi = 0$) while the
two participating sectors counter-rotate ($k = +1$ for the leading
strand, $k = -1$ for the partner strand) so the two-strand
centre-of-mass is preserved.  In the Lean class
`QOU.CategoricalReeb.QReebFlowOnColorCoords`, this is captured by
the single rate-multiplier axiom
`flow_rate : flow t k ψ = ψ + k * q * t` (with corollaries
`flow_spectator`, `flow_active_pos`, `flow_active_neg` for
$k \in \{0, +1, -1\}$); the dictionary from braid generators to
per-sector multipliers is supplied by the consumer (see
[six canonical knot operators](#prop:six-canonical-knot-operators)).
The same signed-rate machine handles uniform-vortex 3-cycle
generators by setting $k = +1$ (positive 3-cycle) or $k = -1$
(negative 3-cycle) on every sector simultaneously.  This is the
geometric content of the Hecke generator $\sigma_i$ acting
nontrivially only on strands $i$ and $i+1$, and is the bridge
between the algebraic braid action and the explicit ODE on
color-sector coordinates exploited in
[six canonical knot operators](#prop:six-canonical-knot-operators).
