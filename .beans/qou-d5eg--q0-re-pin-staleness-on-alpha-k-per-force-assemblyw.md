---
# qou-d5eg
title: 'q0 re-pin staleness on alpha-k-per-force-assembly.witness.json: committed witness is MUON-pinned, q_at() now returns PROTON - every delta_q_value_at_q0 digit moves'
status: todo
type: task
priority: normal
created_at: 2026-08-11T00:51:30Z
updated_at: 2026-08-15T22:32:50Z
blocked_by:
    - qou-7vm4
---

2026-08-15 (reorientation pass): this is the SAME underlying question as
qou-7vm4 defect 1, seen from the witness side rather than the code side. The
committed witness is muon-pinned; q_at() returns proton. Whether that is
staleness or correctness depends entirely on which way the manifest call goes.
Do not regenerate this witness independently of that decision -- doing so would
silently pick the proton side of an undecided owner call. Blocked on qou-7vm4.

## 2026-08-22 — RESOLVED (measured, not assumed)
The straddle this bean describes no longer exists; the manifest was re-tagged in the interim and
all three layers now agree on PROTON, verified on main:
  * q0_anchor_manifest.json  -> `physical_proton` (406 members); NOT in `ideal_muon` (3 members)
  * alpha_k_per_force_assembly.py -> imports q_at() == the proton pin
  * committed witness -> q0_anchor "proton", and its q0 matches the 50-digit proton pin to 1.9e-50
    while differing from the muon pin by 1.16e-8 (the mu-p tension) — so the VALUE agrees with the
    label, not merely the tag.

What WAS still broken, and is fixed here: the producer's own documentation had not been updated with
the re-tag, so it asserted the opposite of the truth in two places — a source comment claiming the
manifest says `ideal_muon` with the decision "deliberately NOT decided here", and, worse, a
HARDCODED witness field `q0_manifest_tag: "ideal_muon"` shipped in every witness it emitted. That
false comment is what sent this session chasing an already-resolved defect.

Fix: the tag is now READ from q0_anchor_manifest.json at run time (`_manifest_tag()`), so it cannot
go stale against a future re-tag; a lookup failure returns an explicit "unknown"/"untagged"/
"AMBIGUOUS" string rather than guessing. Comment and caveat rewritten to the measured state.
Witness regenerated: 4/4 assertions pass, ZERO mathematical values moved (only invocation metadata),
and the environment block is a strict SUPERSET of the committed one (numpy/sympy/mpmath/
pyhecke_native all matched after installing them, plus a new pyhecke_native_build fingerprint) — so
this avoids the provenance-degradation trap recorded in bean qou-5380. Blocking precision gates green.

## 2026-08-22 — scope note
This bean's specific claim (committed witness is MUON-pinned) is resolved — measured proton to
1.9e-50. The sibling bean qou-7vm4 stays OPEN for the remaining q_parameter BYPASS, which is latent
rather than active; see its correction note.
