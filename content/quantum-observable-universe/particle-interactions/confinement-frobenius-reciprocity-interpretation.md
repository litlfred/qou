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

## Evaluation protocol

The rigorous evaluation of the master formula requires:

1. **$G$, $G^{-1}$**: Evaluate the Frobenius Gram matrix and its inverse on the NF basis.
2. **Active set + shadow prices**: Solve the operator-selection linear program for the target bound state to obtain the active set $A^*$ and shadow prices $u_i^* = y_i^*$.
3. **Observable coefficients $\langle O, b_j\rangle$**: Compute the Markov trace $\mathrm{tr}_M(O \cdot b_j)$ for each active $j$.
4. **Pair**: $\langle O\rangle_T = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij} \langle O, b_j\rangle$.
