---
# qou-e9pp
title: 'Witness-refresh advice is unsafe: ZERO of ~700 self-stale witnesses are safe to re-run'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T13:15:18Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5vkl
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


## 2026-09-07 — FIFTH run. `cosmetic = 0` holds; one bucket more than doubled

Re-measured on `main` (this bean's own advice is a BASELINE — re-run, never
quote). Full split, five runs:

| run | date | decided | substantive | cosmetic | import_cone_drift | rewritten | unresolvable |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 2026-08-11 | 678 | 242 | **0** | — | 329 | 107 |
| 2 | 2026-08-19 | 674 | 239 | **0** | — | 329 | 106 |
| 3 | 2026-08-19 | 697 | 256 | **0** | — | 338 | 103 |
| 4 | 2026-08-30 | 559 | 186 (33.3%) | **0** | 4 | 309 (55.3%) | 60 |
| 5 | **2026-09-07** | **603** | **205 (34.0%)** | **0** | **9** | **333 (55.2%)** | **55** |

**Runs 1-3 report no `decided` total; that column is my arithmetic**
(substantive + cosmetic + rewritten + unresolvable), and those runs predate the
`import_cone_drift` bucket existing, which is why it is blank rather than zero
for them. Runs 4-5 quote the script's own printed total.

Also on run 5: `cosmetic_env_differs` 1, `cosmetic_import_infra_only` 0,
`cosmetic_strips_provenance` 0, `unparseable` 0.

**The headline holds a fifth time, across ~4 weeks: ZERO self-stale witnesses
are safe to refresh.** The idle-pass policy that sends the witness half of the
budget to sidecars instead is confirmed, not merely still-believed.

**The finding is the bucket that GREW.** `cosmetic_import_cone_drift` went
**4 → 9** while every other proportion held (substantive 33.3 → 34.0 %,
rewritten 55.3 → 55.2 %), so this is not denominator drift. That bucket's own
label records **"measured 2/2 moved"**: a producer whose source is byte-stable
while a **numeric-bearing module it calls** changed. So these 9 are not "safe
to refresh" — they are the *opposite*, the cases where a re-run is EXPECTED to
move a number, and they are **invisible to the `git diff <producer>` check**
that AGENTS.md's idle-pass policy tells agents to run first. It is the only
bucket trending, and it trends toward more silent wrongness, not less.

**This bean's own title is stale:** "~700 self-stale witnesses" against a
decided population that has been **559–628** for a month. Left as-is rather
than rewritten, since the title is how the bean is cited elsewhere; noted here
so a reader does not carry the 700 forward.

**Its two follow-ups are still open and neither was attempted here:** the
`rewritten` 333 (55.2 %) has no branch-side fix — rebase-merge destroys the
recorded `commitSha`, so `git diff the producer first` is *unrunnable* for over
half the backlog — and the `substantive` 205 is untriaged, needing the runner
rather than this static gate. **Bean stays open.**

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
