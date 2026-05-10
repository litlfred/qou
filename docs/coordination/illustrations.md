# Coordination — paper illustrations

**Goal**  Coordinate authoring of illustrative SVG figures across PRs that
either (a) ship illustrations directly, (b) propose new content blocks
that need accompanying figures, or (c) ship infrastructure that
illustrations depend on.

**Owner branch**  [`claude/add-paper-illustrations-Diggj`](https://github.com/litlfred/qou/tree/claude/add-paper-illustrations-Diggj)
([PR #632](https://github.com/litlfred/qou/pull/632)) — ships
[`docs/illustration-recommendations.md`](../../docs/illustration-recommendations.md)
(47-figure audit), the figure-rendering pipeline (`\includesvg`,
`\figprompt`, `\blockstub`), the first authored SVG (F4.2 Hecke skein
triple), and the `anthropics-skills` package for illustration tooling.

## Scope map (2026-05-10)

| PR | Branch | Status | Overlap | Dep | Cherry-pick | Verdict |
|----|--------|--------|---------|-----|-------------|---------|
| **#632** | `claude/add-paper-illustrations-Diggj` (this) | open, fresh | — | — | — | owner |
| **#633** | `claude/improve-paper-exposition-4a0OT` (Encounter chapter) | open, fresh | additive | their slots → my doc | their `encounter-illustrations.md` ledger | accept all 10 slots; append to `illustration-recommendations.md` post-#633-merge |
| **#31** | `copilot/add-svg-illustration-affine-light` (Affine light cone + Reeb SVGs) | open, draft, ~2 mo stale | conflicting on F5.1 / F6.2 / F9.1 | independent | possibly the 4 existing SVGs | status query posted; awaiting answer before authoring F5.1 / F6.2 |
| #362 | `claude/divisor-visualization-chart-GK3Zq` (3D simulator) | open, ~3 wk stale | low (HTML simulator vs SVG) | independent | none | skip — different artefact |
| #162 | `claude/review-agent-skills-framework-IZ1Gv` (skills framework design) | open, ~6 wk stale, design-only | low | independent | none | skip |
| #436, #411, #373, #369, #510 | various | open | none (Lean / witness / fractals) | independent | none | skip per user direction |

## Coordination posts

| Date | PR | Comment | Verdict |
|------|----|---------|---------|
| 2026-05-10 | [#633](https://github.com/litlfred/qou/pull/633#issuecomment-4414728267) | accept ledger; +3 conventions for sibling adoption (white BG, Unicode-not-LaTeX, prompt sidecar) | sent — awaiting Q1 / Q2 |
| 2026-05-10 | [#31](https://github.com/litlfred/qou/pull/31#issuecomment-4414728834) | status query; flag F5.1 / F6.2 / F9.1 overlap; +3 conventions | sent — awaiting Q1 / Q2 / Q3 |

## Cherry-pick targets

| Source | Target file (#632) | Status |
|--------|-------------------|--------|
| #633 — F13E.1 … F13E.8 + F12.4 / F12.5 slot list | `docs/illustration-recommendations.md` (new "Chapter 13 — The Encounter" section + insertions in Ch 11) | queued — pending #633 merge |
| #31 — `figures/affine-light-cone.svg`, `figures/reeb-viscosity.svg`, `figures/brings-q0.svg`, `figures/brings-qhalf.svg` | per-chapter `rendered/` directories (descartes-universe + lifting-and-descent) | queued — pending Q1 reply on #31 |

## Asks outstanding

| To | Ask | Posted | Answer |
|----|-----|--------|--------|
| #633 author | Q1: post-merge, append slots to `illustration-recommendations.md`, or keep as standalone slate? | 2026-05-10 | — |
| #633 author | Q2: F13E.4 anchor — `sdp-as-thimble-flow.md` table the canonical home? | 2026-05-10 | — |
| #31 author | Q1: PR active, abandoned, or to-be-rebased? | 2026-05-10 | — |
| #31 author | Q2: coordinate via this ledger or a separate issue? | 2026-05-10 | — |
| #31 author | Q3: drop the four `.pdf` companions now that `\includesvg` is wired? | 2026-05-10 | — |

## Conventions (single source of truth — `illustration-recommendations.md`)

For sibling branches authoring SVGs, the rules are:

1. **White background**: `<rect width="100%" height="100%" fill="#ffffff"/>` as the first child. Required for dark-mode legibility.
2. **Plain Unicode in `<text>`**: SVG text is rendered as a vector asset, not processed by MathJax/LaTeX. Use `σ`, `q⁻¹`, `Δ` directly. Math too complex for Unicode belongs in surrounding prose.
3. **Sibling `<stem>.prompt.md`**: the renderer reads it and emits `\figprompt{…}` margin note under the caption in the printed PDF. Optional but recommended for reproducibility.
4. **`\includesvg`**: the LaTeX pipeline emits `\includesvg[width=\textwidth]{…}` for `.svg` urls; CI installs `inkscape` for SVG → PDF conversion.
5. **`\blockstub`**: every block with a label gets its `def:`/`prop:`/`thm:` tag emitted into the right margin via `\blockstub{<label>}`.

## Next-action queue (#632)

1. Author next P0 figures from the **non-overlapping** subset: F0.1 roadmap flow, F4.1 particle↔knot dictionary, F12.1 substrate consistency window, F14.1 carbon half-filled shell. (F5.1 / F6.2 deferred pending #31 reply.)
2. Append F13E.* + F12.4 / F12.5 entries to `illustration-recommendations.md` once #633 merges or after Q1 reply.
3. Periodic §7 triage every ~5 of #632's commits.
