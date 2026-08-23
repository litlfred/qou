---
# qou-jvav
title: witness_dependency_drift resolver missed subdirectory upstreams — 357 of 688 drift records were false
status: in-progress
type: task
created_at: 2026-08-23T17:11:30Z
updated_at: 2026-08-23T17:11:30Z
---

`staleness-gates.sh` is red on `scriptHash + upstream drift`. Two findings, one
fixed here.

## 1. FIXED — the resolver reported 358 files as missing while they sat in the repo

`witness_dependency_drift.py` resolved a recorded upstream by trying exactly two
locations:

    ups_path = witness_path.parent / ups_name   # a sibling
    if not ups_path.exists():
        ups_path = HERE / ups_name              # computations/ root

That was the entire layout before the Phase-6 refactor moved clusters into
subdirectories. Upstreams that landed in `data/`, `alpha/`, `sweeps/` resolve to
neither and were reported `upstream_missing` — while present:

    ame2020.json                          -> computations/data/
    alpha-cluster-recursion.witness.json  -> computations/alpha/
    low-isotope-binding-sweep.witness.json-> computations/sweeps/

119 records each, **357 of 688 drift records, all false**. Added a third step that
searches the tree, skips `_deprecated`, sorts for determinism, and records any
bare-name matching more than one path in `_AMBIGUOUS_UPSTREAMS` so a wrong pick is
visible rather than silent.

    drift records: 688 -> 330

Checked the two names that do resolve ambiguously
(`canonical-mass-table-extended`, `m-p-borromean-verification-50dps`, each in
`computations/` and `qou-mass/src/qou_mass/data/`): the copies are byte-identical,
so the ambiguity is currently harmless.

## 2. NOT fixed — the remaining 330 are real, and have one dominant cause

242 of them are two upstreams that genuinely changed and whose consumers were never
regenerated. 122 `canonical-isotope-witness-Z*` witnesses all record

    recorded ed68106158faf521b4f0   current 184d7e1287bdbc155834

for `canonical-mass-table-extended.witness.json`. One regeneration, 122 stale
consumers. Same shape for `m-p-borromean-verification-50dps` (121).

## 3. Also found: the per-Z renderer has been dead since witnesses went to strings

`atlas_render_per_z.py` died on its first row with

    TypeError: can't multiply sequence by non-int of type 'float'

because `err_ppm` is now a full-precision STRING (`_precision.fmt`) and the
renderer still did `value * 1000.0`. Fixed by coercing through **mpf, not float** —
the coercion should not be where a 28-digit value gets truncated.

**Its output is deliberately NOT committed.** Running it inserts a 4399-line
`AUTO:per-z-sections` block into
`content/.../recursive-atom-knot-atlas.md`, and those markers have **never** been
in the committed file. That is not restoring lost content, it is publishing a new
appendix section — an author's call, not a side effect of fixing a crash.

## What would actually close the gate

`fail = bool(all_drifts) or (bool(n_self_stale) and args.strict)`, and the gate
passes `--strict`, so BOTH must reach zero:

- 330 upstream drift records — mostly regenerating the 122 + 121 consumers above
- 580 self-stale — the full qou-zymu backlog, still blocked on the stale
  `pyhecke_native` wheel (qou-nm6y) for any producer touching native code

Worth noting the tool's own comment: self-staleness is designed WARN-only
"because self-staleness is widespread until adoption + regeneration catch up, and
we don't want to red-wall every PR on day one" — and the gate runs it in the mode
that red-walls anyway.
