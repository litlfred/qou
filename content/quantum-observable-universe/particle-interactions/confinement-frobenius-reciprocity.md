**Proposition (confinement Frobenius reciprocity).**
*Let $T \in H_n(q)$ be a confined bound-state operator selected by the
operator-selection LP ([operator-selection LP](#prop:operator-selection-lp))
with primal optimum $T = \sum_i x_i^* b_i$ and dual optimum
$(y_0^*, y^*)$, where $\{b_1, \ldots, b_d\}$ is the NF basis, $G_{ij} =
\mathrm{tr}_M(b_i b_j)$ is the Frobenius Gram matrix
([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), and the
LP-active set is*

$$
  A^*(T) \;=\; \{\, i \in \{1, \ldots, d\} \;:\; y_i^* > 0 \,\}.
$$

*Then for every observable $O \in H_n(q)$ — interpreted as a linear
functional $b \mapsto \langle O, b\rangle = \mathrm{tr}_M(O \cdot b)$ on
the algebra — the physical expectation value of $O$ in the bound state
$T$ is the **Gram-inverse dual pairing weighted by LP-active shadow
prices**:*

$$
  \boxed{\;
    \langle O \rangle_T
    \;\equiv\;
    O(T)
    \;=\;
    \sum_{i,\,j \,\in\, A^*(T)}
      u_i^*\,(G^{-1})_{ij}\,\langle O,\, b_j\rangle
  \;}
$$

*where $u_i^* = y_i^*$ are the LP shadow prices on the active channels
and $(G^{-1})_{ij}$ is the Frobenius dual-basis matrix on the
$|A^*(T)|$-dimensional active subspace.  Equivalently, in compact
notation*

$$
  \langle O \rangle_T
  \;=\;
  \langle O,\, G^{-1}\,u^*\rangle_{A^*}
  \;=\;
  \langle O,\, T^\vee\rangle,
$$

*where $T^\vee = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij}\,b_j$ is the
**Frobenius dual** of $T$ on the active subspace.*

## Discussion

This proposition is the **master formula** for every numerical
prediction about a confined bound state of $H_n(q)$: binding energies,
form factors, axial couplings, magnetic moments, and any other
observable that is linear in the algebra.  It promotes the binding-
energy-only statement of
[knot-factor-frobenius-pairing](#conj:knot-factor-frobenius-pairing)
to the entire class of bound-state observables.

**Three distinct ingredients are required.**

1. **The Frobenius Gram inverse $G^{-1}$.**  The naïve Markov trace
   $\mathrm{tr}_M(O \cdot \rho(\beta_T))$ is *not* the physical
   expectation value of $O$ in the state created by braid $\beta_T$.
   The Markov form is non-degenerate but non-orthonormal on the NF
   basis, so dualisation requires the Gram inverse.

2. **The LP-active set $A^*(T)$.**  Most of the $d = n!$ NF basis
   elements have zero shadow price ($y_i^* = 0$); they are LP-slack.
   Including them in the dual pairing pollutes the observable with
   off-shell contributions.  Only the active channels — the
   "most receptive sub-braids" of the bound state, in the language
   of [BW shadow price](#prop:mass-coefficient-shadow-price) — carry
   physical weight.

3. **The shadow prices $u_i^* = y_i^*$.**  By LP duality, the shadow
   price on channel $i$ is the marginal cost of saturating the
   Frobenius positivity constraint $\sum_j G_{ij} x_j \geq 0$.  These
   prices are exactly the weights that make $\langle O\rangle_T$
   coincide with the physical expectation under the categorical action
   functional ([Yekutieli 2D nonabelian Stokes](#rem:yekutieli-stokes)).

## Sketch of proof

The proof has two parts.

**Part 1 — Frobenius reciprocity on $H_n(q)$.**
The Markov trace $\mathrm{tr}_M$ is a non-degenerate Frobenius form on
$H_n(q)$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).  The
Frobenius dual $T^\vee$ of any element $T$ is defined by the equation
$\langle T^\vee,\, b_j\rangle = x_j^*$ for the NF coefficients of $T$.
Solving this linear system on the NF basis gives
$T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$.  Frobenius reciprocity
then states $\langle O, T\rangle_{\text{phys}} = \langle O, T^\vee\rangle$
for every observable $O$.

**Part 2 — LP-active reduction.**
The operator-selection LP ([operator-selection LP](#prop:operator-selection-lp))
gives the primal–dual pair $(x^*, y^*)$ with strong duality
$\sum_i t_i x_i^* = n_{\mathrm{target}} y_0^*$.
Complementary slackness forces $y_i^* x_i^{(\text{slack})} = 0$ for
every $i$, so on the LP-inactive set $\{i : y_i^* = 0\}$ either the
constraint is slack and $x_i^*$ is unconstrained, or $x_i^* = 0$.
Substituting $x_i^* = (G^{-1} u^*)_i$ on the active set $A^*(T)$
(this is exactly the KKT stationarity condition for the dualised
LP) gives the boxed formula.

For binding energy the observable is the Hamiltonian $O = H$ acting
diagonally on the NF basis, and the formula reduces to the known
expression in [knot-factor-frobenius-pairing](#conj:knot-factor-frobenius-pairing).
That conjecture is therefore the special case $O = H$ of the present
proposition; conversely, any **other** bound-state observable is
governed by the same reciprocity.

## Corollaries

- **Corollary (g_A as an instance).**  The axial coupling
  $g_A = \langle \sigma_A\rangle_{\mathfrak{p}} / \langle \sigma_V\rangle_{\mathfrak{p}}$
  of the proton bound state $T_{\mathfrak{p}} = \mathcal{B}_3 =
  (\sigma_0 \sigma_1^{-1})^3$ is the ratio of two instances of the
  master formula at the LP-active set $A^*(\mathcal{B}_3)$ selected by
  [confinement operator selection](#prop:confinement-operator-selection).
  See `computations/borromean-axial-coupling.py` for the
  numerical instantiation.

- **Corollary (raw conjugation traces are zero-information).**
  The pattern $\mathrm{tr}_M(\beta \cdot X \cdot \beta^{-1})$ is
  cyclically equal to $\mathrm{tr}_M(X)$ and therefore independent of
  $\beta$.  Any script computing such a quantity as a "bound-state
  observable of $\beta$" is structurally wrong: the dependence on the
  bound-state braid disappears under cyclicity.  The fix is always to
  replace the conjugation pattern with the master formula above —
  load $G^{-1}$, load $A^*$ from the operator-selection LP, and pair
  $O$ against $T^\vee$ on the active subspace.

## Computational protocol

A correct numerical implementation of the master formula requires:

1. **$G$, $G^{-1}$**: load from
   `computations/gram-matrix-dual.witness.json`
   (`gram_matrix`, `gram_inverse` fields).
2. **Active set + shadow prices**: solve the operator-selection LP for
   the target bound state via
   `computations/lp_dual_solver.py::solve_operator_selection_lp`,
   read `active_set` and `y_star`.
3. **Observable coefficients $\langle O, b_j\rangle$**: compute the
   Markov trace $\mathrm{tr}_M(O \cdot b_j)$ for each active $j$.
4. **Pair**: $\langle O\rangle_T = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij}
   \langle O, b_j\rangle$.
5. **Witness**: emit `gram_matrix`, `gram_inverse`, `lp_active_set`,
   `shadow_prices` (so the bound-state-observable CI gate passes), and
   `primal_obj`/`dual_obj`/`duality_gap` (so the LP-dual CI gate passes).

Any witness whose `description` claims to compute a bound-state
observable but lacks these fields is flagged by
`computations/bound_state_observable_validator.py`.
