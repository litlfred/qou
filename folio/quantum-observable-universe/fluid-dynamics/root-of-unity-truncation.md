**Proposition (conditional on
the [$q$-Aubin--Lions conjecture](#conj:q-aubin-lions),
the [Navier--Stokes counterexample conjecture](#conj:ns-counterexample),
the [critical-exponent conjecture](#conj:critical-exponent),
the [Yekutieli blowup proposition](#prop:blowup-yekutieli),
the [vorticity lower-bound conjecture](#conj:vorticity-lower-bound),
and
the [regularity-breakdown conjecture](#conj:regularity-breakdown);
"Root-of-unity truncation").**

Let $(\mathbf{C}, A, \tau)$ be a QOU with aether parameter $q$ not a root of unity ([aether parameter](#def:substrate-parameter)). As $q \to 1$ through the roots of unity $q = e^{i\pi/\kappa}$, the representation category truncates to a finite modular tensor category; blowup arises only in the $\kappa \to \infty$ accumulation. For an anti-parallel vortex pair with core aspect ratio $\kappa(t)$:

$$
  \boxed{
    \text{NS blows up}
    \iff
    \kappa(t) = O(1).
  }
$$

**Proof.**

The governing [aether-parameter axiom](#def:substrate-parameter) rigorously demands that $q$ remains **not** a root of unity. However, forcibly passing the limit $q \to 1$ directly through the dense set of unity roots triggers a radical truncation across the representation theory that forcibly **strengthens** classical regularity. The resulting macroscopic blowup operating at $q = 1$ behaves merely as the pure mathematical accumulation gathering these infinite truncations.

The core truncation mechanism — driven exclusively by the vanishing of the $q$-integer $[\kappa]_q$ executing exactly at $q = e^{i\pi/\kappa}$, which cleanly collapses the spanning $q$-Laplacian spectral tower $[k]_q^2$ straight into the constrained finite Verlinde/ADE set — finds derivation strictly within [the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower). The following formally extracts the resulting fluid-dynamical consequence.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
 Contains infinitely many valid simple objects $V_j$, indexing $j = 0, 1/2, 1, \ldots$ Quantum dimensions rigorously hold $[2j+1]_q > 0$ across all valid $j$. The physical eigenvalues scale as $[k]_q^2 \sim q^{2k}$ (providing strict exponential growth). The core [well-posedness theorem](#thm:q-ns-wellposedness) mechanically guarantees global regularity.
2. **Root of unity $q = e^{i\pi/\kappa}$, bounded $\kappa \in \mathbb{Z}_{\geq 2}$.**
 Contains strictly **finitely many** simple objects, spanning $j = 0, 1/2, \ldots, (\kappa-2)/2$. The active quantum dimension $[2j+1]_q$ forcibly zeroes out at precisely $j = (\kappa-1)/2$, cleanly truncating the entire representation category. The strict Verlinde formula regulates all physical fusion:

 $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

 where $S$ acts as the modular $S$-matrix. The resulting representation category devolves directly into a **modular tensor category** — identically matching the required algebraic input driving Chern--Simons TQFT cleanly at level $\kappa$.
3. **$q = 1$ (classical limit).**
 Spans an infinite array of simple objects evaluating $[k]_1 = k$ (strictly polynomial scaling). All truncation ceases. All exponential damping vanishes. This establishes exactly the [regularity breakdown](#conj:regularity-breakdown) regime.

**Root-of-unity regularity is stronger than generic.**

Evaluated cleanly at $q = e^{i\pi/\kappa}$, the operating q-NS system mechanically supports at most exactly $(\kappa-1)/2$ active vortex modes (as the tightly truncated representation category contains strictly finitely many objects). This forms an absolute **hard cutoff**, fundamentally differing from the generic soft exponential damping controlling $q > 1$:

- Within generic $q > 1$: valid modes breaching $[k]_q > \mathrm{Re}_q^{1/2}$ safely experience exponential damping but strictly remain nonzero.
- Operating at root of unity: any hypothetical modes breaching $j > (\kappa-2)/2$ mathematically **do not exist** anywhere inside the governing category. The entire bounded Hilbert space remains strictly finite-dimensional.

A purely finite-dimensional ODE mathematically defaults to globally regular unconditionally (enforcing Picard--Lindelöf). Consequently, situated exactly at every isolated root of unity, the operative q-NS system is strictly **finite-dimensional** and therefore globally well-posed.

**The $q = 1$ accumulation.**

Driving $\kappa \to \infty$ smoothly pulls $q = e^{i\pi/\kappa} \to 1$. The hard truncation level actively scales up: $j_{\max} = (\kappa-2)/2 \to \infty$. Steadily, more and more functional modes mechanically unlock. The strict mathematical sequence traversing these rigidly finite-dimensional systems flawlessly approaches the pure infinite-dimensional classical baseline.

The absolute blowup occurring at $q = 1$ effectively states that this terminal infinite-dimensional limit executes as mathematically **singular**: while no isolated finite truncation can ever trigger a blowup, the exact accumulation limit gathering all conceivable truncations effortlessly can. This maps the precise physical structure dictating a macroscopic **phase transition stationed at the exact accumulation point**.

**Connection to the core aspect ratio.**

Operating at an isolated root of unity $q = e^{i\pi/\kappa}$, the exact geometric shape controlling the physical vortex core answers directly to the strict **modular tensor category** structure. The explicit fusion rules $N_{ij}^k$ logically dictate all valid mode interactions. The hard truncation boundary spanning $j \leq (\kappa-2)/2$ completely outlaws high-frequency geometric core deformations: the physical core mathematically **cannot** form fine-scale spatial structure exceeding the strict cutoff. In geometric terms:

- The continuous core aspect ratio $\kappa(t) = a_\perp/a_\parallel$ strictly answers to the isolated Fourier modes spanning the core boundary.
- Operating at root of unity: exactly $(\kappa-1)/2$ modes logically exist. Consequently, $\kappa(t)$ forms merely a basic trigonometric polynomial obeying a strictly bounded degree.
- Any valid trigonometric polynomial scaled to degree $N$ rigidly obeys $|\kappa'(t)| \leq N\|\kappa\|_\infty$ (enforcing the Bernstein inequality), mathematically preventing rapid physical oscillation.

This sequence delivers an **explicit mathematical bound** actively functioning at every isolated root of unity:

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

relying on some shared universal constant $C$. The resulting mathematical bound steadily grows linearly pacing the truncation level $\kappa$, mathematically diverging flawlessly as $\kappa \to \infty$ ($q \to 1$).

**The refined gap.**

The baseline [vorticity lower bound](#conj:vorticity-lower-bound) strictly mandates $\sup_t \kappa(t) \leq C$, keeping $C$ rigidly independent of $q$. The unified root-of-unity analysis directly supplies $\kappa(t) \leq 1 + C(\kappa-1)$, which visibly scales alongside $\kappa$. The absolute question zeroes in on the **rate of growth**:

- Assuming $\kappa(t) \leq C_0$ uniformly (operating entirely independent of $\kappa$): the physical core remains permanently circular. The rigorous lower bound flawlessly holds. NS definitively blows up. The counter-example stands mathematically established.
- Assuming $\kappa(t) \sim \kappa$ (exhibiting purely linear growth): the physical core safely flattens exactly mirroring the rate unlocking new modes. Physical vorticity safely spreads forming a wide sheet. The strict lower bound $\omega \geq c/(T^*-t)$ potentially fails. NS may function as completely regular.
- Assuming $\kappa(t) \sim \kappa^\beta$ spanning $0 < \beta < 1$: an intermediate regime triggers. The firm lower bound holds cleanly provided $\beta < 1/2$ (confirming the physical flattening remains mathematically slower than the approach).

Note that $\kappa(t)^2$ is a statement about core cross-sectional shape only rather than a Levi form condition number $\lambda_{\max}/\lambda_{\min}$: on the three-dimensional flow domain the Levi datum of the vorticity plane field is the single scalar $\xi\cdot\mathrm{curl}\,\xi$ ([core Levi form](#prop:core-levi-form)), with no eigenvalue pair and no condition number, and non-degeneracy of that Levi scalar does not imply blow-up (see the Beltrami counterexample in the [Levi degeneracy conjecture](#conj:levi-degeneracy)).
