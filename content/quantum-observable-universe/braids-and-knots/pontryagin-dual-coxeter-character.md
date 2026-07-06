**Theorem (D20 Pontryagin self-duality on $S_n^{\mathrm{ab}}$).**
*For every $n \geq 2$, the abelianisation
$S_n^{\mathrm{ab}} \cong \mathbb{Z}/2$ of the Coxeter group $S_n$
is canonically Pontryagin self-dual: the character group
$\widehat{S_n^{\mathrm{ab}}} = \mathrm{Hom}(\mathbb{Z}/2, \mathbb{C}^\times)$
is canonically isomorphic to $\mathbb{Z}/2$ itself, via the
identification of the unique non-trivial character with the sign
homomorphism.*
## Discussion

This block closes duality tracker entry **D20 — open, low priority** ([`thm:pontryagin-dual-coxeter-character`](#)). Following the Phase-1 Tier-A closure plan ([`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../../../docs/workplans/2026-05-30-source-conjecture-closure-plan.md)), we discharge the theorem using existing Mathlib primitives (`Equiv.Perm.sign`, `ZMod 2` finite-case analysis). The closure introduces no new framework derivation but provides a concrete `Equiv.swap 0 1` witness usable in downstream parity arguments.

## Rationale

We record D20 for completeness. The 13-driver categorical menu lists "Pontryagin / Cartier / Kashiwara crystal $q \to 0$ / $q \to \infty$" as a research direction. This closure confirms the Pontryagin case applies but yields no information beyond the sign-of-a-permutation observable. It isolates the same $\mathbb{Z}/2$ structure classified by the bar involution (D1).

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — abelianisation collapses the filtration.
- **Jet order**: $h^0$ — Pontryagin is a parameter-independent abelian duality.
- **Bar-symmetry**: identical to bar at the abelianised level.

## Cross-references

- [`docs/duality-tracker.md`](../../../docs/duality-tracker.md) D20
- D1 [`def:bar-involution`](#def:bar-involution) — the non-trivial $\mathbb{Z}/2$ that subsumes the abelianised case
- [`docs/workplans/2026-05-30-source-conjecture-closure-plan.md`](../../../docs/workplans/2026-05-30-source-conjecture-closure-plan.md) Phase 1 — Tier A discharge
- [Pontryagin 1934; Hewitt–Ross 1979 for locally-compact abelian duality]
