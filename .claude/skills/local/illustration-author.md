---
name: illustration-author
description: Author SVG illustrations for the paper from a textual prompt. Produces a primary light-mode SVG (white background, dark strokes), an optional hand-tuned dark-mode sibling, the prompt sidecar that surfaces in the printed PDF margin, and (on request) N design variants for the author to pick from. Wires into the figures index. Trial-stage skill; will be formalised after a few iterations.
roles: [collaborator, owner]
user_invocable: false
---

# /illustration-author — prompt-driven SVG figure authoring

## When to invoke

- The author asks for a figure listed in
  [`docs/illustration-recommendations.md`](../../../docs/illustration-recommendations.md).
- A new content block lands that warrants a figure (the author or a
  sibling skill nominates it).
- The author asks for a *redraw* / *alternative* of an existing
  figure ("show me three versions of F4.1").

## What it produces

For a figure with stable slug `<slug>` (taken from the recommendations
doc), the skill writes:

```
content/quantum-observable-universe/<chapter>/rendered/
  <slug>-0.svg                  ← primary light-mode SVG (committed)
  <slug>-0.dark.svg             ← optional dark-mode override (commit when
                                  filter-invert fails — see §3 below)
  <slug>-0.prompt.md            ← prompt sidecar (small italic margin
                                  note in the printed PDF; surfaced via
                                  the \figprompt{…} macro)
```

For multi-variant requests:

```
  <slug>-A.svg, <slug>-A.dark.svg, <slug>-A.prompt.md
  <slug>-B.svg, <slug>-B.dark.svg, <slug>-B.prompt.md
  …
```

The author chooses one and the skill wires it into the target block;
the other variants stay on disk under
`<chapter>/rendered/` until the author asks to delete them, so a later
session can revisit them.

## Authoring conventions (every SVG, every time)

These mirror
[`docs/illustration-recommendations.md` § Conventions](../../../docs/illustration-recommendations.md);
they are duplicated here so a trial run can stay self-contained.

### 1. Light-mode primary (always required)

- **viewBox**: pick a clean integer pair (`720 280`, `900 600`, etc.);
  set `font-family="Georgia, 'Times New Roman', Times, serif"` at the
  root.
- **First child**: a viewBox-filling white rectangle —
  `<rect x="0" y="0" width="<W>" height="<H>" fill="#ffffff"/>` —
  authoritatively defines the light-mode background.
- **Strokes / fills**: dark monochrome (`#1a1a1a`) for line-art;
  one accent colour at most (red `#c0392b`, green `#27ae60`, or blue
  `#2980b9`) when colour carries meaning (e.g. the three coral tubes
  on Bring's surface).
- **`<text>`**: plain Unicode only — `σ`, `q⁻¹`, `Δ`, `χ`, `μ`. Never
  `$\sigma$` / `$q^{-1}$` — SVG text is *not* run through MathJax or
  LaTeX. Math too complex for Unicode belongs in the surrounding
  prose.
- **Labels & sub/superscripts**: prefer absolute-x/y positioning over
  cumulative `dy` chains (the latter drifts across renderers); when
  unavoidable, use the SVG `baseline-shift` attribute.
- **Titles & descriptions**: every SVG has a `<title>` (one line) and
  `<desc>` (free-text describing what the figure depicts) inside the
  root `<svg>` element. Used by accessibility tools and as fallback
  for the prompt sidecar.

### 2. Dark-mode handling (default: do nothing)

The viewer
([`folio-assistant/viewer/index.html`](../../../folio-assistant/viewer/index.html))
applies a CSS filter to embedded SVGs in dark mode:

```css
[data-theme="dark"] { --svg-f: invert(1) hue-rotate(180deg); }
[data-theme="light"] { --svg-f: none; }
.txb img, .txb svg { filter: var(--svg-f); }
```

So a black-on-white figure becomes white-on-near-black automatically
(red → cyan, green → magenta, blue → yellow under hue-rotate 180°,
which preserves perceived chroma well enough for monochrome line-art).
**Do not author a `.dark.svg` sibling unless the filter produces a
bad result** — duplicating files is overhead for no benefit.

### 3. Dark-mode override (`.dark.svg`) — when needed

Author a hand-tuned `<slug>-N.dark.svg` only when:

- The figure has multiple distinct accent colours that hue-rotate
  scrambles (e.g. red/green/blue coral tubes — under invert+hue-rotate
  red becomes cyan and green becomes magenta, which loses the standard
  RGB association).
- The figure has photographic content (raster textures, gradients)
  that filter-invert mangles.
- The figure has labelled regions whose hue conveys meaning that
  must be preserved across modes.

The dark-mode override should:

- Use a near-black background (`#0e0e12` — matches the viewer's
  `--bg` value) and light strokes (`#e0e0e6`).
- Keep accent colours **unchanged from the light variant** (red is
  still red, blue still blue) — these are the colours the override
  exists to preserve.
- Otherwise be byte-for-byte identical to the light variant in
  geometry, layout, and labels.

The `.dark.svg` sibling is consumed by a viewer-side swap (TBD; see
*Followups* in
[`docs/coordination/illustrations.md`](../../../docs/coordination/illustrations.md));
the LaTeX printed-PDF path always uses the light variant.

### 4. Prompt sidecar (every figure)

Author `<slug>-N.prompt.md` next to each SVG. The pipeline reads
this and emits the body as a small italic margin note via
`\figprompt{…}` in the printed PDF, and the title as a small
italic line under the caption via `\figtitle{…}` (see
[`content/pipeline/render-latex.ts`](../../../content/pipeline/render-latex.ts)
`readPromptSidecar`). Format:

```markdown
# <Short generated title — 3–7 words>

F<slot> (P<tier>). <one-paragraph description of what the figure
depicts, what the elements mean, and any constraints inherited from
the surrounding prose (notation register, accent-colour conventions,
etc.). 2–4 sentences; this is the printed-PDF margin note.>
```

The first line **must** be a markdown `#` heading carrying the
figure's title. The title is auto-displayed:

- in the figures index (`docs/figures-index.md`) as a column,
- under the figure in the printed PDF (`\figtitle{…}` below the
  `\caption{…}`),
- in the viewer caption strip when present.

The title should be short, declarative, and self-contained — readable
without seeing the body. Examples: *"The Hecke skein triple"*, *"The
roadmap as argument flow"*, *"Bring's surface as a coral"*.

Keep the body plain prose with inline `$...$` math allowed — it *is*
run through the markdown→LaTeX renderer (unlike the SVG `<text>`).

### 5. Wiring into the target block

Edit the target `.md` block (named in the recommendations entry) and
insert the markdown image at the position specified there. The
renderer auto-emits `\includesvg`, the caption, and the prompt-sidecar
margin note. Example:

```markdown
![Caption text — written for the audience, not for SEO.](rendered/<slug>-N.svg)
```

The alt-text becomes the figure caption in the printed PDF; keep it
informative (1–2 sentences) and obey the notation register.

## Iteration: edits to an existing figure must update the prompt

When the author asks for a change to an authored figure ("make the
arrows thinner", "swap the red thread for blue", "add a third
panel", "use a square viewBox"), do **not** silently re-edit the
SVG. The `.prompt.md` sidecar is the authoritative record of what
the figure depicts; the printed PDF surfaces it as a margin note.
A stale prompt is an audit-flag.

Procedure for every iteration:

1. **Update the title and body of `<slug>.prompt.md`** so they
   describe the *new* state, not the previous one. Treat the prompt
   as the spec; a follow-up author should be able to re-author the
   SVG from scratch given only the prompt.
2. **Re-author the SVG** to match the updated prompt.
3. **Decide variant policy.** A *small tweak* (line weight, label
   wording, viewBox tightening) keeps the same variant letter and
   filename — the prompt edit captures the change. A *substantive
   redesign* (different layout, different visual metaphor) bumps
   the variant letter (`-A` → `-B`) and writes a new
   `<family>-B.svg` + `<family>-B.prompt.md`; the original
   variant stays on disk.
4. **Re-run** `bun run content/pipeline/build-figures-index.ts`
   so the index reflects the new title and prompt.

Never edit the SVG without also editing the prompt. The two files
are a unit.

## Variation generation

When the author asks for "N versions" of a figure (or you suspect
the spec is ambiguous and want to surface alternatives), produce
`<slug>-A`, `<slug>-B`, … each with **a distinct authoring prompt**.
Different prompts should target different stylistic axes:

| Axis | Variant A leans | Variant B leans | Variant C leans |
|------|-----------------|-----------------|-----------------|
| Layout | linear / horizontal | radial / centred | grid / matrix |
| Density | minimal (essentials only) | rich (full annotations) | progressive (key elements highlighted) |
| Style | geometric (clean strokes) | hand-drawn (sketched feel) | schematic (boxes-and-arrows) |
| Colour | monochrome | monochrome + 1 accent | full palette (3 accents) |

Pick 2–3 axes to vary so the author has meaningfully *different*
options, not minor tweaks. Each variant's `.prompt.md` records which
axis values it chose so a follow-up session can re-roll a single axis
without re-authoring everything.

## Indexing

After authoring, run:

```bash
bun run content/pipeline/build-figures-index.ts
```

This regenerates [`docs/figures-index.md`](../../../docs/figures-index.md)
— the master catalogue of every authored figure across the paper,
grouped by chapter, with thumbnail embeds, prompt summaries, and
status badges (single / multi-variant / dark-override-present).
Reviewers (and the editorial pipeline) consume this index to see
the whole illustration slate at a glance.

## Editorial-pipeline hooks (TBD — formalisation)

Once this skill stabilises:

- A pre-merge gate runs the figures-index generator and fails if it
  is out of sync (catches `git add`-omissions on new SVGs).
- The recommendations doc gains an `authored:` field per entry so
  the index can show which P0 / P1 / P2 slots are still open.
- Block kind `figure` (or extension to `diagram`) carries explicit
  `prompt`, `variants[]`, `darkOverride` metadata so the index is
  generated from typed manifests instead of filesystem scan.
- Variation generation goes through a parameterised script so the
  three variants are repeatable from the same axis-choice spec.

For now: filesystem scan, manual variant naming, prompt sidecar
sufficient.

## Anti-patterns

- **Don't put `$...$` math in SVG `<text>`** — it renders as literal
  dollar signs.
- **Don't omit the white background rect** — the figure becomes
  unreadable on dark backgrounds (the viewer filter only works on
  monochrome content).
- **Don't author a `.dark.svg` for every figure** — overhead for no
  benefit on monochrome line-art.
- **Don't bake the equation into the figure** — typeset it in the
  prose where the LaTeX renderer handles spacing and font alignment.
- **Don't use hue-rotated colours in the dark variant** — preserve
  the original accent colours (the whole point of overriding the
  filter).
- **Don't reuse a slug across chapters** — slugs are repository-wide
  unique to keep the figures index clean.
