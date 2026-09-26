---
# qou-7p8r
title: 'Rebase #4834 (convention D bar law) onto current main + re-verify Lean, then prepare-merge'
status: completed
type: task
priority: normal
created_at: 2026-08-10T03:34:08Z
updated_at: 2026-08-10T03:45:49Z
parent: qou-531z
---

RESOLVED: do NOT rebase #4834 - it is superseded and merging would REGRESS main. main adopted convention D by owner ruling 2026-08-09 (one day later, stronger): mass=D, binding=D/D, both 'agreed', C EXCISED (registry.md lines 45/114/115). The branch would put binding back to C/C and weaken 'excised' to 'excluded-by-proof'. Attempted merge produced 6 conflicts, all resolving against the branch. #4834 CLOSED as superseded; branch preserved. RESIDUE: MarkovParameterFibreRank.lean is on main at 114 lines/4 decls; branch has 319 lines/16 decls. The 12 extra (incl. zRank_bar_sub, zD_bar_sub, bar_sub_of_bar_even, zC_ne_bar_sub, zC_not_fibre_family) are the one genuinely unlanded contribution - port onto main's version if wanted, NOT by resurrecting the PR.
