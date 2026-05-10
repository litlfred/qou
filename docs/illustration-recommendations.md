# Illustration recommendations — *On the Mechanics of Quantum Observable Universes*

Audit date: 2026-05-10 — branch
[`claude/add-paper-illustrations-Diggj`](https://github.com/litlfred/qou/tree/claude/add-paper-illustrations-Diggj).

The paper is mathematically dense but visually sparse. Apart from
auto-rendered `tikzcd` commutative diagrams in
[`quantum-universes/rendered/`](https://github.com/litlfred/qou/tree/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/quantum-universes/rendered),
no *illustrative* figures (knot diagrams, surfaces, flow lines,
braid pictures, schematic block flows) appear anywhere in the 1,659
`.md` content blocks across 22 chapters. This document recommends a
prioritised set of SVGs that should be authored, where each belongs,
and a precise description sufficient for an SVG draftsperson (or a
TikZ→SVG pipeline) to draw it.

## Conventions

- **Format**: SVG, embedded as `![Caption](rendered/<slug>.svg)` in
  the `.md` block, mirroring the existing
  `quantum-universes/rendered/` convention. Authoring source may be
  TikZ → SVG (preferred for diagrams), Inkscape, or hand-drawn SVG
  (preferred for knots & surfaces).
- **Style**: monochrome line-art primary; a single accent colour per
  figure when colour is meaningful (e.g. red/green/blue for the
  three coral tubes); thin (0.5 pt) lines, generous whitespace,
  serif Computer-Modern-style labels via `<text>` elements with
  MathJax-compatible `$...$` content where supported.
- **Notation**: figures must obey the notation register
  (`$\mathbf{C}$` not `$\mathcal{C}$`, `$\sigma_i$` not `$T_i$`,
  bold particles `$\mathfrak{p},\mathfrak{n}$`, `$\mathcal{S}_p$`
  not `$E_p$`, `$\varrho$` not `$\gamma$` for vortices, etc.). See
  `content/quantum-observable-universe/notation/`.
- **Placement**: each figure listed below names its target block
  `.md` file and the section it belongs to. The figure caption
  should be added immediately after the block's primary mathematical
  content (theorems get figures *after* the statement, before the
  proof; definitions get figures *immediately after* the formal
  statement).
- **File layout** (proposed): per-chapter `rendered/` directory
  alongside the chapter source, e.g.
  `content/quantum-observable-universe/braids-and-knots/rendered/electron-trefoil.svg`.

---

## Priority tiers

- **P0** — directly aids the central thesis; without these, key
  passages remain abstract and unread by most physicists.
- **P1** — strongly clarifies a constructive technical passage.
- **P2** — nice-to-have; helps but the prose can stand alone.

Total: **47 figures recommended** (16 P0, 22 P1, 9 P2).

---

## Chapter 0 — Introduction

### F0.1 (P0) — The roadmap-as-argument-flow

- **Where**:
  [`introduction/roadmap-diagram.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/introduction/roadmap-diagram.md).
  The block currently uses a `tikzcd` rendering that is a vertical
  chapter-list with arrows; replace or supplement with a true
  argument-flow diagram.
- **What**: A horizontal three-band diagram. *Top band — Inputs*:
  three boxes labelled "everyday observations" (colour mixing,
  rotation, time, volume, free will, computation), "the categorical
  language", and "three calibration scalars
  $(m_\mu/m_e,\,m_e,\,Q_\beta(n))$". *Middle band — Forced
  structure* (with arrows down from inputs): "QOU axioms",
  "$\mathrm{SU}_2(R)$ emerges", "$\chi=-6$ forced",
  "Bring's surface canonical". *Bottom band — Predictions*: a fan
  of arrows pointing at "particle masses", "Q-values",
  "$\alpha_{\mathrm{em}}$", "nuclear binding", "molecular barriers".
  Use a thin red dashed thread that runs through every band along
  the $\mathrm{SU}(2)$ running example; label "running example"
  near its first arrow.
- **Why**: a reader unfamiliar with category theory needs a
  one-page mental map of *what is assumed* vs *what is derived*
  before opening any chapter.

### F0.2 (P0) — The three-fold-observation triangle

- **Where**:
  [`introduction/intro.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/introduction/intro.md),
  immediately after the second paragraph ("Three-fold structure
  recurs throughout nature…").
- **What**: An equilateral triangle with vertices labelled
  "**Three colours** (R/G/B)", "**Three generations**
  ($\mathrm{e},\mu,\tau$ / $u,d / c,s / t,b$)", and
  "**Three-fold chirality**". At the centre, a small circled
  "$\chi(A)=-6$" with three radial lines connecting it to the
  vertices. Beneath the triangle, a single arrow pointing to a box
  labelled "**Bring's surface $\Sigma_4$**".
- **Why**: makes the central numerological coincidence visible
  before the reader meets any algebra.

---

## Chapter 1 — Quantum Universes

### F1.1 (P0) — The Frobenius pairing as a self-duality "snake"

- **Where**:
  [`quantum-universes/frobenius-pairing.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/quantum-universes/frobenius-pairing.md)
  (or wherever the pairing $A\otimes A\to\mathbf{1}$ is first
  introduced).
- **What**: The standard graphical-calculus snake/zig-zag
  ([cup, cap]) showing the rigidity composite
  $A\to A\otimes A^\vee\otimes A\to A$ collapsing to the identity;
  on the same panel, the *dual* snake for $A^\vee$. Use the
  Penrose / string-diagram convention: cups as $\cup$, caps as
  $\cap$, identity strands as vertical lines, with a small black
  dot for the unit/counit.
- **Why**: rigidity is invoked in nearly every chapter; readers
  outside category theory need the picture once.

### F1.2 (P1) — Tannaka–Krein reconstruction triangle

- **Where**: chapter consequences section, in the block introducing
  the fibre functor $\tau$.
- **What**: A triangle: top vertex labelled
  "$(\mathbf{C},A,\tau)$" (the QU); bottom-left "$\mathrm{Aut}^{\otimes}(\tau) = G$"
  (the reconstructed group); bottom-right "$\mathbf{Rep}(G)$";
  arrows: $\mathbf{C}\xrightarrow{\sim}\mathbf{Rep}(G)$ along the
  base, $\tau$ from $\mathbf{C}$ down to $\mathbf{Vect}$ at a fourth
  vertex centred below. Annotate the base arrow with
  "Tannaka–Krein".
- **Why**: anchors how $G=\mathrm{SU}_2(R)$ is *recovered* and not
  postulated.

### F1.3 (P2) — Differential calculus on a categorical object

- **Where**: jet / Kähler-differential definitions in §Structures.
- **What**: A schematic of the short exact sequence
  $0\to \Omega^1(A)\to A\otimes A \xrightarrow{m} A\to 0$ drawn as a
  ladder of three boxes with arrows; below, an inset showing
  $J^1(A)=A\otimes\Omega^1(A)$ as a "thickening" of $A$.

---

## Chapter 2 — Quantum Observable Universes

### F2.1 (P0) — From QU to QOU: the three constraints

- **Where**:
  [`quantum-observable-universes/quantum-observable-universe.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md).
- **What**: A funnel diagram. *Top opening*: a wide cloud labelled
  "all rigid braided monoidal categories with Frobenius–Hopf $A$
  and fibre $\tau$ (QUs)". Three sequential constrictions, each
  labelled with one axiom: "non-degenerate $\int_A$
  (volume)", "$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\mathrm{Ad}(A))=0$
  (observability)", "$c_1(\mathrm{Ad}(A))=c_2(\mathrm{Ad}(A))=0$
  (measurability)". *Bottom outlet*: a small box "QOU
  $(\mathbf{C},\varTheta,G,\mathcal{S})$ with $G=\mathrm{SU}_2(R)$
  forced". A side annotation: "and $\chi(A)=-6$ from the lifting
  obstruction (Ch 3)".
- **Why**: this is the single-most-cited transition in the paper.

### F2.2 (P1) — The categorical Dirac square decomposition

- **Where**: in the
  `categorical-dirac-operator.md` /
  `dq-squared-proof.md` neighbourhood.
- **What**: A 2×2 block-matrix glyph for $\mathcal{D}_\nabla^2$,
  with the diagonal blocks shaded and labelled "Ricci"
  ($\mathrm{Ric}$, spatial curvature) and "Yang–Mills" ($F_\nabla$,
  internal curvature); off-diagonal blocks shown as 0 with a small
  caption "no cross terms — forced by Frobenius–Hopf".
- **Why**: the paper repeatedly says "exactly two curvature terms
  appear"; a picture makes this falsifiable visually.

### F2.3 (P1) — The instanton self-duality projector

- **Where**:
  [`categorical-instanton.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/quantum-observable-universes/categorical-instanton.md).
- **What**: The 2-form bundle $\Omega^2(A)$ split into self-dual
  $\Omega^+$ and anti-self-dual $\Omega^-$ summands as two
  perpendicular axes; a vector $F_\nabla$ landing on the $\Omega^+$
  axis with a caption "$\star_q F_\nabla=F_\nabla$".

---

## Chapter 3 — Lifting and Descent

### F3.1 (P0) — The recursive brane tower

- **Where**:
  [`lifting-and-descent/recursive-brane-tower.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.md).
- **What**: A vertical stack of disks of increasing radius, labelled
  bottom-to-top $A_0,A_1,A_2,\dots$, each connected to the next by
  a fibre-bundle arrow $\hookrightarrow$ marked "$J^1$". On the
  side, annotate $A_n$ as "the brane of $A_{n+1}$" with a faint
  thickening showing $\Omega^1(A_n)$ as an extra dimension. At the
  base, label "$A_0=A$ — the original QOU".
- **Why**: the brane tower controls mass decomposition, descent,
  and the Yekutieli obstruction class — referenced in Chs 3, 4, 8,
  9.

### F3.2 (P1) — Yekutieli obstruction at level $n$

- **Where**: `yekutieli-obstruction.md` neighbourhood.
- **What**: A sequence of staircase steps; at each step a small
  red star labelled $\kappa_n$ marks the obstruction class; below
  each step a vertical bar labelled "Kummer filtration $K^\bullet$"
  controlling lift-ability. Annotate the step where
  $\kappa_n$ first vanishes and the tower stabilises.

### F3.3 (P2) — Cosimplicial descent diagram

- **Where**: descent block.
- **What**: The standard cosimplicial $\Delta^\bullet$ schematic
  (face/degeneracy maps as horizontal arrows between $A^{\otimes n}$
  for $n=1,2,3$).

---

## Chapter 4 — Braids and Knots (highest density of needed figures)

### F4.1 (P0) — The particle ↔ knot dictionary

- **Where**:
  [`braids-and-knots/intro.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/intro.md),
  immediately after the "specific knot types map to particle
  identities" paragraph.
- **What**: A 2-row × 5-column grid of pen-and-ink knot drawings
  with labels:
  - Row 1 (charged leptons): unknot $0_1$ → $\nu_e$ (neutrino,
    massless); trefoil $3_1$ → $e^-$; $T_{2,5}$ (cinquefoil) →
    $\mu^-$; $T_{2,7}$ → $\tau^-$; the "..." closure.
  - Row 2 (quarks): a Borromean ring of three interlocked
    unknots labelled $u,d,c,s,t,b$ in two coloured triples on the
    exceptional divisor. Adjacent: a closed 3-braid labelled
    "proton $\mathfrak{p}=\mathit{closure}(\sigma_1\sigma_2^{-1}\sigma_1)$";
    a closed 3-braid for the neutron.
- **Why**: this is the conceptual centrepiece of the paper. Without
  a picture, the leap from "Hecke algebra" to "particle table" is
  inaccessible.

### F4.2 (P0) — The $R$-matrix crossing and Hecke quotient

- **Where**:
  [`braids-and-knots/braid-action-tensor.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/braid-action-tensor.md).
- **What**: Three panels:
  1. A positive crossing $L_+$ (over-strand on the right) labelled
     "$\sigma_i$".
  2. A negative crossing $L_-$ labelled "$\sigma_i^{-1}$".
  3. A smoothed pair $L_0$ (two horizontal arcs) labelled "$1$".
  Below, the Skein relation
  $\sigma_i - \sigma_i^{-1} = (q-q^{-1})\cdot 1$ written
  pictorially: $L_+ - L_- = (q-q^{-1})L_0$. To the right, the
  Yang–Baxter triangle (three crossings on three strands, two
  ways) with an "$=$" between them.
- **Why**: every Hecke / Skein passage in the paper presupposes
  the reader has this picture in mind.

### F4.3 (P0) — Markov closure: braid → link

- **Where**: `braids-and-knots/hadron-interpretation.md` or
  `markov-moves-brane-tower.md`.
- **What**: A 3-strand braid drawn in a vertical "box"; arcs
  connecting top-$i$ to bottom-$i$ on either side of the box turn
  it into a closed link. Beside it, the two Markov moves: (M1)
  conjugation $\beta\sim\alpha\beta\alpha^{-1}$ shown as an
  isotopy of the closure; (M2) stabilisation
  $\beta\sim\beta\sigma_n^{\pm 1}$ shown as adding an extra
  strand.
- **Why**: the Markov trace is the workhorse of the mass formula.

### F4.4 (P1) — Möbius energy as Frobenius kernel

- **Where**:
  [`mobius-energy-frobenius-kernel-proof.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/mobius-energy-frobenius-kernel-proof.md).
- **What**: A smooth knot drawn in 3-space with two highlighted
  points $x,y$ and a dashed line of length $|x-y|$; an inset
  showing the integrand $1/|x-y|^2 \mathrm{d}s\,\mathrm{d}t$ on
  $K\times K\setminus\Delta$. Annotate "minimised on round
  configurations".

### F4.5 (P0) — Borromean quark configuration on the exceptional divisor

- **Where**: `confined-particle.md` or the quark-flavour
  introduction block.
- **What**: Three unknotted circles in the classic Borromean
  configuration (no two are linked; remove any one and the other
  two fall apart) drawn over a small genus-4 surface patch
  representing the exceptional divisor. Colour the three circles
  red/green/blue. Beneath: "any two unlinked, all three rigidly
  bound — the categorical origin of confinement".
- **Why**: instantly conveys why colour confinement is *topological*,
  not dynamical.

### F4.6 (P1) — Schur–Weyl boson/fermion split

- **Where**:
  [`categorical-boson-fermion.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/categorical-boson-fermion.md).
- **What**: $V^{\otimes 3}$ shown as a square split into one
  shaded triangle (the symmetric $V_{3/2}$ subspace, "boson") and
  a quadrilateral (the mixed-symmetry $V_{1/2}^{\oplus 2}$,
  "fermion"); $B_3$ generators labelled as "scalars on boson side"
  vs "non-trivial on fermion side".

### F4.7 (P1) — The brane-tower mass decomposition

- **Where**:
  [`atom-knot-mass-derivation.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md).
- **What**: An exploded view: input knot $K$ on the left; arrow
  splits it into three contributions stacked on the right —
  (top) Markov trace $|\mathrm{tr}_M(T_w)|$ as a "ground state"
  bar; (middle) brane-tower
  $\sum_i\Phi_q(|\hat V_i|)+z^2\sum_{i<j}\Phi_q(|\hat V_i\hat V_j|)$
  as a stack of stratified bars; (bottom) Frobenius co-Casimir
  $\sum_\lambda 1/\dim_q(\lambda)$ as a small correction.
- **Why**: the multi-term mass formula is asserted as the
  canonical form; the picture clarifies which term carries which
  physics.

### F4.8 (P1) — Knot-complement representation $\to \mathrm{PSL}(2,\mathbb C)$

- **Where**:
  [`knot-complement-group.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/knot-complement-group.md).
- **What**: Trefoil knot drawn lightly; a meridian disk highlighted;
  arrow labelled "$\rho$" pointing to a Möbius transformation
  glyph (a small Riemann sphere with a fixed-point arc). Caption:
  "each meridian generator $\mapsto$ Möbius
  transformation".

### F4.9 (P2) — Crossing-energy stratification

- **Where**: `topological-mass-cat-transient-proof.md` or
  `crossing-graded-proof.md`.
- **What**: Step function vs crossing number; horizontal axis "#
  positive crossings minus # negative", vertical axis "binding
  energy". A staircase showing energy quanta at each integer.

---

## Chapter 5 — Models of QOUs

### F5.1 (P0) — Bring's surface as a coral with three tubes

- **Where**:
  [`descartes-universe/brings-surface.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/descartes-universe/brings-surface.md)
  (note: the Bring blocks live in the `descartes-universe/` dir
  even though Bring is introduced in §5).
- **What**: A schematic genus-4 surface drawn as a "coral"
  (sphere with 4 handles) with three of the handles coloured red,
  green, blue (the colour tubes); the fourth handle drawn black
  and labelled "time / Reeb direction"; below it a small symbol
  "$\chi=-6$, $\mathrm{Aut}=S_5$". This is the paper's icon.
- **Why**: Bring's surface is mentioned ~150 times; an iconic
  picture should appear once and be referred to.

### F5.2 (P1) — The Descartes condition as a polytope vertex

- **Where**: `descartes-condition.md` neighbourhood.
- **What**: A 2D "moduli polytope" with axes "$g$" and
  "Aut order"; Bring's $(g=4,|\mathrm{Aut}|=120)$ marked as a
  distinguished corner; the Hurwitz bound $84(g-1)$ drawn as a
  diagonal ceiling line; the QOU constraint $\chi=-6$ as a
  horizontal line; their intersection highlighted.

### F5.3 (P1) — Yang–Mills mass gap: spectral picture

- **Where**: `yang-mills-mass-gap.md`.
- **What**: A spectrum diagram on a horizontal energy axis: a
  single dot at 0 (the vacuum), a gap region shaded, then a
  continuum starting at $\Delta>0$. Annotate "$\Delta=$ first
  Hecke eigenvalue".

---

## Chapter 6 — The Descartes Universe

### F6.1 (P0) — The colour-tube coordinates on Bring

- **Where**:
  [`color-tube-coordinates.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/descartes-universe/color-tube-coordinates.md).
- **What**: The Bring coral from F5.1 with arrows labelling the
  shifted Lagrange resolvents $c_r=w_2-z$ (red tube),
  $c_g=w_3-z$ (green), $c_b=w_4-z$ (blue), and
  $\sigma=w_1-z$ (the time-like shift) emerging from each tube's
  axis. A small box at one corner labelled "spacetime ratio
  $z=x_0/x_1$".

### F6.2 (P1) — Reeb flow as time direction on the substrate

- **Where**:
  [`algebraic-substrate/categorical-reeb-derivation.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/algebraic-substrate/categorical-reeb-derivation.md)
  (cross-cite from descartes preamble).
- **What**: A torus or 2-handle drawn with a vector field of small
  arrows along the contact direction; arrows accumulate along a
  closed orbit drawn in red. Annotate "Reeb vector field
  $\mathfrak R$ — the categorical arrow of time".

### F6.3 (P0) — The exceptional divisor with three quark Borromeans

- **Where**: `descartes-universe/quark-*.md`.
- **What**: An expanded version of F4.5: the exceptional divisor
  drawn as a small $\mathbb P^1$ at the corner of Bring; the
  Borromean configuration of $u,d,c,s,t,b$ shown as two coloured
  triples (light = up-type, dark = down-type); arrows at the
  bottom of each unknot showing where the three coral tubes
  $c_r,c_g,c_b$ intersect them.

### F6.4 (P1) — The Bring permutohedron of $S_5$ on five points

- **Where**: in the magic-numbers / $S_5$ block.
- **What**: A truncated octahedron (permutohedron of order 5)
  drawn in projection; its 120 vertices are the $S_5$ orbits;
  highlight one orbit class corresponding to "magic numbers".

---

## Chapter 7 — Algebraic Substrate

### F7.1 (P0) — The Frobenius–Hopf substrate as a layered diagram

- **Where**:
  [`frobenius-hopf-substrate.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/algebraic-substrate/frobenius-hopf-substrate.md).
- **What**: A horizontal three-layer cake: bottom layer "Hopf
  algebra structure $(m,\Delta,\eta,\varepsilon,S)$"; middle layer
  "Frobenius pairing $\int_A$"; top layer "compatibility — Reeb
  derivation $\mathfrak R$". String-diagram glyphs (the standard
  Hopf trivalent vertex and antipode loop) drawn at the bottom
  layer; cup/cap pair at the middle; a single straight arrow at
  the top.

### F7.2 (P2) — Tannaka–Krein spectral trace

- **Where**: spectral trace block.
- **What**: A schematic showing the trace $\mathrm{tr}\colon
  \mathrm{End}(A)\to k$ as the closure of a string diagram (a loop
  with a single object label).

---

## Chapter 8 — Information-Theoretic Perspectives

### F8.1 (P1) — Regime table as a temperature/scale diagram

- **Where**:
  [`information-theory/regime-table.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/information-theory/regime-table.md).
- **What**: Horizontal log-scale axis from $10^{-35}$ m (Planck)
  to $10^{26}$ m (Hubble); annotated bands: "categorical
  substrate", "Hecke regime", "thermodynamic", "general relativity".
  Vertical lines at $\ell_P$, $\hbar c/Q_\beta$, atomic, nuclear,
  cosmological scales.

### F8.2 (P1) — Emergent gravity from information geometry

- **Where**: `emergent-gravity-info.md`.
- **What**: Two-panel: left, an information manifold with a
  Fisher metric ellipsoid; right, the same metric reinterpreted as
  spacetime curvature. Arrow between them labelled "categorical
  identification".

### F8.3 (P2) — Planck-time computation cell

- **Where**: `planck-time.md`.
- **What**: A spacetime diamond of side $\ell_P$ with a single
  bit "0/1" inscribed; many such diamonds tiling a strip
  representing one Planck-time of brane evolution.

---

## Chapter 10 — Fluid Dynamics of the Brane

### F10.1 (P0) — $q$-vortex spectrum on the brane

- **Where**:
  [`fluid-dynamics/geodesic-vortices.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/fluid-dynamics/geodesic-vortices.md).
- **What**: The Bring coral with closed flow lines drawn around
  each of the four handles; each flow line annotated with its
  $q$-quantised circulation $\Gamma_n=2\pi[n]_q$. A side scale
  showing the discrete vortex spectrum as a comb of vertical
  bars.
- **Why**: fluid intuition for a categorical
  hydrodynamics is otherwise inaccessible.

### F10.2 (P1) — Madelung phase + density decomposition

- **Where**:
  [`madelung-fluid.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/fluid-dynamics/madelung-fluid.md).
- **What**: A wave $\psi=\sqrt\rho\,e^{iS/\hbar}$ broken into two
  panels: left, density $\rho$ as a height map on the brane;
  right, phase $S$ as a coloured wheel; an arrow combining them
  back into "$\psi$".

### F10.3 (P1) — NS obstruction: $q$-NS regular vs $q=1$ blowup

- **Where**: `ns-obstruction.md`.
- **What**: Two side-by-side phase portraits: left labelled
  "$q>1$: bounded enstrophy"; right labelled "$q=1$: enstrophy
  blowup at $T^*$". Both have time on the horizontal axis,
  enstrophy on the vertical; the right one shoots to infinity
  at finite $T^*$.

### F10.4 (P2) — $q$-Kolmogorov scaling ladder

- **Where**: turbulence section.
- **What**: A log-log plot of energy spectrum $E(k)\sim k^{-5/3}$
  with annotated dissipation scale; a $q$-deformed bend in the
  curve at scale $k_q$.

---

## Chapter 9 — The Descartes Universe (continued; main is Ch 6)

### F9.1 (P0) — Bring's three power-sum equations as nested constraints

- **Where**:
  [`brings-surface-example.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/descartes-universe/brings-surface-example.md).
- **What**: Three concentric ellipses in $\mathbb P^4$ schematic;
  inner = $\sum x_i^3=0$, middle = $\sum x_i^2=0$, outer = $\sum
  x_i=0$. Their intersection is highlighted as a curve marked
  "$\Sigma_4$, $g=4$".

---

## Chapter 11 — Particle Interactions

### F11.1 (P0) — Gröbner–Shirshov reduction tree

- **Where**:
  [`nuclear-groebner-reduction.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/particle-interactions/nuclear-groebner-reduction.md).
- **What**: A tree rooted at an unreduced Hecke word
  $T_w \in H_n(q)$; each downward branch is one rewrite by a
  Gröbner–Shirshov rule; leaves are normal-form monomials. Mark
  the canonical leaf (lex-smallest). Use small Hecke-word
  decorations on each edge: "by Skein", "by braid", "by Markov".
- **Why**: the GS engine is invoked dozens of times; readers need
  to see one full reduction once.

### F11.2 (P0) — Operator-selection LP/SDP active set

- **Where**:
  [`knot-operator-lp-selection.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/knot-operator-lp-selection.md).
- **What**: A 2D feasibility polytope (intersection of half-planes
  $G\succeq 0$ and net constraint); the optimum vertex marked
  with a star; the *active* faces (binding constraints) drawn in
  bold; the dual variables $u_\lambda^\star$ shown as outward
  normals on the active faces. Caption: "active demand channels
  = Wedderburn blocks the bound state saturates (LP shadow
  prices)".
- **Why**: per CLAUDE.md, LP duals are first-class infrastructure;
  a picture makes the "shadow price = binding energy" identity
  concrete.

### F11.3 (P1) — Nuclear shell closure as Hecke eigenvalue gap

- **Where**:
  [`shell-closure-stability.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/braids-and-knots/shell-closure-stability.md).
- **What**: A spectrum bar chart with magic-number gaps at
  $Z=2,8,20,28,50,82,126$; $y$-axis "Hecke eigenvalue gap";
  shading highlights the magic-number rows.

### F11.4 (P1) — Beta-decay channel as Markov-move tower

- **Where**: beta-decay handoff blocks.
- **What**: A vertical chain: parent nucleus knot → emit
  $W^-$ box-braid → daughter knot + electron trefoil + neutrino
  unknot. Each arrow labelled with a Markov stabilisation
  $\sigma_n^{\pm 1}$.

---

## Chapter 12 — Physical Observations

### F12.1 (P0) — Substrate consistency window

- **Where**:
  [`substrate-consistency-window.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/observations/substrate-consistency-window.md).
- **What**: Three vertical bands on a horizontal $q$ axis (range
  ~$1.10\le q \le 1.12$); each band represents the constraint
  derived from one of three independent calibrations
  ($m_\mu/m_e$, $\alpha_{\mathrm{em}}$, $Q_\beta(n)$). Their
  intersection — a tiny vertical sliver — is highlighted and
  labelled "$q_0\approx 1.1097$". A caption: "single-parameter
  overdetermination — the central falsifiability claim".
- **Why**: the entire Ch 7 case rests on this picture.

### F12.2 (P1) — Three-calibration-discipline triangle

- **Where**: `three-calibration-discipline.md`.
- **What**: A triangle whose three vertices are the three
  inputs ($m_\mu/m_e$, $m_e$, $Q_\beta(n)$). Inside, list ~30
  prediction labels (proton mass, neutron mass, $\alpha_{\mathrm{em}}$,
  $\Lambda_{\mathrm{QCD}}$, …) as small dots. No vertex–vertex
  arrows; only vertex–dot arrows showing each input is used in
  every prediction. Caption: "three inputs, $N$ predictions".

### F12.3 (P1) — Predicted-vs-CODATA scatter (existing data, missing plot)

- **Where**: predicted-mass blocks.
- **What**: A log-log plot of "predicted mass" vs "CODATA mass"
  for ~50 particles/atoms/isotopes; identity line; residuals
  panel below showing $|p-c|/c$ at the $10^{-6}$ level.

---

## Chapter 13 — Molecular Construction

### F13.1 (P0) — H₂ as a shared trefoil bond

- **Where**:
  [`molecular-construction/h2-molecular-braid.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/molecular-construction/h2-molecular-braid.md)
  (file exists if `h2-*` blocks present; otherwise place in
  `molecular-braid.md`).
- **What**: Two atomic trefoils side-by-side; one strand of each
  bent across to share with the other, forming a single combined
  link; the shared region highlighted and labelled "covalent
  bond = shared sub-Hopf link"; below, the LP-dual binding
  energy as a small bar.

### F13.2 (P0) — The molecular braid progression H₂→CO→CO₂→CH₄→C₂H₆→C₆H₆

- **Where**:
  [`molecular-construction/molecular-braid.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/molecular-construction/molecular-braid.md).
- **What**: A 2×3 grid of molecular braids; each cell shows the
  closed braid of one molecule with shared trefoils marked. C₆H₆
  cell shows the threading-link $T(2,N)$ structure (see F14.2).
  Below each cell, predicted vs experimental binding in eV.
- **Why**: this progression is the chapter's spine; without a
  picture the reader cannot follow which strand is shared with
  which.

### F13.3 (P2) — Tetrahedral CH₄ symmetry

- **Where**: `ch4-tetrahedral-symmetry.md`.
- **What**: A regular tetrahedron with H atoms at vertices, C at
  the centre; each C–H edge replaced by a small shared-trefoil
  glyph; the $S_4$ symmetry orbits highlighted.

---

## Chapter 14 — Organic Chemistry from Hopf Chains

### F14.1 (P0) — Carbon's four open linking sites (half-filled shell)

- **Where**:
  [`carbon-valence.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/organic-chemistry/carbon-valence.md).
- **What**: A central node "C" with 8 equally-spaced linking
  sites around it; 4 sites occupied (drawn as filled black
  trefoils) labelled "$1s^2$ closed inner shell"; 4 sites open
  (drawn as empty circles) labelled "residual $R$, $|R|=4$ —
  bonding sites". A side note: "$|R|/2n^2=1/2$ — half-filled".
- **Why**: this picture shows *why carbon is uniquely versatile*
  in two seconds.

### F14.2 (P0) — The threading link $T(2,N)$ (benzene)

- **Where**:
  [`organic-chemistry/threading-link.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/organic-chemistry/threading-link.md).
- **What**: A six-fold ring (benzene C-C skeleton) with a single
  large link threading through all six small atomic rings; the
  threading link drawn as $T(2,6)$. Caption: "Alexander
  polynomial halves the crossing energy".

### F14.3 (P1) — Chain vs ring topology comparison

- **Where**:
  [`organic-chemistry/chain-ring-comparison.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/organic-chemistry/chain-ring-comparison.md).
- **What**: Two panels: left, a linear C₆ chain (six trefoils
  joined end-to-end with shared sub-links); right, a closed C₆
  ring (the chain bent around to identify ends). Arrows showing
  the closure energy barrier between them.

### F14.4 (P2) — Benzene aromaticity as bond equalisation

- **Where**: `benzene-bond-equalization.md`.
- **What**: The C₆ ring with alternating double/single bonds (left)
  and equalised "1.5" bonds (right); a $\mathbb Z/6$ rotation
  symmetry arrow between them.

---

## Appendices

### FA.1 (P1) — Knot periodic table

- **Where**:
  [`appendix-knot-periodic-table/`](https://github.com/litlfred/qou/tree/claude/add-paper-illustrations-Diggj/content/quantum-observable-universe/appendix-knot-periodic-table).
- **What**: A periodic-table-style grid of 50–80 knots, columns
  organised by braid index $n$, rows by crossing number;
  each cell contains a small knot diagram + Hecke-word label +
  associated particle / atom / molecule.
- **Why**: the appendix currently lists data; a single "look-up"
  picture is what readers will return to.

### FA.2 (P2) — Knot-operation manipulator

- **Where**: appendix-knot-operations.
- **What**: A 4-panel "before/after" sequence for each elementary
  operation: Reidemeister I, II, III; Markov M1, M2; band-sum;
  smoothing.

### FA.3 (P2) — Transfer-matrix block decomposition

- **Where**: appendix-transfer-matrices.
- **What**: A large block-diagonal matrix glyph; each block
  labelled with its Wedderburn partition $\lambda$ and dimension.

---

## Implementation notes

1. **Naming**: use the slug from the target `.md` file plus an
   index, e.g. `electron-trefoil-0.svg`,
   `bring-coral-3-tubes-0.svg`. Co-locate in a sibling
   `rendered/` directory per chapter.
2. **Insertion**: each `.md` block gains a markdown image tag
   ``![Caption text.](rendered/<slug>.svg)`` at the chosen
   position; the LaTeX renderer
   ([`content/pipeline/render-latex.ts`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/content/pipeline/render-latex.ts))
   already converts SVG references.
3. **TikZ source**: where a TikZ script can produce the figure
   (commutative diagrams, simple knot tangles, polytopes), keep
   the `.tex` source alongside the `.svg` so future edits are
   reproducible. For freehand artwork (the Bring coral, complex
   knot drawings), an Inkscape `.svg` is the source of truth.
4. **Notation register compliance**: every figure must be
   reviewed by the `local/rendering-auditor` skill (notation pass)
   before merging.
5. **Build order suggestion**: P0 figures first (16 figures),
   committed in three batches of ~5, each in a single PR. P1 and
   P2 batches follow once P0 is merged.

---

## Summary table

| # | Chapter | Tier | Slug | Block |
|---|---------|------|------|-------|
| F0.1 | Introduction | P0 | roadmap-flow | roadmap-diagram.md |
| F0.2 | Introduction | P0 | three-fold-triangle | intro.md |
| F1.1 | Quantum Universes | P0 | frobenius-snake | frobenius-pairing.md |
| F1.2 | Quantum Universes | P1 | tannaka-krein-triangle | tannaka-krein.md |
| F1.3 | Quantum Universes | P2 | jet-prolongation-ladder | jet-prolongation.md |
| F2.1 | QOU | P0 | qu-to-qou-funnel | quantum-observable-universe.md |
| F2.2 | QOU | P1 | dirac-square-blocks | dq-squared-proof.md |
| F2.3 | QOU | P1 | instanton-self-dual | categorical-instanton.md |
| F3.1 | Lifting & Descent | P0 | brane-tower-stack | recursive-brane-tower.md |
| F3.2 | Lifting & Descent | P1 | yekutieli-staircase | yekutieli-obstruction.md |
| F3.3 | Lifting & Descent | P2 | cosimplicial-descent | descent-block |
| F4.1 | Braids & Knots | P0 | particle-knot-dictionary | intro.md |
| F4.2 | Braids & Knots | P0 | r-matrix-skein | braid-action-tensor.md |
| F4.3 | Braids & Knots | P0 | markov-closure | hadron-interpretation.md |
| F4.4 | Braids & Knots | P1 | mobius-energy | mobius-energy-frobenius-kernel-proof.md |
| F4.5 | Braids & Knots | P0 | borromean-quarks | confined-particle.md |
| F4.6 | Braids & Knots | P1 | schur-weyl-bose-fermi | categorical-boson-fermion.md |
| F4.7 | Braids & Knots | P1 | mass-decomposition | atom-knot-mass-derivation.md |
| F4.8 | Braids & Knots | P1 | knot-complement-rho | knot-complement-group.md |
| F4.9 | Braids & Knots | P2 | crossing-energy-staircase | topological-mass-cat-transient-proof.md |
| F5.1 | Models | P0 | bring-coral-3-tubes | brings-surface.md |
| F5.2 | Models | P1 | descartes-polytope | descartes-condition.md |
| F5.3 | Models | P1 | ym-mass-gap | yang-mills-mass-gap.md |
| F6.1 | Descartes | P0 | color-tube-coords | color-tube-coordinates.md |
| F6.2 | Descartes | P1 | reeb-flow | categorical-reeb-derivation.md |
| F6.3 | Descartes | P0 | exceptional-divisor-borromeans | quark-borromean.md |
| F6.4 | Descartes | P1 | s5-permutohedron | magic-numbers-bring.md |
| F7.1 | Algebraic Substrate | P0 | frobenius-hopf-cake | frobenius-hopf-substrate.md |
| F7.2 | Algebraic Substrate | P2 | spectral-trace-loop | tannaka-trace.md |
| F8.1 | Information Theory | P1 | regime-scale | regime-table.md |
| F8.2 | Information Theory | P1 | emergent-gravity | emergent-gravity-info.md |
| F8.3 | Information Theory | P2 | planck-time-cell | planck-time.md |
| F10.1 | Fluid Dynamics | P0 | q-vortex-spectrum | geodesic-vortices.md |
| F10.2 | Fluid Dynamics | P1 | madelung-decomposition | madelung-fluid.md |
| F10.3 | Fluid Dynamics | P1 | ns-obstruction-blowup | ns-obstruction.md |
| F10.4 | Fluid Dynamics | P2 | q-kolmogorov | turbulence-block |
| F9.1 | Descartes (cont.) | P0 | bring-power-sums | brings-surface-example.md |
| F11.1 | Particle Interactions | P0 | gs-reduction-tree | nuclear-groebner-reduction.md |
| F11.2 | Particle Interactions | P0 | lp-active-set | knot-operator-lp-selection.md |
| F11.3 | Particle Interactions | P1 | shell-closure-spectrum | shell-closure-stability.md |
| F11.4 | Particle Interactions | P1 | beta-decay-tower | beta-decay-handoff.md |
| F12.1 | Observations | P0 | consistency-window | substrate-consistency-window.md |
| F12.2 | Observations | P1 | calibration-triangle | three-calibration-discipline.md |
| F12.3 | Observations | P1 | predicted-vs-codata | predicted-mass-block |
| F13.1 | Molecular | P0 | h2-shared-trefoil | h2-molecular-braid.md |
| F13.2 | Molecular | P0 | molecular-progression | molecular-braid.md |
| F13.3 | Molecular | P2 | ch4-tetrahedron | ch4-tetrahedral-symmetry.md |
| F14.1 | Organic | P0 | carbon-half-filled | carbon-valence.md |
| F14.2 | Organic | P0 | threading-link-benzene | threading-link.md |
| F14.3 | Organic | P1 | chain-vs-ring | chain-ring-comparison.md |
| F14.4 | Organic | P2 | benzene-aromaticity | benzene-bond-equalization.md |
| FA.1 | Appendix Periodic | P1 | knot-periodic-table | appendix-knot-periodic-table |
| FA.2 | Appendix Operations | P2 | knot-operations-grid | appendix-knot-operations |
| FA.3 | Appendix Transfer | P2 | transfer-block-diagonal | appendix-transfer-matrices |
