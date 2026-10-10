Proof strategy for [archimedean QOU is the standard-part of surreal QOU](#conj:archimedean-stpart). The conjecture is the category-level counterpart of [classical-limit-stpart](#conj:classical-limit-stpart). Reduce to that conjecture via:

1. **Functorial reduction.** Show $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St}, \mathrm{St})$.
2. **Reduce each component**:
   - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at $q = 1 + \varepsilon$: $\mathrm{St}$ recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by [classical-limit-stpart](#conj:classical-limit-stpart).
   - $\varTheta : \mathbf{1} \to A$: $\mathrm{St}$ acts entry-wise.
   - $G = \mathrm{Aut}(A)$: standard-part of an algebraic group object. This is the categorical counterpart of the archimedean realization $\tau$ of [fibre functor rigidity](#rem:fibre-functor-rigidity).
   - $\mathcal{S}$: standard-part of fibre.
3. **Verify axioms.** Each $\varepsilon$-relaxed axiom becomes the strict axiom under $\mathrm{St}$.
4. **Essential surjectivity.** Every archimedean QOU lifts (set $\varepsilon = 0$).

Falsification requires an $\varepsilon$-relaxed surreal QOU whose standard-part image violates a strict QOU axiom. This would require an infinitesimal that becomes non-infinitesimal under standard-part, which is impossible by the definition of $\mathrm{st}$.
