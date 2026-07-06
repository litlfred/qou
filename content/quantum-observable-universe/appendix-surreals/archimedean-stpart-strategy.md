This remark outlines a proof strategy for [archimedean QOU is the standard-part of surreal QOU](#conj:archimedean-stpart). The conjecture remains open.

The conjecture is the category-level counterpart of [classical-limit-stpart](#conj:classical-limit-stpart). We reduce to that conjecture via four steps.

1. **Functorial reduction.** Show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$. The standard-part applies component-wise to the QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

2. **Reduce each component.**
 - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at $q = 1 + \varepsilon$. The functor $\mathrm{St}$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by [classical-limit-stpart](#conj:classical-limit-stpart).
 - $\varTheta : \mathbf{1} \to A$. This is an element of a hom-space. $\mathrm{St}$ acts entry-wise.
 - $G = \mathrm{Aut}(A)$. We take the standard-part of this algebraic group object. This is the categorical counterpart of the archimedean realization $\tau$ of [fibre functor rigidity](#rem:fibre-functor-rigidity), the image of the rigid monoidal embedding into $\mathbb{R}$-linear endomorphisms.
 - $\mathcal{S}$. We take the standard-part of the state bundle fibre.

3. **Verify axioms.** Each $\varepsilon$-relaxed axiom (Frobenius, observability, volume, vacuum) becomes strict under $\mathrm{St}$. This relies on [infinitesimal-frobenius](#conj:infinitesimal-frobenius), [infinitesimal-observability](#conj:infinitesimal-observability), and [vacuum-epsilon](#conj:vacuum-epsilon).

4. **Essential surjectivity.** Every archimedean QOU lifts by setting $\varepsilon = 0$. This direction is automatic.

**Required infrastructure:**

- The five sub-conjectures above.
- A `Functor` instance from `QOU_𝐍𝐨^ε` to `QOU_ℝ` in Lean.
- The `CategoryTheory.MonoidalFunctor` interaction with $\mathrm{St}$.

**Falsification path.** Exhibit an $\varepsilon$-relaxed surreal QOU whose standard-part violates a strict QOU axiom. For example, the Frobenius pairing of the standard-part has positive nullity. This requires an infinitesimal that becomes non-infinitesimal under the standard-part. This contradicts the definition of $\mathrm{st}$.

**Provability assessment.** The proof is structurally clean once the sub-conjectures hold. The remaining argument is bookkeeping over the four QOU components.
