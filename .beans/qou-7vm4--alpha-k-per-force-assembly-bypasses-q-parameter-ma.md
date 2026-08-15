---
# qou-7vm4
title: 'alpha_k_per_force_assembly bypasses q_parameter: manifest says ideal_muon, code imports q_at directly (proton), and the except-fallback silently picks muon if the import fails'
status: todo
type: task
created_at: 2026-08-11T10:31:47Z
updated_at: 2026-08-11T10:31:47Z
---


## Evidence

Three sources disagree about which q₀ anchor this producer uses.

| source | says |
|---|---|
| `computations/q0_anchor_manifest.json` | `alpha_k_per_force_assembly` ∈ **`ideal_muon`** (257 entries) |
| `alpha_k_per_force_assembly.py:85-86` | `from qou_substrate.constants import q_at; Q0 = str(q_at())` — **proton, unconditionally** |
| `:88` fallback literal | `1.1099785955573347198997632204832250266562084087802` — **muon** |
| committed `alpha-k-per-force-assembly.witness.json` | `q0` = 70-digit **muon** |

Three of four say muon; the live import says proton. The manifest's own
`_convention` states *"q_parameter auto-selects by the running producer's stem;
`QOU_Q0_ANCHOR` env var overrides"* — but this producer **never calls
`q_parameter`**, so its manifest tag cannot fire.

## Two defects, one of them anchor-independent

**(1) The manifest tag is not honoured.** Either the code should go through
`q_parameter` (making it muon, reproducing the committed witness, zero number
change from the committed state), or the manifest entry is stale and should move
to `physical_proton` (in which case the witness must be regenerated and every
`delta_q_value_at_q0` moves by 114–148 ppb, with `1/α_EM` moving −78.96 ppb).
**Do not guess which** — the 2026-08-07 directive says touched code defaults to
proton, but the manifest tag is a deliberate per-producer assignment and this
producer is on the α_EM path. Owner call.

**(2) The `except Exception` fallback silently changes the anchor.** Regardless
of (1): if `qou_substrate` fails to import, `Q0` falls back to a hardcoded
**muon** literal while the happy path yields **proton**. So the anchor depends on
whether an import succeeds — a silent, environment-dependent physics choice with
no warning and nothing recorded in the witness. This is a defect under either
reading of (1) and should be fixed independently: fail loudly, or record the
fallback in the witness.

This exactly explains the puzzle a prior agent hit — *"the producer already had
the direct-proton import at `74d93256a6`, yet the witness it produced carries
70-digit muon"*. It did not need another q₀ source: the import path failed (or
predated the re-pin) and the muon fallback fired silently.

## Not a straddle

Checked: `alpha_k_per_force_assembly.py:101` records that the δ_q rule is *"kept
local rather than imported from rosso_jones_three_strand_delta_q.py"*, so the two
producers do not share a cache. `rosso_jones_three_strand_delta_q` is **not
listed** in the manifest and therefore falls through to the proton default. The
two compute the same six δ_q carriers at different anchors **by construction**,
which is legitimate under the two-layer convention but is nowhere stated — a
reader diffing them sees a 114–148 ppb discrepancy with no explanation.

## Settles the earlier question

`qou-4jut`'s ALPHAK front asked whether the committed muon witness was stale.
**Per the manifest it is correct as recorded** — verdict (a), nothing to migrate,
and the earlier decision to restore it rather than adopt the proton pin was
right. What remains is not staleness but this tag-vs-code inconsistency, plus the
`scriptHash` drift left by the guard edit landed in the same PR.

## Also relevant: the ladder is proton, and that is load-bearing

`alpha_em_form_ladder` is **not listed** either, so it falls through to the
**proton** default — which is what makes its 1.672 ppb figure the canonical one
rather than the 80.51 ppb muon evaluation. See
`docs/audits/2026-08-11-alpha-em-anchor-dominance.md`. Whatever is decided in (1)
should not silently move the ladder.
