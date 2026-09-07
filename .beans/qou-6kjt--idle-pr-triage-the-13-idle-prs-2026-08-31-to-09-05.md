---
# qou-6kjt
title: 'IDLE-PR TRIAGE: the 13 idle PRs (2026-08-31 to 09-05) the shallow clone could not merge-test — deepen, measure cleanliness, classify merge-ready vs needs-work'
status: todo
type: task
created_at: 2026-09-07T18:16:49Z
updated_at: 2026-09-07T18:16:49Z
parent: qou-6g7j
---

19 open PRs are idle > 3 h. Four were measured CLEAN (bean above), #7005 and #7093 are being extended. The remaining 13 had NO merge base in the shallow agent clone (git merge-tree could not run): #6359 #6878 #6758 #6807 #6853 #6816 #6804 #6818 #6681 #6744 #6342 #6361 #6353. Task: deepen the fetch (git fetch --deepen or --unshallow on origin/main + each head), run merge-tree, read each PR body's own verification claims, and classify: (i) clean + self-verified → merge-ready list for the owner, (ii) conflicts → name the files, (iii) red/unverified → what is missing. Do not merge; report as a numbered list the owner can pick from.
