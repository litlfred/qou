---
# qou-ztee
title: convention-c-value-audit has no way to mark a deliberate comparison — the census floor will look drainable
status: completed
type: task
priority: normal
created_at: 2026-08-29T09:54:51Z
updated_at: 2026-09-06T06:20:51Z
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


## ✅ IMPLEMENTED — and the mechanism is better than this bean asked for (verified 2026-09-06)

Found by `scripts/bean-staleness-triage.py` (4th of 284 artifact beans). The
predicted failure mode — *"the report reads 'N confirmed convention-C bindings,
exit 1' with every entry deliberate, and the obvious next move deletes
measurements"* — **can no longer happen.** A fresh run of
`scripts/convention-c-value-audit.py`:

```
convention-C bindings (confirmed): 134
    of which co-bound with z_D in the same scope: 76  (hint only — not an exemption)
    of which adjudicated in the ledger: 111
    BLOCKING (confirmed, unadjudicated): 23
sqrtvar shape on a q-variable = 1/[2]_q, NOT C: 5
sqrtvar shape, variable unresolved (needs an eye): 1
convention-D bindings: 504
```

Four things now exist that did not when this bean was written:

- **An adjudication ledger** — `docs/audits/convention-c-comparison-ledger.json`
  (105 KB, committed), with 111 sites adjudicated as deliberate comparisons.
  Adjudicated sites stop blocking, so the floor cannot present as drainable.
- **A `[co-bound with z_D]` annotation** on 76 sites, labelled in the output
  *"hint only — not an exemption"* — the distinction surfaced without becoming
  a mechanism.
- **A `NOT C` class** — 5 `sqrtvar` shapes on a q-variable, correctly excluded
  as `1/[2]_q` rather than counted.
- **An `UNRESOLVED` bucket** — 1 site whose variable the audit cannot resolve,
  flagged for an eye instead of being silently classified.

**The design answers this bean's own worry about exemptions**, and does it
better than an exemption list would. From `_load_ledger`'s docstring:

> *"A `# comparison only` comment or a `z_C`-style name would be an exemption
> an author grants themselves, in the file being audited — which is the evasion
> surface this detector exists to close, reintroduced one level up. A ledger
> entry cannot be granted that way: it lives outside the scanned tree, it has
> to be committed as a separate deliberate act, and because the key includes a
> hash of the site's own source line, **editing that line expires the
> adjudication automatically**."*

That last clause is the part worth carrying: an adjudication that expires when
the adjudicated line changes cannot go stale the way a comment-based exemption
would. Same shape as `docs/audits/lean-vacuity-review-ledger.json`.

**Read the count change carefully — it is growth, not drain.** This bean's
baseline was 85 confirmed (at #5972), 87 on its branch; it is **134** now. The
census got *bigger* while the actionable number shrank to **23**, which is what
you would expect from a detector that improved its reach and gained a ledger at
the same time. Do not quote 134 as a regression against 85.

Closing.
