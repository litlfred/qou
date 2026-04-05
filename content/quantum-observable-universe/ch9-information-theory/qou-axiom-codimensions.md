Each QOU axiom cuts the [moduli of quantum
observables](#def:qo-moduli) by a definable condition with a
definite **motivic codimension** in $K_0(\mathbf{C})[L_q^{-1}]$.

1. **Observability**
   ($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$).
   Kills the Lie algebra of $\mathrm{Aut}^\otimes(\tau)$.
   Motivic codimension $= [\mathrm{Ad}(A)^{\mathbf{1}}]$,
   the class of the invariant subspace of the adjoint
   representation. This is the largest cut — it eliminates
   the continuous automorphism group and makes the fibre
   functor rigid.

2. **Measurability** ($c_1 = c_2 = 0$).
   Kills anomalies in the adjoint representation.
   Motivic codimension $= [H^2(\mathbf{C}, \mathbb{G}_m)]$,
   the Brauer-type obstruction class. After observability,
   this is a discrete constraint — the obstruction either
   vanishes or does not.

3. **Volume constraint**
   ($\Lambda^2 V \twoheadrightarrow \mathbf{1}$).
   Forces the gauge group to $\mathrm{SU}(2)$ and pins
   the determinant of $V$. Motivic codimension
   $= [\mathrm{GL}(V)/\mathrm{SU}(V)]$, measuring the
   coset of gauge groups that fail the volume constraint.

The total motivic codimension of the QOU locus is the
**product** of the three individual codimensions:

$$
  \mathrm{codim}_{\mathrm{mot}}(\mathfrak{M}_{\mathrm{QOU}})
  \;=\; [\mathrm{Ad}(A)^{\mathbf{1}}]
  \;\cdot\; [H^2(\mathbf{C}, \mathbb{G}_m)]
  \;\cdot\; [\mathrm{GL}(V)/\mathrm{SU}(V)]
$$

The [axiom independence](#rem:axiom-independence) result ensures
no factor is trivial — the axioms cut transversely.

"Logical existence is a categorical quantity": each axiom has
a measurable cost in the Grothendieck ring. The observability
axiom is the most expensive (eliminating continuous families),
measurability is intermediate (discrete obstruction), and the
volume constraint is the finest (selecting a specific gauge
group within the discrete family). Together they select a
rigid sublocus from a continuous moduli.
