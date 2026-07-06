A QOU is an archimedean tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$ ([quantum observable universe](#def:quantum-observable-universe)). The categorical algebra $\mathbf{C}$ is $K$-linear with $K = \mathbb{R}$ implicit. The gauge group $G$ is a real Lie group. The state bundle $\mathcal{S}$ is a real vector bundle.

A **surreal QOU** is the same data with $K = \mathbf{No}$. We relax all axioms to hold up to an infinitesimal.

| Axiom | Archimedean | Surreal |
|---|---|---|
| Frobenius pairing | $\int_A \circ \mu = \mathrm{id}$ | $= \mathrm{id} + O(\varepsilon)$ |
| Observability | $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ | $\leq \varepsilon$ |
| Volume | $g_{\mathbf{1}} = \mathrm{id}$ | $= (1 + \varepsilon) \mathrm{id}$ |
| Vacuum | $\mathrm{Geom}(\unicode{9737}) = 0$ | $= \varepsilon$ |

Each relaxation uses the named infinitesimal $\varepsilon \in \mathbf{No}$ from [surreal blow-up calculus](#def:surreal-blowup-calculus).

## Conjecture

The standard-part functor $\mathrm{St}$ ([standard-part functor](#def:standard-part-functor)) sends every surreal QOU to an archimedean QOU. We define a functor

$$
  \mathrm{St}_{\mathrm{QOU}} :
   \mathbf{QOU}_{\mathbf{No}}^{\varepsilon}
   \longrightarrow
   \mathbf{QOU}_{\mathbb{R}},
$$

from the category of surreal QOUs (with $\varepsilon$-relaxed axioms) to archimedean QOUs (with strict axioms). We apply $\mathrm{St}$ to all hom-spaces. This functor is **essentially surjective**. Every archimedean QOU lifts to a surreal QOU. The composition $\mathrm{St}_{\mathrm{QOU}} \circ \iota$ is the identity, where $\iota$ is the inclusion of archimedean QOUs as the "$\varepsilon = 0$" surreal QOUs.

## Strength

If this conjecture holds, the surreal lift carries more information than the archimedean theory. Each archimedean QOU has a fibre of surreal QOUs above it. This fibre is parametrised by the infinitesimal-correction data $\{\varepsilon, \varepsilon^2, \ldots\}$ allowed by the relaxed axioms. Two non-isomorphic surreal QOUs may have the same standard-part image. The additional information is infinitesimal physics. It provides first-order quantum corrections to the Frobenius pairing, observability cohomology, volume normalisation, and vacuum.

It remains open whether these infinitesimal corrections are physical (distinguishing observable predictions) or mathematical (distinguished only by the surreal structure).

## Relation to the classical-limit conjecture

This conjecture is the categorical counterpart of [classical limit as standard-part](#conj:classical-limit-stpart). 

- Classical-limit-stpart states that the $q \to 1$ classical-limit functor on $\mathbf{C}_q$ is $\mathrm{St} \circ \mathrm{ev}_{1 + \varepsilon}$. This is a single-category statement.
- Archimedean-stpart states that the entire QOU framework $(\mathbf{C}, \varTheta, G, \mathcal{S})$ is the standard-part of an $\varepsilon$-relaxed surreal QOU. This is a whole-tuple statement.

The two conjectures are equivalent modulo functoriality. A precise reduction is open.

## Consequences of the lift

If true, the $\varepsilon$-relaxation is a strict generalisation of the main paper.

1. We recover the strict QOU axioms by applying $\mathrm{St}_{\mathrm{QOU}}$ to the surreal axioms.
2. Every theorem proved in the main paper has a surreal counterpart. This counterpart may have non-trivial first-order corrections that vanish under $\mathrm{St}$.
3. Future work can investigate whether these corrections have physical significance. For example, they may explain corrections to the QOU mass formula's $4\%$ MAE on $\mathcal{Q}$-values.
## Proof strategy

This conjecture is the category-level counterpart of [classical-limit-stpart](#conj:classical-limit-stpart). We reduce to that conjecture via four steps.

1. **Functorial reduction.** Show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$. The standard-part applies component-wise to the QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

2. **Reduce each component.** 
 - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at $q = 1 + \varepsilon$. The functor $\mathrm{St}$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by [classical-limit-stpart](#conj:classical-limit-stpart).
 - $\varTheta : \mathbf{1} \to A$. This is an element of a hom-space. $\mathrm{St}$ acts entry-wise.
 - $G = \mathrm{Aut}(A)$. We take the standard-part of this algebraic group object.
 - $\mathcal{S}$. We take the standard-part of the state bundle fibre.

3. **Verify axioms.** Each $\varepsilon$-relaxed axiom (Frobenius, observability, volume, vacuum) becomes strict under $\mathrm{St}$. This relies on [infinitesimal-frobenius](#conj:infinitesimal-frobenius), [infinitesimal-observability](#conj:infinitesimal-observability), and [vacuum-epsilon](#conj:vacuum-epsilon).

4. **Essential surjectivity.** Every archimedean QOU lifts by setting $\varepsilon = 0$. This direction is automatic.

**Required infrastructure:**
- The five sub-conjectures above.
- A `Functor` instance from `QOU_No^ε` to `QOU_ℝ` in Lean.
- The `CategoryTheory.MonoidalFunctor` interaction with $\mathrm{St}$.

**Falsification path.** Exhibit an $\varepsilon$-relaxed surreal QOU whose standard-part violates a strict QOU axiom. For example, the Frobenius pairing of the standard-part has positive nullity. This requires an infinitesimal that becomes non-infinitesimal under the standard-part. This contradicts the definition of $\mathrm{st}$.

**Provability assessment.** The proof is structurally clean once the sub-conjectures hold. The remaining argument is bookkeeping over the four QOU components.
