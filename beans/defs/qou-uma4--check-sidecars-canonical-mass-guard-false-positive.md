---
# qou-uma4
title: 'check-sidecars canonical-mass guard: false positive on binding_hbarq_rung_forward_test.py'
status: completed
type: bug
priority: normal
created_at: 2026-08-23T01:27:28Z
updated_at: 2026-08-23T07:43:11Z
---

Surfaced by running `scripts/check-sidecars.sh` (the mandatory pre-commit
preflight) on 2026-08-23. **Not a defect in the file — a false positive in the
guard.** Recorded because a false positive in a *mandatory* preflight costs every
agent that runs it a triage cycle, and I spent one.

## The hit

    ⚠ canonical-mass status guard: a DEPRECATED absolute-mass figure is cited as live status.
      computations/binding_hbarq_rung_forward_test.py:30:
        mass: m_p/(m_e·Vol(𝓑₃)) = ρ_p/ℏ_q² ≈ 258  (ρ_p = linking_weight ≈ 2.53, O(1))

Verified **not mine**: byte-identical on `origin/main`, and present in **zero** of
my six branch diffs.

## Why it is a false positive

The line is not a mass *claim*. Read in context it is one half of a deliberately
**normalised** comparison, used to argue a scaling separation:

    mass:     m_p/(m_e·Vol(𝓑₃))  = ρ_p/ℏ_q²  ≈ 258
    binding:  B/(m_e·Vol)        = M_need    ≈ 1 … 7.6

with the conclusion being about the **ℏ_q → 0 limit** — rest mass is classical
(survives ℏ_q → 0), nuclear binding is an O(ℏ_q²) quantum correction (vanishes) —
explicitly flagged in the source as *"a statement about ℏ_q→0 SCALING, not a
magnitude coincidence"*. The same docstring is itself a **correction** to an
earlier over-generalisation ("CORRECTION to Lane 2: 'binding residuals are
ℏ_q²-suppressed' over-generalised") and pre-empts the circularity objection.

So the deprecated `Vol(𝓑₃)·ρ` form appears as a *normalisation for a ratio*, which
is exactly the legitimate use the guard's own message anticipates: *"If a hit is a
legitimate historical/deprecation mention, add it to ALLOWLIST_SUBSTR."*

## The one thing that gives me pause, stated rather than buried

`ρ_p = linking_weight_family_a` **is** the λ_A form AGENTS.md calls a
"CODATA-implied FIT". Using a fitted quantity inside a scaling argument is
defensible — the argument turns on the ℏ_q-order, not on λ_A's value — but whether
the guard *should* allowlist a fitted input is an author call, not mine. That is
why this bean proposes rather than patches.

## Proposed action (NOT taken here)

Add the line to `ALLOWLIST_SUBSTR` in the guard, with a comment naming the reason
(normalisation for an ℏ_q-order comparison, not a mass status claim). Deliberately
not done on this branch: it means editing a guard script for a file on nobody's
active PR, from a PR about Lean class laws.

## Adjacent, already covered — do not re-open

- `qou-rz8m` — the `authors-note` Lean-coverage staleness the same preflight
  reports. Already diagnosed as platform tool-version drift and explicitly *not*
  any branch's doing. I checked before writing anything.
- `qou-xwet`, `qou-3wqg` — `canonical-mass-table-extended` witness defects.
  Different subject; the name overlap is only the words "canonical mass".
