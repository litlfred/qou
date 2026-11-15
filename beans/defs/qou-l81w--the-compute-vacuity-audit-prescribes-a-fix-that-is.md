---
# qou-l81w
title: the compute-vacuity audit prescribes a fix that is itself a tautology
status: completed
type: task
priority: normal
created_at: 2026-08-30T09:26:05Z
updated_at: 2026-08-30T09:45:55Z
---


## What it is

`docs/audits/2026-06-14-compute-vacuity-analogue.md` is the document that
defines the tautological-assertion axis (its class **B2**, "153 found (the
headline)"). At line 65 it prescribes a remedy, and the remedy does not work.

For `khovanov_at_q0_probe.py`'s `c_3_match_at_q1` (`computed=-2, expected=-2`)
it says:

> the genuine `empirical_c3` is computed two lines up (`c_3_empirical`, line
> 213) but **never compared**. The honest form is
> `computed=float(empirical_c3), expected=-2`.

Both halves are wrong.

**1. `empirical_c3` is not computed.** Line 190 of the probe is

    empirical_c3 = mpf(-2)

a literal assignment. Nothing derives it.

**2. The prescribed fix is the same tautology.** `float(mpf(-2))` is `-2.0`,
so `computed=float(empirical_c3), expected=-2` evaluates to `-2.0 == -2` —
`x == x` with a variable in front of one side. An AST census keyed on
expression equality will no longer flag it, which makes it *worse* than the
form it replaces: the defect survives and the detector stops seeing it.

## Why this matters more than one site

This audit is the list agents work from. Anyone draining B2 by following its
prescription will convert visible tautologies into invisible ones, at scale,
and the corpus count will fall while nothing improves. That is close to what
happened here — the site was drained correctly only because the prescription
was checked against the source rather than applied.

## The actual fix for that site

There is a real second route in the same module: the Khovanov tabulation
gives `Hopf+` and `unknot` independently, so

    computed = kh_at_q1['Hopf+']
    expected = kh_at_q1['unknot'] * abs(empirical_c3)

compares two things the module computes separately. Landed already.

## Also worth correcting in the audit

The same B2 list names `m_p_m_e_li2q.py:126` "benign re: vacuity". It is not —
it was `computed=1836.152, expected=1836.152`, a literal against a copy of
itself, and has since been demoted to data. The audit's *secondary* point
about it (the hardcoded CODATA literal should come from `codata_constants`)
stands and is still open.

## Suggested action

Correct line 65's prescription, and add a sentence to B2 saying that a remedy
must introduce an **independent route** to the value — a second derivation, a
known constant, a recurrence — and that wrapping one side in a cast or a
variable is not one.

## RESOLVED 2026-08-30

`docs/audits/2026-06-14-compute-vacuity-analogue.md` corrected in three places:

* the **khovanov B2 entry** — the prescription is marked corrected, with the
  reason spelled out (`empirical_c3` is `mpf(-2)`, a literal, so
  `float(empirical_c3) == -2` is `x == x` with a cast, and invisible to the
  census), and the real remedy named: the module's own two independent
  tabulations, `kh_at_q1['Hopf+']` against
  `kh_at_q1['unknot'] * abs(empirical_c3)`;
* the **`m_p_m_e_li2q` entry** — "benign re: vacuity" withdrawn. Its secondary
  point (the hardcoded CODATA literal should come from `codata_constants`) is
  kept and flagged as still open, with the observation that until it does
  there is nothing for an assertion to compare against;
* a new **"What counts as a fix"** subsection stating the rule the document
  was missing.

## The rule, since it is the durable part

An acceptable `expected` comes from a second derivation, a known constant, an
evaluated property, or a coverage count rebuilt from inputs. Wrapping one side
in `float()` / `str()` / `round()` / a variable is not a remedy — it is the
same defect, minus the detector. Nor is a tolerance: a generous or conditional
tolerance around two identical expressions obscures rather than fixes.

The test: **name the two routes out loud.** If the second cannot be described
without repeating the first, demote to `add_data` with
`has_independent_expected_value: false`. A recorded measurement is not a
failure, and it is what most of this class actually is.

Also documented there, because neither is regex-detectable and both cost a
reader to find: `computed=all(_ok)` where each element was bare-asserted on
append, and an `add_assertion` inside an `if` so non-matching cases leave no
trace at all.

## Why this was urgent rather than tidy

That audit is the list agents drain from. Three sibling agents were dispatched
against it in this session; the corrected text and an explicit "do not follow
line 65" warning went into their briefs. Without it the corpus count falls
while the defect is merely relabelled — the one outcome this axis exists to
prevent.
