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
| **c5-involution-leibniz** | stochastic-mechanics | (0) | **Already wired** (false positive) — see detector-bug note below. |

## Disposition status — COMPLETE

**28 blocks wired this tranche** (+ 2 authored prose-lead blocks), in
dependency order with verified-zero forward refs (cross-chapter and
intra-chapter), all rendering exactly once (cross-manifest duplicate
check = 0):

1. **`meson-scale-independence`** (1) — ✅ wired into
   `sec:particle-interactions-orphan-reconnect`. CAL decay-width table
   confirmed canonical, left as-is.
2. **q-beta cluster (22)** — ✅ wired:
   - New section **`sec:mass-algebraic-qbeta-formalize-first-gates`**
     (mass-theory, after Hoefsmit so `t-beta-collapse` is backward) —
     13 gate/recursion blocks + prose lead.
   - New section **`sec:hecke-chi-per-block-delta-tau-canonical-weights`**
     (mass-endomorphism) — 4 cluster-G blocks + prose lead.
   - Existing-section homes: Borromean h⁴ + H₃ weights →
     `sec:mass-algebraic-markov-gram` / residue section; `t_β` collapse
     pair → `sec:hoefsmit-he4-magic-a-binding`; meson-K →
     `sec:mass-physical-face`.
   - `qbeta-z-recursion-to-ck-recursion-bridge` moved mass-endomorphism
     → mass-theory (forward-dep on `c_k`-recursion).
   - Prep fix: `q-beta-c-k-recursion` `uses[]` repaired (`rem:`→`prop:`
     for `alpha-em-habiro-bar-involution`; dropped the forward
     cross-chapter `q-heat-kernel-peter-weyl` edge, kept as narrative).
3. **braids-and-knots (8)** — ✅ triaged: 3 wired
   (`meson-em-sinh-closed-form`, `meson-qcg-fusion-identity` →
   `sec:lepton-meson-parallel`; `unit-modulus-eigenvalue` **moved**
   braids → mass-theory + `thm:`→`prop:` fix →
   `sec:mass-algebraic-markov-gram`). **5 held WIP** — the Habiro chain
   (`a8-partition-function-identity`, `cyclotomic-strand-doubling`,
   `habiro-pochhammer-bridge`, `habiro-precision-ladder-equivalence`,
   `zeta8-witness-level2-su2`). **Decision: leave WIP** (deeper review
   2026-06-24 below).
4. **climax (2)** — ✅ wired (`selection-rule-anchors-c1-c3`,
   `selection-rule-c2-prediction`, both proved) →
   `sec:knot-operator-energy`.
5. **stochastic (1) — `c5-involution-leibniz-decomposition`** — **already
   wired** (false-positive orphan; see below). No action.

### Detector-bug note (regex false negative)

The orphan detector's blocks-array regex (`blocks:\s*\[(.*?)\]`,
non-greedy) closed early on a `]` **inside a manifest comment**
(`"… : generation" [4]` in `stochastic-mechanics.ts`), truncating that
array and falsely orphaning every block after it — here
`c5-involution-leibniz-decomposition` (already wired at line 52). Fix:
strip `//` line comments before the regex
(`scratchpad/orphan_analysis.py`). A cross-manifest duplicate check after
the fix confirms **all 28 wired blocks appear in exactly one manifest** —
no block was double-wired by the false positive.

### Habiro-chain review (2026-06-24) — why WIP, not wired

Per-block soundness is fine; the blockers are **placement + unmaintained
draft metadata**, which make wiring an editorial call, not a mechanical
one. The chain: `a8-partition-function-identity` →
`cyclotomic-strand-doubling` → `habiro-pochhammer-bridge` →
`habiro-precision-ladder-equivalence`; `zeta8-witness-level2-su2` →
{`cyclotomic`, `pochhammer`}.

- **Sound math.** `cyclotomic-strand-doubling` is *not* a soundness
  problem — the refuted "strand-doubling" reading is correctly demoted
  to a documented historical note and the block now states only the true
  algebraic identity Φ₈(X)=Φ₄(X²). The others are proved;
  `zeta8` carries one Wenzl-annihilator `sorry` with a `[wenzl1987]`
  citation (acceptable per §1).
- **Forward cross-chapter deps.** `habiro-pochhammer-bridge` uses
  `def:habiro-ring` and `habiro-precision-ladder-equivalence` uses
  `prop:mass-endomorphism-tower` — both in **mass-theory** (later than
  braids). Wiring requires moving the 5-block chain braids → mass-theory,
  and `mass-endomorphism-tower` sits at line ~639 (after the new gates
  section), so the chain cannot sit with its thematic kin.
- **Unmaintained `uses[]`.** `habiro-precision-ladder-equivalence`'s
  `uses[]` lists `prop:q-schur-y-lambda-closed-form` (exists **nowhere**
  — dangling; the block's `.md` never references it) and
  `prop:mass-endomorphism-tower` (resolves but is unreferenced in prose),
  while the one block its prose *does* cite
  (`prop:tau-M-asymptotic-rep-theory`) is **absent** from `uses[]`.
  Cleaning this is a judgment call about real-vs-spurious deps.
- **Draft-tagged**, in the `c_k`/Habiro flip-flop area (AGENTS.md). The
  owner's instruction was "triage braids-8 *separately*"; the triage
  outcome for these 5 is **hold** — left untouched for the owner to
  clean `uses[]` + place deliberately.

### Remaining

5 orphan provable parents, all the braids-and-knots Habiro chain —
held WIP per the review above (sound math; needs owner-driven `uses[]`
cleanup + braids → mass-theory move).

## Reproduce

```bash
python3 scratchpad/orphan_analysis.py   # writes scratchpad/orphan_report.json
```
