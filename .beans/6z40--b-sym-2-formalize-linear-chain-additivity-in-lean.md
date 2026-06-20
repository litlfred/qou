---
# 6z40
title: 'B_sym #2: formalize linear-chain additivity in Lean (B_sym not a theorem as stated; needs Lean env)'
status: todo
type: task
priority: normal
created_at: 2026-06-20T00:58:14Z
updated_at: 2026-06-20T00:58:54Z
parent: qfzy
---

B_sym = a*ln(tr_free/tr_atom) is a DEFINITION + empirical claim, NOT a theorem. Only Lean is trivial subst;rfl. Provable structural alt: the #2343 linear-chain additivity B_sym = a*[(Z-1)L_pp + L_pn + (N-1)L_nn]. BLOCKED: Lean toolchain un-installable (release.lean-lang.org firewalled, SessionStart elan error).
