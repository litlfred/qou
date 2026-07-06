**Conjecture (B1 conditionally reduces to Volume Conjecture at Borromean rings, Whitehead link, and twist knots).**

Beyond the figure-8 row ([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)) and the seven torus-knot rows ([`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)), B1 ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) holds for additional Bring-embeddable hyperbolic-knot rows, conditional on Volume Conjecture discharges.

### Conditionally discharged rows

See [Table 1](#tbl:b1-hyperbolic-rows-theorem-table1-data).

(Twist knot $K_n$ has $n$ half-twists. $K_2 = 4_1$ is the figure-8. The genus of $K_n$ is 1 for all $n$, so all twist knots are Bring-embeddable.)

*(We record explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link in the `audit/b1-hyperbolic-rows-theorem-audit` block.)*

### Coverage via the Bloch–Suslin chain

For any hyperbolic Bring-embeddable knot or link $K$ with shape parameter in some number field $F = \mathbb{Q}(z_K)$:

- **Step 1 (Bloch–Suslin)** is unconditionally established for any $F$.
- **Step 2 (cell pairing computation)** uses explicit Markov traces and Lobachevsky geometry.
- **Step 3 (VC asymptotic)** is knot-specific. It requires a published proof.

Thus, B1 at a depth-2 row conditionally reduces to the VC discharge for that knot. The rate-limiting step is the VC discharge per knot, not the Bloch–Suslin chain.

### Bring-embeddable hyperbolic knots awaiting VC discharge

See [Table 2](#tbl:b1-hyperbolic-rows-theorem-table2-data).

Each of these becomes a conditionally established B1 row upon VC discharge.

### Significance

The literature conditionally supports three additional B1 rows (Borromean, Whitehead, and figure-8 in [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)). Combined with the seven torus-knot rows ([`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)), the literature supports eleven total B1 rows.

B1 at depth 2 reduces to per-knot VC discharge via the Bloch–Suslin chain and Borel-rank computation. Every published VC discharge for a Bring-embeddable hyperbolic knot yields a conditional B1 row.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Depth-2 ID: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Figure-8 row: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Torus-knot rows: [`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)
- Soft sharpness (any depth): [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
- Bring-embeddable atlas: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
