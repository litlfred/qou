This remark synthesizes the current status of B1 ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) after eleven rounds of sharpening. We record which claims are theorems, which are conditional, and which reduce to external open problems.

### One-line summary

B1 is a theorem at depths 1 and 2 over every Bring-natural number field, and at the figure-8, 7 torus-knot, Borromean, and Whitehead rows. It is conditionally a theorem at depth 3 over $\mathbb{Q}(\zeta_5)$ modulo a single specific real number. It remains conjectural at depth $\ge$ 3 over arbitrary $F$ via the Beilinson and Goncharov conjectures.

### Concrete sharpest open content

After eleven rounds, the open content of B1 reduces to five points.

1. **Per-knot VC discharges** for chiral hyperbolic Bring-embeddable knots ($5_2$, $6_*$, $7_*$, $8_*$). This requires active classical knot-theory research and is not paper-internal.
2. **One specific real number** at depth 3 over $\mathbb{Q}(\zeta_5)$:

   $$
     \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
     \;\approx\; 0.95572314353826862\ldots
   $$

   This number has no known closed form modulo $\zeta(3) + (2\pi i)^3 \mathbb{Q}$. It generates the antisymmetric component of the 2-dimensional regulator image.
3. **Goncharov motivic conjecture at $\mathbb{Q}(\zeta_5)$**. The discharge plan appears in [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5).
4. **Beilinson's conjecture at depth $\ge$ 4**. This remains an external problem.
5. **Geometric realisation of $\mathrm{Cl}_3(2\pi/5)$**. We list three candidates. A SnapPy Chern–Simons computation on Bring torus knots is the smallest concrete test.

### Numerical witnesses

See [Table 2](#tbl:b1-current-status-table2-data). These witnesses are verified to 50 decimal places.

### Contributions of rounds 1–11

See [Table 3](#tbl:b1-current-status-table3-data).

### Status of the framework

We have established the graded-Mikusiński / Goncharov-period-correspondence framework.

- **Structural conjectures**. The joint action, bridge map at small $n$, bi-filtration well-definedness, and Hecke-Baer-* at generic $q$ are theorems.
- **Numerical witnesses**. Depths 2 and 3 are verified to 50 decimal places.
- **B1 keystone**. This is a theorem on its principal rows (figure-8, torus knots, Borromean, Whitehead). It is conditionally a theorem on others modulo VC discharges.
- **The depth-3 unproved surface**. This reduces to a single specific real number plus standard external conjectures.

The remaining work relies on external research areas (Volume Conjecture, Beilinson, motivic cohomology) rather than paper-internal conjectures.
