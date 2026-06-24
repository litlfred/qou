# Orphan provable-parent blocks — re-integration analysis (2026-06-24)

**Scope.** Provable-kind content blocks (`theorem` / `lemma` /
`proposition` / `corollary`) whose `.ts` files exist on disk under
`content/quantum-observable-universe/` but whose root-name appears in
**no chapter manifest** `blocks:[]` array — i.e. they are authored but
never rendered into the paper.

**Why this doc exists.** A prior session set out to "re-add 24
accidentally-dropped orphan parents" on the premise that they were
referenced via `uses[]` by *rendered* blocks (so the paper carried
broken cross-references). That premise does **not** hold under a
from-scratch re-derivation; this doc records the corrected analysis so
the finding survives session restarts.

## Method

`scratchpad/orphan_analysis.py` (self-contained; the `bun run validate`
pipeline is currently miga-broken):

1. Build the *rendered set* = union of every string in every chapter
   manifest's `blocks:[]` arrays.
2. Walk every block `.ts`; read `kind`, `label`, `uses[]`,
   `interprets`.
3. Orphan = block whose root-name ∉ rendered set.
4. For each orphan, reverse-index `uses[]`/`interprets` to find
   consumers, split into **in-manifest (rendered)** vs **orphan**
   consumers.

`uses[]` cites **labels** (`prop:foo`); manifests list **root-names**
(`foo`) — the analysis maps between them.

## Corrected findings

| Metric | Count |
|--------|-------|
| Blocks on disk (QOU) | 2667 |
| Orphans (any kind) | 43 |
| **Orphan provable parents** | **34** |
| …referenced by *some* block | 18 |
| …isolated (no consumer at all) | 16 |
| …with a **same-chapter in-manifest** consumer (mechanically placeable) | **0** |
| …**load-bearing on a rendered block** | **1** |

The headline corrections vs the prior premise:

- **0** orphans have a same-chapter in-manifest consumer — so the
  "place each next to a rendered consumer in its own chapter" mechanical
  plan has **no targets**.
- **Exactly 1** orphan is cited by a rendered block. The other 17
  "referenced" orphans are cited **only by other orphans** — they are
  self-contained clusters dropped (never wired) as units.
- All 34 trace to the genesis mega-commit `3d03626f` (2783 content
  `.ts` files born at once) and have **never** appeared in a manifest
  since. This is *authored-but-unwired WIP*, **not** *accidentally
  removed* content. (Scope discipline: this is a scope-limited
  observation about manifest membership, not a claim that the blocks'
  mathematics is wrong.)

## The one load-bearing orphan — `meson-scale-independence`

`particle-interactions/meson-scale-independence` (`prop:`) is cited by
the **rendered** proof
`mass-theory/calibration-cohomology-alignment-proof`, which relies on it
for the **CAL-3 leg** of the canonical three-calibration count
(`QOU.Mass.calibrations_eq_cohomology`, the AGENTS.md cheat-sheet
theorem). The proof body explicitly invokes "meson scale-independence"
(Hopf-link complement has `Vol = 0`, so the meson scale is a third datum
independent of `(m_e, q_0)`). The edge is real and load-bearing.

- **Core proposition is correct and canon-aligned** — `Vol(Hopf) = 0`
  matches the cheat sheet ("m_π genuinely independent of (m_e, q₀),
  Vol(Hopf)=0").
- **All three of its `uses[]` deps are rendered**
  (`def:categorical-meson` — same chapter;
  `prop:frobenius-lepton-meson-bridge`,
  `prop:hoefsmit-binding-amplitude` — braids-and-knots, earlier
  chapter). Wiring creates **no** dependency cascade and **no**
  forward-ref (consumer chapter mass-theory (#95) is *after*
  particle-interactions (#93) → backward edge).
- **Natural home exists**: section
  `sec:particle-interactions-orphan-reconnect` ("Reconnected orphan
  blocks (Phase 7)") already holds `categorical-meson`; the prop slots
  in immediately after it.
- **Wrinkle — stale CAL-2 framing.** The block's `.md` "Calibration
  structure" table presents **CAL-2 = 𝔇_β** (neutron β-decay width) and
  **Q_β as a calibration**. Current canon (AGENTS.md cheat sheet) is
  **CAL-2 = m_μ**, with "the neutron β-decay width 𝔇_β/τ_n is Q_β's
  experimental face, **not** a third calibration." The *rendered*
  consumer proof itself uses the canonical "q₀-modulus" framing — so the
  table in this block diverges. Rendering the block as-is would inject
  that divergence into the paper; this is an author call (do not
  silently rewrite canonical framing).

## The other 33 — unintegrated WIP clusters (author triage)

Not load-bearing on any rendered block; integrating them is an editorial
decision about publishing in-progress research, **not** a mechanical
fix. Per the detangler-watcher discharge bands, isolated-block /
placement decisions are **author-assist, never auto-discharge**.

| Cluster | Chapters | Count | Character |
|---------|----------|-------|-----------|
| **q-beta c_k / Habiro / qbeta** (`q-beta-*`, `qbeta-*`, `t-beta-*`) | mass-theory (17) + mass-endomorphism (5) | 22 | The unsettled c_k truncation-order / Habiro saga (AGENTS.md flip-flop history; `c_k≥3` are near-matches, not proved). |
| **Habiro / cyclotomic / meson-em / zeta8** | braids-and-knots | 8 | Mixed: Habiro-bridge WIP + meson EM/QCG identities + ζ₈ witnesses. |
| **selection-rule c_k anchors** | climax-volume-mass | 2 | c_k-adjacent (selection-rule-anchors-c1-c3 → c2-prediction). |
| **c5-involution-leibniz** | stochastic-mechanics | 1 | Phase-6 scaffold chapter (manifest comment: "NEW Ch 18 — Phase 6 scaffold"). |

These reference each other but no rendered block, so they were dropped
(never wired) as self-contained units. The q-beta majority is precisely
the research AGENTS.md flags as flip-flop-prone and not production-wired
— integrating it into the rendered paper needs explicit author intent.

## Recommended disposition

1. **`meson-scale-independence`** — wire into
   `sec:particle-interactions-orphan-reconnect` (resolves the dangling
   reference in the central calibration proof). Flag/repair the stale
   CAL-2 table per author preference.
2. **The 33 WIP-cluster blocks** — leave unwired pending author
   direction; record here rather than guessing. None block the rendered
   paper.

## Reproduce

```bash
python3 scratchpad/orphan_analysis.py   # writes scratchpad/orphan_report.json
```
