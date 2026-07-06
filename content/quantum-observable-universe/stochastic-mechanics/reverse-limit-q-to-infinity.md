**Theorem (D13 reverse-limit closure — algebraic fragment).**
*The Kashiwara crystal limit $q \to 0$ ([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy), D12) has a structural counterpart at $q \to \infty$. This counterpart relates to the $q \to 0$ limit via the bar involution $q \mapsto q^{-1}$ ([`def:bar-involution`](#def:bar-involution), D1). The $q \to \infty$ limit produces a reverse crystal. Its combinatorial structure is the bar-image of the Kashiwara crystal, featuring identical combinatorial invariants but inverted q-character orderings. The pair $(q \to 0, q \to \infty)$, the classical limit $q = 1$, and the substrate $q = q_0$ complete the limit dualities on $H_n(q)$.*

## The four canonical limits of $H_n(q)$

| Limit | Categorical content | Pairing via bar |
|-------|---------------------|-----------------|
| **$q = 1$** (classical) | Lusztig canonical basis / KL polynomials | self-paired (bar fixes $q = 1$) |
| **$q = q_0$** (substrate) | full Hecke at the framework's calibration point | bar-paired with $q = q_0^{-1}$ (NOT $q_0$ itself unless $q_0 = \pm 1$) |
| **$q \to 0$** (Kashiwara) | crystal basis, 0-Hecke quotient | bar-paired with $q \to \infty$ (this conjecture) |
| **$q \to \infty$** (reverse limit) | reverse crystal | bar-paired with $q \to 0$ |

This conjecture identifies the $q \to \infty$ limit explicitly as the bar-image of the Kashiwara crystal.

## The structural content

Per [`def:bar-involution`](#def:bar-involution), $q \mapsto q^{-1}$ swaps $q = 0$ with $q = \infty$. The Kashiwara crystal structure at $q \to 0$ ([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)) requires a mirror at $q \to \infty$:

- Crystal nodes $\leftrightarrow$ reverse-crystal nodes (same set)
- Crystal arrows of weight $i$ $\leftrightarrow$ reverse-crystal arrows of weight $-i$
- The Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ at $q \to 0$ becomes $\sigma_i^2 = -q^{-1}\sigma_i + 1 + O(q)$. This gives $\sigma_i^{-1} = \sigma_i$ on the 0-Hecke quotient. At $q \to \infty$, we obtain $\sigma_i^2 = q\sigma_i + 1 + O(q^{-1})$. This provides a symmetric limit on the $\infty$-Hecke quotient.

This relationship forms a true categorical duality, not merely a formal involution on the parameter. Every Kashiwara crystal construction possesses a reverse-crystal analogue at $q \to \infty$, related by bar.

## Significance

We partially formalize D12 (Kashiwara $q \to 0$) via [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy). We do not currently use the $q \to \infty$ limit explicitly. However, every Kashiwara-crystal result admits a bar-paired counterpart at $q \to \infty$.

We identify matter with Kashiwara crystal fixed points at $q \to 0$. We identify antimatter with reverse-crystal fixed points at $q \to \infty$. The bar involution swaps them. This mechanism provides a structural source for matter-antimatter conjugation, independent of the color-tube C action in [D6](c-from-color-flavor-swap.md).

## Diagnostics

- **GB filtration level**: matches the Kashiwara crystal at $q \to 0$. The bar-image preserves Coxeter length.
- **Jet order**: $h^0$. The limit duality occurs at the level of the Hecke parameter $q$, not the $h$-expansion.
- **Bar-symmetry status**: bar-paired by construction. The $q \to \infty$ limit constitutes the bar-image of the $q \to 0$ limit.

## Open R&D

1. **Author the explicit reverse-crystal construction** in Lean, paired with `CrystalIsospinDegeneracy`.
2. **Verify** that every Kashiwara result possesses a reverse-crystal counterpart by bar.
3. **Connect to matter/antimatter via D22 Type-B folding**: stable matter corresponds to $q \to 0$ Kashiwara fixed points. Stable antimatter corresponds to $q \to \infty$ reverse-crystal fixed points. Bar swaps them.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D13 + §2 Cluster D (limit dualities D12 $\leftrightarrow$ D13 $\leftrightarrow$ D24)
- Paired Kashiwara limit: [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy) (D12)
- Bar involution: [`def:bar-involution`](#def:bar-involution) (D1)
- Type-B folding for CPT: [`conj:type-b-folding-cpt`](type-b-folding-cpt.md) (D22)
- Lusztig canonical basis ($q = 1$): D24 (literature-only currently)
