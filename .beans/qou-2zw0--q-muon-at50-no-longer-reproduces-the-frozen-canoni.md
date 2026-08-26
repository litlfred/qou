---
# qou-2zw0
title: q_muon_at(50) no longer reproduces the frozen canonical muon pin
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:29:21Z
updated_at: 2026-08-26T07:29:59Z
---

## The fact

A committed witness's muon row is not reproducible with today's import cone.

`qbeta-barodd-d-ladder-ord17.witness.json` records
`numeric_diagnostic_h_D_vs_S/muon/h = 0.20906032199`, which is exactly
`h(1.1099785955573347...)` — the **frozen canonical muon pin**, i.e.
`derived_50_digit.q` from `q-pinning-50-digit.witness.json`.

The producer computes that row from `qou_substrate.constants.q_muon_at(50)`,
which today returns `1.109978595642739046681795`. That is the **CODATA-2022
lepton-tower derivation**, the third of the three values AGENTS.md warns are
all called "the muon q₀". `q_muon_at` derives from live `MASS_RATIO_MU_E_STR`
via `q = 1/(1 − √(Vol(4₁)/(m_μ/m_e)))`, so it **cannot** produce the frozen
pin, at any dps.

Re-running the producer therefore moves the row by 7.69e-11 in q (7.65e-10 in
h). That is ~100× **smaller** than the 11.5 ppb μ–p separation, which is what
distinguishes it from a pin change and is how it was caught.

## It is import-cone drift, not producer staleness

Checked for all 11 producers in the PR #5823 batch: every witness's recorded
`scriptHash` equals the sha256 prefix of its producer at HEAD. The producers
did not change. Something in their cone did — the case AGENTS.md describes as
*"a producer's own source can be byte-stable while the module it calls
changed"*.

## Cause UNDETERMINED — and the obvious next step does not work

The natural check is `git log <baseline commitSha>..HEAD -- constants.py`.
The baseline `commitSha` is `544ef706b8f0983009862b4390b4bf56723b7e47` and
**does not resolve** (`fatal: bad object`) — the `rewritten` class, ~49 % of
the backlog per AGENTS.md, and a direct `git fetch origin <sha>` is refused by
GitHub regardless of whether the object exists.

So do **not** state that `q_muon_at` changed, or that CODATA moved. What is
established is only: *the committed value is not reproducible today, and
`q_muon_at` is not the function that produced it.*

## Why this is worth more than one witness

`q_muon_at` is THE muon-anchor accessor. If it derives rather than reading the
frozen pin, then every producer using it is on the derived muon value while
every producer reading `q-pinning-50-digit.witness.json` is on the frozen one.
Those two populations disagree at the 11th digit and both call themselves
"muon". That is a second-order version of the same layer-straddle problem
`qou-1c4y` exists to remove, one level down.

**Not measured here:** how many producers call `q_muon_at` vs read the pin
file, and whether any single quantity mixes them. That is the actual scoping
question and it is the next step.

## Surfaced by

PR #5823 (bean `qou-aj91`), as the control run that separated pin-effect from
environment-effect. Not caused by that change and deliberately not fixed
there.
