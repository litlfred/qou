**Conjecture (reverse-limit closure — algebraic fragment).**

*The Kashiwara crystal limit $q \to 0$ ([crystal isospin degeneracy](#prop:crystal-isospin-degeneracy)) has a structural counterpart at $q \to \infty$, related to the $q \to 0$ limit by the bar involution $q \mapsto q^{-1}$ ([bar involution](#def:bar-involution), D1).*

*The $q \to \infty$ limit produces a "reverse crystal" whose combinatorial structure is the bar-image of the Kashiwara crystal, with the same combinatorial invariants but inverted $q$-character orderings. Together, the pair $(q \to 0, q \to \infty)$ + the classical limit $q = 1$ + the aether parameter $q = q_0$ form the complete picture of limit dualities on $H_n(q)$.*

## The four canonical limits of $H_n(q)$

| Limit | Categorical content | Pairing via bar |
|-------|---------------------|-----------------|
| **$q = 1$** (classical) | Lusztig canonical basis / KL polynomials | self-paired (bar fixes $q = 1$) |
| **$q = q_0$** (aether) | full Hecke at the framework's calibration point | bar-paired with $q = q_0^{-1}$ |
| **$q \to 0$** (Kashiwara) | crystal basis, 0-Hecke quotient | bar-paired with $q \to \infty$ (this conjecture) |
| **$q \to \infty$** (reverse limit) | reverse crystal | bar-paired with $q \to 0$ |

## The structural content

Per the [bar involution](#def:bar-involution), $q \mapsto q^{-1}$ swaps $q = 0$ with $q = \infty$. The Kashiwara crystal structure at $q \to 0$ has a mirror at $q \to \infty$:
- Crystal nodes $\leftrightarrow$ reverse-crystal nodes.
- Crystal arrows of weight $i$ $\leftrightarrow$ reverse-crystal arrows of weight $-i$.

The conjecture is that this is a true categorical duality. Every Kashiwara crystal construction has a reverse-crystal analogue at $q \to \infty$, related by bar.

## Significance

If matter is identified with Kashiwara crystal fixed points (at $q \to 0$), antimatter corresponds to reverse-crystal fixed points (at $q \to \infty$), and the bar involution swaps them. This gives a structural source for matter-antimatter conjugation orthogonal to the colour-tube charge-conjugation action of the [colour-flavour swap conjecture](#conj:c-from-color-flavor-swap).

## Diagnostics

- **GB filtration level**: same as the Kashiwara crystal at $q \to 0$.
- **Jet order**: $h^0$.
- **Bar-symmetry status**: bar-paired by construction.
