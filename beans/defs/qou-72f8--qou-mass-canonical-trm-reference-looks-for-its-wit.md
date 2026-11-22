---
# qou-72f8
title: qou_mass canonical_trm_reference looks for its witness in _internal/ where none exists
status: completed
pr: 8248
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T11:12:49Z
updated_at: 2026-11-22T21:33:06Z
parent: qou-5vkl
---


## The defect

`qou-mass/src/qou_mass/_internal/canonical_trm_reference.py`:

    _HERE = Path(__file__).resolve().parent          # -> .../qou_mass/_internal/
    ...
    for name in _WITNESSES:
        p = _HERE / name
        if not p.exists():
            continue
    raise FileNotFoundError(...)

**Measured:** `_internal/` contains **0** `*.witness.json` files; **25** sit one
level up in `qou_mass/`, including both entries of `_WITNESSES`
(`atomic-tr-m-mpfr-50dps-proton.witness.json` and
`atomic-tr-m-mpfr-50dps.witness.json`). So every call raises, with the message

    no |tr_M| witness recorded at this run's pin 1.109978582751380807591669…;
    inspected []

Note `inspected []` — the empty list is the tell. The error is written to
report which candidate files were examined and found to be at the wrong pin;
an empty list means none was even opened, i.e. this is a path bug wearing a
provenance error's clothing. That is probably why it has survived: the message
reads like a legitimate "regenerate at this anchor" complaint.

`_internal/markov_weights_symbolic.py:322` does
`from canonical_trm_reference import tr_m_nucleon`, so that path in the shipped
package is dead.

## Why it is not fixed in the change that found it

Found under `qou-4383` while regenerating the `computations/` copy of the same
witness. Fixing it changes what the **published package** (1.0.0) computes, and
it is a packaging-path question rather than that bean's ordering subject.

## The fix, and the thing to check first

`_HERE.parent` is the obvious one-line change. **Do not land it without
checking what the function then returns**, because until 2026-09-13 the data it
would have found was grouped-era: the `computations/` copy was pre-ruling
(2026-08-19) and the mirror matched it. Both are canonical now
(`52b154af6e1`), so a fix today makes the function work AND return canonical
values — but a fix made against a stale mirror would have quietly switched a
dead path on to serve superseded numbers, which is worse than raising.

So: sync the mirror first (or verify it is synced), then repoint the path, then
re-run whatever `markov_weights_symbolic` feeds and diff.

## Related

`qou-y4gi` — the same module family validates the pin but not the intra-nucleon
ordering, which is the deeper version of this. `qou-4383` — where it surfaced.

## Progress (2026-11-17, PR #8248)

- [x] Update `_rows_for_pin()` in `computations/canonical_trm_reference.py` and `qou-mass/src/qou_mass/_internal/canonical_trm_reference.py` to search `(_HERE, _HERE.parent)` so the vendored `qou_mass/_internal/` module locates `atomic-tr-m-mpfr-50dps*.witness.json` in `qou_mass/` (PR #8248, Commit 1 `d3dcd4c4757a988299ad0246ed502bd2358a90e4`).
- [ ] Merge PR #8248 (`claude/round53-trd0-9nnz-fixes`, HEAD `b4185f1dac70a76b08299e291f3137fb9b60fe3c`)

## 2026-11-22 — CLOSED: the fix is on main via port #8248 (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Checked against main `3c4c98fccf3`.

The "Progress" entry above records the fix on a batch PR that never merged. It reached main as `d226f1ed95` ("port #8248: ..."), which names this bean. Verified on main: `qou-mass/src/qou_mass/_internal/canonical_trm_reference.py` searches `_HERE.parent` as well as `_HERE`.

## 2026-11-22 — Applicability review (owner instruction 2026-11-22, bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Retroactive review of this pass's closure against `docs/coordination/owner-rulings.md` on main `3c4c98fccf3`.

**Verdict: ALREADY-DONE (closure stands).** The bean is about tooling or arithmetic precision (gates, audits, float64 paths, provenance, tracker structure). Its premises name no physics object, convention, anchor or particle assignment, so none of the retired premises (σ₀σ₁ photon, trefoil electron, convention C, the z = 1 Q_β base, census selection, absolute mass, muon pin A, virtual photons, adopted quark charges) or today's rulings (strand colour states, b = −qX, the fixed constant term 1 of the photon, the block U(1)_em charge) bear on it. What landed still answers its question.
