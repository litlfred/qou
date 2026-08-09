---
# qou-kljb
title: 785 of 1659 QOU library modules are unreachable from QOU.lean — build coverage unknown
status: todo
type: task
priority: medium
created_at: 2026-08-09T02:12:05Z
updated_at: 2026-08-09T02:12:05Z
---

Surfaced while verifying PR #4824's §1 consolidation claim using the
three-way per-file drop check sibling #4840 proposed. PR #3793 had recorded,
in a comment on `TorusKnotMass.lean`, that a fabricated
`noncomputable instance : TorusKnotMass := ⟨0, rfl⟩` did not typecheck, and
that the resulting non-compiling file "escaped CI only because it is
orphaned from the `QOU` umbrella". That comment was dropped when the
instance-removal reached main by a different route.

**Half of that claim checks out; the other half does not. Read both before
acting.**

## Verified

1. **The typecheck claim is sound.** At #3793's base (`b759f24f`) the class
   had **9 explicit fields** and `factors_distinct : gauge_mass_factor ≠
   scalar_mass_factor`. `⟨0, rfl⟩` supplies 2 of 9, and `gauge_mass_factor = 0`
   forces `factors_distinct : (0:ℝ) ≠ 0`, unprovable. So it could not have
   elaborated.

2. **The orphan count is real.** Import-closure walk from
   `content/quantum-observable-universe/lean/QOU.lean`:

   | | count |
   |---|---|
   | library modules under `lean/QOU/` | 1659 |
   | reachable from `QOU.lean` | 874 |
   | **not reachable** | **785 (47%)** |

   `QOU.BraidKnot.TorusKnotMass` is one of the 785. The lakefile declares
   `[[lean_lib]] name = "QOU"` with **no `globs` key**.

## NOT established — the inference that orphan ⇒ unbuilt is refuted

The obvious conclusion ("Lake's default glob is the root module, so these
785 are never built, so nothing checks them") is **contradicted by the
evidence**. Against the restored `lake-cache/qou-v4-24-0` build tree:

| set | modules | with `.olean` |
|---|---|---|
| reachable | 874 | 502 (57%) |
| **orphaned** | **785** | **440 (56%)** |

Orphan status does **not** predict whether a module has a build artifact —
the two rates are the same. `TorusKnotMass.olean` is present. So "nothing
builds them" is not true as stated, and #3793's "escaped CI because
orphaned" is an *unverified* explanation, not a finding. It has been left
out of the repaired file comment for that reason.

## The actual open question

Why do orphaned modules have oleans at the same rate as reachable ones?
Candidates, none yet tested:

- **Stale artifacts** — built back when something did import them, and never
  cleaned. Most likely, and would mean current coverage really is poor.
- **A build path other than `lake build QOU`** — a CI job or seeding script
  that enumerates modules directly.
- **Lake glob behaviour differing from the assumed `#[.one "QOU"]` default.**

The uniform ~56% in *both* sets also suggests the cache tarball is simply a
partial snapshot, which would make the whole comparison weaker evidence than
it looks. Do not draw conclusions from these percentages alone.

## Next step — one cheap experiment settles it

From a clean build dir, run `lake build QOU` and check whether an orphan's
olean is produced:

```bash
rm -rf content/quantum-observable-universe/lean/.lake/build/lib/lean/QOU/BraidKnot/TorusKnotMass.olean
lake build QOU
ls content/quantum-observable-universe/lean/.lake/build/lib/lean/QOU/BraidKnot/TorusKnotMass.olean
```

Present ⇒ orphans are built, no coverage gap, close this bean. Absent ⇒ the
coverage gap is real and the 785 need triage (wire up, or delete the dead
ones), which is a scoped tranche and **not** an idle-drain: turning on 785
unbuilt modules at once could be very red.

Related standing gaps in AGENTS.md: a library `.lean` with no `.ts`/`.md`
sibling has no `.qa.json` sidecar and is not covered by
`lean-content-siblings.yml`; CI auto-triggers are disabled repo-wide
(`build.yml` is `workflow_dispatch`-only).
