---
# qou-e9pp
title: 'Witness-refresh advice is unsafe: ZERO of ~700 self-stale witnesses are safe to re-run'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T13:15:18Z
updated_at: 2026-08-19T13:15:50Z
---


## What was measured

`computations/witness_staleness_triage.py` (PR #5002) normalises both producer
versions through `ast.unparse` and reports which self-stale drifts can move a
number. Three runs, 1564 commits of `main` apart, corpus 2898 -> 2985:

    2026-08-11   substantive 242   rewritten 329   unresolvable 107   cosmetic 0
    2026-08-19   substantive 239   rewritten 329   unresolvable 106   cosmetic 0
    2026-08-19   substantive 256   rewritten 338   unresolvable 103   cosmetic 0

`cosmetic` (= safe to refresh) is 0 every time. Source-identical is necessary
but not sufficient; the two extra gates are environment match and whether the
producer emits provenance at all.

## Status: the measurement is done; two follow-ups are NOT

1. **`rewritten` is ~48% of the backlog and has no branch-side fix.** The
   recorded `commitSha` resolves to nothing because rebase-merge rewrites it.
   `main` spent 13 commits in one 8-day window hand-patching the field, which
   buys only the interval until the next merge. A durable fix has to run
   post-merge on `main`, or the field has to stop being treated as decidable.
   Not attempted here.
2. **The `substantive` queue (256) is untriaged.** This script says which drifts
   *can* move a number; it does not say which *did*. That needs the runner
   (`witness_producer_executes_audit.py`, already on `main` via #4960 -- its
   ENV_MISSING / DIFFERS buckets are the run-time complement to this script's
   static env gate). NOTE (2026-08-19): the container-provisioning half of this
   blocker is GONE — `scipy` 1.17.1 and `clarabel` 0.11.1 install from PyPI and
   `pyhecke_native` 0.9.0 builds from `tools/pyhecke-native/` with maturin.
   What remains is compute time, not capability.

## Do not

Do not drain `substantive` by re-running producers in an under-provisioned
container. Measured cost: `binding_canonical.py` without `pyhecke_native` moves
`tr_M_atom` 0.388 -> 0.575 (48%) with no crash and no warning.


## 2026-08-19 — RETRACTION and the mechanism that replaced it

Provisioned this container to try to unblock item 2 (`scipy` + `clarabel` from
PyPI; `pyhecke-native` is not on PyPI but builds from `tools/pyhecke-native/`
with maturin). Testing the env hypothesis falsified it.

**Retracted:** "binding_canonical.py without pyhecke_native moves tr_M_atom
0.388 -> 0.575, therefore environment." With `pyhecke_native 0.9.0` and every
recorded package matched, the producer returns `0.57517233101788385191` --
byte-identical to the no-native run and to what main carries. Environment was
never the cause.

**Actual mechanism:** import-cone drift. The producer is source-stable;
`tr_m_atom_via_transfer.py`, which computes the quantity, is not. Added a
one-hop import-cone gate; it absorbs all three surviving cases
(`cosmetic_import_cone_drift` 3, `env_differs` 0, `strips_provenance` 0).

**Unchanged:** `cosmetic = 0` of ~700. Better supported than before.

**Item 2 is still blocked, but for a different reason.** The container is now
adequately provisioned, so provisioning is no longer the blocker -- what remains
is that triaging 257 `substantive` witnesses means *running* 257 producers,
several of which are long-compute (the `rho_k_co_casimir_extended` entry in
`qou-mnrd` records a 2-hour run that did not finish). That wants a time budget
and a nightly, not an idle pass.

**Do not** re-cite the environment example. Use
`witness_import_cone_staleness_audit.py` for the import axis.

## 2026-08-19 — item 1 closed by measurement; a broken producer found doing it

**Item 1 (import-cone over-flag) is CLOSED.** I had declined to automate an
infra-vs-numeric discriminator because it would be an unvalidated heuristic. So
I measured it: all 8 flagged witnesses re-run, mathematical fields diffed.

    drift confined to witness_base / _precision : 0 moved, 5 unchanged
    drift touching anything else                : 2 moved, 0 unchanged
    1 crashed before writing

Perfect separation on 7 decidable cases; infra-only now has its own bucket.
n=7 is small and `_precision` is only 2/2 — re-measure before leaning on it.

**NEW — a genuinely broken producer (needs an owner call, not a fix from me).**
`casimir_d6_qcorrection_structure.py` requests the ideal/muon anchor;
`q_parameter` refuses with the yfvb/tnjb anti-corruption guard because
`q-pinning-50-digit.witness.json` no longer holds a muon value. Commit
`9a9c6b31c` ("sweep(tnjb): first 25 witnesses regenerated at the proton pin")
flipped it muon → proton. The guard is behaving CORRECTLY. The producer is
simply unrunnable on current main.

Do **not** relax the guard, and do **not** silently re-pin the producer to
proton — which anchor a d6-Casimir q-correction should use is a substantive
question, and AGENTS.md keeps the *ideal* CAL-2 definition muon-based even
though compute defaults to proton. 16 files reference `QOU_Q0_ANCHOR`; this
sweep may have broken more than one.

**AGENTS.md is stale on this point.** It states `q-pinning-50-digit.witness.json`
"holds the muon value `1.10997859555733471…`". On main it holds
`1.1099785827513808075916` — the proton value. Corrected in this branch.

**Self-inflicted lesson worth keeping.** A `git checkout -- computations/`
cleanup landed mid-run and left the triage witness carrying new-format data
under provenance hashed from the reverted script — an internally inconsistent
artifact, the exact corruption class this bean is about. Commit before running,
and never blanket-revert a tree while a producer is in flight.
