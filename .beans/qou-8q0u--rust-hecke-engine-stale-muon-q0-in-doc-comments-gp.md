---
# qou-8q0u
title: 'Rust hecke-engine: stale muon q0 in doc-comments + gp_cross_validate bin (f64 Q_0 already proton; NO production muon literal)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T21:27:22Z
updated_at: 2026-08-19T21:09:10Z
---

COMPLETED 2026-08-19 (PR pending). Two rounds:

Round 1 (PR #5148, merged): fixed the `hecke gram --q` doc comment, which
claimed the muon default while the code returned `gram::Q_0` (proton).

Round 2 (this branch): the round-1 audit was INCOMPLETE and said so wrongly --
it concluded 'no production muon literal remains' because it grepped only the
full-precision spelling 1.1099785955541805, never the truncated 5-digit
1.10998. A sibling caught this and corrected the gram::Q_0 scope note. Five
live binaries carried the truncated value, 1277 ppb off the anchor (100x
further than the re-pin round 1 was about):
  v14_hapower.rs:309, v6.rs:484, v8.rs:682, h9_beta.rs:376, main.rs:370
All now read hecke_engine::gram::Q_0. v6.rs had asserted 'Single source of
truth: q_parameter.py. This must match' directly above a literal that did not.

Also fixed in the same commit:
- h9_beta.rs:389 printed 'z = 1/(q^1/2+q^-1/2)' (convention C, excised
  2026-08-09) while computing convention D q^3/(q^2+1) -- 23% mislabel.
- pyhecke/gram.py banner said 'STILL DIVERGENT ... Tracked as qou-m7py'
  while _native_ok() in the same file reported it resolved+enabled.

Output re-verified (not blind substitution): all 5 binaries run before/after,
z -> 0.6126880371 = gram::markov_z(Q_0) exactly. Max rel moves 7.1e-6 (hapower)
to 3.7e-3 (qvalues, on an already -99.1% row). 201/201 lib tests pass.

LESSON: grep the truncated spellings, not just the canonical one.
