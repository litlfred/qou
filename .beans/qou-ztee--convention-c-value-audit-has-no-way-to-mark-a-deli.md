---
# qou-ztee
title: convention-c-value-audit has no way to mark a deliberate comparison — the census floor will look drainable
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T09:54:51Z
updated_at: 2026-08-29T16:27:27Z
---

Observed 2026-08-29 on branch claude/tower-gap-lean-and-infra-2026-08-29 (PR
#5978), immediately after #5972 landed scripts/convention-c-value-audit.py on
main (8126d7c37f).

NOT A DEFECT IN THE TOOL'S DESIGN. Its design principle is explicit and correct:
"tests the ANSWER, not the source", "cannot be evaded by re-spelling, because it
does not read the spelling". docs/audits/2026-08-15-detector-blindness-taxonomy.md
catalogues thirteen blind spellings, four found BY detectors written to catch the
previous blind spot, and this one breaks that race by construction. Reading names
or comments would reintroduce exactly the evasion surface it was built to close.

THE GAP IS DOWNSTREAM OF THAT, AND IT IS A REPORTING ONE. Because it reads
neither names nor comments, it cannot distinguish

  (a) a producer computing a quantity at the wrong convention   -- a defect
  (b) a probe binding z_C ALONGSIDE z_D in order to compare them -- the subject

and it has no exemption mechanism, by design. So as the C surface drains, the
census converges to a FLOOR consisting entirely of (b). At that point the report
reads "N confirmed convention-C bindings, exit 1" with every entry deliberate,
and the obvious next move -- "drain the last N" -- deletes measurements.

CURRENT NUMBERS. The audit's own baseline at #5972 was 85 confirmed C bindings
in computations/, 0 in tools/ and content/. Measured on this branch's merged
tree: 87. The +2 are

  computations/probes/tower_vhat_markov_parameter_probe.py:77
  computations/probes/tower_z_convention_pole_sensitivity_probe.py:61

both `Z_C = mp.sqrt(Q)/(Q+1)`, both bound BESIDE z_D and h/2 because the probes'
whole subject is where each convention sits relative to the Phi_q pole. Binding
only z_D would delete the measurement. (A third probe on the branch,
tower_vhat_chain_length_pole_margin_probe.py, binds no z_C and is correctly not
listed.) At least two pre-existing entries are the same shape, e.g.

  computations/h2s_chiral_residue_bar_antisymmetric.py:95
      z_c = mp.sqrt(q)/(q+1)   # convention C, for the comparison only
  computations/deuteron_two_body_kernel_overshoot_probe.py:209

so the floor already exists and is not created by this branch.

NOT DONE HERE, DELIBERATELY. The obvious fix -- have comparison sites import a
single shared z_C rather than each re-deriving it -- would cut the census to one
counted site and is arguably better engineering (one source of truth for the
comparison constant). It is NOT done on this branch for two reasons: it is scope
creep on another session's tool, and a change whose visible effect is to reduce
this branch's own contribution to a census is the wrong thing for this branch to
be making. It belongs to whoever owns the audit.

WHAT NOT TO DO. Do not restructure a comparison probe so the detector stops
seeing it. That is AGENTS.md 1a audit-dodging -- a move whose only effect is to
make an audit pass without changing anything real -- and it is precisely what
this detector was built to defeat. If the count is wrong, fix the REPORT.

SUGGESTED SHAPES, for whoever picks this up:
  * report two totals -- "N confirmed, of which M co-bound with z_D at the same
    site" -- since co-binding with D is itself a value-level signal and needs no
    name or comment;
  * or carry a committed ledger of adjudicated comparison sites, the way
    docs/audits/lean-vacuity-review-ledger.json holds agent verdicts that a
    machine cannot reach, keyed on file + line + a hash so a verdict goes stale
    when the site changes.
