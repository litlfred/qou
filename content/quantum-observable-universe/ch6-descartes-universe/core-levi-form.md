The [vorticity lower bound](#prop:vorticity-lower-bound) reduces
to a geometric statement about vortex core shape.  This remark
identifies it with the condition number of the
[Levi form](#rem:levi-form-defect).

**Core cross-section geometry.**
At each point $p$ on a vortex filament $\gamma$, the normal
plane $N_p\gamma$ contains the core cross-section.  Define:

- $a_\parallel$: core radius toward the other filament
- $a_\perp$: core radius perpendicular to the approach
- $\kappa = a_\perp / a_\parallel$: aspect ratio

The Levi form $\mathcal{L}_\theta$ restricted to $N_p\gamma$
has eigenvalues $\lambda_\parallel, \lambda_\perp$.  The
[substrate parameter](#def:substrate-parameter) at $p$ is
$q(p) = 1 + |\langle\mathcal{L}_\theta, F_A^+\rangle|$,
and the core shape is controlled by the eigenvalue ratio:

$$
  \kappa = \frac{a_\perp}{a_\parallel}
  \sim \sqrt{\frac{\lambda_\parallel}{\lambda_\perp}}.
$$

**The equivalences.**

| Core geometry | Levi form | Contact structure | Fluid |
|---|---|---|---|
| $\kappa = 1$ (circular) | $\lambda_\parallel = \lambda_\perp$ | Isotropic contact | Tubular vortex |
| $\kappa \to 0$ (flattened) | $\lambda_\parallel \to 0$ | Partially integrable | Vortex sheet |
| $\kappa \to \infty$ (elongated) | $\lambda_\perp \to 0$ | Partially integrable | Vortex needle |
| $\kappa = O(1)$ (bounded) | Condition number bounded | Non-degenerate contact | Blowup occurs |

The Frobenius integrability theorem says: the horizontal
distribution $\ker(\theta)$ is integrable iff
$d\theta|_H = 0$, i.e. the Levi form vanishes.
Core flattening ($\kappa \to 0$ or $\infty$) is precisely
the Levi form degenerating in one direction — the contact
structure **becomes partially integrable** along the
flattened axis.

When this happens:

1. A 2-dimensional integral submanifold forms (the vortex
   sheet).
2. The [observability condition](#def:quantum-observable-universe)
   $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ fails locally
   — a gauge mode acts trivially in the integrable direction.
3. The vortex ceases to be a well-defined topological defect
   at that point.

**Why $q > 1$ prevents flattening.**
The [quantum pressure](#rem:madelung-fluid)
$Q_q = -(\hbar_q^2/2)\,\Delta_q\sqrt{\rho}/\sqrt{\rho}$
is isotropic in the $q$-deformed metric because $\Delta_q$
respects the contact structure.  If the core tries to flatten
($a_\parallel \to 0$), the quantum pressure diverges as
$\hbar_q^2/a_\parallel^2$ in that direction, preventing it.
The equilibrium shape minimises the
[q-energy functional](#rem:geodesic-vortices), which has
the same $Q_q$ in both directions:

$$
  \kappa_{\mathrm{eq}} = 1 + O(\hbar_q^2) < \infty
  \qquad\text{for } q > 1.
$$

At $q = 1$: $Q_q = 0$ and there is no isotropic resistance.

**The millennium problem in contact-geometric form.**

$$
  \boxed{
    \text{NS blows up}
    \;\Longleftrightarrow\;
    \text{Levi form non-degenerate at collision}
    \;\Longleftrightarrow\;
    \kappa(t) = O(1).
  }
$$

Does the contact structure of the brane remain non-degenerate
at the collision point of two vortex filaments when $q = 1$?

If yes: the vorticity concentrates (cores stay tubular), the
lower bound $\|\omega\|_\infty \geq c/(T^*-t)$ holds, and
the [counter-example](#conj:ns-counterexample) is established.

If no: the vorticity spreads into a sheet (cores flatten),
the lower bound fails, and classical NS may be regular.
