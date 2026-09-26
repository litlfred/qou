---
# qou-k6s6
title: 'Sweep guard: a witness that DEFINES an anchor is not migratable'
status: todo
type: task
created_at: 2026-08-19T20:54:16Z
updated_at: 2026-08-19T20:54:16Z
---


## Where this comes from

The closing line of bean `qou-m9xp`, left unclaimed:

> **The general lesson for the tnjb / qou-1c4y sweeps:** a witness that
> some piece of infrastructure reads as *the definition of an anchor* is
> not a migratable witness. Re-pinning it does not move a value to the
> other layer, it removes the layer. Worth an exclusion list before the
> next batch runs.

`qou-1c4y` (the muon → proton migration) is **in-progress** and the
remaining muon population is ~1906 witnesses, so the next batch will run
against a tree that has no guard against repeating this.

## What happened without one

`9a9c6b31c7` regenerated `computations/q-pinning-50-digit.witness.json`
at the proton pin as batch item 1 of 25. That file is not an instance of
the muon layer — it *is* the muon layer's definition. The result:

- `_q0_value_for_anchor('muon')` and `('proton')` returned the same
  number, so the flip detector could not tell the pins apart
- `Q0_FLIP` 0 → 262, every one a false positive against a correct witness
- the `q_parameter.py:113` pin guard tripped for **208 producers**
- `q0_anchor_manifest.json` still filed the producer under `ideal_muon`,
  so the repo's two records of its anchor disagreed for four days

Fixed by `2e4745448d` / `1f25060f2` (restore, not re-pin). Two agents
found it independently — `qou-m9xp` and `qou-cezp` — which is a sign of
how visible the *symptom* was and how invisible the *cause*.

## The work

An explicit exclusion list the sweep driver consults, plus the mechanism
to keep it honest. Sketch, not a prescription:

1. **Enumerate the anchor-defining files.** Start from what infra reads:
   `qou_substrate.witness._q0_value_for_anchor`,
   `substrate/q_parameter.py`, and anything in
   `q0_anchor_manifest.json`. Grep for witnesses read by *name* from
   library code rather than by glob — that is the signature.
2. **Make the driver refuse them**, with the reason in the refusal, not
   a silent skip.
3. **Prefer a derived guard to a hand list.** A hand-maintained list
   decays exactly like the importer counts in AGENTS.md did. If the set
   can be computed (a witness imported by name from `tools/` or
   `computations/substrate/`), compute it.

## Not claimed by me

`qou-1c4y` has an owner and this is squarely its scope. Filed so the
lesson does not live only in the closing paragraph of a completed bean.
