Of the six canonical knot operators
([six canonical knot operators](#prop:six-canonical-knot-operators)),
the Garside element $\Delta_3 = \sigma_1\sigma_2\sigma_1$ has the
most intricate Reeb-flow trajectory.  Two features deserve to be
unpacked.

**Three-stage compound flow.**  The Garside word factorises the
latitude interval $[0,\pi]$ into three equal sub-intervals
$[0,\pi/3]$, $[\pi/3, 2\pi/3]$, $[2\pi/3, \pi]$.  Inside each
sub-interval, exactly two of the three coral sectors participate
in a localised two-strand spiral while the third remains a
spectator:

| sub-interval | active pair | spectator | flow content |
|---|---|---|---|
| $[0, \pi/3]$ | $r, g$ | $b$ | adjacent half-twist $(rg)$ |
| $[\pi/3, 2\pi/3]$ | $g, b$ | $r$ | adjacent half-twist $(gb)$ |
| $[2\pi/3, \pi]$ | $r, g$ | $b$ | adjacent half-twist $(rg)$ |

Threading the three transpositions yields the composite
permutation
$(rg)\circ(gb)\circ(rg) = (rb)$,
the non-adjacent transposition that swaps the outer pair via the
middle strand.

**Braid relation as flow-trajectory equality.**  The same
non-adjacent transposition arises from the dual decomposition
$\sigma_2\sigma_1\sigma_2$ — three sub-intervals with the roles of
the $(rg)$ and $(gb)$ stages exchanged.  At the algebraic level
the equality $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$
is the braid relation; geometrically the two flow sequences
produce *physically different intermediate states* of the green
sector — pushed outward in one ordering, pulled inward in the
other — but the boundary footprint is the same permutation
$(rb)$.  The braid relation thereby acquires a concrete dynamical
interpretation: it is the equality of two compound Reeb
trajectories with matching boundary data but disagreeing
interior content.

**Why this is not a single closed-form flow.**  Unlike the two
3-cycles, whose Reeb trajectory is a uniform global vortex with
constant rate $\dot\psi = \pm q$ across all three sectors, the
Garside flow is *piecewise*: the angular rate $\dot\psi^{(g)}$ on
the green sector switches sign at each sub-interval boundary.
This explains the user-flagged observation that the Garside
element requires solving "PDEs" rather than a single ODE — the
solution exists, but only as a concatenation of three exact
two-strand solutions.

**Volume signature.**  Unlike the 3-cycles, whose trajectory lies
on a Heegaard torus and contributes zero hyperbolic volume
([torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)),
the Garside trajectory crosses between the two Heegaard tori of
$\mathcal{R}_p \cong S^3$ at each sub-interval boundary, so its
complement does *not* admit a Seifert fibration.  The JSJ
decomposition of $\mathcal{R}_p \setminus \nu(K_{\Delta_3})$
therefore contains a hyperbolic piece, in agreement with
[hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb).

**Proof status (reader guide).**  The boundary-permutation
identity above is the §3b-cond conditional content of
[six canonical knot operators](#prop:six-canonical-knot-operators).
Three layers cooperate, so the differential-geometric integrability
of $\xi_q$ never has to be proved directly:

| layer | status |
|---|---|
| combinatorial $S_3$ bijection on the six braid words | `sorry`-free in Lean (`QOU.CategoricalReeb.boundary_perm_realises_S3`, a finite case check on six `CanonicalBraid` constructors) |
| closed-form ODE per sub-interval | Python-verified (`computations/reeb_flow_garside_closed_form_verification.py`, witness status `verified`) |
| existence of $\phi^q_t$ as a continuous group on $\mathcal{R}_p$ | axiomatised via [$q$-Reeb flow on coral coords](#def:q-reeb-flow-on-coral-coords) per CLAUDE.md §3b-cond |

Discharging the third row — Picard–Lindelöf for the
$q$-deformed Reeb vector field — is a separate research direction,
deliberately held outside this proposition's scope.
