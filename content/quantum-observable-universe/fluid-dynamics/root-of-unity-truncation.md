**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Root-of-unity truncation").**

The [QOU axiom](#def:substrate-parameter) requires $q$ to avoid roots of unity. However, the limit $q \to 1$ passes through a dense set of roots of unity. At each root, the representation theory undergoes a truncation that strengthens regularity. The blowup at $q = 1$ arises as the accumulation of infinitely many such truncations.

The [$q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower) establishes the truncation mechanism: the $q$-integer $[\kappa]_q$ vanishes at $q = e^{i\pi/\kappa}$, collapsing the $q$-Laplacian spectral tower $[k]_q^2$ to the finite Verlinde/ADE set. We determine its fluid-dynamical consequence.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
   Infinitely many simple objects $V_j$ exist for $j = 0, 1/2, 1, \ldots$. Quantum dimensions satisfy $[2j+1]_q > 0$. Eigenvalues grow exponentially: $[k]_q^2 \sim q^{2k}$. The [well-posedness theorem](#thm:q-ns-wellposedness) guarantees global regularity.

2. **Root of unity $q = e^{i\pi/\kappa}$ for $\kappa \in \mathbb{Z}_{\geq 2}$.**
   The category contains finitely many simple objects: $j = 0, 1/2, \ldots, (\kappa-2)/2$. The quantum dimension $[2j+1]_q$ vanishes at $j = (\kappa-1)/2$. This truncates the representation category. The Verlinde formula governs fusion:

   $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

   where $S$ denotes the modular $S$-matrix. The representation category forms a modular tensor category. This provides the algebraic input for Chern--Simons TQFT at level $\kappa$.

3. **$q = 1$ (classical limit).**
   Infinitely many simple objects exist with polynomial eigenvalues $[k]_1 = k$. The system exhibits no truncation and no exponential damping. This corresponds to the [regularity breakdown](#conj:regularity-breakdown) regime.

**Root-of-unity regularity.**

At $q = e^{i\pi/\kappa}$, the q-NS system supports at most $(\kappa-1)/2$ active vortex modes. The truncated representation category contains finitely many objects. This imposes a hard cutoff, in contrast to the soft exponential damping of generic $q > 1$:

- Generic $q > 1$: modes with $[k]_q > \mathrm{Re}_q^{1/2}$ suffer exponential damping but remain nonzero.
- Root of unity: modes with $j > (\kappa-2)/2$ vanish from the category. The Hilbert space becomes finite-dimensional.

A finite-dimensional ODE is globally regular by the Picard--Lindelöf theorem. At every root of unity, the q-NS system reduces to a finite-dimensional, well-posed system.

**The $q = 1$ accumulation.**

As $\kappa \to \infty$, $q = e^{i\pi/\kappa} \to 1$. The truncation level $j_{\max} = (\kappa-2)/2 \to \infty$. More modes become available. The sequence of finite-dimensional systems approaches the infinite-dimensional classical system.

The blowup at $q = 1$ occurs because this infinite-dimensional limit is singular. While no finite truncation blows up, the limit of all truncations diverges. This characterizes a phase transition at the accumulation point.

**Connection to the core aspect ratio.**

At a root of unity $q = e^{i\pi/\kappa}$, the modular tensor category structure controls the vortex core shape. The fusion rules $N_{ij}^k$ govern allowed mode interactions. The truncation $j \leq (\kappa-2)/2$ forbids high-frequency core deformations. The core cannot develop fine-scale structure beyond the cutoff. We observe:

- The Fourier modes of the core boundary control the core aspect ratio $\kappa(t) = a_\perp/a_\parallel$.
- At a root of unity, only $(\kappa-1)/2$ modes exist. The ratio $\kappa(t)$ forms a trigonometric polynomial of bounded degree.
- A trigonometric polynomial of degree $N$ satisfies $|\kappa'(t)| \leq N\|\kappa\|_\infty$ via the Bernstein inequality. This prevents rapid oscillation.

We obtain an explicit bound at each root of unity:

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

for a universal constant $C$. The bound grows linearly with the truncation level $\kappa$. It diverges as $\kappa \to \infty$ ($q \to 1$).

**The refined gap.**

The [vorticity lower bound](#prop:vorticity-lower-bound) requires $\sup_t \kappa(t) \leq C$ with $C$ independent of $q$. The root-of-unity analysis gives $\kappa(t) \leq 1 + C(\kappa-1)$, which grows with $\kappa$. We consider three growth rates:

- If $\kappa(t) \leq C_0$ uniformly in $\kappa$: the core remains circular, the lower bound holds, and Navier--Stokes blows up.
- If $\kappa(t) \sim \kappa$ linearly: the core flattens at the same rate as modes become available. The vorticity spreads into a sheet. The lower bound $\omega \geq c/(T^*-t)$ may fail. Navier--Stokes might remain regular.
- If $\kappa(t) \sim \kappa^\beta$ with $0 < \beta < 1$: the lower bound holds if $\beta < 1/2$, where the flattening is slower than the approach.

The [Levi form condition number](#def:levi-form-defect) at the vortex core is $\lambda_{\max}/\lambda_{\min} = \kappa(t)^2$. The contact structure degenerates (becomes integrable) if and only if $\lambda_{\min} \to 0$, which corresponds to $\kappa(t) \to \infty$. We conclude:

$$
  \boxed{
    \text{NS blows up}
    \iff
    \text{Levi form stays non-degenerate at collision}
    \iff
    \kappa(t) = O(1).
  }
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
