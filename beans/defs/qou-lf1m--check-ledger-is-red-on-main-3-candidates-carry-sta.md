---
# qou-lf1m
title: 'check-ledger is red on main: 3 candidates carry stale verdicts (HadronicMass x2, Torsion/TopologicalMass)'
status: completed
type: task
priority: normal
created_at: 2026-08-22T20:34:09Z
updated_at: 2026-08-22T21:17:31Z
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

## DONE 2026-08-22 — gate green

Scope grew 3 -> **9** between filing and working it (more files changed; the
figure matches what #5371 reports independently). All nine adjudicated:
**8 genuine, 1 advisory**. `--check-ledger` now exits 0 — 'all 136 candidates
carry a fresh agent verdict'.

**Eight are one defect**: a class carrying the CONCLUSION as a field, plus a
'Per-instance form' theorem that projects it (`:= hi.bound` / `hi.eq` /
`hi.identity` / `tmd.decomposition`). AGENTS §3b-cond item 5 — the class must
axiomatise HYPOTHESES and the theorem must DERIVE the conclusion.

Two are worse than the shape:
- **`adjoint_vanishing_propagation`** — binder `(k : ℕ)` entirely unused while
  the docstring promises 'vanishing at level 0 implies at all levels' with a
  six-step induction sketch. The conclusion never mentions k, so the
  PROPAGATION — the whole claim — is absent. Same file as
  `adjoint_has_no_degree_zero`, deleted in #5371 for the same reason.
- **The three HadronicMass ones** carry an anti-laundering concern: the assumed
  fields are NUMERICAL PHYSICS claims (a 0.5-MeV proton/neutron agreement; a
  p/n/deuteron mass identity at substrate q), asserted as class axioms and
  re-exported under names that read as proved. And `skein_mass_relation_holds`
  propagates: `skein_mass_relation_proton_neutron` builds a `SkeinMassRelation`
  from the same instance.

**The one advisory**: `identityB_general` is NOT a projection — its body is
real composition (`RegularRepBlockTrace.identityB_conditional` against an
assembled witness). The detector fires only because the docstring mentions
`sorry` while the body has none; the docstring is describing UPSTREAM bricks,
which is accurate. Reword for clarity, no defect.

Verdicts are recorded, the FIXES are not — the eight remain in the genuine
queue as part of the self-assuming-projection bulk.
