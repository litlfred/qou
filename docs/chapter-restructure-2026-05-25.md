# Chapter Restructure — 2026-05-25

**Branch:** `claude/restructure-framing-2026-05-25`
**Source session branch (instructed via session start):**
`claude/magical-keller-fH4Or` (in use by a parallel session for
pyhecke-native work; this PR uses a themed branch name to avoid
clobbering)
**Status:** plan locked, migration in progress
**Cross-link:** [`docs/reorganization-map.md`](reorganization-map.md) for the
running block-move ledger.

## Motivation

The current paper has 580 forward-reference violations across 23 chapters and
152 one-voice violations, both concentrated in `braids-and-knots` (793 blocks,
59k .md lines — ~1/3 of the entire paper). The chapter sits at the structural
center but bundles four distinct themes (algebra · geometry · particles · mass)
plus most of the paper's quantum-mechanics emergence content (stochastic
mechanics ~370 blocks, Pauli ~150 blocks, measurement ~200 blocks).

Audit findings drove the following decisions:

| Decision | Driver |
|---|---|
| Split `braids-and-knots` into 6 chapters | 793-block chapter; ~80% of voice violations |
| Repurpose `models-of-qous` as a 5-step roadmap framing chapter | Reader has no anchor for the categorical→algebraic→geometric→archimedean→physical arc |
| Split `archimedean-universe` (389 blocks) into structural + spectra | 30 fwd-edges to observations/molecular/organic |
| Promote stochastic mechanics + gravity + Pauli + measurement to their own chapters | ~1100 blocks of major thematic content with no clear home |
| Add NEW Part III "Physical Realization" | Observation/molecular/organic naturally cluster |
| Rename Part IV to "Dynamics, Information, Emergence" | Captures fluid + stochastic + info + measurement + Langlands |

## Final structure

```
FRONT MATTER
  Introduction · Notation (preview)

PART I — FOUNDATIONS                                    (~580 blocks)
  1.  QU axioms                          (was ch3 quantum-universes)
        + Heisenberg uncertainty content folded in
  2.  QOU                                (was ch4 quantum-observable-universes)
        + Lagrangian / action principle folded in
        + def:habiro-ring relocated here (fixes 7 fwd refs)
  3.  Models of QOUs (framing) ←REPURPOSED  (was ch7 models-of-qous)
  4.  Brane tower                        (was ch5 lifting-and-descent)

PART II — STRUCTURAL MECHANICS                        (~1,295 blocks)
  5.  Braids, Knots, Hecke               (from braids-and-knots §A–D)
  6.  q-Hyp → Vol → Mass · tangle-E · E=m·c_q² [climax]
        (from braids-and-knots §E–F + scattered E=mc_q² blocks)
  7.  Bring's surface (deep)             (from archimedean-universe split A)
  8.  Statistics and Symmetrisation       [NEW]
        Pauli, spin-statistics, S_n irreps, fermion/boson derivation
  9.  Particles + CP + Higgs + Neutrino + charge
        (from braids-and-knots §G + particle-interactions + scattered)
  10. Mass — Theory (light)              (from braids-and-knots §H–L statements)
  11. Mass — Application (heavy)         (from braids-and-knots §H–L compute)
  12. Gravity & spacetime emergence     [NEW]
        (from scattered: braids 70, fluid, QOU, observations)

PART III — PHYSICAL REALIZATION (NEW)                   (~493 blocks)
  13. Predicted particle spectra         (from archimedean-universe split B)
        + magnetic moments folded in
  14. Observations (CODATA)              (was ch10 observations)
  15. Molecular construction
  16. Organic chemistry

PART IV — DYNAMICS, INFORMATION, EMERGENCE              (~666 blocks)
        (renamed from "Further Machinery")
  17. Fluid dynamics
  18. Stochastic mechanics              [NEW]
        (~250 blocks centralised from braids-and-knots Markov content)
  19. Information theory                 (PV=nRT, Turing here)
  20. Measurement & Observation         [NEW]
        (~200 blocks centralised from scattered measurement content)
  21. q-Geometric Langlands

BACK MATTER
  Glossary · 8 Appendices · Index of Definitions
```

## Detanglement gains

| Metric | Current | Target | Δ |
|---|---:|---:|---:|
| Forward refs | 580 | ~250 | −57% |
| Largest chapter | 793 | ~370 | −53% |
| Voice violations | 152 | ~57 (post mechanical sweep) | −62% |
| Themes without a home | 6+ | 0 | — |

Critical tangles eliminated:
- `braids-and-knots → archimedean-universe`: 43 fwd edges → 0 (Bring's basics in Ch 3 framing, full Bring's in Ch 7 backward-referenced)
- `braids-and-knots → particle-interactions`: 29 fwd edges → 0 (Particles is AFTER Braids in new order)
- `def:habiro-ring` → 7 fwd refs fixed by moving definition to QOU Ch 2

## Ch 3 framing chapter (priority deliverable)

Repurpose existing `models-of-qous` content. ~22-25 block target.

```
§1 Opening                                    1 block (new prose)
§2 Categorical step                           1 (new remark)
§3 Algebraic step                             1 (new remark)
§4 Geometric step                          ~10-12
       • q-Hyperbolic / knot complements (new)
       • Reeb-bundle = Vol (new)
       • Yekutieli tessellation, h^{2j} ladder (new)
       • Bring's def + role (extract from descartes-universe)
       • Bring's basics: genus 4, χ = -6, S_5/A_5 (extract)
       • Notation conventions (new)
§5 Archimedean step                           1
       • Reuses: categorical-archimedean-bridge content
§6 Physical step                              1
§7 Alternative-model gallery                 ~6
       Archimedean: calabi-yau, ale, instanton (REUSE existing blocks)
       Non-archimedean: enveloping-algebras, p-adic-realisation,
                        finite-field-realisation (REUSE)
§8 Common-language table                      1
§9 Arc diagram                                1
```

Existing models-of-qous blocks to **remove or relocate** (out of Ch 3):
- `q-yang-mills-levi`, `main-commutative-diagram` (+ proof) → move to Climax Ch 6
- `yang-mills-mass-gap` (+ table) → move to Mass — Theory Ch 10 or own block in framing §5
- `gr-substrate-geometry` → move to QOU Ch 2 or Models §5
- `categorical-archimedean-bridge` (+ proof) → keep in framing as §5 anchor
- `c-substrate-via-levi`, `webster-inner-product`, `heisenberg-commutator-prop` → move to QU Ch 1 or QOU Ch 2
- `spatial-realization-functor`, `categorical-action-vs-chern-simons` → move to QOU Ch 2
- `archimedean-encounter-intro`, `outro-models-of-qous` → rewrite as new opener/closer
- `witt-vector-lifting-intro`, `witt-vector-lift`, `skew-poisson-integration` → move to QOU Ch 2 or Brane tower Ch 4
- `jones-polynomials` → move to Hecke Ch 5

## Provenance map (current → new)

### From `braids-and-knots` (793 blocks)

| Current location | → New chapter | Block count |
|---|---|---:|
| §A-D braids/Hecke/knot groups | Ch 5 Braids, Knots, Hecke | ~60 |
| §E-F Möbius/crossing/Reeb/hyperbolic | Ch 6 Climax (q-Hyp → Mass) | ~80 |
| §G skein/particle/hadrons | Ch 9 Particles | ~85 |
| Pauli / spin-statistics content | Ch 8 Statistics & Symmetrization | ~150 |
| §H-L mass statements | Ch 10 Mass — Theory | ~90 |
| §H-L mass compute | Ch 11 Mass — Application | ~280 |
| Stochastic / Markov content | Ch 18 Stochastic mechanics | ~250 |
| Gravity content (70 blocks) | Ch 12 Gravity | ~70 |
| CP/Higgs/Neutrino scattered | Ch 9 Particles | ~120 |
| Measurement scattered | Ch 20 Measurement & Observation | ~150 |
| **Subtotal accounted for** | | **~1,335** |

(Over-counts because keyword-mention vs primary-theme distinction; final block count will be ~793. Provenance map will be revised as we move blocks.)

### From `archimedean-universe` (389 blocks)

| Current section | → New chapter | Block count |
|---|---|---:|
| Bring's geometry (def, χ, S_5) | Ch 7 Bring's surface (deep) | ~115 |
| Bring's intro stub | Ch 3 framing §4 | ~3 |
| Particle assignments on Bring's | Ch 9 Particles | ~80 |
| Predicted particle spectra | Ch 13 Predicted spectra | ~150 |
| Higgs/neutrino content | Ch 9 Particles | ~50 |

### From `models-of-qous` (40 blocks → split)

| Current section | → New chapter | Block count |
|---|---|---:|
| Framing roadmap content (repurposed) | Ch 3 framing (keep here) | ~15 |
| YM-Levi / main-diagram | Ch 6 Climax or Ch 10 Mass-Theory | ~5 |
| Categorical-archimedean bridge | Ch 3 framing §5 | ~3 |
| Heisenberg/Webster commutator | Ch 1 QU + Ch 2 QOU | ~5 |
| Witt vector lifting | Ch 4 Brane tower | ~5 |
| Jones polynomials | Ch 5 Hecke | ~3 |
| Spatial realization functor | Ch 2 QOU | ~2 |
| CY / ALE / instanton (model gallery) | Ch 3 framing §7 (keep) | ~6 |
| Non-archimedean (p-adic, finite-field) | Ch 3 framing §7 (keep) | ~6 |

### From `particle-interactions` (116 blocks)

→ Ch 9 Particles (~110), Ch 11 Mass — Application (~6 nuclear bits)

### From `observations` (236 blocks)

→ Ch 14 Observations (mostly stays), Ch 13 Predicted spectra (~50 comparison
content), Ch 9 Particles (~10 scattered)

### From `information-theory` (102 blocks)

→ Ch 19 Information theory (mostly stays), Ch 20 Measurement (~50 if measurement
content lives here), Ch 18 Stochastic (~14 stochastic-info overlap)

## Migration order

1. **PR phase 1 — framing chapter scaffold** (this branch)
   - Write Ch 3 §1, §2, §3, §5, §6 (the conceptual step-summary blocks — new content)
   - Update `models-of-qous.ts` chapter manifest with new section order
   - Keep all existing blocks for now; deletions happen in phase 4

2. **PR phase 2 — Bring's basics into Ch 3 §4** (separate PR)
   - Extract Bring's def, genus, χ, S_5/A_5 stub blocks from descartes-universe
   - Insert into Ch 3 §4
   - Update downstream `uses[]` refs to point at new location
   - Fixes the 43-edge braids→archimedean tangle

3. **PR phase 3 — habiro-ring + Heisenberg + Lagrangian relocation**
   - Move `def:habiro-ring` from braids-and-knots to QOU Ch 2
   - Migrate Heisenberg uncertainty content to QU Ch 1
   - Migrate Lagrangian content to QOU Ch 2

4. **PR phase 4 — braids-and-knots split** (largest tranche)
   - Create new chapter dirs: Hecke, climax, Statistics, Particles, Mass-Theory, Mass-App, Stochastic, Gravity
   - Move blocks by theme (see provenance map above)
   - Delete the old braids-and-knots manifest

5. **PR phase 5 — archimedean-universe split**
   - Split into Bring's (Ch 7) + Predicted spectra (Ch 13)
   - Relocate Higgs/neutrino content to Particles

6. **PR phase 6 — Part III + Part IV creation**
   - Update paper manifest with new Part labels
   - Add Measurement & Observation chapter (Ch 20)
   - Rename Part IV to "Dynamics, Information, Emergence"

7. **PR phase 7 — final detangler / one-voice sweep**
   - Run `bun run validate` end-to-end
   - Re-run chapter-complexity-review; verify forward refs at target (~250)
   - Run one-voice audit; verify violations at target (~57)

## Decisions made (resolved)

- Part II rename → "Structural Mechanics" ✓
- Part IV rename → "Dynamics, Information, Emergence" ✓
- Pauli/spin-statistics → own chapter (Ch 8) ✓
- Quantum measurement → own chapter in Part IV (Ch 20) ✓
- Stochastic mechanics → Part IV new chapter (Ch 18) ✓
- Gravity → end of Part II (Ch 12) ✓
- Bring's basics in framing Ch 3 §4 (not gallery) ✓
- Heavy Bring's content in Ch 7 (deep properties) ✓
- Mass split: Theory (light) vs Application (heavy) ✓
- archimedean-universe → split into Bring's (Part II) + spectra (Part III) ✓
- organic-chemistry → standalone, not merged ✓
- q-Langlands → stays standalone in Part IV ✓
- Models gallery includes p-adic + char-p (non-archimedean) ✓

## Decisions deferred

- Detailed §-by-§ structure of Ch 9 Particles (will draft when authoring)
- Exact split-seam for Mass — Application sections (Hoefsmit vs Wenzl vs LP)
- Whether Stochastic chapter splits into sub-themes (250 blocks may need internal structure)
- Floater audit (brane tower / tessellation / Etc.) — not returned, lowering priority

## Orphan blocks — content not rendered (101 total)

Audit on 2026-05-25 found 101 block files that exist on disk but are
not listed in any chapter manifest's `blocks: [...]` array, so they
don't render in the paper output. Distribution:

| Chapter dir | Orphan count | Action |
|---|---:|---|
| archimedean-universe | 33 | reconnect — all substantive (simulator + remark content) |
| braids-and-knots | 60 | reconnect — research notes + remarks, 18-161 lines each |
| observations | 2 | reconnect — substantive editorial remarks |
| particle-interactions | 5 | **delete** — stale placeholder data tables |
| quantum-observable-universes | 1 | reconnect — diagram block |
| **total** | **101** | — |

Most likely cause: chapters were refactored and blocks were created
but never added to their manifest's `blocks: [...]` array. Resolution
deferred to a dedicated follow-up PR — each orphan needs a section
placement decision, so the work is per-block.

Example particle-interactions orphans to delete:
- `atomic-braid-mass-table1-data` through `table4-data` (placeholder
  data blocks, 10-15 lines each)
- `wedderburn-mass-formula` (incomplete)

Example archimedean-universe orphans to reconnect:
- `beta-decay-braid-visualizer`, `beta-decay-energy-scale`,
  `beta-decay-interpretation`, `electroweak-higgs-torus-link-triplet`,
  `nucleon-nf-observability`

## Sibling-PR coordination

This is a big restructure. Active sibling branches to coordinate with:
- (none currently identified — will check `gh pr list` before each phase)

Per AGENTS.md sibling-coordination rule: post intent comments on overlapping PRs
once Phase 1 lands.

## Authors

Restructure plan derived from session 2026-05-25 with author and three audits:
- Theme audit (Pass 1, Pass 2, plus tangle/entanglement supplement)
- Detanglement (chapter-complexity-review)
- One-voice audit

Background work in progress:
- Mechanical voice cleanup on branch `claude/voice-cleanup-mechanical-2026-05-25`

## Phase 7 — Post-restructure detangler analysis (2026-05-25)

Forward-edge count: **580 → 514** (11% drop, target was 57%).

The narrower-than-targeted drop reflects an inherent consequence of
splitting one big chapter into focused destinations: cross-references
that used to be intra-chapter are now inter-chapter forward edges.
The split is still a structural win (each new chapter is reviewable
on its own), but raw forward-edge count is a lagging indicator.

### Top remaining tangle pairs

| Source | Target | Edges | Notes |
|---|---|---:|---|
| mass-theory | mass-application | 61 | Theory statements cite compute machinery |
| climax-volume-mass | mass-application | 34 | Climax forward-refs Wenzl/Hoefsmit compute |
| braids-and-knots | mass-application | 24 | Hecke chapter refs mass-compute |
| braids-and-knots | particle-interactions | 23 | Hecke refs particle content |
| mass-application | appendix-surreals | 22 | Compute refs surreal-number appendix |
| braids-and-knots | climax-volume-mass | 21 | Standard fwd (Hecke → Climax = algebra → geometry) |
| mass-theory | stochastic-mechanics | 20 | Theory refs stochastic interpretation |
| particle-interactions | mass-application | 20 | Particles ref mass-compute |
| braids-and-knots | mass-theory | 19 | Hecke ref mass theorems |
| braids-and-knots | predicted-spectra | 16 | Hecke ref predictions |

### Per-chapter forward-edge count (top 5)

| Chapter | Fwd | Bwd | Notes |
|---|---:|---:|---|
| braids-and-knots | 135 | 26 | Hecke chapter — still high, but most refs are to later chapters where mass machinery lives |
| mass-theory | 91 | 94 | Heavy fwd to mass-application (compute) and stochastic-mechanics |
| climax-volume-mass | 86 | 63 | Forward refs to mass machinery downstream |
| particle-interactions | 56 | 49 | |
| mass-application | 52 | 162 | Mostly backward-referenced (162 backward edges) — healthy |

### Interpretation

The Mass-Theory ↔ Mass-Application split, while pedagogically sound
("statements first, compute after"), means Theory statements that
cite the algorithms that prove them become forward edges. Two possible
follow-ups:

1. **Re-extract Theory statements** to remove direct uses[] refs on
   Application implementation blocks; cite at a higher abstraction
   ("by the Wenzl bridge" rather than `uses: ["prop:wenzl-bridge-...]"`).
2. **Reorder Mass-Application before Mass-Theory** in the paper
   manifest — mathematically unconventional but would flip 61 forward
   edges to backward. Probably not worth the narrative cost.

For now: accept 514 forward edges as a structural cost of the split.
Each new chapter has tight thematic identity, which the original
braids-and-knots did not.
