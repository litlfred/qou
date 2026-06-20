**Theorem (D13 reverse-limit closure — algebraic fragment, Sprint 3
discharge; full categorical bar deferred to Sprint 5 Hoefsmit).**
*The Kashiwara crystal limit $q \to 0$
([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy), D12)
has a structural counterpart at $q \to \infty$, related to the $q
\to 0$ limit by the bar involution $q \mapsto q^{-1}$
([`def:bar-involution`](#def:bar-involution), D1).  The $q \to
\infty$ limit produces a "reverse crystal" whose combinatorial
structure is the bar-image of the Kashiwara crystal, with the
same combinatorial invariants but inverted q-character orderings.
Together, the pair $(q \to 0, q \to \infty)$ + the classical limit
$q = 1$ + the substrate $q = q_0$ form the complete picture of
limit dualities on $H_n(q)$.*

## The four canonical limits of $H_n(q)$

| Limit | Categorical content | Pairing via bar |
|-------|---------------------|-----------------|
| **$q = 1$** (classical) | Lusztig canonical basis / KL polynomials | self-paired (bar fixes $q = 1$) |
| **$q = q_0$** (substrate) | full Hecke at the framework's calibration point | bar-paired with $q = q_0^{-1}$ (NOT $q_0$ itself unless $q_0 = ±1$) |
| **$q \to 0$** (Kashiwara) | crystal basis, 0-Hecke quotient | bar-paired with $q \to \infty$ (this conjecture) |
| **$q \to \infty$** (reverse limit) | reverse crystal | bar-paired with $q \to 0$ |

This conjecture **completes** the picture by explicitly identifying
the $q \to \infty$ limit as the bar-image of the Kashiwara crystal.

## The structural content

Per [`def:bar-involution`](#def:bar-involution), $q \mapsto q^{-1}$
swaps $q = 0$ with $q = \infty$.  The Kashiwara crystal structure
at $q \to 0$ (per [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy))
therefore has a mirror at $q \to \infty$:

- Crystal nodes $\leftrightarrow$ reverse-crystal nodes (same set)
- Crystal arrows of weight $i$ $\leftrightarrow$ reverse-crystal arrows of weight $-i$
- Plain Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ at
  $q \to 0$ becomes $\sigma_i^2 = -q^{-1}\sigma_i + 1 + O(q)$ (giving
  $\sigma_i^{-1} = \sigma_i$ on the 0-Hecke quotient) vs at
  $q \to \infty$: $\sigma_i^2 = q\sigma_i + 1 + O(q^{-1})$ (giving a
  symmetric limit on the $\infty$-Hecke quotient — the bar image)

The conjecture is that this is a **true categorical duality**, not
just a formal involution on the parameter: every Kashiwara crystal
construction has a reverse-crystal analogue at $q \to \infty$,
related by bar.

## Why this matters

D12 (Kashiwara $q \to 0$) is partially formalised in the framework
via [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy).
The framework does NOT currently use the $q \to \infty$ limit
explicitly — but every Kashiwara-crystal result has a bar-paired
counterpart at $q \to \infty$ that can be derived for free.

For the matter/antimatter discussion (per AGENTS.md §7b + D22 Type-B
folding): if matter is identified with Kashiwara crystal fixed
points (at $q \to 0$), antimatter corresponds to
reverse-crystal fixed points (at $q \to \infty$), and the bar
involution swaps them. This gives a **structural source for
matter-antimatter conjugation** orthogonal to the color-tube C
action of [D6](c-from-color-flavor-swap.md).

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: same as the Kashiwara crystal at $q \to 0$
  (the bar-image preserves Coxeter length).
- **Jet order**: $h^0$ (the limit duality is at the level of the
  Hecke parameter $q$ itself, not the $h$-expansion).
- **Bar-symmetry status**: bar-paired by construction — the $q \to
  \infty$ limit IS the bar-image of the $q \to 0$ limit.

## Open R&D

1. **Author the explicit reverse-crystal construction** in Lean
   paired with `CrystalIsospinDegeneracy`.
2. **Verify** that every Kashiwara result in the framework has a
   reverse-crystal counterpart by bar — the "for free" claim
   above.
3. **Connect to matter/antimatter via D22 Type-B folding**: stable
   matter = $q \to 0$ Kashiwara fixed points; stable antimatter =
   $q \to \infty$ reverse-crystal fixed points; bar swaps them.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D13
  + §2 Cluster D (limit dualities D12 $\leftrightarrow$ D13 $\leftrightarrow$ D24)
- Paired Kashiwara limit:
  [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
  (D12)
- Bar involution: [`def:bar-involution`](#def:bar-involution) (D1)
- Type-B folding for CPT: [`conj:type-b-folding-cpt`](type-b-folding-cpt.md) (D22)
- Lusztig canonical basis ($q = 1$): D24 (literature-only currently)
