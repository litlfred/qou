---
# qou-8b0q
title: Demote defect-legendrian + topological-charge blocks to conjecture (post-q407)
status: completed
type: task
priority: normal
tags:
    - needs-owner
    - 8f-lean
    - reorg-2026-10-04
created_at: 2026-08-21T15:10:31Z
updated_at: 2026-10-10T07:50:19Z
parent: qou-8lxd
---

q407 converted the vacuous 'theorem (h:P):P:=h' Lean siblings of these two blocks to honest 'def : Prop' (Pattern C), clearing the self-assuming-projection flag. But the .ts block kinds are still 'proposition' (defect-legendrian-knot) and 'theorem' (topological-charge-quantization), while their claims are NOT Lean-provable at this abstraction (the docstrings admit this — the geometric content needs the q-torsion leaf / Reeb-derivation substrate). A proposition/theorem block whose Lean only NAMES the claim will read as a proof-statement-integrity gap on the next qa-sweep.

Recommended: demote both blocks to 'conjecture' (kind conjecture, label conj:… , or §3b-cond conditional class if the geometric setup can be packaged as hypotheses and the claim derived). Only external label refs are in the auto-generated definition-index.md. Requires folio-assistant set up (setup-folio-assistant.sh) to run validate + qa-sweep + rebuild the index. Also refresh the 4 q407 content-block sidecars (left stale for theorem→def) once qa-sweep can run.

Blocks: content/quantum-observable-universe/brings-surface/defect-legendrian-knot.{ts,md,lean}; content/quantum-observable-universe/brings-surface/topological-charge-quantization.{ts,md,lean}. Parent: qou-q407.


## ENACTED and COMPLETED 2026-10-10 — the recommended demotion, with one correction

Both blocks demoted to `conjecture`, per this bean's own recommendation:

| block | was | now |
|---|---|---|
| `defect-legendrian-knot` | `proposition` / `prop:` | `conjecture` / `conj:` |
| `topological-charge-quantization` | `theorem` / `thm:` | `conjecture` / `conj:` |

The manifests corroborated the diagnosis before the edit: both already carried
`validation: "stub"` on their `lean.ref`, and each Lean sibling is a single
`def` that NAMES the claim. An `authorNote` on each block records the demotion,
its reason (§3b-cond item 5), and the measured blast radius.

## CORRECTION to this bean: the blast-radius claim was understated by one

This bean said *"Only external label refs are in the auto-generated
definition-index.md."* Measured before relabelling:

| label | `uses[]` edges | prose anchors `](#...)` |
|---|---|---|
| `prop:defect-legendrian-knot` | **0** | **1** — the generated index |
| `thm:topological-charge-quantization` | **0** | **2** — the generated index **and `prop:phase-transition-boundary`** |

That second anchor is a **live** reference, inside `phase-transition-boundary`'s
`authorNotes` status body, where the withdrawn-Ext note says the topological
integer "has two routes — the residue of
[`thm:topological-charge-quantization`](...)". **It would have broken silently:**
AGENTS.md records that `run-validate` does not check `](#anchor)` targets.
Retargeted in the same commit.

Also updated, none of which the bean listed: each `.lean` docstring's
`LaTeX label:` line, and `QOU/Mathlib/ExtensionClass.lean:13`, which cites the
theorem by label in its module docstring.

**The 0 `uses[]` figure is what made this safe** — §3b conjectural propagation
keys on `uses[]`, so no downstream provable block needed demoting with them.
Validate confirms: 8 issues before, **8 after**, no propagation violation.

## Verification

- `run-validate folio/quantum-observable-universe`: **✓ Valid, 8 issue(s)** —
  identical count and content to before the change.
- `qa-sweep` on both demoted blocks: **0 critical, 0 major, 0 minor**.
- `definition-index.md` regenerated via the platform generator (note: it takes a
  path *relative to the folio root*, `quantum-observable-universe`, not
  `folio/quantum-observable-universe` — the latter double-prefixes and errors).
- Old labels: **0** occurrences left anywhere in `folio/` outside derived
  `.qa.json` / `.jsonld`.

## Two side findings, both filed rather than fixed here

1. **The committed definition index was stale by 10 entries** — regeneration took
   it 1287 -> 1297. Relabelling two blocks cannot add ten, so the index had
   drifted before this change. Now current.
2. **The in-tree `.qa.json` sidecars appear orphaned at this platform pin** —
   qa-sweep wrote only to `test/results/` and `test/attestations/`, leaving both
   sidecars recording the OLD labels with stale `source_hashes`. Recorded on
   `qou-99fk` with the scope of what was actually measured. Not hand-patched:
   they are derived files, and faking one field would not make them current.

The bean's "refresh the 4 `qou-q407` content-block sidecars once qa-sweep can
run" item is **superseded by finding 2** — qa-sweep no longer writes them.
