**Uniformity.** A single integer linear program selects the operator at every level of the QOU construction. The same Gram matrix $G$, the same Frobenius check $Gx \geq 0$, and the same ILP are applied to quarks, nucleons, atoms, and molecules.

**The two constraints.**

1. **$K$ is a non-trivial knot.** The unknot leaves the state unchanged.
2. **Frobenius positivity.** The resulting state must be LP-stable.

When the state is **unstable** ($Gx \not\geq 0$), the Frobenius constraint forces a non-trivial $K$ that restores stability, and the LP selects the minimum-crossing knot that achieves $Gx' \geq 0$. When the state is **stable** ($Gx \geq 0$), any non-trivial knot is a candidate; the LP selects the minimum-crossing one, with $|\mathrm{tr}_M|$ minimised as tiebreaker. This is the bond operator.

**Topological hierarchy.** The topological constraint upgrades at each level:

- Level 1 (confinement): the operator must have the **Borromean property**.
- Level 2 (gluon): the operator must restore **Frobenius stability**.
- Level 3 (electron): the operator is the **pe crossing**.
- Level 4 (molecule): the operator must be a **knot**.

**Consistency.** We use the same energy functional $\Phi_1 = \ln|\mathrm{tr}_M|$ and the same Wedderburn-Artin weights at every level. All energy scales are derived from $q_0$ and $m_e$ alone.
