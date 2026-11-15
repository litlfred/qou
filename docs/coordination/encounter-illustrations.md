# Coordination — Encounter chapter illustrations

**Goal**  Coordinate between
[`claude/improve-paper-exposition-4a0OT`](https://github.com/litlfred/qou/tree/claude/improve-paper-exposition-4a0OT)
(this branch — adds the new "Encounter" chapter and splits
`prop:confinement-sdp` into companion remarks) and
[`claude/add-paper-illustrations-Diggj`](https://github.com/litlfred/qou/tree/claude/add-paper-illustrations-Diggj)
(sibling — authors `docs/illustration-recommendations.md` and
the SVG pipeline producing per-chapter `rendered/<slug>.svg`
figures).

## Scope map

| Branch | Status | Classification |
|--------|--------|----------------|
| `claude/improve-paper-exposition-4a0OT` (this) | pushed (commit `d4d74824`); no PR yet | source of the new content |
| `claude/add-paper-illustrations-Diggj` | pushed (HEAD `2794c36f`); no PR yet | downstream consumer; needs slot list for new content |

**Overlap**  None — different concerns. No file conflicts.
**Dependency**  Their pipeline depends on this branch's new chapter
(figure slots are blocks they have not yet seen); this branch does
not depend on theirs.
**Cherry-pick**  Nothing to cherry-pick yet. The SVG pipeline
conventions are reused without modification.

## Coordination message (for the illustrations author)

Hi — this branch added a new "Encounter" chapter
([`folio/quantum-observable-universe/encounter/`](https://github.com/litlfred/qou/tree/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter))
slotted between Ch. *particle-interactions* and Ch. *observations*,
and split `prop:confinement-sdp` into a slim statement plus four
companion remarks. Below is a list of recommended SVGs in the same
format as
[`docs/illustration-recommendations.md`](https://github.com/litlfred/qou/blob/claude/add-paper-illustrations-Diggj/docs/illustration-recommendations.md).
All slugs are stable: filenames follow the existing
`rendered/<slug>.svg` convention and target `.md` blocks already on
the pushed branch.

No edits to your `docs/illustration-recommendations.md` are
proposed here — append these entries when convenient, or import
them as a new "Chapter 13 — The Encounter" section between F12 and
F13. Notation register applies as usual
($\varTheta$, `$\mathbf{C}$`, `$\mathcal{S}_p$`, `$\varrho$` etc.).

---

## Chapter 13 — The Encounter (new)

### F13E.1 (P0) — The encounter sequence: approach → crossing → merge

- **Where**:
  [`encounter/approach-to-exceptional-divisor.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/approach-to-exceptional-divisor.md),
  immediately after the three-moment list.
- **What**: A three-panel cartoon (left → right):
  *(a) Approach* — two vortex tubes $\varrho_1, \varrho_2$
  propagating on a flat strip representing $M$, separated by a
  visible gap.
  *(b) Crossing onto the fibre* — the strip pinches at a brane
  point $p$; a circle marked $\mathcal{S}_p$ opens above the
  pinch; the two tubes enter the circle.
  *(c) Merge* — inside the circle the two tubes appear as
  two parallel braid strands, with a labelled bracket
  $\pi_1(U \setminus K)$ around them.
  Arrows between panels labelled "Reeb flow", "discriminant
  zero", "amalgamation".
- **Why**: the verbal three-step list is the conceptual heart of
  the chapter; the picture replaces three paragraphs of prose.

### F13E.2 (P0) — Base $M$ versus fibre $\mathcal{S}_p$

- **Where**: same `.md` as F13E.1, just before or after the
  three-panel sequence.
- **What**: A cross-section. Left half: smooth surface labelled
  "$M$ — base manifold; metric well-defined" with a
  monotone-decreasing scale gauge. Right half: at a brane point,
  the metric gauge collapses to zero and a vertical fibre opens up
  labelled "$\mathcal{S}_p$ — exceptional divisor; morphisms are
  knot operators". A dashed boundary marks the threshold; under it,
  the legend "below Planck $\Leftrightarrow$ on the fibre".
- **Why**: removes the metric-distance misreading of
  "below Planck" and introduces the chapter's shift of register
  from $M$ to $\mathcal{S}_p$.

### F13E.3 (P0) — Thurston relaxation as a Newton flow seeded by $q$-Pochhammer poles

- **Where**:
  [`encounter/thurston-relaxation.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/thurston-relaxation.md),
  after the bullet list.
- **What**: A landscape diagram. Top edge: a horizontal row of
  filled dots labelled $x = q^{-k}$ for $k = 0, \dots, n-1$
  (the $q$-Pochhammer poles). Below them, dashed vertical lines
  drop into a curved $\operatorname{Re}(S)$ landscape (a
  Picard--Lefschetz potential surface) with labelled saddle/min
  points at shape parameters $z_k$. Steepest-descent arrows go
  from each pole to its corresponding $z_k$. A small inset on the
  right shows the resulting hyperbolic triangulation
  $\bigsqcup_k \Delta_{z_k}$.
- **Why**: the "SDP solver = Newton iteration on Thurston gluing
  equations" claim is otherwise abstract; this visualises the
  shared computation.

### F13E.4 (P0) — SDP/LP dictionary across the Archimedean wall

- **Where**:
  [`encounter/sdp-as-thimble-flow.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/sdp-as-thimble-flow.md),
  alongside the dictionary table.
- **What**: A two-column figure with a vertical bar between them
  labelled "$\tau_{\mathrm{arch}}$ — Archimedean realisation".
  *Left column (pre-$\tau$, $\mathbb{Z}[q^{\pm 1/2}]$)*: stacked
  boxes for "Primal feasible region", "Cost $T$",
  "Dual $u_\lambda$", "Active support $\mathcal{S}^\ast$".
  *Right column (post-$\tau$, $\mathbb{R}$)*: matching boxes
  "Admissible knot topologies", "$\operatorname{Re}(S)$",
  "Thimble depth", "Saturating thimbles". Horizontal arrows
  cross the bar pairing left ↔ right entries.
- **Why**: the table is the chapter's central dictionary; an
  aligned-box visual makes the cross-wall correspondence
  unmistakable.

### F13E.5 (P0) — Mostow rigidity locking the volume spectrum

- **Where**:
  [`encounter/mostow-confinement.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/mostow-confinement.md),
  immediately after the three-part proposition statement.
- **What**: A staircase. Horizontal axis labelled
  "$\mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$"; vertical axis
  unlabelled but with discrete tick marks. Each step is a
  rectangle marked with a knot type
  ($4_1$, $5_2$, $6_2$, $\mathcal{B}_3$, $7_4$, …) at the
  corresponding volume; gaps between steps shaded with a "Mostow
  gap" annotation. Above the staircase, a no-entry sign marking
  "no continuous deformation"; below, a thin horizontal bar
  labelled "no nearby structures $\Rightarrow$ confinement".
- **Why**: the discreteness-of-mass claim is the payoff of the
  chapter; readers need a single picture explaining why mass is
  quantised.

### F13E.6 (P1) — Algebraic ↔ geometric rigidity pairing

- **Where**:
  [`encounter/algebraic-geometric-rigidity-pairing.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/algebraic-geometric-rigidity-pairing.md),
  alongside the column-table.
- **What**: Two parallel rectangles, vertically stacked.
  Top: "**Algebraic side** — `SDPSlaterUniqueness`, primal $\Phi^\ast$
  unique, $\mathbb{Z}[q^{\pm 1/2}]$".
  Bottom: "**Geometric side** — `MostowRigidity`, hyperbolic
  structure unique, $\mathbb{R}$".
  Two horizontal arrows between them: labelled
  "$\tau_{\mathrm{arch}}$" (top→bottom) and
  "GB ↔ PL thimble bijection" (a curved arrow returning bottom→top
  with a hollow head, marking the Conjecture status). A small
  marker "§3b conditional-class" on each rectangle.
- **Why**: visualises that the manuscript carries two
  independently axiomatised rigidity classes, one on each side of
  the wall.

### F13E.7 (P1) — The Archimedean wall

- **Where**:
  [`encounter/pre-tau-vs-post-tau.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/pre-tau-vs-post-tau.md),
  before the wall-discipline table.
- **What**: A vertical wall down the middle of the figure
  labelled "**Archimedean wall**". Left side: stacked tags
  "Hecke spectra", "Markov traces", "LP/SDP feasibility",
  "Gröbner--Shirshov reductions"; tinted background labelled
  "$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$".
  Right side: stacked tags "hyperbolic volumes", "thimble
  depths", "mass eigenvalues", "Bloch--Wigner $D(z)$"; tinted
  background labelled "$\mathbb{R}$ via $\tau_{\mathrm{arch}}$".
  A single arrow $\tau_{\mathrm{arch}}$ pierces the wall
  (one-way, not a double arrow). Two red "no-entry" signs on the
  wall mark illegal back-crossings.
- **Why**: makes the discipline graphical; useful for a reviewer
  who has only the verbal rule and would benefit from the visual
  one-way arrow.

### F13E.8 (P2) — Literature precedent map

- **Where**:
  [`encounter/encounter-literature-bridge.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/encounter/encounter-literature-bridge.md).
- **What**: A radial diagram. Centre: "QOU encounter picture".
  Five outer satellites, each labelled with citation key:
  "Mostow 1968" (rigidity arrow),
  "Thurston 1978" (gluing equations arrow),
  "Neumann--Zagier 1985" (potential arrow),
  "Witten 2011" (rigid phase arrow),
  "Yekutieli 2015" (non-abelian Stokes arrow),
  "Kashaev 1997" (volume conjecture arrow).
  Each arrow points inward; a small caption next to each names
  the ingredient supplied (e.g. "rigidity of volume", "Newton
  potential", "rigid phase concentration").
- **Why**: shows at a glance that every ingredient has a
  literature home; useful in talks where reviewers might
  otherwise suspect bespoke constructions.

---

## Chapter 12 (existing) — SDP companion-remark figures

The split of `prop:confinement-sdp` introduced four interpretive
remarks. Two are likely candidates for figures.

### F12.4 (P1) — Hecke spectral gap and deconfinement

- **Where**:
  [`particle-interactions/confinement-sdp-spectral-gap.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/particle-interactions/confinement-sdp-spectral-gap.md).
- **What**: A complex-$q$ plane with the unit circle drawn.
  Mark the points $q = \pm i$ (Kauffman degeneracy) with
  thick red dots; shade a wedge labelled "feasible cone" away
  from those points. As $q$ moves toward $\pm i$, draw the wedge
  collapsing (animation hint: arrowed sequence of three
  miniatures). Annotate "$\Delta_\sigma(q) = |q + q^{-1}|$" on
  the figure.
- **Why**: deconfinement = spectral-gap closure is otherwise
  abstract; the picture shows the geometric collapse of the
  feasible cone.

### F12.5 (P1) — Active dual support as binding multiplicity

- **Where**:
  [`particle-interactions/confinement-sdp-multi-operator.md`](https://github.com/litlfred/qou/blob/claude/improve-paper-exposition-4a0OT/folio/quantum-observable-universe/particle-interactions/confinement-sdp-multi-operator.md).
- **What**: A bar chart. Horizontal axis: Wedderburn blocks
  $\lambda_1, \lambda_2, \dots$. Vertical axis: shadow-price
  $u_\lambda^\ast$. Bars at active blocks coloured solid; bars at
  inactive blocks ($u_\lambda^\ast = 0$) drawn as outlined boxes.
  A bracket along the top labelled "$\mathcal{S}^\ast$ — binding
  multiplicity = number of active bars". Two miniature panels
  on the side showing $|\mathcal{S}^\ast| = 1$ (LP regime) and
  $|\mathcal{S}^\ast| \ge 2$ (multi-operator regime).
- **Why**: visualises the active-support reading of the dual,
  which is what shell-closure / magic-number configurations
  actually look like.

---

## Totals

10 new figures recommended (5 P0, 4 P1, 1 P2). Adding to the
existing 47 in `docs/illustration-recommendations.md`, the full
slate would be 57 figures (21 P0, 26 P1, 10 P2).

## Next-action checklist (for the illustration pipeline)

- [ ] Author SVGs for F13E.1 — F13E.5 (P0) first; these unblock
  the most abstract sections of the new chapter.
- [ ] Add a "Chapter 13 — The Encounter" section to
  `docs/illustration-recommendations.md` mirroring the entries
  above (cite this ledger as the source).
- [ ] Drop the per-chapter `rendered/` directory at
  `folio/quantum-observable-universe/encounter/rendered/` and
  embed each SVG via `![](rendered/<slug>.svg)` at the indicated
  block.
- [ ] Author F12.4 and F12.5 once Chapter 12 figures are otherwise
  in flight.

## Cross-PR housekeeping

* This branch has no open PR yet; the illustrations branch has no
  open PR yet. Once either opens, copy this ledger excerpt into
  the PR body (or link to this file) so the GitHub thread carries
  the coordination context.
* If a third sibling subsequently introduces another new chapter
  or remark cluster, append a section here rather than starting a
  new ledger.
