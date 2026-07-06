**Proposition (B1 keystone at the torus-knot rows).**

*Every torus-knot row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) is a theorem. This requires no part of Goncharov's or Beilinson's conjectures. We combine Bloch–Suslin with Garoufalidis–Lê's proof of the Volume Conjecture for torus knots.*

### Scope

We consider the seven Bring-natural torus-knot generators of [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots):

$$
  \{T(2, 3),\; T(2, 5),\; T(2, 7),\; T(2, 9),\;
    T(3, 4),\; T(3, 5),\; T(5, 2)\}
$$

None are hyperbolic. Their complements are Seifert-fibred. The depth-2 volume claim is zero by definition: $\mathrm{Vol}(T(p, q)) = 0$ in $\mathcal{P}_2 / \mathcal{P}_1$. This trivial row of B1 is a theorem by definition.

The non-trivial content lies at depth 3. Each torus knot has a non-zero Chern–Simons invariant:

$$
  \mathrm{CS}(T(p, q))
  \;=\;
  -\frac{(p^2 - 1)(q^2 - 1)}{24 p q} \cdot \pi^2
  \pmod{\pi^2 \mathbb{Z}}
$$

Freed–Gompf (1991) and Kirk–Klassen (1990) compute this explicitly. These are rational multiples of $\pi^2$. They are degenerate depth-3 classes, lying entirely in $\mathcal{P}_2$ when reduced modulo the Tate twist.

### Statement

For each torus-knot row $K = T(p, q)$ in B1:

1. **Depth-2 inclusion.** $\mathrm{Vol}(K) = 0 \in \mathcal{P}_2 / \mathcal{P}_1$. This holds by definition in the period filtration.
2. **Depth-3 inclusion.** $\mathrm{CS}(T(p, q)) \in \pi^2 \cdot \mathbb{Q} \subset \mathcal{P}_2$. This is degenerate and yields no genuine $\mathrm{Li}_3$ contribution.
3. **Volume Conjecture for torus knots.** Garoufalidis–Lê (2005) established this. The asymptotic of $J_{T(p,q)}^{(N)}$ at roots of unity equals exactly the CS-rational expression. This is a published theorem.

These three conditions prove B1 at every torus-knot row. The result is degenerate. No genuine trilog content arises.

### Reduced informativeness of torus-knot rows relative to figure-8

The figure-8 row of B1 ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)) realises a non-trivial depth-2 period $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$. Torus-knot rows realise zero at depth 2, or a Tate-twisted rational at depth 3 inside $\mathcal{P}_2$.

- The figure-8 row is a theorem and non-trivial.
- Torus-knot rows are theorems and degenerate (rational $\pi^2$ values).

For B1's predictive content, the figure-8 row is the cleaner test. Torus-knot rows confirm the framework on degenerate cases.

### Per-knot CS values for the seven Bring generators

See [Table](#tbl:b1-torus-knot-rows-theorem-table-data).

Note $T(2, 5) \cong T(5, 2)$ via cyclic-renaming symmetry, so the last two are equivalent.

These rational $\pi^2$ multiples confirm that torus-knot CS values sit in $\pi^2 \mathbb{Q} \subset \mathcal{P}_2$, not in $\mathcal{P}_3 \setminus \mathcal{P}_2$. Torus knots do not produce genuine depth-3 periods.

### Significance

Two B1 row classes are theorems ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem) and this proposition):

- Figure-8 (depth-2 non-trivial).
- Seven torus-knot generators (depth-2 trivial, depth-3 rational).

Combined, this discharges 8 specific rows of B1. Remaining rows of the Bring-embeddable atlas (chiral hyperbolic knots like $5_2$, $6_2$, $6_3$) are open at depth 3. They are conditional on a Volume Conjecture asymptotic that remains unproved for non-torus/non-figure-8 knots.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Figure-8 row: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- Soft sharpness: [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
- Conway-KT (mutant pairs): [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
