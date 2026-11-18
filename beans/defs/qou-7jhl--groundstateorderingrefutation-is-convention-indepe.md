---
# qou-7jhl
title: GroundStateOrderingRefutation is convention-independent; qa-sweep sidecar left stale
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T21:35:46Z
updated_at: 2026-10-04T15:20:38Z
parent: qou-5vkl
---

PR #5724, branch claude/gso-refutation-convention-d-2026-08-24.

OUTCOME: convention-independent. `QOU.MassTheory.GroundStateOrderingRefutation`
was written in convention C (z = sqrt(q)/(q+1)); it never reads z's formula.
z enters the readout only through c_+ = (z + 1/q)/(q + 1/q) and
c_- = (q - z)/(q + 1/q), whose sum is 1 identically in z, and the A=5
comparison collapses to

    gap = 2 c_+ c_- cMix^4 (q^6 - 1)/q^3 ,
    4 c_+ c_- = 4q(q-z)(qz+1)/(q^2+1)^2 ,

so for q > 1 the refutation holds exactly when -1/q < z < q. Both conventions
are in that window for every q > 1. Lean generalised over (q,z); D and C
specialisations added; 30 declarations, #print axioms clean, lean-direct
exit 0, umbrella QOU.lean checks clean.

MEASURED WINDOWS (probe, exact):
  hU holds        C: 1 < q < 1.13700   D: 1 < q < 1.21061
  conclusion holds C: 1 < q < 1.22092   D: 1 < q < 1.57015
hU is sufficient, not necessary. The audit's "1 < q <~ 1.22" is the CONCLUSION
window and is correct -- I nearly "corrected" it to the hU window. Do not.

OPEN (why this bean stays open):
1. `ground-state-ordering.qa.json` is now STALE -- the .md source hash moved
   and qa-sweep could not be run here (folio-assistant clone absent, disk 97%).
   Needs: bun run folio-assistant/content/pipeline/qa-sweep.ts
          folio/quantum-observable-universe/mass-theory/ground-state-ordering
2. The .md edit is NOT machine-render-validated. Grep battery + expository pass
   only, per the documented fallback.
3. check-sidecars flags the Lean file as "MIXED generic + archimedean" (§7c).
   PRE-EXISTING: the file already carried a generic `Field R` Vieta section
   beside the R-valued readout before this branch. The archimedean half is
   genuinely archimedean (abs, ordering, Real.sqrt), so a split would move two
   lemmas into a new module and break nothing but the module identity the
   content block cites. Left as is, deliberately.


--- follow-up, coordinator review of PR #5724 ---

NEAR-MISS, recorded because it is the most reusable thing here. hU is a
SUFFICIENT condition mistaken for a NECESSARY one. hU only converts the gap
identity into an inequality between ABSOLUTE values; the conclusion outlives
it. I was about to "correct" the audit's "1 < q <~ 1.22" to the hU window
1.13700 -- which would have replaced a correct number with a wrong one, in an
audit doc, on the strength of a real measurement of the wrong quantity.

  hU holds          C: 1 < q < 1.13700    D: 1 < q < 1.21061
  conclusion holds  C: 1 < q < 1.22092    D: 1 < q < 1.57015

Both pairs are now in the audit table, the PR body and the probe output, so
nobody has to re-derive which quantity is which.

SELFTEST DEFECT (fixed on this branch). scripts/lean-overlay-env.sh selftest
asserted shadowing behaviour only, never coverage, and stayed green while the
farm held 0 of 2161 QOU oleans. Check (2) cannot catch it structurally: it runs
lean with LEAN_PATH="$OVL:$BASE_LEAN_PATH", so a module missing from the farm
resolves from the real root behind it. Measured on the buggy variant with no
LEAN_EXTRA_ROOTS: (2) prints "ok". Added (3) root completeness and (4) per-root
reachability, both over an independently computed root list -- a check that
iterated roots() is blind to a dropped root, since it never appears there. Also
per-root link counts in init. Verified: fixed 12 ok / 0 FAIL / rc=0; buggy
variant rc=1 naming the QOU root.

LEAN_EXTRA_ROOTS WORDING CORRECTED. I called /tmp/ocn-overlay "actively
harmful" -- true in my worktree, wrong as general guidance. The dropped root is
always the LAST existing one, so which package it costs depends on the tree: in
the main clone all three paper build dirs exist and the casualty was
unital-groebner-bases, leaving both QOU roots intact. In my worktree only the
QOU package .lake was symlinked in, making QOU last. Honest guidance: unset it
unless you know what it contains; after the fix it is only ever additive.

- **Round 96 (`litlfred/qou#8428`)**: Advanced in `feat/round96-milnororder-signrep-mirrorsplit-multibond-moebius-43c1` (Commit 1 `22d991a251c6bf1bcf86f7ea08f935c2c280b7b3`, Commit 2 `391eb320415cc99c2e005cd0ffab67710cb6bc1d`, probe sha256 `94f6f6be6af6f9daa73f3911e2df79962cba2a56eed95434d4d929e3d5348851`).
