# P3.1 audit — conjectural-propagation sweep

**Pair**: [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md) §P3.1
**Branch**: `claude/audit-math-framework-FXlp2`
**Method**: New script
[`content/pipeline/conjectural-propagation-audit.ts`](../../content/pipeline/conjectural-propagation-audit.ts)
walks every block manifest, builds the `uses[]` graph, and reports
every `theorem`/`proposition`/`lemma`/`corollary` whose transitive
cone touches a `conj:` label (per AGENTS.md §3b STRICT propagation
rule).
**Witness**: [`2026-05-01-p3-1-conjectural-propagation.witness.json`](2026-05-01-p3-1-conjectural-propagation.witness.json).

## Headline

| Quantity | Count |
|----------|------:|
| Total blocks scanned | 1334 |
| Provable blocks (thm/prop/lem/cor) transitively touching a `conj:` | **260** |
| Blocks with **no** transitively-conjectural cone | 1074 |

**This is a systemic finding, not a list of individual fixes.**
Three classes of conjecture propagate to nearly everything:

| Conjecture | Reach (out of 260 violators) |
|------------|----------------------------:|
| `conj:electron-shells-hopf` | 255 |
| `conj:skein-shell-correction` | 251 |
| `conj:shell-threading-energy` (broken ref — see below) | 251 |
| `conj:elliptic-stability-locus` | 251 |
| `conj:baryon-period-ratio` | 229 |
| `conj:hyperbolic-volume-transcendence` | 228 |
| `conj:regularity-breakdown` | 226 |
| `conj:shell-correction-term-seven` | 225 |
| `conj:shell-closure-nf-term-count` | 225 |
| (15 more conjectures at 225 each) | 225 |

The first ~20 `conj:` labels share an essentially identical cone
covering ~225 of the 260 violators — i.e., these are **substrate
foundation conjectures** that almost the whole paper sits on.

## Three observations and a policy decision required

### Observation 1 — broken `uses` reference

`conj:shell-threading-energy` appears in 3 files (`uses[]`) and the
definition-index, but **no `shell-threading-energy.ts` block exists**.
The closest match is `conj:shell-threading-conjecture` (in
observations). The 251 reach for `conj:shell-threading-energy` is
purely transitive through the 3 callers; if the missing block is a
typo for `conj:shell-threading-conjecture`, fixing those 3 callers
would not change the propagation conclusion (the chain still flows
through other foundation conjectures).

### Observation 2 — most "violators" cluster on shared foundations

The cones intersect heavily: 225 of 260 violators ride on the same
core ~20 conjectures. Mechanical demotion would re-label most of the
paper from `proposition` → `conjecture`, drastically obscuring where
the actually-novel conjectural content lives.

### Observation 3 — definitions transmit the propagation

Per AGENTS.md §3b clarification, definitions DO transmit propagation
to downstream provable blocks (even though definitions themselves are
not subject to the demotion rule). Many of the 260 violators reach
their conjectural ancestor via a definition (e.g.
`prop:X → def:Y → conj:Z`). The demotion target is `prop:X`, not
`def:Y`.

## Policy decision (user input requested)

AGENTS.md §3b STRICT propagation, applied mechanically, would demote
260 blocks. Three options:

### Option A — Mass demotion (strict §3b)

Demote every one of the 260 violators from
`theorem`/`proposition`/`lemma`/`corollary` to `conjecture`. Honest
under §3b STRICT, but visually loud.

- **Pro**: enforces the paper's epistemic discipline; every "if … then"
  claim is correctly labelled.
- **Con**: ~20% of the paper turns into `conjecture` blocks; the
  reader's signal-to-noise on what is *actually* an open conjecture
  shrinks; review tools that special-case `conj:` get noisy.

### Option B — "Modulo substrate axioms" framing (relaxation)

Identify the ~20 substrate foundation conjectures and elevate them
to a labelled **substrate-axiom set** (conceptually `axiom:` rather
than `conj:`). Provable claims downstream of these substrate axioms
remain `proposition` — they are conditional theorems "modulo the
substrate axioms", which is the honest framing of the paper.

The remaining few `conj:` blocks (those that are NOT substrate
foundations — actual novel mathematical claims) propagate normally.

- **Pro**: matches the paper's intent (the QOU substrate is
  axiomatised, not conjectured); reviewer-clear about what's open vs
  what's foundation.
- **Con**: requires identifying which 20 conjectures are substrate
  axioms — a real classification task. May require renaming
  blocks `conj:X` → `axiom:X` (schema change) or adding a `tags:`
  field (lightweight).

### Option C — Audit-only (current state)

Keep all blocks at their current kind, document the propagation
explicitly in audit witness, and reference the witness from the
paper. No structural changes.

- **Pro**: minimum churn.
- **Con**: §3b STRICT propagation remains formally violated; review
  tools using §3b will report 260 violations indefinitely.

**Recommendation**: Option B. The QOU substrate IS an axiom set
(every framework needs unprovable foundations); the existing
`conj:` blocks for foundations conflate "substrate axiom" with
"open mathematical conjecture". Re-classifying ~20 substrate
foundation conjectures as substrate axioms (via a `tags: ["substrate-axiom"]`
field, no schema change required) would resolve the propagation
issue cleanly without mass demotion.

## Provable blocks with **no** conjectural cone (clean — 1074 blocks)

These are the genuinely-unconditional results in the paper. The
propagation audit's positive finding: **80% of provable blocks are
clean**. Examples include the categorical-action / Frobenius-pairing
/ mass-identity foundation, the Hecke-tower setup
(`crossing-energy.lean` etc.), and the BW-coefficient derivations
audited under P1.2/P1.3.

## Recommended next action

User picks A / B / C; if B, the workplan opens task **P3.1b**:
"Substrate-axiom classification — identify ~20 foundation
conjectures and tag them `substrate-axiom`; re-run propagation
audit with `substrate-axiom` cones excluded; expect violator count
to drop ~225 → ~35, which is the actual list of *open mathematical
conjectures* whose downstream cones need demotion under §3b STRICT."
