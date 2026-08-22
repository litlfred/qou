---
# qou-7vm4
title: 'alpha_k_per_force_assembly bypasses q_parameter: manifest says ideal_muon, code imports q_at directly (proton), and the except-fallback silently picks muon if the import fails'
status: todo
type: task
priority: normal
created_at: 2026-08-11T10:31:47Z
updated_at: 2026-08-15T22:32:50Z
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


STATUS 2026-08-15 (reorientation pass): DEFECT 2 FIXED, DEFECT 1 STILL OPEN.

Defect 2 (the anchor was chosen by whether an import succeeded) landed with
PR #4961 (6e101ea1bf). At main 08b6ff7e7d the producer now WARNS on the fallback
path and RECORDS which path it took as q0_source / q0_anchor in the witness
payload, so a witness produced in a constrained environment can no longer
silently carry a different anchor. The fallback itself is retained -- the
producer must still run without qou_substrate.

Defect 1 is UNCHANGED and is an owner call, deliberately not decided in code:
q0_anchor_manifest.json lists this producer under ideal_muon, but the code
imports q_at directly (proton) rather than routing through q_parameter, so the
manifest tag cannot fire. Either honour the tag (muon; reproduces the committed
witness; zero numbers move) or re-tag to physical_proton (regenerate; every
delta_q_value_at_q0 moves 114-148 ppb and 1/alpha_EM moves -78.96 ppb). The
2026-08-07 directive says TOUCHED code defaults to proton, but a manifest tag is
a deliberate per-producer assignment and this producer is on the alpha_EM path.

This bean now tracks defect 1 only.

## 2026-08-22 — RESOLVED (measured, not assumed)
The straddle this bean describes no longer exists; the manifest was re-tagged in the interim and
all three layers now agree on PROTON, verified on main:
  * q0_anchor_manifest.json  -> `physical_proton` (406 members); NOT in `ideal_muon` (3 members)
  * alpha_k_per_force_assembly.py -> imports q_at() == the proton pin
  * committed witness -> q0_anchor "proton", and its q0 matches the 50-digit proton pin to 1.9e-50
    while differing from the muon pin by 1.16e-8 (the mu-p tension) — so the VALUE agrees with the
    label, not merely the tag.

What WAS still broken, and is fixed here: the producer's own documentation had not been updated with
the re-tag, so it asserted the opposite of the truth in two places — a source comment claiming the
manifest says `ideal_muon` with the decision "deliberately NOT decided here", and, worse, a
HARDCODED witness field `q0_manifest_tag: "ideal_muon"` shipped in every witness it emitted. That
false comment is what sent this session chasing an already-resolved defect.

Fix: the tag is now READ from q0_anchor_manifest.json at run time (`_manifest_tag()`), so it cannot
go stale against a future re-tag; a lookup failure returns an explicit "unknown"/"untagged"/
"AMBIGUOUS" string rather than guessing. Comment and caveat rewritten to the measured state.
Witness regenerated: 4/4 assertions pass, ZERO mathematical values moved (only invocation metadata),
and the environment block is a strict SUPERSET of the committed one (numpy/sympy/mpmath/
pyhecke_native all matched after installing them, plus a new pyhecke_native_build fingerprint) — so
this avoids the provenance-degradation trap recorded in bean qou-5380. Blocking precision gates green.
