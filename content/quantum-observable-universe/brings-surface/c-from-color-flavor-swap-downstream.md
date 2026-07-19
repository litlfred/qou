## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once D6, D7, D8 close.
- The matter/antimatter sheet structure on Bring's quintic surface ([`def:color-tube-fibers`](color-tube-fibers.md)) acquires a natural C-action that descends to the SO(3) fiber.
- Type-B folding for chirality / CPT (AGENTS.md §7b, **D22** in the duality tracker) emerges as the symmetric-crystal analogue of this conjecture. Folding the $\mathfrak{sl}_n$ Cartan datum to Type B realises C as a symmetric-crystal structure.

## Open R&D

1. **Compute prototype**: `verify_c_color_swap.py`—verify numerically at $q_0$ that the flavor-conjugation involution on the proton/neutron color-tube tensor leaves the canonical Hecke generator invariant.
2. **Close D7 and D8**—author `conj:p-from-braid-mirror` and `conj:t-from-trace-cyclicity` to complete the CPT decomposition.
3. **Promote to proposition** once [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube) and the $S_{5}$$\leftrightarrow$SO(3) fiber-action class (PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3) resolve.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D6 (this conjecture) + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Upstream class: [`conj:inter-nucleon-channel-color-tube`](#conj:inter-nucleon-channel-color-tube) (PR [#1111](https://github.com/litlfred/qou/pull/1111) merged)
- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) (CPT composite already formalised)
- [`bar-involution.md`](bar-involution.md)—the bar-involution = CPT composite identification at the algebraic level
- AGENTS.md §7b—Type-B folding for chirality / CPT (symmetric-crystal authoring shortcut, D22)
