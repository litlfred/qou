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

| Metric | Count (pre-fix) |
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

## The one load-bearing orphan — `meson-scale-independence` (WIRED)

`particle-interactions/meson-scale-independence` (`prop:`) is cited by
the **rendered** proof
`mass-theory/calibration-cohomology-alignment-proof`, which relies on it
for the **CAL-3 leg** of the canonical three-calibration count
(`QOU.Mass.calibrations_eq_cohomology`, the AGENTS.md cheat-sheet
theorem). The proof body explicitly invokes "meson scale-independence"
(Hopf-link complement has `Vol = 0`, so the meson scale is a third datum
independent of `(m_e, q_0)`). The edge is real and load-bearing — wired
into `sec:particle-interactions-orphan-reconnect` after its
`def:categorical-meson` dependency (orphan-parent count 34 → 33).

### Calibration-layer note (owner-clarified 2026-06-24)

The block's `.md` "Calibration structure" table frames **CAL-2 = 𝔇_β**
(neutron β-decay width) and **CAL-3 = 𝔇_π** (pion decay width). Per
owner clarification this is **correct and intended**: the decay-width
triple `(m_e, 𝔇_β, 𝔇_π)` is the **mathematically-ideal canonical
calibration**. The mass-based framing used elsewhere — e.g. the AGENTS.md
cheat-sheet's `CAL-2 = m_μ` / proton-ratio pin — is the
**Physical-Observations layer**: a *derivation* chosen for smaller
experimental error, not a different calibration. This two-layer
distinction is already explained in the paper's Physical chapter. The
table is left **as-is**; an earlier draft of this doc mis-labelled it
"stale" — that was the documentation error, now corrected.

## The other 33 — unintegrated WIP clusters (owner-directed disposition)

Not load-bearing on any rendered block. Owner triage decision
(2026-06-24): **integrate the q-beta cluster + triage the
braids-and-knots set separately** (do **not** leave the cluster as WIP).

| Cluster | Chapters | Count | Disposition (owner 2026-06-24) |
|---------|----------|-------|--------------------------------|
| **q-beta c_k / Habiro / qbeta** (`q-beta-*`, `qbeta-*`, `t-beta-*`) + adjacent (`borromean-h4`, `h3-markov-wenzl-weights`, `meson-kaon-pion-hecke-seifert`) | mass-theory (17) + mass-endomorphism (5) | 22 | **Integrate** into the rendered paper — owner sign-off given. Wire in dependency order; honest block kinds (§3b conjectural propagation for c_k near-matches). |
| **Habiro / cyclotomic / meson-em / zeta8** | braids-and-knots | 8 | **Triage separately, per-block** — some (meson-em / Hecke-Seifert identities) may be sound and wireable independent of q-beta; others stay WIP. |
| **selection-rule c_k anchors** | climax-volume-mass | 2 | Triage with the q-beta cluster (c_k-adjacent). |
| **c5-involution-leibniz** | stochastic-mechanics | 1 | Phase-6 scaffold chapter; triage last / likely leave. |

## Disposition status

1. **`meson-scale-independence`** — ✅ wired
   (`sec:particle-interactions-orphan-reconnect`); CAL-2/3 decay-width
   table confirmed correct, left as-is.
2. **q-beta cluster (22)** — owner-approved for integration; in progress.
3. **braids-and-knots (8)** — per-block triage; in progress.
4. **climax (2) + stochastic (1)** — triaged alongside the above.

## Reproduce

```bash
python3 scratchpad/orphan_analysis.py   # writes scratchpad/orphan_report.json
```
