**Conjecture (D19 quantum Langlands duality closure).**
*The Iwahori–Hecke algebra $H_n(q)$ admits a quantum Langlands dual $H_n(q^{-1})$ obtained by inverting the deformation parameter. Under the Cartan-folding picture (where Type $A_{n-1}$ is self-dual via ${}^L\!A_{n-1} = A_{n-1}$ but with parameter inversion), this duality satisfies:*

- *It is distinct from the bar involution $\bar q = q^{-1}$ ([`def:bar-involution`](#def:bar-involution), D1). Langlands duality acts on the Hecke algebra structure (root data) at fixed generators. The bar involution acts on the generator action at fixed root data.*
- *It coincides with the reverse-limit $q \to \infty$ ([`conj:reverse-limit-q-to-infinity`](#conj:reverse-limit-q-to-infinity), D13) for non-classical specialisations.*
- *For non-simply-laced types (Type B, C, D, $G_{2}$, $F_{4}$), it yields a genuinely distinct dual algebra (e.g., swapping Type B and Type C).*

## Significance

For Type $A_{n-1}$, the Langlands dual is self-dual at the algebra level. The parameter inversion $q \to q^{-1}$ produces a non-trivial $\mathbb{Z}/2$ duality. The $H_n(q)$ algebra possesses a natural Langlands-dual perspective at $q^{-1}$ that:

- Connects to the D13 reverse-limit at $q \to \infty$. This limit extends the Langlands continuation beyond the unit disc.
- Connects to D22 Type-B folding for non-simply-laced extensions, where Langlands duality exchanges Type B and Type C.
- Supplies a categorical origin for the symmetric/antisymmetric mass-tower decomposition, equating matter with Langlands-dual antimatter.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration:** The Coxeter group structure remains invariant, as Langlands duality preserves length. Only the $q$-parameter inverts.
- **Jet order:** The duality operates on the algebra structure rather than the generator action, distinguishing it from the bar involution.
- **Bar-symmetry:** The duality differs from the bar involution algebraically but coincides parametrically (both invert $q$). The combined Langlands $\times$ bar action provides the relevant duality for the matter/antimatter structure.

## Open R&D

1. Determine whether the mass-tower decomposition admits a Langlands-dual interpretation (matter corresponding to antimatter via Type-A self-duality with $q$-inversion).
2. Connect to D22 Type-B folding. For non-simply-laced extensions, the Langlands dual swap between Type B and Type C structurally realises CPT symmetry.
3. Closing D19 requires a Lean class instance for the Langlands functor (currently absent from Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D19
- D13 [`conj:reverse-limit-q-to-infinity`](../stochastic-mechanics/reverse-limit-q-to-infinity.md) — Langlands-paired limit
- D22 [`conj:type-b-folding-cpt`](../particle-interactions/type-b-folding-cpt.md) — non-simply-laced Langlands dual
- [Macdonald 1971; Lusztig 1989; Frenkel–Reshetikhin 2002 for quantum-Langlands]
