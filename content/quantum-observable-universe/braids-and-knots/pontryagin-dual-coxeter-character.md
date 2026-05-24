**Conjecture (D20 Pontryagin closure — restricted, low priority).**
*The abelianisation $S_n^{\mathrm{ab}} \cong \mathbb{Z}/2$ of the
Coxeter group $S_n$ carries a Pontryagin duality on its character
group $\widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2$ — characters ↔
measures on the dual group.  This is **degenerate** (Z/2 is self-
Pontryagin-dual) but provides the framework with a low-information
abelian-level duality structure paired with the bar involution
(D1).*

## Status: degenerate / low priority

The full Pontryagin duality theorem applies to locally-compact
**abelian** groups.  The QOU framework's central objects ($S_n$
Coxeter group, Hecke algebra $H_n(q)$, braid group $B_n$) are all
**non-abelian** — so Pontryagin duality applies only after
abelianisation, which collapses most structure.

For $n \geq 2$:

$$
  S_n^{\mathrm{ab}} \;=\; \mathbb{Z}/2 \quad
  \text{(via the sign homomorphism)}
$$

The character group is $\widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2$,
giving a self-dual Pontryagin structure. This is **not load-
bearing** for any framework derivation — the abelianisation throws
away exactly the categorical structure the rest of the tracker is
about.

## Why we record it anyway

D20 is included in the duality tracker for **completeness**: the
13-driver categorical menu mentions "Pontryagin / Cartier /
Kashiwara crystal q → 0 / q → ∞" as a research direction. This
block establishes that the Pontryagin part of that menu IS
applicable but yields no new information beyond the sign-of-a-
permutation observable — i.e., the same Z/2 that the bar involution
already classifies.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — abelianisation collapses the filtration.
- **Jet order**: $h^0$ — Pontryagin is a parameter-independent
  abelian duality.
- **Bar-symmetry**: identical to bar at the abelianised level.

## Open R&D

D20 → ✅ would require formalising the abelianisation map and the
trivial Pontryagin structure. Low priority because:

1. No framework derivation depends on it.
2. The non-trivial categorical content is captured by the
   non-abelian dualities D1–D19, D22.

Documented and parked.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D20
- D1 [`def:bar-involution`](#def:bar-involution) — the non-trivial
  Z/2 that subsumes the abelianised case
- [Pontryagin 1934; Hewitt–Ross 1979 for locally-compact abelian
  duality]
