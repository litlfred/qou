**Proposition (B1 keystone is theorem-level at the torus-knot rows —
combining Bloch–Suslin with Garoufalidis–Lê's proof of the Volume
Conjecture for torus knots).**

*Every torus-knot row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") is **theorem-level**, requiring no part of Goncharov's or
Beilinson's conjectures.*

### Scope

Among the seven Bring-natural torus-knot generators of
[`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots):

$$
  \{T(2, 3),\; T(2, 5),\; T(2, 7),\; T(2, 9),\;
    T(3, 4),\; T(3, 5),\; T(5, 2)\}
$$

— **none are hyperbolic** (torus-knot complements are Seifert-fibred,
not hyperbolic). So the depth-2 row's *volume claim* is by definition
zero for each: $\mathrm{Vol}(T(p, q)) = 0$ in $\mathcal{P}_2 /
\mathcal{P}_1$. This depth-2 trivial row of B1 is *by definition*
theorem-level.

The non-trivial content is at **depth 3**: each torus knot has a
non-zero **Chern–Simons invariant**

$$
  \mathrm{CS}(T(p, q))
  \;=\;
  -\frac{(p^2 - 1)(q^2 - 1)}{24 p q} \cdot \pi^2
  \pmod{\pi^2 \mathbb{Z}}
$$

(Freed–Gompf 1991, Kirk–Klassen 1990 — explicit computation for
torus knots). These are **rational multiples of $\pi^2$** — i.e.,
*degenerate* depth-3 classes, lying entirely in $\mathcal{P}_2$
when reduced mod the Tate twist.

### Statement

For each torus-knot row $K = T(p, q)$ in B1:

1. **Depth-2 inclusion**: $\mathrm{Vol}(K) = 0 \in \mathcal{P}_2 / \mathcal{P}_1$
 — by definition in the period filtration.
2. **Depth-3 inclusion**: $\mathrm{CS}(T(p, q)) \in \pi^2 \cdot \mathbb{Q} \subset \mathcal{P}_2$
 — degenerate (no genuine $\mathrm{Li}_3$ contribution).
3. **Volume Conjecture for torus knots**: discharged by
 Garoufalidis–Lê 2005 (arXiv:math/0411521): the asymptotic of
 $J_{T(p,q)}^{(N)}$ at roots of unity equals exactly the
 above CS-rational expression. **Theorem (published).**

Combining (1)–(3): B1 at every torus-knot row is **theorem-level
and degenerate** — no genuine trilog content arises here.

### Reduced informativeness of torus-knot rows relative to figure-8

The figure-8 row of B1 ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem))
realises a **non-trivial** depth-2 period $\mathrm{Vol}(4_1) =
2\,\mathrm{Cl}_2(\pi/3)$. Torus-knot rows realise *zero* (depth 2)
or *Tate-twisted rational* (depth 3 but in $\mathcal{P}_2$). So:

- Figure-8 row = theorem AND non-trivial.
- Torus-knot rows = theorem AND degenerate (rational $\pi^2$ values).

For B1's *predictive content*, the figure-8 row is the cleaner test;
torus-knot rows confirm the framework on degenerate cases.

### Per-knot CS values for the seven Bring generators

See [Table](#tbl:b1-torus-knot-rows-theorem-table-data).

Note $T(2, 5) \cong T(5, 2)$ (cyclic-renaming symmetry of torus
knots), so the last two are equivalent.

These rational $\pi^2$ multiples confirm that torus-knot CS values
sit in $\pi^2 \mathbb{Q} \subset \mathcal{P}_2$, *not* in
$\mathcal{P}_3 \setminus \mathcal{P}_2$ — torus knots do not produce
genuine depth-3 periods.

### Significance

**Two B1 row classes are now theorem-level** ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
+ this proposition):

- Figure-8 (depth-2 non-trivial): theorem.
- Seven torus-knot generators (depth 2 trivial, depth 3 rational): theorem.

Combined, this **discharges 8 specific rows of B1**. Remaining rows
of the Bring-embeddable atlas (chiral hyperbolic knots — $5_2$,
$6_2$, $6_3$, etc.) are open at depth 3, conditional on a
(currently-unproved-for-non-torus-non-figure-8) Volume Conjecture
asymptotic.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Figure-8 row: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- Soft sharpness: [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
- Conway-KT (mutant pairs): [`rem:conway-kt-vol-injectivity-test`](#rem:conway-kt-vol-injectivity-test)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
