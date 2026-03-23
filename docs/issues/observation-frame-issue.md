## Summary

Rewrite the foundational definitions in Chapter 1 to use **Observation Frame** as the formal designation for the fibre functor, treating the transition from a "Quantum" to an "Observable" state as the physical realization of a coordinate system emerging from topological flatness.

## Changes Required

### Definition 1.3 — Quantum Universe (QU)

A Quantum Universe over a commutative ring $R$ is a triple $(\mathcal{C}, \mathcal{A}, \Omega^1(\mathcal{A}))$ where:

1. $(\mathcal{C}, \otimes, \mathbb{1})$ is an $R$-linear rigid monoidal category.
2. $\mathcal{A}$ is a Frobenius–Hopf object in $\mathcal{C}$ with an integral $\int_{\mathcal{A}}$.
3. $\Omega^1(\mathcal{A})$ is a dualizable $(\mathcal{A}, \mathcal{A})$-bimodule of Kähler differentials.

### Proposition 1.4 — Existence of the Observation Frame

Let $(\mathcal{C}, \mathcal{A}, \Omega^1(\mathcal{A}))$ be a Quantum Universe. If the primary Chern classes of the adjoint object $\mathrm{Ad}(\mathcal{A})$ vanish in the categorical cohomology:

$$c_1(\mathrm{Ad}(\mathcal{A})) = 0 \quad \text{and} \quad c_2(\mathrm{Ad}(\mathcal{A})) = 0$$

then there exists a faithful, exact, monoidal forgetful functor:

$$\omega: \mathcal{C} \longrightarrow R\text{-Mod}$$

termed the **Observation Frame**.

**Significance**: The vanishing of $c_1$ and $c_2$ kills the cohomological obstruction to a global frame, ensuring the universe is "pointable" and can be observed in terms of $R$-modules.

### Definition 1.5 — Quantum Observable Universe (QOU)

A QOU is a Quantum Universe satisfying the vanishing conditions of Proposition 1.4, uniquely equipped with:

1. **The Observation Frame**: The faithful functor $\omega$ guaranteed by topological flatness.
2. **The Categorical Volume**: A non-degenerate epimorphism $\epsilon: V \otimes V^\vee \to \mathbb{1}$ (where $\dim(V)=2$) invariant under automorphisms of the frame $\omega$.
3. **The Observability Condition**: $\mathrm{Hom}_{\mathcal{C}}(\mathbb{1}, \mathrm{Ad}(\mathcal{A})) = 0$, ensuring the frame captures no trivial global symmetries.

## Downstream Logic

- **Integrability**: Defining the Observation Frame as a consequence of $c_1 = c_2 = 0$ aligns with the Nonabelian Stokes requirement. Flatness allows a global coordinate choice.
- **Emergence**: The volume $\epsilon$ is the "residue" of this integrability — it exists because the frame $\omega$ is stable across the entire category.
- **Physical analogy**: QU = "Potentiality", vanishing Chern classes = "Condition of Stability", Observation Frame = "Realized Perspective".

## Open Question: Symbol for the Observation Frame

Consider replacing $\omega$ with $\tau$ or $T$ to avoid confusion with angular frequency / symplectic forms:

| Symbol | Physical interpretation | Rationale |
|--------|----------------------|-----------|
| $\tau$ | Proper time / Frobenius trace | Links observation to the observer's worldline; connects to the trace map in von Neumann algebras |
| $T$ | Tannaka / Transfer matrix | Pays homage to Tannaka-Krein reconstruction; aligns with partition function in statistical mechanics |

## Scope

- Update content objects for Defs 1.3, 1.4 (new Proposition), 1.5
- Update corresponding `.md` narrative files
- Update Lean stubs if definitions change signature
- Propagate any symbol rename ($\omega \to \tau$ or $T$) through all downstream references
