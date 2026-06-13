**Remark (Bring-embeddable knot table).**

The QOU substrate selects the knots whose Seifert genus is bounded
by Bring's surface genus
([`prop:knot-eigenbasis-complete`](#prop:knot-eigenbasis-complete),
[`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness)):

$$
  \mathrm{Knots}_{\mathrm{Bring}}
  \;:=\;
  \bigl\{ K \,:\, g(K) \;\leq\; 4 \bigr\}.
$$

By the [generation completeness theorem](#prop:knot-eigenbasis-complete),
this class is generated from a finite list of **torus-knot
generators** plus skein crossing changes. The principled atlas in
the paper's recursive atom-knot atlas (`../appendix-knot-periodic-table/recursive-atom-knot-atlas.md`) lists
the canonical low-genus representatives used in the paper.

### Genus stratification (depth-2 witnesses)

The full table of Bring-embeddable knots by genus is in
[Table: Bring-embeddable knot table](#tbl:bring-embeddable-knots-table-data).

(Cells beyond $g = 1$ truncated for brevity; full enumeration in the
atlas.)

### Torus-knot generators

Every Bring-embeddable knot is obtained from the seven torus-knot
generators

$$
  \{T(2, 3),\; T(2, 5),\; T(2, 7),\; T(2, 9),\; T(3, 4),\; T(3, 5),\; T(5, 2)\}
$$

by skein crossing changes. (Genera: $g(T(p, q)) = (p-1)(q-1)/2$.
The seven listed have $g \in \{1, 2, 3, 4, 3, 4, 2\} \subseteq [1, 4]$.)
Skein moves preserve $g \leq 4$ when chosen in the principled
atlas methodology.

### Per-knot witness target under B1

For each Bring-embeddable knot $K$ with dominant cell $\lambda_K$
in $H_n(q)$ and shape parameter $z_K \in \overline{\mathbb{Q}}^\times$:

$$
  [\mathrm{Vol}(K)] \;=\; \tau_{\mathrm{arch}}\bigl( e_{\lambda_K}
  \cdot \mathrm{Li}_2^q(z_K) \bigr) \;\in\; \mathcal{P}_2 / \mathcal{P}_1.
$$

The depth-2 witness is computed for $4_1$ in
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).
Computing the analogous witness for **every Bring-embeddable
hyperbolic knot** is a finite-but-laborious task: each requires
identifying $\lambda_K$ (cell decomposition of the braid word)
and $z_K$ (shape parameter from triangulation). The recursive atom
atlas already records the volumes; the new content is the
*projection* $e_{\lambda_K}$ — the explicit Goncharov-period
witness per [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent).

### Falsifiability of B1 across the table

If [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
holds, **every entry in the principled atlas** must satisfy

$$
  \mathrm{Vol}(K) \;\stackrel{!}{=}\; \tau_{\mathrm{arch}}\bigl(
  e_{\lambda_K} \cdot \mathrm{Li}_2^q(z_K) \bigr).
$$

A single counter-example among the principled-atlas entries would
falsify B1. The figure-8 row is verified
([`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)).
Verifying $5_2$, $6_2$, $6_3$ would multiply the falsifiability
surface significantly with modest implementation cost.
