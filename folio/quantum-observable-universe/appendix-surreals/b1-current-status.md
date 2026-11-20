**Remark (the depth correspondence: what is theorem-level and what is open).**

The current status of the depth correspondence ([GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence)) is collected here in one place.

**Summary:** the correspondence is theorem-level at depths 1, 2 over every Bring-natural number field and at the figure-8 / 7 torus-knot / Borromean / Whitehead rows; conditionally theorem-level at depth 3 over $\mathbb{Q}(\zeta_5)$ modulo a single specific real number; conjectural at depth $\ge$ 3 over arbitrary $F$ via Beilinson/Goncharov.

Its open content reduces to:

1. **Per-knot VC discharges** for chiral hyperbolic Bring-embeddable knots ($5_2$, $6_*$, $7_*$, $8_*$). This is active classical knot-theory research, not paper-internal.
2. **One specific real number** at depth 3 over $\mathbb{Q}(\zeta_5)$:
   $$
     \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right) \approx 0.95572314353826862\ldots
   $$
   This has no known closed form modulo $\zeta(3) + (2\pi i)^3 \mathbb{Q}$. It generates the antisymmetric component of the 2-dim regulator image.
3. **Goncharov motivic conjecture at $\mathbb{Q}(\zeta_5)$**. What a discharge would require is set out in [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5).
4. **Beilinson's conjecture at depth $\ge$ 4** (external).
5. **Geometric realisation of $\mathrm{Cl}_3(2\pi/5)$**. Three candidates are listed; SnapPy CS computation on Bring torus knots is the smallest concrete test.

See [Table 2](#tbl:b1-current-status-table2-data) for numerical witnesses (50-dps verified).

The graded-Mikusiński / Goncharov-period-correspondence framework is substantially established:
- **Structural conjectures** (joint action, bridge map at small $n$, bi-filtration well-definedness, Hecke-Baer-* at generic $q$) are all theorem-level.
- **Numerical witnesses** at depths 2 and 3 are verified to 50 dps.
- **The depth correspondence** is theorem-level on its principal rows (figure-8, torus knots, Borromean, Whitehead) and conditionally theorem-level on others modulo VC discharges.
- **The depth-3 unproved surface** has shrunk to a single specific real number plus standard external conjectures.

The remaining work is outsourced to established research areas (Volume Conjecture, Beilinson, motivic cohomology) rather than residing as paper-internal conjectural content.
