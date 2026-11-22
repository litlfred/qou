---
# qou-w3yy
title: 'EPIC: bean tracker hygiene — off-vocabulary statuses, broken parents, and an 83% orphan rate'
status: todo
type: epic
priority: high
created_at: 2026-09-26T10:50:40Z
updated_at: 2026-11-22T21:23:26Z
parent: qou-5vkl
---


## Reorganisation 2026-10-04

Now the epic for P6.HYG under Platform, tooling and hygiene.

## 2026-11-22 — Re-measured (bean-hygiene wave 2)

Session https://claude.ai/code/session_01Qmmkt95ogQs6aFq9zdMmwF. Main `3c4c98fccf3`, beans branch as of this pass. This pass closed 35 beans as completed and 2 as scrapped, each with evidence in its own note.

- `scripts/check-beans.sh`: **16 problems.** 15 are bean files whose frontmatter id contains an underscore and so fails the `# <id>` regex (e.g. `atomic_nf_witness.md`, mostly in the `qou-uot9` tree), plus `skein_mass_from_linking.md`.
- `check-bean-parents.ts`: 2,006 open beans, **42 problems**: 15 orphans, 26 with a `task` parent, 1 feature under a feature. That is down from the 83 % orphan rate this bean was opened on.
- **17 beans carry `status: open`**, outside beans' vocabulary. All are children of `qou-cj0x` / `qou-lg0x`, under the held meta-epics, so they were not touched.
- **One dangling parent:** `qou-s5v5` (completed) names parent `qou-xhci`, which does not exist. Harmless because the child is closed; recorded rather than edited.

Nothing was bulk-edited: renaming ids or re-parenting is a sweep and waits on the owner. **Stays open.**
