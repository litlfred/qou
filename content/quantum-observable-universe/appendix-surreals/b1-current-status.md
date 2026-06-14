**Remark (canonical B1 current-status synthesis — what is theorem,
what is open, after eleven rounds of sharpening).**

The keystone B1 ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence))
has been progressively sharpened across eleven rounds. *This block
collects the current status in one canonical place: which claims
are theorem, which are conjectural, which are reduced to a known
external open problem, and what specific concrete questions remain.*

### One-line summary

**B1 is theorem-level at depths 1, 2 over every Bring-natural number
field and at the figure-8 / 7 torus-knot / Borromean / Whitehead
rows; conditionally theorem-level at depth 3 over $\mathbb{Q}(\zeta_5)$
modulo a single specific real number; conjectural at depth $\ge$ 3
over arbitrary $F$ via Beilinson/Goncharov.**
### Concrete sharpest open content

After eleven rounds, B1's open content reduces to:

1. **Per-knot VC discharges** for chiral hyperbolic Bring-embeddable
   knots ($5_2$, $6_*$, $7_*$, $8_*$). Active classical knot-theory
   research; not paper-internal.

2. **One specific real number** at depth 3 over $\mathbb{Q}(\zeta_5)$:

   $$
     \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
     \;\approx\; 0.95572314353826862\ldots
   $$

   No known closed form modulo $\zeta(3) + (2\pi i)^3 \mathbb{Q}$.
   Generates the antisymmetric component of the 2-dim regulator image.

3. **Goncharov motivic conjecture at $\mathbb{Q}(\zeta_5)$** —
   discharge plan in [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5)
   (Avenue A: Hecke-NF redundancy enumeration; Avenue B: explicit
   22-term Hecke element).

4. **Beilinson's conjecture at depth $\ge$ 4** — external.

5. **Geometric realisation of $\mathrm{Cl}_3(2\pi/5)$** — three
   candidates listed; SnapPy CS computation on Bring torus knots is
   the smallest concrete test.

### Numerical witnesses (50-dps verified)

See [Table 2](#tbl:b1-current-status-table2-data).

### What rounds 1–11 added

See [Table 3](#tbl:b1-current-status-table3-data).

### Where the framework stands

The graded-Mikusiński / Goncharov-period-correspondence framework
is now **substantially established**:

- **Structural conjectures** (joint action, bridge map at small $n$,
  bi-filtration well-definedness, Hecke-Baer-* at generic $q$):
  all theorem-level.
- **Numerical witnesses** at depths 2 and 3 verified to 50 dps.
- **B1 keystone** is theorem-level on its principal rows
  (figure-8, torus knots, Borromean, Whitehead) and conditionally
  theorem-level on others modulo VC discharges.
- **The depth-3 unproved surface** has shrunk to a single specific
  real number plus standard external conjectures (Goncharov,
  Beilinson).

The remaining work is best characterised as **outsourced** to
established research areas (Volume Conjecture, Beilinson, motivic
cohomology) rather than paper-internal conjectural content.
