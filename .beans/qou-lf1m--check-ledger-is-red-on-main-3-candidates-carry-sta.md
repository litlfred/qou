---
# qou-lf1m
title: 'check-ledger is red on main: 3 candidates carry stale verdicts (HadronicMass x2, Torsion/TopologicalMass)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T20:34:09Z
updated_at: 2026-08-22T20:34:46Z
---

Found while verifying qou-v4ht did not regress the gate. **Pre-existing on main, not caused by that change** — confirmed by stashing the patch and re-running: baseline `--check-ledger` also exits 1.

Three candidates carry no *fresh* agent verdict (the ledger keys a verdict to the file's sha, so a sibling edit to the file staleness-invalidates it):

- `lean/QOU/HadronicMass.lean:470` — `neutron_pair_skein_approx` [self-assuming-projection/field-projection]
- `lean/QOU/HadronicMass.lean:611` — `skein_mass_relation_holds` [same]
- `lean/QOU/Torsion/TopologicalMass.lean:89` — `topological_mass_decomposition` [same]

**Why it matters:** `--check-ledger` is the agent-inspection gate in
`.github/workflows/lean-content-siblings.yml`. It is diff-scoped there, so a
red whole-corpus result does NOT block unrelated PRs — but any PR that touches
those two files will fail its gate until the three are adjudicated.

**Work:** read the three declarations and record `genuine` / `legit` /
`advisory` with evidence, per the agent-inspection ledger discipline. Small —
three decls, two files.
