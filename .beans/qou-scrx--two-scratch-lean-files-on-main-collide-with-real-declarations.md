---
# qou-scrx
title: 'Two scratch_*.lean files on main duplicate real declarations — 6 collisions, 0 importers'
status: todo
type: task
priority: medium
created_at: 2026-08-30T08:00:00Z
updated_at: 2026-08-30T08:00:00Z
---

Found while running the `/prepare-merge` §4a duplicate-declaration gate on the
q-RH branch. **Not that branch's regression** — measured on `origin/main`
itself, and recorded here rather than fixed there because it is a different
domain.

## What

Two files in the **library** tree are scratch debris:

- `content/quantum-observable-universe/lean/QOU/scratch_pmass.lean` (20 lines)
- `content/quantum-observable-universe/lean/QOU/scratch_skein.lean` (29 lines)

Both were added in the **same** commit, `b4a0dc7138` (2026-08-29,
*"fix(coulomb-charge): Q is the STRONG coefficient"*), which is not about
either subject — the shape of a scratch file left behind rather than authored.

## Why it matters

Lean's environment is flat, so two modules declaring the same fully-qualified
name **cannot both be imported by anything**. These duplicate three real
declarations, six collisions in total:

| FQN | real home | scratch copy |
|---|---|---|
| `QOU.Substrate.ProtonMassSubstrateIdentity.proton_mass_substrate_match` | `QOU/Substrate/ProtonMassSubstrateIdentity.lean:41` | `scratch_pmass.lean:15` |
| `QOU.Torsion.SkeinGenerationContext` | `QOU/Torsion/skein_generation.lean:32` | `scratch_skein.lean:13` |
| `QOU.Torsion.skein_generation` | `QOU/Torsion/skein_generation.lean:48` | `scratch_skein.lean:21` |

`scratch_pmass.lean` also carries an `opaque F_Bor (q : ℝ) : ℝ` and a hardcoded
`m_e_codata : ℝ := 0.51099895069` — an opaque stand-in for a derived quantity
plus a bare CODATA literal, both of which the corpus's own disciplines are
against.

## Measured, so the disposition is cheap

- **Importers: 0.** Nothing in `content/` references either module by name
  outside the files themselves.
- **The gate is red on `main`, not on the branch that found it.** Run against
  `origin/main` and against the q-RH branch, `check-duplicate-decls --package
  qou` reports **63** duplicated FQNs on **both** — the branch adds zero. The
  skill's `--baseline 57` is therefore stale relative to main by 6, and all 6
  are these.

## Disposition

Delete both files. They have no importers, they are not cited by any content
block, and their declarations already exist in their proper modules. Then lower
`--baseline` from 57 toward 57 − 6 = 51 in
`.claude/skills/local/prepare-merge-auto.md` §4a, per the ratchet rule.

**Do not simply raise the baseline to 63** — that banks the collisions as
permanent and is the loosening the ratchet exists to prevent.

**Verify before deleting**, cheaply: write a two-line module importing both
`QOU.Torsion.skein_generation` and `QOU.scratch_skein` and confirm it fails with
`environment already contains`. The skill notes that two earlier counts of this
population were wrong while the compile never was.
