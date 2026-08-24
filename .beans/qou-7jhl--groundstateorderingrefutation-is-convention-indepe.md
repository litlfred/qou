---
# qou-7jhl
title: GroundStateOrderingRefutation is convention-independent; qa-sweep sidecar left stale
status: todo
type: task
priority: normal
created_at: 2026-08-24T21:35:46Z
updated_at: 2026-08-24T21:36:05Z
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
          content/quantum-observable-universe/mass-theory/ground-state-ordering
2. The .md edit is NOT machine-render-validated. Grep battery + expository pass
   only, per the documented fallback.
3. check-sidecars flags the Lean file as "MIXED generic + archimedean" (§7c).
   PRE-EXISTING: the file already carried a generic `Field R` Vieta section
   beside the R-valued readout before this branch. The archimedean half is
   genuinely archimedean (abs, ordering, Real.sqrt), so a split would move two
   lemmas into a new module and break nothing but the module identity the
   content block cites. Left as is, deliberately.
