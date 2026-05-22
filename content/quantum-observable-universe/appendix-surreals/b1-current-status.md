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

### Status table

| Layer | Status | Discharger |
|---|---|---|
| **Inclusion** $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$, all $n$ | **theorem** | regulator definition |
| **Soft sharpness**, all $n$, Bring-natural $F$ | **theorem** | [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem) (Borel + Lewin) |
| **Strong sharpness, depth 2**, any $F$ | **theorem** | [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin) (Bloch–Suslin) |
| **B1 figure-8 row** | **theorem** | [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem) (+ Murakami–Murakami 2001) |
| **B1 7 torus-knot rows** | **theorem** | [`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem) (+ Garoufalidis–Lê 2005) |
| **B1 Borromean row** | **theorem** | [`prop:b1-hyperbolic-rows-theorem`](#prop:b1-hyperbolic-rows-theorem) (+ van der Veen 2008) |
| **B1 Whitehead row** | **theorem** | [`prop:b1-hyperbolic-rows-theorem`](#prop:b1-hyperbolic-rows-theorem) (+ Murakami 2002) |
| **Hecke-Baer-* at generic $q$** | **theorem** | [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic) (+ exact failure locus) |
| **Bridge map at $n \leq 4$** | **theorem** | [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases) |
| **Joint Galois $\times$ braid action, all cells** | **theorem** | [`prop:joint-galois-braid-discharged`](#prop:joint-galois-braid-discharged) (round 11) |
| **$\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^{3}/125$** | **theorem** | [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational) (round 10) |
| **$\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5) = -(12/25)\zeta(3)$** | **theorem** | [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity) (round 11) |
| **Jones-faithfulness $\le$ 10 crossings** | **theorem** | [`rem:jones-faithfulness-crossing-8`](#rem:jones-faithfulness-crossing-8) (HTW 1998) |
| **B1 chiral hyperbolic rows** ($5_2, 6_2, 6_3$, $\ldots$) | **conditional theorem** modulo per-knot VC | open knot-by-knot |
| **Cl_3(2π/5) − Cl_3(4π/5) closed form** | **open** — single real number $\approx$ 0.955 | reflection + multiplication formulas exhausted |
| **Strong sharpness, depth 3 over $\mathbb{Q}(\zeta_5)$** | **conditional** on Goncharov $\zeta_5$ sub-case | [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5) (Avenue A or B, ~1-2 weeks) |
| **Strong sharpness, depth $\ge$ 3 over arbitrary $F$** | **conjectural** | Beilinson + Goncharov (external) |
| **Strong sharpness, depth $\ge$ 4** | **conjectural** | Beilinson + Goncharov (external) |
| **Geometric realisation of Cl_3(2π/5)** | **open**, 3 candidates | [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization) |
| **Bridge map at $n \geq 5$ partitions** | **open** | extends the bar-class argument |
| **Lean substantive proofs** | **partial** (sorry pending Mathlib's IwahoriHecke API) | scaffolding in `qou:` namespace |

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

| Witness | Identity | Residual |
|---|---|---|
| [`gb-depth-period-bring-fig8.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/gb-depth-period-bring-fig8.witness.json) | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | < SnapPy precision |
| [`bring-trilog-zeta5-depth-3.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring-trilog-zeta5-depth-3.witness.json) | $\sum \mathrm{Li}_3(\zeta_5^k) = -\tfrac{24}{25}\zeta(3)$ | $5.5 \times 10^{-51}$ |
| [`kummer-reflection-zeta5.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/kummer-reflection-zeta5.witness.json) | $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^3/125$ | $1.3 \times 10^{-51}$ |
| [`cl3-zeta5-orbit-sum.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/cl3-zeta5-orbit-sum.witness.json) | $\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5) = -\tfrac{12}{25}\zeta(3)$ | $1.3 \times 10^{-51}$ |

### What rounds 1–11 added

| Round | Commit | Key contribution |
|---|---|---|
| 1 | `12202fb0` | B1 keystone defined; depth-2 fig-8 50-dps witness |
| 2 | `cdf8442b` | Baer-* foundation, explicit $e_\lambda$, chirality, depth-3 trilog witness |
| 3 | `fd7aa9ae` | Transcendental-accounting ledger; ζ_n notation |
| 4 | `a2fc0e16` | Bi-filtration B5/B6/B7, K-theory Rosetta, Conway-KT, Cl_3 candidates |
| 5 | `bd9d74f8` | Borel partial-discharge with explicit dimensions |
| 6 | `58c97abd` | Bloch–Suslin depth-2 identification (theorem) |
| 7 | `20cf64e4` | Goncharov ζ_5 discharge program (Avenues A, B) |
| 8 | `c5dd15d9` | Soft-sharpness theorem; B1 fig-8 + torus knots = theorem; bridge $n \leq 4$ verified; Jones-faithfulness $\le$ 10 |
| 9 | `115c7932` | B1 Borromean + Whitehead = theorem; joint-action fig-8 verified |
| 10 | `710039e7` | Substantive Lean for Hecke-Baer-*; $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^{3}/125$ closed form |
| 11 | (this) | Joint-action discharged in general; Cl_3 orbit-sum identity; B1 status synthesis |

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
