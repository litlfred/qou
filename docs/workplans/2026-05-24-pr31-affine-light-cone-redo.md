# Workplan — redo PR #31 (affine light cone + Reeb + Bring fibre illustrations)

**Status:** Open workplan, opened 2026-05-24
**Supersedes:** [PR #31](https://github.com/litlfred/qou/pull/31) (Copilot, 2026-03-13, draft, stale 13+ days)
**Owner:** litlfred
**Triggered by:** `/integration-watch all` salvage triage; user directive 2026-05-24

## Why PR #31 cannot be merged as-is

PR #31 was authored 2026-03-13 against a substantially different math + repo state. Four hard blockers prevent direct merge:

| Blocker | Detail |
|---------|--------|
| **B1. Target chapter is gone** | PR #31 modifies `chapters/descartes-universe.tex`. No `content/quantum-observable-universe/descartes-universe/` directory exists today; Ch 3 was reorganized. Reeb work lives in `quantum-observable-universes/` (Ch 4); Bring's surface work lives in `braids-and-knots/` + `archimedean-universe/` (Chs 6, 8). |
| **B2. Architecture mismatch** | Direct edits to `chapters/*.tex` get **overwritten on the next build** — per CLAUDE.md, `chapters/` is a *rendering target* generated from `content/.../*.md` blocks. Figures must be expressed as `diagram` content blocks (the schema defines `diagram` for figures/diagrams; there is no `figure` kind) — optionally paired with a `remark` block for interpretation. |
| **B3. Math framework drift** | PR #31 uses old notation: `(M, Θ, G, P, E)` 5-tuple (deprecated; current archimedean tuple is `(C, Θ, G, S)` per CLAUDE.md §7); `q_p → 0/1` "big bang / heat death" framing (current framework: derived substrate `q_0` from `q_parameter.py`, not `q_p`); ‖L ∧ F⁺‖ as visible annotation (gauge-field conventions have shifted). |
| **B4. Visual style misaligned** | PR #31's SVGs use artistic gradients (brown viscosity gradient, two-step "you are here → Milky Way spiral" pointer, decorative effects). Author directive 2026-05-24: **formal math-book style; no color/gradients unless carrying meaning; natural Bring coordinates only**. |

**Decision:** Close PR #31 with this workplan as the salvage path. The four figure SUBJECTS are valuable; the SVG files themselves are not cherry-pickable.

## Preserved intent (the 4 figure subjects)

PR #31's intent decomposes into 4 illustrations:

1. **Affine light cone on the brane** — wedge geometry from big-bang vertex through observer to heat-death cross-section
2. **Reeb dimension as physical thickness** — companion view showing the Reeb-fibre extent transverse to the brane
3. **Chiral elliptic fibre of Bring's surface at $q \to 0$** — sheet merging near a branch point of the chiral cubic $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$
4. **Chiral elliptic fibre of Bring's surface at $q = \tfrac{1}{2}$** — well-separated sheets along the real $z$-axis, T-duality structure visible

All four are useful pedagogy. None contradict the current math framework when re-expressed in natural coordinates.

## Mapping to current chapters

| Figure | Today's host chapter | Existing content block(s) to attach to |
|--------|----------------------|----------------------------------------|
| Affine light cone | **`quantum-observable-universes/`** (Ch 4) | candidates: a Reeb / brane anchor block already in `quantum-observable-universes/` (e.g. `categorical-reeb.md`, `categorical-reeb-brings.md`, or `reeb-contact-universal-computer.md`), or a new `affine-light-cone-figure.{ts,md}` `diagram` block following an existing remark on the brane geometry. Note: the live `reeb-bundle.md` lives under `braids-and-knots/`, not `quantum-observable-universes/` — choose the Ch 4 Reeb-anchor that best matches the figure's narrative role. |
| Reeb dimension thickness | **`quantum-observable-universes/`** (Ch 4) — alongside the affine light cone | same anchor as above; new `reeb-dimension-figure.{ts,md}` `diagram` block as companion |
| Bring chiral fibre at $q \to 0$ | **`braids-and-knots/`** (Ch 6) or **`archimedean-universe/`** (Ch 8) | candidates: `bring-z5-descent.md`, `bring-figure-eight-depth-2-witness.md`, `x5-bring-prym-jacobian.md`; new `diagram` block (optionally paired with a `remark` for interpretation) reads naturally near the cubic's discriminant locus |
| Bring chiral fibre at $q = \tfrac{1}{2}$ | same as above (paired with the $q \to 0$ figure) | same — paired `diagram` block |

Per CLAUDE.md §3a (remark authoring convention): the figure itself is a `diagram` block (the only figure-bearing kind in the schema). When an interpretive note is needed, pair it with a sibling `remark` block whose `interprets:` field points at the parent definition/proposition. The `remark` carries no new mathematical content, so it does not trip propagation rules even if it sits downstream of a conjecture.

## Per-figure recipe

### F1 — Affine light cone

- **Intent:** show the affine light-cone wedge on the brane surface, with the brane as a 2D surface in 3D ambient space, the wedge opening from a vertex at one end and broadening toward the other. Demonstrate the $\chi(A) = -6$ topology constraint (equivalently $\chi(\Sigma_4) = -6$ for Bring's surface).
- **Natural Bring coordinates:** use the spacetime affine chart $z = x_0/x_1 \in \mathbb{CP}^1$ from Bring's surface, restricted to a real curve $z \in [z_{\text{vertex}}, z_{\text{horizon}}]$. The brane is the locus of the chiral cubic in this chart. No "exponential profile" or invented surface.
- **Style:** formal math-book; black ink line drawing on white. Bring curve as a single thick line. Light cone as two thin straight lines bounding the wedge. $\chi(A) = -6$ label as a plain marginal note. NO gradient, NO color-decoration. Observer location: small filled dot, label "observer" (no "Milky Way" / "you are here" graphics).
- **Annotation:** $q_0$ at the substrate point, two endpoint labels with their actual $z$ values, $\chi(A) = -6$ in a corner box.
- **Compute:** Python + matplotlib. Parameterize by $z_{\text{vertex}}, z_{\text{horizon}}$. Cubic-solve via `numpy.roots`. Output: `figures/affine-light-cone.svg` + `.pdf` via cairosvg.

### F2 — Reeb dimension as physical thickness

- **Intent:** companion to F1 showing the Reeb-fibre extent $\xi_q$ transverse to the brane at multiple points along the brane curve.
- **Natural coordinates:** the Reeb 1-form direction is the kernel of the contact structure derived from $\mathcal{S} \to M$ in the current archimedean tuple `(C, Θ, G, S)`. The thickness $\xi_q$ at each point is the actual derived value, NOT an artistic "viscosity" gradient.
- **Style:** formal math-book; brane curve as in F1; transverse arrows of variable length showing $\xi_q$ at sample points. Length encodes the actual Reeb-fibre extent (a meaningful variable), NOT decorative color. NO "swirl indicators", NO "mud-like viscosity" graphics.
- **Annotation:** $\xi_q$ symbol with units, $\chi(A) = -6$ marker.
- **Compute:** same Python toolchain. Reeb extent computed from the actual derived structure (consult the Reeb-anchor block chosen in the chapter-mapping table above + sibling blocks for the formula).

### F3 — Bring chiral fibre at $q \to 0$

- **Intent:** two-panel figure. **Left panel:** $\mathbb{CP}^1$ base with the 6 branch points of the chiral cubic marked (where the discriminant vanishes). **Right panel:** the 3 sheets $X_1, X_2, X_3$ near the chosen branch point, showing the sheet-merging that produces $B_3$-monodromy.
- **Natural Bring coordinates:** $z = x_0/x_1 \in \mathbb{CP}^1$; sheets $X_k$ from solving $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$ (the actual chiral cubic from Bring's invariant ring — NOT fabricated coefficients). Branch points: actual roots of the discriminant.
- **Style:** formal math-book. Left panel: $\mathbb{CP}^1$ as a circle (one-point compactification); branch points as small filled black dots. Right panel: three sheet curves; the two merging sheets in matched line style (e.g. solid + dashed), the isolated sheet in a different line style (e.g. dotted). Color allowed ONLY if necessary to disambiguate the three sheets (red/blue/green is OK if monochrome line styles aren't legible) — but prefer line styles first.
- **Annotation:** branch point coordinates (actual complex values); sheet separations as labelled distances; monodromy arrow on merging sheets.
- **Compute:** Python + matplotlib + numpy.roots for sheet evaluation along a circle around the branch point.

### F4 — Bring chiral fibre at $q = \tfrac{1}{2}$

- **Intent:** parallel two-panel figure to F3 at intermediate $q$. **Left panel:** $\mathbb{CP}^1$ base with a highlighted real segment $z \in [-0.5, 1.5]$ well away from all branch points. **Right panel:** stacked Re$(X)$ and Im$(X)$ subplots showing the 3 sheets, $X_1$ real and decreasing, $X_2, X_3$ a complex-conjugate pair.
- **Natural Bring coordinates:** same cubic at $q = \tfrac{1}{2}$. Sheet evaluation along the real segment.
- **Style:** same as F3. Two subplots stacked; T-duality axes (if present in framework) marked as thin vertical lines at $z = 0, 1$ with actual derivation cite. Specific values at $z = 0$ ($X_1 = -1$, $X_{2,3} = \pm i$) shown as labelled points, **only if independently verified** in the current framework.
- **Compute:** same toolchain.

## Compute infrastructure to use

- **Python**: `computations/` is the conventional location for figure-generation scripts. New scripts go alongside (`bring_chiral_fibre_figure.py`, `affine_light_cone_figure.py`).
- **Parameter source**: `q_parameter.py` provides $q_0$, $h$, derived constants. Import from there; never hardcode.
- **Witness emission**: each figure-generator emits a `.witness.json` with the parameters used (q value, branch point coordinates, sheet values at sample points) for reproducibility. This makes the figures auditable by `compute-integration-watcher`.
- **CODATA / experimental constants**: for calibration inputs (e.g. $m_e$, $m_\mu/m_e$, $Q_\beta$), import from `experimental_constants.py` (the canonical module for upstream calibration inputs). `codata_constants.py` re-exports these and additionally provides `*_VALIDATION` names (e.g. `M_P_MEV_VALIDATION`) for **comparison only** — its module docstring explicitly warns against using its non-`*_VALIDATION` exports as upstream inputs to mass / binding predictions.

## File plan

| File | Purpose | New / modify |
|------|---------|--------------|
| `docs/workplans/2026-05-24-pr31-affine-light-cone-redo.md` | This workplan | **new** (committed in the workplan PR) |
| `computations/affine_light_cone_figure.py` | F1 generator | new (later commit) |
| `computations/reeb_dimension_figure.py` | F2 generator | new (later commit) |
| `computations/bring_chiral_fibre_figure.py` | F3 + F4 generator | new (later commit) |
| `computations/*.witness.json` | per-figure witnesses | new |
| `figures/affine-light-cone.{svg,pdf}` | F1 output | new |
| `figures/reeb-dimension.{svg,pdf}` | F2 output | new |
| `figures/bring-fibre-q0.{svg,pdf}` | F3 output | new |
| `figures/bring-fibre-qhalf.{svg,pdf}` | F4 output | new |
| `content/quantum-observable-universe/quantum-observable-universes/affine-light-cone-figure.{ts,md}` | F1 content block | new |
| `content/quantum-observable-universe/quantum-observable-universes/reeb-dimension-figure.{ts,md}` | F2 content block | new |
| `content/quantum-observable-universe/braids-and-knots/bring-fibre-q0-figure.{ts,md}` | F3 content block | new |
| `content/quantum-observable-universe/braids-and-knots/bring-fibre-qhalf-figure.{ts,md}` | F4 content block | new |
| `.gitignore` | add `!figures/*.{svg,pdf}` exception (if missing) | modify |

## Phased delivery (one PR per phase OR one batched PR; author decides)

1. **Phase 0 — this workplan** (current PR): doc only; closes PR #31 by reference.
2. **Phase 1 — F3 + F4 (Bring chiral fibres):** lowest-risk; pure algebraic; cubic is well-established; existing `braids-and-knots/bring-*` blocks anchor the content well.
3. **Phase 2 — F1 (affine light cone):** depends on settling natural-coordinate parameterization of the brane in `quantum-observable-universes/` chapter.
4. **Phase 3 — F2 (Reeb dimension):** depends on `reeb-bundle.md` + sibling blocks; companion to F1.

Phases 1-3 can be done by separate sessions / agents; the workplan + closure of PR #31 are the immediate deliverables.

## Closure plan for PR #31

After this workplan is committed and the salvage PR is opened:

1. Post a closing comment on PR #31 with the link to this workplan + the new PR.
2. Note the salvage scope: math intent preserved; SVG assets re-derivable in natural coordinates per the recipe above; chapter targets updated.
3. Close PR #31 (do NOT merge).
