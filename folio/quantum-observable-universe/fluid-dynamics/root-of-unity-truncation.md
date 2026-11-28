**Conditional on
[q-deformed Aubin--Lions lemma: compactness of the solution family as $q \to 1$](#conj:q-aubin-lions),
[Conjectural anti-parallel vortex-collision singularity in the $q \to 1^+$ limit](#conj:ns-counterexample),
[Critical exponent of the enstrophy divergence at $q = 1$](#conj:critical-exponent),
[Blowup mechanism as Yekutieli lifting obstruction in the brane tower](#prop:blowup-yekutieli),
[Vorticity lower bound for anti-parallel filament collision as $q \to 1$](#conj:vorticity-lower-bound),
and
[Regularity breakdown at $q = 1$ and a discretely self-similar blow-up scenario](#conj:regularity-breakdown).**

Let $(\mathbf{C}, A, \tau)$ be a QOU with aether parameter $q$ not a root of unity ([QOU axiom](#def:aether-parameter)). As $q \to 1$ through the roots of unity $q = e^{i\pi/\kappa}$, the representation category truncates to a finite modular tensor category; any singular behaviour in the model can arise only in the $\kappa \to \infty$ accumulation. Within this conditional anti-parallel vortex-pair model with core aspect ratio $\kappa(t)$:

$$
  \boxed{
    \text{limiting collision singularity}
    \iff
    \kappa(t) = O(1).
  }
$$

**Heuristic argument.**

The [QOU axiom](#def:aether-parameter) requires that $q$ is not a root of unity. Passing $q \to 1$ along roots of unity $q = e^{i\pi/\kappa}$ truncates the representation theory to finitely many simple objects at each finite level $\kappa$, so any loss of smoothness in the family is confined to the infinite-level limit $\kappa \to \infty$.

The truncation mechanism — driven by the vanishing of the $q$-integer $[\kappa]_q$ at $q = e^{i\pi/\kappa}$, which restricts the $q$-Laplacian spectral tower $[k]_q^2$ to the finite Verlinde/ADE set — is established in [the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower). The paragraphs below trace its heuristic reading for the $q$-deformed fluid model.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
 Contains infinitely many simple objects $V_j$, $j = 0, 1/2, 1, \ldots$, with quantum dimensions $[2j+1]_q > 0$ and eigenvalues $[k]_q^2 \sim q^{2k}$ growing exponentially. Conditional [global regularity](#thm:q-ns-wellposedness) models smooth evolution in this regime.
2. **Root of unity $q = e^{i\pi/\kappa}$, bounded $\kappa \in \mathbb{Z}_{\geq 2}$.**
 Contains **finitely many** simple objects, $j = 0, 1/2, \ldots, (\kappa-2)/2$, since $[2j+1]_q = 0$ at $j = (\kappa-1)/2$. The Verlinde formula governs fusion:

 $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

 where $S$ is the modular $S$-matrix, yielding a modular tensor category at level $\kappa$.
3. **$q = 1$ (classical limit).**
 Contains infinitely many simple objects with $[k]_1 = k$ (polynomial scaling); both the root-of-unity truncation and the exponential $q > 1$ damping disappear.

**Finite-dimensionality at each root of unity.**

At a fixed root of unity $q = e^{i\pi/\kappa}$, a truncated $q$-NS Galerkin model retains at most $(\kappa-1)/2$ active vortex modes:

- Within generic $q > 1$: modes above $[k]_q > \mathrm{Re}_q^{1/2}$ undergo exponential damping while remaining nonzero.
- At a root of unity: modes with $j > (\kappa-2)/2$ vanish in the quotient category, leaving a finite-dimensional ODE system that is globally smooth by Picard--Lindelöf.

**The $q = 1$ accumulation.**

As $\kappa \to \infty$, $q = e^{i\pi/\kappa} \to 1$ and the cutoff $j_{\max} = (\kappa-2)/2 \to \infty$ unlocks infinitely many modes. Under the conditional hypotheses above, no fixed finite truncation blows up, so any singularity of the limiting family is purely an infinite-mode accumulation effect as $\kappa \to \infty$.

**Connection to the core aspect ratio.**

At a fixed root of unity $q = e^{i\pi/\kappa}$, restricting core-boundary Fourier modes to $j \leq (\kappa-2)/2$ models the core aspect ratio $\kappa(t) = a_\perp/a_\parallel$ by a trigonometric polynomial of degree at most $(\kappa-1)/2$, obeying the Bernstein inequality $|\kappa'(t)| \leq N\|\kappa\|_\infty$. Within this finite-mode ansatz, one obtains a level-dependent upper bound

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

for a constant $C$ independent of $\kappa$, which diverges linearly as $\kappa \to \infty$ ($q \to 1$).

**The conditional growth-rate question.**

The conditional [vorticity lower bound](#conj:vorticity-lower-bound) requires uniform control $\sup_t \kappa(t) \leq C$ independent of $\kappa$, whereas the finite-mode bound $1 + C(\kappa-1)$ grows with $\kappa$. Within this collision ansatz, three asymptotic regimes are distinguished:

- If $\kappa(t) \leq C_0$ uniformly in $\kappa$: the core cross-section remains of bounded aspect ratio and the conditional lower bound of [the vorticity lower bound](#conj:vorticity-lower-bound) yields singular vorticity growth as $t \to T^{*-}$.
- If $\kappa(t) \sim \kappa$: the core flattens into a sheet at the rate new modes unlock, so the lower bound $\omega \geq c/(T^*-t)$ need not hold and the limiting flow may remain regular.
- If $\kappa(t) \sim \kappa^\beta$ with $0 < \beta < 1$: the ansatz predicts singular concentration only for $\beta < 1/2$.

*Geometric scope of $\kappa(t)$.* The core aspect ratio $\kappa(t)$ measures the cross-sectional core shape only and cannot be identified with a Levi-form condition number $\lambda_{\max}/\lambda_{\min}$. On the three-dimensional flow domain the Levi datum of the vorticity plane field is the single scalar $\xi\cdot\mathrm{curl}\,\xi$ ([core Levi form](#prop:core-levi-form)), so there is no eigenvalue pair and no condition number, and any direct blow-up implication from non-degenerate Levi data is refuted by steady Beltrami solutions ([Levi degeneracy conjecture](#conj:levi-degeneracy)).

**Archimedean specialisation.** What follows sits on the archimedean side of the algebraic-to-archimedean wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the aether parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
