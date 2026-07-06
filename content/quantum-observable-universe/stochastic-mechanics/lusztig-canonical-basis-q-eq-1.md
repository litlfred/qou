**Conjecture (D24 Lusztig canonical basis closure, conditional on
[`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)).**
*At the classical limit $q = 1$, the Kashiwara crystal of $H_n(q)$
([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy),
D12 at $q \to 0$) **decategorifies** to the Lusztig canonical basis
of the group algebra $\mathbb{Z}[S_n]$.  The Kazhdan–Lusztig basis
polynomials $\{P_{y, w}(q)\}$ are the structure constants of this
decategorification, and at $q = 1$ they reduce to integer
multiplicities of canonical-basis elements.  Combined with the
$q \to 0$ Kashiwara limit (D12) and the $q \to \infty$ reverse
limit ([D13](reverse-limit-q-to-infinity.md)), D24 completes the
**Cluster D limit-duality picture** for $H_n(q)$:*

$$
  \begin{array}{c}
    q \to 0 \text{ (Kashiwara crystal)} \\
    \updownarrow \text{ bar} \\
    q \to \infty \text{ (reverse crystal, D13)} \\
    \\
    q = 1 \text{ (Lusztig canonical basis, this conjecture)} \\
    \updownarrow \text{ specialise} \\
    q = q_0 \text{ (substrate, framework production)} \\
  \end{array}
$$

## The full Cluster D limit-duality picture

| Limit | Categorical structure | Tracker row |
|-------|----------------------|-------------|
| $q = 1$ (classical) | Lusztig canonical basis / KL polynomials | **D24** (this conjecture) |
| $q = q_0$ (substrate $\approx$ 1.11) | full Hecke algebra | (production, all rows) |
| $q \to 0$ (Kashiwara) | crystal basis / 0-Hecke | D12 |
| $q \to \infty$ (reverse) | bar-image of Kashiwara | D13 |

D24 ties D12 (Kashiwara) to D1 (bar) via the decategorification
functor: the Lusztig canonical basis at $q = 1$ is the **bar-
invariant Kazhdan–Lusztig basis** of the group algebra, and the
Kashiwara crystal at $q \to 0$ is its quantum lift via canonical-
basis-preserving deformation.

## Connection to D9 (isospin) and D22 (Type-B folding)

- The isospin Z/2 swap (D9) acts on the Lusztig canonical basis as
  the **sign character** of the abelianised $S_n$ — providing a
  classical-limit picture of the canonical isospin.
- Type-B folding (D22) provides the symmetric-crystal structure
  that descends to a **bar-invariant** Lusztig basis at $q = 1$,
  closing the Cluster A (CPT) story at the decategorification
  level.

## Diagnostics

- **GB filtration**: KL polynomials are filtered by length $\ell(w)$
  — the same filtration as the Hecke algebra.
- **Jet order**: $q = 1$ specialisation; KL polynomials evaluated
  at $q = 1$ are integers (the canonical-basis multiplicities).
- **Bar-symmetry**: bar-symmetric by construction (the KL basis IS
  the bar-invariant basis).

## Open R&D

1. Explicit Kashiwara $\to$ Lusztig decategorification functor in Lean.
2. Verify the framework's canonical Wedderburn weights $y_\lambda$
   at $q = 1$ reduce to KL multiplicities.
3. D24 to closed requires Lean class for the decategorification functor;
   partial Mathlib infrastructure for Kazhdan–Lusztig theory exists.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D24
  + §2 Cluster D (limit dualities D12 / D13 / D24)
- D12 (Kashiwara $q \to 0$):
  [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
- D13 (reverse $q \to \infty$):
  [`conj:reverse-limit-q-to-infinity`](reverse-limit-q-to-infinity.md)
- D9 (isospin classical limit):
  [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md)
- Upstream conjecture:
  [`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)
- [Kazhdan–Lusztig 1979; Lusztig 1990; Kashiwara 1991]
