The [time reversal barrier](#rem:time-reversal-energy-barrier) dictates infinite energy for chirality reversal in the observable sector. The [cosmological limits](#ex:cosmological-limits) specify two regimes lacking this topological protection.

**At the Big Bang ($q \to \infty$).**

The Frobenius form degenerates: $\int_A(f^\dagger f) \sim q^{-1} \to 0$. The [Heisenberg commutator](#rem:heisenberg-commutator) $[\hat{X}, \hat{P}]_q \to J$ is maximal. Observables become maximally non-commutative. The positive-definiteness axiom vanishes.

Here, $q$ acquires an imaginary part $\theta \neq 0$. The [complex substrate interpretation](#rem:complex-substrate-interpretation) allows continuous fiber chirality rotation. The [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p$ supports phase rotation $\mathcal{X}_\varphi$ between trefoils and their mirrors. Chirality flips occur in the fibers.

This meets Sakharov's conditions:
1. Frobenius degeneration enables baryon number violation.
2. The deformation magnitude $r = \lvert q\rvert$ supplies CP violation. **Not the phase:** the framework's matter-antimatter discriminant is $\delta_{\mathrm{CP}} = (r^2-1)/(r^2+1)$ for every $\theta$, so $\theta$ is absent from it — see [CP violation evidence](#sec:cp-violation-evidence). In this regime that strengthens the condition rather than weakening it: as $q \to \infty$ the discriminant tends to $1$, its maximum, whereas the phase-based reading would have needed an imperfect projection to leave a residual $\theta_{\mathrm{res}}$.
3. The Big Bang provides non-equilibrium.

Condition 2 being satisfied *maximally* does not close baryogenesis; it sharpens what remains. The framework's asymmetry at the substrate anchor already exceeds the observed baryon-to-photon ratio by $\approx 1.7\times10^{8}$, so the open object is a suppression, not a further source of asymmetry (again [CP violation evidence](#sec:cp-violation-evidence)).

**At heat death ($q \to 1$).**

The Hopf algebra becomes cocommutative. The [quantum Planck constant](#def:substrate-parameter) vanishes. The Descartes color tubes collapse to a single $\mathrm{U}(1)$ phase tube ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)). The crossing-energy asymmetry $q - q^{-1} \to 0$ disappears. The electron and muon survive as indistinguishable topological excitations ([rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)) with vanishing masses.

**Categorical picture (conjectural).**

This requires a category of QOU degenerations $\mathbf{QOU}_{\mathrm{deg}}$ with morphisms preserving structure while selectively degrading axioms:

- The **initial object** represents the Big Bang ($q = \infty$, degenerate Frobenius form).
- The **terminal object** is [Bring's surface](#thm:descartes) ($q = 1$).
- The **observable era** is the full subcategory with $1 < q < \infty$.

**The aeon boundary.**

The $1 < q < \infty$ regime enforces chirality conservation:

1. **Big Bang**: Frobenius degeneration lifts the observability constraint. Chirality flips occur freely.
2. **Observable era**: Chirality is frozen.
3. **Heat death**: The $q \to 1$ limit erases chirality distinctions.

In a cyclic universe, exceptional divisors reset topology at the aeon boundary. The conjecture is that this transition is a morphism from the terminal object of one $\mathbf{QOU}_{\mathrm{deg}}$ to the initial object of the next.
