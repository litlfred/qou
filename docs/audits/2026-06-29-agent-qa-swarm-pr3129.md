# Agent-QA review swarm — full-paper pass (PR #3129)

**Date:** 2026-06-29 · **Branch:** `claude/integration-audit-qa-params-ikp76z` ·
**Reviewer:** `claude-opus-4-8` (swarm of high-effort sub-agents, `local/qa-agent-drain`)

## What ran

After the mechanical 6-axis `/integration-audit all` sidecar refresh (332 new + 2,410
refreshed `.qa.json`), a 5-wide agent swarm walked the **whole `quantum-observable-universe`
paper** chapter-by-chapter (65 batches, ≤25 blocks each), reviewing every block against the
**agent-only** QA criteria it lacked a fresh verdict for (24 criteria — the `da-*`
devil's-advocate lenses, `wall-side-*`, `voice-statement-no-interpretation`,
`fit-section-chapter`, `proof-*` equivalence/vacuity; `proof-rater-*` excluded — no score
field in the writer). Findings were merged **append-only** via
`qa-merge-findings.ts` (prior reviewer entries never deleted; each new entry stamps
`reviewer.version = claude-opus-4-8`, fixing the missing-provenance gap).

## Totals

| | |
|---|---|
| Batches merged | **65 / 65** |
| Agent findings written | **21,310** |
| — pass | 16,379 |
| — warn | 1,829 |
| — fail | 453 |
| — n/a | 2,649 |
| QOU blocks now carrying a fresh Opus-4.8 verdict | **1,230** |
| Distinct blocks with ≥1 critical fail | 62 |
| Critical-finding beans created | ~26 |

Full per-block detail (pass/warn/fail + severity + evidence + notes) lives in each block's
`.qa.json` sidecar `criteria.<id>[]` arrays — this doc is the rollup.

## Headline finding: the dominant defect class is **vacuous / divergent Lean siblings**

Across the corpus the recurring (and by far most common) critical pattern is **sound
narrative math paired with a Lean sibling that proves strictly less** — `: True := trivial`
shadow stubs (§0a), self-assuming projections (`:= ctx.claim_X`, §3b-cond degenerate),
`Nonempty`/`∃x,x=expr` tautologies, `0*q`/`id`-degenerate witnesses, conclusion-as-axiom,
and a few `def`-disguised or commented-out (non-compiling) files. This is the same class as
bean `2ti7` (382-orphan drain) and the `2026-06-18-self-assuming-projection-triage.json`
catalogue; tracked in aggregate as bean **`i8dg`** (≈40 blocks listed).

## Genuine math/factual errors found (beaned individually)

| bean | block | defect |
|---|---|---|
| `zxin` | collatz-contact-boundary.md:62 | `[2]_q²−[3]_q = q` is false (=1) |
| `bi65` | borromean-bloch-group-element | `8·Λ(π/3)=8G` false (2.71≠7.33); 2 octahedra at π/4 |
| `maxe` | unit-modulus-eigenvalue-proof:7-8 | "`|tr|≤2` for unit-det 2×2" false (diag(2,½)) |
| `xdgu` | jones-faithfulness-crossing-8:14 | unique Jones ≤11 crossings (Conway/KT mutant ⇒ ≤10) |
| `ni0m` | q-chromaticity.md:51 | "S₅ has exactly three S₃ copies" (has 10) |
| `e0ke` | double-magic-Ca40-diagram:18 | `(5,4,4,4,3)` not self-conjugate (conj `(5,5,5,4,1)`, sum −5) |
| `mpuo` | gram-matrix-h3-symbolic:23 | "det G≠0 for q>0" false (root q≈0.4656) |
| `lsyd` | frobenius-positivity-filter:23 | "exactly half = 2^{A−1}/4^A" (=2^{−A−1}; A=6→1/128) |
| `hs1c` | hoefsmit-ew-cell-content | contradictory multiplicity tuples |
| `58b0` | francium-extremal-metal / helium-hopf-diagram | Cs<Fr ionization; rank-1-vs-2 |
| `qtfu` | topological-mass family | additive norm split from squared Pythagorean |
| `qpfi` | conj-lepton-tower-h-n+1-branching | ξ_m formula self-contradicts (~100× factor) + scratchpad left in |
| `uxon` | ns-obstruction-computation | Bring surface real-dim 2 vs 4 inconsistency |
| `etlc` | toffoli-transfer-matrix-proof | false `z·c+d=z` algebraic claim |

## Discipline / data-integrity beans

`6fib` AI-slop filler overwriting load-bearing steps · `8kfd` §1a audit-dodge (`0*(...)`) ·
`eg0i` purged `λ_scale` reintroduced (vassiliev + higgs-t28) · `meah` + `kaf4` stale CAL
framing / Q_β self-contradiction vs decay-width canon · `m64w` stale z³ Markov-bug ·
`j1sn` stale refuted K_3*=6_1 in Lean · `hyit` stale witness link · `u7c3` `vco8` `4fa3`
`kqdz` `5ixs` `4gwq` hidden-DOF / Millennium-overclaim / non-sequitur-banner / empirical
fragility · `pcti` `dn6e` Lean-weaker-than-narrative · `pzpb` citation misuse.

## Caveats

- Scope: the `quantum-observable-universe` paper only (the other folio papers were not in
  the swarm). The `proof-rater-*` scored criteria were excluded.
- Findings are **agent verdicts**, high-recall; the durable record is the sidecar. The
  beaned items are the agent's confident criticals — each still wants author adjudication
  before a fix lands.
- Two findings (batch 8) skipped by the merger on a path-resolution edge case (negligible).
- Main advanced +41 during the run (sibling `r13d/r13e` orphan-compile work); a rebase is
  needed at merge-prep.
