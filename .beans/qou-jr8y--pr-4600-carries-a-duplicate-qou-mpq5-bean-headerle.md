---
# qou-jr8y
title: 'PR #4600 carries a duplicate qou-mpq5 bean — headerless mojibake fragment orphaning the R2 scope assessment'
status: todo
type: task
created_at: 2026-08-10T15:19:40Z
updated_at: 2026-08-10T15:19:40Z
---


Found 2026-08-10 while verifying #4600 for landing.

Two files in `.beans/` claim bean ID `qou-mpq5`:

| bytes | filename tail | front-matter | body |
|---|---|---|---|
| 3475 | `…dim-v-�.md` | present, correct | the real bean |
| 593 | `…dim-v-\udcce.md` (mojibake) | **absent** | `## 🔥 Scope assessment (2026-08-02)` |

The 593-byte file is not a duplicate bean — it is the **continuation** of the
real one, split off with a corrupted filename and no header. Its body records a
substantive negative: **Mathlib has no Schur–Weyl duality**, classical or
quantum; a scan finds only `SchurZassenhaus`, `CategoryTheory…Schur` (Schur's
lemma) and `Matrix.SchurComplement`, none of which is the
`GL(V) × S_n ↷ V^{⊗n}` double-centralizer, let alone `U_q(gl_N) × H_n(q)`.

Because the file has no front-matter, no `beans` command surfaces it, so that
finding is invisible to the tracker while looking like it was recorded.

Fix: append the fragment's body to the real `qou-mpq5`, delete the fragment.
Blocked on the owner's call about pushing to #4600's branch.
