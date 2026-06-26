**Conjecture (q-harmonic-map heat flow for the substrate field).**
*The substrate parameter $q(p)$, promoted from a fixed modulus to a
field over the base, evolves in time by the **$q$-harmonic-map heat
flow**:*

$$
  \partial_t\, q \;=\; -\,\Delta_q\, q,
  \qquad
  \Delta_q \;=\; q^{-2}\Delta \;+\; q^{-1}(1-q^{-1})\,\mathfrak{C}
            \;+\; (1-q^{-1})^2\,\Delta_\xi ,
$$

*where $\Delta$ is the base Laplacian, $\mathfrak{C}$ the first-order
Casimir/drift term, and $\Delta_\xi$ the Reeb-fibre Laplacian. Its
stationary configurations $\Delta_q q = 0$ are the **$q$-harmonic
sections**; the vacuum constant $q \equiv q_0$ is the trivial one.*

This is the *dynamical* half of the local-$q$ programme. Route 2a
([germ-commutator $=$ $q$-curvature](#prop:germ-commutator-q-curvature))
supplies the *kinematic* half: the germ $\delta q(p)$ of two
disagreeing observations is the $q$-curvature on the loop they trace.
What 2a leaves open is *time evolution* of $q(p)$ — and that is what
this conjecture postulates.

> **Ansatz, not theorem.** The operator $\Delta_q$ is read off from the
> $q$-heat equation
> ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)),
> whose fundamental solution is the Reeb-invariant $q$-Gaussian with the
> clock running at rate $q^{-2}$. But that proposition governs diffusion
> of a *scalar density at fixed $q$*. Making $q(p)$ **itself** the
> diffusing field is a **new postulate** — the specific PDE above is an
> ansatz, not derived from existing blocks. What is solid is the germ
> $\delta q(p)$ (Route 2a, verified) and its identification with the
> $q$-curvature; the evolution law is conjectural.

The fixed-point equation $\Delta_q q = 0$ is the hand-off to the
$q_0$-selection question (Route 1): the vacuum $q \equiv q_0$ is the
trivial $q$-harmonic section, and a *non-trivial* stationary point
balancing the intrinsic curvature $(q-1)\mathcal{F}_q^{\mathrm{intr}}$
against a Reeb-fibre source would be a candidate selection condition for
$q_0$ — but the naive "$q_0$ is the only fixed point" reading is false
(every constant field is stationary), so selection needs an extra
equation. That remains open and is **not** wired to production.

## Lean

The flow is axiomatised as a class
`QOU.LocalQ.QHarmonicFlow` over an additive group $V$ of field
configurations: a configuration `q`, its time-derivative `dq` $= \partial_t q$,
the $q$-Laplacian `Δq`, and the ansatz law `dq = -Δq q`. The *existence*
of such a structure for the physical substrate field is the conjecture.
Conditional on the class, two structural consequences are
**verified, sorry-free**:

1. `stationary_iff_qharmonic` — the flow is stationary ($\partial_t q = 0$)
   iff the configuration is $q$-harmonic ($\Delta_q q = 0$);
2. `vacuum_stationary` — the trivial (zero/constant) field is stationary,
   i.e. the vacuum is a $q$-harmonic fixed point.

The conjectural content is isolated in the class instance (the ansatz
PDE); the consequences hold for *any* flow of this shape.
