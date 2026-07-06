The Lagrange resolvents of the previous section diagonalised the
$C_5$-action on the genus-$4$ base surface but did not yet provide
an operator algebra acting along the resolvent eigenlines.  We now
blow up a brane point $p$ and read the missing operators off the
resulting exceptional divisor.  The blow-up replaces $p$ by a
$\mathbb{CP}^1$ that supports a Reeb circle bundle, and vertex
operators on the resulting bundle play the role of a
state–operator correspondence on the substrate.

The section is structured as a single geometric arc.

**Static arena.**  We first fix the static geometry: the
exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
([exceptional divisor](#def:exceptional-divisor)), the
Reeb bundle $\mathcal{R}_p \cong S^3 \xrightarrow{\pi_H} \mathcal{S}_p$
([Reeb bundle](#def:reeb-bundle)), the interpretive
[Reeb vector field on the exceptional divisor](#rem:reeb-exceptional-divisor),
and the
[vertex operator](#def:vertex-operator) +
[VOA–QOU dictionary](#rem:vertex-operator-dictionary)
that pins each vertex-algebra datum to the categorical structure.

**Dynamics on color coordinates.**  We then put the static arena
in motion: the
[$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)
gives the explicit dynamical equation $\dot\psi = q$ on each
active sector, with two-strand localisation when only a pair of
adjacent strands is involved.

**Six canonical knot operators.**  Threading the flow with each
of the six $S_3$ braid words yields the
[six canonical knot operators](#prop:six-canonical-knot-operators)
— the identity, two adjacent transpositions $\sigma_1, \sigma_2$,
the Garside element $\sigma_1\sigma_2\sigma_1$
([Garside as compound Reeb flow](#rem:garside-as-compound-flow))
and the two 3-cycles — with explicit trajectory ODEs and matching
boundary permutations on the ramified output disc.

**Boundary disc.**  At the foundry boundaries $\phi \in \{0, \pi\}$
the three colour tubes fuse into a single triply-ramified disc;
the
[ramified-disc fusion](#prop:ramified-disc-fusion)
proposition identifies the monodromy as the $S_3$ Galois action
on Lagrange resolvents, closing the loop "Reeb trajectory $\to$
boundary observable" geometrically.

**Complement is the volume.**  Removing tubular neighbourhoods of
the strand trajectories from $\mathcal{R}_p$ produces a knot
complement.  The
[Reeb-bundle complement equals volume](#prop:reeb-bundle-complement-equals-volume)
proposition — the Reeb-bundle face of the existing
mass-volume conjecture — packages the categorical Markov-trace
observable as the JSJ-graded sum
$\sum_{P_i\,\text{hyperbolic}} \rho_F(P_i) \cdot V_{\mathrm{hyp}}(P_i)$
of its complement.  The
[torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)
and
[hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb)
remarks read the geometric dichotomy directly off the Reeb-flow
trajectory: pure rotational 3-cycles trace torus knots on a
Heegaard torus (Seifert-fibered complement, $V_{\mathrm{hyp}} = 0$);
Garside / Borromean / figure-eight trajectories cross between
Heegaard tori, producing a hyperbolic complement with strictly
positive volume.

The next section,
[Vertex Factorisation and the Markov Trace](#sec:vertex-factorisation-markov),
takes the vertex operator and the six trajectory dictionary as
given and shows that every operator acting on the categorical
state space factors through the exceptional divisor.
